# Problems within Reinforcement learning
- There are two fundamental problems in sequential decision making:
- The reinforcement learning problem
- The Planning Problem
- Reinforcement Learning and planning are linked but they are separate problem setups

# Reinforcement learning problem
- The environment is initially unknown, the agent is not told how the environment works
- Literally you drop the robot into the factory floor and tell it to get the most reward
- You don't know how the wind blows or how the factory operates
- The agent figures stuff out for itself
- The agent interacts with its environment and through that it improves its policy
- Trial and error learning
- It figures out the best way to behave in that environment to maximize its reward
- Example Learning Atari through reinforcement learning. The rules of the game are unknown, you learn directly from interactive gameplay. Pick actions on Joystick and see pixels and scores

# The planning problem
- Planning is deliberation, reasoning, thought, introspection, pondering, search
- A model of the environment is known
- This is exactly the environment you are working within
- It roughly knows the rules of the game before it even starts to do stuff
- Example it knows the dynamics of the wind if its an autonomous helicopter, it knows the differential equations describing the wind
- In planning the agent performs internal computations with its model (without external interactions) and the agent can improve its policy
- One way to do reinforcement learning is to learn how the environment works and then do the planning
- An example for the Atari game would be, the rules of the game are known, you can query the emulator. There is a perfect model inside the agent's brain. If I take action from a state s what would the next state be? What would the score b?
- Plan ahead to find the optimal policy, IE the search
- Look ahead planning
- Think ahead

# Explotations vs Exploration Concept
- Reinforcement learning is trial and error learning
- The agent should discover a good policy, for example, a pirate who wants to find a policy to get the most gold without losing too much reward along the way
- it can choose where to go based of its past experience from interacting with the environment things that the pirate already knows but the pirate also wants to make sure it is not giving up opportunities to explore things that it has discovered.
- We have to find a good balance between exploration and explotation
- Usually it's important to explore as well as also exploit

### Exploration
- Find more information about the environment

### Exploitation
- Exploit known information to maximize reward

### Examples of exploitation and exploration
- Restaurant selection
  - Exploration - Try a new restaurant at the risk you will eat something you don't like but you mind find something you like better than your current favorite restaurant
  - Exploitation - Just eat on restaurants you already tried and you already know that you like

- Online banner advertisement
  - Exploitation: Show the most successful advertisement, always
  - Exploration - see if people like this new advertisement

- Oil drill
  - Drill at the best known location
  - Explore new locations to drill

- Game playing
  - Play the move you believe is best
  - Play an experimental move, maybe it's more effective.


# Prediction and control
- Prediction: Evaluate the future, then give a policy, IE If I walk this way, how much reward will I get?
- Control: Optimize the future, find the best policy IE which direction should I go to get the most reward?
- Reinforcement learning - solve the prediction problem in order to solve the control problem

# Categorize RL Agents
- We can build a taxonomy now given the concepts of model, value, and policy
- We can taxonomize all of reinforcement learning according to these quantities, which of these three components the agent contains

## Value based, implicit policy
- value function if it only contains this
- look at the value vunction and pic the best action
- example earlier, the maze, we didn't need an explicit policy, we can just say hey the value of the state we end up in is better than we do this than the other values of the state we end up in when we do other actions

## Policy based (no value function)
## Actor-Critic - Policy + value function present
## Model free
- Policy and/or value function
- no model
- We do not try to explicity understand the environment, we do not try to understand how the helicopter moves, we don't explicitly figure out how the environment works

## Model-based
- first step is build up a model of the environment, of how the environment works
- then we plan for it, we do lookahead, what would be the policy and/or value function

