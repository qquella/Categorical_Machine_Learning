import matplotlib.pyplot as plt
import streamlit as st
from numpy import imag

st.set_page_config(
    page_title="Markrov Decision Process (MDP)", page_icon="⚂", layout="wide"
)

st.title("Markrov Decision Process (MDP)")

st.markdown(
    """
**Boring Defintion**: A mathematical framework used for modeling decision-making in situations where outcomes are partly random and partly controlled by an agent. It is widely used in reinforcement learning and dynamic programming.
"""
)

st.video("./vid/states.mp4", autoplay=True, loop=True)

# Components of an MDP
st.header("Key Components of an MDP")


with st.expander("States (S)"):
    st.write("Represent the different possible situations the agent can be in.")

    st.image("./img/chess_board.png", caption="A board position in a chess game")

with st.expander("Actions (A)"):
    st.write("The choices available to the agent in a given state.")
    st.image("./img/knight.png", caption="Moving a piece to a new position")

with st.expander("Transition Probability (P)"):
    st.write(
        "Defines the probability of reaching a new state given the current state and action."
    )
    st.image(
        "./img/checkmate.png",
        caption="The probability that a given move leads to a checkmate or an advantageous position",
        use_container_width=True,
    )

with st.expander("Rewards (R)"):
    st.write("A function that assigns a numerical value to state transitions.")
    st.image(
        "./img/rewards.png",
        caption="Capturing an opponent’s piece results in a positive reward, while losing a piece gives a negative reward",
    )

with st.expander("Policy (π)"):
    st.write("A mapping from states to actions that defines the agent’s behavior.")
    st.image(
        "./img/strategy.png",
        caption="A strategy that dictates how the player should move based on board positions",
    )


st.markdown(
    """
#### _Example: **Grid World**_

"""
)

st.image("./img/gridworld.png")

st.markdown(
    """

#####  Stochastic (Non-deterministic)

Noisy movement: actions do not always go as planned
 - 80% of the time, the action North takes the agent North (if there is no wall there)
 - 10% of the time, North takes the agent West; 10% East
 - If there is a wall in the direction the agent would have been taken, the agent stays put

```
python gridworld.py -m
```
"""
)

# Explanation of MDP Sequence
st.header("$\pi(a|s)$")
st.markdown(
    """
    ##### For MDPs, we want an optimal :red[policy $\pi^*$: S → A]
    - This is a state dependent distribution over actions a
    - The agent selects actions by sampling from this distrib distribution
    - An optimal policy is one that maximizes expected utility if followed
    - if we run the policy through the mdp we'll get a trajectory of States actions and rewards:
"""
)

st.image(
    "./img/optimal_policy.png",
    caption="Example Optimal Policy $\pi^*$ for Different Reward Function $R(s)$",
)

st.subheader("The Sequence: $(s_0, a_0, r_0, s_1, ...)$")

st.markdown(
    """
An agent interacts with an environment through a sequence of actions and observations. The **MDP sequence** follows this pattern:

1. The agent starts in an initial state $$ s_0 $$.
2. The agent takes an action $$ a_0 $$ based on a policy $$ \pi(s_0) $$.
3. The environment responds with a reward $$ r_0 $$ and a new state $$ s_1 $$.
4. This process repeats over time: $$ (s_0, a_0, r_0, s_1, a_1, r_1, s_2, ...) $$.

"""
)

st.image("./img/mdp_search_tree.png", caption="MDP Search Tree")

st.markdown(
    """
    #### Discounting 
 - More or less?
[1, 2, 2] or [2, 3, 4]

 - Now or later?
[0, 0, 1] or [1, 0, 0]
    """
)

with st.expander("Answer"):
    st.markdown(
        """
        - We want to maximize the sum of rewards
        - We prefer rewards now to rewards later
        - One solution: values of rewards decay exponentially
        """
    )

    st.image("./img/discounting.png", caption="Discounting")

    st.markdown(
        """
        Example: discount of $0.5$
- $U([1,2,3]) = 1*1 + 0.5*2 + 0.25*3$
- $U([1,2,3]) < U([3,2,1])$
        """
    )

st.markdown(
    """

##### we want the gamma discounted sum of future rewards to be high when averaged over many trajectories

The goal of the agent is to maximize the **return** (Utility Function):
#### $$ U =R((s_0, a_0, s1)+γR(s_1, a_1, s_2)++γ^2R(s_2,a_2,s_3)+γ^3R(s_3,a_3,s_4)+.... $$
where $$ \gamma $$ (gamma) is a discount factor that determines the importance of future rewards.
i.e.:
#### $$ U^\pi(s)=\mathbb{E}\left[\sum_{t=0}^{\infty}\gamma^tR(S_t)\\right] $$
"""
)

st.video("./vid/gpi_animation.mp4")


# Discounted Return Visualization
def plot_discounted_return():
    gamma = 0.9
    rewards = [10, 5, 2, 1, 0.5]
    discounted_returns = [r * (gamma**t) for t, r in enumerate(rewards)]

    plt.figure(figsize=(6, 4))
    plt.plot(
        range(len(rewards)), discounted_returns, marker="o", label="Discounted Return"
    )
    plt.xlabel("Time Step")
    plt.ylabel("Value")
    plt.title("Discounted Return Over Time")
    plt.legend()
    plt.grid()
    st.pyplot(plt)


st.subheader("Visualizing Discounted Return")
st.write(
    "This plot shows how rewards are discounted over time based on a discount factor (γ = 0.9)."
)
plot_discounted_return()

st.header("Optimal Quantities")

st.markdown(
    """
##### - :blue[The value (utility) of a state s]:
$V^*(s)$ = expected utility starting in s and acting optimally

##### - :green[The value (utility) of a q-state (s,a)]:
$Q^*(s,a)$ = expected utility starting out having taken action a from state s and (thereafter) acting optimally

##### - :red[The optimal policy]:
$\pi^*(s)$ = optimal action from state s

>>> Example: Gridworld :blue[V Values] and Gridworld :green[Q Values]
```
python gridworld.py -a value -i 100 -k 10
```
"""
)

with st.expander("How to be Optimal???"):
    st.image("./img/opt.png")

st.markdown(
    """
    #### [Bellman Equations] Recursive definition of value:
  #####  $$ V^*(s) = \max_{a}Q^*(s,a) $$

#####    $$ Q^*(s,a) = \sum_{s'} T(s,a,s')[R(s,a,s') + \gamma V^*(s')] $$

##### $$ V^*(s) = \max_{a}  \sum_{s'} T(s,a,s')[R(s,a,s') + \gamma V^*(s')] $$

Example:
```
 python gridworld.py -a value -i 0
```
    """
)

st.markdown(
    """
    #### Value Iteration 
- Start with $V_0(s) = 0$: no time steps left means an expected reward sum of zero
-  Given vector of $V_k(s)$ values, do one ply of expectimax from each state
##### $V_{k+1}(s) <- \max_{a}  \sum_{s'} T(s,a,s')[R(s,a,s') + \gamma V^*(s')] $
- Repeat until convergence
- Complexity of each iteration: $O(S^2A)$
- Theorem: will converge to unique optimal values
    - Basic idea: approximations get refined towards optimal values
    - Policy may converge long before values do

Example:
    """
)

st.image("./img/value_iter.png", caption="Value Iteration Example")

st.markdown(
    """
    #### Policy Methods
    ##### Fixed Policy
    """
)

st.image("./img/fixed_p.png", caption="Fixed Policy")

st.markdown(
    """
    ##### Idea: Turn recursive Bellman equations into updates
    - #### $V^{\pi}_{0}(s) = 0$
    - #### $V^{\pi}_{k+1}(s) <- \sum_{s'} T(s,a,s')[R(s,a,s') + \gamma V^*(s')] $

    Note: Without the maxes, the Bellman equations are just a linear system
    """
)

st.image("./img/rf.png", caption="Policy Evaluation")

# Interactive Policy Example
st.subheader("Policy Demonstration")

policy_type = st.selectbox(
    "Choose a policy type:",
    ["Random Policy", "Greedy Policy", "Exploration-Exploitation Balance"],
)

if policy_type == "Random Policy":
    st.write(
        "In a **random policy**, the agent selects actions at random, without considering rewards."
    )
elif policy_type == "Greedy Policy":
    st.write(
        "In a **greedy policy**, the agent always selects the action with the highest expected reward."
    )
else:
    st.write(
        "In an **exploration-exploitation balance**, the agent sometimes explores new actions while often choosing the best-known action."
    )

st.markdown(
    """
    #### Computing Actions from Q-Values
    ##### $\pi^*(s) = \\argmax_{a} Q^*(s,a)$

    ````
     python gridworld.py -a q -k 20
    ``
    """
)

st.markdown(
    """
    ### Insight into Learning
    """
)

st.image("./img/slot_m.png")
st.image("./img/slot2.png", caption="after 100 rounds: red 150, blue 100")

st.markdown(
    """
    ### $$$    
\n

#### Playing w/ Unknown Model
    """
)

st.image("./img/unknown.png", caption="Rules changed! Red’s win chance is different")

st.image("./img/play2.png")

st.markdown(
    """
    ##### Continue???

    - Exploration
    - Regrets
    - Sampling
    \n
    #### Planing -> Learning
    """
)

st.image("./img/pigoen_ml.png")
st.image("./img/fire.png")

st.title("Monte Carlo(MC) Methods")

st.video("./vid/mc_methods.mp4")

st.markdown(
    """
### Summary
- The **Markov Decision Process (MDP)** is the foundation of reinforcement learning.
- The agent interacts with an **environment** by taking actions and receiving rewards.
- A **policy** defines the agent’s behavior over time.
- The goal is to maximize the expected **return (Utility)** $U$ by choosing optimal actions.
- Side note about Monte Carlo we learned in class...
"""
)

st.success(
    "Congratulations! You now understand the basics of Markov Decision Processes."
)
