# -*- coding: utf-8 -*-
"""
@author: Sarah
"""

import pandas as pd
import numpy as np
from sklearn.metrics import pairwise_distances

class DistanceMatrixClass:
    def __init__(self, data, user_col, total_users):
        """
        Class to preform matrix calculations
        :param data: data to initalise class
        :param user_col: user column
        :param total_users: all users to create memory rating matrixs
        """
        self.data = data
        self.user_col = user_col
        self.total_users  = total_users
        
    def missing_users(self, data):
        """
        Missing_Users

        Takes a DataFrame and adds columns so complete with all users in memory of rating matrix

        Parameters
        ----------
        data : DataFrame
            DataFrame with incomplete users
        Returns
        -------
        data_full: DataFrame
            DataFrame with complete users sorted

        """
        current_users = np.array(data[self.user_col])
        missing_users = list(set(self.total_users) - set(current_users))
        print(len(missing_users))
        columns = [self.user_col]
        new_data = pd.DataFrame(pd.Series(missing_users))
        new_data.columns = columns
        data_full = pd.concat([data, new_data])
        return data_full
    
    def frametoratingmatrix(self, cols_to_drop, col_to_agg, agg_fun):
        """
        Frame_to_ratin_matrix

        Takes a DataFrame and turns it into a rating matrix by grouping byy a column,
        and summarizing with a aggregation function

         Parameters
         ----------
         cols_to_drop : List of column names
             Columns to drop, only want group by and aggregate column
         col_to_agg: String of column name
            column to pivot on
         agg_fun: Function
            function to aggregate on


         Returns
         -------
         data: DataFrame
             dataframe sorted as rating matrix

        """
        data = self.data.drop(cols_to_drop, axis =1)
        data_p = pd.pivot_table(data, index=self.user_col, columns=[col_to_agg], aggfunc=agg_fun)
        data = pd.DataFrame(data_p.to_records())
        data = self.missing_users(data)
        data = data.sort_values(by=[self.user_col])
        data = data.fillna(0)
        return data
        
    def calculate_similarity(self, rating_matrix):
        """
        Calculate_Similarity
        Takes a dataframe rating matrix and returns cosine similarity matrix

        Parameters
        ----------
        rating_matrix : DataFrame
           DataFrame as rating matrix
        Returns
        -------
        cos_matrix: Matrix
           Matrix of  Pairwise Cosine Similarity

        """
        users = rating_matrix[self.user_col].tolist()
        rating_matrix = rating_matrix.drop([self.user_col], axis=1)
        cos_matrix = 1 - pairwise_distances(rating_matrix.as_matrix(), metric="cosine" )
        np.fill_diagonal(cos_matrix, 0)

        cos_matrix[cos_matrix == 0] = 'nan'
        # cos_df = pd.DataFrame(cos_matrix)
        # cos_df.columns = users
        # cos_df.columns = cos_df.columns.map(str)
        # new_data = pd.DataFrame(pd.Series(users))
        # new_data.columns = [self.user_col]
        # cos_df = pd.concat([new_data, cos_df])
        return cos_matrix




        
        
        

