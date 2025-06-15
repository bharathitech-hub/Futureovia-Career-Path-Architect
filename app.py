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
        "Blockchain", "Web3", "Figma", "REST APIs", "Agile", "Scrum", "Linux", "Shell Scripting",
          "Artificial Intelligence", "Machine Learning", "Deep Learning", "Natural Language Processing (NLP)",
         "Computer Vision", "Large Language Models (LLMs)", "Prompt Engineering", "Generative AI",
         "Recommendation Systems", "AI Ethics & Governance", "Amazon Web Services (AWS)", "Microsoft Azure",
         "Google Cloud Platform (GCP)", "Serverless Architecture", "Cloud Monitoring (Prometheus, Grafana)",
        "Cloud Networking", "Edge Computing", "Cloud Storage Solutions", "Cloud Security", "Docker", "Kubernetes",
        "Terraform", "CI/CD Pipelines (GitHub Actions, GitLab CI/CD)", "Infrastructure as Code (IaC)", "Ansible",
       "Jenkins", "GitOps", "ArgoCD", "DevSecOps", "Identity & Access Management (IAM)", "Penetration Testing",
       "Zero Trust Architecture", "Threat Intelligence", "Secure Coding Practices", "Vulnerability Assessment",
       "Red Teaming", "SOC Operations", "Blockchain Security", "Application Security"

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

# Artificial Intelligence
st.write("- AI Engineer")
st.write("- AI Product Analyst")
st.write("- AI Solutions Architect")

# Machine Learning
st.write("- Machine Learning Engineer")
st.write("- ML Ops Engineer")
st.write("- Predictive Modeling Specialist")

# Deep Learning
st.write("- Deep Learning Engineer")
st.write("- AI Researcher")
st.write("- Computer Vision Specialist")

# Natural Language Processing (NLP)
st.write("- NLP Engineer")
st.write("- Conversational AI Developer")
st.write("- Text Analytics Specialist")

# Computer Vision
st.write("- Computer Vision Engineer")
st.write("- AI Imaging Specialist")
st.write("- Autonomous Systems Developer")

# Large Language Models (LLMs)
st.write("- LLM Engineer")
st.write("- Prompt Engineer")
st.write("- AI Research Engineer")

# Prompt Engineering
st.write("- Prompt Engineer")
st.write("- AI Application Specialist")
st.write("- LLM Consultant")

# Generative AI
st.write("- Generative AI Engineer")
st.write("- Creative AI Developer")
st.write("- AI Innovation Specialist")

# Recommendation Systems
st.write("- Recommendation System Engineer")
st.write("- Data Scientist")
st.write("- Personalization Engineer")

# AI Ethics & Governance
st.write("- Responsible AI Specialist")
st.write("- AI Policy Analyst")
st.write("- Ethical AI Consultant")

# Amazon Web Services (AWS)
st.write("- Cloud Engineer")
st.write("- Solutions Architect")
st.write("- DevOps Engineer")

# Microsoft Azure
st.write("- Azure Engineer")
st.write("- Cloud Administrator")
st.write("- Cloud Solutions Consultant")

# Google Cloud Platform (GCP)
st.write("- GCP Engineer")
st.write("- Cloud Infrastructure Specialist")
st.write("- Cloud Developer")

# Serverless Architecture
st.write("- Serverless Developer")
st.write("- Cloud Backend Engineer")
st.write("- Solutions Architect")

# Cloud Monitoring (Prometheus, Grafana)
st.write("- Site Reliability Engineer")
st.write("- Monitoring Specialist")
st.write("- DevOps Engineer")

# Cloud Networking
st.write("- Cloud Network Engineer")
st.write("- Cloud Security Engineer")
st.write("- Infrastructure Architect")

# Edge Computing
st.write("- Edge Developer")
st.write("- IoT Systems Engineer")
st.write("- Embedded Cloud Engineer")

# Cloud Storage Solutions
st.write("- Cloud Storage Engineer")
st.write("- Data Infrastructure Engineer")
st.write("- Cloud Operations Specialist")

# Cloud Security
st.write("- Cloud Security Engineer")
st.write("- Security Analyst")
st.write("- IAM Specialist")

# Docker
st.write("- DevOps Engineer")
st.write("- Containerization Specialist")
st.write("- Infrastructure Engineer")

# Kubernetes
st.write("- Kubernetes Engineer")
st.write("- DevOps Engineer")
st.write("- Cloud Orchestrator")

# Terraform
st.write("- Infrastructure Engineer")
st.write("- DevOps Specialist")
st.write("- IaC Consultant")

# CI/CD Pipelines (GitHub Actions, GitLab CI/CD)
st.write("- DevOps Engineer")
st.write("- CI/CD Engineer")
st.write("- Automation Specialist")

# Infrastructure as Code (IaC)
st.write("- IaC Engineer")
st.write("- Cloud Automation Engineer")
st.write("- DevOps Consultant")

# Ansible
st.write("- Automation Engineer")
st.write("- Configuration Manager")
st.write("- DevOps Specialist")

# Jenkins
st.write("- CI/CD Engineer")
st.write("- DevOps Engineer")
st.write("- Build Engineer")

# GitOps
st.write("- GitOps Engineer")
st.write("- Cloud Developer")
st.write("- Infrastructure DevOps Engineer")

# ArgoCD
st.write("- DevOps Engineer")
st.write("- GitOps Engineer")
st.write("- Deployment Automation Specialist")

# DevSecOps
st.write("- DevSecOps Engineer")
st.write("- Security Automation Specialist")
st.write("- Cloud Security Developer")

# Identity & Access Management (IAM)
st.write("- IAM Engineer")
st.write("- Security Analyst")
st.write("- Access Governance Specialist")

# Penetration Testing
st.write("- Penetration Tester")
st.write("- Security Consultant")
st.write("- Vulnerability Analyst")

# Zero Trust Architecture
st.write("- Security Architect")
st.write("- Zero Trust Engineer")
st.write("- Network Security Consultant")

# Threat Intelligence
st.write("- Threat Intelligence Analyst")
st.write("- Cybersecurity Analyst")
st.write("- Security Researcher")

# Secure Coding Practices
st.write("- Security Software Engineer")
st.write("- Application Security Analyst")
st.write("- Code Auditor")

# Vulnerability Assessment
st.write("- Security Analyst")
st.write("- Risk Assessor")
st.write("- Vulnerability Management Specialist")

# Red Teaming
st.write("- Red Team Specialist")
st.write("- Offensive Security Engineer")
st.write("- Security Analyst")

# SOC Operations
st.write("- SOC Analyst")
st.write("- Security Operations Engineer")
st.write("- Incident Response Specialist")

# Blockchain Security
st.write("- Blockchain Security Engineer")
st.write("- Smart Contract Auditor")
st.write("- Crypto Security Analyst")

# Application Security
st.write("- AppSec Engineer")
st.write("- Secure Software Developer")
st.write("- Security Compliance Analyst")


st.markdown("### 🔧 Skill Gaps Identified: Data Analyst")
st.write("- Data Visualization (Tableau/Power BI)")
st.write("- SQL Optimization")
st.write("- Business Acumen")

st.markdown("### 🔧 Skill Gaps Identified: Backend Developer")
st.write("- API Security")
st.write("- Database Scaling")
st.write("- CI/CD Pipelines")

st.markdown("### 🔧 Skill Gaps Identified: Machine Learning Engineer")
st.write("- Model Deployment")
st.write("- Feature Engineering")
st.write("- MLOps Tools")

st.markdown("### 🔧 Skill Gaps Identified: Frontend Developer")
st.write("- Web Performance Optimization")
st.write("- Accessibility (a11y)")
st.write("- Component Testing")

st.markdown("### 🔧 Skill Gaps Identified: DevOps Engineer")
st.write("- Infrastructure as Code (IaC)")
st.write("- Monitoring (Prometheus/Grafana)")
st.write("- Kubernetes Clustering")

st.markdown("### 🔧 Skill Gaps Identified: Full Stack Developer")
st.write("- API Gateway Integration")
st.write("- Deployment Strategies")
st.write("- End-to-End Testing")

st.markdown("### 🔧 Skill Gaps Identified: Cloud Engineer")
st.write("- Serverless Architecture")
st.write("- IAM Policies")
st.write("- Disaster Recovery Planning")

st.markdown("### 🔧 Skill Gaps Identified: AI Engineer")
st.write("- Responsible AI Practices")
st.write("- Model Interpretability")
st.write("- Scalable AI Systems")

st.markdown("### 🔧 Skill Gaps Identified: Data Scientist")
st.write("- Hypothesis Testing")
st.write("- Model Explainability (SHAP/LIME)")
st.write("- Real-Time Analytics")

st.markdown("### 🔧 Skill Gaps Identified: UI/UX Designer")
st.write("- Design Systems (Figma/Sketch)")
st.write("- Usability Testing")
st.write("- Micro-interactions")

st.markdown("### 🔧 Skill Gaps Identified: Mobile App Developer")
st.write("- Cross-Platform Debugging")
st.write("- App Store Optimization (ASO)")
st.write("- Performance Profiling")

st.markdown("### 🔧 Skill Gaps Identified: Embedded Systems Engineer")
st.write("- Real-Time OS Concepts")
st.write("- Hardware-Software Integration")
st.write("- Memory Optimization")

st.markdown("### 🔧 Skill Gaps Identified: Firmware Developer")
st.write("- Low-Level Driver Development")
st.write("- Bootloader Programming")
st.write("- Power Management Techniques")

st.markdown("### 🔧 Skill Gaps Identified: Game Developer")
st.write("- Game Physics")
st.write("- Rendering Optimization")
st.write("- Cross-Platform Deployment")

st.markdown("### 🔧 Skill Gaps Identified: Cybersecurity Analyst")
st.write("- Threat Hunting")
st.write("- SIEM Tools (Splunk/ELK)")
st.write("- Vulnerability Scanning")

st.markdown("### 🔧 Skill Gaps Identified: Blockchain Developer")
st.write("- Smart Contract Testing")
st.write("- Layer 2 Solutions")
st.write("- Wallet Integration")

st.markdown("### 🔧 Skill Gaps Identified: Smart Contract Auditor")
st.write("- Static Analysis Tools")
st.write("- Formal Verification")
st.write("- Attack Vector Identification")

st.markdown("### 🔧 Skill Gaps Identified: Data Engineer")
st.write("- Distributed Data Processing (Spark/Hadoop)")
st.write("- Data Pipeline Orchestration (Airflow)")
st.write("- Data Lake Architecture")

st.markdown("### 🔧 Skill Gaps Identified: AI Product Analyst")
st.write("- Model Evaluation Metrics")
st.write("- A/B Testing for AI Features")
st.write("- Stakeholder Communication")

st.markdown("### 🔧 Skill Gaps Identified: Site Reliability Engineer")
st.write("- SLAs, SLOs, and SLIs")
st.write("- Observability Tools")
st.write("- Chaos Engineering")

 st.markdown("### 🔧 Skill Gaps Identified: UI/UX Designer")
st.write("- Design Systems")
st.write("- User Research Methods")
st.write("- Accessibility Standards")

st.markdown("### 🔧 Skill Gaps Identified: DevOps Engineer")
st.write("- CI/CD Automation")
st.write("- Infrastructure as Code (IaC)")
st.write("- Monitoring and Logging Tools")

st.markdown("### 🔧 Skill Gaps Identified: Cloud Engineer")
st.write("- Multi-Cloud Strategy")
st.write("- Cost Optimization")
st.write("- Hybrid Cloud Management")

st.markdown("### 🔧 Skill Gaps Identified: NLP Engineer")
st.write("- Tokenization Techniques")
st.write("- Language Model Fine-Tuning")
st.write("- Text Embedding Models")

st.markdown("### 🔧 Skill Gaps Identified: Computer Vision Engineer")
st.write("- Image Augmentation")
st.write("- Object Detection Frameworks")
st.write("- Model Compression")

st.markdown("### 🔧 Skill Gaps Identified: Full Stack Developer")
st.write("- API Security")
st.write("- Scalable Architecture Design")
st.write("- Performance Monitoring")

st.markdown("### 🔧 Skill Gaps Identified: AI Research Engineer")
st.write("- Literature Review Skills")
st.write("- Benchmarking Techniques")
st.write("- Reproducibility in Research")

st.markdown("### 🔧 Skill Gaps Identified: Security Analyst")
st.write("- Threat Modeling")
st.write("- Incident Response Planning")
st.write("- Log Correlation Analysis")

st.markdown("### 🔧 Skill Gaps Identified: SOC Analyst")
st.write("- Intrusion Detection Systems")
st.write("- Threat Intelligence Feeds")
st.write("- Security Playbooks")

st.markdown("### 🔧 Skill Gaps Identified: GitOps Engineer")
st.write("- GitOps Workflow Design")
st.write("- Kubernetes Integration")
st.write("- Rollback Strategy")

st.markdown("### 🔧 Skill Gaps Identified: CI/CD Engineer")
st.write("- Pipeline Orchestration")
st.write("- Rollback Mechanisms")
st.write("- Secrets Management")

st.markdown("### 🔧 Skill Gaps Identified: Data Engineer")
st.write("- Real-Time Data Pipelines")
st.write("- Data Lake Architecture")
st.write("- Data Lineage Tracking")

st.markdown("### 🔧 Skill Gaps Identified: Product Manager")
st.write("- User-Centered Design Principles")
st.write("- Agile Metrics")
st.write("- Product Lifecycle Planning")

st.markdown("### 🔧 Skill Gaps Identified: Technical Writer")
st.write("- API Documentation Standards")
st.write("- Markdown and Sphinx Usage")
st.write("- Version Control for Docs")

st.markdown("### 🔧 Skill Gaps Identified: Mobile App Developer")
st.write("- Cross-Platform Compatibility")
st.write("- App Store Optimization (ASO)")
st.write("- Offline Mode Handling")

st.markdown("### 🔧 Skill Gaps Identified: Ethical Hacker")
st.write("- Web App Security Testing")
st.write("- Exploit Development")
st.write("- Social Engineering Techniques")

st.markdown("### 🔧 Skill Gaps Identified: Blockchain Developer")
st.write("- Smart Contract Security")
st.write("- Consensus Algorithms")
st.write("- Gas Optimization")

st.markdown("### 🔧 Skill Gaps Identified: Game Developer")
st.write("- Physics Engines")
st.write("- Game Monetization Models")
st.write("- Cross-Platform Game Porting")

st.markdown("### 🔧 Skill Gaps Identified: Business Analyst")
st.write("- Stakeholder Communication")
st.write("- Requirement Gathering Techniques")
st.write("- Business Process Modeling")

st.markdown("### 🔧 Skill Gaps Identified: Data Architect")
st.write("- Enterprise Data Modeling")
st.write("- Data Governance Frameworks")
st.write("- Metadata Management")

st.markdown("### 🔧 Skill Gaps Identified: AI Researcher")
st.write("- Scientific Paper Reproduction")
st.write("- Research Experiment Design")
st.write("- Novel Algorithm Development")

st.markdown("### 🔧 Skill Gaps Identified: Software Tester")
st.write("- Test Case Design Techniques")
st.write("- Automation Frameworks")
st.write("- Continuous Testing Integration")

st.markdown("### 🔧 Skill Gaps Identified: Site Reliability Engineer")
st.write("- High Availability Design")
st.write("- Incident Management Practices")
st.write("- Infrastructure Monitoring Tools")

st.markdown("### 🔧 Skill Gaps Identified: Security Analyst")
st.write("- Threat Hunting Techniques")
st.write("- Malware Analysis Basics")
st.write("- Security Information and Event Management (SIEM)")

st.markdown("### 🔧 Skill Gaps Identified: Cloud Developer")
st.write("- Serverless Application Design")
st.write("- Cloud SDK Usage")
st.write("- Cross-Cloud Portability")

st.markdown("### 🔧 Skill Gaps Identified: Edge Computing Engineer")
st.write("- Low Latency Optimization")
st.write("- Edge Node Management")
st.write("- Fog vs. Edge Paradigms")

st.markdown("### 🔧 Skill Gaps Identified: UI/UX Designer")
st.write("- Accessibility Guidelines")
st.write("- Wireframing Tools Mastery")
st.write("- Design System Implementation")

st.markdown("### 🔧 Skill Gaps Identified: Prompt Engineer")
st.write("- Prompt Chaining Techniques")
st.write("- Instruction Tuning Awareness")
st.write("- Multi-Model Prompting")

st.markdown("### 🔧 Skill Gaps Identified: Database Administrator (DBA)")
st.write("- Index Optimization")
st.write("- Backup and Recovery Strategies")
st.write("- Query Execution Plan Analysis")

st.markdown("### 🔧 Skill Gaps Identified: Full Stack Engineer")
st.write("- Microfrontend Architecture")
st.write("- SSR & SSG Techniques")
st.write("- Deployment Automation")

st.markdown("### 🔧 Skill Gaps Identified: Data Architect")
st.write("- Data Lake Architecture")
st.write("- Data Lineage Tools")
st.write("- Enterprise Data Modeling")

st.markdown("### 🔧 Skill Gaps Identified: Computer Vision Engineer")
st.write("- Object Detection Tuning")
st.write("- Image Augmentation Techniques")
st.write("- Real-Time Inference Optimization")

st.markdown("### 🔧 Skill Gaps Identified: MLOps Engineer")
st.write("- ML Pipeline Automation")
st.write("- Model Versioning Systems")
st.write("- CI/CD for ML Workflows")

st.markdown("### 🔧 Skill Gaps Identified: DevSecOps Engineer")
st.write("- Secure CI/CD Integration")
st.write("- Static Code Analysis Tools")
st.write("- Secrets Management")

st.markdown("### 🔧 Skill Gaps Identified: Automation Tester")
st.write("- Scriptless Testing Tools")
st.write("- Selenium Advanced Commands")
st.write("- Parallel Test Execution")

st.markdown("### 🔧 Skill Gaps Identified: NLP Engineer")
st.write("- Text Preprocessing Pipelines")
st.write("- Named Entity Recognition")
st.write("- Transformers Fine-Tuning")

st.markdown("### 🔧 Skill Gaps Identified: Cloud Security Engineer")
st.write("- Cloud-native Security Services")
st.write("- IAM Policies Configuration")
st.write("- Vulnerability Remediation in Cloud")

st.markdown("### 🔧 Skill Gaps Identified: Embedded Systems Engineer")
st.write("- RTOS Configuration")
st.write("- Memory-Constrained Programming")
st.write("- Hardware Abstraction Techniques")

st.markdown("### 🔧 Skill Gaps Identified: Data Visualization Specialist")
st.write("- Storytelling with Data")
st.write("- Interactive Dashboards")
st.write("- Cross-Platform Visualization Tools")

st.markdown("### 🔧 Skill Gaps Identified: Systems Software Engineer")
st.write("- Kernel Module Development")
st.write("- Thread Management Techniques")
st.write("- Systems-Level Debugging")

st.markdown("### 🔧 Skill Gaps Identified: Data Science Manager")
st.write("- Team Workflow Automation")
st.write("- Business Impact Evaluation")
st.write("- Scalable Data Science Practices")

st.markdown("### 🔧 Skill Gaps Identified: Information Security Analyst")
st.write("- Threat Modeling Techniques")
st.write("- SIEM Tools Usage")
st.write("- Cyber Risk Frameworks")

st.markdown("### 🔧 Skill Gaps Identified: QA Engineer")
st.write("- Test Strategy Design")
st.write("- Bug Lifecycle Management")
st.write("- Regression Suite Optimization")

st.markdown("### 🔧 Skill Gaps Identified: API Developer")
st.write("- API Gateway Management")
st.write("- Throttling & Rate Limiting")
st.write("- OAuth 2.0 & JWT Handling")

st.markdown("### 🔧 Skill Gaps Identified: Security Analyst")
st.write("- Incident Detection Tools")
st.write("- Attack Surface Mapping")
st.write("- Endpoint Protection Platforms")

st.markdown("### 🔧 Skill Gaps Identified: AI Product Manager")
st.write("- AI Roadmap Planning")
st.write("- Model Lifecycle Awareness")
st.write("- Cross-Functional AI Strategy")

st.markdown("### 🔧 Skill Gaps Identified: Robotics Engineer")
st.write("- Motion Planning Algorithms")
st.write("- Robotic Sensor Fusion")
st.write("- ROS-based Development")

st.markdown("### 🔧 Skill Gaps Identified: Infrastructure Engineer")
st.write("- Multi-cloud Strategy")
st.write("- High Availability Design")
st.write("- Infrastructure Monitoring Tools")

st.markdown("### 🔧 Skill Gaps Identified: Full Stack Engineer")
st.write("- Microservices Architecture")
st.write("- SSR & CSR Implementation")
st.write("- CI/CD Deployment Pipelines")

st.markdown("### 🔧 Skill Gaps Identified: Technical Program Manager")
st.write("- Agile Risk Assessment")
st.write("- Dev Team Cross-Collaboration")
st.write("- Technical Estimation Techniques")

st.markdown("### 🔧 Skill Gaps Identified: Technical Writer")
st.write("- API Documentation Standards")
st.write("- Git-based Content Management")
st.write("- Tooling (MadCap Flare, DITA)")

st.markdown("### 🔧 Skill Gaps Identified: Mobile App Developer")
st.write("- State Management Techniques")
st.write("- CI/CD for Mobile Apps")
st.write("- Platform-Specific Performance Tuning")

st.markdown("### 🔧 Skill Gaps Identified: Release Engineer")
st.write("- Release Lifecycle Planning")
st.write("- Rollback & Recovery Strategies")
st.write("- Release Automation Frameworks")

st.markdown("### 🔧 Skill Gaps Identified: SEO Specialist")
st.write("- Technical SEO Auditing")
st.write("- Structured Data Markup")
st.write("- Core Web Vitals Optimization")

st.markdown("### 🔧 Skill Gaps Identified: AR/VR Developer")
st.write("- Unity/Unreal Engine Proficiency")
st.write("- ARKit/ARCore SDKs")
st.write("- Immersive Experience Design")

st.markdown("### 🔧 Skill Gaps Identified: Game Developer")
st.write("- Game Physics Optimization")
st.write("- Multi-platform Deployment")
st.write("- Real-time Rendering Techniques")

st.markdown("### 🔧 Skill Gaps Identified: Data Architect")
st.write("- Data Vault Modeling")
st.write("- Cross-System Data Flow Design")
st.write("- Metadata Management")

st.markdown("### 🔧 Skill Gaps Identified: Database Administrator (DBA)")
st.write("- Query Performance Tuning")
st.write("- Backup & Disaster Recovery Plans")
st.write("- Multi-Tenant Database Management")

st.markdown("### 🔧 Skill Gaps Identified: UI/UX Designer")
st.write("- A/B Testing Methodologies")
st.write("- Accessibility Standards (WCAG)")
st.write("- User Flow Optimization")

st.markdown("### 🔧 Skill Gaps Identified: Chatbot Developer")
st.write("- Dialog Management Frameworks")
st.write("- Multilingual NLP Pipelines")
st.write("- Bot Analytics Integration")

st.markdown("### 🔧 Skill Gaps Identified: DevSecOps Engineer")
st.write("- Secure CI/CD Integration")
st.write("- SAST & DAST Tools")
st.write("- Compliance as Code")

st.markdown("### 🔧 Skill Gaps Identified: Prompt Engineer")
st.write("- Effective Prompt Structuring")
st.write("- Model Behavior Understanding")
st.write("- Use-case Adaptation Techniques")

st.markdown("### 🔧 Skill Gaps Identified: Computer Vision Engineer")
st.write("- Object Detection Models (YOLO/RCNN)")
st.write("- Image Preprocessing Pipelines")
st.write("- Real-time Inference Optimization")

st.markdown("### 🔧 Skill Gaps Identified: Data Governance Analyst")
st.write("- Data Privacy Laws (GDPR, CCPA)")
st.write("- Data Lineage Tools")
st.write("- Stewardship Policies")

st.markdown("### 🔧 Skill Gaps Identified: SOC Analyst")
st.write("- Threat Detection Techniques")
st.write("- Log Analysis Using SIEMs")
st.write("- Incident Escalation Procedures")

st.markdown("### 🔧 Skill Gaps Identified: LLM Developer")
st.write("- Model Fine-Tuning Strategies")
st.write("- Tokenization Mechanics")
st.write("- Instruction-Tuning Concepts")

st.markdown("### 🔧 Skill Gaps Identified: Data Storyteller")
st.write("- Narrative Framing Techniques")
st.write("- Visual Encoding Principles")
st.write("- Stakeholder-Centric Storytelling")

st.markdown("### 🔧 Skill Gaps Identified: Edge AI Engineer")
st.write("- On-device Model Deployment")
st.write("- Hardware Acceleration (TPU/NPU)")
st.write("- Power-efficient Inference")

st.markdown("### 🔧 Skill Gaps Identified: Integration Engineer")
st.write("- API Gateway Configurations")
st.write("- Middleware Patterns")
st.write("- System Interface Testing")

st.markdown("### 🔧 Skill Gaps Identified: Digital Marketing Analyst")
st.write("- Campaign Attribution Models")
st.write("- Ad Platform APIs (Google/Facebook)")
st.write("- Conversion Funnel Analysis")

st.markdown("### 🔧 Skill Gaps Identified: Backend Developer")
st.write("- API Architecture Best Practices")
st.write("- Asynchronous Programming")
st.write("- Database Optimization Techniques")

st.markdown("### 🔧 Skill Gaps Identified: Frontend Developer")
st.write("- Component-based Architecture")
st.write("- State Management (Redux, Context API)")
st.write("- Cross-Browser Compatibility")

st.markdown("### 🔧 Skill Gaps Identified: Blockchain Security Engineer")
st.write("- Smart Contract Vulnerabilities")
st.write("- Security Auditing Frameworks")
st.write("- On-chain Monitoring Tools")

st.markdown("### 🔧 Skill Gaps Identified: Technical Program Manager")
st.write("- Agile Portfolio Management")
st.write("- Cross-functional Alignment Techniques")
st.write("- Technical Risk Mitigation")

st.markdown("### 🔧 Skill Gaps Identified: Site Reliability Engineer (SRE)")
st.write("- SLIs, SLOs, and Error Budgets")
st.write("- Reliability Engineering Metrics")
st.write("- Chaos Engineering Tools")

st.markdown("### 🔧 Skill Gaps Identified: Data Architect")
st.write("- Data Modeling Frameworks")
st.write("- Storage Layer Abstractions")
st.write("- Data Lifecycle Design")

st.markdown("### 🔧 Skill Gaps Identified: Bioinformatics Analyst")
st.write("- Genomic Data Processing")
st.write("- Biological Database Querying")
st.write("- Sequence Alignment Techniques")

st.markdown("### 🔧 Skill Gaps Identified: Simulation Engineer")
st.write("- Mathematical Modeling Techniques")
st.write("- Simulation Frameworks (MATLAB/Simulink)")
st.write("- Numerical Stability Analysis")

st.markdown("### 🔧 Skill Gaps Identified: Robotics Engineer")
st.write("- Motion Planning Algorithms")
st.write("- ROS (Robot Operating System)")
st.write("- Sensor Fusion Techniques")

st.markdown("### 🔧 Skill Gaps Identified: Systems Software Engineer")
st.write("- Kernel Module Development")
st.write("- Low-Level Debugging")
st.write("- Real-Time OS Concepts")

# 📘 Suggested Learning Path for First 10 Roles

st.markdown("### 📘 Suggested Learning Path - Data Analyst")
st.write("1. Master Excel, SQL, and data visualization tools (Tableau/Power BI)")
st.write("2. Learn Python for data analysis (Pandas, NumPy)")
st.write("3. Practice EDA and storytelling with real datasets")

st.markdown("### 📘 Suggested Learning Path - Backend Developer")
st.write("1. Deepen knowledge of server-side languages (Java, Python, Node.js)")
st.write("2. Learn REST APIs, databases, and authentication")
st.write("3. Practice building scalable backend systems")

st.markdown("### 📘 Suggested Learning Path - Machine Learning Engineer")
st.write("1. Master Python and ML libraries (Scikit-learn, TensorFlow)")
st.write("2. Study ML theory and real-world use cases")
st.write("3. Work on end-to-end ML projects with deployment")

st.markdown("### 📘 Suggested Learning Path - Android Developer")
st.write("1. Learn Kotlin and Android SDK")
st.write("2. Build mobile apps with modern UI/UX principles")
st.write("3. Explore Firebase integration and app deployment")

st.markdown("### 📘 Suggested Learning Path - Embedded Systems Engineer")
st.write("1. Gain strong understanding of C/C++ and microcontrollers")
st.write("2. Learn hardware-software interfacing")
st.write("3. Work on embedded systems projects (Arduino, Raspberry Pi)")

st.markdown("### 📘 Suggested Learning Path - Firmware Developer")
st.write("1. Learn low-level programming with C/C++")
st.write("2. Understand memory management and real-time systems")
st.write("3. Build and debug firmware for embedded hardware")

st.markdown("### 📘 Suggested Learning Path - System Programmer")
st.write("1. Master C/C++ and Linux internals")
st.write("2. Learn about operating systems and multithreading")
st.write("3. Contribute to open-source systems projects")

st.markdown("### 📘 Suggested Learning Path - Game Developer")
st.write("1. Learn C++, Unity, or Unreal Engine")
st.write("2. Practice building 2D/3D games")
st.write("3. Study game physics, mechanics, and optimization")

st.markdown("### 📘 Suggested Learning Path - Performance Engineer")
st.write("1. Understand software architecture and bottleneck analysis")
st.write("2. Learn profiling tools and optimization techniques")
st.write("3. Conduct stress testing and performance tuning")

st.markdown("### 📘 Suggested Learning Path - Systems Software Engineer")
st.write("1. Learn C/C++, operating systems, and compilers")
st.write("2. Explore system calls and hardware interfaces")
st.write("3. Build tools, drivers, and systems utilities")
# 📘 Suggested Learning Path for Roles 11–20

st.markdown("### 📘 Suggested Learning Path - Frontend Developer")
st.write("1. Learn HTML, CSS, JavaScript, and responsive design")
st.write("2. Master frameworks like React or Angular")
st.write("3. Build interactive UIs and optimize performance")

st.markdown("### 📘 Suggested Learning Path - Full Stack Developer")
st.write("1. Learn frontend (React/Angular) and backend (Node.js/Python)")
st.write("2. Understand databases, REST APIs, and deployment")
st.write("3. Build full-stack apps with authentication and CI/CD")

st.markdown("### 📘 Suggested Learning Path - Web Application Developer")
st.write("1. Learn web fundamentals and MVC frameworks")
st.write("2. Work with APIs, session management, and security")
st.write("3. Build scalable and responsive web applications")

st.markdown("### 📘 Suggested Learning Path - Software Developer")
st.write("1. Strengthen core programming skills (OOP, DSA)")
st.write("2. Explore development tools, version control, and testing")
st.write("3. Contribute to real-world software projects")

st.markdown("### 📘 Suggested Learning Path - Technical Associate")
st.write("1. Build foundational understanding of SDLC and software tools")
st.write("2. Learn basic coding, databases, and support tools")
st.write("3. Gain exposure to real-time software maintenance")

st.markdown("### 📘 Suggested Learning Path - React.js Developer")
st.write("1. Learn JavaScript ES6+ and React fundamentals")
st.write("2. Practice building SPA with routing and hooks")
st.write("3. Explore performance optimization and testing")

st.markdown("### 📘 Suggested Learning Path - Web UI Engineer")
st.write("1. Master frontend tech stack (HTML, CSS, JS, React)")
st.write("2. Study UX design principles and component libraries")
st.write("3. Build pixel-perfect responsive UIs")

st.markdown("### 📘 Suggested Learning Path - Enterprise Application Engineer")
st.write("1. Learn Java EE/Spring, databases, and enterprise design patterns")
st.write("2. Understand microservices and integration with APIs")
st.write("3. Work on scalable, secure enterprise solutions")

st.markdown("### 📘 Suggested Learning Path - Android Developer (Java)")
st.write("1. Learn Java, Android SDK, and activity lifecycle")
st.write("2. Build mobile UIs with XML and Jetpack components")
st.write("3. Deploy and test apps on Android devices")

st.markdown("### 📘 Suggested Learning Path - Data Structures & Algorithms Trainer")
st.write("1. Gain mastery over DSA concepts and patterns")
st.write("2. Practice problem-solving with LeetCode, HackerRank")
st.write("3. Teach others via workshops, blogs, or videos")
# 📘 Suggested Learning Path for Roles 21–30

st.markdown("### 📘 Suggested Learning Path - Embedded Systems Engineer")
st.write("1. Learn C/C++ and microcontroller programming")
st.write("2. Understand RTOS, memory management, and hardware interfaces")
st.write("3. Work on embedded projects using Arduino, Raspberry Pi")

st.markdown("### 📘 Suggested Learning Path - Firmware Developer")
st.write("1. Master low-level programming in C")
st.write("2. Learn device drivers, debugging, and bootloaders")
st.write("3. Work with real-time embedded systems")

st.markdown("### 📘 Suggested Learning Path - System Programmer")
st.write("1. Learn system-level programming in C/C++ or Rust")
st.write("2. Understand operating systems, memory, and processes")
st.write("3. Contribute to open-source system tools")

st.markdown("### 📘 Suggested Learning Path - Game Developer")
st.write("1. Learn C++ and game engines like Unity or Unreal")
st.write("2. Study game physics, rendering, and asset integration")
st.write("3. Build and publish your own games")

st.markdown("### 📘 Suggested Learning Path - Performance Engineer")
st.write("1. Understand system performance metrics and profiling tools")
st.write("2. Learn optimization strategies and low-level debugging")
st.write("3. Conduct performance tuning and stress testing")

st.markdown("### 📘 Suggested Learning Path - Systems Software Engineer")
st.write("1. Learn OS concepts, compilers, and C/C++ programming")
st.write("2. Study systems architecture and concurrent programming")
st.write("3. Work on scalable systems-level software")

st.markdown("### 📘 Suggested Learning Path - Backend Developer")
st.write("1. Learn backend frameworks (Node.js, Django, Spring Boot)")
st.write("2. Understand databases, APIs, and cloud deployment")
st.write("3. Practice with scalable server-side applications")

st.markdown("### 📘 Suggested Learning Path - Cloud Engineer")
st.write("1. Learn cloud platforms (AWS, Azure, GCP)")
st.write("2. Understand compute, networking, storage, and IAM")
st.write("3. Build and deploy cloud-native applications")

st.markdown("### 📘 Suggested Learning Path - DevOps Engineer")
st.write("1. Master CI/CD pipelines, Docker, and Kubernetes")
st.write("2. Learn infrastructure automation (Terraform, Ansible)")
st.write("3. Implement monitoring and scaling strategies")

st.markdown("### 📘 Suggested Learning Path - Solutions Architect")
st.write("1. Understand system design and cloud architecture")
st.write("2. Learn cost-optimized and scalable architecture design")
st.write("3. Get certified in AWS, Azure, or GCP architecture")
# 📘 Suggested Learning Path for Roles 21–30

st.markdown("### 📘 Suggested Learning Path - Embedded Systems Engineer")
st.write("1. Learn C/C++ and microcontroller programming")
st.write("2. Understand RTOS, memory management, and hardware interfaces")
st.write("3. Work on embedded projects using Arduino, Raspberry Pi")

st.markdown("### 📘 Suggested Learning Path - Firmware Developer")
st.write("1. Master low-level programming in C")
st.write("2. Learn device drivers, debugging, and bootloaders")
st.write("3. Work with real-time embedded systems")

st.markdown("### 📘 Suggested Learning Path - System Programmer")
st.write("1. Learn system-level programming in C/C++ or Rust")
st.write("2. Understand operating systems, memory, and processes")
st.write("3. Contribute to open-source system tools")

st.markdown("### 📘 Suggested Learning Path - Game Developer")
st.write("1. Learn C++ and game engines like Unity or Unreal")
st.write("2. Study game physics, rendering, and asset integration")
st.write("3. Build and publish your own games")

st.markdown("### 📘 Suggested Learning Path - Performance Engineer")
st.write("1. Understand system performance metrics and profiling tools")
st.write("2. Learn optimization strategies and low-level debugging")
st.write("3. Conduct performance tuning and stress testing")

st.markdown("### 📘 Suggested Learning Path - Systems Software Engineer")
st.write("1. Learn OS concepts, compilers, and C/C++ programming")
st.write("2. Study systems architecture and concurrent programming")
st.write("3. Work on scalable systems-level software")

st.markdown("### 📘 Suggested Learning Path - Backend Developer")
st.write("1. Learn backend frameworks (Node.js, Django, Spring Boot)")
st.write("2. Understand databases, APIs, and cloud deployment")
st.write("3. Practice with scalable server-side applications")

st.markdown("### 📘 Suggested Learning Path - Cloud Engineer")
st.write("1. Learn cloud platforms (AWS, Azure, GCP)")
st.write("2. Understand compute, networking, storage, and IAM")
st.write("3. Build and deploy cloud-native applications")

st.markdown("### 📘 Suggested Learning Path - DevOps Engineer")
st.write("1. Master CI/CD pipelines, Docker, and Kubernetes")
st.write("2. Learn infrastructure automation (Terraform, Ansible)")
st.write("3. Implement monitoring and scaling strategies")

st.markdown("### 📘 Suggested Learning Path - Solutions Architect")
st.write("1. Understand system design and cloud architecture")
st.write("2. Learn cost-optimized and scalable architecture design")
st.write("3. Get certified in AWS, Azure, or GCP architecture")
# 📘 Suggested Learning Path for Roles 41–50

st.markdown("### 📘 Suggested Learning Path - Mobile App Developer")
st.write("1. Learn Dart with Flutter or React Native")
st.write("2. Understand UI/UX principles for mobile")
st.write("3. Build and publish apps on Android/iOS platforms")

st.markdown("### 📘 Suggested Learning Path - Flutter Developer")
st.write("1. Master Dart and Flutter framework")
st.write("2. Create responsive UIs and handle state management")
st.write("3. Build and deploy cross-platform applications")

st.markdown("### 📘 Suggested Learning Path - Cross-Platform App Developer")
st.write("1. Learn Flutter or React Native for app development")
st.write("2. Integrate APIs and manage local storage")
st.write("3. Test and optimize apps for performance")

st.markdown("### 📘 Suggested Learning Path - UI/UX Designer")
st.write("1. Study design principles and usability heuristics")
st.write("2. Learn Figma, Adobe XD, or Sketch")
st.write("3. Build interactive prototypes and gather user feedback")

st.markdown("### 📘 Suggested Learning Path - Product Designer")
st.write("1. Understand product thinking and user research")
st.write("2. Create design systems and high-fidelity prototypes")
st.write("3. Collaborate with developers for implementation")

st.markdown("### 📘 Suggested Learning Path - Interaction Designer")
st.write("1. Learn motion design and interaction flows")
st.write("2. Study user psychology and micro-interactions")
st.write("3. Build engaging and intuitive UI components")

st.markdown("### 📘 Suggested Learning Path - Backend Developer")
st.write("1. Learn backend languages like Python, Java, or Node.js")
st.write("2. Understand REST APIs, databases, and authentication")
st.write("3. Build and deploy scalable backend systems")

st.markdown("### 📘 Suggested Learning Path - Embedded Systems Engineer")
st.write("1. Learn C/C++ for embedded development")
st.write("2. Understand microcontrollers and hardware interfacing")
st.write("3. Practice on Arduino, Raspberry Pi, or STM32 platforms")

st.markdown("### 📘 Suggested Learning Path - Firmware Developer")
st.write("1. Master C and Assembly for low-level programming")
st.write("2. Learn hardware-software interfacing techniques")
st.write("3. Test and debug firmware on embedded devices")

st.markdown("### 📘 Suggested Learning Path - System Programmer")
st.write("1. Learn C/C++ and systems-level APIs")
st.write("2. Understand OS concepts like memory, threads, and I/O")
st.write("3. Work on low-level tools or device drivers")
# 📘 Suggested Learning Path for Roles 51–60

st.markdown("### 📘 Suggested Learning Path - Game Developer")
st.write("1. Learn C++ and game development frameworks like Unity or Unreal")
st.write("2. Understand game physics, animation, and graphics")
st.write("3. Build and test complete game projects")

st.markdown("### 📘 Suggested Learning Path - Performance Engineer")
st.write("1. Study systems architecture and bottleneck identification")
st.write("2. Learn performance profiling and optimization techniques")
st.write("3. Work on memory management, concurrency, and scaling")

st.markdown("### 📘 Suggested Learning Path - Systems Software Engineer")
st.write("1. Master C/C++ and system-level libraries")
st.write("2. Learn OS internals and hardware interaction")
st.write("3. Contribute to open-source system utilities or drivers")

st.markdown("### 📘 Suggested Learning Path - DevOps Engineer")
st.write("1. Learn CI/CD pipelines and containerization tools like Docker")
st.write("2. Explore monitoring tools, logging, and infrastructure automation")
st.write("3. Practice deployment on cloud platforms (AWS, GCP, Azure)")

st.markdown("### 📘 Suggested Learning Path - Cloud Engineer")
st.write("1. Learn cloud fundamentals and service models (IaaS, PaaS, SaaS)")
st.write("2. Gain hands-on with AWS, GCP, or Azure")
st.write("3. Build scalable and secure cloud infrastructure")

st.markdown("### 📘 Suggested Learning Path - Solutions Architect")
st.write("1. Study system design and architecture patterns")
st.write("2. Understand cloud-native application strategies")
st.write("3. Practice designing scalable solutions using case studies")

st.markdown("### 📘 Suggested Learning Path - Site Reliability Engineer")
st.write("1. Learn system monitoring, observability, and automation")
st.write("2. Understand incident response, SLAs, and SLOs")
st.write("3. Work with Prometheus, Grafana, and cloud logs")

st.markdown("### 📘 Suggested Learning Path - Monitoring Specialist")
st.write("1. Learn time-series data and log management")
st.write("2. Practice with tools like Prometheus, ELK Stack, or Grafana")
st.write("3. Set up real-time alerting and dashboard visualization")

st.markdown("### 📘 Suggested Learning Path - Containerization Specialist")
st.write("1. Learn Docker architecture and image management")
st.write("2. Create and manage multi-container applications")
st.write("3. Integrate with orchestration platforms like Kubernetes")

st.markdown("### 📘 Suggested Learning Path - Kubernetes Engineer")
st.write("1. Master Kubernetes architecture and configurations")
st.write("2. Deploy, scale, and secure Kubernetes clusters")
st.write("3. Automate deployments using Helm and GitOps")
# 📘 Suggested Learning Path for Roles 61–70

st.markdown("### 📘 Suggested Learning Path - Infrastructure Engineer")
st.write("1. Learn networking, system administration, and virtualization")
st.write("2. Understand IaC tools like Terraform and Ansible")
st.write("3. Practice building robust, scalable infrastructure setups")

st.markdown("### 📘 Suggested Learning Path - CI/CD Engineer")
st.write("1. Learn CI/CD tools like Jenkins, GitHub Actions, or GitLab CI")
st.write("2. Automate build, test, and deployment processes")
st.write("3. Implement pipeline security and rollback strategies")

st.markdown("### 📘 Suggested Learning Path - Automation Specialist")
st.write("1. Learn scripting with Python, Shell, or PowerShell")
st.write("2. Automate workflows with Ansible, Jenkins, or Zapier")
st.write("3. Apply automation in system admin, testing, and DevOps")

st.markdown("### 📘 Suggested Learning Path - GitOps Engineer")
st.write("1. Understand Git-based infrastructure and deployment")
st.write("2. Learn tools like ArgoCD or Flux")
st.write("3. Implement GitOps pipelines for production environments")

st.markdown("### 📘 Suggested Learning Path - Cloud Developer")
st.write("1. Learn cloud SDKs (AWS SDK, Firebase, etc.)")
st.write("2. Build cloud-native and serverless applications")
st.write("3. Focus on scalability, authentication, and cost optimization")

st.markdown("### 📘 Suggested Learning Path - Deployment Automation Specialist")
st.write("1. Learn CI/CD and infrastructure-as-code tools")
st.write("2. Automate deployment pipelines using Jenkins, ArgoCD")
st.write("3. Implement blue-green and canary deployments")

st.markdown("### 📘 Suggested Learning Path - DevSecOps Engineer")
st.write("1. Understand security in the DevOps lifecycle")
st.write("2. Use tools like SonarQube, Snyk, and Trivy")
st.write("3. Integrate security testing into pipelines")

st.markdown("### 📘 Suggested Learning Path - Security Automation Specialist")
st.write("1. Learn security scripting and automation tools")
st.write("2. Implement automated security scans in CI/CD")
st.write("3. Practice automating compliance and alerting")

st.markdown("### 📘 Suggested Learning Path - IAM Specialist")
st.write("1. Understand access control models (RBAC, ABAC)")
st.write("2. Learn identity platforms like Okta, AWS IAM")
st.write("3. Implement SSO, MFA, and user lifecycle management")

st.markdown("### 📘 Suggested Learning Path - Security Analyst")
st.write("1. Study network security and vulnerability management")
st.write("2. Learn SIEM tools like Splunk or QRadar")
st.write("3. Analyze logs, monitor alerts, and generate incident reports")
# 71. Blockchain Developer
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Learn blockchain basics and distributed ledgers")
st.write("2. Master Solidity and Ethereum development")
st.write("3. Build and deploy decentralized applications (dApps)")

# 72. Blockchain Security Engineer
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Learn secure smart contract development")
st.write("2. Study vulnerabilities (e.g., reentrancy, overflow)")
st.write("3. Practice auditing smart contracts and using security tools")

# 73. Smart Contract Auditor
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Understand EVM and Solidity architecture")
st.write("2. Learn manual and automated contract auditing methods")
st.write("3. Explore tools like Mythril and Slither")

# 74. Crypto Security Analyst
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Understand cryptographic protocols and wallets")
st.write("2. Analyze threats and vulnerabilities in DeFi protocols")
st.write("3. Monitor on-chain transactions and exploit patterns")

# 75. AppSec Engineer (Application Security)
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Learn secure software development lifecycle (SSDLC)")
st.write("2. Master threat modeling and vulnerability scanning")
st.write("3. Practice code reviews and static/dynamic analysis")

# 76. Secure Software Developer
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Write secure code following OWASP standards")
st.write("2. Learn authentication, encryption, and data protection")
st.write("3. Integrate security into CI/CD pipelines")

# 77. Security Compliance Analyst
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Understand compliance frameworks (ISO, NIST, SOC2)")
st.write("2. Learn risk assessments and security audits")
st.write("3. Monitor policies and ensure regulatory alignment")

# 78. Red Team Specialist
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Learn offensive security tactics and tools")
st.write("2. Master social engineering and advanced penetration testing")
st.write("3. Simulate real-world attacks for defense testing")

# 79. Offensive Security Engineer
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Study penetration testing and red teaming techniques")
st.write("2. Gain expertise in Kali Linux, Metasploit, Burp Suite")
st.write("3. Participate in CTFs and security research")

# 80. Security Analyst
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Master SIEM tools and incident analysis techniques")
st.write("2. Learn security frameworks and risk management")
st.write("3. Monitor alerts, logs, and anomalies continuously")
# 81. Malware Analyst
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Study malware types, behaviors, and indicators")
st.write("2. Learn reverse engineering using tools like IDA Pro")
st.write("3. Practice sandbox analysis and malware dissection")

# 82. Cyber Threat Analyst
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Understand threat intelligence lifecycle")
st.write("2. Use tools for threat detection and IOC correlation")
st.write("3. Track APT groups and analyze attack patterns")

# 83. Security Incident Responder
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Learn incident handling and forensics basics")
st.write("2. Gain expertise in SIEM and endpoint security tools")
st.write("3. Practice response playbooks and breach containment")

# 84. Penetration Tester
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Master vulnerability scanning and exploit development")
st.write("2. Get hands-on with tools like Nmap, Burp Suite, and Metasploit")
st.write("3. Practice reporting and communication of findings")

# 85. Cloud Security Engineer
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Learn cloud security best practices (AWS, Azure, GCP)")
st.write("2. Study IAM, encryption, and cloud compliance")
st.write("3. Implement secure cloud configurations and monitoring")

# 86. DevSecOps Engineer
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Integrate security into DevOps lifecycle")
st.write("2. Automate scanning and testing in CI/CD")
st.write("3. Learn container and secrets management")

# 87. Network Security Engineer
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Study firewalls, VPNs, and IDS/IPS")
st.write("2. Configure and monitor network devices")
st.write("3. Analyze traffic and respond to threats")

# 88. SOC Analyst (Security Operations Center)
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Understand SOC workflows and alert triaging")
st.write("2. Learn SIEM tools like Splunk or QRadar")
st.write("3. Practice identifying and responding to incidents")

# 89. Identity & Access Management (IAM) Engineer
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Learn access control models and identity governance")
st.write("2. Work with SSO, MFA, and directory services")
st.write("3. Implement policies for role-based access")

# 90. Cryptography Engineer
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Understand encryption algorithms and secure protocols")
st.write("2. Implement cryptographic primitives in applications")
st.write("3. Study PKI, TLS, and key management techniques")
# 91. Smart Contract Auditor
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Learn Solidity and smart contract development")
st.write("2. Study common vulnerabilities like reentrancy and overflows")
st.write("3. Use auditing tools and perform manual code reviews")

# 92. Web3 Developer
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Understand blockchain fundamentals and Ethereum")
st.write("2. Build dApps using Web3.js or Ethers.js")
st.write("3. Integrate wallets and smart contracts")

# 93. Blockchain Developer
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Learn blockchain architecture and consensus mechanisms")
st.write("2. Develop on platforms like Ethereum, Hyperledger, or Solana")
st.write("3. Create and deploy smart contracts")

# 94. AI Product Manager
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Understand AI/ML project lifecycles")
st.write("2. Learn data requirements and model evaluation")
st.write("3. Bridge communication between technical and business teams")

# 95. AI Researcher
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Deep dive into ML, DL, and NLP foundations")
st.write("2. Read and publish academic papers")
st.write("3. Experiment with models like Transformers and GANs")

# 96. MLOps Engineer
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Learn model deployment and monitoring tools")
st.write("2. Work with ML pipelines using MLflow, Kubeflow")
st.write("3. Automate retraining and CI/CD for ML models")

# 97. AI Ethics Specialist
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Study fairness, transparency, and accountability in AI")
st.write("2. Explore global AI regulations and ethical frameworks")
st.write("3. Advocate for responsible AI practices in products")

# 98. Data Governance Analyst
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Learn data privacy laws (GDPR, CCPA)")
st.write("2. Work with metadata management and data catalogs")
st.write("3. Develop policies for data quality and compliance")

# 99. Business Intelligence Analyst
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Master BI tools like Tableau or Power BI")
st.write("2. Learn data modeling and SQL querying")
st.write("3. Create dashboards and deliver insights to stakeholders")

# 100. NLP Engineer
st.markdown("### 📘 Suggested Learning Path")
st.write("1. Understand NLP basics and libraries (NLTK, SpaCy)")
st.write("2. Work on text preprocessing and sentiment analysis")
st.write("3. Build and fine-tune language models for tasks like classification")

# Footer
st.markdown("---")
st.caption("🔮 Built with love for future tech talent – Futureovia, 2025")
