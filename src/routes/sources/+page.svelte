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
      <strong>NOAA National Centers for Environmental Information (NCEI)</strong><br>
      <a href="https://www.ncei.noaa.gov/">https://www.ncei.noaa.gov/</a><br>
      A vast repository of environmental data including oceanographic, atmospheric, and climate datasets.
    </li>
  </ul>
</section>

<section id="section2">
  <h1 style="font-weight: bold;">Research Papers</h1>
  <ul>
    <li>
      <strong>NASA Technical Reports Server (NTRS)</strong><br>
      <a href="https://ntrs.nasa.gov/">https://ntrs.nasa.gov/</a><br>
      A vast collection of NASA's scientific and technical information, including research papers and reports.
    </li>
  </ul>
</section>

<section id="section3">
  <h1 style="font-weight: bold;">Code & UI Design</h1>
  <ul>
    <li>
      <strong>NASA GitHub</strong><br>
      <a href="https://github.com/nasa">https://github.com/nasa</a><br>
      A collection of open-source software projects developed by NASA.
    </li>
  </ul>
</section>

<section id="section4">
  <h1 style="font-weight: bold;">Miscellaneous</h1>
  <ul>
    <li>
      <strong>NASA Open Data Portal</strong><br>
      <a href="https://data.nasa.gov/">https://data.nasa.gov/</a><br>
      A comprehensive collection of datasets provided by NASA, covering a wide range of scientific topics.
    </li>

  </ul>
</section>
