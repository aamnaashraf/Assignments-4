import streamlit as st
import base64

# Function to encode image as Base64
def get_image_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# --- PAGE TITLE ---
st.title("My Projects!")

# Custom CSS for project cards and technology boxes
st.markdown(
    """
    <style>
    /* Project Cards */
    .project-card {
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        background-color: #2d2d2d;
        margin: 20px 0;
        border: 1px solid #0078d4;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.5);
        border-color: #00b4d8;
    }
    .project-card img {
    width: full;
    height: auto;
    border-radius: 10px;
    margin-bottom: 15px;
    display: block; /* Ensures the image behaves as a block element */
    margin-left: auto; /* Centers the image horizontally */
    margin-right: auto; /* Centers the image horizontally */
}
    .project-card h3 {
        font-size: 2.5rem;
        color: #00b4d8;
        margin-bottom: 10px;
        text-align: center;
    }
    .project-card p {
        font-size: 1rem;
        color: #a0a0a0;
        margin-bottom: 15px;
        text-align: center;
    }
    .project-card a {
        color: #00b4d8;
        text-decoration: none;
        margin-right: 10px;
        transition: color 0.3s;
    }
    .project-card a:hover {
        color: #0078d4;
    }
      /* Professional Message */
    .professional-message {
        text-align: center;
        font-size: 1.2rem;
        color: #00b4d8;
        margin-top: 40px;
        padding: 20px;
        background-color: #2d2d2d;
        border-radius: 15px;
        border: 1px solid #0078d4;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }
    .professional-message a {
        color: #00b4d8;
        text-decoration: none;
        transition: color 0.3s;
    }
    .professional-message a:hover {
        color: #0078d4;
    }

    /* Technology Boxes */
    .tech-box {
        display: inline-block;
        padding: 5px 10px;
        border-radius: 5px;
        background-color: #0078d4;
        color: white;
        font-size: 0.9rem;
        margin: 5px 5px 5px 0;
    }
    .tech-box.html { background-color: #e34c26; } /* HTML */
    .tech-box.css { background-color: #264de4; } /* CSS */
    .tech-box.js { background-color: #f0db4f; color: black; } /* JavaScript */
    .tech-box.ts { background-color: #3178c6; } /* TypeScript */
    .tech-box.nextjs { background-color: #000000; } /* Next.js */
    .tech-box.react { background-color: #61dafb; color: black; } /* React */
    .tech-box.nodejs { background-color: #68a063; } /* Node.js */
    .tech-box.python { background-color: #3776ab; } /* Python */
    .tech-box.streamlit { background-color: #ff4b4b; } /* Streamlit */
    .tech-box.firebase { background-color: #ffcb2b; color: black; } /* Firebase */
    .tech-box.mongodb { background-color: #4db33d; } /* MongoDB */
    .tech-box.tailwind { background-color: #38b2ac; } /* Tailwind CSS */
    .tech-box.stripe { background-color: #008cdd; } /* Stripe API */
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to create a project card
def create_project_card(title, description, image_path, technologies, github_link, demo_link):
    # Encode image as Base64
    image_base64 = get_image_base64(image_path)
    st.markdown(
        f"""
        <div class="project-card">
            <h3>{title}</h3>
            <img src="data:image/png;base64,{image_base64}" alt="{title}">
            <p>{description}</p>
            <div>
                {" ".join([f'<span class="tech-box {tech.lower()}">{tech}</span>' for tech in technologies])}
            </div>
            <br>
            <a href="{github_link}" target="_blank">GitHub</a>
            <a href="{demo_link}" target="_blank">Live Demo</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# --- PROJECT 1: E-Commerce Website ---
create_project_card(
    title="🛍️ E-Commerce Website",
    description="A fully functional e-commerce website built with Next.js. Features include product listings, a shopping cart, and user authentication.",
    image_path="views/images/furniture website.png",
    technologies=["Next.js", "TypeScript", "Tailwind CSS", "Stripe API"],
    github_link="https://github.com/aamnaashraf/final-hackathon.git",
    demo_link="https://final-hackathon-alpha-six.vercel.app/",
)

# --- PROJECT 2: Tour Website ---
create_project_card(
    title="🌍 Tour Website",
    description="A travel and tour booking website built with React and Node.js. Users can browse destinations, book tours, and manage their bookings.",
    image_path="views/images/tour website.png",
    technologies=["React", "Node.js", "MongoDB"],
    github_link="https://github.com/aamnaashraf/simple-website-with-tailwind-CSS.git",
    demo_link="https://simple-website-with-tailwind-css.vercel.app/",
)

# --- PROJECT 3: Blog Website ---
create_project_card(
    title="📝 Blog Website",
    description="A blogging platform where users can create, read, update, and delete posts. Built with Next.js and Firebase.",
    image_path="views/images/blog website.png",
    technologies=["Next.js", "Firebase", "Tailwind CSS"],
    github_link="https://github.com/aamnaashraf/Dynamic-blog-project.git",
    demo_link="https://dynamic-blog-project.vercel.app/",
)

# --- PROJECT 4: BMI Calculator ---
create_project_card(
    title="🧮 BMI Calculator",
    description="A simple BMI calculator built with Python and Streamlit. Users can input their height and weight to calculate their BMI.",
    image_path="views/images/calculater.PNG",
    technologies=["Python", "Streamlit"],
    github_link="https://github.com/aamnaashraf/BMI-calculator-2.git",
    demo_link="https://bmi-calculator-2.streamlit.app/",
)

# --- PROJECT 5: Unit Converter ---
create_project_card(
    title="📏 Unit Converter",
    description="A unit conversion tool built with Python and Streamlit. Converts units like length, weight, temperature, and more.",
    image_path="views/images/unit conveeter.png",
    technologies=["Python", "Streamlit"],
    github_link="https://github.com/aamnaashraf/Unit-converter.git",
    demo_link="https://unit-converter-aamna-ashraf.streamlit.app/",
)

# --- PROJECT 6: TypeScript Projects ---
create_project_card(
    title="💻 TypeScript Projects",
    description="A collection of small projects built with TypeScript, including a to-do app, weather app, and more.",
    image_path="views/images/typescript2.png",
    technologies=["TypeScript", "React", "Node.js"],
    github_link="https://github.com/aamnaashraf/Todo-List.git",
    demo_link="https://unit-converter.streamlit.app",
)

# --- PROJECT 7: Static Resume Builder ---
create_project_card(
    title="📄 Static Resume Builder",
    description="A static resume builder that allows users to create and download professional resumes in PDF format.",
    image_path="views/images/resume.png",  
    technologies=["HTML", "CSS", "JavaScript"],
    github_link="https://github.com/aamnaashraf/Static-resume-mile-stone-1.git",
    demo_link="https://static-resume-mile-stone-1.vercel.app/",
)

# --- PROJECT 8: Shareable Resume ---
create_project_card(
    title="🔗 Editable Resume",
    description="A web-based resume builder that generates shareable links for resumes. Users can customize and share their resumes online.",
    image_path="views/images/resume2.png",  
    technologies=["React", "Firebase", "Tailwind CSS"],
    github_link="https://github.com/aamnaashraf/Shareable-resume-milestone-5.git",
    demo_link="https://shareable-resume-milestone-5-beta.vercel.app/",
)

# --- PROFESSIONAL MESSAGE ---
st.markdown(
    """
    <div class="professional-message">
        <p>Thank you for exploring my projects! 🚀</p>
        <p>If you'd like to collaborate or discuss opportunities, feel free to <a href="mailto:your.email@example.com">reach out</a>.</p>
    </div>
    """,
    unsafe_allow_html=True,
)