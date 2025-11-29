from pathlib import Path

# Define the directories
ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent
DATA_DIR = ROOT_DIR / "data"
LANDING_DIR = DATA_DIR / "landing"
YELLOW_TAXI_DIR = LANDING_DIR / "trips_data" / "yellow_taxi"

# # # Helper function to get sorted .parquet files
# def get_parquet_files(dir_path):
#     return sorted([os.path.join(dir_path, file) for file in os.listdir(dir_path) if file.endswith('.parquet')])

# # Get the lists of .parquet files
# RAW_FILE_LIST = get_parquet_files(RAW_DATA_DIR)
# PROCESSED_FILE_LIST = get_parquet_files(PROCESSED_DATA_DIR)


# if __name__ == '__main__':
#     print(RAW_FILE_LIST)
#     print(PROCESSED_FILE_LIST)
