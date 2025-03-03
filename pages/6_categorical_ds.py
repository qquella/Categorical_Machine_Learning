import streamlit as st

st.title("Categorical Data Science")

st.header("Applied Category Theory")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
    """
    - CT outside of maths

    - Current rise of ACT (2010's)

    """
    )
    st.image("img/topos.png")

with col2:
    st.image("img/algebraic_dbs.png")

st.header("What Are Database Schemas?")

st.markdown(
"""
1. Schematic for data stored in a database

2. Describes database components such as:

    a. Tables -- how data is laid out

    b. Attributes -- how tables relate to one another

3. Does not contain the data
"""
)

st.header("Example of Schema and Instances")

st.image("img/schema_example.png")

st.header("Database Schemas as Categories")

st.markdown(
"""
- Understood as a finite category

"""
)

st.image("img/finite_category.png")

st.markdown(
"""
- Captures interactions:

    - Between rows of database instances

    - Based on columns of tables
"""
)

st.header("Examples")

st.markdown(
"""
1. [Employees & Department Schema](https://catcolab.org/analysis/01951b86-7642-7723-b5c8-74fa68cf6f06)

2. [Employees & Department & Project Schema](https://catcolab.org/analysis/019515b4-460b-7ff3-8d0f-ee1dfce3aec7)
"""
)

st.header("C-Sets")

st.markdown(
"""
- Given a small category $\\mathbf{C}$, a $\\mathbf{C}$-**set** is a functor

    - $X: \\mathbf{C} \\rightarrow \\mathbf{Set}$

- Given a $\\mathbf{C}$-**set**, $\\mathbf{X}$, it consists of:

    - A set $\mathbf{X}(c)$ for all $c, d \in \mathbf{C}$

    - A function $\mathbf{X}(f): \mathbf{X}(c) \\rightarrow \mathbf{X}(d)$ for all morphisms in $\mathbf{C}$, $f: c \\rightarrow d$
"""
)

st.header("Attributed C-Sets")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
    """
    - ACSets: Instances of database schemas

    - Contains data attributes

    - Enables computation within a categorical framework

    """
    )

with col2:
    st.image("img/acset.png")


st.header("Instances of Databases in ACSets.jl")

col1, col2 = st.columns(2)

with col1:
    st.image("img/instance_example.png")

with col2:
    st.code(
    """
    @present SchCompany(FreeSchema) begin
        Name::AttrType

        Employees::Ob
        emp_id::Hom(Employee, Employee)
        emp_name::Attr(Employee, Name)


        Departments::Ob
        dept_id::Hom(Department, Employee)
        dept_name::Attr(Department, Name)
    end
    """,
    language = "julia"
    )

st.header("Instances of Databases in ACSets.jl")

st.markdown(
"""
- Using categorical computational structures for data science

- More about integration of data assets

- Provides a place "to do" data science*
    
    - *to some extent
"""
)

st.header("Next Steps")

st.markdown(
"""
1. Find datasets to present as ACSets

2. Convert dataset schemas into ACSet language

3. Experiment with models on top of ACSets

    i. Stochastic methods

    ii. Machine learning approaches

4. Report results

"""
)

st.header("Thoughts on Categorical Data Science")

st.markdown(
"""
- Ripe for exploration and innovation

- Can play a role in simplification and improving pipelines

- Problem domain space continues to grow

    - Applicability within traditional data science workflows

    - Larger than memory data handling
"""
)

st.header("References")

st.markdown(
"""
1 Schultz, P., Spivak, D. I., Vasilakopoulou, C., & Wisnesky, R. (2016). Algebraic databases. arXiv preprint arXiv:1602.03501.

2 Patterson, E. (2022) AlgebraicJulia: a compositional approach to technical computing

3 Lynch O., Fairbanks, J. (2023) Computational Category Theory in Applied Mathematics

4 Patterson, E., Lynch, O., & Fairbanks, J. (2022). Categorical data structures for technical computing. Compositionality, 4.

5 CatColab, Patterson, E. (2024). Toward collaborative modeling with categorical logics. Topos Institute Berkeley Seminar

6 nLab Contributors. (2024). FinStoch. https://ncatlab.org/nlab/show/FinStoch

7 nLab Contributors. (2025). Markov Category. https://ncatlab.org/nlab/show/Markov+category
"""
)
