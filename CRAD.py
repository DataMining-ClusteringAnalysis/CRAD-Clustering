import os
import sys
sys.setrecursionlimit(100000)
import numpy as np
from scipy.spatial.distance import cdist
import pandas as pd
from sklearn.metrics import f1_score
from sklearn.metrics import adjusted_rand_score
from sklearn.metrics.cluster import adjusted_mutual_info_score
from sklearn.metrics import pairwise_distances
from sklearn.metrics import silhouette_score
from sklearn.metrics import calinski_harabaz_score
import math
from sklearn.metrics.pairwise import euclidean_distances
import itertools
from sklearn import preprocessing
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.cluster import KMeans

# An Automatic Self-Searching Algorithm of CRAD
def _hist_find_new(l, MAX_STEP, n_bin):
    
    srch,perctl = np.histogram(l, bins=n_bin)
    
    for i in np.arange(len(srch)-1-MAX_STEP,MAX_STEP+1,-1):
        
        tmp_bool = []
        for step in range(1, MAX_STEP+1):
            #if srch[i] < srch[i+step] and srch[i-1] < srch[i+step] and max(srch[i], srch[i-1]) <= srch[i+step]*(1-stepness): 
            #if srch[i] < srch[i-step] and srch[i] < srch[i+step]:# and (srch[i] <= srch[i-step-1] or srch[i] <= srch[i-step-2]):
            if srch[i] < srch[i-step] and srch[i] < srch[i+step]:# and (srch[i] <= srch[i-step-1] or srch[i] <= srch[i-step-2]):
                tmp_bool.append(True)
            else:
                tmp_bool.append(False)
                
        tmp_bool = np.array(tmp_bool)
        num_ = np.where(tmp_bool == True)[0].tolist()

        if len(num_) == MAX_STEP:

            slope = float(srch[i+MAX_STEP] - srch[i])#/float(perctl[1] - perctl[0])
            key_perctl = perctl[i]
            break
    
    
    idx = np.where(l > key_perctl)[0].tolist()
    return idx

# calculate adjacency matrix
def cal_adjM_cutOff(xxDist, MAX_STEP, num_bin):

    adj = []
    for k in range(xxDist.shape[0]):

        temp = [k]
        
        l = np.array(xxDist[k,])
        
        idx = _hist_find_new(l, MAX_STEP, num_bin)  
        #idx = np.where(l > key_perctl)[0].tolist()
        
        if k in idx:
            idx.remove(k)

        temp.extend(idx)

        adj.append(temp)
        
    return adj



# original method - DBCA
#def cal_adj_M_orig(xxDist, theta):

#    adj = []
#    for k in range(xxDist.shape[0]):
#        temp = [k]
#        l = pd.DataFrame(np.array(xxDist[k,]))
#        idx = np.where(l > theta)[0].tolist()
#        if k in idx:
#            idx.remove(k)
#        temp.extend(idx)
#        adj.append(temp)       
#    return adj




def dfs(n, cl, adj, label):

	if cl[n] == -1:

		cl[n] = label

		if len(adj[n])-1 !=0:
			
			for j in range(1, len(adj[n])):

				dfs(adj[n][j], cl, adj, label)

	return
# clustering algorithm CRAD
def clustering_(data,adj):
    n = data.shape[0]
    cl = [-1]*n
    label = 0

    for i in range(n):

        if cl[i] == -1:


            if len(adj[i]) == 1:
                cl[i] = 0

            else:

                label = label+1
                dfs(i, cl, adj, label)
                
    return cl
