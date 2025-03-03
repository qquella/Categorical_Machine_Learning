import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.set_page_config(page_title="Temporal Difference", page_icon="⚂", layout="wide")

st.title("Temporal Difference (TD)")

st.markdown("First we have to introduce _Model-Based_ vs _Model-Free_ Methods")

# Model-Based vs Model-Free
st.header("Model-Based vs Model-Free Methods")

with st.expander("Model-Based Methods"):
    st.write("Model-based methods use a model to plan actions before they are taken.")
    st.write(
        "**Example:** In a chess game, the agent simulates future moves before making a decision."
    )

with st.expander("Model-Free Methods"):
    st.write(
        "Model-free methods do not use a model but instead learn from interactions."
    )
    st.write(
        "**Example:** In reinforcement learning for a robot, the robot learns which actions yield the highest reward by trial and error."
    )

# TD as an Adjusted Version of MC
st.header("TD as an Adjusted Version of Monte Carlo (MC)")

st.markdown(
    """
GPI has two components:
- **Evaluation** (adjusts value estimates based on new experience)
- **Improvement** (adjusts policy based on new value estimates)

The key adjustment in TD learning is within **evaluation**:
- We may study a **Markov Reward Process (MRP)** over an MDP.
- We may reference \( V(s) \) instead of \( Q(s, a) \).

### Issue with MC
Monte Carlo methods require **the entire episode to complete** before updating values:

> *An episode must complete before values can be updated.*

This makes learning **slow** if episodes are long.
TD Learning updates values after **each step**, leading to faster convergence.
"""
)

# Introduction to Temporal Difference Learning
st.header("What is Temporal Difference Learning?")

st.markdown(
    """
Temporal Difference (TD) learning is a method used to estimate the values of states under a given policy.
For a fixed policy $pi$, the Bellman Equation is given by:

#### $$ V_{\pi}(s) = \sum_{s'} T(s, \pi(s), s') \left[R(s, \pi(s), s') + \gamma V_{\pi}(s') \\right] $$

where:
- $ T(s, a, s') $ is the probability of transitioning to state $ s' $ after taking action $a$ in state $s$
- $ R(s, a, s') $ is the reward received after the transition.
- $ \gamma $ is the discount factor.
"""
)

# TD Update Function
st.header("TD Update Function")

st.markdown(
    """ #### $$ V_{\pi}(s) \leftarrow (1 - \\alpha) V_{\pi}(s) + \\alpha \left[R(s, \pi(s), s') + \gamma V_{\pi}(s') \\right] $$"""
)

st.markdown(
    """
Where:
- $ \\alpha $ is the learning rate
- $ R(s, \pi(s), s') $ is the reward received
- $ \gamma $ is the discount factor
- $ V_{\pi}(s') $ is the estimated value of the next state

Unlike MC, TD does **not** require waiting for an episode to finish, making it more efficient.
"""
)

# Example: Random Walk with 7 States
st.header("Example: Random Walk with 7 States (MC VS TD)")

st.markdown(
    """
Consider a simple **random walk** with 7 states. The agent moves randomly left or right, and two terminal states exist:
- **Left terminal state (reward = 0)**
- **Right terminal state (reward = 1)**

##### Remember our goal is to find the $V(s) \\approx E[U|S=s]$ 

The value of intermediate states is learned using **Monte Carlo (MC)** and **Temporal Difference (TD)** learning.
"""
)

st.video("./vid/random_walk_7states.mp4")

st.markdown("##### Now we can also look at the bigger picture")

# Simulation Parameters
alpha = st.slider("Learning Rate (alpha)", 0.01, 1.0, 0.1, 0.01)
gamma = st.slider("Discount Factor (gamma)", 0.0, 1.0, 0.9, 0.01)
n_episodes = st.slider("Number of Episodes", 10, 1000, 100, 10)

# True State Values
true_values = {
    1: 1 / 6,
    2: 2 / 6,
    3: 3 / 6,
    4: 4 / 6,
    5: 5 / 6,
}  # Approximate expected values


# Random Walk Simulation
def simulate_learning(method, alpha, gamma, n_episodes):
    states = np.arange(1, 6)
    V = {s: 0.5 for s in states}  # Initialize values to 0.5
    V[0], V[6] = 0, 1  # Terminal states
    errors = []

    for _ in range(n_episodes):
        s = 3  # Start in the middle state
        while s not in [0, 6]:
            s_prime = s + np.random.choice([-1, 1])
            reward = 1 if s_prime == 6 else 0

            if method == "TD":
                V[s] = (1 - alpha) * V[s] + alpha * (reward + gamma * V.get(s_prime, 0))
            elif method == "MC":
                returns = reward
                V[s] = (1 - alpha) * V[s] + alpha * returns

            s = s_prime

        error = np.mean([abs(V[s] - true_values[s]) for s in states])
        errors.append(error)

    return errors


# Simulate Learning
errors_td = simulate_learning("TD", alpha, gamma, n_episodes)
errors_mc = simulate_learning("MC", alpha, gamma, n_episodes)

# Plot Results
fig, ax = plt.subplots()
ax.plot(errors_td, label="TD Absolute Error", linestyle="dashed")
ax.plot(errors_mc, label="MC Absolute Error")
ax.set_xlabel("Episodes")
ax.set_ylabel("Average Absolute Error")
ax.set_title("TD vs MC Convergence (Absolute Error)")
ax.legend()
st.pyplot(fig)

st.markdown(
    """
### Comparison of MC vs TD
- **MC** updates values only after the episode finishes.
- **TD** updates values after each step.
- **TD generally converges faster**, especially when episodes are long.
"""
)


# Interactive TD Learning Demonstration
st.header("TD Learning in Action")


# Summary
st.markdown(
    """
### Key Takeaways
- TD learning estimates state values iteratively using new experience.
- The update rule:
  $$ V_{\pi}(s) \leftarrow (1 - \\alpha)V_{\pi}(s) + \\alpha \left(R(s, \pi(s), s') + \gamma V_{\pi}(s')\\right) $$
- This method allows learning without knowing the transition probabilities or reward function.
"""
)

st.success("Now you understand the basics of Temporal Difference Learning!")
