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

  section h2 {
    font-size: 1.25rem;
    margin-bottom: 1rem;
    color: #222;
    border-bottom: 1px solid #3b82f6;
    padding-bottom: 0.5rem;
  }

  .photo-grid {
    display: grid;
    gap: 1rem;
  }

  .grid-2x2 {
    grid-template-columns: repeat(2, 1fr);
    max-width: 800px;
    margin: 2rem auto;
  }

  .grid-1x1 {
    max-width: 400px;
    margin: 2rem auto;
    text-align: center;
  }

  .grid-2side {
    grid-template-columns: repeat(2, 1fr);
    max-width: 800px;
    margin: 2rem auto;
  }

  .photo-card {
    background-color: #80cff7;
    padding: 1rem;
    border-radius: 0.75rem;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
    text-align: center;
  }

  .photo-card img {
    width: 100%;
    height: auto;
    border-radius: 0.5rem;
    margin-bottom: 0.5rem;
  }

  .caption {
    font-weight: 600;
    color: #222;
  }



/* Ordered lists */
ol {
  padding-left: 1.5rem; /* indent main list */
  margin-bottom: 1rem;
}

/* Nested ordered lists */
ol ol {
  padding-left: 1.5rem; /* extra indent for sublists */
  margin-top: 0.25rem;
}

/* List items */
li {
  margin: 0.5rem 0;
}

/* Links in lists */
a {
  color: #2563eb;
  text-decoration: underline;
}

a:hover {
  text-decoration: none;
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
    <a href="#section1">Overview</a>
    <a href="#section2">Our Prototype</a>
    <a href="#section3">Next Steps</a>
    <a href="#section4">Why It Matters</a>
  </div>
</div>

<!-- Sections -->
<section id="section1">
  <h1 style="font-weight: bold;">Shark Tag Hardware Development</h1>
  <ul>
Our goal is simple but ambitious: to develop a viable shark tag capable of collecting detailed, specimen-level data on shark behaviour, habitat conditions, and foraging patterns. This information directly supports our habitability model.
</ul>
<br>
<p> Our hardware aims to achieve two key functions:</p>
<ol>
  <li>1. Shark Telemetry: Tracks shark movements to reveal behaviour and foraging patterns.</li>
  <li>2. Habitat Conditions: Monitors environmental factors for habitability.</li>
</ol>

</section>

<section id="section2">
  <h1 style="font-weight: bold;">Our Prototype</h1>
  <ul>
    As part of NASA SpaceApps 2025, our mission was to validate the viability of this shark tag concept. We focused on prototyping and testing key instruments and sensors likely to make it into the final tag design.
  </ul>
  <br>
  <ul>
    Given the time constraints of the hackathon, our team prioritized only the most critical components, while identifying additional sensors for future development (see “Next Steps” below).
  </ul>
  <br>
  <h2 style="font-weight: bold;">Design</h2>
  Our current testbed prototype centers around an ESP32-S3 board serving as the main controller.
  <br>
  <br>
  Connected to it are:
  <ol>
    <li>  1. Temperature Sensor (DS18B20): Records precise temperature readings.</li>
    <li>  2. GPS Module (NEO-M9N): Provides accurate location data.</li>
    <li>  3. Built-in ESP32-S3 Camera: Captures real-time visual data.</li>
  </ol>
  <br>
<p>We also explored integrating an IMU (ICM-20948) for motion tracking and a BMP390 pressure sensor for depth readings. Unfortunately, due to shipping delays, these were de-scoped.</p>
<br>

<h2 style="font-weight: bold;"> Build </h2>
<p>Over a single weekend (Oct 4-5, 2025), our team built a fully functional prototype capable of reading temperature data, retrieving GPS coordinates, and streaming a live camera feed.</p>
<br>
<p>We programmed and tested the system using Arduino IDE, with ChatGPT-assisted debugging and code generation to help accelerate development, interpret error messages, and troubleshoot wiring issues under time pressure.</p>
<br>
<p>For hardware integration, our prototype enclosure was modified from a pre-existing 3D-printable model. Using an Ender 3 Neo V2 3D printer, we successfully printed the enclosure in PLA. Images of our progress, accomplishments, and outputs can be seen below.</p>



<!-- 2x2 Grid -->
<div class="photo-grid grid-2x2">
  <div class="photo-card">
    <img src="/images/photo1.png" alt="Photo 1" />
    <div class="caption">Fig 1: Wiring Diagram</div>
  </div>
  <div class="photo-card">
    <img src="/images/photo2.png" alt="Photo 2" />
    <div class="caption">Fig 2: Prototype Instrumentation Circuit</div>
  </div>
  <div class="photo-card">
    <img src="/images/photo3.png" alt="Photo 3" />
    <div class="caption">Fig 3: 3D Printed Instrumentation Prototype Enclosure (Open)</div>
  </div>
  <div class="photo-card">
    <img src="/images/photo4.png" alt="Photo 4" />
    <div class="caption">Fig 4: 3D Printed Instrumentation Prototype Enclosure (Closed)</div>
  </div>
</div>

<!-- 1x1 Image -->
<div class="grid-1x1 photo-card">
  <img src="/images/photo5.png" alt="Photo 5" />
  <div class="caption">Fig 5: Instrumentation Data Output (Temperature + GPS)</div>
</div>

<!-- 2 Side by Side -->
<div class="photo-grid grid-2side">
  <div class="photo-card">
    <img src="/images/photo6.png" alt="Photo 6" />
    <div class="caption">Fig 6: Live Camera Stream Tests</div>
  </div>
  <div class="photo-card">
    <img src="/images/photo7.png" alt="Photo 7" />
    <div class="caption">Fig 7: Initial Species Predictability Test</div>
  </div>
</div>



</section>

<section id="section3">
  <h1 style="font-weight: bold;">Next Steps</h1>
  <p>While we’ve made significant progress, the next stages of development include:</p>

<ol>
  <li>
    1. Expanded Instrumentation
    <ol>
      <li>a. Integrate and validate the IMU and pressure/depth sensors.</li>
      <li>b. Finalize sensor suite for data accuracy, reliability, and usability.</li>
    </ol>
  </li>

  <li>
    2. Miniaturization & Design
    <ol>
      <li>a. Transition from a bulky testbed to a miniaturized, non-invasive shark tag.</li>
      <li>b. Improve waterproofing and durability for marine deployment.</li>
    </ol>
  </li>

  <li>
    3. Data Logging & Communication
    <ol>
      <li>a. Explore satellite transmission modules for real-time global data sharing.</li>
      <li>b. Investigate cost-effective communication buoys to relay data from key geographical areas of interest.</li>
    </ol>
  </li>

  <li>
    4. Machine Learning & Vision
    <ol>
      <li>a. Enhance the onboard camera with machine learning to identify shark species and nearby marine life.</li>
      <li>b. Expand this capability into a citizen science tool, enabling public participation in shark identification (similar to initiatives like the <a href="https://fishdoorbell.com" target="_blank">Fish Doorbell</a>).</li>
    </ol>
  </li>
</ol>

</section>

<section id="section4">
  <h1 style="font-weight: bold;">Why It Matters</h1>
  <p>By advancing specimen-level tracking and analysis, our shark tag technology has the potential to revolutionize how we monitor marine life. These insights can help improve conservation strategies, deepen ecological understanding, and inspire the public to engage with ocean science in meaningful ways.</p>
  <br>
  <p>Our ultimate goal is to generate data that strengthens our habitability model, making it smarter, more adaptive to real-world ocean dynamics, and truly reflective of the behaviours of one of the ocean’s most iconic predators.</p>
 
</section>
