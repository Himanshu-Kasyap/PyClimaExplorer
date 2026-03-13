"""
Setup script for PyClimaExplorer
Automates installation and initial setup
"""

import subprocess
import sys
import os

def print_header(text):
    """Print formatted header."""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60 + "\n")

def check_python_version():
    """Check if Python version is compatible."""
    print_header("Checking Python Version")
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Error: Python 3.8 or higher is required")
        print("   Please upgrade Python and try again")
        return False
    
    print("✅ Python version is compatible")
    return True

def install_dependencies():
    """Install required packages."""
    print_header("Installing Dependencies")
    
    try:
        print("Installing packages from requirements.txt...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("\n✅ All dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("\n❌ Error installing dependencies")
        print("   Try running manually: pip install -r requirements.txt")
        return False

def create_sample_data():
    """Generate sample climate data."""
    print_header("Creating Sample Data")
    
    response = input("Generate sample climate data? (y/n): ").lower()
    
    if response == 'y':
        try:
            print("\nGenerating sample dataset...")
            subprocess.check_call([sys.executable, "test_sample_data.py"])
            print("\n✅ Sample data created: sample_climate_data.nc")
            return True
        except subprocess.CalledProcessError:
            print("\n⚠️  Could not generate sample data")
            print("   You can run 'python test_sample_data.py' manually later")
            return False
    else:
        print("Skipping sample data generation")
        return True

def create_data_directory():
    """Create data directory if it doesn't exist."""
    if not os.path.exists('data'):
        os.makedirs('data')
        print("✅ Created data/ directory")

def print_next_steps():
    """Print instructions for next steps."""
    print_header("Setup Complete!")
    
    print("🎉 PyClimaExplorer is ready to use!\n")
    print("Next steps:")
    print("  1. Start the dashboard:")
    print("     streamlit run app.py\n")
    print("  2. Upload a NetCDF file or use sample_climate_data.nc\n")
    print("  3. Explore climate data with interactive visualizations!\n")
    print("📖 For detailed instructions, see:")
    print("   - QUICKSTART.md (5-minute guide)")
    print("   - README.md (full documentation)\n")
    print("🌍 Sample data sources:")
    print("   - NOAA: https://www.ncei.noaa.gov/data/")
    print("   - Copernicus: https://cds.climate.copernicus.eu/")
    print("   - NASA: https://earthdata.nasa.gov/\n")

def main():
    """Main setup function."""
    print("\n" + "🌍 " * 20)
    print("  PyClimaExplorer - Setup Script")
    print("🌍 " * 20)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Create data directory
    create_data_directory()
    
    # Create sample data
    create_sample_data()
    
    # Print next steps
    print_next_steps()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {str(e)}")
        sys.exit(1)
