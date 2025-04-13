import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
    "views/about.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)

projects_page = st.Page(
    "views/projects.py",
    title="Additional Projects",
    icon=":material/rocket:",
)
project_1_page = st.Page(
    "views/sales_dashboard.py",
    title="Sales Dashboard",
    icon=":material/bar_chart:",
)

# Add the Services Page
services_page = st.Page(
    "views/services.py",  # Path to your services page file
    title="My Services",     # Title of the page
    icon=":material/code:",  # Icon for the page
)


# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [projects_page, project_1_page],
        "Services": [services_page],  # Add the services page here
    }
)

# --- SHARED ON ALL PAGES ---
st.markdown(
    """
    <style>
    .stLogo img {
        width: 350px; 
        height: 150px; 
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.logo("views/images/codingisfun_logo.png")
st.sidebar.markdown("Made with ❤️ by Aamna Ashraf Rajput")

# Add social links to the sidebar
st.sidebar.markdown("### Connect with Me")
st.sidebar.markdown(
    """
    - [GitHub](https://github.com/aamnaashraf)
    - [LinkedIn](https://www.linkedin.com/in/aamna-ashraf-rajput-552a20280?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
    """
)


# --- RUN NAVIGATION ---
pg.run()