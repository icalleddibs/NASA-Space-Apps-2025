<script lang="ts">
  import {
    MapLibre,
    Marker,
    NavigationControl,
    ScaleControl,
    GlobeControl,
    Popup,
    Projection,
    Light,
    Sky,
    RasterDEMTileSource,
    HillshadeLayer
  } from 'svelte-maplibre-gl';

  let lnglat = $state({ lng: -2.4, lat: 63.09 });
  let lngLatLoc = $derived(`(${lnglat.lat.toFixed(3)}, ${lnglat.lng.toFixed(3)})`);
  let lngLatName = $state('Shark Tag #10026');
  let lngLatTemp = $state('5.9°C');
  let popupOpen = $state(false);

  let lnglat2 = $state({ lng: -71.33, lat: 28.758 });
  let lngLatLoc2 = $derived(`(${lnglat2.lat.toFixed(3)}, ${lnglat2.lng.toFixed(3)})`);
  let lngLatName2 = $state('Shark Tag #79701');
  let lngLatTemp2 = $state('27.5°C');
  let popupOpen2 = $state(false);

  let lnglat3 = $state({ lng: -146.10, lat: 21.306 });
  let lngLatLoc3 = $derived(`(${lnglat3.lat.toFixed(3)}, ${lnglat3.lng.toFixed(3)})`);
  let lngLatName3 = $state('Shark Tag #32098');
  let lngLatTemp3 = $state('25.6°C');
  let popupOpen3 = $state(false);

  let lnglat4 = $state({ lng: -193, lat: -37.349 });
  let lngLatLoc4 = $derived(`(${lnglat4.lat.toFixed(3)}, ${lnglat4.lng.toFixed(3)})`);
  let lngLatName4 = $state('Shark Tag #39420');
  let lngLatTemp4 = $state('19.0°C');
  let popupOpen4 = $state(false);

  let lnglat5 = $state({ lng: -205.72, lat: 36.678 });
  let lngLatLoc5 = $derived(`(${lnglat5.lat.toFixed(3)}, ${lnglat5.lng.toFixed(3)})`);
  let lngLatName5 = $state('Shark Tag #11223');
  let lngLatTemp5 = $state('14.3°C');
  let popupOpen5 = $state(false);

  let lnglat6 = $state({ lng: 52.60, lat: -34 });
  let lngLatLoc6 = $derived(`(${lnglat6.lat.toFixed(3)}, ${lnglat6.lng.toFixed(3)})`);
  let lngLatName6 = $state('Shark Tag #40556');
  let lngLatTemp6 = $state('16.4°C');
  let popupOpen6 = $state(false);

  let offset = $state(24);
  let offsets: maplibregl.Offset = $derived({
    top: [0, offset],
    bottom: [0, -offset],
    left: [offset + 12, 0],
    right: [-offset - 12, 0],
    center: [0, 0],
    'top-left': [offset, offset],
    'top-right': [-offset, offset],
    'bottom-left': [offset, -offset],
    'bottom-right': [-offset, -offset]
  });
</script>

<MapLibre
  class="fixed inset-0 h-screen w-screen"
  style="https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json"
  zoom={1.5}
  center={{ lng: -80, lat: 40 }}
  maxPitch={85}
  attributionControl={false}
>
  <!-- 3D Globe & Projection -->
  <Projection type="globe" />

  <!-- Sun/Lighting -->
  <Light anchor="map" />

  <!-- Sky / Atmosphere -->
  <Sky
    sky-color="#001560"
    horizon-color="#0090c0"
    fog-color="#ffffff"
    sky-horizon-blend={0.9}
    horizon-fog-blend={0.7}
    fog-ground-blend={0.6}
    atmosphere-blend={['interpolate', ['linear'], ['zoom'], 1, 0.6, 3, 0.3, 5, 0]}
  />

  <!-- Terrain & Hillshade for mountains/shading -->
  <RasterDEMTileSource
    tiles={['https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png']}
    minzoom={0}
    maxzoom={15}
    encoding="terrarium"
    attribution="<a href='https://github.com/tilezen/joerd/blob/master/docs/attribution.md'>Mapzen (Terrain)</a>"
  >
    <HillshadeLayer paint={{ 'hillshade-exaggeration': 0.2 }} />
  </RasterDEMTileSource>

  <!-- Navigation & Controls -->
  <NavigationControl />
  <ScaleControl />
  <GlobeControl />

  <!-- Marker 1 -->
  <Marker bind:lnglat>
    {#snippet content()}
      <div class="text-center leading-none">
        <div class="text-3xl">🦈</div>
        <div class="font-bold text-white drop-shadow-xs">{lngLatName}</div>
        <div class="font-bold text-white drop-shadow-xs">{lngLatLoc}</div>
      </div>
    {/snippet}
    <Popup class="w-50 text-black" bind:open={popupOpen} offset={offsets}>
      <span class="text-lg font-bold">{lngLatName}</span><br />
      <span class="text-sm italic">{lngLatLoc}</span><br />
      <span class="text-sm">Temperature: {lngLatTemp}</span><br />
      <span class="text-sm">Last updated: {new Date().toLocaleString()}</span>
    </Popup>
  </Marker>

  <!-- Marker 2 -->
  <Marker bind:lnglat={lnglat2}>
    {#snippet content()}
      <div class="text-center leading-none">
        <div class="text-3xl">🦈</div>
        <div class="font-bold text-white drop-shadow-xs">{lngLatName2}</div>
        <div class="font-bold text-white drop-shadow-xs">{lngLatLoc2}</div>
      </div>
    {/snippet}
    <Popup class="w-50 text-black" bind:open={popupOpen2} offset={offsets}>
      <span class="text-lg font-bold">{lngLatName2}</span><br />
      <span class="text-sm italic">{lngLatLoc2}</span><br />
      <span class="text-sm">Temperature: {lngLatTemp2}</span><br />
      <span class="text-sm">Last updated: {new Date().toLocaleString()}</span>
    </Popup>
  </Marker>

  <!-- Marker 3 -->
  <Marker bind:lnglat={lnglat3}>
    {#snippet content()}
      <div class="text-center leading-none">
        <div class="text-3xl">🦈</div>
        <div class="font-bold text-white drop-shadow-xs">{lngLatName3}</div>
        <div class="font-bold text-white drop-shadow-xs">{lngLatLoc3}</div>
      </div>
    {/snippet}
    <Popup class="w-50 text-black" bind:open={popupOpen3} offset={offsets}>
      <span class="text-lg font-bold">{lngLatName3}</span><br />
      <span class="text-sm italic">{lngLatLoc3}</span><br />
      <span class="text-sm">Temperature: {lngLatTemp3}</span><br />
      <span class="text-sm">Last updated: {new Date().toLocaleString()}</span>
    </Popup>
  </Marker>

  <!-- Marker 4 -->
  <Marker bind:lnglat={lnglat4}>
    {#snippet content()}
      <div class="text-center leading-none">
        <div class="text-3xl">🦈</div>
        <div class="font-bold text-white drop-shadow-xs">{lngLatName4}</div>
        <div class="font-bold text-white drop-shadow-xs">{lngLatLoc4}</div>
      </div>
    {/snippet}
    <Popup class="w-50 text-black" bind:open={popupOpen4} offset={offsets}>
      <span class="text-lg font-bold">{lngLatName4}</span><br />
      <span class="text-sm italic">{lngLatLoc4}</span><br />
      <span class="text-sm">Temperature: {lngLatTemp4}</span><br />
      <span class="text-sm">Last updated: {new Date().toLocaleString()}</span>
    </Popup>
  </Marker>

  <!-- Marker 5 -->
  <Marker bind:lnglat={lnglat5}>
    {#snippet content()}
      <div class="text-center leading-none">
        <div class="text-3xl">🦈</div>
        <div class="font-bold text-white drop-shadow-xs">{lngLatName5}</div>
        <div class="font-bold text-white drop-shadow-xs">{lngLatLoc5}</div>
      </div>
    {/snippet}
    <Popup class="w-50 text-black" bind:open={popupOpen5} offset={offsets}>
      <span class="text-lg font-bold">{lngLatName5}</span><br />
      <span class="text-sm italic">{lngLatLoc5}</span><br />
      <span class="text-sm">Temperature: {lngLatTemp5}</span><br />
      <span class="text-sm">Last updated: {new Date().toLocaleString()}</span>
    </Popup>
  </Marker>

  <!-- Marker 6 -->
  <Marker bind:lnglat={lnglat6}>
    {#snippet content()}
      <div class="text-center leading-none">
        <div class="text-3xl">🦈</div>
        <div class="font-bold text-white drop-shadow-xs">{lngLatName6}</div>
        <div class="font-bold text-white drop-shadow-xs">{lngLatLoc6}</div>
      </div>
    {/snippet}
    <Popup class="w-50 text-black" bind:open={popupOpen6} offset={offsets}>
      <span class="text-lg font-bold">{lngLatName6}</span><br />
      <span class="text-sm italic">{lngLatLoc6}</span><br />
      <span class="text-sm">Temperature: {lngLatTemp6}</span><br />
      <span class="text-sm">Last updated: {new Date().toLocaleString()}</span>
    </Popup>
  </Marker>

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
    Tag Tracking Map
  </p>

  <div class="absolute top-16 left-4 z-50 bg-white/65 hover:bg-white rounded-lg shadow-md px-3 py-2 flex flex-col gap-2 text-sm transition">
  <p> 💡 Select a shark to view its tag information</p>
  </div>