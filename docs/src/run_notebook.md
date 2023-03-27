Module src.run_notebook
=======================
Python script to run the notebook

Functions
---------

    
`run_notebook(location: config.Location = Location(train_data_raw='data/raw/fruits-360/Training', test_data_raw='data/raw/fruits-360/Test', data_process='data/processed/fruits.pkl', data_final='data/final/predictions.pkl', model='models/svc.pkl', input_notebook='notebooks/analyze_results.ipynb', output_notebook='notebooks/results.ipynb'))`
:   Run a notebook with specified parameters then
    generate a notebook with the outputs
    
    Parameters
    ----------
    location : Location, optional
        Locations of inputs and outputs, by default Location()