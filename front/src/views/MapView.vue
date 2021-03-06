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
				<div
					class="draw-opener"
					@click="canViewHobbiesSelector = !canViewHobbiesSelector"
				>
					<button
						class="arrow"
						:class="{ active: canViewHobbiesSelector }"
					></button>
				</div>
			</div>
		</header>
		<div class="contents">
			<HeatMap
				:population-parameters="heatMapData"
				@clickedPrefecture="selectedPrefecture = $event"
			/>
		</div>
		<div class="board-drawer">
			<CommentsBoard
				:prefecture="selectedPrefecture"
				:comments="prefectureComments"
				@postComment="pushPostComment"
			/>
		</div>
	</div>
</template>

<script>
	import { mapState } from "vuex";
	import axios from "axios";
	import jobSelector from "@/components/JobSelector";
	import hobbiesSelector from "@/components/HobbiesSelector";
	import heatMap from "@/components/HeatMap.vue";
	import commentsBoard from "@/components/CommentsBoard.vue";
	export default {
		name: "MapView",
		components: {
			JobSelector: jobSelector,
			HobbiesSelector: hobbiesSelector,
			HeatMap: heatMap,
			CommentsBoard: commentsBoard,
		},
		data() {
			return {
				canViewHobbiesSelector: false,
				selectedJob: "all",
				selectedHobbies: [],
				selectedPrefecture: { prefName: "", prefCode: null },
				heatMapData: {},
				prefectureComments: [],
			};
		},
		computed: {
			...mapState(["userInfo"]),
			hobbiesArrayToString() {
				if (!this.selectedHobbies.length) return "";
				let str = this.selectedHobbies.reduce((acc, value) => {
					return acc + `hobbies=${value}&`;
				}, "?");
				return str.slice(0, -1); //末尾の"&"を消す
			},
		},
		mounted() {
			this.getHeatMapData();
		},
		watch: {
			selectedJob: function () {
				this.getHeatMapData();
			},
			selectedHobbies: function () {
				this.getHeatMapData();
			},
			selectedPrefecture: function () {
				this.getPrefectureComments();
			},
		},
		methods: {
			async getHeatMapData() {
				await axios
					.get(`/api/heatmap/${this.selectedJob}${this.hobbiesArrayToString}`)
					.then((res) => {
						if (res.status == 200) {
							this.heatMapData = { ...res.data.data };
						} else {
							throw new Error(`status: ${res.status}`);
						}
					})
					.catch((error) => {
						alert("データの取得に失敗しました");
						this.$router.push({ name: "home" });
						console.log(error);
					});
			},
			async getPrefectureComments() {
				await axios
					.get(`/api/comments/${this.selectedPrefecture.prefCode}`)
					.then((res) => {
						if (res.status == 200) {
							this.prefectureComments = res.data.comments;
						}
					})
					.catch((error) => {
						console.error(error);
						alert("コメントの取得に失敗しました．");
						this.$router.push({ name: "home" });
					});
			},
			pushPostComment(comment) {
				this.prefectureComments.push({
					born_pref: this.userInfo.born_pref,
					comment: comment,
					job: this.userInfo.job,
				});
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
		overflow-y: auto;
		scroll-snap-type: y mandatory;
		-webkit-overflow-scrolling: touch; /* Important for iOS devices */
	}
	header {
		width: 100%;
		position: fixed;
		top: 0;
		display: flex;
		flex-direction: column;
		row-gap: 10px;
		align-items: center;
		padding: 10px 10px 0 10px;
		background-color: #ffffff;
		box-shadow: 0px 4px 4px #cdcdcd;
	}
	@media screen and (min-width: 1024px) {
		header {
			padding-left: calc((100% - 1024px) / 2);
			padding-right: calc((100% - 1024px) / 2);
		}
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
		min-height: 100%;
		scroll-snap-align: start;
	}
	.board-drawer {
		position: relative;
		top: -80px;
		width: 100%;
		scroll-snap-align: start;
	}
</style>
