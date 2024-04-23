from  logger import *
from datetime import datetime
import json
import pandas as pd

def convert_to_csv():
    with open('../jobs_config.json', 'r') as file:
        table_names = json.load(file)

    for table_name in table_names:
        landing = "../data/landing/"
        datalake = "../data/datalake"  
        table_name = table_name 

        # stroing JSON objects from each file
        json_data = []

        # looping through JSON files 
        for file_name in os.listdir(os.path.join(landing, table_name)):
            if file_name.endswith(".json"):
                file_path = os.path.join(landing, table_name, file_name)
                with open(file_path, "r") as file:
                    # read and parse each line separately, every line is seperate JSON object
                    for line in file:
                        json_object = json.loads(line)
                        json_data.append(json_object)

        # convert JSON file to dataframe
        df = pd.json_normalize(json_data)

        # create folder if it doesn"t exist
        output_dir = os.path.join(datalake, table_name)
        os.makedirs(output_dir, exist_ok=True)

        # getting the current date
        current_date = datetime.now().strftime('%Y-%m-%d')

        # saving data frame as csv file as the name of the current date
        output_file_name = f"{current_date}.csv"
        output_file_path = os.path.join(output_dir, output_file_name)
        df.to_csv(output_file_path, index=False)

# write the date when script executed 
logger.info(f"Script executed on {datetime.now().strftime('%Y-%m-%d')}")
