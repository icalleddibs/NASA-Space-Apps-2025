

<script lang="ts">
  import { MapLibre, GeoJSONSource, HeatmapLayer, GlobeControl } from 'svelte-maplibre-gl';

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
  <HeatmapLayer
    id="ph-heatmap"
    paint={{
      'heatmap-weight': 1,
      'heatmap-intensity': ['interpolate', ['exponential', 2], ['zoom'], 0, 0.9, 18, 10],
      'heatmap-color': [
        'interpolate',
        ['linear'],
        ['heatmap-density'],
        0,
        'rgba(33,102,172,0)',
        0.2,
        'rgb(103,169,207)',
        0.4,
        'rgb(209,229,240)',
        0.6,
        'rgb(253,219,199)',
        0.7,
        'rgb(239,138,98)',
        0.9,
        'rgb(178,24,43)',
        1,
        'rgb(100,0,200)'
      ],
      'heatmap-radius': ['interpolate', ['linear'], ['zoom'], 0, 8, 18, 20],
      'heatmap-opacity': ['interpolate', ['linear'], ['zoom'], 2, 1, 18, 0]
    }}
  />
</GeoJSONSource>
{/if}

{#if chlorophyll}
<GeoJSONSource id="chl-source" data="/chlorophyll.geojson">
  <HeatmapLayer
    id="chl-heatmap"
    paint={{
      'heatmap-weight': 1,
      'heatmap-intensity': ['interpolate', ['exponential', 2], ['zoom'], 0, 0.9, 18, 10],
      'heatmap-color': [
        'interpolate',
        ['linear'],
        ['heatmap-density'],
        0,
        'rgba(0,0,255,0)',
        0.2,
        'rgb(0,255,255)',
        0.4,
        'rgb(0,255,0)',
        0.6,
        'rgb(255,255,0)',
        0.8,
        'rgb(255,165,0)',
        1,
        'rgb(255,0,0)'
      ],
      'heatmap-radius': ['interpolate', ['linear'], ['zoom'], 0, 8, 18, 20],
      'heatmap-opacity': ['interpolate', ['linear'], ['zoom'], 2, 1, 18, 0]
    }}
  />
</GeoJSONSource>
{/if}

{#if temperature}
<GeoJSONSource id="temp-source" data="/temperature.geojson">
  <HeatmapLayer
    id="temp-heatmap"
    paint={{
      'heatmap-weight': 1,
      'heatmap-intensity': ['interpolate', ['exponential', 2], ['zoom'], 0, 0.9, 18, 10],
      'heatmap-color': [
        'interpolate',
        ['linear'],
        ['heatmap-density'],
        0,
        'rgba(0,0,255,0)',
        0.2,
        'rgb(0,255,255)',
        0.4,
        'rgb(0,255,0)',
        0.6,
        'rgb(255,255,0)',
        0.8,
        'rgb(255,165,0)',
        1,
        'rgb(255,0,0)'
      ],
      'heatmap-radius': ['interpolate', ['linear'], ['zoom'], 0, 8, 18, 20],
      'heatmap-opacity': ['interpolate', ['linear'], ['zoom'], 2, 1, 18, 0]
    }}
  />
</GeoJSONSource>
{/if}

{#if salinity}
<GeoJSONSource id="sal-source" data="/salinity.geojson">
  <HeatmapLayer
    id="sal-heatmap"
    paint={{
      'heatmap-weight': 1,
      'heatmap-intensity': ['interpolate', ['exponential', 2], ['zoom'], 0, 0.9, 18, 10],
      'heatmap-color': [
        'interpolate',
        ['linear'],
        ['heatmap-density'],
        0,
        'rgba(0,0,255,0)',
        0.2,
        'rgb(0,255,255)',
        0.4,
        'rgb(0,255,0)',
        0.6,
        'rgb(255,255,0)',
        0.8,
        'rgb(255,165,0)',
        1,
        'rgb(255,0,0)'
      ],
      'heatmap-radius': ['interpolate', ['linear'], ['zoom'], 0, 8, 18, 20],
      'heatmap-opacity': ['interpolate', ['linear'], ['zoom'], 2, 1, 18, 0]
    }}
  />
</GeoJSONSource>
{/if}

{#if turbidity}
<GeoJSONSource id="turb-source" data="/turbidity.geojson">
  <HeatmapLayer
    id="turb-heatmap"
    paint={{
      'heatmap-weight': 1,
      'heatmap-intensity': ['interpolate', ['exponential', 2], ['zoom'], 0, 0.9, 18, 10],
      'heatmap-color': [
        'interpolate',
        ['linear'],
        ['heatmap-density'],
        0,
        'rgba(255,255,255,0)',
        0.2,
        'rgb(200,200,200)',
        0.4,
        'rgb(150,150,150)',
        0.6,
        'rgb(100,100,100)',
        0.8,
        'rgb(50,50,50)',
        1,
        'rgb(0,0,0)'
      ],
      'heatmap-radius': ['interpolate', ['linear'], ['zoom'], 0, 8, 18, 20],
      'heatmap-opacity': ['interpolate', ['linear'], ['zoom'], 2, 1, 18, 0]
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