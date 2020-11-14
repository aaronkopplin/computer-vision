from skimage.io import imread
from matplotlib import pyplot as plt
import numpy as np

# read in the image as greyscale
image = imread('mountain.jpeg', as_gray=True)

# convert the image to a 1D array of greyscale values
pixel_array = np.array(image.flatten())

# set up 100 bins, each are .1 wide
bins = [i/100 for i in range(100)]

# configure the histogram window dimensions
figure, axes = plt.subplots(figsize=(10, 7))

# load the data to the histogram
axes.hist(pixel_array, bins=bins)

# display the histogram
plt.show()