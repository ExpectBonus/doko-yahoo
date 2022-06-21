<template>
	<div id="map-view">
		<header>
			<h1><span class="doko">どこ</span><span class="yahoo">ヤフ</span></h1>
			<HobbiesSelector @selectedHobbies="getHeatMapData" />
		</header>
		<div class="contents">
			<Map
				:populationParameters="heatMapData"
				@clickedPrefecture="selectedPrefecture = $event"
			/>
		</div>
		<div class="drawer-header">
			<p>{{ selectedPrefecture || "みんなはどこで働くつもりだろう？" }}</p>
		</div>
	</div>
</template>

<script>
	import axios from "axios";
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
				selectedPrefecture: null,
				heatMapData: {},
			};
		},
		methods: {
			async getHeatMapData(payload) {
				//set dummyData
				this.heatMapData = {
					東京都: 1,
					大阪府: 0.8,
					愛知県: 0.7,
					福岡県: 0.2,
				};
				/* await axios
					.get("/api/heatmap/", {
						params: {
							hobbies: payload,
						},
					})
					.then((res) => {
						if (res.status == "200") {
							this.heatMapData = { ...res.data };
						} else {
							throw new Error(`status: ${res.status}`);
						}
					})
					.catch((error) => {
						alert("データの取得に失敗しました");
						console.log(error);
					}); */
			},
		},
	};
</script>

<style scoped>
	#map-view {
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	header {
		width: 100%;
		position: fixed;
		top: 0;
		display: flex;
		flex-direction: column;
		align-items: center;
		padding: 10px;
		background-color: #ffffff;
		box-shadow: 0px 4px 4px #cdcdcd;
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
	.contents {
		width: 100%;
		height: 100%;
	}

	.drawer-header {
		width: 100%;
		position: fixed;
		bottom: 0;
		height: 80px;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		font-weight: bold;
		background-color: #d9d9d9;
		border: 1px solid #d9d9d9;
		border-radius: 20px 20px 0px 0px;
	}
	.drawer-header::before {
		content: "";
		display: block;
		width: 20%;
		border: 2px solid #878787;
		border-radius: 2px;
		position: absolute;
		top: 5px;
		left: 40%;
	}
</style>
