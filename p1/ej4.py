import numpy as np
import functions 


dt = 1e-2
t = np.arange(-1,1,dt)
x = functions.rect_array(t,(-0.25,0.25))

functions.plot([(-2,2),(-0.5,3.5)],'t','Amplitud','Grafico de la SVIC','Grafico de la SVIC',25,'red',1.5,t,x)
