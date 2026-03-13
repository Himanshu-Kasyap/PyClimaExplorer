# 🔧 Streamlit Cloud Deployment Troubleshooting

## ✅ SOLUTION: NetCDF4 Installation Error

### The Problem
```
ValueError: did not find HDF5 headers
× Failed to download and build `netcdf4==1.6.5`
```

### The Fix (ALREADY APPLIED)

I've created a `packages.txt` file that tells Streamlit Cloud to install system dependencies:

**packages.txt:**
```
libhdf5-dev
libnetcdf-dev
```

This file must be in your repository root alongside `requirements.txt`.

### What to Do Now

1. **Commit the new files:**
   ```bash
   git add packages.txt requirements.txt
   git commit -m "Fix netCDF4 installation for Streamlit Cloud"
   git push origin main
   ```

2. **Streamlit Cloud will auto-redeploy** (wait 2-3 minutes)

3. **Check the logs** - you should see:
   ```
   Installing system packages from packages.txt...
   ✓ libhdf5-dev installed
   ✓ libnetcdf-dev installed
   ```

4. **Your app should now deploy successfully!** 🎉

---

## Common Streamlit Cloud Issues

### Issue 1: NetCDF4 Build Failure ✅ FIXED

**Error:**
```
ValueError: did not find HDF5 headers
```

**Solution:**
Create `packages.txt` with:
```
libhdf5-dev
libnetcdf-dev
```

**Status:** ✅ Already fixed in your project

---

### Issue 2: Memory Limit Exceeded

**Error:**
```
Your app has exceeded the memory limit
```

**Solutions:**

1. **Reduce dataset size in sample data generator:**
   ```python
   # In test_sample_data.py, change resolution
   lat = np.arange(-90, 91, 10)  # Changed from 5 to 10
   lon = np.arange(-180, 180, 10)  # Changed from 5 to 10
   ```

2. **Add caching to app.py:**
   ```python
   @st.cache_data
   def load_netcdf(uploaded_file):
       # ... existing code
   ```

3. **Limit time range by default:**
   ```python
   # In app.py, set smaller default range
   time_slider = st.slider(
       "Select Time Period",
       min_value=0,
       max_value=len(time_range) - 1,
       value=(0, min(len(time_range) - 1, 24)),  # Changed from 50 to 24
   )
   ```

---

### Issue 3: App Keeps Restarting

**Error:**
```
App is restarting...
```

**Solutions:**

1. **Check for infinite loops** in your code
2. **Verify session state usage** is correct
3. **Check logs** for error messages
4. **Reduce resource usage** (see Issue 2)

---

### Issue 4: Module Not Found

**Error:**
```
ModuleNotFoundError: No module named 'xxx'
```

**Solution:**
Ensure all dependencies are in `requirements.txt`:
```bash
# Check what's imported in your code
grep -r "^import\|^from" *.py utils/*.py

# Add missing packages to requirements.txt
```

---

### Issue 5: File Upload Size Limit

**Error:**
```
File size exceeds maximum allowed size
```

**Solution:**
Update `.streamlit/config.toml`:
```toml
[server]
maxUploadSize = 500
```

**Note:** Streamlit Cloud free tier has a 200MB limit. For larger files:
- Preprocess data to reduce size
- Use data chunking
- Upgrade to paid tier

---

### Issue 6: Slow Performance

**Symptoms:**
- App takes long to load
- Visualizations are slow
- Timeouts

**Solutions:**

1. **Add caching:**
   ```python
   @st.cache_data
   def load_netcdf(uploaded_file):
       # ... code
   
   @st.cache_data
   def create_heatmap(data_array, variable_name):
       # ... code
   ```

2. **Optimize data loading:**
   ```python
   # Use lazy loading
   ds = xr.open_dataset(tmp_path, chunks={'time': 10})
   ```

3. **Reduce default time range** (see Issue 2)

---

### Issue 7: GitHub File Size Limit

**Error:**
```
remote: error: File sample_climate_data.nc is 123.45 MB; this exceeds GitHub's file size limit of 100.00 MB
```

**Solution:**

**Option A: Don't commit data files (RECOMMENDED)**
```bash
# Add to .gitignore
echo "*.nc" >> .gitignore
echo "sample_climate_data.nc" >> .gitignore
git rm --cached sample_climate_data.nc
git commit -m "Remove large data files"
git push
```

Users will generate their own sample data using `test_sample_data.py`

**Option B: Use Git LFS**
```bash
git lfs install
git lfs track "*.nc"
git add .gitattributes
git add sample_climate_data.nc
git commit -m "Add large files with LFS"
git push
```

**Option C: Host data externally**
- Upload to Google Drive, Dropbox, or AWS S3
- Download in app on first run

---

### Issue 8: Python Version Mismatch

**Error:**
```
Python version 3.14.3 is not supported
```

**Solution:**
Create `.python-version` file:
```
3.9
```

Or specify in `runtime.txt`:
```
python-3.9
```

---

### Issue 9: Secrets Not Working

**Error:**
```
KeyError: 'API_KEY'
```

**Solution:**

1. Go to Streamlit Cloud dashboard
2. Click on your app → Settings → Secrets
3. Add secrets in TOML format:
   ```toml
   API_KEY = "your-key-here"
   DATABASE_URL = "your-url-here"
   ```

4. Access in code:
   ```python
   import streamlit as st
   api_key = st.secrets["API_KEY"]
   ```

---

### Issue 10: Custom Domain Not Working

**Error:**
```
Domain not resolving
```

**Solution:**

1. **Add CNAME record** in your DNS:
   ```
   Type: CNAME
   Name: climate (or @)
   Value: your-app.streamlit.app
   ```

2. **Wait for DNS propagation** (up to 48 hours)

3. **Verify in Streamlit Cloud:**
   - App Settings → Custom Domain
   - Add your domain
   - Follow verification steps

---

## Debugging Tips

### 1. Check Logs
- Go to Streamlit Cloud dashboard
- Click "Manage app" → "Logs"
- Look for error messages

### 2. Test Locally First
```bash
streamlit run app.py
```
If it works locally but not on Streamlit Cloud, it's likely a dependency or environment issue.

### 3. Simplify to Debug
Comment out sections of code to isolate the problem:
```python
# Temporarily disable features
# if st.session_state.dataset is not None:
#     # ... visualization code
st.write("Debug: App loaded successfully")
```

### 4. Check Resource Usage
```python
import psutil
st.write(f"Memory usage: {psutil.virtual_memory().percent}%")
```

### 5. Enable Debug Mode
In `.streamlit/config.toml`:
```toml
[logger]
level = "debug"
```

---

## Deployment Checklist

Before deploying, ensure:

- [ ] `requirements.txt` has all dependencies
- [ ] `packages.txt` exists (for system packages)
- [ ] `.gitignore` excludes large files
- [ ] `.streamlit/config.toml` is configured
- [ ] Code works locally
- [ ] No hardcoded secrets
- [ ] File sizes are reasonable
- [ ] Memory usage is optimized

---

## Getting Help

### 1. Streamlit Community Forum
https://discuss.streamlit.io

### 2. Streamlit Documentation
https://docs.streamlit.io/streamlit-community-cloud

### 3. GitHub Issues
Check if others have similar problems

### 4. Stack Overflow
Tag: `streamlit`

---

## Quick Fixes Summary

| Issue | Quick Fix |
|-------|-----------|
| NetCDF4 build error | Add `packages.txt` with HDF5/NetCDF libs |
| Memory exceeded | Reduce data size, add caching |
| Module not found | Add to `requirements.txt` |
| File too large | Add to `.gitignore` or use Git LFS |
| Slow performance | Add `@st.cache_data` decorators |
| App restarting | Check logs, reduce resource usage |

---

## Your Current Status

✅ **packages.txt created** - Fixes NetCDF4 installation  
✅ **requirements.txt updated** - More flexible versions  
⏳ **Waiting for redeploy** - Push changes to GitHub  

### Next Steps:

1. **Commit and push:**
   ```bash
   git add packages.txt requirements.txt
   git commit -m "Fix netCDF4 installation"
   git push origin main
   ```

2. **Wait 2-3 minutes** for auto-redeploy

3. **Check logs** in Streamlit Cloud dashboard

4. **Test your app** at your Streamlit URL

---

**Your app should now deploy successfully! 🎉**

If you still have issues, check the logs and refer to the specific issue sections above.
