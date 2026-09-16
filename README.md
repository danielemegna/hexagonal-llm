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

Install project dependencies (dev deps included)
```
$ uv sync --extra dev
```

Then run tests
```
$ uv run pytest
```

