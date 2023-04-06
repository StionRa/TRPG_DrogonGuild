import os
import json
import uuid

filename = "data.json"

def create_file():
    # Check if the file exists
    if os.path.exists(filename):
        # If the file exists, check if it is empty
        if os.path.getsize(filename) == 0:
            # If the file is empty, create a new dictionary and write it to the file
            data = {"items": []}
            with open(filename, "w") as f:
                json.dump(data, f)
            print("Created new dictionary in file:", filename)
        else:
            print("File is not empty:", filename)
    else:
        # If the file does not exist, create a new dictionary and write it to the file
        data = {"items": []}
        with open(filename, "w") as f:
            json.dump(data, f)
        print("Created new file and dictionary:", filename)

def read_file():
    # Check if the file exists
    if not os.path.exists(filename):
        print("File does not exist:", filename)
        return []

    # Read the file and return the data as a list of dictionaries
    with open(filename, "r") as f:
        data_new = json.load(f)
        return data_new["items"]
def save_file(name_file):
    with open(filename, 'w') as f:
        json.dump(name_file, f)
def append_to_file(new_data):
    # Read the current data from the file
    current_data = read_file()
    # Append the new data to the current data
    current_data.append(new_data)
    # Write the updated data back to the file
    with open(filename, "w") as f:
        json.dump({"items": current_data}, f)

def create_new_data(player_name, role, health_point, mana_point, player_str, player_int, player_icon, position_x, position_y):
    # Create a new dictionary with a unique ID
    new_data = {"id": str(uuid.uuid4()), "player_name": None, "role": None, "health_point": 0, "mana_point": 0,
     "player_str": 0, "player_int": 0, "player_icon": "P",  "position_x": 6, "position_y": 6}
    # Append the new dictionary to the file
    append_to_file(new_data)

if __name__ == "__main__":
    # Create the file if it does not exist or is empty
    create_file()

    # Read the current data from the file
    current_data = read_file()
    print("Current data:", current_data)


    # Read the updated data from the file
    updated_data = read_file()
    print("Updated data:", updated_data)