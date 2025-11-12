# Sample Python package
Small Python package for demonstrating [continuous](https://github.com/edvardlindelof/notebooks-vs-src/actions) packaging, testing and publication.

## Run tests
`uv run --with jupyter jupyter lab`

## Understanding the continuous testing and publication
Study [.github/workflows/test.yaml] and [.github/workflows/publish.yaml] to understand the CICD. The index utilized by the present project is private. One way to adapt this to your own environment is to fork the repo, set up your own index (e.g. an Azure Artifact Feed), change pyproject.toml to point to the corresponding url and add `UV_INDEX_PRIVATE_REGISTRY_{REGISTRY,PASSWORD}` to the repo secrets.

## Install dependencies
This is handled automatically by `uv`, but here is how to do it explicitly for understanding or debugging.
```bash
uv lock  # figure out a set of dependency versions solving all constraints in pyproject.toml
uv sync  # pip install and/or remove packages to assure python .venv conforms to uv.lock
```
