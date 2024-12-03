# Apples to Apples - Python Implementation

A Python implementation of the popular card game **Apples to Apples**.

---

## Features
- Local multiplayer with human players and AI-controlled bots.
- Modular design for easy expansion and customization.
- Simple text-based interface.

---

## Getting Started

### Prerequisites
- Python 3.x ([Download here](https://www.python.org/downloads/))
- `pytest` (library for running tests)

### Clone the Repository
```bash
git clone https://github.com/KikiBerg/applestentan.git
cd applestentan
```

---

### Virtual Environment & Dependencies
A virtual environment is a self-contained directory that contains a Python installation for your project. 
It helps manage dependencies independently. All required dependencies are listed in `requirements.txt`

**Setting up On Windows:**

1.  Open a command prompt and navigate to your project directory.
2.  Run: `python -m venv venv` (This creates a directory named `venv`).
3.  Activate the environment: `venv\Scripts\activate`
4.  Install all dependencies: `pip install -r requirements.txt`
5.  Deactivate the environment: `deactivate`

**On macOS/Linux:**

1.  Open a terminal and navigate to your project directory.
2.  Run: `python -m venv venv`
3.  Activate the environment: `source venv/bin/activate`
4.  Install all dependencies: `pip install -r requirements.txt`
5.  Deactivate the environment: `deactivate`

### Compiling Python Code

Python is an interpreted language, so you don't need to compile code in the traditional sense.
You can directly run Python scripts using the `python` command.

### Running the Game

    `python src/main.py`

#### How to Play
1. Start the game by running python src/main.py.
2. Enter the number of human and bot players.
3. Follow the on-screen prompts to play rounds until a winner is declared.

### Running the Tests
 
Run unit tests using pytest: 

    `pytest tests/`

---

### Project Structure

  * `src`: Contains the main source code files.
  * `tests`: Contains the unit tests.
  * `assets`: Contains the red and green apple text files (redApples.txt and greenApples.txt).

#### Notes on Documentation
  - See `requirements.md` for detailed system requirements and input file formats.
  - See `tests.md` for instructions on running and writing tests.

---

### Diagrams: overview of the game's architecture

#### System Architecture: Class diagram [![](https://mermaid.ink/img/pako:eNqNVW1P2zAQ_isnS5uY1LKWvtFoYkKA2CbBEGhDmvLFJNfEI7Ez2xEUxH_f2Ulo0paXfnKde-6ee-7FjyxSMbKA9fv9UFphMwzgp0S4VKWMQS3glOdYZHwJQsJhUWRo-lb1q1MoPSyUBv-VKCM8FjzRPAdwl0C_Dx_ggmsrIlFwaU11WaxuvPsTmQiJm98uKCzqzftjjG7PuOTJto-XJRF70WPKDba4fZfCCp6JB26Fqq-lsghaJKlt0q-8BXCF1kBZgE0REroPQykaB2ig8HQNfISYCNa5rvDQPzioUwpWgbGBbTVvZdrBtAK0TDoRjpFnMAONMXBfLLAKkEdpHbClgq81ITS_g1ONWBd6mxxewAAusdBokCrqhYDCXRvSIxO3xI4c9cCUN7mwPfhbxgluF6NydnKPUUlBXHwfvhXdm2xK4alKvLeQeL68QqxndOUpENsYmoZ9m0YFIkwbsuLR6HvKqQ30Sl-IuI4N7OB9hIWtsv5Ugz3EozvtVLHzuK3E2saXXMYqd7Wv7ddz_eECUotmGK16-fVMPWQNsZlo5dh4MwN3QlLTJ57Fe7Jr7J912kqsNbQB_CpiTuxMpDR2EqU9hFKYNKfGe09-z4BvJJ55vaHctHRnpRnnO2FT-DJr1-nFmRPGanHjYq9XyTGFI0UrVpYvLpuODL9p1J0Q9Yhp940mjFKBKHXz77SFSMlYvFjwjsMjh4KF0r4oze5smUB_vYjX3pAw1GJfYWeJ5rNUdVfzzMK56vh6o4evLK3iamy1f168tBLv2jsCM6rP9etOVzsuyrjGDgeUcUv2w7hSh6p7TlKbluoZLqqVVju7qOstZJSVMUJa5lwacHrfKLsN2emg6mB84f0GdF3vwDG1Fp1DyXosR51zEdN7--j8hYx2CL0jLKBjjAteZjZkoXwiU15adbWUEQusLrHHSLEkZcGCkz49VvoZqZ_b51ukZJU-q150_7D3GL17f5TKGzf0lwWP7J4Fw73x7nS4PxnN9ybj_eFsv8eWLBiNdgfDyXw2Gwymo9F0OHvqsQePH-zOJ4PZfDAYjWfz8d54-vQfy3q-oA?type=png)](https://mermaid.live/edit#pako:eNqNVW1P2zAQ_isnS5uY1LKWvtFoYkKA2CbBEGhDmvLFJNfEI7Ez2xEUxH_f2Ulo0paXfnKde-6ee-7FjyxSMbKA9fv9UFphMwzgp0S4VKWMQS3glOdYZHwJQsJhUWRo-lb1q1MoPSyUBv-VKCM8FjzRPAdwl0C_Dx_ggmsrIlFwaU11WaxuvPsTmQiJm98uKCzqzftjjG7PuOTJto-XJRF70WPKDba4fZfCCp6JB26Fqq-lsghaJKlt0q-8BXCF1kBZgE0REroPQykaB2ig8HQNfISYCNa5rvDQPzioUwpWgbGBbTVvZdrBtAK0TDoRjpFnMAONMXBfLLAKkEdpHbClgq81ITS_g1ONWBd6mxxewAAusdBokCrqhYDCXRvSIxO3xI4c9cCUN7mwPfhbxgluF6NydnKPUUlBXHwfvhXdm2xK4alKvLeQeL68QqxndOUpENsYmoZ9m0YFIkwbsuLR6HvKqQ30Sl-IuI4N7OB9hIWtsv5Ugz3EozvtVLHzuK3E2saXXMYqd7Wv7ddz_eECUotmGK16-fVMPWQNsZlo5dh4MwN3QlLTJ57Fe7Jr7J912kqsNbQB_CpiTuxMpDR2EqU9hFKYNKfGe09-z4BvJJ55vaHctHRnpRnnO2FT-DJr1-nFmRPGanHjYq9XyTGFI0UrVpYvLpuODL9p1J0Q9Yhp940mjFKBKHXz77SFSMlYvFjwjsMjh4KF0r4oze5smUB_vYjX3pAw1GJfYWeJ5rNUdVfzzMK56vh6o4evLK3iamy1f168tBLv2jsCM6rP9etOVzsuyrjGDgeUcUv2w7hSh6p7TlKbluoZLqqVVju7qOstZJSVMUJa5lwacHrfKLsN2emg6mB84f0GdF3vwDG1Fp1DyXosR51zEdN7--j8hYx2CL0jLKBjjAteZjZkoXwiU15adbWUEQusLrHHSLEkZcGCkz49VvoZqZ_b51ukZJU-q150_7D3GL17f5TKGzf0lwWP7J4Fw73x7nS4PxnN9ybj_eFsv8eWLBiNdgfDyXw2Gwymo9F0OHvqsQePH-zOJ4PZfDAYjWfz8d54-vQfy3q-oA)

#### Sequence diagram: One Round of Gameplay in Apples-to-Apples [![](https://mermaid.ink/img/pako:eNqNVW1P2zAQ_isnS5uY1LKWvtFoYkKA2CbBEGhDmvLFJNfEI7Ez2xEUxH_f2Ulo0paXfnKde-6ee-7FjyxSMbKA9fv9UFphMwzgp0S4VKWMQS3glOdYZHwJQsJhUWRo-lb1q1MoPSyUBv-VKCM8FjzRPAdwl0C_Dx_ggmsrIlFwaU11WaxuvPsTmQiJm98uKCzqzftjjG7PuOTJto-XJRF70WPKDba4fZfCCp6JB26Fqq-lsghaJKlt0q-8BXCF1kBZgE0REroPQykaB2ig8HQNfISYCNa5rvDQPzioUwpWgbGBbTVvZdrBtAK0TDoRjpFnMAONMXBfLLAKkEdpHbClgq81ITS_g1ONWBd6mxxewAAusdBokCrqhYDCXRvSIxO3xI4c9cCUN7mwPfhbxgluF6NydnKPUUlBXHwfvhXdm2xK4alKvLeQeL68QqxndOUpENsYmoZ9m0YFIkwbsuLR6HvKqQ30Sl-IuI4N7OB9hIWtsv5Ugz3EozvtVLHzuK3E2saXXMYqd7Wv7ddz_eECUotmGK16-fVMPWQNsZlo5dh4MwN3QlLTJ57Fe7Jr7J912kqsNbQB_CpiTuxMpDR2EqU9hFKYNKfGe09-z4BvJJ55vaHctHRnpRnnO2FT-DJr1-nFmRPGanHjYq9XyTGFI0UrVpYvLpuODL9p1J0Q9Yhp940mjFKBKHXz77SFSMlYvFjwjsMjh4KF0r4oze5smUB_vYjX3pAw1GJfYWeJ5rNUdVfzzMK56vh6o4evLK3iamy1f168tBLv2jsCM6rP9etOVzsuyrjGDgeUcUv2w7hSh6p7TlKbluoZLqqVVju7qOstZJSVMUJa5lwacHrfKLsN2emg6mB84f0GdF3vwDG1Fp1DyXosR51zEdN7--j8hYx2CL0jLKBjjAteZjZkoXwiU15adbWUEQusLrHHSLEkZcGCkz49VvoZqZ_b51ukZJU-q150_7D3GL17f5TKGzf0lwWP7J4Fw73x7nS4PxnN9ybj_eFsv8eWLBiNdgfDyXw2Gwymo9F0OHvqsQePH-zOJ4PZfDAYjWfz8d54-vQfy3q-oA?type=png)](https://mermaid.live/edit#pako:eNqNVW1P2zAQ_isnS5uY1LKWvtFoYkKA2CbBEGhDmvLFJNfEI7Ez2xEUxH_f2Ulo0paXfnKde-6ee-7FjyxSMbKA9fv9UFphMwzgp0S4VKWMQS3glOdYZHwJQsJhUWRo-lb1q1MoPSyUBv-VKCM8FjzRPAdwl0C_Dx_ggmsrIlFwaU11WaxuvPsTmQiJm98uKCzqzftjjG7PuOTJto-XJRF70WPKDba4fZfCCp6JB26Fqq-lsghaJKlt0q-8BXCF1kBZgE0REroPQykaB2ig8HQNfISYCNa5rvDQPzioUwpWgbGBbTVvZdrBtAK0TDoRjpFnMAONMXBfLLAKkEdpHbClgq81ITS_g1ONWBd6mxxewAAusdBokCrqhYDCXRvSIxO3xI4c9cCUN7mwPfhbxgluF6NydnKPUUlBXHwfvhXdm2xK4alKvLeQeL68QqxndOUpENsYmoZ9m0YFIkwbsuLR6HvKqQ30Sl-IuI4N7OB9hIWtsv5Ugz3EozvtVLHzuK3E2saXXMYqd7Wv7ddz_eECUotmGK16-fVMPWQNsZlo5dh4MwN3QlLTJ57Fe7Jr7J912kqsNbQB_CpiTuxMpDR2EqU9hFKYNKfGe09-z4BvJJ55vaHctHRnpRnnO2FT-DJr1-nFmRPGanHjYq9XyTGFI0UrVpYvLpuODL9p1J0Q9Yhp940mjFKBKHXz77SFSMlYvFjwjsMjh4KF0r4oze5smUB_vYjX3pAw1GJfYWeJ5rNUdVfzzMK56vh6o4evLK3iamy1f168tBLv2jsCM6rP9etOVzsuyrjGDgeUcUv2w7hSh6p7TlKbluoZLqqVVju7qOstZJSVMUJa5lwacHrfKLsN2emg6mB84f0GdF3vwDG1Fp1DyXosR51zEdN7--j8hYx2CL0jLKBjjAteZjZkoXwiU15adbWUEQusLrHHSLEkZcGCkz49VvoZqZ_b51ukZJU-q150_7D3GL17f5TKGzf0lwWP7J4Fw73x7nS4PxnN9ybj_eFsv8eWLBiNdgfDyXw2Gwymo9F0OHvqsQePH-zOJ4PZfDAYjWfz8d54-vQfy3q-oA)

---
