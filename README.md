## Apples to Apples - Python Implementation

This project implements the Apples to Apples game in Python.

**Requirements:**

  * Python 3.x ([https://www.python.org/downloads/](https://www.python.org/downloads/))
    * `pytest` library for the tests

**Project Structure:**

  * `src`: Contains the main source code files.
  * `tests`: Contains the unit tests.
  * `data`: Contains the red and green apple text files (redApples.txt and greenApples.txt).

**Getting Started:**

I chose [PyCharm](https://www.jetbrains.com/pycharm/) as my IDE

#### **Clone the Repository:**

    ```bash
    git clone https://github.com/KikiBerg/applestentan.git
    ```

#### **Set Up a Virtual Environment:**

A virtual environment is a self-contained directory that contains a Python installation for your project. It helps manage dependencies independently.

**On Windows:**

1.  Open a command prompt and navigate to your project directory.
2.  Run: `python -m venv venv` (This creates a directory named `venv`).
3.  Activate the environment: `venv\Scripts\activate`
4.  Install dependencies: `pip install dependency-name-here`
5.  Deactivate the environment: `deactivate`

**On macOS/Linux:**

1.  Open a terminal and navigate to your project directory.
2.  Run: `python -m venv venv` (This creates a directory named `venv`).
3.  Activate the environment: `source venv/bin/activate`
4.  Install dependencies: `pip install unittest`
5.  Deactivate the environment: `deactivate`

**Compiling Python Code:**

Python is an interpreted language, so you don't need to compile code in the traditional sense.
You can directly run Python scripts using the `python` command.

**Running the Game:**

```python
python src/game.py
```

#### **Run the Tests:**

    `pytest test_game.py`

To run all tests at once: 

    `pytest tests/`

These commands will run the tests and report any errors.

#### **Running the Game:**

```python
python src/game.py
```

**Further Development:**


