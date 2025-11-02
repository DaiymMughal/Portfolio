# Image Guidelines for Your Portfolio

## Required Images

You need to add the following images to make your portfolio complete:

### 1. Profile Photo (`profile.jpg`)
**Location:** `static/images/profile.jpg`

**Recommendations:**
- Professional headshot
- Clear, well-lit photo
- Neutral or professional background
- Size: 500x500px (square)
- Format: JPG or PNG
- File size: Under 500KB

**Tips:**
- Smile and look approachable
- Dress professionally
- Good lighting is crucial
- Use a high-resolution camera/phone

---

### 2. Project Screenshots

#### Project 1 (`project1.jpg`)
**Location:** `static/images/project1.jpg`

**Recommendations:**
- Screenshot or mockup of your ML/AI project
- Size: 800x600px (or 16:9 aspect ratio)
- Format: JPG or PNG
- Show the interface or results

**Ideas:**
- Dashboard screenshot
- Model performance graphs
- Application interface
- Before/after comparison

---

#### Project 2 (`project2.jpg`)
**Location:** `static/images/project2.jpg`

**Same requirements as Project 1**

**Alternative Ideas:**
- Code editor with your project
- Jupyter notebook with visualizations
- API documentation page
- Mobile app screens

---

#### Project 3 (`project3.jpg`)
**Location:** `static/images/project3.jpg`

**Same requirements as Project 1 & 2**

---

## Where to Get Images If You Don't Have Them

### For Profile Photo:
1. **Take a new photo** with good lighting
2. **Use a professional photo service** (affordable options available)
3. **AI Generated**: Use tools like [PhotoRoom](https://www.photoroom.com/) for background removal
4. **Edit existing photo**: Use Canva or Photoshop to improve

### For Project Images:
1. **Screenshots**: Capture your actual work
2. **Mockups**: Use Figma, Canva, or Adobe XD
3. **Placeholder Services** (temporary):
   - [Unsplash](https://unsplash.com) - Free tech/code images
   - [Pexels](https://www.pexels.com) - Free stock photos
   - [Lorem Picsum](https://picsum.photos/) - Placeholder images
4. **Create Graphics**: Use Canva to design project covers

---

## Already Included

✅ **Hero Illustration** (`hero-illustration.svg`) - Already created for you!
- Located at: `static/images/hero-illustration.svg`
- Professional coding/AI themed illustration
- No need to replace unless you want to

---

## How to Add Images

### Method 1: Direct Copy
1. Copy your image files
2. Navigate to: `c:\Users\Rayyan Tech\OneDrive\Desktop\My website\static\images\`
3. Paste the files
4. Ensure filenames match exactly:
   - `profile.jpg`
   - `project1.jpg`
   - `project2.jpg`
   - `project3.jpg`

### Method 2: Drag and Drop (in VS Code)
1. Open the project in VS Code
2. Open the `static/images` folder in the sidebar
3. Drag and drop your images into the folder
4. Rename them to match the required names

---

## Image Optimization Tips

### Before Adding Images:

1. **Resize**: Use these tools to resize:
   - [TinyPNG](https://tinypng.com/) - Compress PNG/JPG
   - [Squoosh](https://squoosh.app/) - Google's image optimizer
   - [ImageOptim](https://imageoptim.com/) - Mac app
   - [GIMP](https://www.gimp.org/) - Free editor for resizing

2. **Compress**: Reduce file size without losing quality
   - Target: Under 500KB for profile
   - Target: Under 800KB for projects

3. **Format**:
   - Use JPG for photos
   - Use PNG for images with transparency
   - Use WebP for best compression (modern browsers)

---

## Quick Start Without Your Own Images

### Option 1: Use Placeholders Temporarily
You can use placeholder services:

```html
<!-- Replace the img src in index.html temporarily -->
<img src="https://picsum.photos/500/500" alt="Profile">
<img src="https://picsum.photos/800/600" alt="Project 1">
```

### Option 2: Download Free Stock Images
Visit [Unsplash](https://unsplash.com) and search for:
- "professional portrait" (for profile)
- "coding" or "technology" (for projects)
- "data visualization" (for data science projects)

### Option 3: Use AI-Generated Images
Tools like:
- [DALL-E](https://openai.com/dall-e-2)
- [Midjourney](https://www.midjourney.com)
- [Stable Diffusion](https://stablediffusion.com)

---

## Example Prompts for AI Image Generation

### For Profile (if using AI):
"Professional headshot of a data scientist, neutral background, friendly smile, business casual, high quality, studio lighting"

### For Projects (if using AI):
- "Modern machine learning dashboard with graphs and data visualizations"
- "Futuristic AI neural network interface with glowing connections"
- "Data analysis application screenshot with charts and metrics"

---

## Testing Your Images

After adding images:

1. **Run your website**
   ```powershell
   python app.py
   ```

2. **Check each section**:
   - Hero section (illustration should show)
   - About section (profile photo should show)
   - Projects section (all 3 project images should show)

3. **Test on mobile view**:
   - Press F12 in browser
   - Click mobile icon
   - Check if images look good on small screens

---

## Image Checklist

Before considering your portfolio complete:

- [ ] Profile photo added (`profile.jpg`)
- [ ] Project 1 image added (`project1.jpg`)
- [ ] Project 2 image added (`project2.jpg`)
- [ ] Project 3 image added (`project3.jpg`)
- [ ] All images are optimized (reasonable file size)
- [ ] Images look good on desktop view
- [ ] Images look good on mobile view
- [ ] Hero illustration is showing correctly
- [ ] No broken image icons anywhere

---

## Advanced: Adding More Images

If you want to add more projects or images:

1. **Add the image** to `static/images/` folder
2. **Name it appropriately** (e.g., `project4.jpg`)
3. **Update `index.html`** to include it:
   ```html
   <img src="{{ url_for('static', filename='images/project4.jpg') }}" alt="Project 4">
   ```

---

## Need Help?

If images aren't showing:
1. Check filename spelling (case-sensitive!)
2. Check file location (must be in `static/images/`)
3. Clear browser cache (Ctrl + F5)
4. Check browser console for errors (F12)

---

**Remember:** Professional images make a huge difference in how your portfolio is perceived!

Take your time to get good quality images - it's worth it! 📸
