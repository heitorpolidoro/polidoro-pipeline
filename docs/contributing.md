# Contributing

Thank you for your interest in contributing to Polidoro Pipeline! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

Please be respectful and considerate of others when contributing to this project. We aim to foster an inclusive and welcoming community.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Git

### Setting Up Development Environment

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/polidoro_pipeline.git
   cd polidoro_pipeline
   ```
3. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install development dependencies:
   ```bash
   pip install -e ".[dev,test]"
   # or
   pip install -r requirements.dev.txt
   pip install -r requirements.test.txt
   ```

## Development Workflow

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and ensure they follow the project's coding style

3. Add tests for your changes

4. Run the tests to ensure everything works:
   ```bash
   pytest
   ```

5. Commit your changes with a descriptive commit message:
   ```bash
   git commit -m "Add feature: your feature description"
   ```

6. Push your branch to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

7. Create a Pull Request from your fork to the main repository

## Pull Request Guidelines

- Fill in the pull request template with all required information
- Ensure your code passes all tests
- Include tests for new features or bug fixes
- Update documentation if necessary
- Keep pull requests focused on a single topic
- Be responsive to feedback and be willing to make changes if requested

## Testing

We use pytest for testing. To run the tests:

```bash
pytest
```

To run tests with coverage:

```bash
pytest --cov=ppipeline
```

## Code Style

We follow PEP 8 style guidelines for Python code. Please ensure your code adheres to these standards.

You can use tools like flake8, black, and isort to help maintain code style:

```bash
# Check code style
flake8 ppipeline tests

# Format code
black ppipeline tests
isort ppipeline tests
```

## Documentation

When adding new features or making changes, please update the documentation accordingly. We use Sphinx for generating documentation.

To build the documentation locally:

```bash
cd docs
make html
```

Then open `_build/html/index.html` in your browser to view the documentation.

## Releasing

The project maintainers will handle releases. If you believe a new release is needed, please open an issue to discuss it.

## Questions?

If you have any questions or need help with contributing, please open an issue on GitHub or reach out to the maintainers.

Thank you for contributing to Polidoro Pipeline!
