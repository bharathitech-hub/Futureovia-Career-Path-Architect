import streamlit as st

# App Setup
st.set_page_config(page_title="Futureovia", layout="centered")
st.title("🔮 Futureovia")
st.subheader("Career Path Architect for Tech Aspirants")
st.markdown("Empowering you to discover, align, and grow in your tech journey.")

# User Profile Input
st.markdown("### 👤 Enter Your Profile Details")

name = st.text_input("Enter your full name")

experience_level = st.selectbox("Your Experience Level", ["Fresher", "0-1 Years", "1-3 Years"])

education = st.selectbox(
    "Select Your Education Qualification",
    [
        "B.Sc Computer Science",
        "B.Sc Information Technology",
        "B.Sc Data Science",
        "B.Sc Artificial Intelligence",
        "B.Sc Mathematics",
        "B.Sc Electronics",
        "B.Sc Statistics",
        "BCA – Bachelor of Computer Applications",
        "BBA Information Technology",
        "B.Com Computer Applications",
        "B.E Computer Science Engineering",
        "B.E Information Technology",
        "B.Tech Computer Science",
        "B.Tech Information Technology",
        "B.Tech Artificial Intelligence & Data Science",
        "B.Tech Data Science",
        "B.Tech Electronics and Communication (ECE)",
        "B.Tech Electrical Engineering (with CS elective)",
        "M.Sc Computer Science",
        "M.Sc Information Technology",
        "M.Sc Data Science",
        "M.Sc Artificial Intelligence",
        "MCA – Master of Computer Applications",
        "M.Tech Computer Science",
        "M.Tech Information Technology",
        "M.Tech Data Science",
        "Diploma in Computer Science",
        "Diploma in Information Technology",
        "Diploma in Web Development",
        "Diploma in Data Science",
        "PG Diploma in AI & ML",
        "PG Diploma in Data Analytics",
        "PG Diploma in Cybersecurity",
        "Other (Specify Below)"
    ]
)

if education == "Other (Specify Below)":
    education = st.text_input("Please specify your qualification")

# Skill Input
st.markdown("### 💡 Select Your Current Skills")

skills = st.multiselect(
    "Choose the technical skills you already have:",
    [
        "Python", "Java", "C", "C++", "JavaScript", "TypeScript", "Go", "Ruby", "R", "Kotlin",
        "HTML", "CSS", "Bootstrap", "Tailwind CSS", "React", "Angular", "Vue.js", "Node.js", "Express.js",
        "SQL", "MySQL", "PostgreSQL", "MongoDB", "Firebase", "Redis", "SQLite",
        "AWS", "Azure", "Google Cloud Platform (GCP)", "Docker", "Kubernetes", "Jenkins", "Git", "GitHub", "CI/CD",
        "Pandas", "NumPy", "Matplotlib", "Seaborn", "Scikit-learn", "TensorFlow", "Keras", "OpenCV", "NLP", "Transformers",
        "Excel", "Power BI", "Tableau", "Google Data Studio", "ETL Tools",
        "Flutter", "React Native", "Swift", "Dart", "Android SDK",
        "Network Security", "Ethical Hacking", "Penetration Testing", "Wireshark", "Metasploit",
        "Blockchain", "Web3", "Figma", "REST APIs", "Agile", "Scrum", "Linux", "Shell Scripting"
    ]
)

# Show Recommendations
if st.button("🔍 Show My Career Path"):
    if not name or not skills:
        st.warning("Please enter your name and select at least one skill.")
    else:
        st.success("Here’s your personalized career path 👇")

        st.markdown("### 🎯 Recommended Roles Based on Your Skills")
        st.write("- Data Analyst")
        st.write("- Software Developer")
        st.write("- Front-End Developer")

        st.markdown("### 🔧 Skill Gaps Identified")
        st.write("- Cloud Computing (AWS/GCP)")
        st.write("- Data Structures & Algorithms")

        st.markdown("### 📘 Suggested Learning Path")
        st.write("1. Strengthen SQL and Python foundations")
        st.write("2. Learn version control with Git & GitHub")
        st.write("3. Practice real-world projects and system design")

# Footer
st.markdown("---")
st.caption("🔮 Built with love for future tech talent – Futureovia, 2025")
