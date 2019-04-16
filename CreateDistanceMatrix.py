###### using non-robust (ordinary) variance covariance matrix, percentile method #####
### note the robust variance covariance matrix could be estimated by https://scikit-learn.org/stable/modules/covariance.html#robust-covariance-estimation  ###
### you just need simply replace V by calling scikit-learn package ###

#### data is N by P matrix where N is the number of observations, and the P is the number of dimensions ###
V = np.cov(data.T)
VI = np.linalg.inv(V)

n = data.shape[0]
xxDist = np.zeros((n,n))-1

for i in range(n):
 	x1 = np.array(data[i,:],ndmin=2)
 	for j in range(i,n):

 		x2 = np.array(data[j,:],ndmin=2)
 		c = np.array(x2-x1,ndmin=2)
 		dist = float(1.0/ (1+np.dot(np.dot(c,VI),c.T)))

 		xxDist[i][j] = dist
 		xxDist[j][i] = dist
    
xxDist = np.array(xxDist)
