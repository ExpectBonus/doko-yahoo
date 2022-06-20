<template>
	<div id="map-view">
		<header>
			<h1><span class="doko">どこ</span><span class="yahoo">ヤフ</span></h1>
			<HobbiesSelector @selectedHobbies="selectedHobbies = $event" />
		</header>
		<div>
			<Map :populationParameters="selectedHobbies" />
		</div>
	</div>
</template>

<script>
	import hobbiesSelector from "@/components/HobbiesSelector";
	import map from "@/components/Map.vue";
	export default {
		name: "MapView",
		components: {
			HobbiesSelector: hobbiesSelector,
			Map: map,
		},
		data() {
			return {
				selectedHobbies: [],
			};
		},
	};
</script>

<style scoped>
	#map-view {
		width: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	header {
		width: 100%;
		height: 100px;
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	h1 {
		font-weight: bold;
	}
	span.doko {
		color: #008277;
	}
	span.yahoo {
		color: #ff0033;
	}
</style>
