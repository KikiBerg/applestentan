# Apples to Apples - Testing Documentation

This document provides instructions for running tests, the general testing strategy, and details about generating and analyzing the coverage report for the **Apples2Apples** game.

---

## Prerequisites
- Ensure you have installed the required dependencies: `pip install -r requirements.txt`
- Ensure the `tests/` directory is properly set up.

## 1. Running the Tests
To ensure the quality of the project, tests are implemented using **pytest**. Follow these steps to execute the tests:

- Open a terminal and navigate to the `project/src` directory.
- Run the following command to execute all tests: `pytest`
- If you want to see detailed output, use the -v (verbose) flag: `pytest -v`
- If you want to execute a specific test file: `pytest tests/test_core.py`

## 2. General Testing Strategy
The testing strategy ensures that the game is thoroughly validated for correctness, reliability, and future extensibility.
 - **Unit Tests**: Located in `src/tests/` directory. Tests focus on individual functions and methods to validate that each works as expected.
    - `test_core.py`: Unit tests for the core game logic.
    - `test_bot.py`: Tests the BotPlayer logic, including decision-making and fallback behavior.
    - `test_game_rules.py`: Ensures compliance with game rules and win conditions.
    - `test_phases.py`: Tests the functionality of different game phases.

- **Edge Cases**: Ensure the code handles unusual or extreme inputs gracefully. 
    - Example: When the BotPlayer has no cards `test_bot_no_cards`

- **Automation**: All tests are designed to run automatically using `pytest`

- **Shared Fixtures**: Common fixtures like `players` or `game_engine` are defined in tests/conftest.py for reuse across test files.

## 3. Generating a Coverage Report
Code coverage measures how much of the project’s code is executed during the test run.
To assess test coverage, we use `pytest-cov`. Follow these steps to generate a coverage report:
 - Install pytest-cov if not already installed: `pip install pytest-cov`
 - Run the tests with coverage: `pytest --cov=src`
 - To generate an HTML report: `pytest --cov=src --cov-report=html`
 - Open the `htmlcov/index.html` file in a browser to view detailed coverage information.