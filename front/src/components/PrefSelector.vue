<template>
	<div id="pref-selector">
		<div class="header" :class="{ selected: selectedPrefs.length }">
			<p v-if="!selectedPrefs.length">都道府県を選択してください</p>
			<div v-else>
				<span>{{ selectedPrefs }}</span>
			</div>
		</div>
		<div
			class="region-container"
			v-for="(region, regionIndex) in regionPrefs"
			:key="regionIndex"
		>
			<span>{{ region.section }}</span>

			<div class="prefs-container">
				<div
					class="prefecture"
					v-for="(pref, prefIndex) in region.prefs"
					:key="prefIndex"
					:value="pref"
				>
					<input
						type="radio"
						:id="pref"
						name="born"
						:value="pref"
						v-model="born_pref"
					/>
					<label :for="pref">
						<span>{{ pref }}</span>
					</label>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import { regionPrefs } from "../assets/prefectures.js";
	export default {
		name: "PrefSelector",
		props: {
			request: {
				type: String,
				default: "bornPref", // bornPref || workPref
			},
		},
		data() {
			return {
				regionPrefs,
				selectedPrefs: [],
			};
		},
	};
</script>

<style scoped>
	#pref-selector {
		position: relative;
		width: 100%;
		max-width: 1024px;
		height: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		row-gap: 15px;
		padding: 10px;
		overflow: scroll;
		background-color: #ffffff;
	}

	.header {
		position: sticky;
		top: 0;
		width: 100%;
		min-height: 80px;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		font-size: 1.2rem;
	}
	.header.selected {
		background-color: #008277;
		color: white;
	}

	.region-container {
		width: 100%;
		display: flex;
		flex-direction: column;
		align-items: flex-start;
		row-gap: 5px;
	}

	.prefs-container {
		width: 100%;
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: flex-start;
		flex-wrap: wrap;
		gap: 10px;
	}

	.prefecture {
		position: relative;
		transition: all 0.3s;
	}
	input[type="radio"] {
		opacity: 0;
		position: absolute;
		top: 0;
		left: 0;
		height: 100%;
		width: 100%;
		margin: 0;
		cursor: pointer;
	}
	label {
		width: 100%;
		height: 100%;
		display: block;
		text-align: center;
		font-size: 1.2rem;
		font-weight: bold;
		color: #292929;
		background-color: #d9d9d9;
		border-radius: 10px;
		border: 1px solid #d9d9d9;
		padding: 5px 10px;
		transition: all 0.3s ease-out;
	}

	input[type="checkbox"]:checked + label {
		color: #ffffff;
		background-color: #008277;
		border-color: #008277;
	}

	.modal-close {
		z-index: 20;
		position: absolute;
		top: 5px;
		right: 5px;
		width: 35px;
		color: #95979c !important;
		font-size: 30px;
		font-weight: 700;
		line-height: 35px;
		text-align: center;
		text-decoration: none;
		text-indent: 0;
	}
</style>
