# Notebooks
Small notebooks meant to illustrate how to move code from a notebook into a production Python package.

## Run Jupyter
`uv run --with jupyter jupyter lab`

## Install dependencies (including local `processing` package)
This is handled automatically by `uv`, but here is how to do it explicitly for understanding or debugging.
```bash
uv lock  # figure out a set of dependency versions solving all constraints in pyproject.toml
uv sync  # pip install and/or remove packages to assure python .venv conforms to uv.lock
```
