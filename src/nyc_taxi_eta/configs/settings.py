from pathlib import Path
from dotenv import load_dotenv
import os
load_dotenv()
# Define the directories
ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent
DATA_DIR = ROOT_DIR / "data"
LANDING_DIR = DATA_DIR / "landing"
YELLOW_TAXI_DIR = LANDING_DIR / "trips_data" / "yellow_taxi"
GREEN_TAXI_DIR = LANDING_DIR / "trips_data" / "green_taxi"

WAREHOUSE_DIR = DATA_DIR / "metastore"
BRONZE_DIR = WAREHOUSE_DIR / "bronze"
SILVER_DIR = WAREHOUSE_DIR / "silver"
GOLD_DIR = WAREHOUSE_DIR / "gold"
ML_DIR = WAREHOUSE_DIR / "ml"

DATABASE_USER=os.getenv("DATABASE_USER")
DATABASE_PASSWORD=os.getenv("DATABASE_PASSWORD")