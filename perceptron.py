import numpy as np 
import matplotlib.pyplot as plt 
import random as rd 

class Perceptron:

     def __init__(w,theta):
        self.w=np.array(L)
        self.theta=rd.randint(0,100)

    def step(z):
        return 1 if z>0 else 0
 
    def predict(x): 
        return step(np.matul(np.transpose(w),x)-theta) 
