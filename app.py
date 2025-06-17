import streamlit as st
# 2. Setup Streamlit page
st.set_page_config(page_title="Futureovia", layout="centered")
st.title("🔮 Futureovia")
st.subheader("Career Path Architect for Tech Aspirants")

# 3. Welcome instructions
st.markdown("### 👋 Welcome to Futureovia!")
st.markdown("""
This tool empowers you to explore tech skills, discover aligned career roles, identify your skill gaps, and follow a personalized learning path.

#### 🚀 How to Use:
1. **Select** a tech skill you already know or want to learn  
2. **View** top 3 career roles where that skill matters  
3. **See** the skill gaps and personalized learning roadmap  
4. **Start** working on those steps to upskill and apply!

💡 *Great for students, freshers, and job seekers in tech.*
""")

skill_data = {
    "Python": {
        "roles": ["Data Analyst", "Backend Developer", "ML Engineer"],
        "role_details": {
            "Data Analyst": {
                "gap": ["SQL", "Pandas", "Data Cleaning"],
                "path": [
                    "Learn Python basics and data types",
                    "Master Pandas and data cleaning techniques",
                    "Work with NumPy and Matplotlib",
                    "Analyze real-world datasets",
                    "Build dashboards with Streamlit"
                ]
            },
            "Backend Developer": {
                "gap": ["Flask", "OOP", "APIs"],
                "path": [
                    "Master object-oriented programming in Python",
                    "Build REST APIs using Flask or FastAPI",
                    "Use SQLAlchemy for database integration",
                    "Create scalable backend services",
                    "Write unit tests for your code"
                ]
            },
            "ML Engineer": {
                "gap": ["NumPy", "Scikit-learn", "Model Deployment"],
                "path": [
                    "Learn machine learning fundamentals",
                    "Use NumPy and Pandas for data preparation",
                    "Train models with Scikit-learn",
                    "Deploy models with Flask or FastAPI",
                    "Monitor models using MLflow"
                ]
            }
        }
    },
    "JavaScript": {
        "roles": ["Frontend Developer", "Full Stack Developer", "Web App Engineer"],
        "role_details": {
            "Frontend Developer": {
                "gap": ["ES6+", "DOM", "Events"],
                "path": [
                    "Master modern JavaScript (ES6+)",
                    "Manipulate the DOM directly",
                    "Handle events and UI updates",
                    "Build responsive frontends",
                    "Use modern frameworks with vanilla JS"
                ]
            },
            "Full Stack Developer": {
                "gap": ["Async/Await", "APIs", "Node.js"],
                "path": [
                    "Learn asynchronous JavaScript patterns",
                    "Integrate frontend with backend APIs",
                    "Build server-side code with Node.js",
                    "Develop full-stack applications",
                    "Debug using browser dev tools and Node inspectors"
                ]
            },
            "Web App Engineer": {
                "gap": ["Modules", "Routing", "Testing"],
                "path": [
                    "Structure applications with JavaScript modules",
                    "Implement client-side routing",
                    "Write unit and integration tests",
                    "Optimize application performance",
                    "Deploy using modern build tools"
                ]
            }
        }
    },
    "SQL": {
        "roles": ["Data Analyst", "BI Developer", "Database Engineer"],
        "role_details": {
            "Data Analyst": {
                "gap": ["Joins", "Group By", "Window Functions"],
                "path": [
                    "Write complex SQL queries using joins",
                    "Use GROUP BY and aggregation functions",
                    "Employ window functions for advanced analysis",
                    "Analyze business data efficiently",
                    "Create views for reporting"
                ]
            },
            "BI Developer": {
                "gap": ["CTEs", "Aggregation", "Optimization"],
                "path": [
                    "Structure queries with common table expressions (CTEs)",
                    "Aggregate and summarize data",
                    "Optimize queries for faster performance",
                    "Integrate SQL results with BI tools",
                    "Build interactive dashboards"
                ]
            },
            "Database Engineer": {
                "gap": ["Indexing", "Stored Procedures", "Transactions"],
                "path": [
                    "Design efficient database schemas",
                    "Implement indexing strategies",
                    "Create stored procedures and triggers",
                    "Manage complex transactions",
                    "Tune queries for performance"
                ]
            }
        }
    },
    "Machine Learning": {
        "roles": ["ML Engineer", "AI Researcher", "ML Platform Engineer"],
        "role_details": {
            "ML Engineer": {
                "gap": ["Model Training", "Evaluation", "Deployment"],
                "path": [
                    "Study supervised and unsupervised learning",
                    "Evaluate model performance rigorously",
                    "Deploy models as scalable services",
                    "Automate training pipelines",
                    "Monitor model metrics continuously"
                ]
            },
            "AI Researcher": {
                "gap": ["Mathematics", "Algorithms", "Research Papers"],
                "path": [
                    "Deepen your understanding of linear algebra and statistics",
                    "Implement cutting-edge algorithms",
                    "Read and replicate research papers",
                    "Experiment with novel architectures",
                    "Publish findings in reputable venues"
                ]
            },
            "ML Platform Engineer": {
                "gap": ["MLOps", "Airflow", "Model Registry"],
                "path": [
                    "Set up ML pipelines using Airflow",
                    "Implement continuous integration for models",
                    "Maintain an ML model registry",
                    "Deploy models on Kubernetes",
                    "Monitor model drift and performance"
                ]
            }
        }
    },
    "AWS": {
        "roles": ["Cloud Engineer", "DevOps Engineer", "Solutions Architect"],
        "role_details": {
            "Cloud Engineer": {
                "gap": ["IAM", "EC2", "S3"],
                "path": [
                    "Configure IAM roles and policies",
                    "Launch and manage EC2 instances",
                    "Use S3 for scalable storage",
                    "Set up Virtual Private Clouds (VPCs)",
                    "Monitor services with CloudWatch"
                ]
            },
            "DevOps Engineer": {
                "gap": ["CI/CD", "CloudFormation", "Lambda"],
                "path": [
                    "Automate deployments using CodePipeline",
                    "Define infrastructure with CloudFormation",
                    "Deploy serverless applications using Lambda",
                    "Implement best practices for cloud security",
                    "Integrate with AWS tools for monitoring"
                ]
            },
            "Solutions Architect": {
                "gap": ["Architecture Design", "Security", "Cost Optimization"],
                "path": [
                    "Design scalable and secure architectures",
                    "Implement robust security measures",
                    "Optimize cost with proper resource planning",
                    "Use auto-scaling and load balancing",
                    "Advise on cloud migration strategies"
                ]
            }
        }
    },
    "React": {
        "roles": ["Frontend Developer", "Web App Developer", "UI Engineer"],
        "role_details": {
            "Frontend Developer": {
                "gap": ["JSX", "Hooks", "Routing"],
                "path": [
                    "Develop components using JSX",
                    "Manage state with React hooks",
                    "Implement client-side routing",
                    "Debug with React DevTools",
                    "Optimize rendering performance"
                ]
            },
            "Web App Developer": {
                "gap": ["APIs", "State Management", "Forms"],
                "path": [
                    "Integrate REST APIs in React",
                    "Manage state with Redux or Context API",
                    "Build and validate forms",
                    "Modularize components effectively",
                    "Deploy using modern build pipelines"
                ]
            },
            "UI Engineer": {
                "gap": ["Accessibility", "Styling", "Component Libraries"],
                "path": [
                    "Ensure accessibility compliance",
                    "Style with CSS-in-JS or CSS frameworks",
                    "Utilize component libraries like Material-UI",
                    "Create reusable UI components",
                    "Conduct user testing for feedback"
                ]
            }
        }
    },
    "Docker": {
        "roles": ["DevOps Engineer", "Cloud Engineer", "Backend Developer"],
        "role_details": {
            "DevOps Engineer": {
                "gap": ["Dockerfile", "Volumes", "Networking"],
                "path": [
                    "Write Dockerfiles to containerize applications",
                    "Manage persistent storage with volumes",
                    "Configure container networks",
                    "Optimize images for production",
                    "Deploy containers in CI/CD pipelines"
                ]
            },
            "Cloud Engineer": {
                "gap": ["Containers", "Orchestration", "Security"],
                "path": [
                    "Package applications into Docker containers",
                    "Deploy with orchestration tools like ECS or Kubernetes",
                    "Ensure container security best practices",
                    "Monitor container performance",
                    "Implement container scaling"
                ]
            },
            "Backend Developer": {
                "gap": ["Docker Compose", "Local Dev", "Microservices"],
                "path": [
                    "Use Docker Compose for local development",
                    "Break backend into microservices",
                    "Streamline service dependencies in containers",
                    "Test interactions within Docker setups",
                    "Deploy multi-container applications"
                ]
            }
        }
    },
    "Git": {
        "roles": ["Software Engineer", "DevOps Engineer", "Collaborative Developer"],
        "role_details": {
            "Software Engineer": {
                "gap": ["Branching", "Merging", "Conflict Resolution"],
                "path": [
                    "Use Git for version control",
                    "Manage features with branches",
                    "Merge changes and resolve conflicts",
                    "Write descriptive commit messages",
                    "Leverage Git workflows effectively"
                ]
            },
            "DevOps Engineer": {
                "gap": ["CI/CD Integration", "Hooks", "GitOps"],
                "path": [
                    "Integrate Git into CI/CD pipelines",
                    "Implement Git hooks for automation",
                    "Adopt GitOps practices for deployment",
                    "Audit commit history for security",
                    "Automate release processes"
                ]
            },
            "Collaborative Developer": {
                "gap": ["Pull Requests", "Rebasing", "Code Reviews"],
                "path": [
                    "Create and manage pull requests",
                    "Rebase feature branches for clean history",
                    "Participate actively in code reviews",
                    "Coordinate with team members",
                    "Improve code quality collaboratively"
                ]
            }
        }
    },
    "Linux": {
        "roles": ["System Administrator", "DevOps Engineer", "Cloud Engineer"],
        "role_details": {
            "System Administrator": {
                "gap": ["Shell Scripting", "Permissions", "Cron Jobs"],
                "path": [
                    "Automate tasks with shell scripts",
                    "Manage file permissions and users",
                    "Schedule repetitive tasks using cron",
                    "Monitor system health",
                    "Optimize system performance"
                ]
            },
            "DevOps Engineer": {
                "gap": ["Process Management", "Security", "Networking"],
                "path": [
                    "Monitor processes with Linux tools",
                    "Set up firewalls and secure access",
                    "Configure networking interfaces",
                    "Debug using logs and system metrics",
                    "Automate server configurations"
                ]
            },
            "Cloud Engineer": {
                "gap": ["Command Line", "Package Management", "Services"],
                "path": [
                    "Master the Linux command line",
                    "Install packages using apt or yum",
                    "Configure and manage system services",
                    "Use SSH for secure remote management",
                    "Automate deployments on Linux VMs"
                ]
            }
        }
    },
    "HTML": {
        "roles": ["Frontend Developer", "UI Designer", "Web Developer"],
        "role_details": {
            "Frontend Developer": {
                "gap": ["Semantic Tags", "Forms", "Multimedia"],
                "path": [
                    "Use semantic HTML elements for structure",
                    "Build accessible forms",
                    "Embed audio and video correctly",
                    "Validate markup for errors",
                    "Integrate with CSS and JavaScript"
                ]
            },
            "UI Designer": {
                "gap": ["Accessibility", "Layout", "Visual Hierarchy"],
                "path": [
                    "Design using proper HTML semantics",
                    "Ensure content is accessible",
                    "Structure pages for optimal UX",
                    "Align elements using divs and sections",
                    "Test across browsers for consistency"
                ]
            },
            "Web Developer": {
                "gap": ["Meta Tags", "SEO", "Responsive Design"],
                "path": [
                    "Include meta tags for SEO optimization",
                    "Create mobile-responsive layouts",
                    "Use HTML5 elements appropriately",
                    "Integrate dynamic content seamlessly",
                    "Test webpages on multiple devices"
                ]
            }
        }
    },
    "CSS": {
        "roles": ["Frontend Developer", "UI/UX Designer", "Web Designer"],
        "role_details": {
            "Frontend Developer": {
                "gap": ["Selectors", "Flexbox", "Animations"],
                "path": [
                    "Write clean and efficient CSS selectors",
                    "Build layouts using Flexbox and Grid",
                    "Create smooth transitions and animations",
                    "Maintain consistency using CSS variables",
                    "Debug using browser developer tools"
                ]
            },
            "UI/UX Designer": {
                "gap": ["Responsive Design", "Variables", "Design Systems"],
                "path": [
                    "Create responsive designs with media queries",
                    "Define and use CSS variables",
                    "Develop comprehensive design systems",
                    "Ensure layouts work across all devices",
                    "Collaborate with developers on prototypes"
                ]
            },
            "Web Designer": {
                "gap": ["Typography", "Color Theory", "Layout Composition"],
                "path": [
                    "Select fonts and design with accessibility in mind",
                    "Apply color theory to enhance user experience",
                    "Structure layouts with balance and spacing",
                    "Test design consistency across pages",
                    "Refine design based on user feedback"
                ]
            }
        }
    },
    "TypeScript": {
        "roles": ["Frontend Developer", "Full Stack Developer", "App Developer"],
        "role_details": {
            "Frontend Developer": {
                "gap": ["Types", "Interfaces", "Component Props"],
                "path": [
                    "Learn TypeScript fundamentals",
                    "Define and enforce type interfaces",
                    "Type React component props and state",
                    "Avoid using 'any' type in projects",
                    "Integrate TypeScript into existing projects"
                ]
            },
            "Full Stack Developer": {
                "gap": ["Type Safety", "Backend Typing", "API Contracts"],
                "path": [
                    "Use TypeScript on both frontend and backend",
                    "Enforce type safety across services",
                    "Define API contracts using TypeScript types",
                    "Refactor legacy JavaScript code",
                    "Debug type errors using tooling"
                ]
            },
            "App Developer": {
                "gap": ["Mobile Typing", "Async Types", "Navigation"],
                "path": [
                    "Integrate TypeScript in mobile app frameworks",
                    "Type asynchronous functions properly",
                    "Define navigation props and types",
                    "Ensure stability in large codebases",
                    "Utilize community libraries with type definitions"
                ]
            }
        }
    },
    "PostgreSQL": {
        "roles": ["Database Developer", "Data Engineer", "Backend Developer"],
        "role_details": {
            "Database Developer": {
                "gap": ["Joins", "Indexes", "Stored Procedures"],
                "path": [
                    "Design relational database schemas",
                    "Optimize queries with indexing",
                    "Write and maintain stored procedures",
                    "Use PostgreSQL for data-driven apps",
                    "Perform regular backups and tuning"
                ]
            },
            "Data Engineer": {
                "gap": ["ETL", "Partitioning", "Performance Tuning"],
                "path": [
                    "Set up ETL pipelines using PostgreSQL",
                    "Partition large tables effectively",
                    "Optimize query performance",
                    "Integrate with data warehousing solutions",
                    "Monitor performance and adjust configurations"
                ]
            },
            "Backend Developer": {
                "gap": ["ORM Integration", "Transactions", "Joins"],
                "path": [
                    "Connect PostgreSQL with backend frameworks",
                    "Manage transactions and data consistency",
                    "Write complex queries involving joins",
                    "Utilize ORMs like SQLAlchemy",
                    "Deploy secure database applications"
                ]
            }
        }
    },
    "MongoDB": {
        "roles": ["Backend Developer", "Full Stack Developer", "Data Engineer"],
        "role_details": {
            "Backend Developer": {
                "gap": ["CRUD Operations", "Schema Design", "Indexing"],
                "path": [
                    "Set up MongoDB connections in your app",
                    "Design flexible schema structures",
                    "Implement CRUD operations securely",
                    "Use indexes for query optimization",
                    "Backup and restore databases regularly"
                ]
            },
            "Full Stack Developer": {
                "gap": ["NoSQL Design", "Replication", "Sharding"],
                "path": [
                    "Design applications using NoSQL principles",
                    "Set up replication for high availability",
                    "Implement sharding for large datasets",
                    "Integrate with Express or Node.js",
                    "Secure the database with proper authentication"
                ]
            },
            "Data Engineer": {
                "gap": ["Aggregation", "Data Modeling", "Performance"],
                "path": [
                    "Use MongoDB aggregation for complex queries",
                    "Design collections for analytics",
                    "Monitor performance with built-in tools",
                    "Integrate with big data workflows",
                    "Optimize read and write operations"
                ]
            }
        }
    },
    "Firebase": {
        "roles": ["App Developer", "Frontend Developer", "Full Stack Developer"],
        "role_details": {
            "App Developer": {
                "gap": ["Authentication", "Realtime DB", "Cloud Messaging"],
                "path": [
                    "Integrate Firebase Authentication",
                    "Use Firestore and Realtime Database",
                    "Implement push notifications with Cloud Messaging",
                    "Test app performance with Firebase tools",
                    "Deploy apps with Firebase Hosting"
                ]
            },
            "Frontend Developer": {
                "gap": ["Hosting", "Firestore Queries", "Security Rules"],
                "path": [
                    "Deploy static websites with Firebase Hosting",
                    "Query Firestore for dynamic data",
                    "Write robust security rules",
                    "Integrate Firebase with JavaScript frameworks",
                    "Monitor app usage with Analytics"
                ]
            },
            "Full Stack Developer": {
                "gap": ["Cloud Functions", "Role-Based Access", "Realtime Sync"],
                "path": [
                    "Build serverless APIs with Cloud Functions",
                    "Implement role-based access control",
                    "Synchronize data in realtime",
                    "Integrate frontend and backend seamlessly",
                    "Scale using Firebase best practices"
                ]
            }
        }
    },
    "Tailwind CSS": {
        "roles": ["UI Developer", "Frontend Developer", "Web Designer"],
        "role_details": {
            "UI Developer": {
                "gap": ["Utility Classes", "Responsive Design", "Dark Mode"],
                "path": [
                    "Learn the utility-first approach",
                    "Build responsive components",
                    "Implement dark mode with Tailwind",
                    "Customize design tokens",
                    "Optimize CSS for production"
                ]
            },
            "Frontend Developer": {
                "gap": ["Framework Integration", "Styling Components", "Responsive Utilities"],
                "path": [
                    "Integrate Tailwind with React or Vue",
                    "Style components effectively",
                    "Use responsive utilities for mobile design",
                    "Create custom themes in tailwind.config.js",
                    "Deploy using JIT compilation"
                ]
            },
            "Web Designer": {
                "gap": ["Design Systems", "Typography", "Color Palettes"],
                "path": [
                    "Develop design systems with Tailwind",
                    "Customize typography scales",
                    "Define and apply color palettes",
                    "Collaborate with developers on UI consistency",
                    "Prototype landing pages quickly"
                ]
            }
        }
    },
    "Node.js": {
        "roles": ["Backend Developer", "Full Stack Developer", "API Developer"],
        "role_details": {
            "Backend Developer": {
                "gap": ["Event Loop", "Express", "Asynchronous Programming"],
                "path": [
                    "Learn Node.js fundamentals",
                    "Create servers using Express.js",
                    "Handle async operations with callbacks or promises",
                    "Integrate with databases like MongoDB",
                    "Deploy scalable backend services"
                ]
            },
            "Full Stack Developer": {
                "gap": ["Backend Integration", "API Development", "Security"],
                "path": [
                    "Integrate Node.js backend with frontend",
                    "Build secure REST APIs",
                    "Use middleware for error handling",
                    "Implement JWT authentication",
                    "Deploy full-stack applications"
                ]
            },
            "API Developer": {
                "gap": ["Routing", "Middleware", "Documentation"],
                "path": [
                    "Define RESTful routes in Express.js",
                    "Create robust middleware layers",
                    "Document APIs with Swagger",
                    "Test endpoints with Postman",
                    "Ensure scalability and security"
                ]
            }
        }
    },
    "Express.js": {
        "roles": ["Backend Developer", "API Developer", "Full Stack Developer"],
        "role_details": {
            "Backend Developer": {
                "gap": ["Routing", "Middleware", "Error Handling"],
                "path": [
                    "Set up an Express.js server",
                    "Modularize routes with Express Router",
                    "Write custom middleware for error handling",
                    "Implement logging for requests",
                    "Secure endpoints with proper validation"
                ]
            },
            "API Developer": {
                "gap": ["REST Design", "Async Functions", "Security"],
                "path": [
                    "Design RESTful API endpoints",
                    "Utilize async/await for performance",
                    "Implement security with JWT",
                    "Validate data with middleware",
                    "Test using automated API tests"
                ]
            },
            "Full Stack Developer": {
                "gap": ["Integration", "CORS", "Deployment"],
                "path": [
                    "Connect Express with frontend frameworks",
                    "Configure CORS for cross-origin requests",
                    "Serve static files efficiently",
                    "Deploy Express apps on cloud platforms",
                    "Monitor performance and security"
                ]
            }
        }
    },
    "Pandas": {
        "roles": ["Data Analyst", "Data Scientist", "ML Engineer"],
        "role_details": {
            "Data Analyst": {
                "gap": ["Data Cleaning", "Merging", "Pivot Tables"],
                "path": [
                    "Load data into DataFrames",
                    "Clean and preprocess data",
                    "Merge multiple datasets",
                    "Create pivot tables for summaries",
                    "Visualize data trends"
                ]
            },
            "Data Scientist": {
                "gap": ["Exploratory Data Analysis", "Feature Engineering", "Visualization"],
                "path": [
                    "Perform EDA using Pandas",
                    "Engineer features for models",
                    "Use plotting libraries for insights",
                    "Optimize DataFrame operations",
                    "Integrate with Scikit-learn pipelines"
                ]
            },
            "ML Engineer": {
                "gap": ["Data Preparation", "Scaling", "Memory Optimization"],
                "path": [
                    "Prepare data with Pandas",
                    "Handle large datasets efficiently",
                    "Scale numerical data for ML models",
                    "Integrate with NumPy for speed",
                    "Automate data workflows"
                ]
            }
        }
    },
    "Tableau": {
        "roles": ["Data Analyst", "BI Developer", "Product Analyst"],
        "role_details": {
            "Data Analyst": {
                "gap": ["Dashboard Creation", "Data Blending", "Visualization"],
                "path": [
                    "Connect Tableau to various data sources",
                    "Create interactive dashboards",
                    "Blend data from multiple sources",
                    "Use calculated fields effectively",
                    "Share visual insights with stakeholders"
                ]
            },
            "BI Developer": {
                "gap": ["Data Modeling", "ETL Integration", "Reporting"],
                "path": [
                    "Build data models suitable for BI",
                    "Integrate ETL pipelines with Tableau",
                    "Design custom reports",
                    "Optimize queries for visualization",
                    "Implement user-driven dashboards"
                ]
            },
            "Product Analyst": {
                "gap": ["KPIs", "Cohort Analysis", "Visualization"],
                "path": [
                    "Define key product metrics",
                    "Perform cohort analysis using Tableau",
                    "Visualize user engagement trends",
                    "Build actionable dashboards",
                    "Collaborate with product teams"
                ]
            }
        }
    },
    "Power BI": {
        "roles": ["BI Analyst", "Data Analyst", "Reporting Specialist"],
        "role_details": {
            "BI Analyst": {
                "gap": ["Data Modeling", "DAX", "Performance Optimization"],
                "path": [
                    "Connect multiple data sources to Power BI",
                    "Create and manage data models",
                    "Write DAX formulas for analytics",
                    "Build interactive reports",
                    "Optimize visuals for performance"
                ]
            },
            "Data Analyst": {
                "gap": ["Power Query", "Visualization", "Data Cleaning"],
                "path": [
                    "Clean data using Power Query",
                    "Design dashboards with interactive filters",
                    "Generate insights from large datasets",
                    "Deploy reports to Power BI Service",
                    "Collaborate on shared datasets"
                ]
            },
            "Reporting Specialist": {
                "gap": ["Scheduled Refresh", "Data Gateways", "Publishing"],
                "path": [
                    "Schedule data refresh tasks",
                    "Manage data gateways for live connectivity",
                    "Publish and share reports securely",
                    "Control user access",
                    "Monitor report performance"
                ]
            }
        }
    },
    "Java": {
        "roles": ["Backend Developer", "Android Developer", "Software Engineer"],
        "role_details": {
            "Backend Developer": {
                "gap": ["Spring Boot", "REST APIs", "OOP"],
                "path": [
                    "Master core Java and OOP concepts",
                    "Build REST APIs using Spring Boot",
                    "Integrate with databases using JPA",
                    "Deploy microservices on cloud",
                    "Write unit tests with JUnit"
                ]
            },
            "Android Developer": {
                "gap": ["Android SDK", "UI Development", "Lifecycle"],
                "path": [
                    "Develop apps with Android Studio",
                    "Design responsive UI layouts",
                    "Manage activity and fragment lifecycle",
                    "Integrate APIs for dynamic content",
                    "Test across multiple devices"
                ]
            },
            "Software Engineer": {
                "gap": ["Multithreading", "Collections", "Design Patterns"],
                "path": [
                    "Understand Java concurrency and collections",
                    "Apply design patterns for robust code",
                    "Optimize applications for performance",
                    "Develop scalable systems",
                    "Participate in code reviews"
                ]
            }
        }
    },
    "Kotlin": {
        "roles": ["Android Developer", "Mobile App Developer", "Full Stack Developer"],
        "role_details": {
            "Android Developer": {
                "gap": ["Jetpack", "Coroutines", "Lifecycle"],
                "path": [
                    "Learn Kotlin syntax and basics",
                    "Utilize Jetpack libraries for Android",
                    "Manage coroutines for async tasks",
                    "Build responsive mobile apps",
                    "Deploy apps on the Play Store"
                ]
            },
            "Mobile App Developer": {
                "gap": ["UI Design", "State Management", "API Integration"],
                "path": [
                    "Develop UIs with Kotlin and Jetpack Compose",
                    "Manage app state efficiently",
                    "Integrate REST APIs",
                    "Test on various devices",
                    "Publish high-quality apps"
                ]
            },
            "Full Stack Developer": {
                "gap": ["Server-side Kotlin", "Ktor", "Database Integration"],
                "path": [
                    "Use Ktor for backend development",
                    "Integrate Kotlin on both frontend and backend",
                    "Manage database operations securely",
                    "Build end-to-end applications",
                    "Optimize code with Kotlin features"
                ]
            }
        }
    },
    "C++": {
        "roles": ["System Programmer", "Game Developer", "Embedded Engineer"],
        "role_details": {
            "System Programmer": {
                "gap": ["Memory Management", "Pointers", "Concurrency"],
                "path": [
                    "Understand C++ fundamentals deeply",
                    "Implement safe memory management",
                    "Work with pointers and references",
                    "Debug system-level issues",
                    "Optimize performance-critical code"
                ]
            },
            "Game Developer": {
                "gap": ["STL", "Rendering", "Physics"],
                "path": [
                    "Utilize STL for efficient data handling",
                    "Develop rendering pipelines",
                    "Integrate physics engines",
                    "Design game loops and mechanics",
                    "Optimize for high-performance gaming"
                ]
            },
            "Embedded Engineer": {
                "gap": ["Low-Level Programming", "Interrupts", "Hardware Interfaces"],
                "path": [
                    "Write efficient low-level C++ code",
                    "Manage hardware interrupts",
                    "Interface with microcontrollers",
                    "Optimize for power and performance",
                    "Test on embedded systems"
                ]
            }
        }
    },
    "C#": {
        "roles": [".NET Developer", "Game Developer", "Desktop App Developer"],
        "role_details": {
            ".NET Developer": {
                "gap": ["ASP.NET", "LINQ", "Entity Framework"],
                "path": [
                    "Develop web applications with ASP.NET",
                    "Use LINQ for data manipulation",
                    "Integrate databases via Entity Framework",
                    "Build scalable services",
                    "Deploy to Windows servers"
                ]
            },
            "Game Developer": {
                "gap": ["Unity", "Scripting", "3D Math"],
                "path": [
                    "Use C# in Unity game development",
                    "Script interactive game elements",
                    "Work with 3D math and physics",
                    "Optimize game performance",
                    "Deploy games on multiple platforms"
                ]
            },
            "Desktop App Developer": {
                "gap": ["WPF", "Event Handling", "MVVM"],
                "path": [
                    "Design UIs using WPF",
                    "Implement MVVM architecture",
                    "Manage events and data binding",
                    "Build robust desktop applications",
                    "Deploy using ClickOnce or MSI"
                ]
            }
        }
    },
    "Flutter": {
        "roles": ["Mobile App Developer", "UI Developer", "Full Stack Developer"],
        "role_details": {
            "Mobile App Developer": {
                "gap": ["Widgets", "Navigation", "State Management"],
                "path": [
                    "Learn Flutter basics and widgets",
                    "Design responsive mobile UIs",
                    "Implement navigation and state management",
                    "Integrate with REST APIs",
                    "Test on multiple devices"
                ]
            },
            "UI Developer": {
                "gap": ["Custom Widgets", "Animations", "Design Systems"],
                "path": [
                    "Build custom Flutter widgets",
                    "Implement smooth animations",
                    "Collaborate on design systems",
                    "Ensure app responsiveness",
                    "Optimize widget trees"
                ]
            },
            "Full Stack Developer": {
                "gap": ["Backend Integration", "API Management", "Cross-Platform"],
                "path": [
                    "Integrate Flutter with backend services",
                    "Manage cross-platform state",
                    "Deploy integrated mobile apps",
                    "Ensure API security",
                    "Use Firebase for real-time updates"
                ]
            }
        }
    },
    "Dart": {
        "roles": ["Flutter Developer", "Mobile Developer", "Frontend Developer"],
        "role_details": {
            "Flutter Developer": {
                "gap": ["State Management", "Asynchronicity", "Testing"],
                "path": [
                    "Master Dart basics and OOP",
                    "Use async/await for operations",
                    "Implement state management in Flutter",
                    "Write tests in Dart",
                    "Integrate with Flutter projects"
                ]
            },
            "Mobile Developer": {
                "gap": ["CLI Tools", "Package Management", "Debugging"],
                "path": [
                    "Develop command-line tools in Dart",
                    "Use the pub package manager",
                    "Handle exceptions and logs",
                    "Build modular mobile logic",
                    "Optimize for performance"
                ]
            },
            "Frontend Developer": {
                "gap": ["Web Support", "Interactivity", "Responsive Design"],
                "path": [
                    "Use Dart for web apps with Flutter Web",
                    "Manage interactivity in Dart",
                    "Build responsive designs",
                    "Integrate with backend services",
                    "Optimize for browser performance"
                ]
            }
        }
    },
    "Go": {
        "roles": ["Backend Developer", "DevOps Engineer", "Cloud Engineer"],
        "role_details": {
            "Backend Developer": {
                "gap": ["Goroutines", "Interfaces", "Concurrency"],
                "path": [
                    "Learn the fundamentals of Go",
                    "Use goroutines for concurrency",
                    "Design clean interfaces",
                    "Build REST APIs with net/http",
                    "Deploy as lightweight services"
                ]
            },
            "DevOps Engineer": {
                "gap": ["CLI Tools", "Dockerization", "Scripting"],
                "path": [
                    "Develop CLI tools with Go",
                    "Containerize Go applications",
                    "Automate tasks with Go scripts",
                    "Integrate with CI/CD pipelines",
                    "Monitor performance and uptime"
                ]
            },
            "Cloud Engineer": {
                "gap": ["Cloud SDKs", "Microservices", "Scalability"],
                "path": [
                    "Use Go SDKs for cloud services",
                    "Design microservices in Go",
                    "Implement robust concurrency models",
                    "Deploy on Kubernetes",
                    "Optimize resource utilization"
                ]
            }
        }
    },
    "Rust": {
        "roles": ["System Programmer", "Blockchain Developer", "Security Engineer"],
        "role_details": {
            "System Programmer": {
                "gap": ["Ownership Model", "Memory Safety", "Concurrency"],
                "path": [
                    "Learn Rust syntax and ownership",
                    "Write memory-safe code",
                    "Utilize Rust’s concurrency primitives",
                    "Develop system tools",
                    "Benchmark and optimize performance"
                ]
            },
            "Blockchain Developer": {
                "gap": ["Smart Contracts", "No-Std", "WASM"],
                "path": [
                    "Develop smart contracts using Rust",
                    "Work in no_std environments",
                    "Compile to WebAssembly (WASM)",
                    "Integrate with blockchain frameworks",
                    "Test and secure contract code"
                ]
            },
            "Security Engineer": {
                "gap": ["Static Analysis", "Safe Concurrency", "FFI"],
                "path": [
                    "Use Rust for secure coding practices",
                    "Implement safe concurrency patterns",
                    "Interface securely with C via FFI",
                    "Perform static code analysis",
                    "Harden cryptographic implementations"
                ]
            }
        }
    },
    "Ruby": {
        "roles": ["Web Developer", "Rails Developer", "Automation Engineer"],
        "role_details": {
            "Web Developer": {
                "gap": ["MVC", "Routing", "ERB Templates"],
                "path": [
                    "Build web apps with Ruby on Rails",
                    "Design MVC architecture cleanly",
                    "Manage routes and controllers",
                    "Use ERB for templating",
                    "Deploy to cloud platforms"
                ]
            },
            "Rails Developer": {
                "gap": ["Gems", "ActiveRecord", "Testing"],
                "path": [
                    "Leverage Ruby gems for functionality",
                    "Use ActiveRecord for database access",
                    "Write tests with RSpec",
                    "Optimize Rails performance",
                    "Follow best practices for MVC"
                ]
            },
            "Automation Engineer": {
                "gap": ["Scripting", "Web Scraping", "Data Processing"],
                "path": [
                    "Write automation scripts in Ruby",
                    "Scrape data with Nokogiri",
                    "Process CSV, JSON, and XML",
                    "Schedule tasks with cron",
                    "Monitor script performance"
                ]
            }
        }
    },
    "R": {
        "roles": ["Data Scientist", "Statistician", "Research Analyst"],
        "role_details": {
            "Data Scientist": {
                "gap": ["Data Wrangling", "Visualization", "Modeling"],
                "path": [
                    "Import and clean data in R",
                    "Visualize data with ggplot2",
                    "Build statistical models",
                    "Use RMarkdown for reports",
                    "Automate analysis pipelines"
                ]
            },
            "Statistician": {
                "gap": ["Hypothesis Testing", "Regression", "Probability"],
                "path": [
                    "Use statistical tests effectively",
                    "Model data using regression",
                    "Interpret p-values correctly",
                    "Generate reproducible reports",
                    "Share insights with stakeholders"
                ]
            },
            "Research Analyst": {
                "gap": ["Data Analysis", "Reporting", "Visualization"],
                "path": [
                    "Analyze datasets with tidyverse",
                    "Visualize research findings",
                    "Prepare academic reports",
                    "Collaborate on research projects",
                    "Document methodologies clearly"
                ]
            }
        }
    },
    "MATLAB": {
        "roles": ["Research Engineer", "Signal Processing Engineer", "Data Scientist"],
        "role_details": {
            "Research Engineer": {
                "gap": ["Scripting", "Toolboxes", "Visualization"],
                "path": [
                    "Write scripts for data analysis",
                    "Utilize MATLAB toolboxes",
                    "Plot data for research",
                    "Automate simulation runs",
                    "Generate publication-quality figures"
                ]
            },
            "Signal Processing Engineer": {
                "gap": ["Filter Design", "FFT", "Simulink"],
                "path": [
                    "Design filters using MATLAB",
                    "Use FFT for signal analysis",
                    "Model systems in Simulink",
                    "Validate signal processing algorithms",
                    "Document engineering results"
                ]
            },
            "Data Scientist": {
                "gap": ["Machine Learning", "Data Import", "EDA"],
                "path": [
                    "Import and preprocess data",
                    "Conduct exploratory data analysis",
                    "Apply ML algorithms with toolboxes",
                    "Visualize model performance",
                    "Automate report generation"
                ]
            }
        }
    },
    "Shell Scripting": {
        "roles": ["System Admin", "DevOps Engineer", "Security Engineer"],
        "role_details": {
            "System Admin": {
                "gap": ["Bash Basics", "Script Automation", "Cron Jobs"],
                "path": [
                    "Write bash scripts for routine tasks",
                    "Automate system maintenance",
                    "Schedule tasks with cron",
                    "Monitor system logs",
                    "Ensure script reliability"
                ]
            },
            "DevOps Engineer": {
                "gap": ["Pipeline Scripting", "Logging", "Environment Variables"],
                "path": [
                    "Integrate shell scripts in CI/CD",
                    "Write detailed logs for debugging",
                    "Manage environment variables securely",
                    "Automate deployment scripts",
                    "Optimize script performance"
                ]
            },
            "Security Engineer": {
                "gap": ["Log Analysis", "Process Monitoring", "Audit Scripts"],
                "path": [
                    "Develop scripts to analyze logs",
                    "Monitor processes in real time",
                    "Automate security audits",
                    "Harden scripts against attacks",
                    "Document security procedures"
                ]
            }
        }
    },
    "Jenkins": {
        "roles": ["DevOps Engineer", "Build Engineer", "CI/CD Engineer"],
        "role_details": {
            "DevOps Engineer": {
                "gap": ["Pipeline Automation", "Plugin Management", "Integration"],
                "path": [
                    "Set up Jenkins pipelines",
                    "Manage plugins for enhanced functionality",
                    "Integrate Jenkins with version control",
                    "Automate testing and deployment",
                    "Monitor build performance"
                ]
            },
            "Build Engineer": {
                "gap": ["Freestyle Jobs", "Artifact Archiving", "Build Reports"],
                "path": [
                    "Configure freestyle projects",
                    "Archive build artifacts",
                    "Generate comprehensive build reports",
                    "Automate job triggers",
                    "Maintain build servers"
                ]
            },
            "CI/CD Engineer": {
                "gap": ["Jenkinsfile", "Declarative Syntax", "Parallel Builds"],
                "path": [
                    "Write and maintain Jenkinsfiles",
                    "Adopt declarative pipeline syntax",
                    "Configure parallel stages for efficiency",
                    "Secure credentials in pipelines",
                    "Integrate automated tests"
                ]
            }
        }
    },
    "Kubernetes": {
        "roles": ["Cloud Engineer", "DevOps Engineer", "ML Platform Engineer"],
        "role_details": {
            "Cloud Engineer": {
                "gap": ["Cluster Setup", "Pods", "Load Balancing"],
                "path": [
                    "Set up Kubernetes clusters with Minikube or managed services",
                    "Deploy applications as pods",
                    "Configure services and load balancers",
                    "Manage persistent storage with PV/PVC",
                    "Monitor clusters with Prometheus"
                ]
            },
            "DevOps Engineer": {
                "gap": ["CI/CD Integration", "Secrets Management", "Rolling Updates"],
                "path": [
                    "Integrate Kubernetes with CI/CD pipelines",
                    "Manage secrets securely",
                    "Implement rolling deployments",
                    "Automate scaling with HPA",
                    "Troubleshoot using kubectl"
                ]
            },
            "ML Platform Engineer": {
                "gap": ["Model Serving", "GPU Scheduling", "Pipeline Orchestration"],
                "path": [
                    "Deploy ML models using KServe",
                    "Configure GPU-enabled pods",
                    "Orchestrate ML pipelines with Kubeflow",
                    "Monitor model performance",
                    "Automate retraining workflows"
                ]
            }
        }
    },
    "Terraform": {
        "roles": ["Cloud Engineer", "Infrastructure Engineer", "DevOps Engineer"],
        "role_details": {
            "Cloud Engineer": {
                "gap": ["Providers", "Resource Blocks", "Remote Backends"],
                "path": [
                    "Define infrastructure using Terraform",
                    "Configure cloud providers",
                    "Use remote backends for state management",
                    "Plan and apply configurations",
                    "Integrate Terraform with CI/CD"
                ]
            },
            "Infrastructure Engineer": {
                "gap": ["Module Creation", "Dependency Graph", "Workspaces"],
                "path": [
                    "Create reusable Terraform modules",
                    "Manage dependencies across modules",
                    "Utilize workspaces for environment isolation",
                    "Test infrastructure changes safely",
                    "Document IaC standards"
                ]
            },
            "DevOps Engineer": {
                "gap": ["CI/CD Integration", "Secrets Handling", "Drift Detection"],
                "path": [
                    "Integrate Terraform into pipelines",
                    "Securely manage secrets using Vault",
                    "Detect and remediate drift",
                    "Collaborate on infrastructure code",
                    "Automate deployments continuously"
                ]
            }
        }
    },
    "Apache Spark": {
        "roles": ["Data Engineer", "Big Data Engineer", "ML Engineer"],
        "role_details": {
            "Data Engineer": {
                "gap": ["RDD", "DataFrames", "SparkSQL"],
                "path": [
                    "Install and configure Apache Spark",
                    "Work with RDDs and DataFrames",
                    "Write SparkSQL queries",
                    "Build ETL pipelines with Spark",
                    "Optimize Spark jobs for performance"
                ]
            },
            "Big Data Engineer": {
                "gap": ["Cluster Management", "Data Partitioning", "Streaming"],
                "path": [
                    "Manage Spark clusters on cloud platforms",
                    "Partition and distribute data efficiently",
                    "Implement Spark Streaming for real-time data",
                    "Integrate with Hadoop ecosystems",
                    "Monitor job metrics and logs"
                ]
            },
            "ML Engineer": {
                "gap": ["MLlib", "Feature Engineering", "Model Deployment"],
                "path": [
                    "Use Spark MLlib for scalable machine learning",
                    "Engineer features on large datasets",
                    "Deploy ML models with Spark pipelines",
                    "Evaluate models using cross-validation",
                    "Automate workflows with Spark Streaming"
                ]
            }
        }
    },
    "Airflow": {
        "roles": ["Data Engineer", "ETL Developer", "ML Engineer"],
        "role_details": {
            "Data Engineer": {
                "gap": ["DAG Creation", "Task Scheduling", "Error Handling"],
                "path": [
                    "Design DAGs for workflow automation",
                    "Schedule tasks reliably",
                    "Implement retries and alerts",
                    "Integrate with external data sources",
                    "Monitor task execution"
                ]
            },
            "ETL Developer": {
                "gap": ["Data Pipelines", "Operator Customization", "Logging"],
                "path": [
                    "Develop ETL pipelines in Airflow",
                    "Customize operators to fit needs",
                    "Implement robust logging",
                    "Schedule complex data movements",
                    "Debug failed tasks effectively"
                ]
            },
            "ML Engineer": {
                "gap": ["Dynamic DAGs", "XComs", "Pipeline Orchestration"],
                "path": [
                    "Orchestrate ML workflows using Airflow",
                    "Pass data between tasks with XComs",
                    "Dynamically generate DAGs",
                    "Integrate model retraining steps",
                    "Monitor model performance pipelines"
                ]
            }
        }
    },
    "FastAPI": {
        "roles": ["Backend Developer", "ML Engineer", "API Developer"],
        "role_details": {
            "Backend Developer": {
                "gap": ["Routing", "Asynchronicity", "Deployment"],
                "path": [
                    "Build APIs with FastAPI",
                    "Leverage async features for performance",
                    "Integrate with databases seamlessly",
                    "Secure endpoints with OAuth2",
                    "Deploy using Uvicorn and Docker"
                ]
            },
            "ML Engineer": {
                "gap": ["Model Serving", "Input Validation", "CORS"],
                "path": [
                    "Serve ML models via FastAPI",
                    "Validate input using Pydantic",
                    "Enable CORS for frontend integration",
                    "Monitor API health continuously",
                    "Implement caching for performance"
                ]
            },
            "API Developer": {
                "gap": ["Request Parsing", "Documentation", "Testing"],
                "path": [
                    "Parse and validate requests effectively",
                    "Generate interactive API docs",
                    "Test endpoints with Swagger",
                    "Secure APIs with JWT tokens",
                    "Automate integration tests"
                ]
            }
        }
    }
}
selected_skill = st.selectbox("🔍 Select a Tech Skill to Explore", list(skill_data.keys()))

if selected_skill:
    st.markdown(f"## 📌 Selected Skill: **{selected_skill}**")

    roles = skill_data[selected_skill]["roles"]
    role_details = skill_data[selected_skill]["role_details"]

    st.markdown("### 👨‍💻 Top 3 Roles for this Skill:")
    for role in roles:
        with st.expander(f"💼 {role}"):
            st.markdown("#### 🔧 Skill Gaps:")
            for gap in role_details[role]["gap"]:
                st.write(f"• {gap}")

            st.markdown("#### 🛣️ Learning Path:")
            for step_num, step in enumerate(role_details[role]["path"], start=1):
                st.write(f"{step_num}. {step}")
                # --------------------------------------
# 4. Optional: Collect Feedback from Users
# --------------------------------------

st.markdown("---")
st.markdown("### 💬 We'd love your feedback!")

with st.form("feedback_form"):
    feedback_text = st.text_area("📣 Share your thoughts, suggestions, or issues here:")
    rating = st.slider("⭐ Rate this app (1 = Needs Improvement, 5 = Excellent)", 1, 5, 4)
    submit_button = st.form_submit_button("Submit Feedback")

if submit_button:
    if feedback_text.strip() == "":
        st.warning("Please enter some feedback before submitting.")
    else:
        st.success("✅ Thank you! Your feedback has been received.")
        # Optional: Save feedback to a local file or database
        with open("user_feedback.txt", "a") as f:
            f.write(f"\n---\nSkill: {selected_skill}\nRating: {rating}/5\nFeedback: {feedback_text}\n")

