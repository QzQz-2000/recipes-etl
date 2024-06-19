# Recipe Data Processing Scripts

## Overview
This Python script downloads a JSON file containing recipes from a web URL, parses the data into a Pandas DataFrame, filters recipes based on ingredients containing specific keywords ('chilies', 'chiles', 'chili'), calculates the difficulty level of each recipe based on preparation and cooking times, and outputs the filtered recipes with difficulty levels to a CSV file.

## Requirements
- Python 3.11.5 or higher
- Required Python modules specified in requirements.txt

## Installation
1. Clone the repository using the following command:
```bash
git clone https://github.com/your_username/recipe-processing.git
cd recipe-processing
```

2. Install dependencies:

Create a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

Install required packages:

```bash
pip install -r requirements.txt
```

## RUNNING

1. Execute the python script:

```bash
python recipes_etl.py
```

## Files

**recipes_etl.py**: Main Python script that downloads, processes, and analyzes recipes data.

**requirements.txt**: Specifies Python packages required to run the script.

**README.md**: This file, providing instructions and information about the script.

**final_recipes.csv**: Example output CSV file containing filtered recipes with difficulty levels.
