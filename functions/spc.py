import spc_spectra as spc
import pandas as pd

def read_spc(file: str, output: str) -> pd.DataFrame:
    """
    Function for converting .spc file to Pandas dataframe
    
    Arguments:
        file (str): name of the file to convert with .spc extension.
        output (str): whether the dataframe is returned in 'long' or 'wide' format.

    Return:
        Pandas dataframe of the data contained within the .spc file.
    
    """

    data = spc.File(file)

    if data.dat_fmt == "gx-y":

        x = data.x
        y = data.sub[0].y

    else:
        
        print("only gx-y format supported at this time")

    if output == "long":

        df = pd.DataFrame({"File": [file], f"{data.xlabel}": x, f"{data.ylabel}": y})

    else:

        df = pd.DataFrame([y], columns=x, index=[file])

    return df