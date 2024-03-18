import turtle
import pandas as pd
import fetch_name  # custom module for fetching state names

# Read the data from the CSV file
data = pd.read_csv('50_states.csv')
data_list = data.state.to_list()

# Set up the turtle screen and window
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Initialize variables
game_is_on = True
answers = []
count = 0

# Main game loop
while game_is_on:
    # Get user input for state name
    answer_state = screen.textinput(title=f"{count}/50 States Correct", prompt="What's another state name?").title()

    # Exit the game if the user types "Exit"
    if answer_state == "Exit":
        break

    # Check if the entered state name is valid
    if answer_state in data_list:
        # If the state hasn't been guessed yet
        if answer_state not in answers:
            # Add the state to the list of correct answers
            answers.append(answer_state)
            count += 1  # Increment the count of correct answers

            # Get the coordinates of the state from the dataframe
            row = data[data.state == answer_state]
            x = row.x.iloc[0]
            y = row.y.iloc[0]

            # Use a custom module to fetch and display the state name on the map
            name = fetch_name.FetchName(answer_state, x, y)

        if count == 50:
            print("You Win!")
            break

# Create a list of states not yet guessed
study = [state for state in data_list if state not in answers]

# Write the remaining states to a CSV file for revision
study_df = pd.DataFrame(study)
study_df.to_csv("revise.csv")
