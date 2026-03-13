# 🌍 PyClimaExplorer - Climate Data Visualization Dashboard

An interactive web-based dashboard for exploring and visualizing climate datasets stored in NetCDF (.nc) files. Built for rapid prototyping and data exploration during hackathons.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

### Core Functionality
- **📁 Dataset Upload**: Upload NetCDF climate datasets directly through the web interface
- **🎯 Variable Selection**: Choose from temperature, precipitation, wind speed, and other climate variables
- **📅 Time Range Selection**: Interactive slider to select specific time periods
- **🗺️ Location Selection**: Pick any geographic coordinates for detailed analysis
- **📊 Interactive Visualizations**: Zoom, pan, and hover for detailed information

### Visualizations
- **Global Heatmap**: Spatial distribution of climate variables across the globe
- **Time Series Plot**: Temporal trends at specific locations with trend lines
- **Comparison Mode**: Side-by-side comparison of two time periods
- **Difference Maps**: Visualize changes between time periods

### Advanced Features
- **🤖 AI-Generated Insights**: Automatic statistical analysis and trend detection
- **🔮 Future Predictions**: Linear regression-based climate trend forecasting
- **📈 Statistical Analysis**: Mean, min, max, standard deviation, and anomaly detection
- **🎨 Modern Dark Theme**: Eye-friendly interface optimized for data visualization

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. Clone or download this repository:
```bash
git clone <repository-url>
cd PyClimaExplorer
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Running the Dashboard

Start the Streamlit application:
```bash
streamlit run app.py
```

The dashboard will open automatically in your default web browser at `http://localhost:8501`

## 📂 Project Structure

```
PyClimaExplorer/
│
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── utils/
│   ├── data_loader.py         # NetCDF data loading and extraction
│   ├── visualization.py       # Plotly visualization functions
│   └── analysis.py            # Statistical analysis and predictions
│
└── data/                      # Place your NetCDF files here (optional)
```

## 📊 Sample Datasets

You can download sample climate datasets from these sources:

### Free Climate Data Sources
1. **NOAA Climate Data Online**
   - URL: https://www.ncei.noaa.gov/data/
   - Datasets: Temperature, precipitation, sea level data
   - Format: NetCDF

2. **Copernicus Climate Data Store**
   - URL: https://cds.climate.copernicus.eu/
   - Datasets: ERA5 reanalysis, climate projections
   - Format: NetCDF (requires free registration)

3. **NASA Earth Data**
   - URL: https://earthdata.nasa.gov/
   - Datasets: Global temperature, precipitation, atmospheric data
   - Format: NetCDF, HDF

4. **CMIP6 Climate Model Data**
   - URL: https://esgf-node.llnl.gov/projects/cmip6/
   - Datasets: Climate model outputs
   - Format: NetCDF

### Quick Test Dataset
For quick testing, you can use sample data from:
- **Xarray Tutorial Data**: Built-in sample datasets
  ```python
  import xarray as xr
  ds = xr.tutorial.open_dataset('air_temperature')
  ds.to_netcdf('sample_temperature.nc')
  ```

## 🎯 Usage Guide

### Basic Workflow

1. **Upload Dataset**
   - Click "Browse files" in the sidebar
   - Select a NetCDF (.nc) file from your computer
   - Wait for the dataset to load

2. **Select Variable**
   - Choose a climate variable from the dropdown (e.g., temperature, precipitation)

3. **Choose Time Range**
   - Use the slider to select start and end time points
   - The date range will be displayed below the slider

4. **Select Location**
   - Enter latitude and longitude coordinates
   - Or use the default center point

5. **Explore Visualizations**
   - View the global heatmap showing spatial distribution
   - Examine the time series plot for temporal trends
   - Read AI-generated insights
   - Check future trend predictions

### Comparison Mode

1. Select "Comparison Mode" in the sidebar
2. Choose two different time periods using the sliders
3. View side-by-side heatmaps
4. Examine the difference map showing changes
5. Compare statistics between periods

## 🛠️ Technical Stack

- **Language**: Python 3.8+
- **Web Framework**: Streamlit
- **Data Processing**: 
  - Xarray (NetCDF handling)
  - Pandas (data manipulation)
  - NumPy (numerical operations)
- **Visualization**: Plotly (interactive charts)
- **Machine Learning**: Scikit-learn (trend prediction)

## 📝 Code Examples

### Loading a NetCDF File
```python
from utils.data_loader import load_netcdf

# Load dataset
dataset = load_netcdf(uploaded_file)

# Get available variables
variables = get_variables(dataset)
```

### Creating Visualizations
```python
from utils.visualization import create_heatmap, create_timeseries

# Create heatmap
fig = create_heatmap(data_array, 'temperature')

# Create time series
fig = create_timeseries(dataset, 'temperature', lat=40.0, lon=-100.0)
```

### Generating Insights
```python
from utils.analysis import generate_insights, predict_future_trend

# Get AI insights
insights = generate_insights(dataset, 'temperature', lat, lon, start, end)

# Predict future trends
prediction_fig = predict_future_trend(dataset, 'temperature', lat, lon, start, end)
```

## 🎨 Customization

### Changing the Color Scheme
Edit the CSS in `app.py`:
```python
st.markdown("""
    <style>
    h1, h2, h3 {
        color: #YOUR_COLOR;
    }
    </style>
""", unsafe_allow_html=True)
```

### Adding New Variables
The system automatically detects climate variables. To add custom detection:
Edit `utils/data_loader.py` in the `get_variables()` function.

## 🐛 Troubleshooting

### Common Issues

**Issue**: "Error loading NetCDF file"
- **Solution**: Ensure the file is a valid NetCDF format (.nc extension)
- Check that the file isn't corrupted

**Issue**: "No variables found"
- **Solution**: The dataset might use non-standard variable names
- Check the dataset structure using `ncdump -h filename.nc`

**Issue**: "Memory error with large files"
- **Solution**: Use smaller time ranges or spatial subsets
- Consider downsampling the data before upload

**Issue**: Visualizations not displaying
- **Solution**: Ensure Plotly is properly installed
- Clear browser cache and reload

## 🚀 Performance Tips

- Start with smaller datasets (< 100MB) for faster loading
- Use time range sliders to limit data processing
- Close unused browser tabs to free memory
- For large datasets, consider preprocessing to reduce size

## 🚀 Deployment

### Recommended: Streamlit Community Cloud (Free & Easy)

**See [DEPLOY_STREAMLIT_CLOUD.md](DEPLOY_STREAMLIT_CLOUD.md) for complete step-by-step guide**

1. Push your code to GitHub
2. Go to https://share.streamlit.io
3. Sign in with GitHub
4. Click "New app" and select your repository
5. Deploy in 1 click!

Your app will be live at: `https://your-app-name.streamlit.app`

### Alternative Deployment Options

**See [DEPLOY_ALTERNATIVES.md](DEPLOY_ALTERNATIVES.md) for detailed guides on:**

- **Heroku**: Easy deployment with CLI
- **Railway**: Modern platform with auto-scaling
- **Google Cloud Run**: Scalable production deployment
- **Docker**: Deploy anywhere with containers
- **AWS EC2**: Full control VPS hosting

### Quick Docker Deployment

```bash
# Build image
docker build -t pyclima-explorer .

# Run container
docker run -p 8501:8501 pyclima-explorer

# Access at http://localhost:8501
```

### Important Note About Vercel

⚠️ **Vercel is NOT supported** for Streamlit apps because:
- Streamlit requires persistent WebSocket connections
- Vercel is optimized for static sites and serverless functions
- Use Streamlit Cloud, Heroku, or Railway instead

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 👥 Authors

Built for hackathon prototyping and climate data exploration.

## 🙏 Acknowledgments

- Streamlit for the amazing web framework
- Xarray team for NetCDF handling
- Plotly for interactive visualizations
- Climate data providers (NOAA, Copernicus, NASA)

## 📧 Support

For questions or issues:
- Open an issue on GitHub
- Check the troubleshooting section
- Review sample datasets documentation

---

**Happy Climate Exploring! 🌍📊**
