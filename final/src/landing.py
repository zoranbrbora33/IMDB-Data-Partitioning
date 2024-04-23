import requests
import json
import awswrangler as wr
import pandas as pd
import os

def get_partitions():

    with open("../jobs_config.json", "r") as file:
        jobs = json.load(file)

    rest_api_url = "https://ogj9fvz5cf.execute-api.eu-central-1.amazonaws.com/v1/imdb"
    landing = "../data/landing/"
    
    for table_name in jobs.keys():
        # get date of the patrition in jobs_config.json for specific table
        if jobs[table_name]["params"]["min_ingestion_dttm"] is None:
            date = 0
        else:
            date = int(jobs[table_name]["params"]["min_ingestion_dttm"][:8])
        
        partitions_endpoint = f"/partitions/{table_name}"
        response = requests.get(rest_api_url + partitions_endpoint)
        partitions = response.json()

        print(f"{table_name} - {partitions}")
      
        for partition in partitions:
            try:
                # check if date of the partition is bigger than previous partition
                if int(partition[:8]) > date:
                
                    data_endpoint = f"/dataset/{table_name}?min_ingestion_dttm={partition}"
                    response = requests.get(rest_api_url + data_endpoint)
                    data = response.json()

                    #upload data to s3
                    df = pd.read_json(data, lines=True)
                    dtypes = {col_name: "string" for col_name in df.columns}
                    wr.s3.to_parquet(df=df, dtype=dtypes,path=f's3://zbrbora-academy-python/imdb/landing/{table_name}', dataset=True, database='zbrbora-academy-python-landing', table=table_name)
                
                    # save data locally
                    if not os.path.exists(f"{landing}{table_name}"):
                        os.mkdir(f"{landing}{table_name}")
                    file_path = os.path.join(landing, f"{table_name}/{table_name}_{partition}.json")
                    with open(file_path, "w") as file:
                        file.write(data)

                    print(f"Table: {table_name} - New partition: {partition}")
                else:
                    continue
            except ValueError as e:
                print(e)
                print(f"Partition {partition} can\"t be uploaded cause it is probably damaged!!!")

        jobs[table_name]["params"]["min_ingestion_dttm"] = partition
        
        with open("../jobs_config.json", "w") as file:
            json.dump(jobs, file, indent=4)