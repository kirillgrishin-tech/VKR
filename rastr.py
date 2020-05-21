import rasterio
from rasterio import plot
import matplotlib.pyplot as plt
import numpy as np

def Rastr(b4,b5,mini,maxi):
    np.seterr(divide='ignore', invalid='ignore')
    band4 = rasterio.open(b4) 
    band5 = rasterio.open(b5)
    band4.height
    band4.width
    band4.dtypes[0]
    band4.crs
    band4.transform
    band4.read(1)
    red = band4.read(1).astype('float64')
    nir = band5.read(1).astype('float64')
    ndvi=np.where(
        (nir+red)==0., 
        0, 
        (nir-red)/(nir+red))
    for i in range(len(ndvi)):
        for t in range(len(ndvi[i])):
            ndvi[i][t] = -ndvi[i][t]
            if ndvi[i][t] < mini or ndvi[i][t] > maxi:
                ndvi[i][t]= None
    ndviImage = rasterio.open('NDVI.tiff','w',driver='Gtiff',
                            width=band4.width, 
                            height = band4.height, 
                            count=1, crs=band4.crs, 
                            transform=band4.transform, 
                            dtype='float64')
    ndviImage.write(ndvi,1)
    ndviImage.close()
    ndvi = rasterio.open('NDVI.tiff')
    plot.show(ndvi)