import streamlit as st

st.set_page_config(
    page_title="Reinforcement Learning & FinStoch in ML",
    page_icon="./img/unicorn.png",
    layout="wide",
)

st.title(":red[Reinforcement Learning] & :green[FinStoch] in _Machine Learning_")
st.markdown("> A presentation for Machine Learning 2 MATH 7339")
st.markdown("> Author: :red[@Quella Wang] :red[@Jacob Zelko]")
st.video("./vid/coin_toss.mp4", autoplay=True, loop=True)

with st.expander("Topics Overview", expanded=True):
    st.page_link(
        "./pages/1_markrov_decision_process.py",
        label="Markrov Decision Process",
        icon="🎲",
    )
    st.page_link(
        "./pages/2_temporal_difference.py",
        label="Temporal Difference Learning",
        icon="🎮",
    )
    st.page_link("./pages/3_q_learning.py", label="Q-Learning", icon="♟️")
    st.page_link(
        "./pages/4_category_theory_basics.py",
        label="What Is Catergory Theory?",
        icon="🧩",
    )
    st.page_link("./pages/5_finstoch.py", label="FinStoch - Stochastic Maps", icon="🗺️")
    st.page_link(
        "./pages/6_categorical_ds.py", label="Categorical Data Science", icon="📊"
    )
    st.page_link("./pages/7_next_steps.py", label="Next Steps", icon="🐾")
    st.page_link("./pages/8_rescources.py", label="Resources", icon="📚")

st.image("./img/ml_xkcd.png", caption="xkcd Ml meme", use_container_width=True)
