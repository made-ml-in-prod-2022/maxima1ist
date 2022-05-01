from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile


RAW_DATA_PATH = "data/raw/"


def unzip(file: str, path: str):
    with ZipFile(file, 'r') as zip:
        zip.extractall(path)


def download_dataset(dataset: str, path: str):
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(
        dataset=dataset,
        path=path
    )


if __name__ == "__main__":
    download_dataset("cherngs/heart-disease-cleveland-uci", "data/raw")
    unzip(RAW_DATA_PATH + "heart-disease-cleveland-uci.zip", RAW_DATA_PATH)
