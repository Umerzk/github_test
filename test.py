import gym

env = gym.make('CartPole-v1')
observation = env.reset()

for _ in range(1000):
    env.render()  # No need to specify the render mode
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)

    if done:
        observation = env.reset()

env.close()