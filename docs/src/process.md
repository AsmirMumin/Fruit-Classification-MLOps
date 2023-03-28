Module src.process
==================
Python script to process the data

Functions
---------

    
`load_fruit_images(fruits: list[str], path: str, dim: int = 100) ‑> tuple`
:   

    
`process(location: config.Location = Location(train_data_raw='data/raw/fruits-360/Training', test_data_raw='data/raw/fruits-360/Test', data_process='data/processed/fruits.pkl', data_final='data/final/predictions.pkl', model='models/svc.pkl', scaler='processors/scaler.pkl', input_notebook='notebooks/analyze_results.ipynb', output_notebook='notebooks/results.ipynb'), config: config.ProcessConfig = ProcessConfig(fruits=['apple', 'banana'], test_size=0.3))`
:   Flow to process the ata
    
    Parameters
    ----------
    location : Location, optional
        Locations of inputs and outputs, by default Location()
    config : ProcessConfig, optional
        Configurations for processing data, by default ProcessConfig()

    
`save_processed_data(data: dict, save_location: str)`
:   Save processed data
    
    Parameters
    ----------
    data : dict
        Data to process
    save_location : str
        Where to save the data

    
`save_scaler(scaler: sklearn.preprocessing._data.StandardScaler, save_location: str)`
:   

    
`scale_data(train_data: numpy.ndarray, test_data: numpy.ndarray) ‑> tuple`
:   

    
`split_train_test(X: pandas.core.frame.DataFrame, y: pandas.core.frame.DataFrame, test_size: int) ‑> dict`
:   _summary_
    
    Parameters
    ----------
    X : pd.DataFrame
        Features
    y : pd.DataFrame
        Target
    test_size : int
        Size of the test set