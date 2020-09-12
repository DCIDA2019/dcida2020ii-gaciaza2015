# -*- coding: utf-8 -*-
import pandas as pd
import requests

url = "https://idconline.mx/laboral/salarios-minimos/salarios-minimos-1986-2007"
html = requests.get(url).content
df_list = pd.read_html(html, header = 1)
print(df_list)