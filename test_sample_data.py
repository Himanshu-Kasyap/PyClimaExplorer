"""
Sample script to generate test NetCDF data for PyClimaExplorer
Run this to create a sample dataset if you don't have real climate data
"""

import xarray as xr
import numpy as np
import pandas as pd

def create_sample_climate_data():
    """Create a sample NetCDF file with synthetic climate data."""
    
    # Define dimensions
    time = pd.date_range('2020-01-01', '2023-12-31', freq='M')
    lat = np.arange(-90, 91, 5)
    lon = np.arange(-180, 180, 5)
    
    # Create coordinate arrays
    coords = {
        'time': time,
        'lat': lat,
        'lon': lon
    }
    
    # Generate synthetic temperature data (in Celsius)
    # Base temperature with latitude gradient
    base_temp = 30 - 0.5 * np.abs(lat)
    temp_data = np.zeros((len(time), len(lat), len(lon)))
    
    for t in range(len(time)):
        for i, latitude in enumerate(lat):
            for j, longitude in enumerate(lon):
                # Base temperature
                temp = base_temp[i]
                # Add seasonal variation
                temp += 10 * np.sin(2 * np.pi * t / 12)
                # Add some random noise
                temp += np.random.normal(0, 2)
                # Add longitude-based variation (continental effect)
                temp += 5 * np.sin(2 * np.pi * longitude / 360)
                
                temp_data[t, i, j] = temp
    
    # Generate synthetic precipitation data (in mm)
    precip_data = np.zeros((len(time), len(lat), len(lon)))
    
    for t in range(len(time)):
        for i, latitude in enumerate(lat):
            for j, longitude in enumerate(lon):
                # Base precipitation (higher near equator)
                precip = 100 - np.abs(latitude)
                # Add seasonal variation
                precip += 50 * np.sin(2 * np.pi * t / 12 + np.pi/2)
                # Add random variation
                precip += np.random.normal(0, 20)
                # Ensure non-negative
                precip = max(0, precip)
                
                precip_data[t, i, j] = precip
    
    # Generate synthetic wind speed data (in m/s)
    wind_data = np.zeros((len(time), len(lat), len(lon)))
    
    for t in range(len(time)):
        for i, latitude in enumerate(lat):
            for j, longitude in enumerate(lon):
                # Base wind speed (higher at mid-latitudes)
                wind = 5 + 10 * np.exp(-((latitude - 45)**2) / 500)
                # Add seasonal variation
                wind += 3 * np.sin(2 * np.pi * t / 12)
                # Add random variation
                wind += np.random.normal(0, 2)
                # Ensure non-negative
                wind = max(0, wind)
                
                wind_data[t, i, j] = wind
    
    # Create dataset
    ds = xr.Dataset(
        {
            'temperature': (['time', 'lat', 'lon'], temp_data, {
                'units': 'degrees_celsius',
                'long_name': 'Air Temperature',
                'standard_name': 'air_temperature'
            }),
            'precipitation': (['time', 'lat', 'lon'], precip_data, {
                'units': 'mm',
                'long_name': 'Precipitation',
                'standard_name': 'precipitation_amount'
            }),
            'wind_speed': (['time', 'lat', 'lon'], wind_data, {
                'units': 'm/s',
                'long_name': 'Wind Speed',
                'standard_name': 'wind_speed'
            })
        },
        coords=coords,
        attrs={
            'title': 'Sample Climate Dataset',
            'institution': 'PyClimaExplorer',
            'source': 'Synthetic data for testing',
            'history': 'Created for demonstration purposes',
            'references': 'https://github.com/your-repo',
            'comment': 'This is synthetic data, not real climate observations'
        }
    )
    
    return ds

if __name__ == '__main__':
    print("Generating sample climate dataset...")
    ds = create_sample_climate_data()
    
    # Save to file
    output_file = 'sample_climate_data.nc'
    ds.to_netcdf(output_file)
    
    print(f"✅ Sample dataset created: {output_file}")
    print(f"\nDataset info:")
    print(f"  - Time range: {ds.time.values[0]} to {ds.time.values[-1]}")
    print(f"  - Spatial coverage: {len(ds.lat)} latitudes × {len(ds.lon)} longitudes")
    print(f"  - Variables: {list(ds.data_vars)}")
    print(f"  - File size: ~{ds.nbytes / 1024 / 1024:.2f} MB")
    print(f"\nYou can now upload this file to PyClimaExplorer!")
