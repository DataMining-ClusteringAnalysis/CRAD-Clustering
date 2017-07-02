import os
import sys
sys.setrecursionlimit(100000)
import numpy as np
import math
import pandas as pd

#Extension to DBSCAN by using CARD clustering algorithm framework
UNCLASSIFIED = False
NOISE = 0

def _region_query_cutOff(xxDist, point_id, MAX_STEP, n_bin):
    
    l = pd.DataFrame(np.array(xxDist[point_id,]))

    idx = _hist_find_new(l, MAX_STEP, n_bin)

    if point_id in idx:
        idx.remove(point_id)
        
    return idx


def _expand_cluster(xxDist, classifications, point_id, cluster_id, MAX_STEP, n_bin, min_points):
    seeds = _region_query_cutOff(xxDist, point_id, MAX_STEP, n_bin)
    if len(seeds) < min_points:
        classifications[point_id] = NOISE
        return False
    else:
        classifications[point_id] = cluster_id
        for seed_id in seeds:
            classifications[seed_id] = cluster_id
            
        while len(seeds) > 0:
            current_point = seeds[0]
            results = _region_query_cutOff(xxDist, current_point, MAX_STEP, n_bin)
            if len(results) >= min_points:
                for i in range(0, len(results)):
                    result_point = results[i]
                    if classifications[result_point] == UNCLASSIFIED or \
                       classifications[result_point] == NOISE:
                        if classifications[result_point] == UNCLASSIFIED:
                            seeds.append(result_point)
                        classifications[result_point] = cluster_id
            seeds = seeds[1:]
        return True
        
def dbscan_newM(xxDist, StepSize, Nbin, min_points):
    
    cluster_id = 1
    n_points = xxDist.shape[0]
    classifications = [UNCLASSIFIED] * n_points
    for point_id in range(0, n_points):
        #point = m[:,point_id]
        if classifications[point_id] == UNCLASSIFIED:
            if _expand_cluster(xxDist, classifications, point_id, cluster_id, StepSize, Nbin, min_points):
                cluster_id = cluster_id + 1
    return classifications



'''
To perform externsion of DBSCAN, simply call the function dbscan_newM(xxDist, StepSize, Nbin, min_points)

Inputs:
xxDist - A distance matrix using robust mahalanobis distance 
StepSize - Maximum steps of neighborhood you check in histogram to find optimal cut-off parameter
Nbin - Number of bin in histogram to find optimal cut-off parameter
min_points - The minimum number of points to make a cluster

Outputs:
An array with either a cluster id number.
'''
