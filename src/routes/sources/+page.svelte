<style>
  /* Shared pill-style box */
  .pill {
    background: rgb(9, 151, 179);
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 0.75rem;
    font-weight: 600;
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
    display: inline-flex;
    align-items: center;
    gap: 1rem;
    white-space: nowrap;
    transition: background 0.2s;
  }

  .top-bar {
    position: fixed;
    top: 1rem;
    left: 0;
    right: 0;
    z-index: 50;
    display: flex;
    align-items: center;
    justify-content: center;
    pointer-events: none; /* prevent overlap issues */
  }

  .toc-pill {
    pointer-events: auto; /* make it clickable */
  }

  /* Left controls container (home + data sources) */
  .left-controls {
    position: fixed;
    top: 1rem;
    left: 1rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
    z-index: 60;
  }

  .home-btn {
    background: rgba(169, 234, 248, 0.813);
    color: black;
    padding: 0.5rem 0.75rem;
    border-radius: 0.5rem;
    font-weight: 600;
    text-decoration: none;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    transition: background 0.2s;
  }

  .home-btn:hover {
    background: white;
  }

  .toc-links a {
    color: white;
    text-decoration: none;
    font-weight: 500;
    transition: color 0.2s;
  }

  .toc-links a:hover {
    color: #035c64;
  }

  /* Section styling */
  section {
    margin: 6rem auto;
    padding: 2rem;
    max-width: 800px;
    border-radius: 0.75rem;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
    background-color: #d4f6ff;
    line-height: 1.6;
  }

  section h1 {
    font-size: 1.6rem;
    margin-bottom: 1rem;
    color: #222;
    border-bottom: 2px solid #3b82f6;
    padding-bottom: 0.5rem;
  }

  section ul {
    list-style: none;
    padding: 0;
  }

  section li {
    margin-bottom: 1rem;
  }

  section a {
    color: #2563eb;
    text-decoration: underline;
  }

  section a:hover {
    color: #1d4ed8;
  }


</style>

<!-- Left side (Home + Data Sources) -->
<div class="left-controls">
  <a href="/" class="home-btn">← Home</a>
  <div class="pill">Data Sources</div>
</div>

<!-- Centered TOC -->
<div class="top-bar">
  <div class="pill toc-links toc-pill">
    <a href="#section1">Environmental Datasets</a>
    <a href="#section2">Research Papers</a>
    <a href="#section3">Code & UI Design</a>
    <a href="#section4">Miscellaneous</a>
  </div>
</div>

<!-- Sections -->
<section id="section1">
  <h1 style="font-weight: bold;">Environmental Datasets</h1>
  <ul>
    <li>
      <strong>NASA: MODIS Sea Surface Temperature</strong><br>
      <a href="https://podaac.jpl.nasa.gov/dataset/MUR-JPL-L4-GLOB-v4.1">https://podaac.jpl.nasa.gov/dataset/MUR-JPL-L4-GLOB-v4.1</a><br>
      JPL MUR MEaSUREs Level 4 Global Sea Surface Temperature data, used to identify potential shark habitats.
    </li>
  </ul>
  <ul>
    <li>
      <strong>NASA: Chlorophyll-a Concentration</strong><br>
      <a href="https://oceancolor.gsfc.nasa.gov/l3/">https://oceancolor.gsfc.nasa.gov/l3/</a><br>
      Global chlorophyll-a concentration data from MODIS-Aqua satellite, used to identify potential shark habitats.
    </li>
  </ul>
  <ul>
    <li>
      <strong>NASA: SMAP Sea Surface Salinity</strong><br>
      <a href="https://podaac.jpl.nasa.gov/dataset/SMAP_JPL_L3_SSS_CAP_8DAY-RUNNINGMEAN_V5">https://podaac.jpl.nasa.gov/dataset/SMAP_JPL_L3_SSS_CAP_8DAY-RUNNINGMEAN_V5</a><br>
      SMAP Level 3 Sea Surface Salinity data, used to identify potential shark habitats.
    </li>
  </ul>
  <ul>
    <li>
      <strong>NASA: Distance from Coast</strong><br>
      <a href="https://oceancolor.gsfc.nasa.gov/resources/docs/distfromcoast/">https://oceancolor.gsfc.nasa.gov/resources/docs/distfromcoast/</a><br>
      Global distance from coast data, used to identify potential shark habitats.
    </li>
  </ul>
  <ul>
    <li>
      <strong>ESA COPERNICUS: Global Ocean Biogeochemistry</strong><br>
      <a href="https://data.marine.copernicus.eu/product/GLOBAL_MULTIYEAR_BGC_001_029/">https://data.marine.copernicus.eu/product/GLOBAL_MULTIYEAR_BGC_001_029/</a><br>
      Global Ocean Biogeochemistry data, including parameters like nitrate concentration, used to identify potential shark habitats.
    </li>
  </ul>
</section>

<section id="section2">
  <h1 style="font-weight: bold;">Research Papers</h1>
  <ul>
  <li>
  <p>R. Sun et al., “Global distribution prediction and ecological conservation of basking shark (Cetorhinus maximus) under integrated impacts,” Global Ecology and Conservation, p. e03310, Nov. 2024, doi: 10.1016/j.gecco.2024.e03310.</p>
  <br>
  <p>P. M. Yates, M. R. Heupel, A. J. Tobin, and C. A. Simpfendorfer, “Ecological Drivers of Shark Distributions along a Tropical Coastline,” PLoS ONE, vol. 10, no. 4, p. e0121346, Apr. 2015, doi: 10.1371/journal.pone.0121346.</p>
  <br>
  <p>P. Matich et al., “Long‐term effects of climate change on juvenile bull shark migratory patterns,” Journal of Animal Ecology, vol. 93, no. 10, pp. 1445–1461, Jul. 2024, doi: 10.1111/1365-2656.14140.</p>
  <br>
  <p>C. W. Bangley, L. Paramore, D. S. Shiffman, and R. A. Rulifson, “Increased Abundance and Nursery Habitat Use of the Bull Shark (Carcharhinus leucas) in Response to a Changing Environment in a Warm-Temperate Estuary,” Scientific Reports, vol. 8, no. 1, Apr. 2018, doi: 10.1038/s41598-018-24510-z.</p>
  <br>
  <p>J. Dziergwa et al., "Acid-base adjustments and first evidence of denticle corrosion caused by ocean acidification conditions in a demersal shark species," Sci. Rep., vol. 9, no. 1, art. 18668, Dec. 2019. <a href="https://doi.org/10.1038/s41598-019-54795-7" target="_blank">[Online]</a></p>
  <br>
  <p>J. C. A. Pistevos, I. Nagelkerken, T. Rossi, M. Olmos, and S. D. Connell, "Ocean acidification and global warming impair shark hunting behaviour and growth," Sci. Rep., vol. 5, art. 16293, Nov. 2015. <a href="https://doi.org/10.1038/srep16293" target="_blank">[Online]</a></p>
  <br>
  <p>B. D'Antonio, M. Meekan, L. C. Ferreira et al., "Salinity drives the distribution of a top-order predator, the tiger shark (Galeocerdo cuvier), in an inverse estuary," Sci. Rep., vol. 15, art. 9612, Mar. 2025. <a href="https://doi.org/10.1038/s41598-025-92272-6" target="_blank">[Online]</a></p>
  <br>
  <p>B. Worm et al., "Predator diversity hotspots in the blue ocean," Proc. Natl. Acad. Sci. U.S.A., vol. 100, no. 17, pp. 9884-9888, Aug. 2003. <a href="https://doi.org/10.1073/pnas.1333941100" target="_blank">[Online]</a></p>
  <br>
  <p>I. A. Bouyoucos et al., "Thermal tolerance and hypoxia tolerance are associated in blacktip reef shark (Carcharhinus melanopterus) neonates," J. Exp. Biol., vol. 223, no. 14, art. jeb221937, Jul. 2020. <a href="https://doi.org/10.1242/jeb.221937" target="_blank">[Online]</a></p>
  <br>
  <p>C. R. Wheeler, B. J. Lang, J. W. Mandelman, and J. L. Rummer, "The upper thermal limit of epaulette sharks (Hemiscyllium ocellatum) is conserved across three life history stages, sex and body size," Conserv. Physiol., vol. 10, no. 1, art. coac074, Jan. 2022. <a href="https://doi.org/10.1093/conphys/coac074" target="_blank">[Online]</a></p>
  <br>
  <p>A. M. Schlaff, M. R. Heupel, and C. A. Simpfendorfer, "Influence of environmental variables on shark and ray movement, behaviour and habitat use: a review," Rev. Fish Biol. Fish., vol. 24, no. 4, pp. 1089-1103, Dec. 2014. <a href="https://doi.org/10.1007/s11160-014-9364-8" target="_blank">[Online]</a></p>
  <br>
  <p>J. M. Gardiner, J. Atema, R. E. Hueter, and P. J. Motta, "Multisensory integration and behavioral plasticity in sharks from different ecological niches," PLoS ONE, vol. 7, no. 4, art. e93036, Apr. 2012. <a href="https://doi.org/10.1371/journal.pone.0093036" target="_blank">[Online]</a></p>
  <br>
  <p>R. L. Cramp et al., "Osmoregulation by juvenile brown-banded bamboo sharks, Chiloscyllium punctatum, in hypo- and hyper-saline waters," Comp. Biochem. Physiol. A Mol. Integr. Physiol., vol. 185, pp. 107-114, Jul. 2015. <a href="https://doi.org/10.1016/j.cbpa.2015.04.001" target="_blank">[Online]</a></p>
  <br>
  <p>R. D. Pillans, C. E. Franklin, and J. W. Tibbetts, "Plasma osmolyte concentrations and rectal gland mass of bull sharks Carcharhinus leucas, captured along a salinity gradient," Comp. Biochem. Physiol. A Mol. Integr. Physiol., vol. 138, no. 3, pp. 363-371, Jul. 2005. <a href="https://doi.org/10.1016/j.cbpb.2004.05.006" target="_blank">[Online]</a></p>
  <br>
  <p>B. A. Block et al., "Tracking apex marine predator movements in a dynamic ocean," Nature, vol. 475, no. 7354, pp. 86-90, Jul. 2011. <a href="https://doi.org/10.1038/nature10082" target="_blank">[Online]</a></p>
  <br>
  <p>M. R. Heupel, J. K. Carlson, and C. A. Simpfendorfer, "Shark nursery areas: concepts, definition, characterization and assumptions," Mar. Ecol. Prog. Ser., vol. 337, pp. 287-297, May 2007. <a href="https://doi.org/10.3354/meps337287" target="_blank">[Online]</a></p>
  <br>
  <p>C. W. Speed, M. G. Meekan, and C. J. A. Bradshaw, "Reef shark movements between foraging and resting areas," Mar. Ecol. Prog. Ser., vol. 416, pp. 261-276, Oct. 2010. <a href="https://doi.org/10.3354/meps08763" target="_blank">[Online]</a></p>
  <br>
  <p>R. W. Dwyer et al., "Niche partitioning between river shark species is driven by seasonal fluctuations in environmental salinity," Funct. Ecol., vol. 34, no. 10, pp. 2170-2185, Oct. 2020. <a href="https://doi.org/10.1111/1365-2435.12423" target="_blank">[Online]</a></p>
  <br>
  <p>C. Jennings de Jong et al., "Global distribution prediction and ecological conservation of basking shark (Cetorhinus maximus) under integrated impacts," Glob. Ecol. Conserv., vol. 55, art. e03238, Nov. 2024. <a href="https://doi.org/10.1016/j.gecco.2024.e03238" target="_blank">[Online]</a></p>
  <br>
  <p>National Centers for Environmental Information, "Seafloor Mapping," NOAA. <a href="https://www.ncei.noaa.gov/products/seafloor-mapping" target="_blank">[Online]</a>. [Accessed: Oct. 5, 2025].</p>
  </li>
  </ul>
</section>

<section id="section3">
  <h1 style="font-weight: bold;">Code & UI Design</h1>
  <ul>
    <li>
      <strong>Svelte MapLibre Library</strong><br>
      <a href="https://github.com/MIERUNE/svelte-maplibre-gl">https://github.com/MIERUNE/svelte-maplibre-gl</a><br>
      A Svelte wrapper for MapLibre GL JS, utilized as the basis of the interactive maps.
    </li>
  </ul>
  <ul>
    <li>
      <strong>Svelte MapLibre GL Examples</strong><br>
      <a href="https://svelte-maplibre-gl.mierune.dev/examples/plain">https://svelte-maplibre-gl.mierune.dev/examples/plain</a><br>
      A list of basic examples depicting Svelte MapLibre GL usage, used as a reference for developing both maps.
    </li>
  </ul>
</section>

<section id="section4">
  <h1 style="font-weight: bold;">Miscellaneous</h1>
  <ul>
    <li>
      <strong>Slidesgo Sharks Template</strong><br>
      <a href="https://slidesgo.com/theme/stop-shark-massacre">https://slidesgo.com/theme/stop-shark-massacre</a><br>
      Shark-themed presentation template used for the pitch deck and webapp homepage branding.
    </li>

  </ul>
</section>
