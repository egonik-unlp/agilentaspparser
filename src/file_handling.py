from .spectra import Spectra, load_dir
from .spectrum import Spectrum, load_file
import numpy as np
import os
def load_all_files(object):
	try:
		spectra_=load_dir(object)
		_=spectra_.as_pandas
	except ValueError:
		print("Since spectra were registered with different precisions, a list of spectra will be returned")
		if type(object)==list:
			bunch=[load_file(file) for file in object]
		elif type(object)==str:
			bunch=[load_file(file) for file in os.listdir(object)]
		else:
			print("Bad syntax")
		shapes={spectrum.wavenumber.shape[0] for spectrum in bunch}
		rv={shape:[] for shape in shapes}
		for file in bunch:
			rv[file.wavenumber.shape[0]].append(file)
		spectra_=list(rv.values())
	
		
