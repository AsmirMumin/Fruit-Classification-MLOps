Module src.main
===============
Create a flow

Functions
---------

    
`fruit_classification_flow(location: config.Location = Location(train_data_raw='data/raw/fruits-360/Training', test_data_raw='data/raw/fruits-360/Test', data_process='data/processed/fruits.pkl', data_final='data/final/predictions.pkl', model='models/svc.pkl', scaler='processors/scaler.pkl', input_notebook='notebooks/analyze_results.ipynb', output_notebook='notebooks/results.ipynb'), process_config: config.ProcessConfig = ProcessConfig(fruits=['apple', 'banana'], test_size=0.3), model_params: config.ModelParams = ModelParams(C=[1, 10], gamma=[1, 0.1]))`
:   Flow to run the process, train, and run_notebook flows
    
    Parameters
    ----------
    location : Location, optional
        Locations of inputs and outputs, by default Location()
    process_config : ProcessConfig, optional
        Configurations for processing data, by default ProcessConfig()
    model_params : ModelParams, optional
        Configurations for training models, by default ModelParams()