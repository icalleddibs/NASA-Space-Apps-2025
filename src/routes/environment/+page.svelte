<style>
  /* Shared pill-style box */
  .pill {
    background: #ffa2a2;
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
    background: #ffc5c5;
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
    color: #eb3535;
  }

  /* Section styling */
  section {
    margin: 6rem auto;
    padding: 2rem;
    max-width: 800px;
    border-radius: 0.75rem;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
    background-color: #fcdcdc;
    line-height: 1.6;
  }

  section h1 {
    font-size: 1.6rem;
    margin-bottom: 1rem;
    color: #222;
    border-bottom: 2px solid #f86868;
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
    color: #eb5959;
    text-decoration: underline;
  }

  section a:hover {
    color: #1d4ed8;
  }

  body {
    padding-bottom: 4rem;
  }
</style>

<!-- Left side (Home + Data Sources) -->
<div class="left-controls">
  <a href="/" class="home-btn">← Home</a>
  <div class="pill">Environmental Factors</div>
</div>

<!-- Centered TOC -->
<div class="top-bar">
  <div class="pill toc-links toc-pill">
    <a href="#section1">Purpose</a>
    <a href="#section2">Acidity</a>
    <a href="#section3">Chlorophyll</a>
    <a href="#section4">Salinity</a>
    <a href="#section5">Temperature</a>
    <a href="#section6">Turbidity</a>
  </div>
</div>

<!-- Sections -->
<section id="section1">
  <h1 style="font-weight: bold;">Habitability Map Purpose</h1>
  <ul>
   This map measures the relevant oceanographic factors for a habitat to be suitable to sharks. 
   Higher values indicate better suitability for sharks, while lower values mean the area is less comfortable for sharks. 
   This is not a direct map of the oceanographic values, but rather an estimate of how close those values are to ideal conditions 
   for a shark to live in. The datasets used for these estimations are collected by NASA and ESA satellites, providing very 
   frequent data to predict shark habitat change in near-real-time.
  </ul>
</section>

<section id="section2">
  <h1 style="font-weight: bold;">Acidity</h1>
  <ul>
    pH (Acidity) measures the acidity/alkalinity of seawater on a logarithmic scale from 0-14, with lower values being more acidic. 
    Most sharks prefer slightly basic seawater (pH 8.1) and can physiologically compensate for changes to the ocean’s pH, but at 
    extreme values (pH less than 7.8) they may experience denticle corrosion, reduced hunting ability, and metabolic stress (Dziergwa et al., 2019).
    Here, conditions are more suitable for sharks when pH is higher, with a high penalty for areas that may have acidification 
    from industrial sources (Dziergwa et al., 2019, Pistevos et al., 2015).Data source:CMEMS biogeochemical model (not satellite-based).
  </ul>
</section>

<section id="section3">
  <h1 style="font-weight: bold;">Chlorophyll</h1>
  <ul>
    Chlorophyll-a concentration measures phytoplankton abundance in mg/m³, indicating ocean productivity and food web health. As sharks 
    are predators, they exist in higher numbers in areas where there is more prey, who in turn exist where there are more plants to eat 
    (Worm et al., 2003; Block et al., 2011). Here, we emphasize how important this parameter is for shark feeding zones by designating highly 
    productive areas (top 10% by km²) as hotspots. Data source: Aqua MODIS.
  </ul>
</section>

<section id="section4">
  <h1 style="font-weight: bold;">Salinity</h1>
  <ul>
    Salinity measures the salt concentration in seawater, typically expressed in Practical Salinity Units (PSU). Sharks are strenohaline, 
    meaning they can only survive in very narrow ranges of salinity, with ranges being unique to each species (D’Antonio et al., 2015).  
    Additionally, sharks who live closer to the coastline are less affected by changes in salinity, as they are adapted to live in environments
    with more freshwater from rain and river outflow. Here, areas are deemed suitable if the salinity range is between 35 PSU and 40 PSU 
    (Pillans et al., 2008; Cramp et al., 2015), with deviations from this range becoming more important further from the coasts.
    Data source: SMAP satellite.
  </ul>
</section>

<section id="section5">
  <h1 style="font-weight: bold;">Temperature</h1>
  <ul>
    Each shark species has a different range of temperatures in which they are comfortable, from warm oceans for tropical reef sharks 
    to freezing temperatures for greenland sharks. Sharks are known to migrate to warmer areas within their comfortable range, as these 
    may indicate upwelling zones where prey congregate, but extreme temperatures may stress their bodies (Bouyoucos et al., 2020; Wheeler et
     al., 2022). This layer looks at the anomaly of sea surface temperature (SST), which indicates changes from average regional temperature.
      We map habitability by emphasizing zones which are a bit warmer than the surroundings (+2°C above local mean) and penalizing areas with 
      extreme values (±10°C). Data source: Multi-satellite (MODIS/Aqua+Terra, VIIRS, AVHRR, AMSR2).
  </ul>
</section>

<section id="section6">
  <h1 style="font-weight: bold;">Turbidity</h1>
  <ul>
    Turbidity is a measure of how murky the water is and how many suspended particles are in it, measured through a parameter called the
     diffuse attenuation coefficient Kd. Sharks rely heavily on vision and electroreception for hunting, so moderate turbidity near coasts 
     can indicate productive estuaries, but excessive turbidity impairs sensory functions (Gardiner et al., 2012; Schlaff et al., 2014). 
     Further from the shore, this is a less significant factor, so moderate turbidities in proximity to coastlines were emphasized in the 
     habitability estimate. Data source: Aqua MODIS.
  </ul>
</section>