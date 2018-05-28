# -*- coding: utf-8 -*-
"""
Created on Sun May 27 20:37:38 2018

@author: Sarah
"""

import pandas as pd
import numpy as np
from sklearn.metrics import pairwise_distances

class DistanceMatrixClass:
    def __init__(self, data, user_col, total_users):
        self.data = data
        self.user_col = user_col
        self.total_users  = total_users
        
    def missing_users(self):
        current_users =  np.array(self.data[self.user_col])
        missing_users = list(set(self.total_users) - set(current_users))
        print(len(missing_users))
        columns = [self.user_col]
        new_data =  pd.DataFrame(pd.Series(missing_users))
        new_data.columns = columns
        data_full = pd.concat([self.data,new_data])
        return(data_full)
    
    def frametoratingmatrix(self,cols_to_drop, col_to_agg, agg_fun):
        data = self.data.drop([cols_to_drop], axis =1)
        data = pd.pivot_table(data, index=self.user_col, columns=[col_to_agg], aggfunc=agg_fun)
        data =  pd.DataFrame(data.to_records())
        data = self.missing_users()
        data = data.fillna(0)
        return(data)
        
    def calculate_similarity(self, rating_matrix):
        users =  rating_matrix[self.user_col].tolist()
        rating_matrix =  rating_matrix.drop([self.user_col], axis =1)
        cos_matrix = 1 - pairwise_distances( rating_matrix.as_matrix(), metric="cosine" )
        np.fill_diagonal( cos_matrix, 0 )
        cos_df = pd.DataFrame( cos_matrix )
        cos_df.columns = users
        cos_df.columns = cos_df.columns.astype(str)
        cos_df[self.user_col] = pd.Series(users)
        cos_df = pd.as_matrix(cos_df)
        cos_df[cos_df == 0] = 'nan'
        return cos_df


    def join_similarities(self, matrix_list):
        matrix_mean = np.nanmean(matrix_list)
        return(matrix_mean)

        
        
        

