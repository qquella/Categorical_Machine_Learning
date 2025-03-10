import streamlit as st

st.set_page_config(
    page_title="Resources for Further Reinforcement Learning and Category Theory",
    page_icon="⚂",
    layout="wide",
)

st.title("Resources for :red[Reinforcement Learning] & :green[FinStoch]")

tab3, tab2, tab4, tab1 = st.tabs(
    ["👾 Video Rescources", "🔖 Environments", "📖 Books", "🗞️ Articles"]
)

tab3.subheader(":red[YouTube]")
tab3.markdown(
    """
- [Crash Course on Reinforcement Learning](https://youtu.be/nIgIv4IfJ6s?si=SqKVMhYIuZNXlMUp)
    \n
- [DeepMind x UCL lecture](https://www.youtube.com/@googledeepmind)
    \n
- [What is Q-Learning?](https://www.youtube.com/watch?v=nOBm4aYEYR4)
"""
)

tab2.subheader(":green[Environments]")
tab2.markdown(
    """

##### - [Gymnasium](https://gymnasium.farama.org/) - Highly recommanded! Gymnasium is a maintained fork of OpenAI’s Gym library. The Gymnasium interface is simple, pythonic, and capable of representing general RL problems, and has a compatibility wrapper for old Gym environments
\n

- [Carla](https://github.com/carla-simulator/carla) - Open-source simulator for autonomous driving research.
- [CuLE](https://github.com/NVlabs/cule) - A CUDA port of the Atari Learning Environment (ALE).
- [Deepdrive](https://github.com/deepdrive/deepdrive) - End-to-end simulation for self-driving cars.
- [DeepMind AndroidEnv](https://github.com/deepmind/android_env) - A library for doing RL research on Android devices.
- [DeepMind DM Control](https://github.com/deepmind/dm_control) - The DeepMind Control Suite and Package.
- [DeepMind Lab](https://github.com/deepmind/lab) - A customisable 3D platform for agent-based AI research.
- [DeepMind pycolab](https://github.com/deepmind/pycolab) - A highly-customisable gridworld game engine with some batteries included.
- [DeepMind PySC2](https://github.com/deepmind/pysc2) - StarCraft II Learning Environment.
- [DeepMind RL Unplugged](https://github.com/deepmind/deepmind-research/tree/master/rl_unplugged) - Benchmarks for Offline Reinforcement Learning.
- [Facebook EmbodiedQA](https://github.com/facebookresearch/EmbodiedQA) - Train embodied agents that can answer questions in environments.
- [Facebook Habitat](https://github.com/facebookresearch/habitat-api) - A modular high-level library to train embodied AI agents across a variety of tasks, environments, and simulators.
- [Facebook House3D](https://github.com/facebookresearch/House3D) - A Rich and Realistic 3D Environment.
- [Facebook natural_rl_environment](https://github.com/facebookresearch/natural_rl_environment) - natural signal Atari environments, introduced in the paper Natural Environment Benchmarks for Reinforcement Learning.
- [Google Research Football](https://github.com/google-research/football) - An RL environment based on open-source game Gameplay Football.
- [GVGAI Gym](https://github.com/rubenrtorrado/GVGAI_GYM) - An OpenAI Gym environment for games written in the Video Game Description Language, including the Generic Video Game Competition framework.
- [gym-doom](https://github.com/ppaquette/gym-doom) - Doom environments based on VizDoom.
- [gym-duckietown](https://github.com/duckietown/gym-duckietown) - Self-driving car simulator for the Duckietown universe.
- [gym-gazebo2](https://github.com/AcutronicRobotics/gym-gazebo2) - A toolkit for developing and comparing reinforcement learning algorithms using ROS 2 and Gazebo.
- [gym-ignition](https://github.com/robotology/gym-ignition) - Experimental OpenAI Gym environments implemented with Ignition Robotics.
- [gym-idsgame](https://github.com/Limmen/gym-idsgame) - An Abstract Cyber Security Simulation and Markov Game for OpenAI Gym
- [gym-super-mario](https://github.com/ppaquette/gym-super-mario) - 32 levels of original Super Mario Bros.
- [Holodeck](https://github.com/BYU-PCCL/holodeck) - High Fidelity Simulator for Reinforcement Learning and Robotics Research.
- [home-platform](https://github.com/HoME-Platform/home-platform) - A platform for artificial agents to learn from vision, audio, semantics, physics, and interaction with objects and other agents, all within a realistic context
- [ma-gym](https://github.com/koulanurag/ma-gym) - A collection of multi agent environments based on OpenAI gym.
- [mazelab](https://github.com/zuoxingdong/mazelab) - A customizable framework to create maze and gridworld environments.
- [Meta-World](https://github.com/rlworkgroup/metaworld) - An open source robotics benchmark for meta- and multi-task reinforcement learning.
- [Microsoft AirSim](https://github.com/Microsoft/AirSim) - Open source simulator for autonomous vehicles built on Unreal Engine / Unity, from Microsoft AI & Research.
- [Microsoft Jericho](https://github.com/microsoft/jericho) - A learning environment for man-made Interactive Fiction games.
- [Microsoft Malmö](https://github.com/Microsoft/malmo) - A platform for Artificial Intelligence experimentation and research built on top of Minecraft.
- [Microsoft MazeExplorer](https://github.com/microsoft/MazeExplorer) - Customisable 3D environment for assessing generalisation in Reinforcement Learning.
- [Microsoft TextWorld](https://github.com/microsoft/TextWorld) - A text-based game generator and extensible sandbox learning environment for training and testing reinforcement learning (RL) agents.
- [MineRL](https://github.com/minerllabs/minerl) - MineRL Competition for Sample Efficient Reinforcement Learning.
- [MuJoCo](http://www.mujoco.org) - Advanced physics simulation.
- [OpenAI Coinrun](https://github.com/openai/coinrun) - Code for the environments used in the paper Quantifying Generalization in Reinforcement Learning.
- [OpenAI Gym Retro](https://github.com/openai/retro) - Retro Games in Gym.
- [OpenAI Gym Soccer](https://github.com/openai/gym-soccer) - A multiagent domain featuring continuous state and action spaces.
- [OpenAI Gym](https://github.com/openai/gym) - A toolkit for developing and comparing reinforcement learning algorithms.
- [OpenAI Multi-Agent Particle Environment](https://github.com/openai/multiagent-particle-envs) - A simple multi-agent particle world with a continuous observation and discrete action space, along with some basic simulated physics.
- [OpenAI Neural MMO](https://github.com/openai/neural-mmo) - A Massively Multiagent Game Environment.
- [OpenAI Procgen Benchmark](https://github.com/openai/procgen) - Procedurally Generated Game-Like Gym Environments.
- [OpenAI Roboschool](https://github.com/openai/roboschool) - Open-source software for robot simulation, integrated with OpenAI Gym.
- [OpenAI RoboSumo](https://github.com/openai/robosumo) - A set of competitive multi-agent environments used in the paper Continuous Adaptation via Meta-Learning in Nonstationary and Competitive Environments.
- [OpenAI Safety Gym](https://github.com/openai/safety-gym) - Tools for accelerating safe exploration research.
- [Personae](https://github.com/Ceruleanacg/Personae) - RL & SL Methods and Envs For Quantitative Trading.
- [Pommerman](https://github.com/MultiAgentLearning/playground) - A clone of Bomberman built for AI research.
- [pybullet-gym](https://github.com/benelot/pybullet-gym) - Open-source implementations of OpenAI Gym MuJoCo environments for use with the OpenAI Gym Reinforcement Learning Research Platform
- [PyGame Learning Environment](https://github.com/ntasfi/PyGame-Learning-Environment) - Reinforcement Learning Environment in Python.
- [RLBench](https://github.com/stepjam/RLBench) - A large-scale benchmark and learning environment.
- [RLGym](https://github.com/lucas-emery/rocket-league-gym) - A python API to treat the game Rocket League as an OpenAI Gym environment.
- [RLTrader](https://github.com/notadamking/RLTrader) - A cryptocurrency trading environment using deep reinforcement learning and OpenAI's gym.
- [RoboNet](https://blog.ml.cmu.edu/2019/11/26/robonet/) - A Dataset for Large-Scale Multi-Robot Learning.
- [rocket-lander](https://github.com/arex18/rocket-lander) - SpaceX Falcon 9 Box2D continuous-action simulation with traditional and AI controllers.
- [Stanford Gibson Environments](https://github.com/StanfordVL/GibsonEnv) - Real-World Perception for Embodied Agents.
- [Stanford osim-rl](https://github.com/stanfordnmbl/osim-rl) - Reinforcement learning environments with musculoskeletal models.
- [Unity ML-Agents Toolkit](https://github.com/Unity-Technologies/ml-agents) - Unity Machine Learning Agents Toolkit.
- [UnityObstableTower](https://github.com/Unity-Technologies/obstacle-tower-env) - A procedurally generated environment consisting of multiple floors to be solved by a learning agent.
- [VizDoom](https://github.com/mwydmuch/ViZDoom) - Doom-based AI Research Platform for Reinforcement Learning from Raw Visual Information.
- [RLCard](https://github.com/datamllab/rlcard/) - A research platform for reinforcement learning in card games.
- [DouZero](https://github.com/kwai/DouZero/) - A research platform for reinforcement learning in DouDizhu (Chinese poker).

"""
)

tab1.subheader(":orange[Blogs/Academic Papers]")
tab1.markdown(
    """
- [Berkeley AI Research](https://bair.berkeley.edu/blog/) -- Virtual Personas for Language Models via an Anthology of Backstories
    \n
- [Google Latest Research](https://research.google/blog/)
    \n
- [Alex Irpan's Blogs](https://www.alexirpan.com/) -- a Senior Research Scientist on the AGI Safety and Alignment team at Google DeepMind. He shares loads of his interesting takes on RL, angents, AI, etc.  [Here is one of his articles on RL](https://www.alexirpan.com/2018/02/14/rl-hard.html)
    \n
- [Uber Engieering Blogs](https://www.uber.com/blog/boston/engineering/?uclick_id=18f65113-74c3-4331-a760-429faad389d1) -- The technology behind Uber Engineering
    \n
- [Markov category (nLab)](https://ncatlab.org/nlab/show/Markov+category) -- a wiki for collaborative work on Mathematics, Physics, and Philosophy

    """
    \n
- [Function Approximation in Reinforcement Learning](https://towardsdatascience.com/function-approximation-in-reinforcement-learning-85a4864d566/) -- What to do when state and action spaces explode… literally?
\n
- [Introduction to Q-learning with OpenAI Gym](https://medium.com/swlh/introduction-to-q-learning-with-openai-gym-2d794da10f3d) -- A step-by-step guide to using Q-learning to solve a simple Taxi-3 environment in OpenAI Gym

"""

)

tab4.subheader(":blue[Books]")
tab4.markdown(
    """
- [Algorithms for Reinforcement Learning. Szepesvari et. al.](https://www.amazon.com/Algorithms-Reinforcement-Learning-Csaba-Szepesvari/dp/1608454924)
    \n
- An Introduction to Deep Reinforcement Learning. Francois-Lavet et. al.
    \n
- Deep Reinforcement Learning Hands-On. Lapan
    \n
- Deep Reinforcement Learning in Action. Zai & Brown
    """
)

st.markdown(
    """
    ### RL Timeline

- 1947: [Monte Carlo Sampling](http://eniacinaction.com/the-articles/3-los-alamos-bets-on-eniac-nuclear-monte-carlo-simulations-1947-8/)
- 1958: [Perceptron](https://www.ling.upenn.edu/courses/cogs501/Rosenblatt1958.pdf)
- 1959: [Temporal Difference Learning](https://dl.acm.org/citation.cfm?id=1661924)
- 1983: [ASE-ALE — the first Actor-Critic algorithm](https://psycnet.apa.org/record/1984-13799-001)
- 1986: [Backpropagation algorithm](https://www.nature.com/articles/323533a0)
- 1989: [CNNs](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.476.479&rep=rep1&type=pdf)
- 1989: [Q-Learning](http://www.cs.rhul.ac.uk/~chrisw/new_thesis.pdf)
- 1991: [TD-Gammon](http://bkgm.com/books/Robertie-LearningFromTheMachine.html)
- 1992: [REINFORCE](https://dl.acm.org/citation.cfm?id=139614)
- 1992: [Experience Replay](https://dl.acm.org/citation.cfm?id=139620)
- 1994: [SARSA](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.17.2539)
- 1999: [Nvidia invented the GPU](https://www.nvidia.com/object/gpu.html)
- 2007: [CUDA released](https://developer.nvidia.com/cuda-zone)
- 2012: [Arcade Learning Environment (ALE)](https://arxiv.org/abs/1207.4708)
- 2013: [DQN](https://arxiv.org/abs/1312.5602)
- 2015 Feb: [DQN human-level control in Atari](https://www.nature.com/articles/nature14236)
- 2015 Feb: [TRPO](https://arxiv.org/abs/1502.05477)
- 2015 Jun: [Generalized Advantage Estimation](https://arxiv.org/abs/1506.02438)
- 2015 Sep: [Deep Deterministic Policy Gradient (DDPG)](https://arxiv.org/abs/1509.02971)
- 2015 Sep: [DoubleDQN](https://arxiv.org/abs/1509.06461)
- 2015 Nov: [DuelingDQN](https://arxiv.org/abs/1511.06581)
- 2015 Nov: [Prioritized Experience Replay](https://arxiv.org/abs/1511.05952)
- 2015 Nov: [TensorFlow](https://www.tensorflow.org/)
- 2016 Feb: [A3C](https://arxiv.org/abs/1602.01783)
- 2016 Mar: [AlphaGo beats Lee Sedol 4-1](https://deepmind.com/alphago-korea)
- 2016 Jun: [OpenAI Gym](https://github.com/openai/gym)
- 2016 Jun: [Generative Adversarial Imitation Learning (GAIL)](https://arxiv.org/abs/1606.03476)
- 2016 Oct: [PyTorch](https://pytorch.org/)
- 2017 Mar: [Model-Agnostic Meta-Learning (MAML)](https://arxiv.org/abs/1703.03400)
- 2017 Jul: [Distributional RL](https://arxiv.org/abs/1707.06887)
- 2017 Jul: [PPO](https://arxiv.org/abs/1707.06347)
- 2017 Aug: [OpenAI DotA 2 1:1](https://openai.com/blog/more-on-dota-2/)
- 2017 Aug: [Intrinsic Cusiority Module (ICM)](https://arxiv.org/abs/1705.05363)
- 2017 Oct: [Rainbow](https://arxiv.org/abs/1710.02298)
- 2017 Oct: [AlphaGo Zero masters Go without human knowledge](https://deepmind.com/blog/article/alphago-zero-starting-scratch)
- 2017 Dec: [AlphaZero masters Go, Chess and Shogi](https://arxiv.org/abs/1712.01815)
- 2018 Jan: [Soft Actor-Critic](https://ai.googleblog.com/2019/01/soft-actor-critic-deep-reinforcement.html)
- 2018 Feb: [IMPALA](https://deepmind.com/blog/article/impala-scalable-distributed-deeprl-dmlab-30)
- 2018 Jun: [Qt-Opt](https://ai.googleblog.com/2018/06/scalable-deep-reinforcement-learning.html)
- 2018 Nov: [Go-Explore solved Montezuma’s Revenge](https://eng.uber.com/go-explore/)
- 2018 Dec: [AlphaZero becomes the strongest player in history for chess, Go, and Shogi](https://deepmind.com/blog/article/alphazero-shedding-new-light-grand-games-chess-shogi-and-go)
- 2019 Apr: [OpenAI Five defeated world champions at DotA 2](https://openai.com/five/)
- 2019 May: [FTW Quake III Arena Capture the Flag](https://deepmind.com/blog/article/capture-the-flag-science)
- 2019 Aug: [AlphaStar: Grandmaster level in StarCraft II](https://deepmind.com/blog/article/AlphaStar-Grandmaster-level-in-StarCraft-II-using-multi-agent-reinforcement-learning)
- 2019 Sep: [Emergent Tool Use from Multi-Agent Interaction](https://openai.com/blog/emergent-tool-use/)
- 2019 Oct: [Solving Rubik’s Cube with a Robot Hand](https://openai.com/blog/solving-rubiks-cube/)
- 2020 Mar: [Agent57 outperforms the standard human benchmark on all 57 Atari games](https://deepmind.com/blog/article/Agent57-Outperforming-the-human-Atari-benchmark)
- 2020 Nov: [AlphaFold for protein folding](https://deepmind.com/blog/article/alphafold-a-solution-to-a-50-year-old-grand-challenge-in-biology)
- 2020 Dec: [MuZero masters Go, chess, shogi and Atari without rules](https://deepmind.com/blog/article/muzero-mastering-go-chess-shogi-and-atari-without-rules)
- 2021 Aug: [Generally capable agents emerge from open-ended play](https://deepmind.com/blog/article/generally-capable-agents-emerge-from-open-ended-play)
    """
)
