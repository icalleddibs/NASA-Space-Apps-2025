<script lang="ts">
  import { inview } from 'svelte-inview';
  import { fly, fade } from 'svelte/transition';

  // Track which sections are in view
  let section1InView = false;
  let section2InView = false;
  let section3InView = false;
  let section4InView = false;

  // Navigation function
  const goTo = (path: string) => {
    window.location.href = path;
  };
</script>

<style>
  section {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 2rem;
  }

  section2 {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center; 
    padding: 2rem;
  }

  h1, h2 {
    font-weight: bold;
  }

  h1 {
    font-size: 4rem;
    color: #0070f3;
  }

  h2 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
  }

  .buttons {
    display: flex;
    gap: 1.5rem;
    margin-top: 2rem;
  }

  button {
    padding: 1rem 2rem;
    font-size: 1.2rem;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    background: linear-gradient(45deg, #0070f3, #00c3ff);
    color: white;
    transition: transform 0.2s;
  }

  button:hover {
    transform: scale(1.08);
  }
 
  .info {
    margin-top: 2rem;
    font-size: 1.2rem;
    max-width: 1000px;
  }

.grid-container {
  display: grid;
  grid-template-columns: repeat(5, 1fr); /* Creates 5 equal-width columns */
  gap: 35px; /* Optional: adds space between columns */
}

.column-item {
  /* Add styling for your column content here */
  padding: 25px;
  background-color: #ffc5c5;
  border: 4px solid #ff9f9f;
  border-radius: 25px;
}


</style>

<section
  use:inview
  on:inview_change={(e) => (section1InView = e.detail.inView)}
  class="relative h-screen flex flex-col justify-center items-center text-white bg-cover bg-center"
  style="background-image: url('/images/homepage.png');"
>
  {#if section1InView}
    <h1 transition:fly={{ y: -50, duration: 800 }}>sharkonauts</h1>

    <div class="buttons" transition:fade={{ duration: 1000, delay: 600 }}>
      <button on:click={() => goTo('/tags')}>Tag Tracking Map</button>
      <button on:click={() => goTo('/heatmap')}>Habitability Map</button>
      <button on:click={() => goTo('/prototype')}>Tag Prototype</button>
    </div>

    <div class="info" transition:fly={{ y: 50, duration: 800, delay: 1500 }}>
      <p class="text-black">
        NASA Space Apps Challenge 2025 | 
        <a 
          href="https://github.com/icalleddibs/NASA-Space-Apps-2025" 
          target="_blank" 
          rel="noopener noreferrer"
          class="underline hover:text-red-600"
        >
          GitHub Repository
        </a>
      </p>
    </div>
  {/if}

 <!-- svelte-ignore a11y_consider_explicit_label -->
 <a href="#aboutSection" class="flex justify-center mt-15 animate-bounce">
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 30 30" stroke-width="5"
    stroke="currentColor" class="w-10 h-10 text-blue-400 cursor-pointer hover:scale-110 transition-transform duration-200">
    <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
  </svg>
</a>

</section>

<!-- Section 2 -->
<section 
  use:inview
  on:inview_change={(e) => section2InView = e.detail.inView}
  class="min-h-screen bg-center bg-cover bg-no-repeat"
  style="background-image: url('/images/section2.png'); background-size: contain; aspect-ratio: 16/9;"
  id="aboutSection"
>
  {#if section2InView}
    <div transition:fly={{ y: 50, duration: 800 }}>
      <h2>Mission & Vision</h2>
      <p class="info">Due to climate change, shark foraging patterns are shifting rapidly. As key contributors to ocean ecosystems, sharks play an essential role in maintaining marine balance, but research on them remains limited due to sparse data and unpredictable behaviour. The Sharkonauts Initiative seeks to address this by predicting shark movement patterns through existing behavioural data combined with a novel shark tag prototype.</p>
      <p class="info">A core component of our project is the Habitability Map, which integrates open-access NASA oceanographic data with known physiological parameters of sharks to predict regions most suitable for their survival. The model generates a global grid of probabilities, visualizing how favourable different ocean areas are for sharks.</p>
      <p class="info">We have also developed a working prototype of a shark tag equipped with GPS, a temperature sensor, and a camera. Because shark tag data availability varies widely by species and region, this device can complement our habitability model by tracking understudied populations. To present these findings, we built an interactive web app displaying both the habitability map and a sample tag tracker.</p>
      <p class="info">Together, these tools can help scientists and students better predict shark movements and understand their changing habitats in a warming world.</p>
    </div>
  {/if}
  <!-- svelte-ignore a11y_consider_explicit_label -->
 <a href="#overviewSection" class="flex justify-center mt-15 animate-bounce">
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 30 30" stroke-width="5"
    stroke="currentColor" class="w-10 h-10 cursor-pointer hover:scale-110 transition-transform duration-200" style="color: #fe8080ff">
    <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
  </svg>
</a>
</section>

<!-- Section 3 -->
<section
  use:inview
  on:inview_change={(e) => section3InView = e.detail.inView}
  class="min-h-screen bg-center bg-cover bg-no-repeat"
  style="background-image: url('/images/section3.png'); background-size: contain; aspect-ratio: 16/9;"
  id="overviewSection"
>
  {#if section3InView}
    <div transition:fly={{ y: 50, duration: 800 }}>
        <h2>Functionalities</h2>
        <p class="info">Sharkonauts offers interactive methods of visualizing relevant data on share behaviour and predicted habitats.</p>
        <p class="info">Information on the environmental factors used to create the habitability model can be found on the Environmental Factors page. Furthermore,
          a mathematical model was developed to predict shark movement patterns, which is detailed on the Mathematical Model page. 
          Finally, all data sources used in this project are listed on the Data Sources page.</p>
    </div>
    <div class="buttons" transition:fade={{ duration: 1000, delay: 600 }}>
      <button on:click={() => goTo('/environment')}>Environmental Factors</button>
      <button on:click={() => goTo('/model')}>Mathematical Model</button>
      <button on:click={() => goTo('/sources')}>Data Sources</button>
    </div>
  {/if}
  
    <!-- svelte-ignore a11y_consider_explicit_label -->
  <a href="#meetTeam" class="flex justify-center mt-15 animate-bounce">
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 30 30" stroke-width="5"
      stroke="currentColor" class="w-10 h-10 text-blue-400 cursor-pointer hover:scale-110 transition-transform duration-200">
      <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
    </svg>
  </a>
</section>

<!-- Section 4 -->
<section2 
  use:inview
  on:inview_change={(e) => section4InView = e.detail.inView}
  class="min-h-screen bg-center bg-cover bg-no-repeat"
  style="background-image: url('/images/section4.png'); background-size: contain; aspect-ratio: 16/9;"
  id="meetTeam"
>
  {#if section4InView}
    <div transition:fly={{ y: 50, duration: 800 }}>
      <h2>Meet the Team</h2>
      <p>A group of young professionals across Canada dedicated to making a lasting impact on the space industry.</p>
      <p>As Zenith Fellows (Class of 2024 and 2025), we represent the next generation of students and emerging professionals in the Canadian space sector.</p>
      <br />
      <!-- make 5 colums for all 5 people, a little image and a short bio -->
        <div class="grid-container">
            <div class="column-item">
                <h3 class="text-2xl font-bold mb-2">Adara Hagman</h3>
                <p class="text-sm">Digital Media Arts student at York University. Interested in mechatronics, space science, and assistive devices.</p>
            <a
                href="https://www.linkedin.com/in/adarahagman/"
                target="_blank"
                class="hover:decoration-orange-500 underline transition-all duration-200"
                style="color: #fe8080ff"
            >LinkedIn</a>
            <span class="text-orange-400">|</span>
            <a
                href="https://www.zenithpathways.ca/adara-hagman"
                target="_blank"
                class="hover:decoration-orange-500 underline transition-all duration-200"
                style="color: #fe8080ff"
            >Zenith Fellow '24</a>
            </div>

            <div class="column-item">
                <h3 class="text-2xl font-bold mb-2">Adithi Balaji</h3>
                <p class="text-sm">Master's candidate in Physics at the University of Toronto, with research interests in Earth Observation and planetary science.</p>
                <a
                    href="https://www.linkedin.com/in/adithi-balaji-00483827b/"
                    target="_blank"
                    class="hover:decoration-orange-500 underline transition-all duration-200"
                    style="color: #fe8080ff"
                >LinkedIn</a>
                <span class="text-orange-400">|</span>
                <a
                    href="https://www.zenithpathways.ca/adithi-balaji"
                    target="_blank"
                    class="hover:decoration-orange-500 underline transition-all duration-200"
                    style="color: #fe8080ff"
                >Zenith Fellow '25</a>
            </div>

            <div class="column-item">
                <h3 class="text-2xl font-bold mb-2">Diba Alam</h3>
                <p class="text-sm">Engineering Science student at the University of Toronto. Major in Machine Intelligence, with a Minor in Robotics.
                  Passionate about leveraging AI & robotics to support space exploration.
                </p>
                <a
                    href="https://www.linkedin.com/in/diba-alam/"
                    target="_blank"
                    class="hover:decoration-orange-500 underline transition-all duration-200"
                    style="color: #fe8080ff"
                >LinkedIn</a>
                <span class="text-orange-400">|</span>
                <a
                    href="https://www.zenithpathways.ca/diba-alam"
                    target="_blank"
                    class="hover:decoration-orange-500 underline transition-all duration-200"
                    style="color: #fe8080ff"
                >Zenith Fellow '24</a>
            </div>

            <div class="column-item">
                <h3 class="text-2xl font-bold mb-2">Nora Dawood</h3>
                <p class="text-sm">Electrical engineering student from the University of British Columbia. Interested in space technology and systems.</p>
                <a
                    href="https://www.linkedin.com/in/noradawood/"
                    target="_blank"
                    class="hover:decoration-orange-500 underline transition-all duration-200"
                    style="color: #fe8080ff"
                >LinkedIn</a>
                <span class="text-orange-400">|</span>
                <a
                    href="https://www.zenithpathways.ca/nora-dawood"
                    target="_blank"
                    class="hover:decoration-orange-500 underline transition-all duration-200"
                    style="color: #fe8080ff"
                >Zenith Fellow '24</a>
            </div>

            <div class="column-item">
                <h3 class="text-2xl font-bold mb-2">Umar Shabbir</h3>
                <p class="text-sm">Aerospace engineering graduate from Toronto Metropolitan University with an interest in rockets, rovers, and robotics.</p>
                <a
                    href="https://www.linkedin.com/in/umaremshabbir/"
                    target="_blank"
                    class="hover:decoration-orange-500 underline transition-all duration-200"
                    style="color: #fe8080ff"
                >LinkedIn</a>
                <span class="text-orange-400">|</span>
                <a
                    href="https://www.zenithpathways.ca/umar-shabbir"
                    target="_blank"
                    class="hover:decoration-orange-500 underline transition-all duration-200"
                    style="color: #fe8080ff"
                >Zenith Fellow '25</a>
            </div>
        </div>
    </div>
  {/if}
</section2>



