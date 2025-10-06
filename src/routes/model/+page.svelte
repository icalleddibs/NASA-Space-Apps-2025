
<script lang="ts">
  import { onMount } from 'svelte';
  import katex from 'katex';
  import 'katex/dist/katex.min.css';

  interface Equation {
    tex: string;
    caption?: string;
    description?: string;
  }

  const equations: Equation[] = [
    {
      tex: `M_{pH} = \\text{clip}\\left(\\frac{pH - 7.75}{0.05}, 0, 1\\right)`,
      caption: "pH Mask",
      description: `
        Input: pH value (typically 7.75--7.8) <br/>
        Output: 0 (pH ≤ 7.75) → 1 (pH ≥ 7.8) <br/>
        Interpretation: Higher values indicate less acidic conditions, more suitable for sharks
      `
    },
    {
      tex: `M_{chl} = \\left[\\text{clip}\\left(\\frac{chl - chl_{min}}{chl_{p90} - chl_{min}}, 0, 1\\right)\\right]^{10}`,
      caption: "Chlorophyll-a Mask",
      description: `
        Input: Chlorophyll-a concentration (mg/m³) <br/>
        Parameters: chl_{p90} = 90th percentile of chlorophyll values <br/>
        Output: 0–1, with exponential emphasis on high values (exponent = 10) <br/>
        Interpretation: Higher values indicate more productive waters with more prey availability
      `
    },
    {
      tex: `M_{sal,binary} = \\begin{cases} 
1 & \\text{if } 37 \\leq sal \\leq 40 \\\\ 
0 & \\text{otherwise} 
\\end{cases}`,
      caption: "Salinity Mask",
      description: `
        Input: Salinity (PSU - Practical Salinity Units) <br/>
        Output: 1 inside optimal range, 0 outside <br/>
        Interpretation: Binary threshold for physiologically suitable salinity range
      `
    },
    {
      tex: `M_{sst} = \\frac{sst_{anom} - sst_{anom,min}}{sst_{anom,max} - sst_{anom,min}}`,
      caption: "SST Anomaly Mask",
      description: `
        Input: SST anomaly (°C from local mean) <br/>
        Output: Linear normalization from 0–1 <br/>
        Interpretation: Uses pre-computed anomaly data; higher positive anomalies indicate warmer waters relative to local conditions
      `
    },
    {
      tex: `M_{turb} = \\left[\\frac{turb - turb_{min}}{turb_{max} - turb_{min}} \\times \\left(1 - \\text{clip}\\left(\\frac{dist}{100}, 0, 1\\right)\\right)\\right]^{0.5}`,
      caption: "Turbidity Combined Mask",
      description: `
        Input: Turbidity (Kd(490) in m⁻¹) and distance from shore (km) <br/>
        Components: Normalized turbidity value × distance weight (1 at shore, 0 at 100km+) <br/>
        Square root (0.5 exponent) boosts visibility of smaller values
      `
    },
    {
      tex: `M_{sal,combined} = \\frac{sal - sal_{min}}{sal_{max} - sal_{min}} \\times \\text{clip}\\left(\\frac{dist}{100}, 0, 1\\right) \\times B(37 \\leq sal \\leq 40)`,
      caption: "Salinity Combined Mask",
      description: `
        Input: Salinity (PSU) and distance from shore (km) <br/>
        Components: Normalized salinity × distance weight × binary penalty (1 if 37 ≤ sal ≤ 40) <br/>
        Interpretation: Higher salinity further from shore is weighted more heavily; values outside 37–40 PSU range are set to zero
      `
    },
    {
      tex: `\\text{clip}(x, 0, 1) = \\begin{cases} 
0 & \\text{if } x < 0 \\\\ 
x & \\text{if } 0 \\leq x \\leq 1 \\\\ 
1 & \\text{if } x > 1 
\\end{cases}`,
      caption: "The clip() function",
      description: `Constrains all output values to the range [0, 1].`
    }
  ];

  let rendered: string[] = [];

  onMount(() => {
    rendered = equations.map(eq =>
      katex.renderToString(eq.tex, { throwOnError: false, displayMode: true })
    );
  });
</script>

<style>
  main {
    padding: 2rem;
    max-width: 900px;
    margin: auto;
  }

  h1 {
    text-align: center;
    font-size: 1.8rem;
    font-weight: bold;
    margin-bottom: 2rem;
  }

  section {
    margin: 6rem auto;
    padding: 2rem;
    max-width: 800px;
    border-radius: 0.75rem;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
    background-color: #fcdcdc;
    line-height: 1.6;
  }

  h2 {
    font-size: 1.5rem;
    font-weight: bold;
    margin-bottom: 1rem;
  }

  p {
    margin-top: 1rem;
    line-height: 1.4;
  }

  .equation {
    margin: 1rem 0;
  }
  
 
</style>

<main>
  <h1>Mathematical Formulas for Shark Habitat Suitability Masks</h1>

  {#if rendered.length === equations.length}
    {#each equations as eq, i}
      <section class={i % 2 === 1 ? 'section-alt' : ''}>
        <h2>{eq.caption ?? 'Equation'}</h2>
        <div class="equation">
          {@html rendered[i] ?? ''}
        </div>
        {#if eq.description}
          <p>{@html eq.description}</p>
        {/if}
      </section>
    {/each}
  {/if}
</main>

<!-- Return Home Button -->
<a
  href="/"
  class="absolute top-4 left-4 bg-white/80 hover:bg-white text-black px-3 py-2 rounded-lg shadow-md text-sm font-semibold transition"
>
  ← Home
</a>

<p
  class="absolute top-0.5 left-28 bg-black/60 text-white px-3 py-2 rounded-lg shadow-md text-sm font-semibold transition"
>
  Mathematical Model
</p>
