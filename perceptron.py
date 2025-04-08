import numpy as np 
import matplotlib.pyplot as plt 
import random as rd 

class Perceptron:
<<<<<<< HEAD

     def __init__(w,theta):
        self.w=np.array(L)
        self.theta=rd.randint(0,100)

    def step(z):
        return 1 if z>0 else 0
 
    def predict(x): 
=======
    def __init__(w,theta):
        self.w=np.array(L)
        self.theta=rd.randint(0,100)
    
    def step(z):
        return 1 if z>0 else 0

    def predict(x):
>>>>>>> 6cb6202684cf3ee8d8468eb03d37e828c251a9cd
        return step(np.matul(np.transpose(w),x)-theta) 
