import gym

env = gym.make("CartPole-v1")
env.reset()

for _ in range(1000):
    env.render()
    action = env.action_space.sample()
    env.step(action)

env.close()
