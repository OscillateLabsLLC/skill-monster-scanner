# Contributing to skill-monster-scanner

Thanks for your interest in contributing!

## Development Setup

### Prerequisites

- Python 3.9+
- pip

### Getting Started

```bash
git clone https://github.com/OscillateLabsLLC/skill-monster-scanner
cd skill-monster-scanner

# Install dependencies (including test extras)
pip install -e ".[test]"
```

## Common Commands

```bash
# Run tests
pytest

# Run a specific test file
pytest test/test_skill.py
```

## Pull Requests

1. Create a feature branch: `git checkout -b feat/my-feature`
2. Make your changes and add tests where applicable
3. Run `pytest` to ensure everything passes
4. Commit using [Conventional Commits](https://www.conventionalcommits.org/) (e.g., `feat:`, `fix:`, `docs:`)
5. Open a pull request

**PR Guidelines:**
- Keep PRs focused on a single concern
- Include tests for new functionality
- Ensure all CI checks pass

## License

By contributing, you agree that your contributions will be licensed under the Apache 2.0 License.
