import numpy as np
import gym


env = gym.make('CartPole-v1')
env.reset()

for _ in range(1000):
    action = env.action_space.sample()
    env.step(action)
    env.render()  # No need to specify the render mode
