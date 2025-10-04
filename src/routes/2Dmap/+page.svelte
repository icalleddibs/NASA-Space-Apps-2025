<h1 class="text-4xl font-bold mb-2">Live Shark Tag Tracker</h1>
<p class="text-lg text-gray-400">A 2D interactive map displaying active shark tags.</p>

<script lang="ts">
    import {
        MapLibre,
        Marker,
        NavigationControl,
        ScaleControl,
        GlobeControl,
        Popup
    } from 'svelte-maplibre-gl';

    let lnglat = $state({ lng: -30, lat: 40 });
    let lngLatLoc = $derived(`(${lnglat.lat.toFixed(3)}, ${lnglat.lng.toFixed(3)})`);
    let lngLatName = $state('Shark Tag #12345');
    let popupOpen = $state(false);

    let lnglat2 = $state({ lng: -55, lat: 21 });
    let lngLatLoc2 = $derived(`(${lnglat2.lat.toFixed(3)}, ${lnglat2.lng.toFixed(3)})`);
    let lngLatName2 = $state('Shark Tag #67890');
    let popupOpen2 = $state(false);

    let lnglat3 = $state({ lng: -140, lat: 20 });
    let lngLatLoc3 = $derived(`(${lnglat3.lat.toFixed(3)}, ${lnglat3.lng.toFixed(3)})`);
    let lngLatName3 = $state('Shark Tag #54321');
    let popupOpen3 = $state(false);

    let lnglat4 = $state({ lng: -146, lat: -12 });
    let lngLatLoc4 = $derived(`(${lnglat4.lat.toFixed(3)}, ${lnglat4.lng.toFixed(3)})`);
    let lngLatName4 = $state('Shark Tag #98765');
    let popupOpen4 = $state(false);

    let lnglat5 = $state({ lng: -193, lat: 40 });
    let lngLatLoc5 = $derived(`(${lnglat5.lat.toFixed(3)}, ${lnglat5.lng.toFixed(3)})`);
    let lngLatName5 = $state('Shark Tag #11223');
    let popupOpen5 = $state(false);

    let lnglat6 = $state({ lng: 93, lat: -34 });
    let lngLatLoc6 = $derived(`(${lnglat6.lat.toFixed(3)}, ${lnglat6.lng.toFixed(3)})`);
    let lngLatName6 = $state('Shark Tag #44556');
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
    class="h-[55vh] min-h-[600px]"
    style="https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json"
    zoom={1.5}
    center={{ lng: -80, lat: 40 }}
    maxPitch={85}
    attributionControl={false}
>
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
    <Popup class="w-50 text-white" bind:open={popupOpen} offset={offsets}>
      <span class="text-lg font-bold">{lngLatName}</span>
      <br />
      <span class="text-sm italic">{lngLatLoc}</span>
      <br />
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
    <Popup class="w-50 text-white" bind:open={popupOpen2} offset={offsets}>
      <span class="text-lg font-bold">{lngLatName2}</span>
      <br />
      <span class="text-sm italic">{lngLatLoc2}</span>
      <br />
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
    <Popup class="w-50 text-white" bind:open={popupOpen3} offset={offsets}>
      <span class="text-lg font-bold">{lngLatName3}</span>
      <br />
      <span class="text-sm italic">{lngLatLoc3}</span>
      <br />
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
    <Popup class="w-50 text-white" bind:open={popupOpen4} offset={offsets}>
      <span class="text-lg font-bold">{lngLatName4}</span>
      <br />
      <span class="text-sm italic">{lngLatLoc4}</span>
      <br />
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
    <Popup class="w-50 text-white" bind:open={popupOpen5} offset={offsets}>
      <span class="text-lg font-bold">{lngLatName5}</span>
      <br />
      <span class="text-sm italic">{lngLatLoc5}</span>
      <br />
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
    <Popup class="w-50 text-white" bind:open={popupOpen6} offset={offsets}>
      <span class="text-lg font-bold">{lngLatName6}</span>
      <br />
      <span class="text-sm italic">{lngLatLoc6}</span>
      <br />
      <span class="text-sm">Last updated: {new Date().toLocaleString()}</span>
    </Popup>
    </Marker>

</MapLibre>
