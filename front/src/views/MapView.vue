<template>
	<v-main>
		<v-container fluid fill-height>
			<div id="map-container"></div>
		</v-container>
	</v-main>
</template>

<script>
	import * as d3 from "d3";
	import geoJson from "@/assets/japan_geo.json";
	export default {
		name: "MapView",
		data() {
			return {
				mapBox: {
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
					.center(this.mapBox.centerPos)
					.translate([this.mapBox.width / 2, this.mapBox.height / 2])
					.scale(this.mapBox.scale);
				// 地図をpathに投影(変換)
				const path = d3.geoPath().projection(projection);
				return path;
			},
		},
		mounted() {
			// SVG要素を追加
			const svg = d3
				.select(`#map-container`)
				.append(`svg`)
				.attr(`viewBox`, `0 0 ${this.mapBox.width} ${this.mapBox.height}`)
				.attr(`width`, `100%`)
				.attr(`height`, `100%`);

			svg
				.selectAll(`path`)
				.data(geoJson.features)
				.enter()
				.append(`path`)
				.attr(`d`, this.path)
				.attr(`stroke`, `#666`)
				.attr(`stroke-width`, 0.25)
				.attr(`fill`, `#2566CC`)
				.attr(`fill-opacity`, (item) => {
					// メモ
					// item.properties.name_ja に都道府県名が入っている

					// 透明度をランダムに指定する (0.0 - 1.0)
					return Math.random();
				});
		},
	};
</script>

<style scoped></style>
