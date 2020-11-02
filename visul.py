from skimage import io
 
img = io.imread('testimg.tif')
 
import numpy as np
 
data=np.random.random([100,100])
 
io.imsave('rand_data.tif',np.float32(data))
