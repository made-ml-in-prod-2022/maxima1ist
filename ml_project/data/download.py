import opendatasets as od

od.download(
    "https://www.kaggle.com/rashikrahmanpritom/heart-attack-analysis-prediction-dataset",
    data_dir="data/raw/"
)
