import streamlit as st
from views.contact import contact_form
import base64

# Function to toggle the contact form visibility
def toggle_contact_form():
    st.session_state.show_contact_form = not st.session_state.show_contact_form




# Initialize session state for contact form visibility
if "show_contact_form" not in st.session_state:
    st.session_state.show_contact_form = False


# --- CUSTOM CSS FOR DARK THEME, BORDERS, TRANSITIONS, AND FOOTER ---
st.markdown(
    """
    <style>
/* Dark theme */
@media (prefers-color-scheme: dark) {
    body {
        color: #ffffff;
        background-color: #1e1e1e;
    }
    .stApp {
        background-color: #1e1e1e;
    }
    .stButton button {
        background-color: #0078d4;
        color: white;
    }
    .skill-box {
        background-color: #2d2d2d;
        border: 2px solid #0078d4;
    }
    .timeline-item {
        background-color: #2d2d2d;
        border: 1px solid #3d3d3d;
    }
    .soft-skill-card {
        background: linear-gradient(45deg, #2d2d2d, #3d3d3d);
        border: 1px solid #0078d4;
    }
    .footer {
        background-color: #2d2d2d;
        border-top: 2px solid #0078d4;
    }
}

/* Light theme */
@media (prefers-color-scheme: light) {
    body {
        color: #000000;
        background-color: #ffffff;
    }
    .stApp {
        background-color: #ffffff;
    }
    .stButton button {
        background-color: #1e90ff;
        color: white;
    }
    .skill-box {
        background-color:rgb(63, 61, 61);
        border: 2px solid #1e90ff;
    }
    .timeline-item {
        background-color: rgb(63, 61, 61);
        border: 1px solid #e0e0e0;
    }
    .soft-skill-card {
        background: rgb(63, 61, 61);
        border: 1px solid #1e90ff;
    }
    .footer {
        background-color:rgb(63, 61, 61);
        border-top: 2px solid #1e90ff;
    }
    
}

/* Common styles */
.stButton button {
    border-radius: 5px;
    border: none;
    padding: 10px 20px;
    transition: background-color 0.3s;
}
.stButton button:hover {
    background-color: #005bb5;
}
/* Download Resume Button */
.resume-button {
    background-color: #0078d4; /* Same blue color */
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    text-decoration: none;
    font-size: 1rem;
    cursor: pointer;
    transition: background-color 0.3s ease;
    width: 100%;
    text-align: center;
}
.resume-button:hover {
    background-color: #005bb5; /* Same darker blue on hover */
}



/* Social Icons */
.social-icons {
    display: flex;
    
    gap: 20px;
    margin-top: 20px;
    margin-right:40px;
    margin-left:20px;
}
.social-icons a {
    color: #00b4d8;
    text-decoration: none;
    font-size: 1.5rem;
    transition: color 0.3s;
}
.social-icons a:hover {
    color: orange;
}

/* Section Headings */
.section-heading {
    font-size: 2.2rem !important;
    color: #00b4d8 !important;
    border-left: 5px solid #0078d4;
    padding-left: 15px;
    margin: 30px 0 !important;
}

/* Timeline Items */
.timeline-item {
    padding: 20px;
    margin: 15px 0;
    border-radius: 10px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
.timeline-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 12px rgba(0, 180, 216, 0.2);
    border: 1px solid #00b4d8;
}
.timeline-title {
    font-size: 1.3rem;
    color: #00b4d8;
    margin-bottom: 5px !important;
    transition: color 0.3s ease;
}
.timeline-item:hover .timeline-title {
    color: #90e0ef;
}
.timeline-sub {
    color: #a0a0a0;
    font-size: 0.95rem;
    transition: color 0.3s ease;
}
.timeline-item:hover .timeline-sub {
    color: #c0c0c0;
}

/* Soft Skills Grid */
.soft-skill-card {
    padding: 25px;
    border-radius: 15px;
    margin: 15px 0;
}
.soft-skill-title {
    font-size: 1.5rem;
    color: #00b4d8;
    margin-bottom: 15px !important;
    text-align: center;
}
.soft-skill-text {
    color: #c0c0c0;
    font-size: 1rem;
    line-height: 1.6;
}

/* Skill boxes */
.skill-box {
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    text-align: center;
    margin: 20px;
    transition: transform 0.2s, box-shadow 0.2s;
    height: 250px;
    width: 200px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.skill-box:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.5);
    border-color: #00b4d8;
}
.skill-box h3 {
    margin: 0;
    font-size: 1.8rem;
    color: #00b4d8;
    font-weight: bold;
}
.skill-box p {
    margin: 10px 0 0;
    font-size: 1.1rem;
    color: #a0a0a0;
}

/* Footer */
.footer {
    width: 100%;
    color: white;
    text-align: center;
    padding: 20px;
    box-shadow: 0 -4px 8px rgba(0, 0, 0, 0.3);
    margin-top: 40px;
}
.footer a {
    color: #00b4d8;
    text-decoration: none;
    transition: color 0.3s;
}
.footer a:hover {
    color: #0078d4;
}

/* Skill Circles - Light Mode */
@media (prefers-color-scheme: light) {
    .circle {
        background-color: white; /* Light background */
        color: black; /* Black text */
        border: 6px solid #e0e0e0; /* Light border */
    }
    .figma { border-color: #76FF03; box-shadow: 0px 0px 10px #76FF03; }
    .html { border-color: #FF5722; box-shadow: 0px 0px 10px #FF5722; }
    .css { border-color: #00E5FF; box-shadow: 0px 0px 10px #00E5FF; }
    .nextjs { border-color: #000000; box-shadow: 0px 0px 10px #000000; }
    .python { border-color: #FFD700; box-shadow: 0px 0px 10px #FFD700; }
    .typescript { border-color: #3178C6; box-shadow: 0px 0px 10px #3178C6; }
}

.circle_text {
color:black;
}


/* Skill Circles */
.skill-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 30px;
    margin-top: 30px;
}
.skill {
    text-align: center;
}
.circle {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    border: 6px solid #222;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 18px;
    color: white;
    background-color: black;
}
.figma { border-color: #76FF03; box-shadow: 0px 0px 10px #76FF03; }
.html { border-color: #FF5722; box-shadow: 0px 0px 10px #FF5722; }
.css { border-color: #00E5FF; box-shadow: 0px 0px 10px #00E5FF; }
.nextjs { border-color: #FFFFFF; box-shadow: 0px 0px 10px #FFFFFF; }
.python { border-color: #FFD700; box-shadow: 0px 0px 10px #FFD700; }
.typescript { border-color: #3178C6; box-shadow: 0px 0px 10px #3178C6; }
</style>
    """,
    unsafe_allow_html=True,
)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    # Profile Image
    st.image("views/images/logo3.png", width=230)
    
    # Social Icons Below the Picture
    st.markdown(
        """
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <div class="social-icons">
            <a href="https://www.facebook.com/AamnAashraff" target="_blank"><i class="fab fa-facebook"></i></a>
            <a href="https://www.instagram.com/aamnaashrafrajput2244?igsh=dWUxeTQ2Njl1YW0x" target="_blank"><i class="fab fa-instagram"></i></a>
            <a href="https://www.linkedin.com/in/aamna-ashraf-rajput-552a20280?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" target="_blank"><i class="fab fa-linkedin"></i></a>
         <a href="https://twitter.com/YourTwitterHandle" target="_blank"><i class="fab fa-twitter"></i></a>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown('<div class="title" style="color:#00b4d8;font-size:2.4rem;">Aamna Ashraf Rajput</div>', unsafe_allow_html=True)
    st.markdown('<div class="title" style="color:gray;font-size:1.5rem;">Developer | Designer</div>', unsafe_allow_html=True)
    st.markdown(
        """
      <div class="description" style="color:white;">
    💻 Passionate <strong>Frontend Developer</strong> with a knack for crafting seamless, user-friendly web experiences.<br><br>
</div>
        """,
        unsafe_allow_html=True,
    )

    # Buttons in a horizontal layout
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("✉️ Contact Me", key="contact_button"):
            toggle_contact_form()
    
    with col_btn2:
        # Download Resume Button
      st.markdown(
    '<a href="https://drive.google.com/file/d/1ud0FF5LCyAEU6MzHSZpdZ05dWl4cxOMa/view?usp=drivesdk" class="stButton button" download="Aamna_Ashraf_Resume.pdf">📄Resume</a>',
    unsafe_allow_html=True
)
      # --- CONTACT FORM ---
if st.session_state.show_contact_form:
    contact_form()


# --- QUALIFICATIONS SECTION ---
st.markdown('<div class="section-heading">🎓 Educational Journey</div>', unsafe_allow_html=True)

st.markdown("""
<div class="timeline-item">
    <div class="timeline-title">🏫 Matriculation</div>
    <div class="timeline-sub">Al Kamran Public School | Karachi Board | 2012</div>
</div>

<div class="timeline-item">
    <div class="timeline-title">📚 Intermediate</div>
    <div class="timeline-sub">Govt.degree College Malir Cantt,Karachi | Karachi Board | 2014</div>
</div>

<div class="timeline-item">
    <div class="timeline-title">🎓 Bachelor's Degree</div>
    <div class="timeline-sub">University of Karachi | 2018</div>
</div>

<div class="timeline-item">
    <div class="timeline-title">🚀 Generative AI & Cloud Computing</div>
    <div class="timeline-sub">Governor House | 2023-Present</div>
</div>
""", unsafe_allow_html=True)


# --- EXPERIENCE SECTION ---
st.markdown('<div class="section-heading">💼 Professional Odyssey</div>', unsafe_allow_html=True)

st.markdown("""
<div class="timeline-item">
    <div class="timeline-title">👩🏫 Educator & Coordinator</div>
    <div class="timeline-sub">Private Institutions | 2016-2019</div>
    <div class="soft-skill-text">
        • Orchestrated academic programs & student mentoring<br>
        • Developed innovative teaching methodologies<br>
        • Managed cross-functional team collaborations
    </div>
</div>

<div class="timeline-item">
    <div class="timeline-title">📈 Data Analyst</div>
    <div class="timeline-sub">Tech Solutions Inc. | 2019-2021</div>
    <div class="soft-skill-text">
        • Transform raw data into actionable insights<br>
        • Create dynamic dashboards for stakeholders<br>
        • Drive data-informed decision making
    </div>
</div>

<div class="timeline-item">
    <div class="timeline-title">💻 Software Developer Intern</div>
    <div class="timeline-sub">CodeCraft Solutions | 2021</div>
    <div class="soft-skill-text">
        • Developed and maintained web applications using Python and Django<br>
        • Collaborated with cross-functional teams to deliver projects on time<br>
        • Debugged and optimized code for improved performance
    </div>
</div>

<div class="timeline-item">
    <div class="timeline-title">🖥️ IT Support Specialist</div>
    <div class="timeline-sub">TechNova Systems | 2022-2024</div>
    <div class="soft-skill-text">
        • Provided technical support and troubleshooting for hardware and software issues<br>
        • Managed network configurations and system updates<br>
        • Assisted in the implementation of IT security protocols
    </div>
</div>
""", unsafe_allow_html=True)


# --- SOFT SKILLS SECTION ---
st.markdown('<div class="section-heading">🌟 Core Competencies</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="soft-skill-card">
        <div class="soft-skill-title">🤝 Team Synergy</div>
        <div class="soft-skill-text">
            Believing in collective intelligence through collaborative problem-solving. Creating environments where diverse perspectives merge to achieve shared objectives.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="soft-skill-card">
        <div class="soft-skill-title">🗣️ Strategic Dialogue</div>
        <div class="soft-skill-text">
            Fostering open communication channels that encourage idea exchange and constructive feedback. Ensuring clarity in both technical and non-technical discourse.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="soft-skill-card">
        <div class="soft-skill-title">🔍 Solution Crafting</div>
        <div class="soft-skill-text">
            Approaching challenges with analytical rigor and creative thinking. Balancing critical analysis with innovative approaches to develop and maintain sustainable solutions.
        </div>
    </div>
    """, unsafe_allow_html=True)


# --- TECHNICAL SKILLS SECTION ---
st.markdown('<div class="section-heading">🛠️ Technical Skills</div>', unsafe_allow_html=True)

# Skills data
skills = [
    {"name": "HTML", "description": "🌐 Markup language for web development."},
    {"name": "Tailwind CSS", "description": "⚡ Utility-first CSS framework."},
    {"name": "Next.js", "description": "🚀 React framework for production."},
    {"name": "TypeScript", "description": "🔒 Typed superset of JavaScript."},
    {"name": "JavaScript", "description": "💻 Programming language for the web."},
    {"name": "Python", "description": "🐍 Versatile programming language."},
]

# Display skills in boxes
cols = st.columns(3)  # 3 columns for the boxes
for i, skill in enumerate(skills):
    with cols[i % 3]:  # Distribute skills across columns
        st.markdown(
            f"""
            <div class="skill-box">
                <h3>{skill['name']}</h3>
                <p>{skill['description']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Display the title
st.markdown("<h3 style='text-align: center; color: rgb(0, 120, 212);'><br>My Core Skills in Different Sectors!</h3>", unsafe_allow_html=True)

# HTML structure for skills
html_code = """
    <div class='skill-container'>
        <div class='skill'>
            <div class='circle figma'>85%</div>
            <p style="color: rgb(0, 120, 212); font-size: 16px;">Figma</p>
        </div>
        <div class='skill'>
            <div class='circle html'>75%</div>
            <p style="color: rgb(0, 120, 212); font-size: 16px;">HTML</p>
        </div>
        <div class='skill'>
            <div class='circle css'>95%</div>
            <p style="color:rgb(0, 120, 212); font-size: 16px;">CSS</p>
        </div>
        <div class='skill'>
            <div class='circle nextjs'>80%</div>
            <p style="color: rgb(0, 120, 212); font-size: 16px;">Next.js</p>
        </div>
        <div class='skill'>
            <div class='circle python'>85%</div>
            <p style="color: rgb(0, 120, 212); font-size: 16px;">Python</p>
        </div>
        <div class='skill'>
            <div class='circle typescript'>70%</div>
            <p style="color: rgb(0, 120, 212); font-size: 16px;">TypeScript</p>
        </div>
    </div>
"""

# Render the HTML in Streamlit
st.markdown(html_code, unsafe_allow_html=True)





# --- FOOTER WITH SOCIAL LINKS ---
st.markdown(
    """
    <div class="footer">
        <div class="social-links">
            <a href="https://github.com/aamnaashraf" target="_blank">GitHub</a>
            <a href="https://www.linkedin.com/in/aamna-ashraf-rajput-552a20280?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" target="_blank">LinkedIn</a>
        </div>
        <p>Made with ❤️ by <a href="https://github.com/aamnaashraf" target="_blank">Aamna Ashraf Rajput</a></p>
    </div>
    """,
    unsafe_allow_html=True,
)