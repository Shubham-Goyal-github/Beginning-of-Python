# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 22:07:10 2021

@author: NITESH
"""

import numpy as np
class NeuralNetwork():
    def __init__(self):
        np.random.seed(1)
        self.synaptic_weights=2*np.random.random((3,1))-1
    def sigmoid(self,x):
        return 1/(1+np.exp(-x))
    def sigmoid_derivative(self,x):
        return x*(1-x)
    def train(self,training_inputs,training_outputs,training_iterations):
        for iteration in range(training_iterations):
            output=self.think(training_inputs)
            error=training_outputs-output
            adjustments=np.dot(training_inputs.T,error*self.sigmoid_derivative(output))
            self.synaptic_weights+=adjustments
    def think(self,inputs):
        inputs=inputs.astype(float)
        output=self.sigmoid(np.dot(inputs,self.synaptic_weights))
        return output
if __name__=="__main__":
    neural_network=NeuralNetwork()
    print("random generated weight:")
    print(neural_network.synaptic_weights)
    training_inputs=np.array([[0,0,1],
                              [1,1,1],
                              [1,0,1],
                              [0,1,1]])
    training_outputs=np.array([[0,1,1,0]]).T
    neural_network.train(training_inputs,training_outputs,15000)
    print("ending weight")
    print(neural_network.synaptic_weights)
    user_input_one=str(input("user input one"))
    user_input_two=str(input("user input two"))
    user_input_three=str(input("user input Three:"))
    print(user_input_one,user_input_two,user_input_three)
    print("new output")
    print(neural_network.think(np.array([user_input_one,user_input_two,user_input_three])))
    print("we did it")
    
    