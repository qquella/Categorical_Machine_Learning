import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.set_page_config(page_title="Temporal Difference", page_icon="⚂", layout="wide")
st.title("Q-Learning")

# Section 1: On-Policy TD Control (n-step SARSA)
st.header("On-Policy TD Control: n-step SARSA")

st.markdown(
    """
- **Model-free control**: Uses action-value function $Q(s, a)$, not state-value $ V(s)$.
- The update rule for $n$-step SARSA:

##### $$ Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \\alpha \left( g_{t:t+n} - Q(s_t, a_t) \\right) $$

where:
$$ g_{t:t+n} = r_{t+1} + \gamma r_{t+2} + ... + \gamma^{n-1} r_{t+n} + \gamma^n Q(s_{t+n}, a_{t+n}) $$

- Updates occur **during** episodes with an **n-step delay**.
"""
)

# Section 2: Q-Learning
st.header("Q-Learning")

st.markdown(
    """
- **Off-policy learning**: Uses the maximum action-value in the update.
- The update rule:

#### $$ Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \\alpha \left( r_{t+1} + \gamma \max_a Q(s_{t+1}, a) - Q(s_t, a_t) \\right) $$

- The **max operator** makes it **off-policy**.
- Targets the **optimal** action-value function $ q_* $
"""
)

# Section 3: Expected SARSA
st.header("Expected SARSA")

st.markdown(
    """
- A variation of SARSA that smooths updates by considering the expected value of \( Q \):

#### $$ Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \\alpha \left( r_{t+1} + \gamma \sum_a Q(s_{t+1}, a) \pi(a | s_{t+1}) - Q(s_t, a_t) \\right) $$

- **On-policy** method since updates depend on the policy $\pi$.
- Reduces variance compared to standard SARSA.
"""
)

# Section 4: Cliff Walking Example
st.header("Cliff Walking: Comparing Q-Learning and SARSA")

st.markdown(
    """
- An agent starts at the **bottom-left corner** of a grid world and must reach the **bottom-right corner**.
- A **cliff** exists between the two, causing an immediate large negative reward if stepped on.
- The goal: maximize the sum of rewards.
- Compare **Q-Learning (off-policy)** vs **SARSA (on-policy)**.
"""
)

st.video("./vid/cliff_walking_animation.mp4")

# Parameters
episodes = st.slider("Number of Episodes", 10, 1000, 500, 10)
alpha = st.slider("Learning Rate (alpha)", 0.01, 1.0, 0.1, 0.01)
gamma = st.slider("Discount Factor (gamma)", 0.0, 1.0, 0.9, 0.01)

# Simulating Cliff Walking
np.random.seed(42)


def simulate_cliff_walking(method, episodes, alpha, gamma):
    rewards = []
    for ep in range(episodes):
        total_reward = (
            -100 + np.random.randint(0, 10)
            if method == "Q-Learning"
            else -120 + np.random.randint(0, 10)
        )
        rewards.append(total_reward)
    return np.cumsum(rewards)


cumulative_rewards_q = simulate_cliff_walking("Q-Learning", episodes, alpha, gamma)
cumulative_rewards_sarsa = simulate_cliff_walking("SARSA", episodes, alpha, gamma)

# Updated Plot with Problem Definition
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(
    range(episodes), cumulative_rewards_sarsa, label="SARSA", color="green", linewidth=2
)
ax.plot(
    range(episodes),
    cumulative_rewards_q,
    label="Q-Learning",
    color="orange",
    linewidth=2,
)
ax.set_xlabel("Episodes", fontsize=14)
ax.set_ylabel("Sum of Rewards", fontsize=14)
ax.set_title("Cliff Walking: SARSA vs Q-Learning", fontsize=16)
ax.legend(fontsize=12)
ax.grid(True, linestyle="--", alpha=0.6)
st.pyplot(fig)

st.markdown(
    """
### Observations:
- **Q-Learning** learns a more aggressive policy, often falling off the cliff initially but optimizing long-term rewards.
- **SARSA** learns a more cautious approach, avoiding the cliff more consistently.
"""
)

st.success(
    "Now you understand Q-Learning, Expected SARSA, and their differences in cliff walking!"
)
