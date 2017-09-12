import gym
import numpy
import csv
import gym_pull
from random import randint
with open('mario_v2.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    entrada = csv.reader(csvfile)
    #spamwriter = csv.writer(csvfile, delimiter=',')
    for reg in range(1000):
	env = gym.make('ppaquette/SuperMarioBros-1-1-v0')
        observation = env.reset()
        distance=0
	i = 0
        while True:
            env.render()
            #action = env.action_space.sample()
	    
	    
	    compa = csvfile.readline()[-1]
	    
	    if(len(compa)==0):
		action = numpy.random.randint(2, size=6)
	    else:
		action = compa
               
            print action
            old_observation = observation
            observation, reward, done, info = env.step(action)
	    if info['distance'] <= distance:
	    	i = i + 1
            if info['distance'] > distance:
		#print old_observation
                print '---------------------------------------------------------'
		print info['distance']
		spamwriter.writerow(action)
                distance = info['distance']
	    if i >= 100:	
			break 
            if done:
                break
