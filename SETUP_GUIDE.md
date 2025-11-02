# Quick Setup Guide

## Step-by-Step Instructions

### 1. Add Your Images

You need to add the following images to the `static/images/` folder:

**Required:**
- `profile.jpg` - Your professional photo (recommended size: 500x500px)
- `project1.jpg` - First project screenshot (recommended size: 800x600px)
- `project2.jpg` - Second project screenshot (recommended size: 800x600px)
- `project3.jpg` - Third project screenshot (recommended size: 800x600px)

**Note:** The hero illustration SVG is already included!

### 2. Update Your Personal Information

Open `templates/index.html` and find these sections to update:

#### Your Name & Title (Around line 80)
```javascript
const texts = ['Your Name', 'ML Engineer', 'AI Specialist', 'Data Scientist', 'Python Developer'];
```
Change 'Your Name' to your actual name.

#### Hero Section (Around line 60)
```html
<p class="hero-greeting">Hello, I'm</p>
```

#### Email & Contact Info (Search for "your.email@example.com")
- Replace with your actual email address (appears in multiple places)
- Update your location
- Update your education details

#### Social Media Links (Search for "linkedin.com", "github.com", etc.)
- Update LinkedIn URL
- Update GitHub URL
- Update Fiverr URL
- Update any other social media links

### 3. Customize Content

#### About Section
Update the description about yourself (around line 120-130)

#### Skills Section
Modify the skills and their percentages (around line 180-280)

#### Projects Section
- Add your project images
- Update project titles
- Update project descriptions
- Update technologies used
(around line 320-420)

#### Experience Section
Update your work experience and education (around line 450-530)

### 4. Install and Run

```powershell
# Navigate to project folder
cd "c:\Users\Rayyan Tech\OneDrive\Desktop\My website"

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### 5. View Your Website

Open your browser and go to: `http://localhost:5000`

### 6. Make It Your Own

#### Change Colors
Edit `static/css/style.css` (lines 1-20) to change the color scheme:
```css
:root {
    --primary-color: #6366f1;    /* Main color */
    --secondary-color: #8b5cf6;  /* Secondary color */
    --accent-color: #ec4899;     /* Accent color */
}
```

#### Add More Projects
Copy a project card in `index.html` and paste it to add more projects.

#### Update Skills
Add or remove skill categories and individual skills in the Skills section.

### 7. Testing

- Test on mobile view (resize browser or use DevTools)
- Test all navigation links
- Test the contact form
- Check that all animations work smoothly

### 8. Deploy (Optional)

Once everything looks good locally, you can deploy to:
- **Heroku** (Free tier available)
- **PythonAnywhere** (Free tier available)
- **Vercel/Netlify** (For static hosting)
- **AWS/Azure/GCP** (Production-grade)

See the main README.md for deployment instructions.

## Common Issues

### Issue: Virtual Environment Won't Activate
**Solution:** Run this first:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Issue: Flask Not Found
**Solution:** Make sure you activated the virtual environment and ran:
```powershell
pip install -r requirements.txt
```

### Issue: Images Not Showing
**Solution:** 
1. Check that images are in `static/images/` folder
2. Check that filenames match exactly (case-sensitive)
3. Clear browser cache (Ctrl+F5)

### Issue: Styles Not Loading
**Solution:**
1. Make sure CSS file is in `static/css/style.css`
2. Hard refresh browser (Ctrl+F5)
3. Check browser console for errors (F12)

## Checklist Before Going Live

- [ ] Updated all personal information
- [ ] Added all images
- [ ] Updated social media links
- [ ] Tested on mobile devices
- [ ] Tested contact form
- [ ] Changed SECRET_KEY in app.py
- [ ] Set DEBUG=False in app.py
- [ ] Updated meta tags for SEO
- [ ] Tested all navigation links
- [ ] Proofread all text content

## Need Help?

Review the main README.md file for detailed documentation on each section.

---

**Your portfolio is ready to showcase your ML & AI expertise! 🚀**
