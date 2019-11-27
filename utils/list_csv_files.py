import os
from DoubleChainList import DoubleChainList

def list_csv_from(local):
    return DoubleChainList([filename for filename in os.listdir(local) if filename.endswith(".csv")])
