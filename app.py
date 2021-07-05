# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 12:40:54 2021

@author: aspdiscovery
"""

from flask import Flask,request

import joblib

model=joblib.load(r'ccpp-model.pkl')

app=Flask(__name__)

@app.route('/',methods=['POST'])
                        
def abcd():
    data=request.get_json(force=True)
    data=data['test']
    output=model.predict(data)
    return str(output)
                       
               
                        
                        
                        
                        