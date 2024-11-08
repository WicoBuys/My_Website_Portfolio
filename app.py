import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path


# Function to send email
def send_email(name, email, message):
    sender_email = "your_email@example.com"  # Replace with your email
    receiver_email = "wico.pydev@gmail.com"
    password = "your_email_password"  # Replace with your email password

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "New Contact Form Submission"
    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        return "Email sent successfully!"
    except Exception as e:
        return f"Error sending email: {e}"


# Sidebar navigation menu
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Contact Us"])

# Custom CSS for styling, icons, and animations
st.markdown(
    """
    <style>
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css');

    .stApp {
        background-color: #333333;  /* Dark grey background */
        color: #ffffff;  /* Light text color */
        font-family: 'Roboto', sans-serif;
        overflow-y: auto;  /* Ensure vertical scroll bar */
    }
    body {
        background-color: #333333;  /* Dark grey background */
        font-family: 'Roboto Mono', monospace;
    }
    .project-card {
        background-color: #444444;  /* Slightly lighter grey for project cards */
        padding: 10px;
        margin: 10px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .project-card h3 {
        color: #1f77b4;
    }
    .project-card p {
        color: #dddddd;
    }
    .project-card a {
        color: #ff6347;
        text-decoration: none;
        font-weight: bold;
    }
    .project-card a:hover {
        text-decoration: underline;
    }
    .icon {
        margin-right: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

projects = [
    {
        "title": "Project 1",
        "description": "Description of Project 1",
        "github": "https://github.com/wicobuys",
        "app": "https://project1.app"
    },
    {
        "title": "Project 2",
        "description": "Description of Project 2",
        "github": "https://github.com/wicobuys",
        "app": "https://project2.app"
    },
    {
        "title": "Project 3",
        "description": "Description of Project 3",
        "github": "https://github.com/wicobuys",
        "app": "https://project3.app"
    },
    {
        "title": "Project 4",
        "description": "Description of Project 4",
        "github": "https://github.com/wicobuys",
        "app": "https://project4.app"
    },
    {
        "title": "Project 5",
        "description": "Description of Project 5",
        "github": "https://github.com/wicobuys",
        "app": "https://project5.app"
    },
    {
        "title": "Project 6",
        "description": "Description of Project 6",
        "github": "https://github.com/wicobuys",
        "app": "https://project6.app"
    },
    {
        "title": "Project 7",
        "description": "Description of Project 7",
        "github": "https://github.com/wicobuys",
        "app": "https://project7.app"
    },
    {
        "title": "Project 8",
        "description": "Description of Project 8",
        "github": "https://github.com/wicobuys",
        "app": "https://project8.app"
    }
]

if page == "Home":
    st.title("My Programming Projects")
    st.write(
        "Welcome to my portfolio! Explore my projects and see what I've been working on. Here's a brief overview of my skills and interests:")

    # Executive summary
    st.markdown(
        """
        I am a passionate programmer with experience in web development, data analysis, and machine learning. 
        My projects reflect my skills in Python, JavaScript, and various frameworks. I enjoy creating visually 
        appealing and functional applications. Below are some of my featured projects.
        """
    )

    # Animated header
    st.markdown(
        """
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
        <div class="animate__animated animate__bounce">
            <h3 style="color: #ffffff;">Featured Projects</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Smaller featured projects section
    col1, col2 = st.columns(2)

    for index, project in enumerate(projects):
        if index < 2:  # Display only two projects as featured
            with col1 if index % 2 == 0 else col2:
                st.markdown(f"""
                <div class="project-card animate__animated animate__fadeIn">
                    <h3>{project['title']}</h3>
                    <p>{project['description']}</p>
                    <p><a href="{project['github']}"><i class="fas fa-code icon"></i>GitHub Repository</a></p>
                    <p><a href="{project['app']}"><i class="fas fa-external-link-alt icon"></i>Live App</a></p>
                </div>
                """, unsafe_allow_html=True)

elif page == "Projects":
    st.title("All Projects")

    # Full project listing
    col1, col2 = st.columns(2)

    for index, project in enumerate(projects):
        with col1 if index % 2 == 0 else col2:
            st.markdown(f"""
            <div class="project-card animate__animated animate__fadeInUp">
                <h3>{project['title']}</h3>
                <p>{project['description']}</p>
                <p><a href="{project['github']}"><i class="fas fa-code icon"></i>GitHub Repository</a></p>
                <p><a href="{project['app']}"><i class="fas fa-external-link-alt icon"></i>Live App</a></p>
            </div>
            """, unsafe_allow_html=True)

elif page == "Contact Us":
    st.title("Contact Us")
    st.write(
        "Feel free to reach out via email at [wico.pydev@gmail.com](mailto:wico.pydev@gmail.com) or fill out the form below:")

    # Contact form
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send")

    if submit:
        response = send_email(name, email, message)
        st.success(response)

# Footer
st.markdown(
    """
    <div class="footer">
        <p>© 2024 Wico Buys. All rights reserved.</p>
        <p>Contact: <a href="mailto:wico.pydev@gmail.com">wico.pydev@gmail.com</a></p>
    </div>
    """,
    unsafe_allow_html=True
)