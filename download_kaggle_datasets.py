import os
from kaggle.api.kaggle_api_extended import KaggleApi  # type: ignore
import logging
from dotenv import load_dotenv  # type: ignore
import argparse

load_dotenv()

logging.basicConfig(level=logging.INFO)

# Set your Kaggle username and API key
os.getenv("KAGGLE_USERNAME")
os.getenv("KAGGLE_KEY")

api = KaggleApi()
api.authenticate()

argparser = argparse.ArgumentParser()
argparser.add_argument(
    "--dataset", type=str, required=True, help="Name of the dataset to download"
)
argparser.add_argument("--path", type=str, default=".", help="Path to save the dataset")
args = argparser.parse_args()

# Download the dataset
logging.info("Downloading the dataset")
api.dataset_download_files(args.dataset, path=args.path, unzip=True)

logging.info("Dataset downloaded successfully")
