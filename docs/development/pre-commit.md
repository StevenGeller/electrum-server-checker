# BitKey Electrum Server Checker

A tool to help BitKey users verify and configure their Electrum server connections.

## Pre-commit hooks

This project uses pre-commit hooks to maintain code quality. To set up:

```bash
# Install pre-commit
pip install pre-commit

# Install the pre-commit hooks
pre-commit install

# (Optional) Run against all files
pre-commit run --all-files
```

The following hooks are configured:

1. **pre-commit-hooks**
   - trailing-whitespace
   - end-of-file-fixer
   - check-yaml
   - check-added-large-files
   - check-toml
   - check-merge-conflict
   - detect-private-key
   - mixed-line-ending

2. **black**
   - Code formatting

3. **isort**
   - Import sorting
   - Configured to be compatible with black

4. **flake8**
   - Style guide enforcement
   - Additional plugins:
     - flake8-bugbear
     - flake8-comprehensions
     - flake8-docstrings
     - flake8-simplify

5. **mypy**
   - Static type checking
   - Additional type stubs:
     - types-requests
     - types-urllib3

## Configuration

The hooks are configured in `.pre-commit-config.yaml`. Settings for individual tools are in `pyproject.toml`.