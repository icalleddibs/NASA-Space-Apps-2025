"""
Ocean data fetcher
Fetches sea surface salinity, temperature, ocean acidity, and chlorophyll data
Currently using NASA earthaccess
##TODO: Add SWOT access
"""
import earthaccess
import xarray as xr
from datetime import datetime
import copernicusmarine
import logging
import os


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ocean_data_fetch.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Create all data directories
os.makedirs("./data/sst", exist_ok=True)
os.makedirs("./data/chlorophyll", exist_ok=True)
os.makedirs("./data/salinity", exist_ok=True)
os.makedirs("./data/acidity", exist_ok=True)
os.makedirs("./data/turbidity", exist_ok=True)

# Authenticate with NASA Earthdata
logger.info("Authenticating with NASA Earthdata...")
earthaccess.login()

# Define date range
start_date = "2024-01-01"
end_date = "2024-12-31"

# Define bounding box - [min_lon, min_lat, max_lon, max_lat]
bbox = [-128, -60, 68, 58]
#bbox = [-180, -90, 180, 90]  # Whole Earth

logger.info("Searching for datasets...")
logger.info(f"Date range: {start_date} to {end_date}")
logger.info(f"Bounding box: {bbox}")

# 1. SEA SURFACE TEMPERATURE (SST)
# Using GHRSST Level 4 MUR Global Foundation SST (0.01 degree resolution)
logger.info("=" * 50)
logger.info("SEA SURFACE TEMPERATURE")
logger.info("=" * 50)
sst_results = earthaccess.search_data(
    short_name='MUR-JPL-L4-GLOB-v4.1',
    temporal=(start_date, end_date),
)
logger.info(f"Found {len(sst_results)} SST granules")

# 2. CHLOROPHYLL CONCENTRATION
# Using MODIS Aqua Level 3 (4km resolution)
logger.info("=" * 50)
logger.info("CHLOROPHYLL CONCENTRATION")
logger.info("=" * 50)
chl_results = earthaccess.search_data(
    short_name='MODISA_L3m_CHL',
    temporal=(start_date, end_date),
)
logger.info(f"Found {len(chl_results)} Chlorophyll granules")

# 3. SEA SURFACE SALINITY (SSS)
# Using SMAP Level 3 (0.25 degree resolution)
logger.info("=" * 50)
logger.info("SEA SURFACE SALINITY")
logger.info("=" * 50)
sss_results = earthaccess.search_data(
    short_name='SMAP_JPL_L3_SSS_CAP_8DAY-RUNNINGMEAN_V5',
    temporal=(start_date, end_date),
)
logger.info(f"Found {len(sss_results)} SSS granules")

# 4. OCEAN ACIDITY (pH) from CMEMS
# Using Global Ocean Biogeochemistry model (0.25 degree resolution)
logger.info("=" * 50)
logger.info("OCEAN ACIDITY (pH)")
logger.info("=" * 50)
logger.info("Downloading pH data from CMEMS...")

# Get CMEMS credentials
cmems_username = input("Enter your Copernicus username: ")
cmems_password = input("Enter your Copernicus password: ")

try:
    copernicusmarine.subset(
        # This dataset is only have monthly, pH not in more frequent data
        # Only available for 2022 onwards
        dataset_id="cmems_mod_glo_bgc_myint_0.25deg_P1M-m",  
        variables=["ph"],
        start_datetime=start_date + "T00:00:00",
        end_datetime=end_date + "T23:59:59",
        minimum_longitude=bbox[0],
        maximum_longitude=bbox[2],
        minimum_latitude=bbox[1],
        maximum_latitude=bbox[3],
        output_filename="./data/acidity/ocean_ph.nc",
        username=cmems_username,
        password=cmems_password,
    )
    logger.info("Downloaded pH data to: ./data/acidity/ocean_ph.nc")
except Exception as e:
    logger.error(f"Failed to download pH data: {e}")

# 5. TURBIDITY (via Kd_490)
# Using derived diffusivity parameter from MODIS and VIIRS
logger.info("=" * 50)
logger.info("TURBIDITY (Kd_490)")
logger.info("=" * 50)
kd_results = earthaccess.search_data(
    short_name='MODISA_L3m_KD',
    temporal=(start_date, end_date),
)
logger.info(f"Found {len(kd_results)} Turbidity granules")

# Download SST
if sst_results:
    logger.info("Downloading SST data...")
    sst_files = earthaccess.download(sst_results[0], "./data/sst")
    logger.info(f"Downloaded to: {sst_files}")
else:
    logger.warning("No SST results found to download")

# Download Chlorophyll
if chl_results:
    logger.info("Downloading Chlorophyll data...")
    chl_files = earthaccess.download(chl_results[0], "./data/chlorophyll")
    logger.info(f"Downloaded to: {chl_files}")
else:
    logger.warning("No Chlorophyll results found to download")

# Download SSS
if sss_results:
    logger.info("Downloading SSS data...")
    sss_files = earthaccess.download(sss_results[0], "./data/salinity")
    logger.info(f"Downloaded to: {sss_files}")
else:
    logger.warning("No SSS results found to download")

# Download Turbidity (Fixed: was checking sss_results instead of kd_results)
if kd_results:
    logger.info("Downloading Turbidity (via Kd) data...")
    kd_files = earthaccess.download(kd_results[0], "./data/turbidity")
    logger.info(f"Downloaded to: {kd_files}")
else:
    logger.warning("No Turbidity results found to download")

logger.info("=" * 50)
logger.info("COMPLETE!")
logger.info("=" * 50)
