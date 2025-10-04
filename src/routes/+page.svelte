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
    transform: scale(1.05);
  }
 
  .info {
    margin-top: 2rem;
    font-size: 1.2rem;
    max-width: 1000px;
  }

  .section-alt {
    background-color: #f0f0f0;
    color: #333;
  }

.grid-container {
  display: grid;
  grid-template-columns: repeat(5, 1fr); /* Creates 5 equal-width columns */
  gap: 10px; /* Optional: adds space between columns */
}

.column-item {
  /* Add styling for your column content here */
  padding: 40px;
  background-color: rgb(185, 222, 234);
  border: 3px solid rgb(59, 102, 168);
  border-radius: 25px;
}

</style>

<!-- Hero Section -->
<section
  use:inview
  on:inview_change={(e) => section1InView = e.detail.inView}
>
  {#if section1InView}
    <h1 transition:fly={{ y: -50, duration: 800 }}>Sharkonauts</h1>

    <div class="buttons" transition:fade={{ duration: 1000, delay: 1000 }}>
      <button on:click={() => goTo('/heatmap')}>Heatmap</button>
      <button on:click={() => goTo('/tags')}>Tag Tracker</button>
      <button on:click={() => goTo('/information')}>Information</button>
    </div>

    <div class="info" transition:fly={{ y: 50, duration: 800, delay: 1500 }}>
      <p>NASA Space Apps 2025 Submission!</p>
    </div>
  {/if}
</section>

<!-- Section 2 -->
<section class="section-alt"
  use:inview
  on:inview_change={(e) => section2InView = e.detail.inView}
>
  {#if section2InView}
    <div transition:fly={{ y: 50, duration: 800 }}>
      <h2>Mission & Vision</h2>
      <p class="info">Sharkonauts offers an interactive way to visualize various environmental data taken by satellites, and interprets this data to provide insights into shark foraging behavior and habitat.</p>
      <p class="info">Ultimately, we aim to provide a demonstration of how climate change affects environmental factors that sharks rely on.
        By integrating these features, Sharkonauts aims to provide a comprehensive tool for researchers, conservationists, and the general public to understand and protect shark populations.</p>
    </div>
  {/if}
</section>

<!-- Section 3 -->
<section
  use:inview
  on:inview_change={(e) => section3InView = e.detail.inView}
>
  {#if section3InView}
    <div transition:fly={{ y: 50, duration: 800 }}>
        <h2>Functionalities</h2>
        <p class="info">Sharkonauts offers two mapping services to learn more about the impact of climate change on shark foraging patterns.
        The Tag Tracker page displays live tracking data from deployed SharkTags, offering a way to follow individual sharks in real-time.
        The Heatmap page visualizes various environmental factors that affect shark behavior and habitat. This includes a predictive model on shark movement patterns, 
        as well as overlays of phytoplankton, temperature, salinity to emphasize regions best suited for shark nourishment. </p>

    </div>
  {/if}
</section>

<!-- Section 4 -->
<section class="section-alt"
  use:inview
  on:inview_change={(e) => section4InView = e.detail.inView}
>
  {#if section4InView}
    <div transition:fly={{ y: 50, duration: 800 }}>
      <h2>Meet the Team</h2>
      <p>A group of University students across Canada dedicated to making a lasting impact on the space industry.</p>
      <br />
      <!-- make 5 colums for all 5 people, a little image and a short bio -->
        <div class="grid-container">
            <div class="column-item">
                <h3 class="text-2xl font-bold mb-2">Adara Hagman</h3>
                <p>Short bio for person 1.</p>
                <!-- linkedin link -->
                <a href="https://www.linkedin.com/in/adarahagman/" target="_blank" class="underline hover:text-blue-500">LinkedIn</a>
            </div>
            <div class="column-item">
                <h3 class="text-2xl font-bold mb-2">Adithi Balaji</h3>
                <p>Short bio for person 2.</p>
                <a href="https://www.linkedin.com/in/adithi-balaji-00483827b/" target="_blank" class="underline hover:text-blue-500">LinkedIn</a>
            </div>
            <div class="column-item">
                <h3 class="text-2xl font-bold mb-2">Diba Alam</h3>
                <p>Short bio for person 3.</p>
                <a href="https://www.linkedin.com/in/diba-alam/" target="_blank" class="underline hover:text-blue-500">LinkedIn</a>
            </div>
            <div class="column-item">
                <h3 class="text-2xl font-bold mb-2">Nora Dawood</h3>
                <p>Short bio for person 4.</p>
                <a href="https://www.linkedin.com/in/noradawood/" target="_blank" class="underline hover:text-blue-500">LinkedIn</a>
            </div>
            <div class="column-item">
                <h3 class="text-2xl font-bold mb-2">Umar Shabbir</h3>
                <p>Short bio for person 5.</p>
                <a href="https://www.linkedin.com/in/umaremshabbir/" target="_blank" class="underline hover:text-blue-500">LinkedIn</a>
            </div>
        </div>
    </div>
  {/if}
</section>



