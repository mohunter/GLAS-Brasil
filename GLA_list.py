import os

import matplotlib as mpl
import matplotlib.pyplot as ply
import numpy as np
import h5py

### GOAL: LIST waveform files necessary to match to GLAH14 records within a bounding box

#List of GLAH14 files in a given directory (imagine that this will be on LAPIG machines

#lapig_dir = 'DADOS01/RASTER/GLAS/'

#LIST_GLA14 = [x for x in os.listdir(lapig_dir) if x.endswith(".H5")]
#	print(LIST_GLA14)
#	file_name = LIST_GLA14[x]
#	f = h5py.File(file_name, mode='r'

#GET HDF FILES USED TO CREATE GLA14 File
	# There is 1 GLA01 file per GLA05 File, with the same naming convention. This way the list from GLA14 can be used to cull both GLA05 and GLA01 files
Inputs_var = f['/METADATA/PROVENANCE/STEP_1/ProcessInput']
Inputs_str = Inputs_var.attrs['Name'].split(',')
Inputs_GLA = []
Waveforms_GLA01 = []
for x in range(0,len(Inputs_str)):
	if Inputs_str[x].startswith('GLA05'):
		#correct file name from .dat to .h5 version currently available
		Inputs_GLA.append('GLAH'+Inputs_str[x][3:-3]+'H5')
		Waveforms_GLA01.append('GLAH01_033'+Inputs_str[x][9:-11]+'*.H5'
			#this statement removes the granule version number and allows for multi-file granules and corrects for the hdf5 format both in the name and file type

latvar = f['/Data_40HZ/Geolocation/d_lat']
            latitude = latvar[:]
            lat_vr = [latvar.attrs['valid_min'], latvar.attrs['valid_max']]

#find dates for each file
UTCTime = f['/Data_40HZ/Time/d_UTCTime_40']
UTCTimeF = UTCTime[1]
UTCTimeL = UTCTime[-1]

#correct time to isotime (1970 start)
ISOTime = UTCTime[:] + 946684800

#define Day
Day = []

#get dates for all items
for x in range(0,len(ISOTime)):
	Day.append(datetime.datetime.fromtimestamp(UTCTime[x].strftime('%Y.%m.%d'))

#get Gaussian parameters for each waveform
Gau_Amp = f['/Data_40HZ/Waveform/d_Gamp']
Gau_Wid = f['/Data_40HZ/Waveform/d_Gsigma']
Gau_CtrRng = f['/Data_40HZ/Elevation_Offsets/d_gpCntRngOff']
RefRng = f['/Data_40HZ/Elevation_Surfaces/d_refRng']




#make list of filenames with datepath
#import urllib2
#wf_list = []
#url_base = 'https://n5eil01u.ecs.nsidc.org/GLAS/GLAH01.033/'
#for x in range(0,len(ISOTime)):
	
	
