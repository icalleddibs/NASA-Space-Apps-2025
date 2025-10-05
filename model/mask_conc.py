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


##Mask applications
# Apply mask to pH data (7.8+ → 0, 7.75- → 1, linear in between)
#This is empirically chosen from papers
pH_masked = np.clip((pH_data['ph'][0][0] - min_pH) / (max_pH - min_pH), 0, 1)


# Exponential mask (min → 0, max → 1)
chl = chl_data['chlor_a']
chl_masked = ((chl - chl.min()) / (chl.max() - chl.min())) ** exp_alpha

# Binary mask (37-40 → 1, outside → 0)
sss = salinity_data['smap_sss']  
sss_masked = ((sss >= min_sal) & (sss <= max_sal)).astype(int)


# Check coordinate ranges
print("pH lat range:", pH_masked.latitude.min().values, "to", pH_masked.latitude.max().values)
print("Chl lat range:", chl_masked.lat.min().values, "to", chl_masked.lat.max().values)
print("SSS lat range:", sss_masked.latitude.min().values, "to", sss_masked.latitude.max().values)

# Plot with explicit imshow
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].imshow(pH_masked, cmap='Blues', aspect='auto', origin = 'lower')
axes[0].set_title('Ocean pH Mask')

axes[1].imshow(chl_masked, cmap='Blues', aspect='auto')
axes[1].set_title('Chlorophyll Mask')

axes[2].imshow(sss_masked, cmap='Blues', aspect='auto')
axes[2].set_title('Salinity Mask (37-40 PSU)')

plt.tight_layout()
plt.savefig('ocean_masks.png', dpi=150, bbox_inches='tight')
plt.show()
