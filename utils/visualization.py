import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
from utils.data_loader import get_spatial_bounds, extract_point_timeseries

def create_heatmap(data_array, variable_name, title=None):
    """Create an interactive global heatmap."""
    # Get spatial bounds
    spatial_bounds = get_spatial_bounds(data_array)
    lat_name = spatial_bounds['lat_name']
    lon_name = spatial_bounds['lon_name']
    
    # Calculate mean over time
    data_mean = data_array.mean(dim='time', skipna=True)
    
    # Get coordinates
    lats = data_mean[lat_name].values
    lons = data_mean[lon_name].values
    values = data_mean.values
    
    # Create figure
    fig = go.Figure(data=go.Heatmap(
        z=values,
        x=lons,
        y=lats,
        colorscale='RdYlBu_r',
        colorbar=dict(
            title=variable_name,
            titleside='right',
            tickmode='linear',
            thickness=20
        ),
        hovertemplate='Lat: %{y:.2f}<br>Lon: %{x:.2f}<br>Value: %{z:.2f}<extra></extra>'
    ))
    
    fig.update_layout(
        title=title or f'{variable_name} - Global Distribution',
        xaxis_title='Longitude',
        yaxis_title='Latitude',
        template='plotly_dark',
        height=500,
        hovermode='closest',
        plot_bgcolor='#0e1117',
        paper_bgcolor='#0e1117',
        font=dict(color='#ffffff')
    )
    
    return fig

def create_timeseries(dataset, variable, lat, lon, start_time, end_time):
    """Create time series plot for a specific location."""
    # Extract point data
    point_data = extract_point_timeseries(dataset, variable, lat, lon)
    
    # Filter by time range
    point_data = point_data.sel(time=slice(start_time, end_time))
    
    # Convert to pandas for easier plotting
    df = point_data.to_dataframe().reset_index()
    
    # Create figure
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df['time'],
        y=df[variable],
        mode='lines+markers',
        name=variable,
        line=dict(color='#00d4ff', width=2),
        marker=dict(size=4),
        hovertemplate='Time: %{x}<br>Value: %{y:.2f}<extra></extra>'
    ))
    
    # Add trend line
    if len(df) > 2:
        z = np.polyfit(range(len(df)), df[variable].values, 1)
        p = np.poly1d(z)
        fig.add_trace(go.Scatter(
            x=df['time'],
            y=p(range(len(df))),
            mode='lines',
            name='Trend',
            line=dict(color='#ff6b6b', width=2, dash='dash'),
            hovertemplate='Trend: %{y:.2f}<extra></extra>'
        ))
    
    fig.update_layout(
        title=f'{variable} Time Series at ({lat:.2f}°, {lon:.2f}°)',
        xaxis_title='Time',
        yaxis_title=variable,
        template='plotly_dark',
        height=400,
        hovermode='x unified',
        plot_bgcolor='#0e1117',
        paper_bgcolor='#0e1117',
        font=dict(color='#ffffff'),
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        )
    )
    
    return fig

def create_comparison_heatmap(data1, data2, variable_name):
    """Create a difference heatmap comparing two time periods."""
    spatial_bounds = get_spatial_bounds(data1)
    lat_name = spatial_bounds['lat_name']
    lon_name = spatial_bounds['lon_name']
    
    # Calculate means
    mean1 = data1.mean(dim='time', skipna=True)
    mean2 = data2.mean(dim='time', skipna=True)
    
    # Calculate difference
    diff = mean2 - mean1
    
    # Get coordinates
    lats = diff[lat_name].values
    lons = diff[lon_name].values
    values = diff.values
    
    # Create figure
    fig = go.Figure(data=go.Heatmap(
        z=values,
        x=lons,
        y=lats,
        colorscale='RdBu_r',
        zmid=0,
        colorbar=dict(
            title=f'Δ {variable_name}',
            titleside='right',
            tickmode='linear',
            thickness=20
        ),
        hovertemplate='Lat: %{y:.2f}<br>Lon: %{x:.2f}<br>Change: %{z:.2f}<extra></extra>'
    ))
    
    fig.update_layout(
        title=f'{variable_name} - Change Between Periods',
        xaxis_title='Longitude',
        yaxis_title='Latitude',
        template='plotly_dark',
        height=500,
        hovermode='closest',
        plot_bgcolor='#0e1117',
        paper_bgcolor='#0e1117',
        font=dict(color='#ffffff')
    )
    
    return fig
