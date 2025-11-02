# Deployment Guide for Portfolio Website

## 🚀 GitHub Repository Setup

Your repository is now ready! Follow these steps to push to GitHub:

### Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com)
2. Click the **"+"** icon (top right) → **"New repository"**
3. Repository name: **Portfolio**
4. Description: *Professional AI/ML Portfolio - Muhammad Daiym Mughal*
5. Keep it **Public** (so it can be deployed for free)
6. **DO NOT** initialize with README (we already have one)
7. Click **"Create repository"**

### Step 2: Push to GitHub

After creating the repository, run these commands in your terminal:

```powershell
cd "c:\Users\Rayyan Tech\OneDrive\Desktop\My website"
git remote add origin https://github.com/DaiymMughal/Portfolio.git
git push -u origin main
```

**Note:** You'll be asked to authenticate. Use your GitHub username and a **Personal Access Token** (not password).

#### Creating a Personal Access Token:
1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Give it a name: "Portfolio Deployment"
4. Select scopes: ✅ **repo** (all repo permissions)
5. Click **"Generate token"**
6. **Copy the token** (you won't see it again!)
7. Use this token as your password when pushing

---

## 🌐 Deployment Options

### Option 1: Render (Recommended - Free & Easy)

**Best for Flask apps. Free tier available.**

1. Go to [Render](https://render.com)
2. Sign up/Login with GitHub
3. Click **"New +"** → **"Web Service"**
4. Connect your **Portfolio** repository
5. Configure:
   - **Name:** `portfolio-daiym` (or any unique name)
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Instance Type:** Free
6. Add environment variable:
   - Key: `PYTHON_VERSION`
   - Value: `3.13.5`
7. Click **"Create Web Service"**

**Important:** Add gunicorn to requirements.txt first:
```powershell
echo "gunicorn==21.2.0" >> requirements.txt
git add requirements.txt
git commit -m "Add gunicorn for deployment"
git push
```

Your site will be live at: `https://portfolio-daiym.onrender.com`

---

### Option 2: PythonAnywhere (Free Python Hosting)

1. Go to [PythonAnywhere](https://www.pythonanywhere.com)
2. Create a free account
3. Go to **"Web"** tab → **"Add a new web app"**
4. Choose **"Manual configuration"** → **"Python 3.10"**
5. In the **"Code"** section:
   - Source code: `/home/yourusername/Portfolio`
   - Working directory: `/home/yourusername/Portfolio`
6. Open a **Bash console** and run:
   ```bash
   git clone https://github.com/DaiymMughal/Portfolio.git
   cd Portfolio
   pip install --user -r requirements.txt
   ```
7. In **"Web"** tab, edit WSGI file:
   ```python
   import sys
   path = '/home/yourusername/Portfolio'
   if path not in sys.path:
       sys.path.append(path)
   
   from app import app as application
   ```
8. Click **"Reload"**

Your site will be at: `https://yourusername.pythonanywhere.com`

---

### Option 3: Railway (Modern & Simple)

1. Go to [Railway](https://railway.app)
2. Sign up with GitHub
3. Click **"New Project"** → **"Deploy from GitHub repo"**
4. Select **Portfolio** repository
5. Railway auto-detects Python and deploys!

Add a `Procfile` first:
```powershell
echo "web: gunicorn app:app" > Procfile
git add Procfile
git commit -m "Add Procfile for Railway"
git push
```

---

### Option 4: Vercel (For Static + API)

**Note:** Vercel works best with serverless functions. Requires slight modification.

1. Go to [Vercel](https://vercel.com)
2. Sign up with GitHub
3. Click **"Import Project"**
4. Select **Portfolio** repository
5. Framework: **Other**
6. Deploy!

Create `vercel.json`:
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

---

## 📋 Pre-Deployment Checklist

Before deploying, make sure:

- [x] Git repository initialized
- [x] All files committed
- [ ] GitHub repository created
- [ ] Code pushed to GitHub
- [ ] Gunicorn added to requirements.txt (for Render/Railway)
- [ ] SECRET_KEY changed in app.py (for security)
- [ ] DEBUG set to False in production
- [ ] Environment variables configured (if needed)

---

## 🔒 Security Best Practices

### Update app.py for production:

```python
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback-secret-key-change-this')

# For production
if os.environ.get('PRODUCTION'):
    app.config['DEBUG'] = False
else:
    app.config['DEBUG'] = True
```

---

## 🎯 Custom Domain (Optional)

Once deployed, you can add a custom domain:

1. Buy a domain (Namecheap, GoDaddy, etc.)
2. In your hosting platform, go to Settings → Custom Domains
3. Add your domain: `www.daiym.com` or `daiym.dev`
4. Update DNS records as instructed
5. Wait 24-48 hours for DNS propagation

---

## 🔄 Updating Your Live Site

After making changes locally:

```powershell
cd "c:\Users\Rayyan Tech\OneDrive\Desktop\My website"
git add .
git commit -m "Description of changes"
git push
```

Most platforms auto-deploy when you push to GitHub!

---

## 📞 Need Help?

- **Render Issues:** [Render Docs](https://render.com/docs)
- **PythonAnywhere:** [PythonAnywhere Help](https://help.pythonanywhere.com)
- **Railway:** [Railway Docs](https://docs.railway.app)
- **Vercel:** [Vercel Docs](https://vercel.com/docs)

---

## 🎉 Your Portfolio URLs

Once deployed, update these in your CV and profiles:

- **GitHub Repo:** `https://github.com/DaiymMughal/Portfolio`
- **Live Site:** `https://your-app-name.platform.com` (after deployment)

---

**Good luck with your deployment! 🚀**

*Last updated: November 3, 2025*
