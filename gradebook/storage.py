import json
import logging

DEFAULT_PATH = "data/gradebook.json"

# Configure logging to write INFO and ERROR messages to logs/app.log
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# This function loads data from a JSON file.
# If the file does not exist, it returns an empty structure.
# If the JSON is invalid, it shows a message and returns empty data.
def load_data(path=DEFAULT_PATH):
    try:
        # Open the file in read mode
        with open(path, "r", encoding="utf-8") as file:
            # Convert JSON content into a Python dictionary
            data = json.load(file)

        logging.info("Data loaded successfully from %s", path)
        return data

    except FileNotFoundError:
        logging.info("Data file not found. Starting with empty gradebook.")
        return {
            "students": [],
            "courses": [],
            "enrollments": []
        }

    except json.JSONDecodeError:
        logging.error("Invalid JSON format in file: %s", path)
        print("The data file is corrupted or contains invalid JSON. Starting with empty data.")
        return {
            "students": [],
            "courses": [],
            "enrollments": []
        }


# This function saves data (Python dictionary) into a JSON file.
# It overwrites the file if it already exists.
def save_data(data, path=DEFAULT_PATH):
    try:
        # Open the file in write mode
        with open(path, "w", encoding="utf-8") as file:
            # Convert Python dictionary into JSON and save it
            json.dump(data, file, indent=4)

        logging.info("Data saved successfully to %s", path)

    except OSError as error:
        logging.error("Error saving data to %s: %s", path, error)
        print(f"Error saving data: {error}")