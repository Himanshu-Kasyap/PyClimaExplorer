# 🚀 Deploy PyClimaExplorer to Streamlit Community Cloud

## Why Streamlit Cloud?

✅ **FREE** hosting for public apps  
✅ **Purpose-built** for Streamlit  
✅ **One-click** deployment  
✅ **Auto-updates** from GitHub  
✅ **No configuration** needed  
✅ **Custom domains** supported  

## Step-by-Step Deployment

### Step 1: Prepare Your Repository

1. **Create a GitHub account** (if you don't have one)
   - Go to https://github.com
   - Sign up for free

2. **Create a new repository**
   - Click "New repository"
   - Name: `pyclima-explorer`
   - Make it Public (required for free tier)
   - Don't initialize with README (we have files)

3. **Push your code to GitHub**

   ```bash
   # Initialize git (if not already done)
   git init
   
   # Add all files
   git add .
   
   # Commit
   git commit -m "Initial commit - PyClimaExplorer"
   
   # Add remote (replace YOUR_USERNAME)
   git remote add origin https://github.com/YOUR_USERNAME/pyclima-explorer.git
   
   # Push to GitHub
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy to Streamlit Cloud

1. **Go to Streamlit Cloud**
   - Visit: https://share.streamlit.io
   - Click "Sign up" or "Sign in with GitHub"

2. **Authorize GitHub**
   - Allow Streamlit to access your repositories

3. **Create New App**
   - Click "New app" button
   - Select your repository: `pyclima-explorer`
   - Branch: `main`
   - Main file path: `app.py`
   - Click "Deploy!"

4. **Wait for Deployment** (2-3 minutes)
   - Streamlit will install dependencies
   - Build the app
   - Launch it

5. **Your App is Live!**
   - You'll get a URL like: `https://your-app-name.streamlit.app`
   - Share this URL with anyone!

### Step 3: Configure (Optional)

1. **Custom Domain**
   - Go to app settings
   - Add your custom domain
   - Update DNS records

2. **Secrets Management**
   - If you need API keys
   - Go to app settings → Secrets
   - Add secrets in TOML format

3. **Resource Limits**
   - Free tier: 1 GB RAM, 1 CPU
   - Upgrade if needed for larger datasets

## Important Notes

### File Size Considerations

⚠️ **GitHub has a 100MB file limit**

If your sample data file is large:

**Option A: Use .gitignore**
```bash
# Add to .gitignore
sample_climate_data.nc
*.nc
```

Then users generate their own sample data after deployment.

**Option B: Use Git LFS**
```bash
# Install Git LFS
git lfs install

# Track large files
git lfs track "*.nc"
git add .gitattributes
git commit -m "Add Git LFS"
```

**Option C: Host data separately**
- Upload to cloud storage (AWS S3, Google Cloud Storage)
- Download in app on first run

### Recommended .gitignore for Deployment

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/

# Data files (users will generate)
sample_climate_data.nc
*.nc
data/

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Streamlit
.streamlit/secrets.toml
```

## Troubleshooting

### Issue: "Requirements installation failed"

**Solution**: Ensure `requirements.txt` has correct versions
```txt
streamlit==1.31.0
xarray==2024.1.1
pandas==2.2.0
numpy==1.26.3
plotly==5.18.0
netCDF4==1.6.5
scikit-learn==1.4.0
```

### Issue: "App crashes on startup"

**Solution**: Check logs in Streamlit Cloud dashboard
- Look for import errors
- Verify all dependencies installed
- Check Python version compatibility

### Issue: "Out of memory"

**Solution**: 
- Reduce dataset size
- Use data chunking
- Upgrade to paid tier (more RAM)

### Issue: "App is slow"

**Solution**:
- Add `@st.cache_data` decorators
- Optimize data loading
- Use smaller time ranges by default

## Auto-Updates

Every time you push to GitHub:
```bash
git add .
git commit -m "Update feature"
git push
```

Streamlit Cloud will automatically redeploy! 🎉

## Monitoring

- **View logs**: Streamlit Cloud dashboard
- **Check usage**: App analytics
- **Monitor uptime**: Built-in monitoring

## Sharing Your App

Once deployed, share your URL:
```
https://pyclima-explorer.streamlit.app
```

Or create a custom domain:
```
https://climate.yourdomain.com
```

## Cost

- **Free tier**: 
  - 1 GB RAM
  - 1 CPU core
  - Unlimited public apps
  - Community support

- **Paid tier** ($20/month):
  - More resources
  - Private apps
  - Priority support
  - Custom domains

## Example Deployment

Here's what your deployed app will look like:

**URL**: `https://pyclima-explorer.streamlit.app`

**Features**:
- ✅ Full functionality
- ✅ Fast loading
- ✅ Global access
- ✅ Auto-updates
- ✅ HTTPS secure

## Next Steps After Deployment

1. **Test the deployed app**
   - Upload sample data
   - Try all features
   - Check performance

2. **Share with users**
   - Post on social media
   - Add to portfolio
   - Submit to hackathon

3. **Monitor usage**
   - Check analytics
   - Read user feedback
   - Fix issues

4. **Iterate**
   - Push updates to GitHub
   - Auto-deploys to Streamlit Cloud

## Additional Resources

- **Streamlit Cloud Docs**: https://docs.streamlit.io/streamlit-community-cloud
- **GitHub Guide**: https://docs.github.com/en/get-started
- **Git LFS**: https://git-lfs.github.com

---

**Your app will be live in minutes! 🚀🌍**
