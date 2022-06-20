<template>
	<div id="map-container"></div>
</template>

<script>
	import * as d3 from "d3";
	import geoJson from "@/assets/japan_geo.json";
	export default {
		name: "Map",
		props: {
			populationParameters: {
				type: Object,
				defalut: () => {},
			},
		},
		data() {
			return {
				mapImage: null,
				mapBoxParameters: {
					width: 400,
					height: 400,
					centerPos: [137.0, 38.2],
					scale: 1000,
				},
			};
		},
		computed: {
			path() {
				// 地図の投影設定
				const projection = d3
					.geoMercator()
					.center(this.mapBoxParameters.centerPos)
					.translate([
						this.mapBoxParameters.width / 2,
						this.mapBoxParameters.height / 2,
					])
					.scale(this.mapBoxParameters.scale);
				// 地図をpathに投影(変換)
				const path = d3.geoPath().projection(projection);
				return path;
			},
		},
		mounted() {
			// SVG要素を追加
			this.mapImage = d3
				.select(`#map-container`)
				.append(`svg`)
				.attr(
					`viewBox`,
					`0 0 ${this.mapBoxParameters.width} ${this.mapBoxParameters.height}`
				)
				.attr(`width`, `100%`)
				.attr(`height`, `100%`);

			this.mapImage
				.selectAll(`path`)
				.data(geoJson.features)
				.enter()
				.append(`path`)
				.attr(`d`, this.path)
				.attr(`stroke`, `#666`)
				.attr(`stroke-width`, 0.25);
		},
		watch: {
			populationParameters: function (newData, oldData) {
				this.repaintMap(newData);
			},
		},
		methods: {
			repaintMap(data) {
				this.mapImage
					.selectAll(`path`)
					.attr(`fill`, `#FF0033`)
					.attr(`fill-opacity`, (item) => {
						// 透明度をランダムに指定する (0.0 - 1.0)
						console.log(data);
						console.log(item.properties.name_ja);
						return Math.random();
					});
			},
		},
	};
</script>

<style scoped>
	#map-container {
		width: 100%;
		height: 100%;
	}
</style>
