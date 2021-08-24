import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import csv

class Spectrum():
    def __init__(self):
        self.name = 0
        self.wavenumber = []
        self.transmittance = 0
        self.dict = 0 
        self.file = 0
    def __len__(self):
        return len(self.transmittance)
    def load_files(self, file):
        self.name = file[:-4]
        self.file = file
        self.parse_file()

    def parse_file(self):
        with open(self.file, 'r') as f:
            conv = [int, float, float]
            reader = csv.reader(f)
            param = [con(next(reader)[0]) for con,i in zip(conv,range(3))]
            trash = [next(reader) for i in range(3)]
            self.wavenumber = np.linspace(param[1], param[2], int(param[0]))
            self.transmittance = [float(line[0]) for line in reader]

    def as_pandas(self):
        return pd.Series(data = self.transmittance, index = self.wavenumber)
    def as_dict(self):
        return {'wavenumber': self.wavenumber, 'transmittance': self.transmittance}
    def as_array(self):
        return np.array((self.wavenumber, self.transmittance))
        
def load_file(file):
    obj = Spectrum()
    obj.load_files(file)    
    return obj