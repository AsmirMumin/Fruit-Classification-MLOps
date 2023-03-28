Module src.train_model
======================
Python script to train the model

Functions
---------

    
`get_processed_data(data_location: str)`
:   Get processed data from a specified location
    
    Parameters
    ----------
    data_location : str
        Location to get the data

    
`predict(search: sklearn.model_selection._search.GridSearchCV, X_test: pandas.core.frame.DataFrame)`
:   _summary_
    
    Parameters
    ----------
    search : GridSearchCV
    X_test : pd.DataFrame
        Features for testing

    
`save_model(model: sklearn.model_selection._search.GridSearchCV, save_path: str)`
:   Save model to a specified location
    
    Parameters
    ----------
    model : GridSearchCV
    save_path : str

    
`save_predictions(predictions: <built-in function array>, save_path: str)`
:   Save predictions to a specified location
    
    Parameters
    ----------
    predictions : np.array
    save_path : str

    
`train(location: config.Location = Location(train_data_raw='data/raw/fruits-360/Training', test_data_raw='data/raw/fruits-360/Test', data_process='data/processed/fruits.pkl', data_final='data/final/predictions.pkl', model='models/svc.pkl', scaler='processors/scaler.pkl', input_notebook='notebooks/analyze_results.ipynb', output_notebook='notebooks/results.ipynb'), svc_params: config.ModelParams = ModelParams(C=[1, 10], gamma=[1, 0.1]))`
:   Flow to train the model
    
    Parameters
    ----------
    location : Location, optional
        Locations of inputs and outputs, by default Location()
    svc_params : ModelParams, optional
        Configurations for training the model, by default ModelParams()

    
`train_model(model_params: config.ModelParams, X_train: pandas.core.frame.DataFrame, y_train: pandas.core.series.Series)`
:   Train the model
    
    Parameters
    ----------
    model_params : ModelParams
        Parameters for the model
    X_train : pd.DataFrame
        Features for training
    y_train : pd.Series
        Label for training