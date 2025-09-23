import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import base64
import time

# Page config
st.set_page_config(
    page_title="Dnyaneshwar Bhosale - AI Engineer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful styling
st.markdown("""
<style>
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom styling */
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .skill-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    
    .project-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
    }
    
    .experience-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.37);
    }
    
    .education-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(240, 147, 251, 0.4);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin: 0.5rem;
    }
    
    .contact-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.8rem 2rem;
        border-radius: 25px;
        text-decoration: none;
        display: inline-block;
        margin: 0.5rem;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        transition: transform 0.3s ease;
    }
    
    .contact-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Animated gradient background */
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Custom sidebar */
    .css-1d391kg {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .css-1d391kg .css-1v0mbdj {
        color: white;
    }
    
    /* Typography */
    .big-font {
        font-size: 3rem !important;
        font-weight: bold;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
    }
    
    .medium-font {
        font-size: 1.5rem !important;
        color: #4a5568;
        text-align: center;
    }
    
    /* Progress bars */
    .stProgress .st-bo {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .fade-in {
        animation: fadeIn 0.8s ease-out;
    }
    
    /* Custom containers */
    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("# 🚀 Navigation")
page = st.sidebar.selectbox("Choose Section", 
    ["🏠 Home", "👨‍💻 About", "⚡ Skills", "💼 Experience", "🚀 Projects", "🎓 Education", "📞 Contact"])

# Helper function for typing effect simulation
def create_typing_effect(text, placeholder):
    for i in range(len(text) + 1):
        placeholder.markdown(f"<h2 style='color: #667eea; font-weight: bold;'>{text[:i]}|</h2>", unsafe_allow_html=True)
        time.sleep(0.1)

# Main Content
if page == "🏠 Home":
    # Hero Section
    st.markdown("""
    <div class="main-header fade-in">
        <h1>Hi, I'm Dnyaneshwar Bhosale 👋</h1>
        <h2>AI Engineer | Data Scientist | Generative AI Enthusiast</h2>
        <p style="font-size: 1.2rem; margin-top: 1rem;">
            🚀 Passionate about building intelligent, data-driven solutions using Machine Learning, Deep Learning, NLP, and Generative AI. 
            Skilled in turning raw data into actionable insights and creating real-world AI applications.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Contact Info
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>📧 Email</h3>
            <p>dnyaneshwarbhosale111@gmail.com</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>📞 Phone</h3>
            <p>+91 9082063239</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>💼 GitHub</h3>
            <p>Portfolio Projects</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>🔗 LinkedIn</h3>
            <p>Professional Network</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick Stats
    st.markdown("---")
    st.markdown("### 📊 Quick Stats")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Experience", "1.4 year", "Currently Working")
    with col2:
        st.metric("Projects", "7+ Major", "AI/ML Focus")
    with col3:
        st.metric("Education", "M.Sc. Math", "Mumbai University")
    with col4:
        st.metric("Specialization", "GenAI & NLP", "Advanced")

elif page == "👨‍💻 About":
    st.markdown('<p class="big-font">📝 About Me</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Animated profile placeholder
        st.markdown("""
        <div style="text-align: center; padding: 2rem;">
            <div style="width: 200px; height: 200px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        border-radius: 50%; margin: 0 auto; display: flex; align-items: center; justify-content: center;
                        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);">
                <span style="color: white; font-size: 4rem; font-weight: bold;">🧠</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        I'm an adaptable **AI Engineer & Data Scientist** with expertise in **Machine Learning, Deep Learning, NLP, and Generative AI**.

        <p>With a strong background in <strong>Mathematics and Statistics</strong>, 
        I specialize in building robust models, deploying end-to-end AI applications, 
        and developing innovative solutions that solve real-world problems.</p>

        <h3>🔥 What Drives Me?</h3>
        <ul>
        <li>🚀 Building intelligent systems that make a difference</li>
        <li>📊 Transforming complex data into actionable insights</li>
        <li>🤖 Exploring the frontiers of Generative AI and LLMs</li>
        <li>💡 Solving real-world problems with AI/ML solutions</li>
        </ul>
        """, unsafe_allow_html=True)

    # Core Competencies
    st.markdown("### 🎯 Core Competencies")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="project-card">
            <h4>🤖 AI/ML Engineering</h4>
            <p>End-to-end model development, deployment, and optimization</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="project-card">
            <h4>🧠 Generative AI</h4>
            <p>LLMs, RAG systems, and agentic AI applications</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="project-card">
            <h4>📊 Data Science</h4>
            <p>Statistical analysis, data visualization, and insights</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "⚡ Skills":
    st.markdown('<p class="big-font">⚡ Technical Skills</p>', unsafe_allow_html=True)
    
    # Skills data
    skills_data = {
        'Programming & Data': ['Python', 'SQL', 'Pandas', 'NumPy'],
        'ML & AI': ['Scikit-learn', 'TensorFlow', 'Keras', 'Machine Learning', 'Deep Learning', 'Generative AI', 'LLMs'],
        'Specialized Areas': ['NLP', 'Agentic AI', 'LangChain', 'LlamaIndex', 'RAG', 'Computer Vision'],
        'Tools & Platforms': ['Streamlit', 'FAISS', 'VectorDB', 'Power BI', 'Git/GitHub'],
        'Mathematics & Statistics': ['MSc Mathematics', 'Statistical Analysis', 'Mathematical Modeling']
    }
    
    # Interactive skill levels
    skill_levels = {
        'Programming & Data': 90,
        'ML & AI': 85,
        'Specialized Areas': 88,
        'Tools & Platforms': 82,
        'Mathematics & Statistics': 95
    }
    
    # Create interactive skill visualization
    for category, skills in skills_data.items():
        with st.container():
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"""
                <div class="skill-card">
                    <h3>{category}</h3>
                    <p>{', '.join(skills)}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                # Progress bar
                progress = skill_levels[category]
                st.metric(f"Proficiency", f"{progress}%")
                st.progress(progress / 100)
    
    # Skills Chart
    st.markdown("### 📈 Skills Overview")
    
    # Create radar chart using go.Scatterpolar
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=[skill_levels[cat] for cat in skill_levels.keys()],
        theta=list(skill_levels.keys()),
        fill='toself',
        name='Skills',
        line_color='#667eea'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        showlegend=False,
        title="Technical Skills Radar Chart",
        title_font_size=20,
        title_x=0.5
    )
    st.plotly_chart(fig, use_container_width=True)

elif page == "💼 Experience":
    st.markdown('<p class="big-font">💼 Professional Experience</p>', unsafe_allow_html=True)
    
    # Experience using native Streamlit components
    with st.container():
        col1, col2 = st.columns([1, 4])
        
        with col1:
            st.markdown("### 🏢")
            st.markdown("#### 📅")
        
        with col2:
            st.subheader("Data Scientist")
            st.markdown("**Codenera Pvt Ltd**")
            st.markdown("📅 **Duration:** June 2024 – Present")
    
    st.markdown("---")
    
    # Role Description
    st.markdown("#### 📋 Role Description")
    st.write("Designed and deployed **end-to-end AI-driven solutions** for real-world use cases.")
    
    # Key Achievements
    st.markdown("#### 🏆 Key Achievements")
    
    achievements = [
        "🤖 Built an **AI-powered RAG-based Assignment Checker** for automated, context-aware evaluation and feedback",
        "🛠️ Worked extensively with **Python, Scikit-learn, TensorFlow, NLP, and LLMs**",
        "🚀 Developed and deployed multiple AI applications in production environment",
        "📊 Implemented advanced machine learning pipelines for business solutions"
    ]
    
    for achievement in achievements:
        st.write(f"• {achievement}")
    
    # Technologies Used
    st.markdown("#### 💡 Technologies Used")
    tech_used = ["Python", "TensorFlow", "Scikit-learn", "NLP", "LLMs", "RAG Systems", "Machine Learning"]
    
    cols = st.columns(len(tech_used))
    for i, tech in enumerate(tech_used):
        with cols[i]:
            st.button(tech, disabled=True, use_container_width=True, key=f"exp_tech_{i}")
    
    # Experience Timeline
    st.markdown("---")
    st.markdown("### 📅 Career Timeline")
    
    timeline_data = {
        'Date': ['June 2024', 'July 2024', 'August 2024', 'Present'],
        'Milestone': [
            'Started as Data Scientist',
            'First AI Project Deployed',
            'RAG System Implementation',
            'Continuing Innovation'
        ],
        'Impact': [85, 70, 95, 90]
    }
    
    fig = px.line(
        x=timeline_data['Date'],
        y=timeline_data['Impact'],
        markers=True,
        title="Career Impact Timeline",
        labels={'y': 'Impact Score', 'x': 'Timeline'}
    )
    fig.update_traces(line_color='#667eea', marker_size=10)
    fig.update_layout(title_font_size=20, title_x=0.5)
    st.plotly_chart(fig, use_container_width=True)


elif page == "🚀 Projects":
    st.markdown('<p class="big-font">🚀 Featured Projects</p>', unsafe_allow_html=True)
    
    # Project 1 - AI-powered SQL Assistant
    with st.container():
        st.markdown("---")
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            st.subheader("🤖 AI-powered SQL Assistant")
        with col2:
            st.markdown("**📅 July 2025 – Present**")
        with col3:
            st.link_button("🔗 GitHub", "https://github.com/Dbhosale146/RAG-SQL-", use_container_width=True)
        
        st.markdown("#### 🎯 Project Overview")
        st.write("Revolutionary SQL assistance tool that reduces query time by **70%** using natural language processing and real-time visualization.")
        
        st.markdown("#### 🌟 Key Features")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("🗣️ **Natural Language to SQL:** Convert English questions to SQL queries")
            st.write("🎤 **Voice Integration:** Voice-to-SQL conversion capabilities")
            st.write("🔍 **RAG Pipeline:** LangChain + LlamaIndex for contextual grounding")
        
        with col2:
            st.write("🌐 **Streamlit Interface:** User-friendly web application")
            st.write("📊 **Real-time Visualization:** Instant query results and charts")
        
        st.markdown("#### 🛠️ Technology Stack")
        tech_stack = ["Python", "LangChain", "LlamaIndex", "Streamlit", "NLP", "RAG Systems", "Voice Processing"]
        
        cols = st.columns(len(tech_stack))
        for i, tech in enumerate(tech_stack):
            with cols[i]:
                st.button(tech, disabled=True, use_container_width=True, key=f"sql_tech_{i}")
    
    # Project 2 - AgriTech Smart Farming Assistant
    with st.container():
        st.markdown("---")
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            st.subheader("🌾 AgriTech – Smart Farming Assistant System")
        with col2:
            st.markdown("**📅 June 2025 – July 2025**")
        with col3:
            st.link_button("🔗 GitHub", "https://github.com/Dbhosale146/AgriTech-", use_container_width=True)
        
        st.markdown("#### 🎯 Project Overview")
        st.write("AI-powered agricultural assistant (AgroBot) designed to guide farmers on crops, fertilizers, and irrigation practices.")
        
        st.markdown("#### 🌟 Key Features")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("🤖 **AgroBot Chatbot:** Intelligent farming guidance system")
            st.write("🌤️ **Weather Integration:** Real-time weather API for actionable advice")
            st.write("🌱 **Crop-Specific Modules:** Specialized advice for wheat, rice, grapes, and tomato")
        
        with col2:
            st.write("💧 **Irrigation Optimization:** Smart watering recommendations")
            st.write("🌿 **Fertilizer Guidance:** Optimal fertilization strategies")
        
        st.markdown("#### 🛠️ Technology Stack")
        agri_tech_stack = ["AI/ML", "Chatbot Development", "Weather APIs", "Agricultural Data Processing"]
        
        cols = st.columns(len(agri_tech_stack))
        for i, tech in enumerate(agri_tech_stack):
            with cols[i]:
                st.button(tech, disabled=True, use_container_width=True, key=f"agri_tech_{i}")
    
    # Project 3 - Spam Detection
    with st.container():
        st.markdown("---")
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            st.subheader("📧 Spam Detection System")
        with col2:
            st.markdown("**📅 Machine Learning Project**")
        with col3:
            st.link_button("🔗 GitHub", "https://github.com/Dbhosale146/ml-project", use_container_width=True)
        
        st.markdown("#### 🎯 Project Overview")
        st.write("Advanced spam detection system using machine learning algorithms to classify emails and messages as spam or legitimate.")
        
        st.markdown("#### 🌟 Key Features")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("📊 **Text Preprocessing:** Advanced NLP techniques for text cleaning")
            st.write("🤖 **ML Models:** Multiple algorithms for optimal performance")
            st.write("📈 **Feature Engineering:** TF-IDF and word embeddings")
        
        with col2:
            st.write("⚡ **Real-time Classification:** Instant spam detection")
            st.write("📋 **Model Evaluation:** Comprehensive performance metrics")
        
        st.markdown("#### 🛠️ Technology Stack")
        spam_tech_stack = ["Python", "Scikit-learn", "NLTK", "Pandas", "Machine Learning"]
        
        cols = st.columns(len(spam_tech_stack))
        for i, tech in enumerate(spam_tech_stack):
            with cols[i]:
                st.button(tech, disabled=True, use_container_width=True, key=f"spam_tech_{i}")
    
    # Project 4 - Medical Chatbot
    with st.container():
        st.markdown("---")
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            st.subheader("🏥 MediChat Pro - Medical Chatbot")
        with col2:
            st.markdown("**📅 AI Healthcare Project**")
        with col3:
            st.link_button("🔗 GitHub", "https://github.com/Dbhosale146/MediChat-Pro-", use_container_width=True)
        
        st.markdown("#### 🎯 Project Overview")
        st.write("Intelligent medical chatbot providing healthcare assistance, symptom analysis, and medical information to users.")
        
        st.markdown("#### 🌟 Key Features")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("🩺 **Symptom Analysis:** AI-powered symptom checker")
            st.write("💬 **Natural Conversation:** Human-like medical consultation")
            st.write("📚 **Medical Knowledge Base:** Comprehensive health information")
        
        with col2:
            st.write("🚨 **Emergency Detection:** Critical condition identification")
            st.write("💊 **Medicine Information:** Drug details and interactions")
        
        st.markdown("#### 🛠️ Technology Stack")
        medical_tech_stack = ["Python", "NLP", "Healthcare AI", "Chatbot", "Medical APIs"]
        
        cols = st.columns(len(medical_tech_stack))
        for i, tech in enumerate(medical_tech_stack):
            with cols[i]:
                st.button(tech, disabled=True, use_container_width=True, key=f"medical_tech_{i}")
    
    # Project 5 - License Plate Detection
    with st.container():
        st.markdown("---")
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            st.subheader("🚗 License Plate Detection System")
        with col2:
            st.markdown("**📅 Computer Vision Project**")
        with col3:
            st.link_button("🔗 GitHub", "https://github.com/Dbhosale146/license-plate-number-detection", use_container_width=True)
        
        st.markdown("#### 🎯 Project Overview")
        st.write("Advanced computer vision system for automatic license plate detection and recognition using deep learning techniques.")
        
        st.markdown("#### 🌟 Key Features")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("👁️ **Object Detection:** YOLO/CNN-based plate detection")
            st.write("🔍 **OCR Integration:** Text recognition from detected plates")
            st.write("📸 **Real-time Processing:** Live video feed analysis")
        
        with col2:
            st.write("📊 **High Accuracy:** Optimized detection algorithms")
            st.write("🚀 **Fast Processing:** Efficient inference pipeline")
        
        st.markdown("#### 🛠️ Technology Stack")
        plate_tech_stack = ["Python", "OpenCV", "YOLO", "OCR", "Deep Learning"]
        
        cols = st.columns(len(plate_tech_stack))
        for i, tech in enumerate(plate_tech_stack):
            with cols[i]:
                st.button(tech, disabled=True, use_container_width=True, key=f"plate_tech_{i}")
    
    # Project 6 - Housing Project
    with st.container():
        st.markdown("---")
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            st.subheader("🏠 Housing Price Prediction System")
        with col2:
            st.markdown("**📅 Data Science Project**")
        with col3:
            st.link_button("🔗 GitHub", "https://github.com/Dbhosale146/Housing_Project", use_container_width=True)
        
        st.markdown("#### 🎯 Project Overview")
        st.write("Machine learning model for predicting housing prices based on various features like location, size, amenities, and market trends.")
        
        st.markdown("#### 🌟 Key Features")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("📊 **Data Analysis:** Comprehensive housing market analysis")
            st.write("🤖 **ML Models:** Regression algorithms for price prediction")
            st.write("📈 **Feature Engineering:** Property characteristics optimization")
        
        with col2:
            st.write("🎯 **Accurate Predictions:** High-precision price estimates")
            st.write("📋 **Market Insights:** Housing trend analysis")
        
        st.markdown("#### 🛠️ Technology Stack")
        housing_tech_stack = ["Python", "Scikit-learn", "Pandas", "Data Analysis", "Regression"]
        
        cols = st.columns(len(housing_tech_stack))
        for i, tech in enumerate(housing_tech_stack):
            with cols[i]:
                st.button(tech, disabled=True, use_container_width=True, key=f"housing_tech_{i}")
    
    # Project 7 - Flight Price Prediction
    with st.container():
        st.markdown("---")
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            st.subheader("✈️ Flight Price Prediction System")
        with col2:
            st.markdown("**📅 Predictive Analytics**")
        with col3:
            st.link_button("🔗 GitHub", "https://github.com/Dbhosale146/Flight-Price-Prediction", use_container_width=True)
        
        st.markdown("#### 🎯 Project Overview")
        st.write("Intelligent flight price prediction system helping travelers find the best deals using historical data and machine learning algorithms.")
        
        st.markdown("#### 🌟 Key Features")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("📅 **Dynamic Pricing:** Real-time price trend analysis")
            st.write("🤖 **ML Algorithms:** Advanced prediction models")
            st.write("📊 **Historical Data:** Comprehensive flight price database")
        
        with col2:
            st.write("🎯 **Best Deal Finder:** Optimal booking time suggestions")
            st.write("📈 **Price Trends:** Future price movement predictions")
        
        st.markdown("#### 🛠️ Technology Stack")
        flight_tech_stack = ["Python", "Machine Learning", "Data Analytics", "Price Prediction", "Time Series"]
        
        cols = st.columns(len(flight_tech_stack))
        for i, tech in enumerate(flight_tech_stack):
            with cols[i]:
                st.button(tech, disabled=True, use_container_width=True, key=f"flight_tech_{i}")
    
    # Project Impact Chart
    st.markdown("---")
    st.markdown("### 📊 Project Portfolio Overview")
    
    project_metrics = {
        'Project': ['SQL Assistant', 'AgriTech', 'Spam Detection', 'Medical Chatbot', 'License Plate', 'Housing Price', 'Flight Price'],
        'Complexity': [90, 75, 70, 85, 80, 75, 70],
        'Impact': [95, 88, 82, 90, 85, 78, 75]
    }
    
    df = pd.DataFrame(project_metrics)
    
    fig = px.bar(
        df,
        x='Project',
        y=['Complexity', 'Impact'],
        title="Project Portfolio - Complexity vs Impact Analysis",
        barmode='group',
        color_discrete_sequence=['#667eea', '#764ba2']
    )
    fig.update_layout(title_font_size=20, title_x=0.5, xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)

elif page == "🎓 Education":
    st.markdown('<p class="big-font">🎓 Educational Background</p>', unsafe_allow_html=True)
    
    # Education Cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="education-card fade-in">
            <h3>🎓 Master of Science (M.Sc.)</h3>
            <h4>Mathematics</h4>
            <p><strong>🏫 Institution:</strong> Mumbai University</p>
            <p><strong>📅 Duration:</strong> 2020 – 2022</p>
            <p><strong>🎯 Focus:</strong> Advanced Mathematics, Statistics, Mathematical Modeling</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="education-card fade-in">
            <h3>🎓 Bachelor of Science (B.Sc.)</h3>
            <h4>Mathematics</h4>
            <p><strong>🏫 Institution:</strong> Karmaveer Bhaurao Patil College</p>
            <p><strong>📅 Duration:</strong> 2017 – 2020</p>
            <p><strong>🎯 Focus:</strong> Pure Mathematics, Applied Mathematics, Statistics</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Certifications
    st.markdown("### 🏆 Certifications & Achievements")
    
    st.markdown("""
    <div class="project-card fade-in">
        <h3>🎖️ Generative AI with NLP & Agentic AI</h3>
        <p><strong>🏢 Issuing Organization:</strong> EURON</p>
        <p><strong>📅 Year:</strong> 2025</p>
        <p><strong>📋 Skills Covered:</strong></p>
        <ul>
            <li>🧠 Advanced Generative AI techniques</li>
            <li>🗣️ Natural Language Processing (NLP)</li>
            <li>🤖 Agentic AI systems development</li>
            <li>🔗 Integration of AI agents in real-world applications</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Academic Progress Chart
    st.markdown("### 📈 Academic Journey")
    
    academic_data = {
        'Year': [2017, 2018, 2019, 2020, 2021, 2022, 2024, 2025],
        'Milestone': ['B.Sc. Started', 'Foundation', 'Specialization', 'B.Sc. Completed', 
                     'M.Sc. Progress', 'M.Sc. Completed', 'Industry Entry', 'AI Certification'],
        'Knowledge Level': [20, 35, 50, 65, 75, 85, 90, 95]
    }
    
    fig = px.line(
        x=academic_data['Year'],
        y=academic_data['Knowledge Level'],
        markers=True,
        title="Academic & Professional Growth",
        labels={'y': 'Knowledge Level (%)', 'x': 'Year'}
    )
    fig.update_traces(line_color='#f093fb', marker_size=8)
    fig.update_layout(title_font_size=20, title_x=0.5)
    st.plotly_chart(fig, use_container_width=True)

elif page == "📞 Contact":
    st.markdown('<p class="big-font">📞 Let\'s Connect!</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("#### 📧 Contact Information")
        st.write("**Email:** dnyaneshwarbhosale111@gmail.com")
        st.write("**Phone:** +91 9082063239")
        st.write("**Location:** India")
        
        st.markdown("#### 🔗 Professional Links")
        st.link_button("GitHub","https://github.com/Dbhosale146",use_container_width=True)
        st.link_button("LinkedIn","https://www.linkedin.com/in/dnyaneshwar-bhosale-99b441197/",use_container_width=True)
        
        st.markdown("#### 💼 Open For")
        opportunities = [
            "🚀 AI/ML Engineering Roles",
            "🤝 Collaboration on AI Projects", 
            "📊 Data Science Consulting",
            "🧠 GenAI & LLM Projects"
        ]
        
        for opportunity in opportunities:
            st.write(f"• {opportunity}")
    
    with col2:
        st.markdown("### 📝 Send a Message")
        
        # Contact Form
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            subject = st.selectbox("Subject", 
                ["General Inquiry", "Job Opportunity", "Project Collaboration", "Consulting"])
            message = st.text_area("Message", height=150)
            
            if st.form_submit_button("Send Message 🚀"):
                st.success("Thanks for reaching out! I'll get back to you soon. 😊")
                st.balloons()
        
        # Quick Contact Buttons
        st.markdown("### ⚡ Quick Contact")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📧 Email Me", use_container_width=True):
                st.info(" email : dnyaneshwarbhosale111@gmail.com")
        
        with col2:
            if st.button("📞 Call Me", use_container_width=True):
                st.info("Phone: +91 9082063239")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>Made with ❤️ using Streamlit | © 2025 Dnyaneshwar Bhosale</p>
    <p>🚀 "Building the future with AI, one algorithm at a time" 🚀</p>
</div>
""", unsafe_allow_html=True)