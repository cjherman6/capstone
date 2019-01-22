import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances,cosine_similarity

df = pd.read_csv('app_data/breed_traits.csv',index_col='Unnamed: 0')

def profile_recommender(profile,breed_list,dist='cosine'):
    '''
    Input: Profile created from radio inputs (np array)
    Output: 5 Breeds with most similar temperaments according to dogtime.com ratings
    '''
    y = profile
    X = df.loc[breed_list,:]
    euc_dists = euclidean_distances(X.values,y)
    euc_ind = np.argsort(euc_dists.flatten())
    cos_dists = cosine_similarity(X.values,y)
    cos_ind = np.argsort(cos_dists.flatten())
    if dist == 'euclidean':
        return [X.iloc[ind,:].name for ind in euc_ind]
    elif dist == 'cosine':
        return [X.iloc[ind,:].name for ind in cos_ind][::-1]

def initial_profile():
    return df.describe().T['mean'].values

def rec_page_output(profile,breeds,predictions):
    recommendations = profile_recommender(profile,breeds)
    image_loc= [predictions[recommendation] for recommendation in recommendations]
    recommendations = [' '.join(recommendation.split('-')) for recommendation in recommendations]
    rank = list(np.arange(len(recommendations))+1)
    return rank, recommendations, image_loc

def overall_recommender(profile,dist='cosine'):
    '''
    Input: Name of breed (string)
    Output: 5 Breeds with most similar temperaments according to dogtime.com ratings
    '''
    y = profile
    euc_dists = euclidean_distances(df.values,y)
    euc_ind = np.argsort(euc_dists.flatten())
    cos_dists = cosine_similarity(df.values,y)
    cos_ind = np.argsort(cos_dists.flatten())
    if dist == 'euclidean':
        return [df.iloc[ind,:].name for ind in euc_ind][1:6]
    elif dist == 'cosine':
        return [df.iloc[ind,:].name for ind in cos_ind][-1:-6:-1]
