# Professional Portfolio Website

A modern, responsive portfolio website built with Flask and Python, featuring stunning animations, interactive elements, and a professional design perfect for showcasing your ML & AI expertise on platforms like Fiverr, LinkedIn, and more.

## 🌟 Features

- **Modern Design**: Beautiful gradient themes and smooth animations
- **Fully Responsive**: Works perfectly on all devices (mobile, tablet, desktop)
- **Interactive Elements**: 
  - Particle.js animated background
  - Smooth scroll effects
  - Typing animation
  - Skill progress bars with animation
  - 3D card tilt effects
  - Parallax scrolling
- **Sections**:
  - Hero section with animated text
  - About Me with profile information
  - Skills & Technologies with progress indicators
  - Featured Projects showcase
  - Experience & Education timeline
  - Contact form with validation
- **SEO Optimized**: Meta tags and semantic HTML
- **Fast Loading**: Optimized assets and lazy loading

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project**
   
2. **Navigate to the project directory**
   ```powershell
   cd "c:\Users\Rayyan Tech\OneDrive\Desktop\My website"
   ```

3. **Create a virtual environment (recommended)**
   ```powershell
   python -m venv venv
   ```

4. **Activate the virtual environment**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   
   If you get an execution policy error, run:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

5. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the Flask server**
   ```powershell
   python app.py
   ```

2. **Open your browser and visit**
   ```
   http://localhost:5000
   ```

## 📁 Project Structure

```
My website/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
│
├── templates/
│   └── index.html        # Main HTML template
│
├── static/
│   ├── css/
│   │   └── style.css     # Main stylesheet with animations
│   │
│   ├── js/
│   │   └── script.js     # JavaScript interactions
│   │
│   └── images/           # Image assets folder
│       ├── profile.jpg   # Your profile photo
│       ├── hero-illustration.svg
│       ├── project1.jpg
│       ├── project2.jpg
│       └── project3.jpg
```

## 🎨 Customization

### 1. Personal Information

Edit `templates/index.html` and update:
- Your name in the typing animation (line ~80)
- Email addresses
- Location
- Education details
- Social media links (LinkedIn, GitHub, Fiverr, etc.)

### 2. Profile Photo

Add your profile photo to `static/images/profile.jpg`

### 3. Projects

Update the projects section in `templates/index.html`:
- Add project images to `static/images/`
- Update project titles, descriptions, and technologies

### 4. Skills

Modify the skills section to match your expertise:
- Update skill names
- Adjust progress percentages
- Add or remove skill categories

### 5. Experience & Education

Update the timeline section with your:
- Work experience
- Education background
- Certifications
- Internships

### 6. Color Scheme

Edit `static/css/style.css` CSS variables (lines 1-20):
```css
:root {
    --primary-color: #6366f1;    /* Change primary color */
    --secondary-color: #8b5cf6;  /* Change secondary color */
    --accent-color: #ec4899;     /* Change accent color */
    /* ... more colors */
}
```

### 7. Contact Form

The contact form currently returns a success message. To implement email functionality:
1. Update the `/contact` route in `app.py`
2. Configure SMTP settings for email sending
3. Or integrate with services like SendGrid, Mailgun, etc.

## 🖼️ Adding Images

### Required Images:
1. **profile.jpg** - Your professional headshot (recommended: 500x500px)
2. **hero-illustration.svg** - Hero section illustration (or use PNG/JPG)
3. **project1.jpg, project2.jpg, project3.jpg** - Project screenshots (recommended: 800x600px)

Place all images in the `static/images/` directory.

## 🌐 Deployment

### Deploying to Production

1. **Set DEBUG to False** in `app.py`
2. **Update SECRET_KEY** with a secure random key
3. **Choose a hosting platform**:
   - **Heroku**: Easy deployment with Git
   - **PythonAnywhere**: Free tier available
   - **AWS/Azure/GCP**: Scalable options
   - **DigitalOcean**: VPS hosting

### Example: Deploying to Heroku

1. Create a `Procfile`:
   ```
   web: gunicorn app:app
   ```

2. Add gunicorn to requirements.txt:
   ```
   gunicorn==21.2.0
   ```

3. Deploy:
   ```bash
   git init
   heroku create your-portfolio-name
   git add .
   git commit -m "Initial commit"
   git push heroku master
   ```

## 📱 Responsive Design

The website is fully responsive with breakpoints for:
- Mobile devices (< 480px)
- Tablets (480px - 768px)
- Desktop (768px - 992px)
- Large screens (> 992px)

## 🎯 SEO Tips

1. Update meta tags in `index.html` with your information
2. Add descriptive alt text to all images
3. Create a `sitemap.xml`
4. Add Google Analytics tracking code
5. Submit to Google Search Console

## 🔧 Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Animations**: AOS (Animate On Scroll)
- **Particles**: Particles.js
- **Icons**: Font Awesome 6
- **Fonts**: Google Fonts (Poppins, Playfair Display)

## 📝 License

This project is free to use for personal and commercial purposes. Feel free to customize it according to your needs.

## 🤝 Support

If you need help customizing the website:
1. Review the code comments
2. Check the structure documentation above
3. Modify one section at a time
4. Test changes in your browser

## 🎓 Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [CSS Grid Guide](https://css-tricks.com/snippets/css/complete-guide-grid/)
- [JavaScript ES6 Features](https://www.w3schools.com/js/js_es6.asp)

## 📞 Contact Form Setup (Optional)

To enable email functionality in the contact form:

```python
# Add to app.py
import os
from flask_mail import Mail, Message

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')

mail = Mail(app)
```

## 🚀 Performance Tips

1. Compress images before uploading
2. Use WebP format for better compression
3. Enable browser caching
4. Minify CSS and JavaScript for production
5. Use a CDN for static assets

---

**Built with ❤️ using Flask and modern web technologies**

*Last updated: November 2025*
