# views/services.py
import streamlit as st

# Custom CSS for styling, animations, and horizontal layout
st.markdown(
    """
    <style>
    /* Flexbox container for horizontal layout */
    .horizontal-container {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        margin: 20px 0;
    }
    /* Service card styling */
    .service-card {
        border: 2px solid #FFD700; /* Yellow border */
        border-radius: 10px;
        padding: 20px;
        flex: 1 1 calc(33.333% - 40px);
        background-color: rgba(49, 51, 63, 0.05);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .service-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
    .service-card h3 {
        color: #2e86de;
        margin-bottom: 10px;
    }
    /* Testimonial card styling */
    .testimonial-card {
        border: 2px solid #FFD700; /* Yellow border */
        border-radius: 10px;
        padding: 20px;
        flex: 1 1 calc(33.333% - 40px);
        background-color: rgba(49, 51, 63, 0.05);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .testimonial-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
    .testimonial-card h4 {
        color: #2e86de;
        margin-bottom: 10px;
    }
    /* Animation for cards */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .service-card, .testimonial-card {
        animation: fadeIn 0.5s ease-out;
    }
    /* Dark mode adjustments */
    @media (prefers-color-scheme: dark) {
        .service-card, .testimonial-card {
            border-color: #FFD700; /* Yellow border */
            background-color: rgba(255, 255, 255, 0.05);
        }
        .service-card h3, .testimonial-card h4 {
            color: #4dabf7;
        }
    }
    /* Main heading styling */
      .main-heading {
        background: linear-gradient(135deg, #6a11cb, #2575fc); /* Gradient background */
        color: white;
        font-size: 36px; /* Slightly larger font size */
        padding: 25px;
        border-radius: 15px; /* Rounded corners */
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2); /* Subtle shadow */
        transition: all 0.3s ease-in-out; /* Smooth transition */
        border: 2px solid transparent; /* Transparent border for hover effect */
    }
    .main-heading:hover {
        transform: scale(1.02); /* Slight zoom on hover */
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3); /* Enhanced shadow on hover */
        border-color: #FFD700; /* Yellow border on hover */
    }
    .main-heading::before {
        content: "✨"; /* Emojis before the text */
        margin-right: 10px;
    }
    .main-heading::after {
        content: "✨"; /* Emojis after the text */
        margin-left: 10px;
    }
   /* Additional Text Section */
.closing-section {
    background: #1a1a1a;
    border-radius: 12px;
    padding: 3rem 2rem;
    margin: 3rem 0;
    text-align: center;
    border: 1px solid #2e2e2e;
    transition: all 0.3s ease-in-out;
}

/* Hover Effect for Closing Section */
.closing-section:hover {
    border-color: #76FF03;
    transform: translateY(-5px);
    box-shadow: 0 0 15px rgba(118, 255, 3, 0.4);
}

.closing-text {
    color: #ffffff;
    font-size: 1.1rem;
    line-height: 1.6;
    max-width: 800px;
    margin: 0 auto;
}

/* Contact Section */
.contact-section {
    background: #1a1a1a;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    text-align: center;
    border: 1px solid #2e2e2e;
    transition: all 0.3s ease-in-out;
}

/* Hover Effect for Contact Section */
.contact-section:hover {
    border-color: #64DD17;
    transform: translateY(-5px);
    box-shadow: 0 0 15px rgba(100, 221, 23, 0.5);
}

/* Contact Title */
.contact-title {
    color: #ffffff;
    font-size: 1.4rem;
    font-weight: 600;
    margin-bottom: 1.5rem;
    transition: color 0.3s ease-in-out;
}

/* Hover Effect for Contact Title */
.contact-section:hover .contact-title {
    color: #76FF03;
}

/* Contact Info */
.contact-info {
    color: #ffffff;
    font-size: 1.1rem;
    line-height: 1.6;
    transition: color 0.3s ease-in-out;
}

/* Hover Effect for Contact Info */
.contact-section:hover .contact-info {
    color: #76FF03;
}
    </style>
    """,
    unsafe_allow_html=True,
)

# Page Title with Updated Styling
st.markdown('<div class="main-heading">My Services as a Web Developer</div>', unsafe_allow_html=True)
st.write("Here are the services I offer:")

# Services Section
st.header("📦 Services")

# Horizontal layout for services
st.markdown('<div class="horizontal-container">', unsafe_allow_html=True)

# Service 1: Web Development
st.markdown(
    """
    <div class="service-card">
        <h3>🌐 Web Development</h3>
        <ul>
            <li><strong>Frontend Development</strong>: Building responsive and user-friendly interfaces using HTML, CSS, JavaScript, and modern frameworks like React.</li>
            <li><strong>Backend Development</strong>: Developing robust server-side applications using Python, Node.js, and databases like PostgreSQL and MongoDB.</li>
            <li><strong>Full-Stack Development</strong>: Comprehensive web solutions from frontend to backend, ensuring seamless integration and performance.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# Service 2: Web Design
st.markdown(
    """
    <div class="service-card">
        <h3>🎨 Web Design</h3>
        <ul>
            <li><strong>UI/UX Design</strong>: Creating intuitive and visually appealing designs that enhance user experience.</li>
            <li><strong>Wireframing & Prototyping</strong>: Developing wireframes and prototypes to visualize the final product before development.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# Service 3: Consulting & Maintenance
st.markdown(
    """
    <div class="service-card">
        <h3>🔧 Consulting & Maintenance</h3>
        <ul>
            <li><strong>Technical Consulting</strong>: Providing expert advice on web technologies, architecture, and best practices.</li>
            <li><strong>Website Maintenance</strong>: Regular updates, bug fixes, and performance optimization to keep your website running smoothly.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('</div>', unsafe_allow_html=True)

# Custom CSS for styling with hover and transition effects
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 2em;
            font-weight: bold;
            color: #2e86de;
            padding-bottom: 20px;
        }

        .testimonial {
            background-color: #111;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            border: 2px solid #444;
            transition: all 0.3s ease-in-out;
        }

        .testimonial:hover {
            background-color: #222;
            border-color: #76FF03;
            transform: translateY(-5px);
            box-shadow: 0 0 15px rgba(118, 255, 3, 0.5);
        }

        .highlight {
            background-color: #76FF03;
            color: black;
            border: 2px solid black;
            transition: all 0.3s ease-in-out;
        }

        .highlight:hover {
            background-color: #64DD17;
            border-color: black;
            transform: translateY(-5px);
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.5);
        }

        .profile {
            width: 60px;
            height: 60px;
            background-color: gray;
            color: white;
            font-size: 20px;
            font-weight: bold;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0 auto 10px;
            transition: all 0.3s ease-in-out;
        }

        .testimonial:hover .profile {
            background-color: black;
        }

        .highlight .profile {
            background-color: black;
        }

        .quote {
            font-size: 24px;
            color: #76FF03;
        }

        .highlight .quote {
            color: black;
        }

        .name {
            font-weight: bold;
            font-size: 18px;
            margin-bottom: 10px;
        }

        .desc {
            color: #bbb;
        }

        .highlight .desc {
            color: black;
            font-weight: 500;
        }
    </style>
""", unsafe_allow_html=True)

# Display section title
st.markdown('<div class="title">What My Clients Say!</div>', unsafe_allow_html=True)

# Create 3 columns for side-by-side layout
col1, col2, col3 = st.columns(3)

# Left Testimonial
with col1:
    st.markdown("""
        <div class="testimonial">
            <div class="profile">JB</div>
            <div class="name">Jerome Bell</div>
            <div class="desc">"Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia consequat duis enim velit mollit."</div>
            <div class="quote">“”</div>
        </div>
    """, unsafe_allow_html=True)

# Center Highlighted Testimonial
with col2:
    st.markdown("""
        <div class="testimonial highlight">
            <div class="profile">JB</div>
            <div class="name">Jerome Bell</div>
            <div class="desc">"Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia consequat duis enim velit mollit."</div>
            <div class="quote">“”</div>
        </div>
    """, unsafe_allow_html=True)

# Right Testimonial
with col3:
    st.markdown("""
        <div class="testimonial">
            <div class="profile">JB</div>
            <div class="name">Jerome Bell</div>
            <div class="desc">"Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia consequat duis enim velit mollit."</div>
            <div class="quote">“”</div>
        </div>
    """, unsafe_allow_html=True)

# Additional Text Section
st.markdown("""
<div class="closing-section">
    <div class="closing-text">
        Let's create something extraordinary together. With a focus on user-centered design 
        and cutting-edge technology, I deliver solutions that not only look stunning but 
        also drive measurable results. Get in touch to discuss your next digital project.
    </div>
</div>
""", unsafe_allow_html=True)

# Contact Section
st.markdown("""
<div class="contact-section">
    <div class="contact-title">📞 Contact Me</div>
    <div class="contact-info">
        <p>Phone: 03342570180</p>
        <p>Email: aamnaashraf501@gmail.com</p>
    </div>
</div>
""", unsafe_allow_html=True)

