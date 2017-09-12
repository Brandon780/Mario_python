import gym
import gym_pull
import random
import csv
#with open('mario_v2.csv', 'wb') as csvfile:
#spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

def move(x):
	r = random.randrange(2)
	if r == 0:
                return  [0, 0, 0, 1, 0, 1]  # Right + B
	
	if r == 1:
                return  [0, 0, 0, 0, 1, 0]  # Up

#gym_pull.pull('github.com/ppaquette/gym-super-mario')
env = gym.make('ppaquette/SuperMarioBros-1-1-v0')
for i_episode in range(100):
    observation = env.reset()
    while True:
	
        env.render()
	
        action = move(0) 
#env.action_space.sample()
	print action
        #[up,down,left,right,a,b]
        observation, reward, done, info = env.step(action)
        print  reward, done, info
        	 if info['distance'] > distance:
			print old_observation
                	print '---------------------------------------------------------'
			#spamwriter.writerow(numpy.append(old_observation, action))
                	distance = info['distance']
        if done:
            break
