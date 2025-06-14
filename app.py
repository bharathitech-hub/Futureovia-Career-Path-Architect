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
# Python
st.write("- Data Analyst")
st.write("- Backend Developer")
st.write("- Machine Learning Engineer")

# Java
st.write("- Backend Developer")
st.write("- Android Developer")
st.write("- Enterprise Application Engineer")

# C
st.write("- Embedded Systems Engineer")
st.write("- Firmware Developer")
st.write("- System Programmer")

# C++
st.write("- Game Developer")
st.write("- Performance Engineer")
st.write("- Systems Software Engineer")

# JavaScript
st.write("- Frontend Developer")
st.write("- Full Stack Developer")
st.write("- Web Application Developer")

# TypeScript
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Go
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Ruby
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# R
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Kotlin
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# HTML
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# CSS
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Bootstrap
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Tailwind CSS
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# React
st.write("- Frontend Developer")
st.write("- React.js Developer")
st.write("- Web UI Engineer")

# Angular
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Vue.js
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Node.js
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Express.js
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# SQL
st.write("- Data Analyst")
st.write("- Database Developer")
st.write("- BI Analyst")

# MySQL
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# PostgreSQL
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# MongoDB
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Firebase
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Redis
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# SQLite
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# AWS
st.write("- Cloud Engineer")
st.write("- DevOps Engineer")
st.write("- Solutions Architect")

# Azure
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Google Cloud Platform (GCP)
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Docker
st.write("- DevOps Engineer")
st.write("- Cloud Infrastructure Engineer")
st.write("- Containerization Specialist")

# Kubernetes
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Jenkins
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Git
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# GitHub
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# CI/CD
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Pandas
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# NumPy
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Matplotlib
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Seaborn
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Scikit-learn
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# TensorFlow
st.write("- Machine Learning Engineer")
st.write("- Deep Learning Specialist")
st.write("- AI Research Engineer")

# Keras
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# OpenCV
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# NLP
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Transformers
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Excel
st.write("- Data Analyst")
st.write("- Reporting Analyst")
st.write("- Operations Associate")

# Power BI
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Tableau
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Google Data Studio
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# ETL Tools
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Flutter
st.write("- Mobile App Developer")
st.write("- Flutter Developer")
st.write("- Cross-Platform App Developer")

# React Native
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Swift
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Dart
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Android SDK
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Network Security
st.write("- Cybersecurity Analyst")
st.write("- Network Security Engineer")
st.write("- SOC Analyst")

# Ethical Hacking
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Penetration Testing
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Wireshark
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Metasploit
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Blockchain
st.write("- Blockchain Developer")
st.write("- Smart Contract Engineer")
st.write("- Web3 Developer")

# Web3
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Figma
st.write("- UI/UX Designer")
st.write("- Product Designer")
st.write("- Interaction Designer")

# REST APIs
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Agile
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Scrum
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Linux
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

# Shell Scripting
st.write("- Software Developer")
st.write("- Full Stack Developer")
st.write("- Technical Associate")

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
