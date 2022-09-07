# Importing the packages
import gym
print(gym.__version__)

# Creating the environment
ics_env = gym.make('CartPole-v1')

# Getting the action space
print(f'Action space {ics_env.action_space}')

# Getting the observation space
print(f'Observation space {ics_env.observation_space}')

# Running the episodes; 170
for episode in range(1, 171):
    score = 0                   # Initialising the score
    state = ics_env.reset()     # Resetting the environment
    done = False                # Setting done to false

    # While loop to run until done = True
    while not done:
        ics_env.render()    # Render environment using pyGame
        action = ics_env.action_space.sample()  # Selecting a random action from the action space
        n_state, reward, done, info = ics_env.step(action)  # Get the next state
        score += reward # Add the reward to the score

    print(f'Episode: {episode}, Score: {score}')    # Printing the episode and the score

# Closing the environment
ics_env.close()
