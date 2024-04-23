import os
import shutil

def move_files():
    landing = "../data/landing"
    processed = "../data/processed"

    for folder in os.listdir(landing):
        landing_table_names = os.path.join(landing, folder)
        processed_table_names = os.path.join(processed, folder)

        if not os.path.exists(processed_table_names):
            os.makedirs(processed_table_names)

        for filename in os.listdir(landing_table_names):
            file_path = os.path.join(landing_table_names, filename)
            if os.path.isfile(file_path):
                shutil.move(file_path, os.path.join(processed_table_names, filename))
