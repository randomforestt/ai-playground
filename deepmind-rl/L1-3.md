# INSIDE AND RL AGENT
- Recap: We talked about the problem, we haven't talked about the solution.

### Policy
- The agents behavior function
### Value Function
- How good each state and/or action
### Model
- Agent's representation of the environment

```
Important, the list above (Policy, Value Function, Model)is not an exclusive list, they're not the only ones.
An RL agent may or may not include any or all of these
```

# Policy
- The agent's behavior function
- How the robot picks its action
- How it gets from its state to its decision about what action to take

# Value Function
- How good is it to be at a particular state
- How good is it to do a particular action
- How much reward do we expect to get if we take a particular action given that we are in a particular state

# Model
- An agent's representation of the environment
- How the agent thinks the environment works
- Not the reality of the environment but the agent's view of the environment.


```
Policy, value, model are not always required, but these are the pieces that may or may not be used
```

# Policy
- Agent's behavior
- Map from state to action

```
DETERMINISTIC POLICY

a = pi(s)

a - action
s - state
pi - policy function that spits out the action
to take given state
```

- The policy function `pi()` tells us how to get from some state `s` to some action `a` (decision which the agent takes)
- It's really literally the thing we care about
- We want to learn or develop this thing, the policy, we want to learn this from experience
- We want to learn a policy such that we get the most possible reward
- The brain we are trying to build is the thing that figures out this policy

```
STOCHASTIC POLICY

pi(a|s) = P(A = a | S = s)

the policy of an action given the state is equal to the probability of a better reward of the specific action given the specific state.

Useful! We can make random exploratory decisions on the state space.
```

# VALUE FUNCTION
- A prediction of future reward
- Used to evaluate the goodness / badness of states
- Why do we need this? If we need to choose between state 1 and state 2 or if we need to choose between action 1 and action 2, how do you choose between them?
- The basis of the value function is the expected future total reward to select between actions
- More formally,

```
Vpi(S) = Epi[ F | (St | s )]

where F = R(t) + gamma * R(t+1) + gamma_squared * R(t+2) + ... + gamma_raised_to_n * R(t+n)

F is the cumulative reward
gamma is the discount factor

Vpi(s) - the value function given state s on which the agent is behaving, so we subscript it given the policy

how much total reward we expect to get from some state onwards if we follow this particular behavior (policy)

Epi - expected cumulative discounted reward  given that state St as time t given curent s

```
#### THE DISCOUNT FACTOR GAMMA
- This is the mathematical formulation which means that we care more about immediate rewards than later rewards.


#### Value Functions Examples
- If I have a robot which is falling a lot, that robot will totally have a different reward compared to a robot who is standing up and walking effectively, so the amount of reward we get depends on the policy???
- Example: If I'm in a helicopter and I know I'm going to execute some particular trajectory how much reward will that trajectory get me? And if we can compare these things then we've got a basis where we can compare these decisions
- In summary, the value function is a helpful quantity for optimizing total behavior
- Example: For a specific Atari game, the actions we can take are only four. `Forward`, `Right`, `Left`, `No operation (NOP)`. We can plot a bar chart of the value (expected reward) vs operation (action)
- After getting a reward, the current possible future reward could go smaller or higher, because the previous received rewards don't matter, only the possible rewards moving forward. So if we plot the reward value vs time, it fluctuates.

#### COMMON QUESTIONS
- Is there a horizon on how far ahead we look? Given by the discount factor gamma
- How about Risk trade offs? The formalism of the reward is scalar how do we account for the risk in reward? One way is that the risk should already be factored in the reward, the behavior should correctly balance the risk.
- HOWEVER. There are risk-sensitive markov decision processes like for stock-trading which explicitly account for risks.
- BOTTOMLINE: You can bring risk in but you can also factor it in the reward. The reward can be designed such that the risk is already accounted for.

# MODEL
- Predicts what the environement will do next.
- The model is not the environment itself, but it is useful to predict the behavior of that environment to help make a plan of what to do next
- Sometimes it is useful to imagine what the environment might do
- Sometimes it is useful to try to learn the behavior the environment and use that model of the environment to help make a plan and help figure out what to do next
- Normally, the model has two parts: Transition model and reward model

## TRANSITION MODEL
- predicts the next state (IE Dynamics)

```
P(s, s', a) = P[S'=s' | S=s, A=a]

Probability of s' to be the next state
given the current state is s and the action we take is a
```
- What is the probability that we will end up at the next immediate state `s'` at the next immediate timestep given that we are currently in state `s` and that we will do action `a`
- TRANSISTION HELICOPTER EXAMPLE: If the helicopter is facing this way, in this position and in this angle and the wind is coming in a particular direction, then it is likely to more at position and at this angle if I accelerate by this much and turn by this much at the same time

## REWARD MODEL
- predicts the next immediate reward
- Immediate reward given that I'm currently in state `s` and I will do action `a`

```
R(a, s) = E[ R | S=s, A=a]

Expected reward R given the current state s and the action you will do next
```

- HELICOPTER EXAMPLE: How much reward do we get if the helicopter is in this situation, if we do something and it will not crash then it will get some x reward for staying alive or whatever else.

# MODEL
- It is optional to do this and a lot of the course will actually focus on `MODEL-FREE` methods that don't use a model at all. This is not a requirement, it is not necessary to explicitly build a model of the environment, but it is something that you can do.

# MAZE EXAMPLE

## This is a blank maze :)
- This is an example of a deterministic policy function
- If i'm in a particular state, do this, if i'm in a particular state go left

```
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+

Reward = -1 per timestep

Actions:
  ^      >      <    V
(North, East, South, West)
(up, right, down, left)

States: Agent's location
```

## NON-BLANK MAZE

```
       +---+---+---+---+---+---+---+---+
       | : | : | : | : | : | : | : | : |
       +---+---+---+---+---+---+---+---+
       | : |   |   |   |   |   |   | : |
       +---+---+---+---+---+---+---+---+
 START |   |   | : | : |   | : |   | : |
       +---+---+---+---+---+---+---+---+
       | : |   |   | : | : |   |   | : |
       +---+---+---+---+---+---+---+---+
       | : | : |   |   | : |   | : | : |
       +---+---+---+---+---+---+---+---+
       | : |   | : |   | : |   |   | : |
       +---+---+---+---+---+---+---+---+
       | : |   |   |   |   | : |   |   | GOAL
       +---+---+---+---+---+---+---+---+
       | : | : | : | : | : | : | : | : |
       +---+---+---+---+---+---+---+---+
```

## POLICY

- This is an example of a deterministic policy function
- If i'm in a particular state, do this, if i'm in a particular state go left


```

Arrow represents policy given state pi(s)

^  >     V    <
Up Right Down Left

       +---+---+---+---+---+---+---+---+
       | : | : | : | : | : | : | : | : |
       +---+---+---+---+---+---+---+---+
       | : | > | > | > | > | > | V | : |
       +---+---+---+---+---+---+---+---+
 START | > | ^ | : | : | ^ | : | V | : |
       +---+---+---+---+---+---+---+---+
       | : | ^ | < | : | : | V | < | : |
       +---+---+---+---+---+---+---+---+
       | : | : | ^ | < | : | V | : | : |
       +---+---+---+---+---+---+---+---+
       | : | V | : | ^ | : | > | V | : |
       +---+---+---+---+---+---+---+---+
       | : | > | > | ^ | < | : | > | > | GOAL
       +---+---+---+---+---+---+---+---+
       | : | : | : | : | : | : | : | : |
       +---+---+---+---+---+---+---+---+
```

## Value function
- The number in each location represents the value `Vpi(s)`

```
       +---+---+---+---+---+---+---+---+
       | : | : | : | : | : | : | : | : |
       +---+---+---+---+---+---+---+---+
       | : |-14|-13|-12|-11|-10| -9| : |
       +---+---+---+---+---+---+---+---+
 START |-16|-15| : | : |   | : | -8| : |
       +---+---+---+---+---+---+---+---+
       | : |-16|-17| : | : | -6| -7| : |
       +---+---+---+---+---+---+---+---+
       | : | : |-18|-19| : | -5| : | : |
       +---+---+---+---+---+---+---+---+
       | : |-24| : |-20| : | -4| -3| : |
       +---+---+---+---+---+---+---+---+
       | : |-23|-22|-21|-22| : | -2| -1| GOAL
       +---+---+---+---+---+---+---+---+
       | : | : | : | : | : | : | : | : |
       +---+---+---+---+---+---+---+---+
```

## Model
- Let's say the agent has seen one trajectory and moved around like this and then it reached the goal. It can try to build a model of how the environment works. You can think of it as trying to build its own map of the environment, and this map represents what it understood of its environment so far
as you move around
- The layout represents the transition model and for each location
the number represents the immediate reward `R(s, a)` from each pair of
state `s` and `a`.
- It is the agent's model of what immediate reward it gets for every step
- one step prediction
- in general you want to have a different immediate reward for each action though
- The model is not reality, it's just the agent's model of reality


```
           +---+---+---+---+---+---+
           | -1| -1| -1| -1| -1| -1|
       +---+---+---+---+---+---+---+
 START | -1| -1|       | -1|   | -1|
       +---+---+       +---+---+---+
           | -1|           | -1| -1|
           +---+           +---+---+
                           | -1|
                           +---+---+
                           | -1| -1|
                           +---+---+---+
                               | -1| -1| GOAL
                               +---+---+
```
