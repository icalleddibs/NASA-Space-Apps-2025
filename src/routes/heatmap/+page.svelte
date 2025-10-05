

<script lang="ts">
  import { MapLibre, GeoJSONSource, HeatmapLayer, GlobeControl, CircleLayer } from 'svelte-maplibre-gl';

  let center: [number, number] = [-80, 40];
  let zoom = $state(1.5);
  let pH = $state(false);
  let chlorophyll = $state(false);
  let salinity = $state(false);
  let temperature = $state(false);
  let turbidity = $state(false);

</script>


<div class="absolute top-16 left-4 z-50 bg-white/80 hover:bg-white rounded-lg shadow-md px-3 py-2 flex flex-col gap-2 text-sm font-semibold transition">
  <label class="flex items-center gap-2 cursor-pointer">
    <input type="checkbox" bind:checked={pH} class="rounded border p-1" />
    Acidity (pH)
  </label>

  <label class="flex items-center gap-2 cursor-pointer">
    <input type="checkbox" bind:checked={chlorophyll} class="rounded border p-1" />
    Chlorophyll Concentration
  </label>

  <label class="flex items-center gap-2 cursor-pointer">
    <input type="checkbox" bind:checked={salinity} class="rounded border p-1" />
    Sea Surface Salinity
  </label>

  <label class="flex items-center gap-2 cursor-pointer">
    <input type="checkbox" bind:checked={temperature} class="rounded border p-1" />
    Sea Surface Temperature
  </label>

  <label class="flex items-center gap-2 cursor-pointer">
    <input type="checkbox" bind:checked={turbidity} class="rounded border p-1" />
    Turbidity (Kd)
  </label>
</div>




<MapLibre
  class="fixed inset-0 h-screen w-screen"
  style="https://basemaps.cartocdn.com/gl/voyager-gl-style/style.json"
  bind:zoom
  bind:center
  maxPitch={85}
  attributionControl={false}
>
  <GlobeControl />

  <!-- Heatmap overlay -->

  <!-- <GeoJSONSource data="https://jma-assets.mierune.dev/codes/amedas_ame.geojson"> -->
  
  <!-- add our real data in there -->
  <!-- to do: figure out how to overlay multiple heatmaps -->

{#if pH}
<GeoJSONSource id="ph-source" data="/acidity.geojson">
  <CircleLayer
    id="ph-circles"
    paint={{
      'circle-color': 'rgb(224, 221, 110)',
      'circle-opacity': [
        '*',
        ['get', 'value'],
        0.10  // adjust for layering
      ]
      // 'circle-radius': ['interpolate', ['linear'], ['zoom'], 0, 4, 18, 10] // optional zoom scaling
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
        '*',
        ['get', 'value'],
        0.2  // adjust for layering
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
      'circle-color': 'rgb(237, 33, 33)',
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
    id="temp-circles"
    paint={{
      'circle-color': 'rgb(101, 105, 224)',
      'circle-opacity': [
        '*',
        ['get', 'value'],
        0.2  // adjust for layering
      ],
      'circle-radius': ['interpolate', ['linear'], ['zoom'], 0, 4, 18, 10] // optional zoom scaling
    }}
  />
</GeoJSONSource>
{/if}

{#if turbidity}
<GeoJSONSource id="turb-source" data="/turbidity.geojson">
        <CircleLayer
    id="temp-circles"
    paint={{
      'circle-color': 'rgb(153, 81, 184)',
      'circle-opacity': [
        '*',
        ['get', 'value'],
        0.2  // adjust for layering
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