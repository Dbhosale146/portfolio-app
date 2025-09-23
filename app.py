import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(
    page_title="John Doe - Portfolio",
    page_icon="👋",
    layout="wide",
)

# --- INTRO ---
st.title("John Doe")
st.subheader("Aspiring Data Scientist | Python & SQL")
st.write(
    "I am a passionate and results-driven aspiring data scientist with a strong foundation in Python and SQL. I am eager to apply my skills to solve real-world problems and contribute to a data-driven organization."
)

# --- SOCIAL LINKS ---
st.write("---")
st.subheader("Find Me Online")
st.write(
    """
- [LinkedIn](https://www.linkedin.com/)
- [GitHub](https://github.com/)
- [Twitter](https://twitter.com/)
"""
)

# --- SKILLS ---
st.write("---")
st.subheader("Skills")
st.write(
    """
- **Programming Languages:** Python, SQL
- **Data Science Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- **Databases:** PostgreSQL, MySQL
- **Tools:** Git, Docker
"""
)

# --- PROJECTS ---
st.write("---")
st.subheader("Projects")

# Project 1
st.write("**Project 1: Customer Churn Prediction**")
st.write(
    "Developed a machine learning model to predict customer churn for a telecommunications company. The model achieved an accuracy of 85% and helped the company to identify at-risk customers."
)
st.write("**Technologies:** Python, Scikit-learn, Pandas")
st.write("[Link to Project](https://github.com/)")

# Project 2
st.write("**Project 2: Sales Data Analysis**")
st.write(
    "Analyzed sales data for a retail company to identify trends and patterns. The analysis helped the company to make informed decisions about pricing, promotions, and inventory management."
)
st.write("**Technologies:** Python, Pandas, Matplotlib, Seaborn")
st.write("[Link to Project](https://github.com/)")

# --- EDUCATION ---
st.write("---")
st.subheader("Education")
st.write(
    """
- **Bachelor of Science in Computer Science**
  - University of Example, 2018-2022
"""
)

# --- CONTACT ---
st.write("---")
st.subheader("Contact Me")
st.write("Feel free to reach out to me for any inquiries or collaborations.")

with st.form(key="contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        st.success("Thank you for your message! I will get back to you soon.")

