# Contributing to BitKey Electrum Server Checker

First off, thank you for considering contributing to BitKey Electrum Server Checker! It's people like you that make this tool better for everyone.

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* Use a clear and descriptive title
* Describe the exact steps which reproduce the problem
* Provide specific examples to demonstrate the steps
* Describe the behavior you observed after following the steps
* Explain which behavior you expected to see instead and why
* Include any error messages or output

### Suggesting Enhancements

Enhancement suggestions are tracked as issues. When creating an enhancement suggestion, please include:

* Use a clear and descriptive title
* Provide a step-by-step description of the suggested enhancement
* Provide specific examples to demonstrate the steps
* Describe the current behavior and explain which behavior you expected to see instead
* Explain why this enhancement would be useful

### Pull Requests

* Fill in the required template
* Do not include issue numbers in the PR title
* Follow the Python styleguide (PEP 8)
* Include appropriate test coverage
* Document new code based on the Documentation Styleguide
* End all files with a newline

## Development Process

1. Fork the repo
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run the tests
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Setting up Development Environment

```bash
# Clone your fork
git clone <repository-url>
cd electrum-server-checker

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Code Style

This project uses:
* Black for code formatting
* isort for import sorting
* flake8 for style guide enforcement

To check your code:
```bash
black .
isort .
flake8
```

## Documentation Styleguide

* Use [Google style](https://google.github.io/styleguide/pyguide.html) for docstrings
* Keep docstrings clear and concise
* Document all public methods and classes

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the tags on this repository.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.