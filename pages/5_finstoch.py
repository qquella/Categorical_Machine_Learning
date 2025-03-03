import streamlit as st

st.title("$\mathbf{FinStoch}$ -- Category of Stochastic Maps")

st.subheader(
"""
$\mathbf{FinStoch}$ Definition
"""
)

st.markdown(
"""
- A category equipped with:

    - **Objects**: Finite Sets

    - **Morphisms**: Stochastic Maps
"""
)

col1, col2 = st.columns(2)

with col1:
    st.subheader(
    """
    Additional Properties
    """
    )
    st.markdown(
    """
    **Composition:** $(g \circ f)(z | x): \Sigma_{y \in Y} g(z | y)f(y | x)$

    - Chapman-Kolmogorov Equation

    **Associativity:** Matrix Multiplication

    **Unit:** Singleton Set (with subcategory $\mathbf{Set}_{fin}$)

    **Identity:** Identity Matrices

    """
    )


with col2:
    st.markdown(
    """
    #### Reference Maps
    """
    )

    st.markdown(
    """
    $f: X \\rightarrow Y$

    $g: Y \\rightarrow Z$

    """
    )

st.subheader(
"""
Additional Properties
"""
)

st.markdown(
"""
1. $\mathbf{FinStoch}$ - an example of a Markov Category

2. Goals categorical probability

    a. Generalize results in probability theory

    b. Enable looser conditions such as countability, etc.

3. Markov Categories' maps are like "random functions"
"""
)
