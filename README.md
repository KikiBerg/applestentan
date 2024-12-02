## Apples to Apples - Python Implementation

This project implements the Apples to Apples game in Python.

### Requirements

  * Python 3.x ([https://www.python.org/downloads/](https://www.python.org/downloads/))
    * `pytest` library for the tests

### Project Structure

  * `src`: Contains the main source code files.
  * `tests`: Contains the unit tests.
  * `data`: Contains the red and green apple text files (redApples.txt and greenApples.txt).

---

### Getting Started

- I chose [PyCharm](https://www.jetbrains.com/pycharm/) as my IDE
- I used [Mermaid Live Editor](https://mermaid.js.org/) for my diagrams.

#### Clone the Repository:

    ```bash
    git clone https://github.com/KikiBerg/applestentan.git
    ```

#### Set Up a Virtual Environment:

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

#### Compiling Python Code

Python is an interpreted language, so you don't need to compile code in the traditional sense.
You can directly run Python scripts using the `python` command.

#### Running the Game

    `python src/game.py`

#### Running the Tests

    `pytest test_game.py`

To run all tests at once: 

    `pytest tests/`

These commands will run the tests and report any errors.

---

### Diagrams

#### System Architecture: Class diagram [![](https://mermaid.ink/img/pako:eNqNVW1P2zAQ_isnS5uY1LKWvtFoYkKA2CbBEGhDmvLFJNfEI7Ez2xEUxH_f2Ulo0paXfnKde-6ee-7FjyxSMbKA9fv9UFphMwzgp0S4VKWMQS3glOdYZHwJQsJhUWRo-lb1q1MoPSyUBv-VKCM8FjzRPAdwl0C_Dx_ggmsrIlFwaU11WaxuvPsTmQiJm98uKCzqzftjjG7PuOTJto-XJRF70WPKDba4fZfCCp6JB26Fqq-lsghaJKlt0q-8BXCF1kBZgE0REroPQykaB2ig8HQNfISYCNa5rvDQPzioUwpWgbGBbTVvZdrBtAK0TDoRjpFnMAONMXBfLLAKkEdpHbClgq81ITS_g1ONWBd6mxxewAAusdBokCrqhYDCXRvSIxO3xI4c9cCUN7mwPfhbxgluF6NydnKPUUlBXHwfvhXdm2xK4alKvLeQeL68QqxndOUpENsYmoZ9m0YFIkwbsuLR6HvKqQ30Sl-IuI4N7OB9hIWtsv5Ugz3EozvtVLHzuK3E2saXXMYqd7Wv7ddz_eECUotmGK16-fVMPWQNsZlo5dh4MwN3QlLTJ57Fe7Jr7J912kqsNbQB_CpiTuxMpDR2EqU9hFKYNKfGe09-z4BvJJ55vaHctHRnpRnnO2FT-DJr1-nFmRPGanHjYq9XyTGFI0UrVpYvLpuODL9p1J0Q9Yhp940mjFKBKHXz77SFSMlYvFjwjsMjh4KF0r4oze5smUB_vYjX3pAw1GJfYWeJ5rNUdVfzzMK56vh6o4evLK3iamy1f168tBLv2jsCM6rP9etOVzsuyrjGDgeUcUv2w7hSh6p7TlKbluoZLqqVVju7qOstZJSVMUJa5lwacHrfKLsN2emg6mB84f0GdF3vwDG1Fp1DyXosR51zEdN7--j8hYx2CL0jLKBjjAteZjZkoXwiU15adbWUEQusLrHHSLEkZcGCkz49VvoZqZ_b51ukZJU-q150_7D3GL17f5TKGzf0lwWP7J4Fw73x7nS4PxnN9ybj_eFsv8eWLBiNdgfDyXw2Gwymo9F0OHvqsQePH-zOJ4PZfDAYjWfz8d54-vQfy3q-oA?type=png)](https://mermaid.live/edit#pako:eNqNVW1P2zAQ_isnS5uY1LKWvtFoYkKA2CbBEGhDmvLFJNfEI7Ez2xEUxH_f2Ulo0paXfnKde-6ee-7FjyxSMbKA9fv9UFphMwzgp0S4VKWMQS3glOdYZHwJQsJhUWRo-lb1q1MoPSyUBv-VKCM8FjzRPAdwl0C_Dx_ggmsrIlFwaU11WaxuvPsTmQiJm98uKCzqzftjjG7PuOTJto-XJRF70WPKDba4fZfCCp6JB26Fqq-lsghaJKlt0q-8BXCF1kBZgE0REroPQykaB2ig8HQNfISYCNa5rvDQPzioUwpWgbGBbTVvZdrBtAK0TDoRjpFnMAONMXBfLLAKkEdpHbClgq81ITS_g1ONWBd6mxxewAAusdBokCrqhYDCXRvSIxO3xI4c9cCUN7mwPfhbxgluF6NydnKPUUlBXHwfvhXdm2xK4alKvLeQeL68QqxndOUpENsYmoZ9m0YFIkwbsuLR6HvKqQ30Sl-IuI4N7OB9hIWtsv5Ugz3EozvtVLHzuK3E2saXXMYqd7Wv7ddz_eECUotmGK16-fVMPWQNsZlo5dh4MwN3QlLTJ57Fe7Jr7J912kqsNbQB_CpiTuxMpDR2EqU9hFKYNKfGe09-z4BvJJ55vaHctHRnpRnnO2FT-DJr1-nFmRPGanHjYq9XyTGFI0UrVpYvLpuODL9p1J0Q9Yhp940mjFKBKHXz77SFSMlYvFjwjsMjh4KF0r4oze5smUB_vYjX3pAw1GJfYWeJ5rNUdVfzzMK56vh6o4evLK3iamy1f168tBLv2jsCM6rP9etOVzsuyrjGDgeUcUv2w7hSh6p7TlKbluoZLqqVVju7qOstZJSVMUJa5lwacHrfKLsN2emg6mB84f0GdF3vwDG1Fp1DyXosR51zEdN7--j8hYx2CL0jLKBjjAteZjZkoXwiU15adbWUEQusLrHHSLEkZcGCkz49VvoZqZ_b51ukZJU-q150_7D3GL17f5TKGzf0lwWP7J4Fw73x7nS4PxnN9ybj_eFsv8eWLBiNdgfDyXw2Gwymo9F0OHvqsQePH-zOJ4PZfDAYjWfz8d54-vQfy3q-oA)
#### Sequence diagram: One Round of Gameplay in Apples-to-Apples [![](https://mermaid.ink/img/pako:eNqNVW1P2zAQ_isnS5uY1LKWvtFoYkKA2CbBEGhDmvLFJNfEI7Ez2xEUxH_f2Ulo0paXfnKde-6ee-7FjyxSMbKA9fv9UFphMwzgp0S4VKWMQS3glOdYZHwJQsJhUWRo-lb1q1MoPSyUBv-VKCM8FjzRPAdwl0C_Dx_ggmsrIlFwaU11WaxuvPsTmQiJm98uKCzqzftjjG7PuOTJto-XJRF70WPKDba4fZfCCp6JB26Fqq-lsghaJKlt0q-8BXCF1kBZgE0REroPQykaB2ig8HQNfISYCNa5rvDQPzioUwpWgbGBbTVvZdrBtAK0TDoRjpFnMAONMXBfLLAKkEdpHbClgq81ITS_g1ONWBd6mxxewAAusdBokCrqhYDCXRvSIxO3xI4c9cCUN7mwPfhbxgluF6NydnKPUUlBXHwfvhXdm2xK4alKvLeQeL68QqxndOUpENsYmoZ9m0YFIkwbsuLR6HvKqQ30Sl-IuI4N7OB9hIWtsv5Ugz3EozvtVLHzuK3E2saXXMYqd7Wv7ddz_eECUotmGK16-fVMPWQNsZlo5dh4MwN3QlLTJ57Fe7Jr7J912kqsNbQB_CpiTuxMpDR2EqU9hFKYNKfGe09-z4BvJJ55vaHctHRnpRnnO2FT-DJr1-nFmRPGanHjYq9XyTGFI0UrVpYvLpuODL9p1J0Q9Yhp940mjFKBKHXz77SFSMlYvFjwjsMjh4KF0r4oze5smUB_vYjX3pAw1GJfYWeJ5rNUdVfzzMK56vh6o4evLK3iamy1f168tBLv2jsCM6rP9etOVzsuyrjGDgeUcUv2w7hSh6p7TlKbluoZLqqVVju7qOstZJSVMUJa5lwacHrfKLsN2emg6mB84f0GdF3vwDG1Fp1DyXosR51zEdN7--j8hYx2CL0jLKBjjAteZjZkoXwiU15adbWUEQusLrHHSLEkZcGCkz49VvoZqZ_b51ukZJU-q150_7D3GL17f5TKGzf0lwWP7J4Fw73x7nS4PxnN9ybj_eFsv8eWLBiNdgfDyXw2Gwymo9F0OHvqsQePH-zOJ4PZfDAYjWfz8d54-vQfy3q-oA?type=png)](https://mermaid.live/edit#pako:eNqNVW1P2zAQ_isnS5uY1LKWvtFoYkKA2CbBEGhDmvLFJNfEI7Ez2xEUxH_f2Ulo0paXfnKde-6ee-7FjyxSMbKA9fv9UFphMwzgp0S4VKWMQS3glOdYZHwJQsJhUWRo-lb1q1MoPSyUBv-VKCM8FjzRPAdwl0C_Dx_ggmsrIlFwaU11WaxuvPsTmQiJm98uKCzqzftjjG7PuOTJto-XJRF70WPKDba4fZfCCp6JB26Fqq-lsghaJKlt0q-8BXCF1kBZgE0REroPQykaB2ig8HQNfISYCNa5rvDQPzioUwpWgbGBbTVvZdrBtAK0TDoRjpFnMAONMXBfLLAKkEdpHbClgq81ITS_g1ONWBd6mxxewAAusdBokCrqhYDCXRvSIxO3xI4c9cCUN7mwPfhbxgluF6NydnKPUUlBXHwfvhXdm2xK4alKvLeQeL68QqxndOUpENsYmoZ9m0YFIkwbsuLR6HvKqQ30Sl-IuI4N7OB9hIWtsv5Ugz3EozvtVLHzuK3E2saXXMYqd7Wv7ddz_eECUotmGK16-fVMPWQNsZlo5dh4MwN3QlLTJ57Fe7Jr7J912kqsNbQB_CpiTuxMpDR2EqU9hFKYNKfGe09-z4BvJJ55vaHctHRnpRnnO2FT-DJr1-nFmRPGanHjYq9XyTGFI0UrVpYvLpuODL9p1J0Q9Yhp940mjFKBKHXz77SFSMlYvFjwjsMjh4KF0r4oze5smUB_vYjX3pAw1GJfYWeJ5rNUdVfzzMK56vh6o4evLK3iamy1f168tBLv2jsCM6rP9etOVzsuyrjGDgeUcUv2w7hSh6p7TlKbluoZLqqVVju7qOstZJSVMUJa5lwacHrfKLsN2emg6mB84f0GdF3vwDG1Fp1DyXosR51zEdN7--j8hYx2CL0jLKBjjAteZjZkoXwiU15adbWUEQusLrHHSLEkZcGCkz49VvoZqZ_b51ukZJU-q150_7D3GL17f5TKGzf0lwWP7J4Fw73x7nS4PxnN9ybj_eFsv8eWLBiNdgfDyXw2Gwymo9F0OHvqsQePH-zOJ4PZfDAYjWfz8d54-vQfy3q-oA)

---
