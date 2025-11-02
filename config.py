# Configuration file for easy customization
# Update these values and they can be imported in your Flask app

# Personal Information
PERSONAL_INFO = {
    'name': 'Your Name',
    'title': 'ML & AI Specialist',
    'email': 'your.email@example.com',
    'location': 'Your City, Country',
    'phone': '+1234567890',
    'website': 'www.yourwebsite.com',
}

# Social Media Links
SOCIAL_LINKS = {
    'linkedin': 'https://linkedin.com/in/yourprofile',
    'github': 'https://github.com/yourusername',
    'fiverr': 'https://fiverr.com/yourusername',
    'twitter': 'https://twitter.com/yourusername',
    'email': 'mailto:your.email@example.com',
}

# About Section
ABOUT_TEXT = """
I am a passionate Machine Learning and Artificial Intelligence professional with extensive experience 
in developing innovative solutions using cutting-edge technologies. My expertise lies in creating 
intelligent systems that can learn, adapt, and make data-driven decisions.
"""

# Skills Configuration
SKILLS = {
    'Machine Learning': [
        {'name': 'TensorFlow', 'level': 90},
        {'name': 'PyTorch', 'level': 85},
        {'name': 'Scikit-learn', 'level': 95},
    ],
    'Programming': [
        {'name': 'Python', 'level': 95},
        {'name': 'SQL', 'level': 80},
        {'name': 'JavaScript', 'level': 75},
    ],
    'Data Science': [
        {'name': 'Pandas', 'level': 90},
        {'name': 'NumPy', 'level': 90},
        {'name': 'Matplotlib/Seaborn', 'level': 85},
    ],
    'Deep Learning': [
        {'name': 'Computer Vision', 'level': 85},
        {'name': 'NLP', 'level': 80},
        {'name': 'Neural Networks', 'level': 90},
    ],
}

# Projects
PROJECTS = [
    {
        'title': 'Image Classification System',
        'description': 'Advanced CNN-based image classification system with 95% accuracy.',
        'tags': ['Computer Vision', 'Deep Learning'],
        'technologies': ['Python', 'TensorFlow', 'AWS'],
        'image': 'project1.jpg',
        'link': '#',
    },
    {
        'title': 'Sentiment Analysis Tool',
        'description': 'Real-time sentiment analysis application for social media data.',
        'tags': ['NLP', 'Sentiment Analysis'],
        'technologies': ['Python', 'PyTorch', 'BERT'],
        'image': 'project2.jpg',
        'link': '#',
    },
    {
        'title': 'Predictive Analytics Dashboard',
        'description': 'Interactive dashboard for business intelligence with ML predictions.',
        'tags': ['Predictive Analytics', 'ML'],
        'technologies': ['Python', 'Plotly', 'PostgreSQL'],
        'image': 'project3.jpg',
        'link': '#',
    },
]

# Experience Timeline
EXPERIENCE = [
    {
        'type': 'work',  # 'work', 'education', or 'certification'
        'title': 'ML & AI Intern',
        'organization': 'Tech Company',
        'date': '2024 - Present',
        'description': 'Working on cutting-edge machine learning projects and AI solutions.',
    },
    {
        'type': 'work',
        'title': 'Python Developer',
        'organization': 'Software Solutions Inc.',
        'date': '2023 - 2024',
        'description': 'Developed Python-based applications and data pipelines.',
    },
    {
        'type': 'education',
        'title': "Bachelor's Degree",
        'organization': 'University Name',
        'date': '2020 - 2024',
        'description': 'Specialized in Computer Science with focus on AI and Machine Learning.',
    },
    {
        'type': 'certification',
        'title': 'Professional Certifications',
        'organization': 'Various Platforms',
        'date': '2023',
        'description': 'ML Specialization, Deep Learning, Python for Data Science, AWS.',
    },
]

# Email Configuration (for contact form)
EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'use_tls': True,
    'sender_email': 'your.email@example.com',
    'sender_password': 'your-app-password',  # Use app password, not regular password
}

# Site Configuration
SITE_CONFIG = {
    'title': 'Portfolio - ML & AI Professional',
    'description': 'Professional Portfolio showcasing ML & AI expertise',
    'keywords': 'machine learning, artificial intelligence, data science, python, portfolio',
    'author': 'Your Name',
    'og_image': 'static/images/og-image.jpg',  # For social media sharing
}
