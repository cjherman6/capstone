import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances,cosine_similarity

df = pd.read_csv('app_data/breed_traits.csv',index_col='Unnamed: 0')

def overall_recommender(breed,dist='euclidean'):
    '''
    Input: Name of breed (string)
    Output: 5 Breeds with most similar temperaments according to dogtime.com ratings
    '''
    y = df.loc[[breed],:]
    euc_dists = euclidean_distances(df.values,y.values)
    euc_ind = np.argsort(euc_dists.flatten())
    cos_dists = cosine_similarity(df.values,y.values)
    cos_ind = np.argsort(cos_dists.flatten())
    if dist == 'euclidean':
        return [df.iloc[ind,:].name for ind in euc_ind][1:6]
    elif dist == 'cosine':
        return [df.iloc[ind,:].name for ind in cos_ind][1:6]

def predictions_recommender(breed,photo_list,dist='euclidean'):
    '''
    Input: Name of breed (string), List of dogs you're considering (list)
    Output: Ordered list starting from most similar to least
    '''
    y = df.loc[[breed],:]
    X = df.loc[photo_list,:]
    euc_dists = euclidean_distances(X.values,y.values)
    euc_ind = np.argsort(euc_dists.flatten())
    cos_dists = cosine_similarity(X.values,y.values)
    cos_ind = np.argsort(cos_dists.flatten())
    if dist == 'euclidean':
        return [X.iloc[ind,:].name for ind in euc_ind]
    elif dist == 'cosine':
        return [X.iloc[ind,:].name for ind in cos_ind]
