This script, `get_partitions.py`, interacts with an IMDb API to retrieve data partitions based on specified table names. It iterates through each table defined in a JSON configuration file `jobs_config.json`, retrieves partitions from the API, and processes each partition's data. It then uploads the data to an AWS S3 bucket, saves it locally, and updates the configuration file with the latest partition date.

#### Main Functionality:

1. **Retrieve Jobs Configuration**: Reads the JSON configuration file `jobs_config.json` to get table names and their associated parameters.

2. **Retrieve Partitions**: Utilizes the IMDb API to retrieve partitions for each table. It compares the partition date with the minimum ingestion date specified in the configuration.

3. **Process and Upload Data**:

   - Downloads data associated with each partition from the API.
   - Converts the JSON data to a pandas DataFrame.
   - Uploads the DataFrame to an AWS S3 bucket in Parquet format using AWS Wrangler.
   - Saves the data locally in JSON format.

4. **Update Configuration**: Updates the minimum ingestion date for each table in the configuration file based on the latest partition processed.

#### External Dependencies:

- `requests`: Used for making HTTP requests to the IMDb API.
- `awswrangler`: Facilitates interactions with AWS services like S3.
- `pandas`: Handles data manipulation tasks.
- `os`: Provides functions for interacting with the operating system.

#### Additional Notes:

- Error handling is implemented to manage cases where partitions cannot be uploaded, possibly due to data corruption.
- The script prints information about the processed partitions for each table.
- It logs errors and informational messages during execution.
