# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/04_Block_Diagrams.ipynb.

# %% auto 0
__all__ = ['SimplerCar']

# %% ../nbs/04_Block_Diagrams.ipynb 3
import numpy as np
import matplotlib.pyplot as plt

# %% ../nbs/04_Block_Diagrams.ipynb 72
class SimplerCar:
    _g = 9.8
    
    def __init__(self, x0, params):
        self._x_1 = x0[0] # position (along the road)
        self._x_2 = x0[1] # velocity
        self._m, self._alpha, self._beta, self._gamma = params
        
    def step(self, dt, u, theta):
        self.theta = theta
        self._x_1 = self._x_1 + dt*self._x_2
        self._x_2 = self._x_2 + dt*(- self._beta/self._m*self._x_2 + \
                                    self._gamma/self._m*u - Car._g*np.sin(theta))
        
    def speedometer(self):        
        v = self._x_2
        return (v,)
