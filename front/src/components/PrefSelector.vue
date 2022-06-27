<template>
	<div class="modal-wrapper" id="select-born-pref">
		<a href="#!" class="modal-overlay"></a>
		<div class="modal-window">
			<div class="modal-content">
				<p class="modal-title">1つ選んでください</p>
				<span v-if="born_pref" class="selected-born">
					{{ born_pref }}
				</span>
				<div
					class="section-container"
					v-for="(value, key) in regionPrefs"
					:key="key"
					:value="value"
				>
					<div class="label-section">
						<span>{{ value.section }}</span>
						<div class="prefs-container">
							<span v-for="(pref, key) in value.prefs" :key="key" :value="pref">
								<input
									type="radio"
									class="input-born-field"
									:id="pref"
									name="born"
									:value="pref"
									v-model="born_pref"
								/>
								<label :for="pref" class="label-born"
									><span class="pref-field">{{ pref }}</span></label
								>
							</span>
						</div>
					</div>
				</div>
			</div>
			<a href="#!" class="modal-close">✖️<i class="far fa-times-circle"></i></a>
		</div>
	</div>
</template>

<script>
	export default {
    name: "PrefSelector"
  };
</script>

<style scoped>
.modal-wrapper {
		z-index: 999;
		position: fixed;
		width: 100%;
		height: 100vh;
		height: 100dvh;
		top: 0;
		right: 0;
		bottom: 0;
		left: 0;
		padding: 40px 10px;
		text-align: center;
	}
.modal-wrapper:not(:target) {
		opacity: 0;
		visibility: hidden;
		transition: opacity 0.3s, visibility 0.3s;
	}
	.modal-wrapper:target {
		opacity: 1;
		visibility: visible;
		transition: opacity 0.4s, visibility 0.4s;
	}
  .modal-wrapper::after {
		display: inline-block;
		height: 100%;
		margin-left: -0.05em;
		vertical-align: middle;
		content: "";
	}

  .modal-overlay {
		z-index: 10;
		position: absolute;
		width: 100%;
		height: 100%;
		top: 0;
		right: 0;
		bottom: 0;
		left: 0;
		background: rgba(0, 0, 0, 0.8);
	}

.modal-window {
		box-sizing: border-box;
		display: inline-block;
		z-index: 20;
		position: relative;
		width: 100%;
		max-width: 700px;
		padding: 10px 30px 25px;
		border-radius: 2px;
		background: #fff;
		box-shadow: 0 0 30px rgba(0, 0, 0, 0.6);
		vertical-align: middle;
	}

  .modal-content {
		max-height: 80vh;
		overflow-y: auto;
		/* text-align: left */
	}

  .modal-title {
		position: relative;
		font-size: 25px;
		padding: 20px;
		height: 70px;
		background: #e6f4ff;
		color: #5c98d4;
		font-weight: bold;
		vertical-align: middle;
	}

	.modal-title:after {
		position: absolute;
		content: "";
		top: 100%;
		border: 15px solid transparent;
		border-top: 15px solid #e6f4ff;
		width: 0;
		height: 0;
	}

  .modal-title p {
		margin: 0;
		padding: 0;
	}

  .selected-born {
		font-size: 20px;
		background-color: #008277;
		color: white;
		/* padding: 10px 50px 15px 50px; */
		padding: 10px 60px 15px 60px;
		border-radius: 7px;
	}

  .section-container {
		min-width: 150px;
	}

.label-section {
		font-family: "Hiragino Kaku Gothic ProN";
		font-style: normal;
		font-weight: 400;
		font-size: 30px;
		/* line-height: 27px; */
		letter-spacing: 0.01em;
		text-align: left;
		margin: 20px;
	}

  .prefs-container {
		display: flex;
		flex-direction: row;
		flex-wrap: wrap;
	}

  .label-born {
		margin: 6px;
		padding: 5px;
		border-radius: 7px;
		border: 2px solid grey;
		background-color: #d9d9d9;
		transition: all 0.3s;
	}

  .input-born-field:checked + .label-born {
		background: #008277;
		color: white;
		border-radius: 10px;
		text-shadow: 0 0 1px rgba(0, 0, 0, 0.7);
	}

	.input-born-field:focus + .label-born {
		/* outline-color: #4D90FE; */
		outline-offset: 0px;
		outline-style: auto;
		outline-width: 5px;
	}

  .pref-field {
		font-size: 20px;
		text-align: center;
		vertical-align: middle;
		padding: 20px;
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

  .modal-close:hover {
		color: #2b2e38;
	}
</style>
