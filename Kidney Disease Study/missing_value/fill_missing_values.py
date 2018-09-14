# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 17:52:54 2018

@author: Yang
"""
# Import CategoricalImputer: inputs and outputs numpy array
from sklearn_pandas import CategoricalImputer

# Import pandas
import pandas as pd

# categorical_imputer
class Categorical_Imputer:
    """
    Imputing categorical data using the most frequent value
    """
    
    # instance attribute
    def __init__(self, strategy):
        self.strategy = strategy
        
    # instance method
    def fit_transform(self, df:'dataframe')->'dataframe':
        """
        Fill in missing categorical values using most frequent value
        """
        
        # instantiate CategoricalImputer
        imputer = CategoricalImputer()
        
        # convert array to dataframe
        df_filled = df.apply(lambda x: imputer.fit_transform(x), axis=0)
        
        # return filled dataframe
        return df_filled
        
        