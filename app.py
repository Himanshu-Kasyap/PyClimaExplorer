import streamlit as st
import xarray as xr
import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Add utils to path
sys.path.append(str(Path(__file__).parent))

from utils.data_loader import load_netcdf, get_variables, get_time_range, get_spatial_bounds
from utils.visualization import create_heatmap, create_timeseries, create_comparison_heatmap
from utils.analysis import calculate_statistics, generate_insights, predict_future_trend

# Page configuration
st.set_page_config(
    page_title="PyClimaExplorer",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stApp {
        background-color: #0e1117;
    }
    h1, h2, h3 {
        color: #00d4ff;
    }
    .metric-card {
        background-color: #1e2130;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #00d4ff;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>🌍 PyClimaExplorer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>Interactive Climate Data Visualization Dashboard</p>", unsafe_allow_html=True)

# Initialize session state
if 'dataset' not in st.session_state:
    st.session_state.dataset = None
if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None

# Sidebar
with st.sidebar:
    st.markdown("## 📁 Data Upload")
    uploaded_file = st.file_uploader("Upload NetCDF Dataset (.nc)", type=['nc'])
    
    if uploaded_file is not None:
        if st.session_state.uploaded_file != uploaded_file:
            st.session_state.uploaded_file = uploaded_file
            with st.spinner("Loading dataset..."):
                st.session_state.dataset = load_netcdf(uploaded_file)
            st.success("✅ Dataset loaded successfully!")
    
    if st.session_state.dataset is not None:
        ds = st.session_state.dataset
        
        st.markdown("---")
        st.markdown("## 🎯 Variable Selection")
        variables = get_variables(ds)
        selected_var = st.selectbox("Select Climate Variable", variables)
        
        st.markdown("---")
        st.markdown("## 📅 Time Range")
        time_range = get_time_range(ds)
        if time_range:
            time_slider = st.slider(
                "Select Time Period",
                min_value=0,
                max_value=len(time_range) - 1,
                value=(0, min(len(time_range) - 1, 50)),
                format="%d"
            )
            start_time = time_range[time_slider[0]]
            end_time = time_range[time_slider[1]]
            st.info(f"From: {start_time}\nTo: {end_time}")
        
        st.markdown("---")
        st.markdown("## 🗺️ Location Selection")
        spatial_bounds = get_spatial_bounds(ds)
        
        col1, col2 = st.columns(2)
        with col1:
            lat = st.number_input(
                "Latitude",
                min_value=float(spatial_bounds['lat_min']),
                max_value=float(spatial_bounds['lat_max']),
                value=float((spatial_bounds['lat_min'] + spatial_bounds['lat_max']) / 2)
            )
        with col2:
            lon = st.number_input(
                "Longitude",
                min_value=float(spatial_bounds['lon_min']),
                max_value=float(spatial_bounds['lon_max']),
                value=float((spatial_bounds['lon_min'] + spatial_bounds['lon_max']) / 2)
            )
        
        st.markdown("---")
        st.markdown("## 🔬 Analysis Mode")
        analysis_mode = st.radio(
            "Select Mode",
            ["Single Period", "Comparison Mode"]
        )
        
        if analysis_mode == "Comparison Mode":
            st.markdown("### Period 2")
            time_slider2 = st.slider(
                "Select Second Time Period",
                min_value=0,
                max_value=len(time_range) - 1,
                value=(min(len(time_range) - 1, 51), len(time_range) - 1),
                format="%d"
            )
            start_time2 = time_range[time_slider2[0]]
            end_time2 = time_range[time_slider2[1]]

# Main content
if st.session_state.dataset is not None:
    ds = st.session_state.dataset
    
    # Extract data for selected parameters
    data_subset = ds[selected_var].sel(time=slice(start_time, end_time))
    
    # Statistics
    st.markdown("## 📊 Key Statistics")
    stats = calculate_statistics(data_subset)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Mean", f"{stats['mean']:.2f}")
    with col2:
        st.metric("Min", f"{stats['min']:.2f}")
    with col3:
        st.metric("Max", f"{stats['max']:.2f}")
    with col4:
        st.metric("Std Dev", f"{stats['std']:.2f}")
    
    st.markdown("---")
    
    # Visualizations
    if analysis_mode == "Single Period":
        # Global Heatmap
        st.markdown("## 🗺️ Global Climate Heatmap")
        with st.spinner("Generating heatmap..."):
            fig_map = create_heatmap(data_subset, selected_var)
            st.plotly_chart(fig_map, use_container_width=True)
        
        st.markdown("---")
        
        # Time Series
        st.markdown("## 📈 Time Series Analysis")
        with st.spinner("Generating time series..."):
            fig_ts = create_timeseries(ds, selected_var, lat, lon, start_time, end_time)
            st.plotly_chart(fig_ts, use_container_width=True)
        
        # AI Insights
        st.markdown("---")
        st.markdown("## 🤖 AI-Generated Insights")
        insights = generate_insights(ds, selected_var, lat, lon, start_time, end_time)
        st.info(insights)
        
        # Future Prediction
        st.markdown("---")
        st.markdown("## 🔮 Future Trend Prediction")
        with st.spinner("Calculating prediction..."):
            fig_pred = predict_future_trend(ds, selected_var, lat, lon, start_time, end_time)
            if fig_pred:
                st.plotly_chart(fig_pred, use_container_width=True)
    
    else:  # Comparison Mode
        st.markdown("## 🔄 Climate Comparison")
        
        data_subset2 = ds[selected_var].sel(time=slice(start_time2, end_time2))
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"### Period 1: {start_time} to {end_time}")
            fig_map1 = create_heatmap(data_subset, selected_var, title=f"{selected_var} - Period 1")
            st.plotly_chart(fig_map1, use_container_width=True)
        
        with col2:
            st.markdown(f"### Period 2: {start_time2} to {end_time2}")
            fig_map2 = create_heatmap(data_subset2, selected_var, title=f"{selected_var} - Period 2")
            st.plotly_chart(fig_map2, use_container_width=True)
        
        # Difference map
        st.markdown("### 📊 Difference Map (Period 2 - Period 1)")
        fig_diff = create_comparison_heatmap(data_subset, data_subset2, selected_var)
        st.plotly_chart(fig_diff, use_container_width=True)
        
        # Comparison insights
        stats1 = calculate_statistics(data_subset)
        stats2 = calculate_statistics(data_subset2)
        
        st.markdown("### 📈 Comparison Statistics")
        col1, col2, col3 = st.columns(3)
        with col1:
            change = stats2['mean'] - stats1['mean']
            st.metric("Mean Change", f"{change:.2f}", f"{(change/stats1['mean']*100):.1f}%")
        with col2:
            change = stats2['max'] - stats1['max']
            st.metric("Max Change", f"{change:.2f}")
        with col3:
            change = stats2['min'] - stats1['min']
            st.metric("Min Change", f"{change:.2f}")

else:
    # Welcome screen
    st.markdown("""
    <div style='text-align: center; padding: 50px;'>
        <h2>👋 Welcome to PyClimaExplorer!</h2>
        <p style='color: #888; font-size: 18px;'>
            Upload a NetCDF climate dataset to get started with interactive visualizations.
        </p>
        <br>
        <p style='color: #666;'>
            📁 Use the sidebar to upload your .nc file<br>
            🌡️ Explore temperature, precipitation, and wind speed data<br>
            📊 Generate interactive charts and insights<br>
            🔮 Predict future climate trends
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📚 Sample Datasets")
    st.markdown("""
    You can download sample climate datasets from:
    - [NOAA Climate Data](https://www.ncei.noaa.gov/data/)
    - [Copernicus Climate Data Store](https://cds.climate.copernicus.eu/)
    - [NASA Earth Data](https://earthdata.nasa.gov/)
    """)
