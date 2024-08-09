Skip to content
Navigation Menu
devjs2806
/
Prodigy_DS_05

Type / to search
Code
Issues
Pull requests
Actions
Projects
Security
Insights
BreadcrumbsProdigy_DS_05
/.py
Go to file
t
Latest commit
devjs2806
devjs2806
Add files via upload
e5cf162
 · 
yesterday
History
BreadcrumbsProdigy_DS_05
/.py
File metadata and controls

Code

Blame
35 lines (31 loc) · 1000 Bytes
import opendatasets as od
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as mn
import plotly.graph_objects as go
from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as ticker
import matplotlib.patches as mpatches
import matplotlib.patheffects as PathEffects
from plotly import graph_objs as pt_go
import plotly.express as px
import plotly.figure_factory as ff
from pylab import *
from nltk.corpus import stopwords
import geopandas as gpd
import geoplot
from geopy.geocoders import Nominatim
import warnings

# Ignore warnings
warnings.filterwarnings('ignore')

# Download the dataset
od.download("https://www.kaggle.com/sobhanmoosavi/us-accidents")

# Verify files downloaded
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Set matplotlib inline for Jupyter Notebooks
%matplotlib inline
Prodigy_DS_05/.py at main · devjs2806/Prodigy_DS_05 