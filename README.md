# LLM as Hexagonal Architecture Port

Let's use some LLMs as Hexagonal Architecture ports

## Setup

A local running OpenAI API compatibile LLM engine is needed on `localhost:8000` to run the main or the tests (see `src/common/http_llm_client.py`).

Install uv (if not installed)

```
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

Install project dependencies
```
$ uv sync
```

Run the main as demo
```
$ uv run main
```

## Run tests

Dev dependencies (pytest) are installed by `uv sync`, then run tests
```
$ uv run pytest
```

## Fine-tuning

Train a LoRA adapter with `mlx-lm` and fuse it into a base model installed in oMLX (Apple Silicon only).

1. Configure the first lines of `fine_tuning()` in `src/fine_tuning.py`:
   - `base_model_name`: the base model, relative to `~/.omlx/models` (e.g. `mlx-community/Qwen2.5-3B-Instruct-4bit`)
   - `training_file`: the training jsonl file
   - `prompt_to_use`: the `Prompt` implementation class that wraps every training input (the same one used at inference time)
   - `trained_model_name`: the name of the trained model
   - `max_lines` (optional): train on the first lines of the training file only, `None` to use all of them

2. Put the training jsonl file in the `material` folder (e.g. `material/motorcyles/train.jsonl`). Every line is a user-assistant chat where the user message holds only the bare input, without the prompt: the `prompt_to_use` class wraps it during the fine-tuning. The assistant message is the expected answer.
   ```
   {"messages": [{"role": "user", "content": "<bare input>"}, {"role": "assistant", "content": "<expected answer>"}]}
   ```
   10% of the lines are held out as validation set.

3. Stop oMLX to free memory and start the fine-tuning from the project root:
   ```
   $ omlx stop
   $ uv run finetuning
   ```
   The fused model is saved in `trained/<trained_model_name>`.

4. Make the trained model visible to oMLX:
   ```
   $ mkdir -p ~/.omlx/models/local-trained
   $ ln -s $PWD/trained/<trained_model_name> ~/.omlx/models/local-trained/<trained_model_name>
   ```

5. Start oMLX and try the trained model using its name, e.g. `AIMotorcycleAdvertisementAnalyzer("Qwen2.5-3B-Instruct-4bit-motorcycle")`:
   ```
   $ omlx start
   ```
