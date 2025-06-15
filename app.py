import streamlit as st

# ------------------- Setup -------------------
st.set_page_config(page_title="Futureovia", layout="centered")
st.title("🚀 Futureovia: Career Path Architect")

# ------------------- Skills to Roles Mapping -------------------
skill_to_roles = {
    "AI/ML Model Deployment": ["MLOps Engineer", "AI Engineer", "ML Platform Engineer"],
    "AWS": ["Cloud Engineer", "Solutions Architect", "DevOps Engineer"],
    "Azure": ["Cloud Engineer", "Azure Specialist", "Infrastructure Engineer", "Cloud Engineer", "Azure DevOps Engineer", "Solutions Architect"],
    "BigQuery": ["Data Engineer", "Analytics Engineer", "BI Developer"],
    "Blockchain": ["Blockchain Developer", "Smart Contract Engineer", "Web3 Developer", "Blockchain Developer", "Smart Contract Engineer", "Web3 Developer"],
    "Bootstrap": ["Frontend Developer", "UI Engineer", "Web Designer", "UI Developer", "Web Designer", "Frontend Developer"],
    "CI/CD": ["DevOps Engineer", "Release Engineer", "Automation Engineer", "DevOps Engineer", "Automation Engineer", "Release Manager"],
    "CSS": ["Frontend Developer", "UI/UX Engineer", "Web Developer", "Web Designer", "UI Developer", "Frontend Developer"],
    "Dart": ["Flutter Developer", "Mobile App Engineer", "Cross-Platform Developer", "Mobile App Developer", "Flutter Developer", "Cross-Platform Developer"],
    "Data Visualization": ["Data Analyst", "BI Developer", "Data Storyteller"],
    "Deep Learning": ["Deep Learning Engineer", "AI Researcher", "Computer Vision Engineer"],
    "Docker": ["DevOps Engineer", "Cloud Engineer", "Site Reliability Engineer"],
    "ETL Tools": ["Data Engineer", "ETL Developer", "BI Analyst", "Data Engineer", "BI Developer", "ETL Developer"],
    "Excel": ["Data Analyst", "Operations Analyst", "Reporting Specialist"],
    "Express.js": ["Backend Developer", "Full Stack Developer", "Node.js Engineer", "Backend Developer", "JavaScript Engineer", "API Developer"],
    "Firebase": ["Mobile App Developer", "Backend Developer", "Realtime Database Engineer", "Mobile App Developer", "Backend Developer", "Realtime Database Engineer"],
    "Figma": ["UI/UX Designer", "Product Designer", "Interaction Designer", "UI/UX Designer", "Product Designer"],
    "Git": ["Version Control Engineer", "DevOps Engineer", "Software Developer", "Version Control Engineer", "DevOps Engineer", "Software Engineer"],
    "GitHub": ["Collaboration Engineer", "Open Source Contributor", "Software Engineer", "Software Engineer", "DevOps Engineer", "Open Source Contributor"],
    "Go": ["Systems Engineer", "Backend Developer", "Cloud-Native Developer"],
    "Google Cloud Platform (GCP)": ["Cloud Engineer", "GCP Solutions Architect", "DevOps Specialist"],
    "HTML": ["Frontend Developer", "Email Developer", "Web Designer"],
    "Jenkins": ["DevOps Engineer", "Automation Engineer", "CI/CD Specialist"],
    "Kubernetes": ["Cloud Infrastructure Engineer", "DevOps Engineer", "Platform Engineer", "DevOps Engineer", "Site Reliability Engineer", "Cloud Infrastructure Engineer"],
    "Keras": ["Deep Learning Engineer", "AI Engineer", "Model Prototyper"],
    "Kotlin": ["Android Developer", "Mobile App Engineer", "Jetpack Compose Developer", "Android Developer", "Mobile App Developer", "Backend Engineer"],
    "MySQL": ["Database Administrator", "Data Engineer", "Backend Developer", "Data Analyst", "Database Administrator", "Software Engineer"],
    "NLP": ["NLP Engineer", "AI Researcher", "Language Model Developer", "NLP Engineer", "AI Research Scientist", "Data Scientist", "NLP Engineer", "AI Researcher", "Chatbot Developer"],
    "Node.js": ["Backend Developer", "Full Stack Developer", "API Developer", "Backend Developer", "Full Stack Developer", "API Developer", "Interaction Designer"],
    "NumPy": ["Data Scientist", "ML Engineer", "Scientific Programmer", "Data Scientist", "Machine Learning Engineer", "Research Analyst"],
    "OpenCV": ["Computer Vision Engineer", "Robotics Engineer", "ML Developer", "Computer Vision Engineer", "AI Engineer", "Robotics Engineer"],
    "Pandas": ["Data Analyst", "Data Scientist", "ETL Developer", "Data Analyst", "Data Engineer", "Machine Learning Engineer"],
    "Penetration Testing": ["Security Analyst", "Red Team Specialist", "Vulnerability Assessor", "Security Analyst", "Ethical Hacker", "Vulnerability Assessor"],
    "PostgreSQL": ["Database Administrator", "Data Engineer", "Backend Developer", "Database Developer", "Backend Developer", "Data Engineer"],
    "Power BI": ["Business Intelligence Analyst", "Data Analyst", "Reporting Specialist", "BI Analyst", "Data Analyst", "Reporting Specialist"],
    "Python": ["Data Analyst", "Backend Developer", "Machine Learning Engineer", "Data Analyst", "Backend Developer", "Machine Learning Engineer"],
    "React": ["Frontend Developer", "UI Engineer", "Full Stack Developer", "Frontend Developer", "UI Developer", "Full Stack Developer"],
    "React Native": ["Mobile App Developer", "Frontend Engineer", "Cross-Platform Developer", "Mobile App Developer", "React Native Developer", "Cross-Platform App Developer"],
    "Redis": ["Caching Specialist", "Backend Developer", "Infrastructure Engineer", "Backend Developer", "Data Engineer", "System Architect"],
    "REST APIs": ["API Developer", "Integration Engineer", "Backend Developer", "Backend Developer", "Integration Engineer", "API Developer", "Backend Developer", "API Developer", "Integration Engineer"],
    "R": ["Statistician", "Data Analyst", "Research Scientist", "Statistician", "Data Scientist", "Research Analyst"],
    "Ruby": ["Backend Developer", "Ruby on Rails Developer", "Web Application Engineer", "Web Developer", "Backend Engineer", "DevOps Engineer"],
    "Scikit-learn": ["Machine Learning Engineer", "Data Scientist", "AI Engineer", "Machine Learning Engineer", "Data Scientist", "AI Engineer"],
    "Scrum": ["Scrum Master", "Agile Project Manager", "Product Owner", "Scrum Master", "Agile Coach", "Technical Project Manager"],
    "Seaborn": ["Data Analyst", "Data Visualization Specialist", "Research Analyst", "Data Analyst", "Data Visualization Specialist", "BI Analyst"],
    "Shell Scripting": ["DevOps Engineer", "Systems Administrator", "Automation Engineer", "Linux System Administrator", "DevOps Engineer", "Automation Engineer"],
    "SQL": ["Data Analyst", "Database Developer", "BI Analyst", "Data Analyst", "Database Developer", "BI Analyst"],
    "SQLite": ["Mobile Developer", "Embedded Systems Engineer", "Application Developer", "Mobile App Developer", "Embedded Systems Engineer", "Data Engineer"],
    "Swift": ["iOS Developer", "Mobile App Developer", "Software Engineer", "iOS Developer", "Mobile App Engineer", "Application Developer"],
    "Tailwind CSS": ["Frontend Developer", "UI Developer", "Web Designer", "UI Developer", "Frontend Developer", "Web Designer", "Frontend Developer", "UI Developer", "Web Designer"],
    "Tableau": ["Data Visualization Analyst", "Business Analyst", "BI Developer", "Data Analyst", "BI Developer", "Data Visualization Specialist"],
    "TensorFlow": ["Deep Learning Engineer", "AI Engineer", "Computer Vision Engineer", "Deep Learning Engineer", "AI Engineer", "ML Researcher"],
    "TypeScript": ["Frontend Developer", "Full Stack Developer", "Application Engineer", "Frontend Developer", "Full Stack Engineer", "Web Application Developer"],
    "Vue.js": ["Frontend Developer", "Web Application Developer", "JavaScript Developer", "Frontend Developer", "UI Developer", "JavaScript Developer"],
    "Web3": ["Web3 Developer", "Blockchain Engineer", "Smart Contract Developer", "Web3 Developer", "Blockchain Engineer", "DApp Developer"],
    "Wireshark": ["Network Analyst", "Security Analyst", "Network Forensics Expert", "Network Analyst", "Cybersecurity Engineer", "SOC Analyst"],
    "Agile": ["Agile Coach", "Product Manager", "Scrum Master"],
    "Android SDK": ["Android Developer", "Mobile Application Engineer", "Kotlin Developer"],
    "Ethical Hacking": ["Ethical Hacker", "Security Analyst", "Penetration Tester"],
    "Linux": ["System Administrator", "DevOps Engineer", "Backend Developer"],
    "Matplotlib": ["Data Analyst", "Data Visualization Specialist", "Research Analyst"],
    "Metasploit": ["Penetration Tester", "Ethical Hacker", "Security Researcher"],
    "MongoDB": ["Backend Developer", "Full Stack Developer", "Database Engineer"],
    "Network Security": ["Cybersecurity Analyst", "Security Engineer", "Network Administrator"],
    "Google Data Studio": ["Reporting Analyst", "Marketing Data Analyst", "BI Specialist"],
    "Transformers": ["NLP Engineer", "AI Engineer", "LLM Specialist", "Model Monitoring & Drift Detection", "Scalable ML Infrastructure Setup", "CI/CD Pipelines for ML Workflows", "Production-Ready AI Pipelines", "Integration with Business Systems", "Optimization for Inference Efficiency", "End-to-End ML Workflow Orchestration", "Cross-Team Platform Usability", "Cost-Aware Resource Management", "Proficiency in Infrastructure as Code (IaC) using AWS CDK or Pulumi", "Deep understanding of AWS Networking (Transit Gateway, VPC Peering)", "Cost Optimization using AWS Cost Explorer & Trusted Advisor", "Designing Event-Driven Architectures with Step Functions & SNS/SQS", "Migration Strategy Planning (CloudEndure, AWS Migration Hub)", "Mastery in AWS Well-Architected Framework pillars", "Advanced CI/CD on AWS using CodePipeline + GitOps", "Monitoring with CloudWatch Metrics Insights & X-Ray Tracing", "Secure DevOps with IAM Roles, KMS, and Secrets Manager", "Mastery of Azure CLI and Bicep for Infrastructure as Code (IaC)", "Azure Resource Optimization and Cost Management", "Multi-region deployment and global VNet peering", "Expertise in Azure Kubernetes Service (AKS) configuration and scaling", "Security Center & Defender for Cloud best practices", "Advanced ARM templates and Azure Policy enforcement", "Hybrid cloud networking using Azure Arc and ExpressRoute", "Automation using Azure PowerShell and Logic Apps", "Deep understanding of Load Balancing, Traffic Manager & Front Door", "Optimization of BigQuery SQL for large-scale joins and partitions", "Data pipeline orchestration using Cloud Composer", "Cost control techniques for high-frequency query environments", "dbt modeling best practices with BigQuery integration", "Complex analytical functions and windowing in BigQuery", "CI/CD for data pipelines using GitHub Actions or Cloud Build", "Efficient dashboard querying from BigQuery to BI tools (e.g., Looker)", "Data governance implementation in GCP environment", "Real-time reporting using Pub/Sub + BigQuery streaming", "Gas optimization techniques in Solidity and EVM", "Secure smart contract upgrade patterns (e.g., proxy pattern)", "Chainlink and oracle integration for off-chain data", "Formal verification and static analysis of smart contracts", "Understanding of cross-chain interoperability tools (e.g., LayerZero)", "Advanced Solidity patterns for modular contract architecture", "Wallet integration using Web3Modal or Wagmi", "Understanding of decentralized storage (e.g., IPFS, Filecoin)", "Real-time on-chain data visualization and indexing (e.g., The Graph)", "Customizing Bootstrap themes beyond default variables", "Integrating Bootstrap with modern JS frameworks (React, Vue)", "Accessibility (WCAG) compliance using Bootstrap components", "Building design systems using Bootstrap tokens and utility classes", "Responsive behavior testing across device stacks", "Bootstrap + Tailwind hybrid adoption challenges", "Prototyping interactive layouts with Bootstrap and Figma handoff", "Animation integration within Bootstrap components", "Performance tuning for Bootstrap-heavy sites", "Managing secrets securely in CI/CD pipelines", "Multi-environment deployments using Infrastructure as Code (IaC)", "GitOps implementation using ArgoCD or Flux", "Automated rollback strategies for failed releases", "Version control best practices in microservice ecosystems", "Canary and blue-green deployment integration", "End-to-end CI/CD test automation integration", "Trigger-based deployment pipelines (webhooks, Git events)", "Monitoring CI/CD pipeline health with metrics and alerts", "Mastery of modern layout techniques (CSS Grid, Flexbox)", "CSS-in-JS strategies (styled-components, Emotion)", "Performance impact of complex CSS selectors", "Creating scalable, reusable CSS architectures (BEM, SMACSS)", "Visual regression testing for CSS changes", "Advanced transitions and micro-interactions with pure CSS", "Managing style conflicts in large CSS codebases", "Dark mode theming and media query handling", "CSS Variables for theme customization and scalability", "Advanced state management (Riverpod, Bloc)", "Writing platform-specific native code with Dart FFI", "Performance profiling and frame rendering optimization", "Offline-first architecture and local storage strategies", "Deep linking and navigation in Flutter apps", "Security practices in mobile API handling (JWT, OAuth)", "Handling native SDKs across iOS and Android via Dart", "Integration with third-party services and platform channels", "Managing app lifecycle and state consistency across platforms", "Building interactive dashboards with minimal latency", "Choosing appropriate chart types for storytelling", "Automating visualization pipelines using Python or R", "Advanced DAX and custom visuals in Power BI/Tableau", "Embedding BI reports securely into enterprise platforms", "Designing scalable data models for visuals", "Crafting narrative-driven visuals for non-technical stakeholders", "Designing mobile-first or responsive visualizations", "Human-centered design principles in dashboards", "Efficient data pipeline design for large-scale training", "Hyperparameter tuning using tools like Optuna or Ray Tune", "Understanding and debugging exploding/vanishing gradients", "Custom loss function development for novel objectives", "Paper reproduction and model benchmarking practices", "Model interpretability tools (SHAP, LIME) for deep models", "Deploying CV models on edge devices or mobile", "Annotating and augmenting datasets for real-world variability", "Evaluating models on robustness, bias, and drift", "Writing optimized multi-stage Dockerfiles", "Secure container image handling and vulnerability scanning", "Integrating Docker into CI/CD with minimal build time", "Container orchestration with ECS, EKS, or GKE", "Creating production-ready Docker images for microservices", "Managing container networking and service discovery", "Debugging container failures in distributed environments", "Monitoring container metrics (Prometheus, Grafana)", "Scaling container-based infrastructure reliably", "Designing incremental and real-time ETL pipelines", "Handling schema evolution in ETL workflows", "Optimizing data ingestion using Spark, Airflow, or dbt", "Mastering orchestration tools (Apache Airflow, Prefect)", "Implementing automated data validation and alerts", "Ensuring idempotency and recovery in ETL jobs", "Understanding upstream data lineage and ETL flow impact", "Collaborating with data engineers for reliable pipelines", "Identifying bottlenecks in ETL that affect reporting quality", "Building dynamic dashboards using pivot tables and slicers", "Automating repetitive tasks with VBA or Office Scripts", "Using advanced Excel functions (INDEX-MATCH, XLOOKUP, LAMBDA)", "Scenario modeling using Excel’s What-If tools", "Creating real-time trackers with conditional formatting and formulas", "Auditing and error-checking large datasets efficiently", "Linking Excel reports to external data sources (Power Query)", "Designing professional-grade, shareable Excel dashboards", "Managing version control and collaboration in shared workbooks", "Structuring large-scale Express apps using modular design", "Implementing middleware efficiently for authentication and logging", "Managing API rate limits and performance optimization", "Handling seamless integration between frontend and Express APIs", "Managing secure RESTful API endpoints with role-based access", "Using async/await properly for backend efficiency", "Mastery of Express request lifecycle and error handling", "Implementing secure headers, CORS, and JWT in Express", "Profiling and debugging memory leaks or performance issues", "Integrating Firebase Authentication with mobile platforms", "Using Firestore effectively for real-time sync", "Managing Firebase Analytics for user behavior insights", "Using Firebase Functions for serverless backend logic", "Structuring scalable data in Firestore and Realtime Database", "Handling security rules and access controls", "Designing scalable and normalized database structures", "Minimizing read/write costs in real-time apps", "Implementing real-time listeners and syncing across devices", "Creating responsive designs using auto-layout and constraints", "Building interactive prototypes with advanced transitions", "Collaborating efficiently using components and design systems", "Aligning design with product KPIs and usability goals", "Designing end-to-end flows for user journeys", "Conducting and incorporating feedback from user testing", "Implementing complex micro-interactions in Figma prototypes", "Using variables and conditional logic in interactive flows", "Syncing interaction design with development handoff tools", "Mastery of advanced branching strategies (Git Flow, trunk-based)", "Handling complex merge conflicts across collaborative teams", "Auditing commit histories for traceability and compliance", "Automating Git workflows in CI/CD pipelines", "Managing Git hooks for quality checks and automation", "Enforcing Git policies across distributed teams", "Writing clean, informative commit messages", "Effectively using rebase, stash, and cherry-pick", "Troubleshooting detached HEAD and version rollback scenarios", "Managing organization-level GitHub projects and permissions", "Enforcing branch protection rules and code reviews", "Utilizing GitHub Actions for automation and deployments", "Understanding and adhering to contribution guidelines", "Raising well-documented pull requests and resolving review feedback", "Participating in issue discussions and community triaging", "Creating and maintaining clean GitHub repositories", "Using GitHub Discussions, Projects, and Wiki for documentation", "Implementing automated testing via GitHub Actions", "Leveraging Goroutines and channels for concurrency", "Writing memory-efficient, low-latency code", "Profiling Go applications for performance bottlenecks", "Designing RESTful APIs using Go frameworks (Gin, Echo)", "Structuring clean Go projects using idiomatic design patterns", "Connecting and managing SQL/NoSQL databases in Go", "Containerizing Go apps with Docker and deploying to Kubernetes", "Writing scalable microservices in Go", "Integrating with cloud-native tools (e.g., gRPC, Prometheus, etc.)", "Managing IAM roles and security policies effectively", "Monitoring and optimizing compute engine resources", "Automating infrastructure provisioning with Deployment Manager", "Designing cost-optimized cloud architectures", "Implementing multi-region high availability systems", "Integrating GCP services like Pub/Sub, BigQuery, and Cloud Functions", "CI/CD integration using GCP tools (Cloud Build, Cloud Run)", "Managing Kubernetes clusters on GKE", "Implementing observability with Cloud Monitoring and Logging", "Structuring semantic HTML for accessibility and SEO", "Mastering HTML5 APIs (e.g., Web Storage, Canvas, Geolocation)", "Creating responsive layouts using modern HTML techniques", "Crafting bulletproof HTML emails compatible with all clients", "Avoiding CSS pitfalls in email rendering engines", "Using media queries and fallbacks for mobile-first design", "Ensuring pixel-perfect implementation of UI designs in HTML", "Structuring reusable and scalable HTML components", "Understanding WCAG compliance and ARIA roles", "Creating and managing Jenkins pipelines as code (Jenkinsfile)", "Implementing automated testing and deployment workflows", "Scaling Jenkins with agents and distributed builds", "Integrating Jenkins with third-party tools (Slack, Docker, Nexus)", "Debugging complex job failures and optimizing builds", "Using shared libraries for pipeline code reusability", "Designing secure and efficient CI/CD workflows", "Managing credentials and secrets in Jenkins", "Implementing parallel builds and matrix jobs", "Designing production-ready Kubernetes clusters", "Implementing network policies and service meshes (e.g., Istio)", "Managing persistent volumes and storage classes", "Writing efficient Helm charts for deployments", "Automating CI/CD with Kubernetes-native tools (e.g., ArgoCD, Flux)", "Handling pod scaling, rollout strategies, and health checks", "Building self-service Kubernetes platforms for teams", "Ensuring observability with Prometheus, Grafana, and OpenTelemetry", "Maintaining multi-tenant Kubernetes environments securely", "Customizing Keras layers and loss functions", "Optimizing training for performance and memory efficiency", "Debugging model convergence and overfitting issues", "Integrating Keras models with production pipelines (e.g., TF Serving)", "Applying Keras for real-time inference in edge/cloud", "Experiment tracking and reproducibility using MLflow or Weights & Biases", "Rapidly experimenting with Keras Functional API", "Translating research papers into working Keras models", "Balancing accuracy vs. performance trade-offs in model design", "Mastering Kotlin coroutines for async operations", "Implementing Jetpack libraries (e.g., Navigation, Room) effectively", "Migrating legacy Java codebases to Kotlin", "Structuring scalable MVVM/MVI architecture in Kotlin", "Managing app lifecycle and state with Kotlin Flows and LiveData", "Integrating Kotlin Multiplatform for shared codebases", "Mastering Compose UI state management and recomposition", "Animating UI elements with Compose APIs", "Integrating Compose with traditional Views and libraries", "Tuning slow SQL queries and indexes for performance", "Automating backups, replication, and recovery processes", "Enforcing database security and user access policies", "Designing scalable MySQL schemas for large datasets", "Optimizing ETL pipelines with MySQL integrations", "Handling data versioning and schema evolution", "Writing performant SQL queries within APIs", "Managing connection pooling and transaction consistency", "Integrating MySQL with ORMs like Sequelize or TypeORM", "Fine-tuning transformer models for domain-specific tasks", "Handling noisy, low-resource, or multilingual data", "Deploying NLP models with low latency in production", "Designing benchmark evaluations for LLM-based systems", "Creating novel embeddings and pretraining objectives", "Conducting explainability and bias analysis in NLP models", "Tokenizer customization and prompt engineering techniques", "Optimizing inference and quantization for large LLMs", "Implementing retrieval-augmented generation (RAG)", "Writing non-blocking async/await logic effectively", "Structuring scalable RESTful and GraphQL APIs", "Managing environment variables and secure secrets", "Connecting Node.js with modern frontend frameworks", "Handling auth (JWT, OAuth) across stack securely", "Building CI/CD pipelines for full stack deployments", "Designing versioned APIs with OpenAPI/Swagger", "Rate-limiting, caching, and logging best practices", "Testing APIs with Postman and automated test suites", "Writing efficient vectorized operations vs. loops", "Broadcasting and reshaping multidimensional arrays", "Profiling and optimizing NumPy-heavy computations", "Leveraging NumPy for custom layer implementations", "Managing memory and array copying behavior", "Integrating NumPy arrays with other ML libraries", "Handling numerical instability in large-scale simulations", "Writing unit tests for numerical algorithms", "Using NumPy alongside SciPy for scientific analysis", "Applying object detection and tracking algorithms", "Preprocessing visual data for ML pipelines", "Working with real-time video stream processing", "Integrating OpenCV with ROS-based systems", "Calibrating cameras and correcting distortions", "Developing stereo vision and depth estimation", "Extracting and engineering features from images", "Combining OpenCV with deep learning models", "Optimizing vision pipelines for performance", "Handling large datasets efficiently with chunking", "Writing complex groupby, pivot, and melt operations", "Chaining operations with method chaining for clarity", "Optimizing data pipelines with vectorized operations", "Managing missing values and data imputation techniques", "Combining Pandas with NumPy, Scikit-learn, and matplotlib", "Automating data cleaning and transformation pipelines", "Ensuring data consistency across multiple sources", "Logging, error handling, and validation in ETL scripts", "Interpreting penetration testing reports and risk scoring", "Identifying misconfigurations in modern cloud platforms", "Implementing preventive controls post-vulnerability scans", "Simulating sophisticated attack vectors (e.g., phishing, lateral movement)", "Evading detection tools and logging mechanisms", "Reporting findings in alignment with MITRE ATT&CK framework", "Prioritizing CVEs based on exploitability and business impact", "Performing authenticated vs unauthenticated scans", "Utilizing tools like Nessus, Burp Suite, and OWASP ZAP effectively", "Automating backups, WAL archiving, and PITR", "Tuning PostgreSQL configurations for performance (e.g., shared_buffers, work_mem)", "Managing roles, permissions, and security policies", "Designing normalized and denormalized schemas", "Building CDC (Change Data Capture) pipelines", "Managing large-scale partitioned tables and indexes", "Writing secure, optimized SQL queries within ORM contexts", "Handling transactions, locks, and deadlock prevention", "Using PostgreSQL-specific features like JSONB, CTEs, and window functions", "Building optimized data models using star and snowflake schemas", "Writing advanced DAX expressions for dynamic measures", "Designing interactive dashboards with cross-filtering and drill-down", "Integrating Power BI with cloud sources (e.g., Azure, GCP, AWS)", "Implementing row-level security (RLS) for data access control", "Creating reusable templates and themes for consistency", "Automating report refresh and scheduling with Power BI Service", "Using bookmarks, tooltips, and custom visuals for enhanced UX", "Managing Power BI workspaces and sharing governance", "Writing efficient Pandas/Numpy code for large datasets", "Automating analysis workflows using scripting and scheduling", "Creating visualizations using Matplotlib, Seaborn, or Plotly", "Structuring scalable APIs with Flask or FastAPI", "Writing asynchronous code using `asyncio` and `aiohttp`", "Managing background tasks, jobs, and queues (e.g., Celery)", "Organizing ML code using clean architecture and pipelines", "Tracking experiments with MLflow or Weights & Biases", "Handling model deployment and serving with FastAPI or Flask", "Writing efficient R scripts for large-scale statistical modeling", "Implementing reproducible research using RMarkdown and knitr", "Using the `tidyverse` for modern, clean data manipulation", "Building machine learning models using `caret` and `mlr3`", "Handling big data with `data.table` and database connections (DBI)", "Creating interactive visualizations using `shiny` and `plotly`", "Applying advanced statistical tests and multivariate analysis", "Automating data pipelines and reporting workflows in R", "Visualizing longitudinal and time-series data effectively", "Implementing complex state management using Redux Toolkit or Zustand", "Optimizing React app performance and lazy loading strategies", "Managing component reusability and prop drilling solutions", "Creating accessible, WCAG-compliant components", "Styling with utility-first CSS frameworks (e.g., Tailwind CSS)", "Animating UI transitions with Framer Motion or React Spring", "Integrating React with secure backend APIs and auth (JWT, OAuth)", "Managing monorepos with tools like Nx or Turborepo", "Testing frontends with Jest, React Testing Library, and Cypress", "Implementing responsive UIs with React Native Flexbox", "Managing navigation stacks with React Navigation", "Handling offline support and local storage with SQLite or AsyncStorage", "Bridging native modules for platform-specific features", "Optimizing app performance and reducing bundle size", "Using Expo vs bare workflow based on project scope", "Ensuring consistent design and behavior across iOS/Android", "Leveraging device APIs (camera, GPS, notifications) securely", "Testing and debugging on real devices and emulators effectively", "Implementing Redis for caching strategies to reduce database load", "Managing Redis key expiration, eviction policies, and data persistence", "Monitoring Redis performance and debugging latency issues", "Integrating Redis streams for real-time data pipelines", "Leveraging Redis as a message broker (e.g., pub/sub architecture)", "Scaling Redis clusters for high-availability data workflows", "Designing distributed systems using Redis Sentinel and Cluster mode", "Ensuring Redis security (AUTH, ACLs, SSL/TLS setup)", "Balancing memory constraints vs speed in large-scale architectures", "Designing RESTful endpoints following OpenAPI/Swagger standards", "Implementing proper error handling, pagination, and versioning", "Ensuring secure REST APIs (rate limiting, auth, validation)", "Creating scalable, modular API layers with FastAPI/Express/Django", "Writing automated tests for API endpoints", "Optimizing API response time and payload size", "Connecting heterogeneous systems via REST APIs efficiently", "Handling API gateways, throttling, and service meshes", "Troubleshooting API failures in distributed environments", "Mastering Ruby on Rails conventions for rapid development", "Integrating frontend stacks (React/Vue) with Rails backends", "Writing maintainable and test-driven Ruby code", "Profiling and optimizing Ruby code for performance bottlenecks", "Managing background jobs using Sidekiq or Resque", "Structuring APIs and services with Rails API mode or Sinatra", "Automating Ruby-based CI/CD pipelines with tools like Capistrano", "Managing environment variables and secure configs in Rails apps", "Monitoring Ruby apps in production (e.g., New Relic, Scout)", "Optimizing model performance using pipeline and GridSearchCV", "Handling imbalanced datasets with techniques like SMOTE or class weighting", "Integrating Scikit-learn models into production APIs", "Interpreting model outputs and feature importance for stakeholders", "Creating reusable modeling pipelines with transformers and estimators", "Understanding model limitations and selecting appropriate metrics", "Combining Scikit-learn with deep learning libraries for hybrid models", "Customizing estimators and extending Scikit-learn classes", "Building scalable training and inference systems using Scikit-learn", "Enforcing Scrum ceremonies while adapting to team dynamics", "Removing team blockers through proactive facilitation", "Coaching teams on Agile maturity and continuous improvement", "Balancing traditional PM responsibilities with Agile values", "Managing cross-functional teams in SAFe or LeSS environments", "Translating business requirements into prioritized sprints", "Writing clear, value-driven user stories and acceptance criteria", "Managing product backlogs using tools like Jira or Azure Boards", "Collaborating with devs and stakeholders for roadmap clarity", "Creating multi-variable plots for insights (e.g., `pairplot`, `catplot`)", "Fine-tuning plot aesthetics and themes for dashboards or reports", "Communicating statistical relationships visually (confidence intervals, etc.)", "Customizing Seaborn with Matplotlib for detailed control", "Storytelling with comparative and temporal visualizations", "Scaling visualizations for large datasets and interactivity", "Choosing the right visual representation for statistical analyses", "Annotating plots with meaningful context and metadata", "Using Seaborn in exploratory data analysis for hypothesis generation", "Writing idempotent scripts for CI/CD pipelines", "Automating infrastructure tasks using Bash with tools like Ansible", "Debugging shell scripts in cross-platform environments", "Managing cron jobs and log automation for system health checks", "Creating reusable maintenance scripts with parameters and loops", "Ensuring secure scripting practices (permissions, escaping, etc.)", "Integrating shell scripts with Jenkins, Git, or Python workflows", "Building monitoring and alerting scripts for microservices", "Documenting and modularizing automation scripts for teams", "Writing optimized queries for large datasets using joins and CTEs", "Performing complex aggregations and time-series analysis", "Automating SQL report generation with scripts or BI tools", "Designing normalized and efficient schemas", "Writing stored procedures, triggers, and indexing strategies", "Ensuring data consistency and integrity through constraints", "Translating business KPIs into actionable SQL queries", "Creating dashboards from SQL outputs (Power BI, Tableau, etc.)", "Handling nested queries and performance tuning", "Adopting Swift Concurrency with async/await and structured concurrency", "Managing app states using Combine or SwiftData", "Writing testable, modular Swift code with protocol-oriented programming", "Implementing advanced animations and gesture recognizers", "Integrating iOS-specific APIs (e.g., CoreML, ARKit) using Swift", "Ensuring backward compatibility and adaptive layouts", "Applying design patterns in Swift (MVVM, VIPER, etc.)", "Writing reusable components and extensions", "Using Swift Package Manager and handling dependencies effectively", "Structuring reusable utility-first components efficiently", "Managing large-scale design systems using Tailwind with CSS-in-JS tools", "Optimizing Tailwind performance for production builds", "Creating fully responsive layouts using Tailwind’s grid and flex utilities", "Extending Tailwind with custom themes and plugin integrations", "Ensuring accessibility compliance with utility-first styling", "Translating Figma/Sketch designs into Tailwind-based interfaces", "Designing dark/light mode themes with Tailwind utilities", "Leveraging Tailwind UI components effectively for rapid prototyping", "Building interactive dashboards with dynamic filters and actions", "Writing complex calculated fields and LOD (Level of Detail) expressions", "Embedding Tableau into web platforms or enterprise systems", "Turning business KPIs into actionable Tableau visual insights", "Creating automated report workflows using Tableau Prep", "Applying forecasting, clustering, and trend lines within Tableau", "Optimizing Tableau dashboards for performance and scalability", "Managing data extracts and live connections securely", "Using Tableau REST API for automation and user access control", "Building custom training loops using TensorFlow 2.x and Keras APIs", "Debugging training instability using TensorBoard and callbacks", "Optimizing model training using mixed precision and distributed strategies", "Deploying TensorFlow models using TensorFlow Serving or TFLite", "Integrating models with real-time inference pipelines", "Handling data preprocessing pipelines within TensorFlow efficiently", "Using TensorFlow for object detection and segmentation (TF Object Detection API)", "Applying transfer learning with CNN backbones (e.g., EfficientNet, ResNet)", "Exporting and optimizing models for edge devices (TFLite, Coral, etc.)", "Writing strongly typed reusable components with TypeScript", "Managing types across API integrations and asynchronous data", "Using advanced utility types and generics for scalable frontends", "Structuring monorepos using TypeScript across frontend and backend", "Type-safe database queries using tools like Prisma or Drizzle", "Integrating strict typing with GraphQL and REST APIs", "Managing application-wide state with Redux Toolkit and TypeScript", "Handling TypeScript in build systems (Vite/Webpack) efficiently", "Creating end-to-end typed test cases using Cypress or Playwright", "Using Composition API and reactive refs efficiently", "Managing modular architecture in large-scale Vue apps", "Optimizing performance with lazy loading and dynamic imports", "Creating reusable components and slots using Vue 3", "Integrating Tailwind CSS or Vuetify with Vue projects", "Ensuring accessibility and responsiveness across devices", "Combining Vue with modern JS patterns (e.g., Observables, Proxies)", "Managing state with Pinia or Vuex in complex data apps", "Testing Vue components with Vitest or Vue Test Utils", "Developing secure smart contracts with Solidity and Hardhat", "Managing wallet integration and authentication (e.g., MetaMask, WalletConnect)", "Handling gas optimization and smart contract upgrades", "Designing scalable dApp architectures across L1 and L2 chains", "Implementing cross-chain bridges and interoperability protocols", "Maintaining on-chain/off-chain data sync with oracles", "Building responsive frontends with Web3.js/Ethers.js and Vue/React", "Using IPFS/Filecoin for decentralized storage integration", "Auditing contracts for common vulnerabilities (Reentrancy, Overflows)", "Interpreting packet-level anomalies and protocol behaviors", "Automating traffic analysis with tshark and scripting", "Detecting covert channels and encrypted threats in live captures", "Creating custom filters and profiles for intrusion detection", "Integrating Wireshark with SIEM/logging systems", "Performing forensic analysis on pcap dumps from advanced threats", "Correlating network captures with incident response timelines", "Identifying lateral movement and pivoting in packet data", "Extracting indicators of compromise (IoCs) from raw traffic", "Developing domain-specific tokenizers and pipelines", "Applying weak supervision and prompt-based tuning", "Handling multilingual and low-resource NLP tasks", "Innovating on text generation and reasoning with large corpora", "Evaluating NLP systems using advanced benchmarks (e.g., HELM, SuperGLUE)", "Developing ethical and unbiased NLP systems for global deployment", "Designing multi-turn conversations with contextual memory", "Integrating NLP backends with frontend UX tools", "Fine-tuning open-source LLMs for dialogue systems", "Fine-tuning transformer models with LoRA, PEFT, and QLoRA", "Tokenizing and managing long sequences with memory-efficient methods", "Deploying transformer pipelines using HuggingFace Accelerate", "Quantizing and pruning large models for on-device inference", "Building custom attention mechanisms for domain-specific tasks", "Evaluating hallucination and factuality in model outputs", "Training large-scale models with distributed GPUs and TPUs", "Using Retrieval-Augmented Generation (RAG) pipelines", "Managing token limits, latency, and scaling in production LLMs"],
}


# ------------------- Role to Career Path -------------------
career_paths = {
    "MLOps Engineer": [

    ],
    "AI Engineer": [

    ],
    "ML Platform Engineer"": [
        "Master ML model lifecycle: versioning, packaging, and serving (MLflow, TFX)",
        "Learn CI/CD for ML with Jenkins, GitHub Actions, or Kubeflow Pipelines",
        "Use Docker, Kubernetes, and cloud platforms (AWS/GCP/Azure) for scalable deployment"
    ],
    "Cloud Engineer": [

    ],
    "Solutions Architect": [

    ],
    "DevOps Engineer (AWS": [
        "Deep dive into AWS core services: EC2, S3, Lambda, IAM, and VPC",
        "Automate infrastructure using Terraform or AWS CloudFormation",
        "Set up CI/CD, containerization (ECS/EKS), and monitoring with CloudWatch"
    ],
    "Azure Specialist": [

    ],
    "Infrastructure Engineer (Azure": [
        "Learn Azure core services: App Services, Functions, Azure VMs, and Storage",
        "Implement DevOps workflows using Azure DevOps and Bicep",
        "Focus on network/security best practices and Azure Monitor for observability"
    ],
    "Data Engineer": [

    ],
    "Analytics Engineer": [

    ],
    "BI Developer (BigQuery": [
        "Master SQL for analytics and Google BigQuery's architecture and pricing model",
        "Learn ELT data workflows using Dataflow, dbt, or Apache Beam",
        "Build dashboards by integrating BigQuery with Looker Studio, Tableau, or Power BI"
    ],
    "Blockchain Developer": [

    ],
    "Smart Contract Engineer": [

    ],
    "Web3 Developer"": [
        "Learn Ethereum architecture and smart contract development using Solidity",
        "Explore frameworks like Hardhat, Truffle, and testing with Ganache",
        "Integrate Web3.js or Ethers.js with DApps and deploy using IPFS or Alchemy"
    ],
    "Frontend Developer": [

    ],
    "UI Engineer": [

    ],
    "Web Designer (Bootstrap": [
        "Learn responsive design principles and master Bootstrap 5 components",
        "Customize Bootstrap with SCSS and extend UI with JavaScript interactions",
        "Optimize designs for performance and accessibility (a11y, ARIA roles)"
    ],
    "DevOps Engineer": [

    ],
    "Release Engineer": [

    ],
    "Automation Engineer (CI/CD": [
        "Learn CI/CD fundamentals and tools like Jenkins, GitHub Actions, and GitLab CI",
        "Automate build-test-deploy workflows and integrate with Docker/Kubernetes",
        "Implement rollback strategies, monitor pipelines, and handle release orchestration"
    ],
    "UI/UX Engineer": [

    ],
    "Web Developer (CSS": [
        "Master CSS fundamentals: Flexbox, Grid, transitions, and media queries",
        "Learn BEM naming conventions and CSS preprocessors like SASS/SCSS",
        "Build responsive, cross-browser UIs and apply accessibility best practices"
    ],
    "Flutter Developer": [

    ],
    "Mobile App Engineer": [

    ],
    "Cross-Platform Developer (Dart": [
        "Master Dart fundamentals and async programming with Futures & Streams",
        "Learn Flutter widgets, layouts, state management (Provider/Bloc)",
        "Build, test, and deploy cross-platform apps using Firebase or APIs"
    ],
    "Data Analyst": [

    ],
    "BI Developer": [

    ],
    "Data Storyteller (Data Visualization": [
        "Understand data storytelling principles and dashboard best practices",
        "Learn tools like Tableau, Power BI, and libraries like Seaborn, Plotly",
        "Practice designing executive-level dashboards and interpreting insights"
    ],
    "Deep Learning Engineer": [

    ],
    "AI Researcher": [

    ],
    "Computer Vision Engineer (Deep Learning": [
        "Learn neural networks, CNNs, RNNs using TensorFlow or PyTorch",
        "Master transfer learning, attention mechanisms, and model tuning",
        "Apply DL to real-world tasks like image classification and object detection"
    ],
    "Site Reliability Engineer (Docker": [
        "Learn containerization basics and Docker CLI for image/lifecycle management",
        "Build Dockerfiles, use Compose, and manage multi-container setups",
        "Integrate Docker into CI/CD workflows and deploy to Kubernetes or cloud"
    ],
    "ETL Developer": [

    ],
    "BI Analyst (ETL Tools": [
        "Learn ETL concepts and design data pipelines using tools like Apache NiFi, Talend, or Informatica",
        "Gain proficiency in writing efficient SQL for data extraction and transformation",
        "Work with cloud-based ETL tools (e.g., AWS Glue, Azure Data Factory) for scalable solutions"
    ],
    "Operations Analyst": [

    ],
    "Reporting Specialist (Excel": [
        "Master Excel formulas, pivot tables, and data cleaning techniques",
        "Learn advanced features like Power Query, Power Pivot, and VBA scripting",
        "Visualize and report insights through dashboards and charts for decision support"
    ],
    "Backend Developer": [

    ],
    "Full Stack Developer": [

    ],
    "Node.js Engineer (Express.js": [
        "Learn core concepts of Node.js and asynchronous JavaScript (Promises, async/await)",
        "Build RESTful APIs using Express.js with routing, middleware, and error handling",
        "Integrate Express with databases (MongoDB, PostgreSQL) and secure APIs with JWT/OAuth"
    ],
    "Mobile App Developer": [

    ],
    "Realtime Database Engineer (Firebase": [
        "Learn core Firebase services: Firestore, Realtime Database, Authentication, and Cloud Functions",
        "Integrate Firebase into mobile apps for real-time sync and backend functionality",
        "Explore Firebase Hosting, Analytics, and security rules for end-to-end app development"
    ],
    "UI/UX Designer": [

    ],
    "Product Designer": [

    ],
    "Interaction Designer (Figma": [
        "Master Figma interface, auto-layout, components, and design systems",
        "Practice wireframing, prototyping, and creating interactive user flows",
        "Collaborate using Figma's team features and implement accessibility-focused designs"
    ],
    "Version Control Engineer": [

    ],
    "Software Developer (Git": [
        "Master Git fundamentals: branching, merging, rebasing, conflict resolution",
        "Learn to manage repositories with Git CLI and GUI tools",
        "Explore advanced workflows: GitFlow, trunk-based development"
    ],
    "Collaboration Engineer": [

    ],
    "Open Source Contributor": [

    ],
    "Software Engineer (GitHub": [
        "Understand GitHub features: forks, pull requests, actions, issues, and projects",
        "Practice collaborative development with branching and review workflows",
        "Contribute to open-source projects and build a visible GitHub profile"
    ],
    "Systems Engineer": [

    ],
    "Cloud-Native Developer (Go": [
        "Learn Go syntax, goroutines, and channels for concurrency",
        "Build web services using Go’s standard library or frameworks like Gin",
        "Write performant, modular, and testable Go code for backend systems"
    ],
    "GCP Solutions Architect": [

    ],
    "DevOps Specialist (GCP": [
        "Understand GCP core services: Compute Engine, Cloud Storage, VPC, IAM",
        "Learn GCP deployment tools like Cloud Build and Deployment Manager",
        "Master GCP DevOps practices: CI/CD, monitoring, and infrastructure automation"
    ],
    "Email Developer": [

    ],
    "Web Designer (HTML": [
        "Master HTML5 semantic elements, forms, tables, and media tags",
        "Understand responsive layout structure with HTML and CSS integration",
        "Practice accessibility standards (ARIA) and SEO-friendly HTML markup"
    ],
    "Automation Engineer": [

    ],
    "CI/CD Specialist (Jenkins": [
        "Learn Jenkins fundamentals: freestyle projects, pipelines, plugins",
        "Implement CI/CD workflows using Jenkinsfile and declarative pipelines",
        "Integrate Jenkins with Git, Docker, Kubernetes, and monitoring tools"
    ],
    "Cloud Infrastructure Engineer": [

    ],
    "Platform Engineer (Kubernetes": [
        "Understand core Kubernetes concepts: pods, deployments, services, namespaces",
        "Practice writing YAML files for resource definitions and Helm chart templating",
        "Master cluster scaling, monitoring, and Kubernetes-native CI/CD workflows"
    ],
    "Model Prototyper (Keras": [
        "Learn deep learning fundamentals: layers, activations, optimizers, loss functions",
        "Build models using Keras Sequential and Functional APIs",
        "Train and fine-tune models using callbacks, regularization, and transfer learning"
    ],
    "Android Developer": [

    ],
    "Jetpack Compose Developer (Kotlin": [
        "Master Kotlin syntax, OOP principles, and coroutines for async operations",
        "Build apps using Jetpack components: Navigation, Room, LiveData, ViewModel",
        "Explore Jetpack Compose for declarative UI and integrate with existing components"
    ],
    "Database Administrator": [

    ],
    "Backend Developer (MySQL": [
        "Learn MySQL syntax, data types, indexing, and query optimization",
        "Manage schemas, users, and security using MySQL Workbench or CLI",
        "Perform database tuning, backup strategies, and replication setup"
    ],
    "NLP Engineer": [

    ],
    "Language Model Developer (NLP": [
        "Master text preprocessing, tokenization, and embeddings",
        "Explore classical NLP tasks (NER, POS tagging, sentiment analysis) using libraries like spaCy and NLTK",
        "Train transformer models (e.g., BERT, GPT) using Hugging Face and fine-tuning techniques"
    ],
    "API Developer (Node.js": [
        "Understand Node.js runtime, event loop, and async programming",
        "Build RESTful APIs using Express.js and integrate with databases",
        "Apply authentication, testing (Jest), and containerization with Docker"
    ],
    "Data Scientist": [

    ],
    "ML Engineer": [

    ],
    "Scientific Programmer (NumPy": [
        "Learn NumPy arrays, broadcasting, and linear algebra operations",
        "Optimize numerical computation using vectorization and array manipulation",
        "Integrate NumPy with Pandas, SciPy, and machine learning workflows"
    ],
    "Computer Vision Engineer": [

    ],
    "Robotics Engineer": [

    ],
    "ML Developer (OpenCV": [
        "Learn image processing fundamentals: filters, contours, transformations",
        "Use OpenCV for object detection, tracking, and feature extraction",
        "Integrate OpenCV with deep learning models for real-time applications"
    ],
    "ETL Developer (Pandas": [
        "Master data structures: Series, DataFrames, indexing, and slicing",
        "Perform data cleaning, aggregation, and transformation operations",
        "Integrate Pandas workflows with NumPy, Matplotlib, and Scikit-learn"
    ],
    "Security Analyst": [

    ],
    "Red Team Specialist": [

    ],
    "Vulnerability Assessor (Penetration Testing": [
        "Learn ethical hacking fundamentals, OWASP Top 10, and reconnaissance techniques",
        "Use tools like Nmap, Metasploit, and Burp Suite for penetration testing",
        "Conduct vulnerability assessments and write detailed remediation reports"
    ],
    "Backend Developer (PostgreSQL": [
        "Understand PostgreSQL architecture, data types, and indexing",
        "Write efficient SQL queries, joins, and stored procedures",
        "Perform database tuning, replication, and security hardening"
    ],
    "BI Analyst": [

    ],
    "Reporting Specialist (Power BI": [
        "Load and transform data using Power Query and DAX",
        "Build interactive dashboards and KPI reports",
        "Share and publish insights via Power BI Service and apps"
    ],
    "Machine Learning Engineer (Python": [
        "Master Python fundamentals: data types, functions, OOP, and error handling",
        "Work with libraries like Pandas, NumPy, and Requests for real-world tasks",
        "Dive into ML workflows using Scikit-learn, TensorFlow, or PyTorch"
    ],
    "Statistician": [

    ],
    "Research Analyst (R": [
        "Learn data manipulation with dplyr and data visualization with ggplot2",
        "Conduct statistical modeling using linear regression, ANOVA, and time-series",
        "Use R Markdown and Shiny for reporting and interactive dashboards"
    ],
    "UI Developer": [

    ],
    "Full Stack Developer (React": [
        "Understand JSX, components, props, and state management",
        "Build single-page applications using React Router and Hooks",
        "Integrate REST APIs and manage global state with Redux or Context API"
    ],
    "React Native Developer": [

    ],
    "Cross-Platform App Developer (React Native": [
        "Learn React Native core components and styling with Flexbox",
        "Handle navigation, state, and device features (camera, GPS)",
        "Optimize performance and deploy apps to Android and iOS stores"
    ],
    "System Architect (Redis": [
        "Learn Redis data structures (strings, hashes, sets) and persistence models",
        "Implement caching strategies for improving backend performance",
        "Set up Redis clustering and pub/sub patterns for scalable systems"
    ],
    "API Developer": [

    ],
    "Integration Engineer (REST APIs": [
        "Understand REST principles: statelessness, resources, verbs, status codes",
        "Build APIs with frameworks like Express.js, Flask, or Django",
        "Document and secure APIs using Swagger/OpenAPI and OAuth2"
    ],
    "Web Developer": [

    ],
    "Backend Engineer": [

    ],
    "DevOps Engineer (Ruby": [
        "Learn Ruby syntax, control flow, OOP, and metaprogramming",
        "Build web apps using Ruby on Rails, focusing on MVC and RESTful routes",
        "Optimize deployments with Capistrano and integrate CI/CD pipelines"
    ],
    "Machine Learning Engineer": [

    ],
    "AI Engineer (Scikit-learn": [
        "Understand supervised/unsupervised learning concepts and ML workflows",
        "Apply Scikit-learn for preprocessing, model training, and evaluation",
        "Tune models using GridSearchCV and Pipelines for reproducibility"
    ],
    "Scrum Master": [

    ],
    "Agile Project Manager": [

    ],
    "Product Owner (Scrum": [
        "Learn Agile principles and Scrum framework (sprints, roles, ceremonies)",
        "Master backlog grooming, sprint planning, and velocity tracking",
        "Use tools like Jira/Trello and practice servant leadership"
    ],
    "Data Visualization Specialist": [

    ],
    "Research Analyst (Seaborn": [
        "Explore Seaborn for statistical plots: box, violin, pairplot, heatmaps",
        "Combine with Pandas and Matplotlib for in-depth analysis",
        "Customize plot aesthetics for storytelling and reporting"
    ],
    "Systems Administrator": [

    ],
    "Automation Engineer (Shell Scripting": [
        "Master Bash scripting: variables, loops, conditionals, and functions",
        "Automate system tasks like backups, monitoring, and deployments",
        "Integrate with cron jobs and other DevOps tools (Docker, Jenkins)"
    ],
    "Database Developer": [

    ],
    "BI Analyst (SQL": [
        "Learn SQL basics: SELECT, JOINs, GROUP BY, subqueries",
        "Optimize queries and use indexing for performance",
        "Work with analytical functions (RANK, LAG) for advanced insights"
    ],
    "Mobile Developer": [

    ],
    "Embedded Systems Engineer": [

    ],
    "Application Developer (SQLite": [
        "Understand SQLite's structure, constraints, and transactions",
        "Integrate SQLite with Android, Flutter, or desktop apps",
        "Optimize performance using indexing and parameterized queries"
    ],
    "iOS Developer": [

    ],
    "Software Engineer (Swift": [
        "Learn Swift fundamentals: optionals, structs, protocols, closures",
        "Build apps using UIKit or SwiftUI and manage state with MVVM",
        "Test, debug, and publish iOS apps through Xcode and App Store"
    ],
    "Web Designer (Tailwind CSS": [
        "Learn utility-first CSS concepts and Tailwind configuration",
        "Build responsive layouts using Tailwind grid and flex utilities",
        "Customize themes and extend Tailwind with plugins"
    ],
    "Data Visualization Analyst": [

    ],
    "Business Analyst": [

    ],
    "BI Developer (Tableau": [
        "Master Tableau basics: dimensions, measures, and calculated fields",
        "Create dashboards with filters, actions, and storytelling techniques",
        "Connect to live data sources and optimize dashboard performance"
    ],
    "Computer Vision Engineer (TensorFlow": [
        "Understand TensorFlow core APIs and model-building workflows (Sequential, Functional)",
        "Train models on image, text, and tabular data using GPU acceleration",
        "Deploy models using TensorFlow Serving, Lite, or.js"
    ],
    "Application Engineer (TypeScript": [
        "Learn TypeScript syntax: types, interfaces, generics, and type inference",
        "Integrate TypeScript into React, Angular, or Node.js projects",
        "Use type safety to improve code maintainability and scalability"
    ],
    "JavaScript Developer (Vue.js": [
        "Learn Vue.js fundamentals: directives, components, and reactivity system",
        "Build apps using Vue Router, Vuex, and Composition API",
        "Optimize performance and test Vue apps with Jest and Vite"
    ],
    "Web3 Developer": [

    ],
    "Blockchain Engineer": [

    ],
    "DApp Developer (Web3": [
        "Understand blockchain fundamentals and smart contract logic",
        "Learn Solidity and deploy contracts using Remix or Hardhat",
        "Integrate smart contracts into frontends using Web3.js or Ethers.js"
    ],
    "Network Analyst": [

    ],
    "Cybersecurity Engineer": [

    ],
    "SOC Analyst (Wireshark": [
        "Learn networking protocols (TCP/IP, HTTP, DNS, etc.)",
        "Master packet sniffing, filtering, and analysis using Wireshark",
        "Detect anomalies, security threats, and latency issues"
    ],
    "Reporting Analyst": [

    ],
    "Marketing Data Analyst": [

    ],
    "BI Specialist (Google Data Studio": [
        "Understand data connectors and build insightful dashboards",
        "Use calculated fields, blended data, and interactive controls",
        "Share, schedule, and optimize performance of reports"
    ],
    "Chatbot Developer (NLP": [
        "Learn text preprocessing, tokenization, and embeddings",
        "Apply NLP pipelines with spaCy, NLTK, and Hugging Face",
        "Build chatbots and sentiment models with fine-tuned transformers"
    ],
    "LLM Specialist (Transformers": [
        "Study transformer architecture: attention, encoders, decoders",
        "Train/fine-tune models using Hugging Face Transformers and datasets",
        "Deploy LLMs using ONNX, TorchServe, or API-based solutions"
    ],
}


# ------------------- App Interface -------------------
st.markdown("### 💡 Select Your Skill")
selected_skill = st.selectbox("Choose a technical skill:", list(skill_to_roles.keys()))

if selected_skill:
    st.markdown(f"### 💼 Roles Related to: {selected_skill}")
    roles = skill_to_roles[selected_skill]

    for role in roles:
        st.markdown(f"#### 🔹 {role}")

        # Placeholder Skill Gaps (customize as needed)
        st.markdown(f"### 🔧 Skill Gaps Identified: {role}")
        st.write("- Skill gap 1 (customize if needed)")
        st.write("- Skill gap 2")
        st.write("- Skill gap 3")

        # Career Path
        st.markdown(f"### 🛤️ Career Path for {role}")
        for step in career_paths.get(role, ["No path found"]):
            st.write(f"✅ {step}")
