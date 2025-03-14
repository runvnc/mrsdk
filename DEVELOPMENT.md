# Development Guide

## Setup Development Environment

1. Clone the repository

```bash
git clone https://github.com/mindroot/mindroot-python-sdk.git
cd mindroot-python-sdk
```

2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install in development mode

```bash
pip install -e .
pip install -e ".[dev]"
```

## Running Tests

Tests are written using pytest. To run the tests:

```bash
python -m pytest
```

Or run with coverage:

```bash
python -m pytest --cov=mrsdk
```

## Code Style

This project uses [Black](https://github.com/psf/black) for code formatting and [isort](https://pycqa.github.io/isort/) for import sorting.

To format your code:

```bash
black mrsdk tests examples
isort mrsdk tests examples
```

## Adding Features

1. Create a new branch for your feature

```bash
git checkout -b feature/your-feature-name
```

2. Implement your changes

3. Add tests for your changes

4. Update documentation as needed

5. Run the tests to ensure everything works

```bash
python -m pytest
```

6. Submit a pull request

## Release Process

1. Update version in `mrsdk/__init__.py` and `pyproject.toml`

2. Update the CHANGELOG.md

3. Create and push a new tag

```bash
git tag v0.1.0
git push origin v0.1.0
```

4. Build and upload to PyPI

```bash
python -m build
python -m twine upload dist/*
```

## Project Structure

```
mrsdk/
├── mrsdk/              # Main package
│   ├── __init__.py     # Package initialization
│   ├── client.py       # MindRoot API client
│   ├── exceptions.py   # Custom exceptions
│   └── cli.py          # Command-line interface
├── examples/           # Example scripts
│   ├── basic_usage.py
│   └── advanced_usage.py
├── tests/              # Test suite
│   ├── __init__.py
│   └── test_client.py
├── LICENSE            # MIT License
├── README.md          # Documentation
├── DEVELOPMENT.md     # Development guide
├── pyproject.toml     # Build configuration
└── setup.py           # Installation script
```
