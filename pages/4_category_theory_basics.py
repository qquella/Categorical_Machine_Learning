import streamlit as st

st.title("Summary of Category Theory")

st.header("General Idea of Category Theory")

st.markdown(
    """
> "Category theory takes a bird's eye view of mathematics. 
> From high in the sky, details become invisible, but we can spot patterns that were impossible to detect from ground level." 
>
>  Tom Leinster, _Basic Category Theory_
"""
)

st.markdown(
    """
---
"""
)

# TODO: Add Michael Scott meme

st.markdown(
    """
> "How things relate to things."
>
>  Jacob S. Zelko
"""
)

st.header(
    """
Basics of Categories
"""
)

st.video("./vid/BasicCategoriesAnimation.mp4")

st.subheader(
    """
Definition
"""
)

st.markdown(
    """
- Fundamental data structure is a category equipped with:

    - A collection (Objects)

    - Morphisms (Arrows)

        - $f : A \\rightarrow B$

    - Notation: $\\mathbf{C}$
"""
)

st.subheader(
    """
Properties of Categories
"""
)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
    **Composition:** $g \\circ f : A \\rightarrow C$

    **Associativity:** $h \\circ (g \\circ f) = (h \\circ f) \\circ f$

    **Unit:** $f \\circ 1_A = f = 1_B \\circ f$

    **Identity:** $1_A : \\rightarrow A$

    """
    )


with col2:
    st.markdown(
        """
    ##### Reference Maps
    """
    )

    st.markdown(
        """
    $f: A \\rightarrow B$

    $g: B \\rightarrow C$

    $h: C \\rightarrow D$
    \n

    """
    )


st.subheader(
    """
Functors
"""
)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
    **Functor:** Maps objects to objects, arrows to arrows

    - $F: \\mathbf{C} \\rightarrow \\mathbf{D}$
    """
    )


with col2:
    st.markdown(
        """
    ##### Properties
    """
    )

    st.markdown(
        """
    - $F(f: A \\rightarrow B) = F(f) : F(A) \\rightarrow F(B)$

    - $F(g \circ f) = F(g) \circ F(f)$

    - $F_{1_A} = 1_{F_A}$
    """
    )


st.markdown(
    """
---
"""
)

st.header("Examples of Categories")

st.markdown(
    """
- $\mathbf{Set}_{fin}:$ finite sets (Objs); functions (Morphs)

- $\mathbf{Ab}:$ Abelian groups (Objs); group homomorphisms (Morphs)

- $\mathbf{Schema}:$ Database schemas (Objs); schema mappings (Morphs)

- $\mathbf{FinStoch}:$ finite sets (Objs); stochastic maps (Morphs)
"""
)
