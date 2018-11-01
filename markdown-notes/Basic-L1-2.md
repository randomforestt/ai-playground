# Lecture 1: Introduction Part 2
- Work in progress

## SUMMARY
- Interaction of agent and environment
- History
- State
  - Agent State
  - Environment State
  - Information State  
- Markov Property
- Environment state vs Agent state
- Observability

## The agent and its environment
```
           ---------
|--------> | BRAIN | ------>----|
|          ---------            |
^              ^                ^
|              |                |
----          -----             ---
SENSOR        REWARD            ACTUATION
----          ------            ---
|              ^                |
|              |                |
^         ---------------       v
|----<----| Environment | <-----|
          ---------------
```
- Brain (of agent) makes decisions
  - which evaluates which is the best action to take
- And then performs an action (by the actuator)

- The brain perceives the reward
from its environment, (how well is it doing?)

- The brain also observes the Environment
by using a sensor like a camera

- Take note that the actuation or action
may not be perfectly executed and the  
sensing or observation might also not
be totally perfect


### Agent (brain)
- At each step (A loop)
  - Executes an action `At`
  - Receives an observation `Ot`
  - Received a reward `Rt`

### Environment
- Receives an action `At`
- Emits an observation `Ot`
- Emits a scalar reward `Rt`


```
We influence the environment based on the action we take.

Essentially:
There is (ENDLESS??) INTERACTION between agent and environment
```

- A robot can move around and it can influence not only where it is in the environment, but also where the objects are in the environment if it pushes things around.

- Why is the reward scalar? Is a vector reward possible? Different sets of goals for example. For simplicity, we can use weights. Place different weights different goals depending on how important they are and add them together to get a scalar reward.

# HISTORY AND STATE

# The history

- The history is a sequence of observations, actions and rewards.

```
Ht = A1, O1, R1, A2, O2, R2... At, Ot, Rt

A - action
O - observation
R - Reward
```

- All observable variables from the beginning
to  time `t`

- Observation: Sensory motor stream of a robot or embodied agent

```
WHAT HAPPENS NEXT DEPENDS ON HISTORY

THE HISTORY DETERMINES WHAT HAPPENS NEXT

THE HISTORY DETERMINES LITERALLY THE NATURE OF
HOW THINGS PROCEEDS
```
- You can say that the environment "selects" observations/rewards...
- However using the history to select the next action is not very practical, it is typically very enormous especially agents which have long lives!

### THE ALGORITHMIC GOAL
```
The agent selects actions, and the goal is to build an algorithm of how the agents selects actions

THE ALGORITHM IS THE MAPPING OF THE CURRENT
HISTORY TO PICKING THE NEXT ACTION  
```

# THE STATE
- A state is the summary of the information from history that is used to determine what happens NEXT - If we can replace "history" by some concise summary that captures all the information that we need to determine what we should do next, or what is likely to happen next, then we have a much better chance to do some "real things" with machine learning

- The concept of state is a crucial concept

```
THE STATE IS A FUNCTION OF HISTORY

St = F(Ht)

The state at time t is a function of the
history from the beginning up to time t.
```

## There are many definitions of state but we'll be discussing three definitions of it.
- The environment state
- The agent state
- The information state

## The Environment state `Se(t)`
- Environment's private representation information used within the environment to which determines which happens next
- This state can be thought of able to spit out observed environment and reward based on action.
- Can also be thought of as whatever data the environment uses to pick the next observation or reward
- The environment state is usually not visible to the agent.
- For example: the eyes of the humanoid robot can't see want's on the back of it or what's behind the wall.
- The environment state is more like a formalism that helps us understand what the environment is rather than something practical that helps us build the algorithms here.
- Our algorithms can't depend on the the environment's private state `Se(t)` or representation at the particular time because our agent can only see the observation and reward coming in from the environment.
- Further more, even if we could see this information it may contain many irrelevant distracting information
- It is even possible that it might be a good think that our agent has its own subjective representation of the environment

```
POSSIBLE MULTI-AGENT SYSTEM

One possible scenario is that one agent can consider all other possible agent outside itself as part of the environment

It can be such that multi-agent systems are communicating with each other at cooperating each other but that's beyond the scope of this course!
```

# The agent state `Sa(t)`
- The agent's internal representation of what lives inside our algorithm
- This is whatever relevant information we use to pick the next action
- Algorithm - how to process observation, what to remember, what to throw away.
- The information used by reinforcement algorithms
- The agent state can be any function of history ie
```
Sa(t) = F(Ht)
```
- GOAL: Build an algorithm or understand how to pick actions based on the agent's state which summarizes what we've seen so far.

# Information state
- Markov state
- Contains all useful information from history

### Markov Property (Assumption)
- NOT ALL SYSTEMS HAVE THE MARKOV PROPERTY
- A state St at a given time t is a Markov STATE if and only if the probability of the next state given the current state is the same as the probability of the next state if you stored all the previous state

- In other words, you can throw away all the previous states and just retain the current state

```
P[S(t+1) | St] = P[S(t+1) | S0, S1, S2... St]

- probability of the next state given the current state
is equal to the probability of the next state given the
the current state and all the previous states before
the current state   
```
- One possible way of looking at it: The future is independent of the past given the present.
- You can throw away everything you've learned before except for the current state, everything else is useless
- The current state is a sufficient statistic of the future.
- HELICOPTER EXAMPLE: Markov state: Current position, velocity, angular velocity, angular position of the helicopter plus wind direction?
- It doesn't matter where the helicopter was 20 minutes ago, that doesn't make a difference anymore to where the helicopter will be at the next moment, All that matters is where it is now. You don't need to remember the detailed information from its previous trajectory because it is irrelevant to decide which action you have to do next.

# MARKOV VS NON MARKOV
- Is the environment state `Se(t)` Markov? Is the history `Ht` Markov?

```
RAT EXAMPLE:
- Rat will press lever for food

GIVEN
episode 1: Light Light Switch Bell -> Zap!
episode 2: Bell Light Switch Bell -> Cheese!
episode 3: Switch Light Light Bell -> ???

QUESTION: WHAT WILL HAPPEN NEXT in episode 3?

Hypothesis 1: Zap!
Because the sequence of the order bulb, switch, bell
from episode 1 is Zap!
We represent the agent state as a memory of the last sequence of the last three things we've seen.

Hypothesis 2: Cheese!
because 2 levels and 2 cheese.
We represent the state as counting the number of switches and the number of bells in the last four things we've seen. Order is important.

LESSON: Build an agent state that is useful for predicting the next state.
```

## DEFINITION: Fully-observable environment
- the "nice state" where we get to see everything
- IE

```
observation = agent state = environment state = information state

O(t) = Sa(t) = Se(t)

Formally this is the MARKOV DECISION PROCESS(MDP)
```

- In other cases, obviously, not everything is fully observable, but for now let's go with this assumption
- Full-observability the agent gets to see everything

# DEFINITION: PARTIAL OBSERVABILITY
- The agent indirectly observes the environment
### Examples of partial observability  
- A robot with a camera vision that is not told of its absolute location.
- A trading agent that only observes current price, it doesn't know what is hiding behind which are driving the prices.
- A poker playing agent that can only observe public cards.
- In a nutshell:

```
AGENT STATE IS NOT EQUAL TO ENVIRONMENT State

Or more formally,
PMDP - partially observable markov decision process
```

# LESSON: THE AGENT MUST CONSTRUCT ITS OWN STATE REPRESENTATION `Sa(t)`
- But how?

# How to construct own state representation for agent

- But how?
1.  Using the complete history? `Sa(t) = Ht`, This is the naive approach, just remember everything, but this is not very practical. Why?
2. Vector of probabilities can define the states we can use. Beliefs of environment state is probabilistic or bayesian approach. I don't know for sure but I can build a probability distribution for each possible environment state
```
Sa(t+1) = { P(P0 | Sa(t)), ... , P(Sn| Sa(t))}
```

# How to construct own state representation for agent

- Complete history
- Bayesian Approach: probabilities
- Recurrent Neural Networks
- Linear combination of the last state and latest observation.
- Linear transformation of old state and new state
```
Sa(t) = F(ws * Sa(t-1) + wo * O(t))

ws, wo are scalar constants?
```
