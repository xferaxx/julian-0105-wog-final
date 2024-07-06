# imports
from utils import SCORES_FILE_NAME, BAD_RETURN_CODE


# ################# Score ##################

def add_score(level):
    """ Function to add score based on game difficulty """
    points = calculate_points(level)

    current_score = read_current_score()
    if current_score is None:
        current_score = points  # Initialize with points if no score found
    else:
        if current_score < 0:
            current_score = 0
            current_score += points  # Add points to current score
        else:
            current_score += points  # Add points to current score

    write_score(current_score)


def calculate_points(level):
    """ Function to calculate points based on game difficulty """
    return (level * 3) + 5


def read_current_score():
    """ Function to read current score from file """
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            score = int(file.read().strip())
        file.close()
        return score
    except FileNotFoundError:
        return None
    except ValueError:
        print(f"Error: Invalid data found in {SCORES_FILE_NAME}.")
        file.close()
        return BAD_RETURN_CODE


def write_score(score):
    """ Function to write score to file """
    try:
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(score))
        print(f"Score updated and saved successfully.")
        file.close()
    except IOError:
        print(f"Error writing to file {SCORES_FILE_NAME}.")
        file.close()
