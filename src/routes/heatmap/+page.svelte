<h1>HEATMAP</h1>
<p>This is the Heatmap page where we will display the heatmap.</p>

<script lang="ts">
  import { MapLibre, GeoJSONSource, HeatmapLayer, GlobeControl } from 'svelte-maplibre-gl';

  let center: [number, number] = [-80, 40];
  let zoom = 1.5;
</script>

<MapLibre
  class="h-[55vh] min-h-[600px]"
  style="https://basemaps.cartocdn.com/gl/voyager-gl-style/style.json"
  bind:zoom
  bind:center
  maxPitch={85}
  attributionControl={false}
>
    <GlobeControl />

  <!-- Heatmap overlay -->
  <!-- <GeoJSONSource data="https://jma-assets.mierune.dev/codes/amedas_ame.geojson"> -->
    <GeoJSONSource data="/temperature.geojson">
    <!-- add our real data in there -->
    <!-- to do: figure out how to overlay multiple heatmaps -->
    <HeatmapLayer
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
</MapLibre>
