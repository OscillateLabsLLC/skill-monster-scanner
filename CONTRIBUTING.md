# Contributing to skill-monster-scanner

Thanks for your interest in contributing!

## Development Setup

### Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)

### Getting Started

```bash
git clone https://github.com/OscillateLabsLLC/skill-monster-scanner
cd skill-monster-scanner

# Install dependencies (including test extras)
uv sync --extra test
```

## Common Commands

```bash
# Run tests
uv run pytest

# Run a specific test file
uv run pytest test/test_skill.py
```

## Pull Requests

1. Create a feature branch: `git checkout -b feat/my-feature`
2. Make your changes and add tests where applicable
3. Run `uv run pytest` to ensure everything passes
4. Commit using [Conventional Commits](https://www.conventionalcommits.org/) (e.g., `feat:`, `fix:`, `docs:`)
5. Open a pull request

**PR Guidelines:**
- Keep PRs focused on a single concern
- Include tests for new functionality
- Ensure all CI checks pass

## License

By contributing, you agree that your contributions will be licensed under the Apache 2.0 License.
