

<!-- svelte-ignore non_reactive_update -->
<script lang="ts">
  import { MapLibre, GeoJSONSource, NavigationControl, GlobeControl, CircleLayer } from 'svelte-maplibre-gl';

  let center: [number, number] = [-80, 40];
  let zoom = $state(1.5);
  let pH = $state(false);
  let chlorophyll = $state(false);
  let salinity = $state(false);
  let temperature = $state(false);
  let turbidity = $state(false);

</script>


<div class="absolute top-16 left-4 z-50 bg-white/80 hover:bg-white rounded-lg shadow-md px-3 py-2 flex flex-col gap-2 text-sm font-semibold transition">
  <p> Select Data Layers:</p>

  <button
    class="bg-gray-300/90 hover:bg-gray-400 text-black font-semibold text-xs px-3 py-1 rounded-lg shadow-md transition self-start"
    onclick={() => {
      pH = chlorophyll = salinity = temperature = turbidity = false;
    }}
    >
    Clear All Layers
  </button>

  <label class="flex items-center gap-2 cursor-pointer">
    <input type="checkbox" bind:checked={pH} class="rounded border p-1" style="accent-color: rgb(255, 255, 0);" />
    <span
      class="inline-block w-3 h-3 rounded-full"
      style="background-color: rgb(255, 255, 0); opacity: 1;"
  ></span>
  Acidity (pH)
  </label>

  <label class="flex items-center gap-2 cursor-pointer">
    <input type="checkbox" bind:checked={chlorophyll} class="rounded border p-1" style="accent-color: rgb(26, 204, 10);" />
    <span
    class="inline-block w-3 h-3 rounded-full"
    style="background-color: rgb(26, 204, 10); opacity: 1;"
  ></span>
    Chlorophyll Concentration
  </label>

  <label class="flex items-center gap-2 cursor-pointer">
    <input type="checkbox" bind:checked={turbidity} class="rounded border p-1" style="accent-color: rgb(0,255,255);" />
    <span
      class="inline-block w-3 h-3 rounded-full"
      style="background-color: rgb(0,255,255); opacity: 1;"
    ></span>
    Turbidity (Kd)
  </label>

  <label class="flex items-center gap-2 cursor-pointer">
    <input type="checkbox" bind:checked={temperature} class="rounded border p-1" style="accent-color: rgb(255,0,255);" />
    <span
      class="inline-block w-3 h-3 rounded-full"
      style="background-color: rgb(255,0,255); opacity: 1;"
    ></span>
    Sea Surface Temperature
  </label>

  <label class="flex items-center gap-2 cursor-pointer">
    <input type="checkbox" bind:checked={salinity} class="rounded border p-1" style="accent-color: rgb(252, 28, 3);" />
    <span
      class="inline-block w-3 h-3 rounded-full"
      style="background-color: rgb(252, 28, 3); opacity: 1;"
    ></span>
    Sea Surface Salinity
  </label>


<!-- Shared intensity scale -->
<div class="mt-4 text-sm text-gray-600 pl-3">
  <div
    class="w-48 h-2 rounded-full mb-1"
    style="background: linear-gradient(to right, rgba(33,102,172,0.1), rgb(33,102,172));"
  ></div>
  <div class="flex justify-between w-48 text-xs text-gray-500">
    <span>Low suitability</span>
    <span>High suitability</span>
  </div>
</div>
  
</div>




<MapLibre
  class="fixed inset-0 h-screen w-screen"
  style="https://basemaps.cartocdn.com/gl/voyager-gl-style/style.json"
  bind:zoom
  bind:center
  maxPitch={85}
  attributionControl={false}
>
  <NavigationControl />
  <GlobeControl />

  <!-- Heatmap overlay -->


{#if pH}
<GeoJSONSource id="ph-source" data="/acidity.geojson">
  <CircleLayer
    id="ph-circles"
    paint={{
      'circle-color': 'rgb(255, 255, 0)',
      'circle-opacity': [
        '*',
        ['get', 'value'],
        0.08  // adjust for layering
      ]
    }}
  />
</GeoJSONSource>
{/if}

{#if chlorophyll}
<GeoJSONSource id="chl-source" data="/chlorophyll.geojson">
  <CircleLayer
    id="chlorophyll-circles"
    paint={{
      'circle-color': 'rgb(26, 204, 10)',
      'circle-opacity': [
          'interpolate',
          ['linear'],
          ['ln', ['max', ['get', 'value'], 1e-30]], // avoid log(0)
          Math.log(1e-30), 0.0005,  // very small values → faint
          Math.log(1e-2), 0.15,
          Math.log(1), 0.35       // near 1 → darker
      ],
      'circle-radius': ['interpolate', ['linear'], ['zoom'], 0, 4, 18, 10] // optional zoom scaling
    }}
  />
</GeoJSONSource>
{/if}

{#if temperature}
<GeoJSONSource id="temp-source" data="/temperature.geojson">
    <CircleLayer
    id="temp-circles"
    paint={{
      'circle-color': 'rgb(255,0,255)',
      'circle-opacity': [
        '*',
        ['get', 'value'],
        0.25  // adjust for layering
      ],
      'circle-radius': ['interpolate', ['linear'], ['zoom'], 0, 4, 18, 10] // optional zoom scaling
    }}
  />
</GeoJSONSource>
{/if}

{#if salinity}
<GeoJSONSource id="sal-source" data="/salinity.geojson">
  <CircleLayer
    id="sal-circles"
    paint={{
      'circle-color': 'rgb(252, 28, 3)',
      // big ramp near the top; whole ramp then multiplied by 0.6 to cap per-point opacity
      'circle-opacity': [
        '*',
        [
          'interpolate',
          ['linear'],
          ['get', 'value'],
          0.0, 0.02,   // basically invisible for very small values
          0.8, 0.02,   // slowly increasing opacity
          0.87, 0.13,  
          0.92, 0.18,
          0.97, 0.62,
          0.99, 0.90,  
          1.0, 0.95
        ]
        ,
        0.6 
      ],
      'circle-radius': ['interpolate', ['linear'], ['zoom'], 0, 4, 18, 10]
    }}
  />
</GeoJSONSource>
{/if}

{#if turbidity}
<GeoJSONSource id="turb-source" data="/turbidity.geojson">
        <CircleLayer
    id="turbidity-circles"
    paint={{
      'circle-color': 'rgb(0,255,255)',
      'circle-opacity': [
        '*',
        ['get', 'value'],
        0.32  // adjust for layering
      ],
      'circle-radius': ['interpolate', ['linear'], ['zoom'], 0, 4, 18, 10] // optional zoom scaling
    }}
  />
</GeoJSONSource>
{/if}

</MapLibre>

<!-- Return Home Button -->
  <a
    href="/"
    class="absolute top-4 left-4 bg-white/80 hover:bg-white text-black px-3 py-2 rounded-lg shadow-md text-sm font-semibold transition"
  >
    ← Home
  </a>

  <p
    class="absolute top-4 left-27 bg-black/60 text-white px-3 py-2 rounded-lg shadow-md text-sm font-semibold transition"
  >
    Habitat Conditions
  </p>