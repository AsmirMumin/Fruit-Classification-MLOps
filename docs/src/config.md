Module src.config
=================
create Pydantic models

Functions
---------

    
`must_be_non_negative(v: float) ‑> float`
:   Check if the v is non-negative
    
    Parameters
    ----------
    v : float
        value
    
    Returns
    -------
    float
        v
    
    Raises
    ------
    ValueError
        Raises error when v is negative

Classes
-------

`Location(**data: Any)`
:   Specify the locations of inputs and outputs
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `data_final: str`
    :

    `data_process: str`
    :

    `input_notebook: str`
    :

    `model: str`
    :

    `output_notebook: str`
    :

    `scaler: str`
    :

    `test_data_raw: str`
    :

    `train_data_raw: str`
    :

`ModelParams(**data: Any)`
:   Specify the parameters of the `train` flow
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `C: list[float]`
    :

    `gamma: list[float]`
    :

`ProcessConfig(**data: Any)`
:   Specify the parameters of the `process` flow
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `fruits: list[str]`
    :

    `test_size: float`
    :