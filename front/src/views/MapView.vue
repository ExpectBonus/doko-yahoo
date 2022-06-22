<template>
	<div id="map-view">
		<header>
			<h1><span class="doko">どこ</span><span class="yahoo">ヤフ</span></h1>
			<JobSelector @selectedJob="selectedJob = $event" />
			<div class="hobbies-selector-drawer">
				<HobbiesSelector
					v-show="canViewHobbiesSelector"
					@selectedHobbies="selectedHobbies = $event"
				/>
				<div class="draw-opener" @click="drawHobbiesSelector">
					<button
						class="arrow"
						:class="{ active: canViewHobbiesSelector }"
					></button>
				</div>
			</div>
		</header>
		<div class="contents">
			<Map
				:populationParameters="heatMapData"
				@clickedPrefecture="selectedPrefecture = $event"
			/>
		</div>
		<div class="drawer">
			<Board :prefectureName="selectedPrefecture" />
		</div>
	</div>
</template>

<script>
	import axios from "axios";
	import jobSelector from "@/components/JobSelector";
	import hobbiesSelector from "@/components/HobbiesSelector";
	import map from "@/components/Map.vue";
	import board from "@/components/Board.vue";
	export default {
		name: "MapView",
		components: {
			JobSelector: jobSelector,
			HobbiesSelector: hobbiesSelector,
			Map: map,
			Board: board,
		},
		data() {
			return {
				canViewHobbiesSelector: false,
				selectedJob: null,
				selectedHobbies: [],
				selectedPrefecture: null,
				heatMapData: {},
			};
		},
		methods: {
			drawHobbiesSelector() {
				this.canViewHobbiesSelector &&
					this.getHeatMapData(this.selectedHobbies);
				this.canViewHobbiesSelector = !this.canViewHobbiesSelector;
			},
			async getHeatMapData(payload) {
				//set dummyData
				this.heatMapData = {
					東京都: 1,
					大阪府: 0.8,
					愛知県: 0.7,
					福岡県: 0.2,
				};
				/* await axios
					.get(`/api/heatmap/${selectedJob}`, {
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
		padding: 10px 10px 0 10px;
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
	.hobbies-selector-drawer {
		width: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.draw-opener {
		width: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
	}
	.arrow {
		position: relative;
		width: 30px;
		height: 30px;
		border: none;
		background-color: transparent;
	}
	.arrow:before,
	.arrow:after {
		content: "";
		background-color: #008277;
		position: absolute;
		top: 50%;
		width: 3px;
		height: calc(70% - 1px);
		margin-top: -35%;
	}
	.arrow:before {
		left: 50%;
		margin-left: -25%;
		transform: rotate(-45deg);
	}
	.arrow:after {
		right: 50%;
		margin-right: -25%;
		transform: rotate(45deg);
	}
	.arrow:before,
	.arrow:after {
		transition: transform 0.34s ease;
	}
	.arrow.active:before {
		transform: rotate(45deg);
	}
	.arrow.active:after {
		transform: rotate(-45deg);
	}

	.contents {
		width: 100%;
		height: 100%;
	}
	.drawer {
		width: 100%;
	}
</style>
