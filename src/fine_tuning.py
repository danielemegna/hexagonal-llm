import json
import random
import subprocess
import sys
import time
from pathlib import Path

import yaml

from aimotorcycle.prompts.grab_motorcycle_specs import GrabMotorcycleSpecs


def fine_tuning() -> None:
    base_model = Path.home() / ".omlx/models/mlx-community/Qwen2.5-3B-Instruct-4bit"
    trained_model = Path("trained/Qwen2.5-3B-Instruct-4bit-motorcycle")
    training_file = Path("material/motorcyles/train.jsonl")
    work_dir = Path("trained/lora-work") / trained_model.name
    data_dir = work_dir / "data"
    adapter_dir = work_dir / "adapters"
    max_lines: int | None = 1000  # e.g. 1000 to train on the first lines of train.jsonl only, None for all of them
    started_at = time.monotonic()

    print("============= LoRA fine-tuning =============\n")
    print(f"Base model: {base_model}")
    print(f"Trained model: {trained_model}")
    print(f"Work dir (data, adapters, config): {work_dir}")

    print(f"\n[1/3] Preparing training data from {training_file}...")
    lines = training_file.read_text().splitlines()
    if max_lines is not None:
        print(f"Using only the first {max_lines} of {len(lines)} lines (max_lines)")
        lines = lines[:max_lines]
    print(f"Injecting the prompt into {len(lines)} examples...")
    examples = [with_prompt(json.loads(line)) for line in lines]
    random.Random(0).shuffle(examples)
    valid_size = len(examples) // 10
    write_jsonl(data_dir / "valid.jsonl", examples[:valid_size])
    write_jsonl(data_dir / "train.jsonl", examples[valid_size:])
    print(f"Written {len(examples) - valid_size} train examples and {valid_size} valid examples in {data_dir}")
    print(f"Done in {elapsed_since(started_at)}")

    batch_size = 4
    iters = (len(examples) - valid_size) // batch_size  # one epoch
    lora_config = work_dir / "lora_config.yaml"
    lora_config.write_text(yaml.safe_dump({
        "model": str(base_model),
        "train": True,
        "data": str(data_dir),
        "adapter_path": str(adapter_dir),
        "fine_tune_type": "lora",
        "mask_prompt": True,  # loss on the assistant answer only, not on the prompt
        "num_layers": 16,
        "lora_parameters": {"rank": 8, "scale": 20.0, "dropout": 0.0},
        "batch_size": batch_size,
        "iters": iters,
        "learning_rate": 1e-4,
        "max_seq_length": 2048,
        "steps_per_report": 50,
        "steps_per_eval": 200,
        "val_batches": 25,
        "save_every": 200,
        "seed": 0,
    }, sort_keys=False))
    print(f"\n[2/3] LoRA fine-tuning: {iters} iterations of {batch_size} examples (one epoch)...")
    print(f"Config written in {lora_config}")
    print("mlx_lm reports the train loss every 50 iterations and the val loss every 200")
    step_started_at = time.monotonic()
    run_mlx_lm("lora", "--config", str(lora_config))
    print(f"Adapters saved in {adapter_dir}, done in {elapsed_since(step_started_at)}")

    print("\n[3/3] Fusing adapters into the base model...")
    step_started_at = time.monotonic()
    run_mlx_lm("fuse", "--model", str(base_model), "--adapter-path", str(adapter_dir), "--save-path", str(trained_model))
    print(f"Fused model saved in {trained_model}, done in {elapsed_since(step_started_at)}")

    print(f"\n================= Fine-tuning done in {elapsed_since(started_at)} ==================")


def elapsed_since(started_at: float) -> str:
    minutes, seconds = divmod(int(time.monotonic() - started_at), 60)
    return f"{minutes}m {seconds}s"

def with_prompt(row: dict) -> dict:
    # training file user messages hold the bare input: wrap it in the prompt used at inference time
    user, assistant = row["messages"]
    return {"messages": [
        {"role": "user", "content": str(GrabMotorcycleSpecs(user["content"]))},
        assistant,
    ]}

def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

def run_mlx_lm(command: str, *args: str) -> None:
    result = subprocess.run([sys.executable, "-m", "mlx_lm", command, *args])
    if result.returncode:
        raise SystemExit(f"mlx_lm {command} failed with exit code {result.returncode}")
