<template>
	<div id="map-container">
		<svg
			:width="mapBoxParameters.width"
			:height="mapBoxParameters.height"
			:viewBox="mapBoxParameters.viewport"
			@wheel="zoomPan"
		></svg>
	</div>
</template>

<script>
	import * as d3 from "d3";
	import geoJson from "@/assets/japan_geo.json";
	export default {
		name: "Map",
		props: {
			populationParameters: {
				type: Array,
				defalut: () => {},
			},
		},
		data() {
			return {
				mapImage: null,
				mapBoxParameters: {
					width: 400,
					height: 400,
					viewport: "0 0 400 400",
					ratio: 1,
					dx: 0,
					dy: 0,
					centerPos: [137.0, 38.2],
					scale: 1000,
				},
			};
		},
		computed: {},
		mounted() {
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

			// SVG要素を追加
			this.mapImage = d3
				.select("#map-container svg")
				.selectAll("path")
				.data(geoJson.features)
				.enter()
				.append("path")
				.attr("d", path)
				.attr("stroke", "#666")
				.attr("stroke-width", 0.25);
		},
		watch: {
			populationParameters: function (newData, oldData) {
				this.repaintMap(newData);
			},
		},
		methods: {
			/**
			 * ホイール操作による地図画像の変化
			 * @param {element} event wheelイベント
			 */
			zoomPan(event) {
				//viewportの値をそれぞれ格納
				let [x, y, w, h] = this.mapBoxParameters.viewport
					.split(" ")
					.map((v) => parseFloat(v));

				// コントロールキー押下中のドラッグ(orトラックパッドのピンチイン/アウト)
				if (event.ctrlKey) {
					// 拡大（Y軸が上がる場合） 縮小（Y軸が下がる場合）
					if (event.deltaY > 0) {
						w = w * 1.01;
						h = h * 1.01;
					} else {
						w = w * 0.99;
						h = h * 0.99;
					}
					this.makeViewBox(x, y, w, h);
					this.mapBoxParameters.ratio = w / this.mapBoxParameters.width;
					event.preventDefault();
				} else {
					// 移動
					if (
						this.mapBoxParameters.dx + event.deltaX >
							-this.mapBoxParameters.width &&
						this.mapBoxParameters.dy + event.deltaY >
							-this.mapBoxParameters.width &&
						this.mapBoxParameters.dx + event.deltaX <
							this.mapBoxParameters.width * 2 &&
						this.mapBoxParameters.dy + event.deltaY <
							this.mapBoxParameters.width * 2
					) {
						this.makeViewBox(x + event.deltaX, y + event.deltaY, w, h);
						this.mapBoxParameters.dx += event.deltaX;
						this.mapBoxParameters.dy += event.deltaY;
					}
				}
			},
			// viewboxを作成
			makeViewBox(x, y, w, h) {
				this.mapBoxParameters.viewport = [x, y, w, h].join(" ");
			},
			repaintMap(data) {
				this.mapImage.attr("fill", "#FF0033").attr("fill-opacity", (item) => {
					// 透明度をランダムに指定する (0.0 - 1.0)
					//console.log(data);
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
	svg {
		width: 100%;
		height: 100%;
	}
</style>
