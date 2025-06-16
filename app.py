import streamlit as st

st.set_page_config(page_title="Futureovia", layout="centered")
st.title("🔮 Futureovia")
st.subheader("Career Path Architect for Tech Aspirants")

st.markdown("### 👋 Welcome to Futureovia!")
st.markdown("""
This tool empowers you to explore tech skills, discover aligned career roles, identify your skill gaps, and follow a personalized learning path.

#### 🚀 How to Use:
1. **Click** on a skill you want to explore.  
2. **View** the top 3 career roles suggested for that skill.  
3. **Expand** each role to see the required skills vs your current skills.  
4. **Follow** the suggested learning path to close the gap.  

💡 *Ideal for students, freshers, and professionals navigating their tech journey.*
""")
skill_data = {
    "Python": {
        "roles": ["Data Analyst", "Backend Developer", "ML Engineer"],
        "gap": ["SQL", "Pandas", "OOP in Python"],
        "path": [
            "Master Python basics and OOP",
            "Work with Pandas and NumPy",
            "Build small data analysis projects",
            "Learn how to create APIs with Flask or FastAPI",
            "Practice with LeetCode problems"
        ]
    },
    "JavaScript": {
        "roles": ["Frontend Developer", "Full Stack Developer", "Web App Engineer"],
        "gap": ["ES6+", "Async/Await", "DOM Manipulation"],
        "path": [
            "Understand ES6+ and modern syntax",
            "Work with DOM and browser events",
            "Build mini projects like to-do apps",
            "Explore frontend frameworks like React",
            "Practice API integration"
        ]
    },
    "SQL": {
        "roles": ["Data Analyst", "BI Developer", "Database Engineer"],
        "gap": ["Joins", "Window Functions", "Query Optimization"],
        "path": [
            "Understand relational databases",
            "Write complex queries with joins",
            "Practice window functions and CTEs",
            "Learn performance tuning techniques",
            "Apply in real-world database projects"
        ]
    },
    "Machine Learning": {
        "roles": ["ML Engineer", "AI Researcher", "ML Platform Engineer"],
        "gap": ["Model Deployment", "Feature Engineering", "Evaluation Metrics"],
        "path": [
            "Review ML algorithms and math behind them",
            "Focus on model evaluation and cross-validation",
            "Learn model deployment with Flask or FastAPI",
            "Build end-to-end ML projects",
            "Explore MLOps basics (DVC, MLflow)"
        ]
    },
    "Data Visualization": {
        "roles": ["Data Analyst", "BI Analyst", "Product Analyst"],
        "gap": ["Tableau", "Power BI", "Storytelling"],
        "path": [
            "Learn principles of visual storytelling",
            "Use Tableau or Power BI for dashboards",
            "Work on KPI-focused reports",
            "Practice with open datasets",
            "Combine visuals with business insight"
        ]
    },
    "AWS": {
        "roles": ["Cloud Engineer", "DevOps Engineer", "Solutions Architect"],
        "gap": ["IAM", "EC2", "S3", "CloudFormation"],
        "path": [
            "Understand basic cloud concepts",
            "Learn core AWS services like EC2, S3, IAM",
            "Try deploying a web app on EC2",
            "Use Lambda for serverless functions",
            "Explore Terraform or CloudFormation"
        ]
    },
    "Docker": {
        "roles": ["DevOps Engineer", "ML Ops Engineer", "Platform Engineer"],
        "gap": ["Dockerfile", "Image Optimization", "Networking"],
        "path": [
            "Install and configure Docker",
            "Learn how to write Dockerfiles",
            "Build and manage images and containers",
            "Work on containerized microservices",
            "Deploy containers using Docker Compose"
        ]
    },
    "React": {
        "roles": ["Frontend Developer", "Web App Developer", "UI Engineer"],
        "gap": ["Hooks", "State Management", "Component Design"],
        "path": [
            "Learn JSX and React components",
            "Use hooks like useState, useEffect",
            "Build reusable UI components",
            "Explore routing with React Router",
            "Connect to APIs and manage state"
        ]
    },
    "Linux": {
        "roles": ["DevOps Engineer", "Cloud Engineer", "Security Engineer"],
        "gap": ["Bash", "File Permissions", "Networking"],
        "path": [
            "Understand Linux file system and commands",
            "Work with bash scripting",
            "Manage permissions and processes",
            "Configure cron jobs and system services",
            "Debug network and performance issues"
        ]
    },
    "Git": {
        "roles": ["Software Developer", "DevOps Engineer", "Data Scientist"],
        "gap": ["Branching", "Merging", "Conflict Resolution"],
        "path": [
            "Understand version control concepts",
            "Practice git add, commit, push, pull",
            "Use branches for feature development",
            "Resolve conflicts and rebase",
            "Collaborate using GitHub or GitLab"
        ]
    }
}
    "HTML": {
        "roles": ["Frontend Developer", "Web Designer", "Email Developer"],
        "gap": ["Semantic Tags", "Forms", "Accessibility"],
        "path": [
            "Learn semantic HTML5 structure",
            "Build responsive forms",
            "Use tables and layout tags correctly",
            "Improve accessibility with ARIA",
            "Build and test HTML email templates"
        ]
    },
    "CSS": {
        "roles": ["Frontend Developer", "UI Designer", "Web Developer"],
        "gap": ["Flexbox", "Grid", "Animations"],
        "path": [
            "Understand box model and layout",
            "Practice Flexbox and Grid systems",
            "Style components with transitions",
            "Use preprocessors like SCSS",
            "Build responsive designs"
        ]
    },
    "TypeScript": {
        "roles": ["Frontend Developer", "Full Stack Developer", "App Developer"],
        "gap": ["Interfaces", "Generics", "Type Safety"],
        "path": [
            "Understand types, interfaces and enums",
            "Convert JS apps to TS",
            "Use types in React components",
            "Work with generics and utility types",
            "Debug and test TypeScript code"
        ]
    },
    "PostgreSQL": {
        "roles": ["Database Developer", "Data Engineer", "Backend Developer"],
        "gap": ["Indexing", "Stored Procedures", "Window Functions"],
        "path": [
            "Install and configure PostgreSQL",
            "Practice schema design",
            "Write efficient queries with indexes",
            "Work with advanced SQL functions",
            "Use pgAdmin and CLI tools"
        ]
    },
    "MongoDB": {
        "roles": ["Backend Developer", "Full Stack Developer", "Data Engineer"],
        "gap": ["Aggregation Pipeline", "Indexes", "Schema Design"],
        "path": [
            "Understand NoSQL concepts",
            "Perform CRUD operations",
            "Build schemas using Mongoose",
            "Explore aggregation framework",
            "Deploy MongoDB in production"
        ]
    },
    "Firebase": {
        "roles": ["App Developer", "Frontend Developer", "Full Stack Developer"],
        "gap": ["Authentication", "Firestore", "Hosting"],
        "path": [
            "Use Firebase for real-time database",
            "Set up auth and user management",
            "Host static apps",
            "Trigger functions on Firestore events",
            "Integrate with mobile/web apps"
        ]
    },
    "Tailwind CSS": {
        "roles": ["UI Developer", "Frontend Developer", "Web Designer"],
        "gap": ["Utility Classes", "Responsive Design", "Custom Themes"],
        "path": [
            "Learn utility-first concepts",
            "Build modern layouts",
            "Customize themes with Tailwind config",
            "Use Tailwind with frameworks like React",
            "Build landing pages and UI kits"
        ]
    },
    "Node.js": {
        "roles": ["Backend Developer", "Full Stack Developer", "API Developer"],
        "gap": ["Express.js", "Async Handling", "Middleware"],
        "path": [
            "Understand event loop and architecture",
            "Build REST APIs using Express.js",
            "Use middlewares and routing",
            "Connect to databases like MongoDB",
            "Deploy using PM2 or Docker"
        ]
    },
    "Express.js": {
        "roles": ["Backend Developer", "API Developer", "Full Stack Developer"],
        "gap": ["Routing", "Error Handling", "Middleware Logic"],
        "path": [
            "Learn routing basics",
            "Add validation and error handling",
            "Use async/await for APIs",
            "Secure routes with JWT",
            "Deploy with CI/CD"
        ]
    },
    "Pandas": {
        "roles": ["Data Analyst", "Data Scientist", "ML Engineer"],
        "gap": ["Data Cleaning", "Merging", "Aggregation"],
        "path": [
            "Load and manipulate DataFrames",
            "Clean and preprocess real-world data",
            "Work with groupby, merge, join",
            "Perform exploratory data analysis",
            "Create visual insights with Pandas & Matplotlib"
        ]
    },
    "Tableau": {
        "roles": ["Data Analyst", "BI Analyst", "Product Analyst"],
        "gap": ["Dashboard Design", "Data Blending", "Filters & Parameters"],
        "path": [
            "Install Tableau Public/Desktop",
            "Connect to data sources",
            "Build dashboards with filters",
            "Use calculated fields and parameters",
            "Publish and share dashboards"
        ]
    },
    "Power BI": {
        "roles": ["BI Analyst", "Data Analyst", "Reporting Specialist"],
        "gap": ["DAX", "Power Query", "Data Modeling"],
        "path": [
            "Understand Power BI architecture",
            "Use Power Query for ETL",
            "Model relationships and hierarchies",
            "Write DAX expressions",
            "Publish reports to Power BI Service"
        ]
    },
    "Java": {
        "roles": ["Backend Developer", "Android Developer", "Software Engineer"],
        "gap": ["OOP", "JVM", "Multithreading"],
        "path": [
            "Review OOP principles",
            "Understand JVM memory model",
            "Build REST APIs using Spring Boot",
            "Handle exceptions and multithreading",
            "Deploy using Maven or Gradle"
        ]
    },
    "Kotlin": {
        "roles": ["Android Developer", "Mobile App Developer", "Full Stack Developer"],
        "gap": ["Coroutines", "Extensions", "Jetpack"],
        "path": [
            "Understand Kotlin syntax",
            "Use extensions and collections",
            "Develop apps with Android Studio",
            "Implement navigation and Jetpack",
            "Handle background tasks with coroutines"
        ]
    },
    "C++": {
        "roles": ["System Programmer", "Game Developer", "Embedded Engineer"],
        "gap": ["Pointers", "Memory Management", "STL"],
        "path": [
            "Understand C++ syntax and classes",
            "Work with pointers and memory",
            "Use STL for data structures",
            "Build console-based projects",
            "Debug and optimize C++ code"
        ]
    },
    "C#": {
        "roles": [".NET Developer", "Game Developer", "Desktop App Developer"],
        "gap": ["LINQ", "Delegates", "Async Programming"],
        "path": [
            "Learn C# syntax and control flow",
            "Use Visual Studio and .NET SDK",
            "Create forms and desktop apps",
            "Practice LINQ and async/await",
            "Build web apps with ASP.NET Core"
        ]
    },
    "Flutter": {
        "roles": ["Mobile App Developer", "UI Developer", "Full Stack Developer"],
        "gap": ["Widgets", "State Management", "Firebase Integration"],
        "path": [
            "Install Flutter and Dart SDK",
            "Learn widgets and UI design",
            "Manage state with Provider/Bloc",
            "Connect apps to Firebase",
            "Publish app to Play Store"
        ]
    },
    "Dart": {
        "roles": ["Flutter Developer", "Mobile Developer", "Frontend Developer"],
        "gap": ["Asynchronous Code", "Classes", "Collections"],
        "path": [
            "Understand Dart basics and syntax",
            "Work with lists, maps, sets",
            "Use async/await and Futures",
            "Build small Dart CLI tools",
            "Practice with Flutter integration"
        ]
    },
    "Go": {
        "roles": ["Backend Developer", "DevOps Engineer", "Cloud Engineer"],
        "gap": ["Goroutines", "Interfaces", "Error Handling"],
        "path": [
            "Install Go and set up workspace",
            "Learn syntax and basic types",
            "Write concurrent apps with goroutines",
            "Use interfaces and channels",
            "Build web APIs using net/http"
        ]
    },
    "Rust": {
        "roles": ["System Programmer", "Blockchain Developer", "Security Engineer"],
        "gap": ["Ownership", "Borrowing", "Cargo"],
        "path": [
            "Learn Rust syntax and concepts",
            "Understand ownership and lifetimes",
            "Build small CLI tools",
            "Work with crates and Cargo",
            "Practice memory-safe programming"
        ]
    },
    "Ruby": {
        "roles": ["Web Developer", "Ruby on Rails Developer", "Automation Engineer"],
        "gap": ["Blocks", "Gems", "Rails MVC"],
        "path": [
            "Learn Ruby basics and syntax",
            "Use blocks and metaprogramming",
            "Build apps with Rails framework",
            "Work with ActiveRecord",
            "Deploy using Heroku"
        ]
    },
    "R": {
        "roles": ["Data Scientist", "Statistician", "Research Analyst"],
        "gap": ["ggplot2", "dplyr", "Tidyverse"],
        "path": [
            "Install R and RStudio",
            "Work with data frames using dplyr",
            "Visualize data using ggplot2",
            "Use tidyverse packages",
            "Conduct statistical analysis"
        ]
    },
    "MATLAB": {
        "roles": ["Research Engineer", "Signal Processing Engineer", "Data Scientist"],
        "gap": ["Toolboxes", "Scripting", "Simulink"],
        "path": [
            "Learn basic syntax and plotting",
            "Use matrix operations and loops",
            "Work with toolboxes",
            "Model systems in Simulink",
            "Analyze signals and systems"
        ]
    },
    "Shell Scripting": {
        "roles": ["System Admin", "DevOps Engineer", "Security Engineer"],
        "gap": ["Bash", "Loops", "File Management"],
        "path": [
            "Write bash scripts for automation",
            "Use conditional statements",
            "Loop through files and processes",
            "Automate cron jobs",
            "Create system reports"
        ]
    },
    "Jenkins": {
        "roles": ["DevOps Engineer", "Build Engineer", "CI/CD Engineer"],
        "gap": ["Pipelines", "Plugins", "Integrations"],
        "path": [
            "Install and configure Jenkins",
            "Create freestyle and pipeline jobs",
            "Integrate with GitHub/GitLab",
            "Use Jenkinsfile for CI/CD",
            "Automate testing and deployments"
        ]
    },
    "Kubernetes": {
        "roles": ["Cloud Engineer", "DevOps Engineer", "ML Platform Engineer"],
        "gap": ["Pods", "Services", "Volumes"],
        "path": [
            "Understand container orchestration",
            "Deploy pods and manage services",
            "Use config maps and secrets",
            "Scale deployments",
            "Monitor clusters"
        ]
    },
    "Terraform": {
        "roles": ["Cloud Engineer", "Infrastructure Engineer", "DevOps Engineer"],
        "gap": ["HCL", "State Files", "Modules"],
        "path": [
            "Learn HCL syntax",
            "Define infrastructure as code",
            "Use variables and modules",
            "Work with providers like AWS",
            "Apply and manage state"
        ]
    },
    "Apache Spark": {
        "roles": ["Data Engineer", "Big Data Engineer", "ML Engineer"],
        "gap": ["RDD", "DataFrames", "SparkSQL"],
        "path": [
            "Install Spark locally",
            "Work with RDDs and DataFrames",
            "Write SparkSQL queries",
            "Process large datasets",
            "Build ETL pipelines"
        ]
    },
    "Airflow": {
        "roles": ["Data Engineer", "ETL Developer", "ML Engineer"],
        "gap": ["DAGs", "Task Scheduling", "XComs"],
        "path": [
            "Install Apache Airflow",
            "Create DAGs with Python",
            "Manage task dependencies",
            "Use XComs to share data",
            "Schedule data pipelines"
        ]
    },
    "FastAPI": {
        "roles": ["Backend Developer", "ML Engineer", "API Developer"],
        "gap": ["Path Operations", "Pydantic Models", "Deployment"],
        "path": [
            "Install and use FastAPI",
            "Build async REST APIs",
            "Validate inputs with Pydantic",
            "Add CORS and middleware",
            "Deploy with Uvicorn or Docker"
        ]
    },
    "Numpy": {
        "roles": ["Data Analyst", "ML Engineer", "Quant Developer"],
        "gap": ["Array Operations", "Broadcasting", "Indexing"],
        "path": [
            "Install and import numpy",
            "Create and manipulate arrays",
            "Use slicing and indexing",
            "Understand broadcasting",
            "Perform vectorized computations"
        ]
    },
    "Matplotlib": {
        "roles": ["Data Analyst", "Data Scientist", "ML Engineer"],
        "gap": ["Plot Types", "Customization", "Subplots"],
        "path": [
            "Create bar, line, scatter plots",
            "Customize axis, labels, and colors",
            "Work with multiple subplots",
            "Save and export charts",
            "Combine with Pandas for EDA"
        ]
    },
    "Seaborn": {
        "roles": ["Data Scientist", "Data Analyst", "Statistician"],
        "gap": ["Categorical Plots", "Heatmaps", "Pairplots"],
        "path": [
            "Use Seaborn for statistical plotting",
            "Draw distribution plots",
            "Visualize correlations with heatmaps",
            "Use pairplots for multi-variable insights",
            "Integrate with Pandas"
        ]
    },
    "Hadoop": {
        "roles": ["Big Data Engineer", "Data Engineer", "ETL Developer"],
        "gap": ["HDFS", "MapReduce", "YARN"],
        "path": [
            "Understand Hadoop ecosystem",
            "Work with HDFS commands",
            "Write MapReduce jobs",
            "Manage clusters with YARN",
            "Integrate with Hive and Spark"
        ]
    },
    "Hive": {
        "roles": ["Data Engineer", "Big Data Analyst", "ETL Developer"],
        "gap": ["HiveQL", "Partitioning", "Joins"],
        "path": [
            "Install Hive and set up metastore",
            "Write HiveQL queries",
            "Use partitions and buckets",
            "Perform joins and aggregations",
            "Optimize query performance"
        ]
    },
    "Scala": {
        "roles": ["Big Data Engineer", "Backend Developer", "Data Scientist"],
        "gap": ["Case Classes", "Pattern Matching", "Functional Programming"],
        "path": [
            "Learn Scala syntax",
            "Work with functions and collections",
            "Use pattern matching and case classes",
            "Build Spark jobs in Scala",
            "Deploy Scala apps"
        ]
    },
    "LangChain": {
        "roles": ["LLM Engineer", "AI Developer", "ML Researcher"],
        "gap": ["Chains", "Agents", "Memory"],
        "path": [
            "Install LangChain and OpenAI SDK",
            "Build simple chains for QA",
            "Use agents to control flow",
            "Manage memory with chat history",
            "Deploy LLM apps"
        ]
    },
    "MLflow": {
        "roles": ["ML Engineer", "MLOps Engineer", "Data Scientist"],
        "gap": ["Tracking", "Model Registry", "Deployment"],
        "path": [
            "Install MLflow and set up tracking",
            "Log experiments and parameters",
            "Register and manage models",
            "Deploy models from registry",
            "Integrate with CI/CD"
        ]
    },
    "MLOps": {
        "roles": ["MLOps Engineer", "ML Platform Engineer", "AI Ops Engineer"],
        "gap": ["CI/CD", "Monitoring", "Model Lifecycle"],
        "path": [
            "Understand MLOps pipeline",
            "Build CI/CD for ML workflows",
            "Automate training and deployment",
            "Monitor model drift",
            "Use MLflow, DVC, or Kubeflow"
        ]
    },
    "DevOps": {
        "roles": ["DevOps Engineer", "Platform Engineer", "Cloud Engineer"],
        "gap": ["CI/CD Tools", "Monitoring", "Containerization"],
        "path": [
            "Learn DevOps culture and principles",
            "Use GitHub Actions or Jenkins",
            "Work with Docker and Kubernetes",
            "Set up monitoring with Prometheus",
            "Automate deployments"
        ]
    },
    "ETL": {
        "roles": ["ETL Developer", "Data Engineer", "Analytics Engineer"],
        "gap": ["Data Ingestion", "Transformation", "Workflow Orchestration"],
        "path": [
            "Understand ETL architecture",
            "Extract data using APIs/SQL",
            "Transform using Pandas or Spark",
            "Load into databases or warehouses",
            "Orchestrate with Airflow"
        ]
    },
    "BigQuery": {
        "roles": ["Data Engineer", "BI Analyst", "Analytics Engineer"],
        "gap": ["SQL Syntax", "Partitioning", "Data Studio Integration"],
        "path": [
            "Access BigQuery console",
            "Run SQL queries on datasets",
            "Use partitions and clustering",
            "Connect with Data Studio",
            "Analyze performance and cost"
        ]
    },
    "PowerShell": {
        "roles": ["System Admin", "Windows Engineer", "DevOps Engineer"],
        "gap": ["Cmdlets", "Scripting", "Automation"],
        "path": [
            "Write scripts using cmdlets",
            "Automate tasks and reporting",
            "Manage files, processes, services",
            "Use variables and loops",
            "Schedule tasks with Task Scheduler"
        ]
    },
    "Kafka": {
        "roles": ["Data Engineer", "Streaming Engineer", "Backend Developer"],
        "gap": ["Producer/Consumer", "Brokers", "Stream Processing"],
        "path": [
            "Set up Kafka cluster",
            "Write producer and consumer apps",
            "Stream data between services",
            "Monitor Kafka topics",
            "Process data using Kafka Streams"
        ]
    },
    "Snowflake": {
        "roles": ["Data Engineer", "BI Developer", "Analytics Engineer"],
        "gap": ["Warehousing", "Data Sharing", "Virtual Warehouses"],
        "path": [
            "Create and manage Snowflake account",
            "Ingest structured data",
            "Run queries and build views",
            "Optimize using caching",
            "Integrate with ETL tools"
        ]
    },
    "Redshift": {
        "roles": ["Data Engineer", "Data Analyst", "Cloud Engineer"],
        "gap": ["Distribution Styles", "Sort Keys", "Spectrum"],
        "path": [
            "Provision Redshift clusters",
            "Design schemas and tables",
            "Optimize with sort/distribution keys",
            "Query with SQL",
            "Connect with BI tools"
        ]
    },
    "Cybersecurity": {
        "roles": ["Security Analyst", "Penetration Tester", "SOC Analyst"],
        "gap": ["Firewalls", "Incident Response", "SIEM Tools"],
        "path": [
            "Understand security fundamentals",
            "Work with antivirus and firewall systems",
            "Analyze logs with SIEM",
            "Respond to threat incidents",
            "Study ethical hacking methods"
        ]
    },
    "Selenium": {
        "roles": ["QA Engineer", "Automation Tester", "Software Tester"],
        "gap": ["XPath", "WebDriver API", "TestNG"],
        "path": [
            "Learn Selenium WebDriver",
            "Write test cases in Python/Java",
            "Use locators like XPath/CSS",
            "Create test suites with TestNG",
            "Integrate with CI tools"
        ]
    },
    "Informatica": {
        "roles": ["ETL Developer", "Data Engineer", "BI Developer"],
        "gap": ["PowerCenter", "Mapping", "Workflow Monitor"],
        "path": [
            "Install and configure Informatica",
            "Create mappings and transformations",
            "Run and monitor workflows",
            "Handle sessions and logs",
            "Integrate with data warehouses"
        ]
    },
    "Talend": {
        "roles": ["Data Engineer", "ETL Developer", "Integration Specialist"],
        "gap": ["Components", "Job Design", "Error Handling"],
        "path": [
            "Use Talend Studio",
            "Design ETL jobs",
            "Use tMap and other components",
            "Manage metadata and schema",
            "Deploy and schedule jobs"
        ]
    },
    "Unity": {
        "roles": ["Game Developer", "XR Developer", "AR/VR Developer"],
        "gap": ["Scenes", "C# Scripting", "Physics"],
        "path": [
            "Install Unity and learn interface",
            "Create scenes and objects",
            "Write C# scripts for logic",
            "Apply animations and physics",
            "Publish game builds"
        ]
    },
    "YOLO": {
        "roles": ["Computer Vision Engineer", "AI Developer", "ML Researcher"],
        "gap": ["Object Detection", "Bounding Boxes", "Model Deployment"],
        "path": [
            "Understand object detection theory",
            "Train YOLO on custom datasets",
            "Use OpenCV for image processing",
            "Evaluate with precision-recall",
            "Deploy model to app or web"
        ]
    },
    "OpenCV": {
        "roles": ["Computer Vision Engineer", "Robotics Engineer", "AI Developer"],
        "gap": ["Image Processing", "Contours", "Video Capture"],
        "path": [
            "Install OpenCV library",
            "Read, process, and write images",
            "Draw and detect contours",
            "Capture from video/webcam",
            "Combine with ML models"
        ]
    },
    "Transformers": {
        "roles": ["NLP Engineer", "LLM Developer", "AI Researcher"],
        "gap": ["Tokenization", "Attention Mechanism", "Fine-Tuning"],
        "path": [
            "Learn about transformer architecture",
            "Use HuggingFace library",
            "Preprocess text and tokenize",
            "Fine-tune pretrained models",
            "Deploy NLP apps"
        ]
    },
    "Blockchain": {
        "roles": ["Blockchain Developer", "Smart Contract Engineer", "Web3 Developer"],
        "gap": ["Consensus", "Wallets", "DApps"],
        "path": [
            "Understand blockchain basics",
            "Write smart contracts with Solidity",
            "Connect with wallets using Web3.js",
            "Deploy DApps to testnet",
            "Learn security best practices"
        ]
    }
}
# --- USER INTERFACE ---
selected_skill = st.selectbox("🔍 Select a Skill to Explore", list(skill_data.keys()))

if selected_skill:
    details = skill_data[selected_skill]
    st.markdown(f"### 💼 Top 3 Roles for **{selected_skill}**")
    for role in details["roles"]:
        with st.expander(f"🔎 Explore: {role}"):
            st.markdown("#### 🧩 Skill Gap Analysis")
            st.write("Gaps to Fill:", details["gap"])

            st.markdown("#### 📘 Suggested Learning Path")
            for i, step in enumerate(details["path"], 1):
                st.write(f"{i}. {step}")
# --- FEEDBACK ---
st.markdown("---")
st.markdown("## 🗣️ Share Your Feedback")

feedback_choice = st.radio(
    "How would you rate your overall experience?",
    ("🌟 Excellent", "👍 Good", "😐 Average", "👎 Needs Improvement", "✍️ I have a suggestion"),
    key="feedback_radio"
)

additional_feedback = st.text_area("Any specific suggestions or comments?", key="feedback_comments")

if st.button("📩 Submit Feedback"):
    st.success("✅ Thank you for helping us make Futureovia better!")
    st.write("📝 Your feedback:", feedback_choice)
    st.write("💬 Your comments:", additional_feedback)
