#GLAS METRICS DESIRED:
#	(GLA14 ONLY) Date, Time, Campaign, Estimated Diameter, Saturation, Est. Slope, Ground Return Amplitude, Est Ground Elevation (GLAS), Est Ground Elevation (SRTM), Cloud Contaminated, Gaussian Fits to Waveform (1-6), Area under model alternate fit (MAF), (GLA01 necessary) raw waveform, Area under raw, Leading Edge Extent, Trailing Edge Extent, Full Extent, Noise Threshold

import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import h5py

#LIST GLA14 files at lapig
lapig.dir = 'DADOS01/RASTER/GLAS/'
LIST_GLA14 = [x for x in os.listdir(lapig.dir) if x.startswith('GLAH14')]
	file_name = LIST_GLA14[x]
	f = h5py.File(file_name, mode='r')
	
	UTCTime = f['/Data_40HZ/Time/d_UTCTime_40']
	ISOTime = UTCTime[:] + 946684800
	Date = []
	Time = []
	for x in range(0,len(ISOTime)):
		Date.append(datetime.datetime.fromtimestamp(UTCTime[x].strftime('%Y.%m.%d'))
		Time.append(datetime.datetime.fromtimestamp(UTCTime[x].strftime('%H:%M:%s'))
	
	latvar = f['/Data_40HZ/Geolocation/d_lat']
	latitude = latvar[:]
	lonvar = f['/Data_40HZ/Geolocation/d_lon']
	longitude = lonvar[:]
	
	#Flags for data cleaning: Clouds and Signal Saturation
	cloudF = f['/Data_40HZ/Atmosphere/FRir_qa_flg']
	CloudFlag = cloudf[:] # for future cleaning, no clouds = 15
	saturF = f['/Data_40HZ/Quality/sat_corr_flg']
	SatFlag = saturF[:] # for future cleaning, 0-1 ok (no sat or inconsequential)
	
	#Gaussians
	Gau_Amp = f['/Data_40HZ/Waveform/d_Gamp']
	Gau_A = Gau_Amp[:]
	Gau_Wid = f['/Data_40HZ/Waveform/d_Gsigma']
	Gau_w = Gau_Wid[:]
	Gau_CtrRng = f['/Data_40HZ/Elevation_Offsets/d_gpCntRngOff']
	Gau_CtrR = np.array(Gau_CtrRng[:])
	RefRng = f['/Data_40HZ/Elevation_Surfaces/d_refRng']
	RefRngRep = [RefRng[:]]*6 #repeat the array 6 times
	RefRngRep = np.transpose(RefRngRep) #transpose the repeated array
	Gau_CtrCorr = Gau_CtrR + RefRngRep #add the reference range to the gaussian center offsets to get the true range centers
	Gau_CtrCorr[Gau_CtrCorr>1000000] = np.nan #fills in non-valid values with nans
	
	#total waveform area - use precalculated gaussian areas, sum
	Gau_Areaf = f['/Data_40HZ/Waveform/d_Garea']
	Gau_Area = Gau_Areaf[:]
	Gau_Area[Gau_Area>1.0e6]=0
	Gau_Sum = np.sum(Gau_Area,axis=1)
	
	#SRTM and GLAS Elevation Estimates
	GLAS_E = f['/Data_40HZ/Elevation_Surfaces/d_elev']
	GLAS_Elev = GLAS_E[:]
	SRTM_E = f['/Data_40HZ/Geophysical/d_DEM_elv']
	SRTM_Elev = SRTM_E[:]
	
	#LINK RECORD TO GLA01
	#create unique identifier joining i_rec_ndx and i_shot_count
	ndx = f['/Data_40HZ/Time/i_rec_ndx']
	cnt = f['/Data_40HZ/Time/i_shot_count']
	iden = #turn into a unique string identifier??? or just match both
	
	

