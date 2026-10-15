# Rock, Paper, Scissors With ChatGPT Insults

A command-line Rock, Paper, Scissors game written in Python. Play against the computer, and every time you lose, ChatGPT generates a unique insult to motivate you to do better.

## Features

- Play Rock, Paper, Scissors against a computer opponent that picks at random
- Live score tracking for both the player and the computer
- Unique, AI-generated insult after every loss, created through the OpenAI API
- Option to play again after each round
- API key kept out of the codebase and excluded from version control

## Demo

```
Enter your choice (r = rock, p = paper, s = scissors): s
You chose: Scissors
Computer chose: Rock

Computer wins!
Score - You: 0 | Computer: 1

"<a unique ChatGPT-generated insult appears here>"

Play again?
```

## How It Works

The project is split into three files:

| File | Purpose |
|------|---------|
| `RPS.py` | Main game loop. Handles player input, the computer's random choice, score tracking, and the play-again prompt. |
| `DetermineWinner.py` | Compares the player's and computer's choices and returns the result to the main game. |
| `insult.py` | Sends a prompt to the OpenAI API and returns the generated insult to the player. |

**Game flow**

1. The player enters `r`, `p`, or `s`.
2. The computer picks a random option from the list of possible actions.
3. Both choices are passed to the winner logic, and the result is stored.
4. The scores update and the result is displayed.
5. If the computer wins, a prompt is sent to ChatGPT and the insult is shown.
6. The player is offered another round.

## Getting Started

### Prerequisites

- Python 3.11 or newer
- An [OpenAI API key](https://platform.openai.com/api-keys)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SalehSandhu/RockPaperScissorsWithChatGBT.git
   cd RockPaperScissorsWithChatGBT
   ```

2. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/Scripts/activate   # Windows (Git Bash)
   # .venv\Scripts\activate        # Windows (Command Prompt / PowerShell)
   # source .venv/bin/activate     # macOS / Linux
   ```

3. Install the dependencies:

   ```bash
   pip install openai
   ```

4. Add your API key. Create a file named `API_KEY.txt` in the project folder and paste your key into it, with nothing else in the file.

   > **Important:** `API_KEY.txt` is listed in `.gitignore` so it is never uploaded to GitHub. Never commit your key or share it publicly.

### Running the Game

```bash
python Main.py
```

## Controls

| Key | Choice |
|-----|--------|
| `r` | Rock |
| `p` | Paper |
| `s` | Scissors |

## Project Structure

```
RockPaperScissorsWithChatGBT/
├── RPS.py                # Main game logic and loop
├── DetermineWinner.py    # Winner comparison logic
├── insult.py             # OpenAI API call for insults
├── .gitignore            # Excludes API key, virtual environment, caches
└── README.md
```

## Technologies Used

- Python 3.11
- OpenAI API

## What I Learned

- Structuring a small program across multiple modules
- Calling an external API and handling the response
- Keeping secrets out of version control with `.gitignore`
- Managing game state such as scores and repeated rounds

## Future Improvements

- Add input validation for unexpected entries
- Add a best-of-N match mode
- Let the player choose the insult tone (playful, sarcastic, dramatic)
- Build a simple graphical interface

## Author

**Saleh Sandhu**
Computer Science graduate, University of Westminster

- GitHub: [@SalehSandhu](https://github.com/SalehSandhu)
- Portfolio: [salehsandhu.github.io/SalehPortfolio](https://salehsandhu.github.io/SalehPortfolio/)
