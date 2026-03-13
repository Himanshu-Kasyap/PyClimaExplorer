# 📚 PyClimaExplorer - Usage Examples

This document provides practical examples for using PyClimaExplorer with different types of climate data.

## Table of Contents
1. [Basic Usage](#basic-usage)
2. [Temperature Analysis](#temperature-analysis)
3. [Precipitation Patterns](#precipitation-patterns)
4. [Climate Change Detection](#climate-change-detection)
5. [Advanced Analysis](#advanced-analysis)
6. [Programmatic Usage](#programmatic-usage)

---

## Basic Usage

### Example 1: First Time Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Generate sample data
python test_sample_data.py

# Launch dashboard
streamlit run app.py
```

### Example 2: Upload and Explore

1. **Upload**: Click "Browse files" → Select `sample_climate_data.nc`
2. **Select Variable**: Choose "temperature"
3. **Time Range**: Drag slider to months 0-24
4. **Location**: Enter lat=40, lon=-100 (Central USA)
5. **View**: Observe heatmap and time series

---

## Temperature Analysis

### Example 3: Global Temperature Distribution

**Objective**: Visualize global temperature patterns

**Steps**:
1. Variable: `temperature`
2. Time Range: Full dataset (all months)
3. View: Global heatmap

**Expected Results**:
- Warmer temperatures near equator (red)
- Cooler temperatures at poles (blue)
- Seasonal variations visible in time series

**Insights to Look For**:
- Temperature gradient from equator to poles
- Seasonal cycles (summer/winter)
- Continental vs oceanic patterns

### Example 4: Urban Heat Island Effect

**Objective**: Compare urban vs rural temperatures

**Steps**:
1. Variable: `temperature`
2. Location 1: Urban center (e.g., lat=40.7, lon=-74.0 - NYC)
3. Location 2: Rural area (e.g., lat=40.0, lon=-74.0)
4. Compare time series

**Analysis**:
- Urban areas typically show higher temperatures
- Less temperature variation in urban areas
- Heat island effect more pronounced in summer

### Example 5: Temperature Trend Detection

**Objective**: Identify warming/cooling trends

**Steps**:
1. Variable: `temperature`
2. Time Range: Full dataset
3. Location: Any point
4. View: Time series with trend line

**Interpretation**:
- Upward trend line = warming
- Downward trend line = cooling
- Flat trend line = stable
- Check AI insights for quantitative analysis

---

## Precipitation Patterns

### Example 6: Seasonal Precipitation

**Objective**: Identify wet and dry seasons

**Steps**:
1. Variable: `precipitation`
2. Time Range: One year (12 months)
3. Location: Tropical region (lat=0-10)
4. View: Time series

**Expected Patterns**:
- Tropical regions: Two rainy seasons
- Temperate regions: Summer or winter peaks
- Arid regions: Low, sporadic precipitation

### Example 7: Drought Detection

**Objective**: Identify periods of low precipitation

**Steps**:
1. Variable: `precipitation`
2. Time Range: Multi-year period
3. View: Time series
4. Check: AI insights for anomalies

**Indicators**:
- Values consistently below mean
- Anomaly detection flags
- Comparison with historical average

### Example 8: Monsoon Analysis

**Objective**: Analyze monsoon patterns

**Steps**:
1. Variable: `precipitation`
2. Location: South Asia (lat=20, lon=80)
3. Time Range: Annual cycle
4. View: Time series

**Look For**:
- Sharp increase in summer months
- Dry winter period
- Year-to-year variability

---

## Climate Change Detection

### Example 9: Decadal Temperature Change

**Objective**: Compare temperatures across decades

**Steps**:
1. Mode: **Comparison Mode**
2. Variable: `temperature`
3. Period 1: First year (months 0-11)
4. Period 2: Last year (months 36-47)
5. View: Difference map

**Analysis**:
- Red areas: Warming
- Blue areas: Cooling
- Check statistics for mean change
- Look for spatial patterns (Arctic amplification)

### Example 10: Precipitation Changes

**Objective**: Detect changes in precipitation patterns

**Steps**:
1. Mode: **Comparison Mode**
2. Variable: `precipitation`
3. Period 1: Early period
4. Period 2: Recent period
5. View: Side-by-side and difference maps

**Interpretation**:
- Positive values: Increased precipitation
- Negative values: Decreased precipitation
- Look for regional patterns

### Example 11: Extreme Event Frequency

**Objective**: Identify changes in extreme events

**Steps**:
1. Variable: `temperature` or `precipitation`
2. Time Range: Full dataset
3. View: Time series
4. Check: AI insights for anomalies

**Indicators**:
- Increased frequency of values >2σ from mean
- Higher maximum values in recent years
- More variable patterns

---

## Advanced Analysis

### Example 12: Spatial Correlation

**Objective**: Find regions with similar climate patterns

**Steps**:
1. Select reference location
2. View time series
3. Test multiple locations
4. Compare time series shapes

**Use Cases**:
- Identify climate zones
- Find analogous regions
- Understand teleconnections

### Example 13: Future Trend Prediction

**Objective**: Forecast future climate conditions

**Steps**:
1. Variable: `temperature`
2. Time Range: Historical period
3. Location: Any point
4. View: Prediction chart

**Interpretation**:
- Dashed line shows forecast
- Based on linear trend
- Uncertainty increases with time
- Use for short-term projections only

### Example 14: Multi-Variable Analysis

**Objective**: Understand relationships between variables

**Steps**:
1. Analyze temperature time series
2. Switch to precipitation
3. Compare patterns at same location
4. Look for inverse relationships

**Relationships to Explore**:
- Temperature vs precipitation
- Wind speed vs temperature
- Seasonal co-variations

---

## Programmatic Usage

### Example 15: Using Utils Modules Directly

```python
from utils.data_loader import load_netcdf, get_variables
from utils.visualization import create_heatmap
from utils.analysis import calculate_statistics

# Load data
with open('sample_climate_data.nc', 'rb') as f:
    dataset = load_netcdf(f)

# Get variables
variables = get_variables(dataset)
print(f"Available variables: {variables}")

# Calculate statistics
stats = calculate_statistics(dataset['temperature'])
print(f"Temperature stats: {stats}")

# Create visualization
fig = create_heatmap(dataset['temperature'], 'temperature')
fig.show()
```

### Example 16: Batch Processing

```python
import xarray as xr
from pathlib import Path
from utils.analysis import calculate_statistics

# Process multiple files
data_dir = Path('data')
results = {}

for nc_file in data_dir.glob('*.nc'):
    ds = xr.open_dataset(nc_file)
    stats = calculate_statistics(ds['temperature'])
    results[nc_file.name] = stats

# Print summary
for filename, stats in results.items():
    print(f"{filename}: mean={stats['mean']:.2f}")
```

### Example 17: Custom Analysis

```python
import numpy as np
from utils.data_loader import extract_point_timeseries

# Load dataset
dataset = xr.open_dataset('sample_climate_data.nc')

# Extract data for multiple locations
locations = [
    (40, -100),  # Central USA
    (51, 0),     # London
    (-33, 151),  # Sydney
]

for lat, lon in locations:
    data = extract_point_timeseries(dataset, 'temperature', lat, lon)
    mean_temp = data.mean().values
    print(f"Location ({lat}, {lon}): {mean_temp:.2f}°C")
```

### Example 18: Export Processed Data

```python
import pandas as pd
from utils.data_loader import extract_point_timeseries

# Extract time series
dataset = xr.open_dataset('sample_climate_data.nc')
data = extract_point_timeseries(dataset, 'temperature', 40, -100)

# Convert to pandas
df = data.to_dataframe().reset_index()

# Export to CSV
df.to_csv('temperature_timeseries.csv', index=False)
print("Data exported to temperature_timeseries.csv")
```

---

## Real-World Use Cases

### Use Case 1: Agricultural Planning

**Scenario**: Farmer wants to understand precipitation patterns

**Workflow**:
1. Upload regional climate data
2. Select precipitation variable
3. Analyze seasonal patterns
4. Identify optimal planting times
5. Check future predictions

### Use Case 2: Climate Research

**Scenario**: Researcher studying Arctic warming

**Workflow**:
1. Upload Arctic temperature data
2. Use comparison mode for different decades
3. Analyze spatial patterns
4. Generate insights report
5. Export visualizations for publication

### Use Case 3: Urban Planning

**Scenario**: City planner assessing heat risk

**Workflow**:
1. Upload urban temperature data
2. Identify heat island locations
3. Analyze temporal trends
4. Compare with rural areas
5. Plan mitigation strategies

### Use Case 4: Education

**Scenario**: Teacher demonstrating climate concepts

**Workflow**:
1. Use sample data
2. Show global temperature distribution
3. Demonstrate seasonal cycles
4. Explain climate zones
5. Discuss climate change

---

## Tips and Tricks

### Tip 1: Optimize Performance
- Start with smaller time ranges
- Use time averaging for large datasets
- Close unused browser tabs

### Tip 2: Better Visualizations
- Adjust time range for clearer patterns
- Use comparison mode for change detection
- Hover over charts for exact values

### Tip 3: Interpretation
- Always check units in variable names
- Consider seasonal effects
- Look for spatial patterns
- Read AI insights for quick understanding

### Tip 4: Data Quality
- Check for missing values (NaN)
- Verify coordinate systems
- Validate time ranges
- Compare with known patterns

### Tip 5: Sharing Results
- Take screenshots of visualizations
- Export time series data
- Document analysis parameters
- Save insights text

---

## Common Patterns

### Pattern 1: Temperature Gradient
- Decreases from equator to poles
- ~0.5-1°C per degree latitude

### Pattern 2: Seasonal Cycle
- 6-month offset between hemispheres
- Amplitude varies with latitude

### Pattern 3: Continental Effect
- Larger temperature ranges inland
- Moderated temperatures near coasts

### Pattern 4: Precipitation Belts
- High near equator (ITCZ)
- Low at 30° latitude (deserts)
- Moderate at mid-latitudes

### Pattern 5: Climate Change Signal
- Arctic amplification (2-3x global average)
- Increased precipitation variability
- More frequent extremes

---

## Troubleshooting Examples

### Problem: No data showing
**Solution**: Check coordinate names match dataset

### Problem: Slow performance
**Solution**: Reduce time range or spatial extent

### Problem: Strange patterns
**Solution**: Verify units and coordinate system

### Problem: Missing time series
**Solution**: Ensure location is within data bounds

---

## Additional Resources

### Sample Datasets
- **NOAA NCEP Reanalysis**: Global atmospheric data
- **ERA5**: High-resolution climate reanalysis
- **CMIP6**: Climate model projections

### Learning Resources
- Xarray documentation: https://docs.xarray.dev
- Climate data guide: https://climatedataguide.ucar.edu
- NetCDF tutorial: https://www.unidata.ucar.edu/software/netcdf/

### Community
- Xarray discussions: https://github.com/pydata/xarray/discussions
- Streamlit forum: https://discuss.streamlit.io
- Climate data science: https://pangeo.io

---

**Happy Exploring! 🌍📊**

For more examples and updates, check the GitHub repository.
