from .spectrum import Spectrum, load_file
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import csv

class Spectra(Spectrum):
    def __init__(self):
        super().__init__()
        self.index  = []
        self.columns = {}
        self.spectra_list = 0
        self.name_list = None
    def __iter__(self):
        return self.spectra_list.__iter__()
    def __len__(self):
        return len(self.spectra_list)
    
    def rename(self, ft):
        for sp, name in zip(self.spectra_list, self. name_list):
            sp.name = name[:-len(ft)] 
        
	def import_obj(self,object, ft = '.asp'):
		if type(object) == str:
			file_list = [file for file in os.listdir(object) if ft in file[-len(ft):]]
			path_list = [os.path.join(object, file) for file in file_list ]
			self.name_list = file_list.copy()
			self.spectra_list = [load_file(file) for file in path_list]
			self.rename(ft = ft)
		elif type(object) == list:
			if type(object[0]) == Spectrum:
				self.spectra_list=object
			else:
				self.spectra_list = [load_file(file) for file in file_list if ft in file[-len(ft):]]
		


		self.columns =  {sp.name:sp.transmittance for sp in self.spectra_list}
        self.index = np.array(self.spectra_list[0].wavenumber)
        
	@property
	def as_pandas(self):
		return pd.DataFrame(data = self.columns, index = self.index)
	def plot(self, filename=None, figsize=(12,8), plt_style="ggplot", xinterval=(4000,650)):
		plt.style.use(plt_style)
		df=self.as_pandas
		fig,ax=plt.subplots(1,1, figsize=figsize)
		for column in df:
			ax.plot(df.index, df[column], label=column)
		plt.xlim(xinterval)

    def as_array(self):
        return np.array(self.index, self.columns)
    def as_dict(self):
        full_dict = self.columns.copy()
        full_dict['wavenumber'] = self.index
        return full_dict
    def export_csv(self, filename):
        self.as_pandas().to_csv(filename + '.csv')
    
        
def load_dir(object):
    obj_sa = Spectra()
    obj_sa.import_obj(object)
    return obj_sa
