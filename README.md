## CRAD-Clustering
Python implementation of CRAD clustering algorithm (CRAD.py) and extended DBSCAN algorithm using CRAD framework (ExtensionToDBSCAN.py).

## Setup

`python setup.py install`

## Documentation

For CRAD-Clustering:

Call the function cal_adjM_cutOff(xxDist, StepSize, Nbin) to calculate adjancey matrix
where 
Inputs:
xxDist - A distance matrix using robust mahalanobis distance 
StepSize - Maximum steps of neighborhood you check in histogram to find optimal cut-off parameter
Nbin - Number of bin in histogram to find optimal cut-off parameter
Outputs:
An adjancey matrix
Then you can call function clustering_(data, adj) to get clustering result
where 
Inputs:
data - A m by n matrix where m corresponds to number of observations, and n corresponds to number of features.
adj - An adjancey matrix which is calculated in above step.
Output:
An array with either a cluster id number.


For Extended DBSCAN:

Call the function dbscan_newM(xxDist, StepSize, Nbin, min_points)
Inputs:
xxDist - A distance matrix using robust mahalanobis distance 
StepSize - Maximum steps of neighborhood you check in histogram to find optimal cut-off parameter
Nbin - Number of bin in histogram to find optimal cut-off parameter
min_points - The minimum number of points to make a cluster
Outputs:
An array with either a cluster id number.
