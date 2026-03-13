import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from utils.data_loader import extract_point_timeseries

def calculate_statistics(data_array):
    """Calculate basic statistics for a data array."""
    return {
        'mean': float(data_array.mean(skipna=True).values),
        'min': float(data_array.min(skipna=True).values),
        'max': float(data_array.max(skipna=True).values),
        'std': float(data_array.std(skipna=True).values),
        'median': float(data_array.median(skipna=True).values)
    }

def generate_insights(dataset, variable, lat, lon, start_time, end_time):
    """Generate AI-powered insights from the data."""
    # Extract point data
    point_data = extract_point_timeseries(dataset, variable, lat, lon)
    point_data = point_data.sel(time=slice(start_time, end_time))
    
    # Convert to array
    values = point_data.values
    
    # Calculate statistics
    mean_val = np.nanmean(values)
    std_val = np.nanstd(values)
    trend = np.polyfit(range(len(values)), values, 1)[0] if len(values) > 1 else 0
    
    # Calculate change
    if len(values) > 1:
        first_half = values[:len(values)//2]
        second_half = values[len(values)//2:]
        change = np.nanmean(second_half) - np.nanmean(first_half)
        percent_change = (change / np.nanmean(first_half)) * 100 if np.nanmean(first_half) != 0 else 0
    else:
        change = 0
        percent_change = 0
    
    # Generate insight text
    insights = []
    
    insights.append(f"📍 Location: ({lat:.2f}°, {lon:.2f}°)")
    insights.append(f"📊 Average {variable}: {mean_val:.2f} (±{std_val:.2f})")
    
    if abs(trend) > 0.001:
        direction = "increasing" if trend > 0 else "decreasing"
        insights.append(f"📈 Trend: {variable} is {direction} at a rate of {abs(trend):.4f} per time step")
    else:
        insights.append(f"📊 Trend: {variable} remains relatively stable over the period")
    
    if abs(percent_change) > 1:
        direction = "increased" if change > 0 else "decreased"
        insights.append(f"🔄 Change: {variable} {direction} by {abs(change):.2f} ({abs(percent_change):.1f}%) between first and second half of the period")
    
    # Anomaly detection
    anomalies = np.sum(np.abs(values - mean_val) > 2 * std_val)
    if anomalies > 0:
        insights.append(f"⚠️ Detected {anomalies} anomalous values (>2σ from mean)")
    
    return "\n\n".join(insights)

def predict_future_trend(dataset, variable, lat, lon, start_time, end_time, forecast_steps=20):
    """Predict future trends using linear regression."""
    try:
        # Extract point data
        point_data = extract_point_timeseries(dataset, variable, lat, lon)
        point_data = point_data.sel(time=slice(start_time, end_time))
        
        # Convert to dataframe
        df = point_data.to_dataframe().reset_index()
        
        if len(df) < 3:
            return None
        
        # Prepare data for regression
        X = np.arange(len(df)).reshape(-1, 1)
        y = df[variable].values
        
        # Remove NaN values
        mask = ~np.isnan(y)
        X = X[mask]
        y = y[mask]
        
        if len(X) < 3:
            return None
        
        # Fit model
        model = LinearRegression()
        model.fit(X, y)
        
        # Make predictions
        future_X = np.arange(len(df), len(df) + forecast_steps).reshape(-1, 1)
        future_y = model.predict(future_X)
        
        # Create figure
        fig = go.Figure()
        
        # Historical data
        fig.add_trace(go.Scatter(
            x=df['time'],
            y=df[variable],
            mode='lines+markers',
            name='Historical',
            line=dict(color='#00d4ff', width=2),
            marker=dict(size=4)
        ))
        
        # Fitted line
        fitted_y = model.predict(X)
        fig.add_trace(go.Scatter(
            x=df['time'].iloc[mask],
            y=fitted_y,
            mode='lines',
            name='Fitted',
            line=dict(color='#ffd700', width=2, dash='dash')
        ))
        
        # Future prediction
        last_time = df['time'].iloc[-1]
        time_delta = df['time'].iloc[-1] - df['time'].iloc[-2] if len(df) > 1 else pd.Timedelta(days=1)
        future_times = pd.date_range(start=last_time + time_delta, periods=forecast_steps, freq=time_delta)
        
        fig.add_trace(go.Scatter(
            x=future_times,
            y=future_y,
            mode='lines+markers',
            name='Forecast',
            line=dict(color='#ff6b6b', width=2, dash='dot'),
            marker=dict(size=4)
        ))
        
        fig.update_layout(
            title=f'{variable} - Future Trend Prediction',
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
    
    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        return None
