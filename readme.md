# iOLAP Academy 2023

# IMDb Data Partitioning

## Overview

This project is a data processing pipeline designed to retrieve, process, and move data from a source to a destination. It consists of several Python scripts and configuration files that automate various data-related tasks.

## Project Structure

The project structure is organized as follows:

- **src**: Contains the source code for the data processing pipeline.
  - `landing.py`: Script to retrieve data partitions from an external API and store them locally.
  - `datalake.py`: Script to convert JSON data to CSV format and store it in a data lake.
  - `move_files.py`: Script to move files from a landing directory to a processed directory.
  - `main.py`: Main script that orchestrates the execution of the data processing pipeline.
  - `logger.py`: Script to configure logging for the project.
- **jobs_config.json**: JSON configuration file containing metadata about various data tables and their parameters.
- **run_script.bat**: Batch script to automate the activation of a virtual environment and execution of the main Python script.

## Usage

To run the data processing pipeline, follow these steps:

1. Activate the virtual environment using `run_script.bat`.
2. Execute the main Python script `main.py` to start the data processing pipeline.

## Dependencies

The project depends on the following external libraries:

- `requests`: For making HTTP requests to external APIs.
- `pandas`: For data manipulation and conversion.
- `awswrangler`: For interacting with AWS services such as S3.
- `shutil`: For file manipulation operations.
- `logging`: For configuring and utilizing logging in the project.

## Contributors

- Zoran Brbora
