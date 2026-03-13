# 🚀 Quick Start Guide - PyClimaExplorer

Get up and running with PyClimaExplorer in 5 minutes!

## Step 1: Install Dependencies (2 minutes)

Open your terminal and run:

```bash
pip install -r requirements.txt
```

This installs:
- Streamlit (web framework)
- Xarray (NetCDF handling)
- Plotly (visualizations)
- Pandas, NumPy (data processing)
- Scikit-learn (predictions)

## Step 2: Generate Sample Data (1 minute)

If you don't have a NetCDF file, create sample data:

```bash
python test_sample_data.py
```

This creates `sample_climate_data.nc` with synthetic temperature, precipitation, and wind speed data.

## Step 3: Launch the Dashboard (30 seconds)

```bash
streamlit run app.py
```

Your browser will automatically open to `http://localhost:8501`

## Step 4: Explore Climate Data (2 minutes)

### Upload Dataset
1. Click "Browse files" in the sidebar
2. Select `sample_climate_data.nc` (or your own NetCDF file)
3. Wait for loading confirmation ✅

### Basic Exploration
1. **Select Variable**: Choose "temperature", "precipitation", or "wind_speed"
2. **Choose Time Range**: Drag the slider to select months
3. **Pick Location**: Enter coordinates (try lat: 40, lon: -100 for USA)
4. **View Results**:
   - Global heatmap shows spatial distribution
   - Time series shows trends at your location
   - AI insights provide automatic analysis
   - Future predictions show trend forecasts

### Advanced Features
1. **Comparison Mode**:
   - Select "Comparison Mode" in sidebar
   - Choose two different time periods
   - View side-by-side maps and difference visualization

2. **Interactive Features**:
   - Hover over charts for detailed values
   - Zoom and pan on maps
   - Click legend items to toggle visibility

## Common Use Cases

### 1. Temperature Trend Analysis
```
Variable: temperature
Time Range: Full dataset
Location: Your city coordinates
Result: See warming/cooling trends
```

### 2. Precipitation Patterns
```
Variable: precipitation
Time Range: Seasonal (e.g., months 0-12)
Location: Agricultural region
Result: Identify wet/dry seasons
```

### 3. Climate Change Detection
```
Mode: Comparison Mode
Period 1: First year
Period 2: Last year
Result: Visualize climate changes
```

## Tips for Best Results

✅ **DO**:
- Start with smaller time ranges for faster processing
- Use the hover tooltips to explore data details
- Try different locations to compare regions
- Read the AI insights for quick understanding

❌ **DON'T**:
- Upload extremely large files (>500MB) without preprocessing
- Select the entire time range on first try
- Ignore the statistics panel - it shows key metrics

## Troubleshooting

**Dashboard won't start?**
```bash
# Check Python version (need 3.8+)
python --version

# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

**Can't upload file?**
- Ensure file has .nc extension
- Check file isn't corrupted
- Try the sample data first

**Visualizations not showing?**
- Refresh the browser
- Check browser console for errors
- Try a different browser (Chrome recommended)

## Next Steps

- 📖 Read the full [README.md](README.md) for detailed documentation
- 🌍 Download real climate data from NOAA, Copernicus, or NASA
- 🎨 Customize the dashboard colors and layout
- 🔧 Extend functionality by modifying the utils modules

## Getting Real Climate Data

### Quick Links:
1. **NOAA**: https://www.ncei.noaa.gov/data/
2. **Copernicus**: https://cds.climate.copernicus.eu/
3. **NASA**: https://earthdata.nasa.gov/

### Using Xarray Tutorial Data:
```python
import xarray as xr
ds = xr.tutorial.open_dataset('air_temperature')
ds.to_netcdf('real_temperature.nc')
```

## Support

Need help? Check:
- README.md for detailed documentation
- Code comments in utils/ modules
- Streamlit docs: https://docs.streamlit.io
- Xarray docs: https://docs.xarray.dev

---

**You're all set! Start exploring climate data! 🌍📊**
