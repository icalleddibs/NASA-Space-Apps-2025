import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import os

min_pH = 7.75
max_pH = 7.8
exp_alpha = 10
min_sal = 37
max_sal = 40

##Loading data
#Hardcoding for now
pH_data = xr.open_dataset('./data/acidity/ocean_ph.nc', engine='netcdf4')
chl_data = xr.open_dataset('./data/chlorophyll/AQUA_MODIS.20020704_20250228.L3m.CU.CHL.chlor_a.9km.nc', engine='netcdf4')
salinity_data = xr.open_dataset('./data/salinity/SMAP_L3_SSS_20240625_8DAYS_V5.0.nc', engine='netcdf4')
sst_data = xr.open_dataset('./data/sst/20240629090000-JPL-L4_GHRSST-SSTfnd-MUR-GLOB-v02.0-fv04.1.nc', engine='netcdf4')

##Mask applications with simple downsampling
# Apply mask to pH data (7.8+ → 0, 7.75- → 1, linear in between)
#This is empirically chosen from papers
# pH - already at 0.25°
pH_masked = np.clip((pH_data['ph'][0, 0] - min_pH) / (max_pH - min_pH), 0, 1)


# Exponential mask (min → 0, max → 1)
# Chlorophyll - downsample by ~6x (4km to ~0.25°)
chl = chl_data['chlor_a'][::6, ::6]
chl_masked = ((chl - chl.min()) / (chl.max() - chl.min())) ** exp_alpha

# Binary mask (37-40 → 1, outside → 0)
# Salinity - already at 0.25° (select first time if needed)
sss = salinity_data['smap_sss']
if len(sss.shape) == 3:  # Has time dimension
    sss = sss[0, :, :]
sss_masked = ((sss >= min_sal) & (sss <= max_sal)).astype(int)

#No acual masking as anomlay product already exists
# SST - downsample by 25x (0.01° to 0.25°)
sst_anom = sst_data['sst_anomaly'][0, ::25, ::25]
sst_masked = (sst_anom - sst_anom.min()) / (sst_anom.max() - sst_anom.min())

# Check shapes
print("pH shape:", pH_masked.shape)
print("Chl shape:", chl_masked.shape)
print("SSS shape:", sss_masked.shape)
print("SST shape:", sst_masked.shape)

# Plot
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

axes[0, 0].imshow(pH_masked, cmap='Blues', aspect='auto', origin='lower')
axes[0, 0].set_title('Ocean pH Mask')

axes[0, 1].imshow(chl_masked, cmap='Greens', aspect='auto', origin='lower')
axes[0, 1].set_title('Chlorophyll Mask')

axes[1, 0].imshow(sss_masked, cmap='Blues', aspect='auto', origin='lower')
axes[1, 0].set_title('Salinity Mask (37-40 PSU)')

axes[1, 1].imshow(sst_masked, cmap='Reds', aspect='auto', origin='lower')
axes[1, 1].set_title('SST Anomaly Mask')

plt.tight_layout()
plt.savefig('ocean_masks_all.png', dpi=150, bbox_inches='tight')
plt.show()
