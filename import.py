#Mengimport library dan data yang akan digunakan
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap


data = pd.read_csv("crime.csv",encoding='latin-1')

