from setuptools import setup, find_namespace_packages
from tethys_apps.app_installation import find_all_resource_files
from tethys_apps.base.app_base import TethysAppBase

# -- Apps Definition -- #
app_package = 'national_water_level_forecast_ecuador'
release_package = f'{TethysAppBase.package_namespace}-{app_package}'

# -- Python Dependencies -- #
dependencies = []

# -- Get Resource File -- #
resource_files = find_all_resource_files(app_package, TethysAppBase.package_namespace)


setup(
    name=release_package,
    version='2.0',
    description='This app uses the Bias Correction, the GESS forecast, and the observed water level to create a  National Hydrological Forecast Model in Ecuador.',
    long_description='',
    keywords='"Hydrology", "Time Series", "Bias Correction", "Hydrostats", "GEOGloWS", "Water Level", "Ecuador"',
    author='Darlly Judith Rojas-Lesmes, Jorge Luis Sanchez-Lozano, Karina Larco, Juseth E. Chancay',
    author_email='djrojasl@unal.edu.co, jorgessanchez7@gmail.com, karynina3@gmail.com, juseth.chancay@gmail.com',
    url='',
    license='',
    packages=find_namespace_packages(),
    package_data={'': resource_files},
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
)