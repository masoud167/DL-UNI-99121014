import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Read RGB image
rgb = mpimg.imread("input.jpg.jpg")  # use a small sample RGB image

# Ensure it's in float format [0,1]
if rgb.dtype != np.float32 and rgb.max() > 1.0:
    rgb = rgb / 255.0

# Manual grayscale conversion using luminosity method
grayscale = 0.299 * rgb[:, :, 0] + 0.587 * rgb[:, :, 1] + 0.114 * rgb[:, :, 2]

# Save grayscale
plt.imsave("grayscale.png", grayscale, cmap='gray')
