import json
from datetime import date

def load_riddles(file_path="riddles.json"):
    """
    Load riddles from a JSON file.
    """
    with open(file_path, "r") as file:
        riddles = json.load(file)
    return riddles

def get_daily_riddle(riddles):
    """
    Get the riddle of the day based on the current date.
    """
    today = date.today().toordinal()  # Unique integer for each day
    index = today % len(riddles)      # Cycle through riddles
    return riddles[index]  # Returns riddle, answer, and hint as a dictionary
