# 🏗️ PyClimaExplorer - Architecture Documentation

## System Overview

PyClimaExplorer is a modular web application built with Streamlit that provides interactive visualization and analysis of climate data stored in NetCDF format.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        User Interface                        │
│                      (Streamlit Web App)                     │
│                          app.py                              │
└────────────────────────┬────────────────────────────────────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
         ▼               ▼               ▼
┌────────────────┐ ┌──────────────┐ ┌──────────────┐
│  Data Loader   │ │Visualization │ │   Analysis   │
│  data_loader.py│ │visualization │ │  analysis.py │
│                │ │     .py      │ │              │
└────────┬───────┘ └──────┬───────┘ └──────┬───────┘
         │                │                │
         │                │                │
         ▼                ▼                ▼
┌────────────────────────────────────────────────────┐
│              External Libraries                     │
│  Xarray | Pandas | NumPy | Plotly | Scikit-learn  │
└────────────────────────────────────────────────────┘
         │
         ▼
┌────────────────────────────────────────────────────┐
│              NetCDF Data Files                      │
│         (.nc climate datasets)                      │
└────────────────────────────────────────────────────┘
```

## Component Details

### 1. User Interface Layer (app.py)

**Responsibility**: Main application logic and UI rendering

**Key Features**:
- Streamlit page configuration and theming
- Session state management
- Sidebar controls (upload, variable selection, time range, location)
- Main panel visualizations
- Mode switching (Single Period vs Comparison)

**Data Flow**:
1. User uploads NetCDF file → Stored in session state
2. User selects parameters → Passed to utility functions
3. Utility functions return processed data/figures → Rendered in UI

**Session State Variables**:
- `dataset`: Loaded xarray Dataset object
- `uploaded_file`: Reference to uploaded file

### 2. Data Loader Module (utils/data_loader.py)

**Responsibility**: NetCDF file handling and data extraction

**Functions**:

```python
load_netcdf(uploaded_file)
├─ Saves uploaded file to temp location
├─ Opens with xarray
└─ Returns Dataset object

get_variables(dataset)
├─ Filters coordinate variables
├─ Identifies climate variables
└─ Returns list of variable names

get_time_range(dataset)
├─ Searches for time dimension
├─ Extracts time values
└─ Returns time array

get_spatial_bounds(dataset)
├─ Identifies lat/lon coordinates
├─ Calculates min/max bounds
└─ Returns bounds dictionary

extract_point_timeseries(dataset, variable, lat, lon)
├─ Selects nearest point to coordinates
├─ Extracts time series
└─ Returns DataArray
```

**Design Patterns**:
- Flexible coordinate name matching (handles 'lat', 'latitude', 'LAT', etc.)
- Graceful fallback to defaults if coordinates not found
- Error handling with descriptive messages

### 3. Visualization Module (utils/visualization.py)

**Responsibility**: Creating interactive Plotly visualizations

**Functions**:

```python
create_heatmap(data_array, variable_name, title)
├─ Calculates temporal mean
├─ Creates Plotly Heatmap
├─ Applies dark theme styling
└─ Returns Figure object

create_timeseries(dataset, variable, lat, lon, start, end)
├─ Extracts point data
├─ Filters by time range
├─ Adds trend line
├─ Creates Plotly Scatter
└─ Returns Figure object

create_comparison_heatmap(data1, data2, variable_name)
├─ Calculates means for both periods
├─ Computes difference
├─ Creates diverging colorscale heatmap
└─ Returns Figure object
```

**Visualization Features**:
- Interactive hover tooltips
- Zoom and pan capabilities
- Dark theme consistency
- Responsive layouts
- Color scales optimized for climate data

### 4. Analysis Module (utils/analysis.py)

**Responsibility**: Statistical analysis and predictions

**Functions**:

```python
calculate_statistics(data_array)
├─ Computes mean, min, max, std, median
├─ Handles NaN values
└─ Returns statistics dictionary

generate_insights(dataset, variable, lat, lon, start, end)
├─ Extracts point data
├─ Calculates trend
├─ Detects anomalies
├─ Generates text insights
└─ Returns formatted string

predict_future_trend(dataset, variable, lat, lon, start, end)
├─ Extracts historical data
├─ Fits linear regression model
├─ Generates future predictions
├─ Creates visualization with forecast
└─ Returns Figure object
```

**Analysis Techniques**:
- Linear regression for trend detection
- Standard deviation for anomaly detection
- Percentage change calculations
- Time series decomposition

## Data Flow

### Upload and Load Flow
```
User Upload → Streamlit File Uploader → Temp File → Xarray → Session State
```

### Visualization Flow
```
Session State Dataset → Data Loader (extract) → Visualization Module → Plotly Figure → Streamlit Display
```

### Analysis Flow
```
Session State Dataset → Data Loader (extract) → Analysis Module → Statistics/Insights → UI Display
```

## Technology Stack Details

### Core Technologies

**Streamlit (1.31.0)**
- Purpose: Web framework
- Why: Rapid prototyping, built-in widgets, easy deployment
- Usage: UI rendering, state management, file uploads

**Xarray (2024.1.1)**
- Purpose: NetCDF data handling
- Why: Native NetCDF support, labeled arrays, lazy loading
- Usage: Loading datasets, coordinate selection, slicing

**Plotly (5.18.0)**
- Purpose: Interactive visualizations
- Why: Web-native, interactive, beautiful defaults
- Usage: Heatmaps, time series, comparison charts

**Pandas (2.2.0)**
- Purpose: Data manipulation
- Why: Easy time series handling, DataFrame operations
- Usage: Converting xarray to tabular format

**NumPy (1.26.3)**
- Purpose: Numerical operations
- Why: Fast array operations, mathematical functions
- Usage: Statistical calculations, array manipulations

**Scikit-learn (1.4.0)**
- Purpose: Machine learning
- Why: Simple regression models, well-documented
- Usage: Linear regression for trend prediction

**NetCDF4 (1.6.5)**
- Purpose: NetCDF file format support
- Why: Required backend for xarray
- Usage: Low-level NetCDF operations

## Design Decisions

### 1. Modular Architecture
**Decision**: Separate concerns into utils modules
**Rationale**: 
- Easier testing and maintenance
- Reusable components
- Clear separation of responsibilities

### 2. Session State for Data
**Decision**: Store dataset in Streamlit session state
**Rationale**:
- Avoid reloading on every interaction
- Faster user experience
- Persistent across widget updates

### 3. Dark Theme
**Decision**: Default dark theme with cyan accents
**Rationale**:
- Reduces eye strain for data analysis
- Modern aesthetic
- Better contrast for visualizations

### 4. Lazy Loading
**Decision**: Use xarray's lazy loading capabilities
**Rationale**:
- Handle large datasets efficiently
- Load only needed data
- Reduce memory footprint

### 5. Flexible Coordinate Matching
**Decision**: Support multiple coordinate name conventions
**Rationale**:
- Different data sources use different conventions
- Improves compatibility
- Better user experience

## Performance Considerations

### Optimization Strategies

1. **Lazy Loading**: Xarray loads data on-demand
2. **Temporal Averaging**: Heatmaps use time-averaged data
3. **Nearest Neighbor Selection**: Fast point selection
4. **Caching**: Streamlit's built-in caching (can be added)
5. **Chunking**: Large datasets can be chunked

### Scalability Limits

- **File Size**: Recommended < 500MB (configurable)
- **Time Steps**: Optimal < 1000 time points
- **Spatial Resolution**: Works well up to 0.25° resolution
- **Memory**: Depends on available RAM

## Extension Points

### Adding New Visualizations
1. Create function in `utils/visualization.py`
2. Follow Plotly dark theme pattern
3. Add to `app.py` main panel

### Adding New Analysis Methods
1. Create function in `utils/analysis.py`
2. Return formatted results
3. Display in UI with appropriate widget

### Supporting New Data Formats
1. Add loader function in `utils/data_loader.py`
2. Convert to xarray Dataset
3. Ensure coordinate compatibility

### Custom Themes
1. Modify CSS in `app.py`
2. Update Plotly theme in visualization functions
3. Adjust `.streamlit/config.toml`

## Security Considerations

1. **File Upload**: Limited to .nc files, size restricted
2. **Temp Files**: Cleaned up after loading
3. **Input Validation**: Coordinate bounds checked
4. **No Code Execution**: Pure data processing
5. **XSRF Protection**: Enabled in Streamlit config

## Testing Strategy

### Unit Tests (Recommended)
```python
# Test data loading
test_load_netcdf()
test_get_variables()
test_get_time_range()

# Test visualizations
test_create_heatmap()
test_create_timeseries()

# Test analysis
test_calculate_statistics()
test_generate_insights()
```

### Integration Tests
- Upload sample file → Verify loading
- Select parameters → Verify visualizations render
- Switch modes → Verify state persistence

### Manual Testing
- Test with various NetCDF formats
- Test with different coordinate conventions
- Test with edge cases (single time step, missing data)

## Deployment Options

### Local Development
```bash
streamlit run app.py
```

### Streamlit Cloud
1. Push to GitHub
2. Connect to Streamlit Cloud
3. Deploy from repository

### Docker
```dockerfile
FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

### Heroku
- Add `Procfile`: `web: streamlit run app.py`
- Configure buildpack
- Deploy via Git

## Future Enhancements

### Potential Features
1. **Multi-file comparison**: Compare different datasets
2. **Export capabilities**: Download processed data
3. **Advanced statistics**: Correlation, EOF analysis
4. **Custom colormaps**: User-selectable color schemes
5. **Animation**: Temporal animations of climate variables
6. **3D visualizations**: Vertical profile plots
7. **Region selection**: Draw custom regions on map
8. **Batch processing**: Process multiple files
9. **API integration**: Direct download from climate APIs
10. **Collaborative features**: Share analysis sessions

## Maintenance

### Regular Updates
- Update dependencies quarterly
- Test with new Streamlit versions
- Monitor for security vulnerabilities
- Update sample data sources

### Code Quality
- Follow PEP 8 style guide
- Add type hints
- Maintain docstrings
- Keep functions focused and small

---

**Last Updated**: 2024
**Version**: 1.0.0
**Maintainer**: PyClimaExplorer Team
