import gym
print(gym.__version__)

ics_env = gym.make('CartPole-v1')
# print(ics_env.action_space)

for episode in range(1, 171):
    score = 0
    state = ics_env.reset()
    done = False

    while not done:
        ics_env.render()
        action = ics_env.action_space.sample()
        n_state, reward, done, info = ics_env.step(action)
        score += reward

    print(f'Episode: {episode}, Score: {score}')

ics_env.close()
