# Lecture 1: Introduction Part 1

## Summary

1. **Characteristics of RL Paradigm**
  - no supervisor, only reward signal
  - feedback is delayed, not instantaneous
  - time really matters, its a sequential process
  - the agent gets to take actions, and its actions influences the environment


2. **The RL Problem**
  - Concept of reward and the reward hypothesis
    - All goals can be described as the maximization of expected cumulative reward
  - Sequential decision making
    - The goal is to select actions to maximize the total future reward (best results)
    - We need to think ahead, rewards maybe delayed, actions may have long term consequences. It might be better to sacrifice immediate rewards now to gain more longterm reward.

## Characteristics of RL Paradigm

1. **No supervisor, only reward signal**
  - trial and error
  - No supervisor means:
    - nobody tells you: "that's the best thing to do"
    - nobody tells you: "do this action in this situation"
  - Reward signal
    - that is good, that is bad
    - that is worth 10 points or -3 points


2. **Feedback is delayed, not instantaneous**
  - When you make a decision now, it might take many many steps for your you/agent to realize whether that decision is good or bad.. it might take many many steps for you to realize how good or bad it is.
  - It might be the case that something might be good at the short term but in the long term it is catastrophic.

3. **Time really matters. Assumption: Sequential process**
  - You are in a dynamic ever-changing environment / world
  - Example: Robot in an environment, what the robot sees in one second will be correlated with what it will see in the next second depending on your action
  - You get to take actions, and that actions influences the environment.
  - The action of the robot influences the subsequent data it receives.
  - If the robot goes to the left, what it will see will be very different if instead of chooses to go to the right instead.

###### There are many examples of reinforcement learning problems. Take a look at David Silver's lectures.

## The RL Problem

### **ONE:THE REWARD HYPOTHESIS**

```
ASSUMPTION: ALL GOALS CAN BE DESCRIBED AS THE MAXIMIZATION OF
EXPECTED CUMULATIVE REWARD

Side Comment:
- Do you agree with this?
- Like philosophically and stuff?
- this real life????
```
- `Rt` - the reward at time `t`
  - A scalar feed back signal. This is just a number
  - It indicates how well you the agent is doing at time step `t`


**EXAMPLES OF REWARDS**
1. **Fly stunt maneuvers in a helicopter.**
  - positive reward for following the desired trajectory
  - negative reward for crashing


2. **Defeat world champion at backgammon**
  - positive reward for winning a game
  - negative reward for losing a game
  - no intermediate rewards inside the game, you only get a reward after the game is finished.


3. **Manage an investment portfolio**
  - positive reward for each dollar


4. **Control a power station**
  - positive reward for producing power
  - negative reward for exceeding safety thresholds


5. **Make a robot walk**
  - positive reward for forward motion
  - negative reward for falling over

6. **Play many different Atari games better than humans**
  - positive reward for increasing score
  - negative reward for decreasing score

### **TWO:SEQUENTIAL DECISION MAKING**
```
GOAL: SELECT ACTIONS TO MAXIMIZE TOTAL FUTURE REWARDS
(IE Best results)
```

**We need to think ahead**
- Actions may have long term consequences
- Reward maybe delated
  - It might not come now, it might come in some future step
  - It might be better to sacrifice an immediate reward now to gain more long term reward.

**EXAMPLES OF THINKING AHEAD**

1. **Financial Investment**
  - Spend some money now (lose money), you believe later you get more money back

2. **Refuelling a Helicopter**
  - Stop, lose your reward for following your maneuvers, to refuel for a while, but it might prevent a crash in several hourse
  - Longer runs? More reward in the long run

3. **Choose a move in a game chess(that does not look like you will get an immediate gain)**
  - Example: block opponent moves (refrain from taking the opponents queen) but take a strategic move which might help you later on. Might help winning chances many moves from now.
