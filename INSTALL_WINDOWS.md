# 🪟 Windows Installation Guide - PyClimaExplorer

Complete step-by-step installation guide for Windows users.

## Prerequisites

### 1. Install Python

**Check if Python is installed:**
```cmd
python --version
```

If you see "Python 3.8" or higher, skip to step 2.

**If Python is not installed:**

1. Download Python from: https://www.python.org/downloads/
2. Run the installer
3. ⚠️ **IMPORTANT**: Check "Add Python to PATH" during installation
4. Click "Install Now"
5. Verify installation:
   ```cmd
   python --version
   ```

### 2. Install pip (Python Package Manager)

Pip usually comes with Python. Verify:
```cmd
pip --version
```

If not installed:
```cmd
python -m ensurepip --upgrade
```

## Installation Methods

### Method 1: Automated Setup (Recommended)

1. **Open Command Prompt**
   - Press `Win + R`
   - Type `cmd`
   - Press Enter

2. **Navigate to project folder**
   ```cmd
   cd path\to\PyClimaExplorer
   ```

3. **Run setup script**
   ```cmd
   python setup.py
   ```

4. **Follow prompts**
   - Setup will install dependencies
   - Optionally generate sample data
   - Show next steps

### Method 2: Manual Installation

1. **Open Command Prompt**
   ```cmd
   Win + R → cmd → Enter
   ```

2. **Navigate to project**
   ```cmd
   cd C:\Users\YourName\PyClimaExplorer
   ```

3. **Install dependencies**
   ```cmd
   pip install -r requirements.txt
   ```

4. **Generate sample data (optional)**
   ```cmd
   python test_sample_data.py
   ```

5. **Verify installation**
   ```cmd
   python verify_installation.py
   ```

## Running the Dashboard

### Option 1: Using Batch File (Easiest)

Double-click `run_dashboard.bat` in File Explorer

### Option 2: Command Line

```cmd
streamlit run app.py
```

### Option 3: PowerShell

```powershell
streamlit run app.py
```

The dashboard will automatically open in your default browser at:
```
http://localhost:8501
```

## Troubleshooting

### Problem: "python is not recognized"

**Solution:**
1. Python is not in PATH
2. Reinstall Python with "Add to PATH" checked
3. Or add manually:
   - Search "Environment Variables" in Windows
   - Edit "Path" variable
   - Add Python installation directory

### Problem: "pip is not recognized"

**Solution:**
```cmd
python -m pip install -r requirements.txt
```

### Problem: "streamlit is not recognized"

**Solution:**
```cmd
python -m streamlit run app.py
```

### Problem: Permission denied

**Solution:**
Run Command Prompt as Administrator:
- Right-click Command Prompt
- Select "Run as administrator"

### Problem: Module not found errors

**Solution:**
```cmd
pip install --upgrade -r requirements.txt
```

### Problem: Port already in use

**Solution:**
```cmd
streamlit run app.py --server.port 8502
```

### Problem: Browser doesn't open

**Solution:**
Manually open browser and go to:
```
http://localhost:8501
```

## Verification Steps

### 1. Check Python Installation
```cmd
python --version
```
Expected: Python 3.8.0 or higher

### 2. Check pip Installation
```cmd
pip --version
```
Expected: pip 20.0 or higher

### 3. Verify Dependencies
```cmd
python verify_installation.py
```
Expected: All ✅ checkmarks

### 4. Test Sample Data
```cmd
python test_sample_data.py
```
Expected: Creates `sample_climate_data.nc`

### 5. Launch Dashboard
```cmd
streamlit run app.py
```
Expected: Browser opens with dashboard

## Common Windows Issues

### Issue: Long path names

**Symptom**: Errors with file paths
**Solution**: 
- Move project closer to C:\ drive
- Example: `C:\PyClimaExplorer`

### Issue: Antivirus blocking

**Symptom**: Installation fails or files deleted
**Solution**:
- Temporarily disable antivirus
- Add Python to exclusions
- Re-run installation

### Issue: Firewall blocking

**Symptom**: Can't access localhost:8501
**Solution**:
- Allow Python through Windows Firewall
- Settings → Firewall → Allow an app

### Issue: Multiple Python versions

**Symptom**: Wrong Python version used
**Solution**:
```cmd
py -3.9 -m pip install -r requirements.txt
py -3.9 -m streamlit run app.py
```

## Performance Tips for Windows

### 1. Close Unnecessary Programs
- Free up RAM for data processing
- Close browser tabs

### 2. Use SSD if Available
- Store project on SSD for faster loading
- Move NetCDF files to SSD

### 3. Increase Virtual Memory
- Settings → System → About → Advanced system settings
- Performance → Settings → Advanced → Virtual memory

### 4. Disable Windows Search Indexing
- For project folder only
- Speeds up file operations

## Uninstallation

### Remove Python Packages
```cmd
pip uninstall streamlit xarray pandas numpy plotly netCDF4 scikit-learn -y
```

### Remove Project
Simply delete the PyClimaExplorer folder

### Remove Python (if needed)
- Settings → Apps → Python → Uninstall

## Updating

### Update Dependencies
```cmd
pip install --upgrade -r requirements.txt
```

### Update Streamlit Only
```cmd
pip install --upgrade streamlit
```

### Check for Updates
```cmd
pip list --outdated
```

## Windows-Specific Features

### Create Desktop Shortcut

1. Right-click `run_dashboard.bat`
2. Select "Create shortcut"
3. Move shortcut to Desktop
4. Rename to "PyClimaExplorer"

### Pin to Taskbar

1. Create shortcut (above)
2. Right-click shortcut
3. Select "Pin to taskbar"

### Add to Start Menu

1. Press `Win + R`
2. Type `shell:programs`
3. Copy `run_dashboard.bat` here

## Advanced Configuration

### Change Default Browser

Edit `.streamlit/config.toml`:
```toml
[browser]
serverAddress = "localhost"
serverPort = 8501
```

### Increase Upload Limit

Edit `.streamlit/config.toml`:
```toml
[server]
maxUploadSize = 1000
```

### Enable CORS (for remote access)

Edit `.streamlit/config.toml`:
```toml
[server]
enableCORS = true
```

## Getting Help

### Check Logs
Streamlit logs appear in Command Prompt window

### Enable Debug Mode
```cmd
streamlit run app.py --logger.level=debug
```

### Clear Cache
```cmd
streamlit cache clear
```

### Reinstall Everything
```cmd
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

## Next Steps

After successful installation:

1. ✅ Read [QUICKSTART.md](QUICKSTART.md) for 5-minute guide
2. ✅ Check [README.md](README.md) for full documentation
3. ✅ Try [EXAMPLES.md](EXAMPLES.md) for usage examples
4. ✅ Download real climate data from NOAA/NASA

## Support

If you encounter issues:

1. Check this troubleshooting guide
2. Run `python verify_installation.py`
3. Check Python and pip versions
4. Try reinstalling dependencies
5. Search error messages online

## System Requirements

### Minimum
- Windows 10 or higher
- Python 3.8+
- 4 GB RAM
- 1 GB free disk space

### Recommended
- Windows 11
- Python 3.9+
- 8 GB RAM
- 5 GB free disk space (for data)
- SSD storage

---

**Installation complete! Start exploring climate data! 🌍📊**

For questions, check the main [README.md](README.md) or [QUICKSTART.md](QUICKSTART.md).
