import manim
from manim import *
import numpy as np

class graphs(Scene):
    def construct(self):
        #number plane to create graph
        numbergraph = NumberPlane()
        
        # self.play will play something for EX: create: create hass a pretty cool animation that creates the object from scratch
        #run_time is the amount of time it will be running
        self.play(Create(numbergraph),run_time=3)
        
        #Axes will put a number line in the origin if x_range and y_range isnt defined
        ax = Axes(x_length=12,y_length=6,axis_config={"include_numbers": True,'include_tip': True,"color":YELLOW})
        self.play(Create(ax))
        
        #plot a function
        #here i put an anonymous function
        graph = ax.plot(lambda x: (x**2))
        self.add(graph)
        self.wait(0.3)
        
        graph2 = ax.plot(lambda x: (x**2)-3)
        self.play(Transform(graph,graph2),rate_func = exponential_decay,run_time = 4)
        
        graph3 = ax.plot(lambda x: (x**1))
        self.play(Transform(graph,graph3),rate_func = exponential_decay,run_time = 4)

        graph4 = ax.plot(lambda x: int(np.exp(x)))
        self.play(Transform(graph,graph4),rate_func = exponential_decay,run_time = 4)
        
        graph4 = ax.plot(lambda x: int(x *100* (np.sin(x))))
        self.play(Transform(graph,graph4),rate_func = exponential_decay,run_time = 4)
        
        graph4 = ax.plot(lambda x: int(-x))
        self.play(Transform(graph,graph4),rate_func = exponential_decay,run_time = 4)
        #now plot the points before the line
        
        