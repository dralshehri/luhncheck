# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Python package to validate identification numbers using the Luhn algorithm with additional optional checks.

### Core Structure
- **`src/luhncheck/`** - Main package code
  - `__init__.py` - Contains the `is_luhn()` function for validation

### Key Function
- **`is_luhn(number, length, prefix)`** - Validates identification numbers using Luhn algorithm

## Development

The project uses `uv` as the package manager. Run `uv sync` to set up the environment.

### Commands
```bash
uv run ruff format       # Format code
uv run ruff check --fix  # Lint code
uv run mypy              # Type check
uv run pytest --cov      # Test with coverage
```

## Code Quality Standards

- **100% test coverage** is required - coverage will fail if below 100%
- **Type hints** are mandatory for all functions and methods
- **Ruff** is used for both formatting and linting
- **MyPy** runs in strict mode
- **Google docstring style** for all public APIs

## Critical Constraints

- **Zero runtime dependencies** - do not add any
- **Performance matters** - this is an optimized library
