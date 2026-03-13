"""
Installation verification script for PyClimaExplorer
Checks that all dependencies are properly installed
"""

import sys

def check_module(module_name, package_name=None):
    """Check if a module can be imported."""
    if package_name is None:
        package_name = module_name
    
    try:
        __import__(module_name)
        print(f"✅ {package_name} is installed")
        return True
    except ImportError:
        print(f"❌ {package_name} is NOT installed")
        return False

def main():
    print("="*60)
    print("  PyClimaExplorer - Installation Verification")
    print("="*60)
    print()
    
    # Check Python version
    print("Checking Python version...")
    version = sys.version_info
    print(f"Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ required")
        return False
    else:
        print("✅ Python version OK")
    
    print()
    print("Checking required packages...")
    print()
    
    # Check all required packages
    packages = [
        ('streamlit', 'Streamlit'),
        ('xarray', 'Xarray'),
        ('pandas', 'Pandas'),
        ('numpy', 'NumPy'),
        ('plotly', 'Plotly'),
        ('netCDF4', 'NetCDF4'),
        ('sklearn', 'Scikit-learn'),
    ]
    
    all_installed = True
    for module, name in packages:
        if not check_module(module, name):
            all_installed = False
    
    print()
    print("="*60)
    
    if all_installed:
        print("✅ All dependencies are installed!")
        print()
        print("You're ready to run PyClimaExplorer:")
        print("  streamlit run app.py")
        print()
        return True
    else:
        print("❌ Some dependencies are missing")
        print()
        print("Please install missing packages:")
        print("  pip install -r requirements.txt")
        print()
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
