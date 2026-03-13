import xarray as xr
import numpy as np
import tempfile
from pathlib import Path

def load_netcdf(uploaded_file):
    """Load NetCDF file from uploaded file object."""
    try:
        # Save uploaded file to temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix='.nc') as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_path = tmp_file.name
        
        # Load with xarray
        ds = xr.open_dataset(tmp_path)
        return ds
    except Exception as e:
        raise Exception(f"Error loading NetCDF file: {str(e)}")

def get_variables(dataset):
    """Extract available climate variables from dataset."""
    # Filter out coordinate variables
    coord_vars = set(dataset.coords.keys())
    data_vars = [var for var in dataset.data_vars if var not in coord_vars]
    
    # Common climate variable names
    climate_vars = []
    for var in data_vars:
        var_lower = var.lower()
        if any(keyword in var_lower for keyword in ['temp', 'precip', 'wind', 'pressure', 'humidity', 'cloud']):
            climate_vars.append(var)
    
    # If no climate vars found, return all data vars
    return climate_vars if climate_vars else data_vars

def get_time_range(dataset):
    """Extract time range from dataset."""
    time_dims = ['time', 'Time', 'TIME', 't']
    
    for dim in time_dims:
        if dim in dataset.dims:
            time_values = dataset[dim].values
            return time_values
    
    return None

def get_spatial_bounds(dataset):
    """Extract spatial bounds (lat/lon) from dataset."""
    # Common latitude names
    lat_names = ['lat', 'latitude', 'Latitude', 'LAT', 'y']
    lon_names = ['lon', 'longitude', 'Longitude', 'LON', 'x']
    
    lat_coord = None
    lon_coord = None
    
    # Find latitude coordinate
    for name in lat_names:
        if name in dataset.coords or name in dataset.dims:
            lat_coord = name
            break
    
    # Find longitude coordinate
    for name in lon_names:
        if name in dataset.coords or name in dataset.dims:
            lon_coord = name
            break
    
    if lat_coord and lon_coord:
        lat_values = dataset[lat_coord].values
        lon_values = dataset[lon_coord].values
        
        return {
            'lat_min': np.min(lat_values),
            'lat_max': np.max(lat_values),
            'lon_min': np.min(lon_values),
            'lon_max': np.max(lon_values),
            'lat_name': lat_coord,
            'lon_name': lon_coord
        }
    
    # Default bounds if not found
    return {
        'lat_min': -90,
        'lat_max': 90,
        'lon_min': -180,
        'lon_max': 180,
        'lat_name': 'lat',
        'lon_name': 'lon'
    }

def extract_point_timeseries(dataset, variable, lat, lon):
    """Extract time series data for a specific point."""
    spatial_bounds = get_spatial_bounds(dataset)
    lat_name = spatial_bounds['lat_name']
    lon_name = spatial_bounds['lon_name']
    
    try:
        # Select nearest point
        point_data = dataset[variable].sel(
            {lat_name: lat, lon_name: lon},
            method='nearest'
        )
        return point_data
    except Exception as e:
        raise Exception(f"Error extracting point data: {str(e)}")
