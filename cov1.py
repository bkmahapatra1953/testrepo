#####calculate covariance in two ways
import numpy as np

#####first way
a = np.array([[2,3,5],[8,7,9],[5,8,7]])
print('original matrix = ',a)
meu = np.mean(a,axis=0)
print('mean = ',meu)
a_d = a - meu
print(a_d)
cov1 = np.dot(a_d.T,a_d) / a.shape[0]
print('covariance = ',cov1)

#########second way
cov2 = np.cov(a,rowvar=False,bias=True)
print('covariance using numpy = ',cov2)

######covariance using another formula
#cov3 = np.dot(a_d,a_d.T) / a.shape[0]
#print('covariance using another formula = ',cov3)
      


