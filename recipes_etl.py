import json
import re
import pandas as pd
import requests


def download_and_parse_recipes(url):
    """
    Download recipes dataset from the given url, parse it as JSON
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        raw_data = response.text
        recipes = [json.loads(line) for line in raw_data.splitlines() if line.strip()]
        return recipes
    
    except requests.RequestException as e:
        print(f"HTTP request error: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return None

def save_to_json(data, file_path):
    """
    Save data to a JSON file.
    """
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

def save_to_csv(data, file_path):
    """
    Save data to a CSV file.
    """
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    
def filter_recipes_by_keyword(df, keyword):
    """
    Filter recipes DataFrame by a keyword in the 'ingredients' column
    """
    filtered_df = df[df['ingredients'].str.lower().str.contains(keyword, regex=True)]
    return filtered_df

def parse_iso_duration(duration):
    """
    Parse an ISO 8601 duration string into hours and minutes.
    """
    # where duration is only 'PT'
    if duration == "PT":
        return 0, 0

    # use regex to match the hours and mins
    hour_min = re.match(r'^PT(?:(\d+)H)?(?:(\d+)M)?$', duration)
    if hour_min is False:
        return 0, 0

    # extract hours and minutes
    hours = int(hour_min.group(1)) if hour_min.group(1) else 0
    minutes = int(hour_min.group(2)) if hour_min.group(2) else 0
    return hours, minutes

def calculate_difficulty(row):
    """
    Calculate the difficulty of a recipe based on prepTime and cookTime
    """
    try:
        prep_time = row.get("prepTime", "PT0M")
        cook_time = row.get("cookTime", "PT0M")

        # parse the prepTime and cookTime into hours and mins
        prep_hours, prep_minutes = parse_iso_duration(prep_time)
        cook_hours, cook_minutes = parse_iso_duration(cook_time)
        total_mins = (prep_hours * 60 + prep_minutes) + (cook_hours * 60 + cook_minutes)

        # determine the difficulty level based on total minutes
        if total_mins > 60:
            return "Hard"
        elif 30 <= total_mins <= 60:
            return "Medium"
        elif total_mins < 30:
            return "Easy"
        else:
            return "Unknown"
    except Exception:
        return "Unknown"

def main():
    """
    Main function to download recipes data, process it, and save the processed data to CSV
    """
    url = "https://bnlf-tests.s3.eu-central-1.amazonaws.com/recipes.json"
    # download the dataset
    recipes = download_and_parse_recipes(url)

    # save the dataset files
    if recipes:
        save_to_json(recipes, 'recipes.json')
        save_to_csv(recipes, 'recipes.csv')
    
    # read the CSV file into a DataFrame
    df = pd.read_csv('recipes.csv')
    
    # filter recipes by keywords
    chilli_recipes = filter_recipes_by_keyword(df, 'chilies|chiles|chili|chilie|chile')
    
    #print(chilli_recipes.head())
    
    # add the difficulty columnn
    chilli_recipes['difficulty'] = chilli_recipes.apply(calculate_difficulty, axis=1)
    
    chilli_recipes.to_csv('final_recipes.csv', index=False, header=True)

if __name__ == "__main__":
    main()
