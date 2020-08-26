# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 16:37:19 2020

@author: gasati
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())