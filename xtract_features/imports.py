# all import statements
import numpy as np
import pandas as pd
import pydicom as pyd
import os
import matplotlib.pyplot as plt
# import mudicom
import scipy
import pickle
import cv2
import math
import statistics
!pip install --upgrade scipy

!python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

!pip install pillow
!pip install python-resize-image
from resizeimage import resizeimage
!python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

!pip install pillow
!pip install python-resize-image
from resizeimage import resizeimage



from numpy import newaxis
from numpy import array
from os.path import dirname, join
# from pydicom.data import get_testdata_files
# from pydicom.filereader import read_dicomdir
from PIL import Image
from scipy.misc import *
from scipy.signal import convolve2d
from skimage.segmentation import slic, mark_boundaries, clear_border
from skimage.measure import label, regionprops
from skimage.filters import threshold_otsu
from skimage.morphology import closing, square
from skimage.color import label2rgb
from scipy import ndimage as ndi
from skimage.morphology import watershed
from skimage.feature import peak_local_max
from skimage.measure import shannon_entropy
from skimage import io, color, img_as_ubyte
from skimage.feature import greycomatrix, greycoprops
from sklearn.metrics.cluster import entropy
