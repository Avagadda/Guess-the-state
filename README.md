# India States Guessing Game

This Python script creates an interactive game using the `turtle` library where users can guess the names of Indian states displayed on a map. The game presents a blank map of India, prompting users to input the names of the states. 

## Requirements
- `turtle` library (typically comes pre-installed with Python)
- `pandas` library

## Usage
1. **Setup:** Ensure the script (`india_states_game.py`) is in the same directory as the necessary files (`blankmap.gif` and `istates2.csv`).
2. **Run:** Execute the Python script.
3. **Gameplay:** Enter the names of Indian states when prompted. Type 'Exit' to end the game.
4. **Outcome:** If any states are missed, a file named `new_st.csv` will contain the names of the missed states.

## How it Works
- A blank map of India (`blankmap.gif`) is displayed using the `turtle` library.
- State information is stored in the `istates2.csv` file, containing state names and corresponding coordinates.
- Users are prompted to guess the names of the states by inputting their names.
- Correctly guessed states are displayed on the map, and the count of correct guesses is shown.
- If the user types 'Exit,' the game stops, and a CSV file (`new_st.csv`) is created containing the names of the states that were not guessed.

## Game Mechanics
- The script allows users to interact with the map and guess the names of states.
- It keeps track of the guessed states and displays them on the map.
- Exiting the game generates a CSV file listing the states that were not guessed correctly.

Feel free to explore the code, customize the map, or extend the functionalities to fit your needs. If you encounter any issues or have suggestions, please let us know!

---

*Note:* This game offers an interactive way to learn and test your knowledge of Indian states. Modify the map or expand the game's features to enhance the user experience!
