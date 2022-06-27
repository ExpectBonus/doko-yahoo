<template>
	<div id="profile-view">
		<span v-if="isClicked" class="loading">
			<span> </span>
			<span> </span>
		</span>
		<header>
			<h2>プロフィールを登録しましょう</h2>
			<p>(必須項目 *)</p>
		</header>
		<div v-if="errorMsg.length" class="error-msg">
			<span v-for="(err, index) in errorMsg" :key="index">
				{{ err }}
				<br />
			</span>
		</div>
		<div class="content">
			<div class="form-wrapper">
				<div class="form-title-columns required">
					<img class="title-icon" src="../assets/badge.png" />
					<span class="title">名前</span>
				</div>
				<div class="input-form name">
					<input
						type="text"
						v-model="username"
						placeholder="矢風 太郎"
						required
					/>
				</div>
			</div>

			<div class="form-wrapper">
				<div class="form-title-columns required">
					<img class="title-icon" src="../assets/business_center.png" />
					<span class="title">職種</span>
				</div>
				<div class="input-form job">
					<JobSelector
						:includeAll="false"
						@selectedJob="selectedJob = $event"
					/>
				</div>
			</div>

			<div class="form-wrapper">
				<div class="form-title-columns required">
					<img class="title-icon" src="../assets/home.png" />
					<span class="title">今、どこに住んでいる？</span>
				</div>
				<div class="input-form from-pref">
					<button
						@click="requestingType = '出身地'"
						class="modal-button"
						:class="{ selected: selectedBornPref }"
					>
						{{ selectedBornPref || "都道府県を選ぶ" }}
					</button>
				</div>
			</div>

			<div class="form-wrapper">
				<div class="form-title-columns required">
					<img class="title-icon" src="../assets/home_work.png" />
					<span class="title">就職後はどこに住みたい？</span>
				</div>

				<div class="input-form to-pref">
					<button
						@click="requestingType = '希望の勤務地'"
						class="modal-button"
						:class="{ selected: selectedWorkPrefs.length }"
					>
						{{ selectedWorkPrefsToStr || "都道府県を選ぶ" }}
					</button>
				</div>
			</div>

			<div
				class="modal"
				v-show="requestingType"
				@click.self="requestingType = null"
			>
				<PrefSelector
					:request="requestingType"
					:selecting="propsSelectedPrefectures"
					@emitPrefs="setPrefs"
					@closeModal="requestingType = null"
				/>
			</div>

			<div class="form-wrapper">
				<div class="form-title-columns">
					<img class="title-icon" src="../assets/interests.png" />
					<span class="title">趣味</span>
				</div>
				<div class="input-form hobbies">
					<HobbiesSelector @selectedHobbies="selectedHobbies = $event" />
				</div>
			</div>
			<div class="send-button-field">
				<a href="#">
					<button class="send-button" @click="sendUserInfo">
						利用を始める
					</button>
				</a>
			</div>
		</div>
	</div>
</template>
<script>
	import { mapState } from "vuex";
	import { prefectures as prefs } from "../assets/prefectures.js";
	import { regionPrefs } from "../assets/prefectures.js";
	import JobSelector from "@/components/JobSelector.vue";
	import PrefSelector from "@/components/PrefSelector.vue";
	import HobbiesSelector from "@/components/HobbiesSelector.vue";
	import axios from "axios";

	export default {
		name: "ProfileView",
		components: {
			JobSelector,
			PrefSelector,
			HobbiesSelector,
		},
		data: function () {
			return {
				// import prefs
				regionPrefs,
				prefs,
				// input
				username: "",
				selectedJob: "",
				selectedBornPref: "",
				selectedWorkPrefs: [],
				selectedHobbies: [],
				// button
				requestingType: null,
				onModal: false,
				isClicked: false,
				// error flag
				errorMsg: [],
				shortName_f: false,
				selectJob_f: false,
				selectBorn_f: false,
				selectFirst_f: false,
			};
		},
		computed: {
			...mapState(["userIdToken", "userInfo"]),
			selectedWorkPrefsToStr() {
				if (!this.selectedWorkPrefs) return ""; //都道府県が選ばれていない場合は即空白リターン
				let str = this.selectedWorkPrefs.reduce((prefs, pref) => {
					return prefs + `${pref}, `; //文字列として並べていく
				}, "");
				return str.slice(0, -2); //末尾のカンマとスペースを削除
			},
			getPrefIndex() {
				return function (pref) {
					if (pref == null) {
						return null;
					}
					return this.prefs.indexOf(pref);
				};
			},
			propsSelectedPrefectures() {
				if (this.requestingType == "出身地") {
					return this.selectedBornPref ? [this.selectedBornPref] : [];
				} else if (this.requestingType == "希望の勤務地") {
					return this.selectedWorkPrefs;
				} else {
					return [];
				}
			},
		},
		methods: {
			setPrefs(array) {
				if (this.requestingType == "出身地") {
					this.selectedBornPref = array[0];
				} else if (this.requestingType == "希望の勤務地") {
					this.selectedWorkPrefs = array;
				}
			},
			sendUserInfo: async function () {
				let err_f;

				// for deactivate submit button
				this.initFlag();

				// 空値チェック
				err_f = this.checkParams();
				if (err_f) {
					// for resubmit
					this.isClicked = false;
					this.setErrorMsg();
					return;
				}
				let params = {
					username: this.username,
					job: this.selectedJob,
					born_pref: this.getPrefIndex(this.selectedBornPref),
					first_pref: this.getPrefIndex(this.selectedWorkPrefs[0]),
					second_pref: this.getPrefIndex(this.selectedWorkPrefs[1]),
					third_pref: this.getPrefIndex(this.selectedWorkPrefs[2]),
					hobbies: this.selectedHobbies,
				};
				await axios
					.post("/api/user/", {
						...params,
						token: this.userIdToken,
					})
					.then(function (res) {
						console.log(`user id: ${res.data}`);
						this.$store.commit("setUserInfo", { ...params, id: res.data.id });
						this.$router.push({ name: "map" });
					})
					.catch(function (err) {
						console.log(err);
						alert("プロフィールの登録に失敗しました");
						this.$router.push({ name: "home" });
					});
			},
			checkParams: function () {
				let err_f = false;
				// 値存在チェック
				if (!this.username) {
					this.shortName_f = true;
					err_f = true;
				}
				if (!this.selectedJob) {
					this.selectJob_f = true;
					err_f = true;
				}
				if (!this.selectedBornPref) {
					this.selectBorn_f = true;
					err_f = true;
				}
				if (!this.selectedWorkPrefs.length) {
					this.selectFirst_f = true;
					err_f = true;
				}
				return err_f;
			},
			setErrorMsg: function () {
				if (this.shortName_f) {
					this.errorMsg.push("名前を入力してください。");
				}
				if (this.selectJob_f) {
					this.errorMsg.push("職業を選んでください。");
				}
				if (this.selectBorn_f) {
					this.errorMsg.push("出身地を選んでください。");
				}
				if (this.selectFirst_f) {
					this.errorMsg.push("住みたい都道府県の第1希望を選んでください。");
				}
			},
			initFlag: function () {
				this.isClicked = true;
				this.errorMsg = [];
				this.shortName_f = false;
				this.selectJob_f = false;
				this.shortBorn_f = false;
				this.selectFirst_f = false;
			},
		},
	};
</script>
<style scoped>
	#profile-view {
		position: relative;
		width: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		row-gap: 20px;
	}

	header {
		width: 100%;
		padding: 10px;
		text-align: center;
	}

	.content {
		width: 100%;
		max-width: 600px;
		padding: 0 10px;
		display: flex;
		flex-direction: column;
		align-items: center;
		row-gap: 30px;
	}

	.form-wrapper {
		width: 100%;
		display: flex;
		flex-direction: column;
		align-items: flex-start;
		row-gap: 15px;
	}

	.form-title-columns {
		width: 100%;
		display: flex;
		flex-direction: row;
		align-items: center;
		column-gap: 10px;
	}

	.form-title-columns .title-icon {
		width: 40px;
		height: 40px;
	}

	.title {
		font-weight: bold;
		font-size: 20px;
		align-items: center;
	}
	.required .title::after {
		content: "*";
		top: 30px;
		right: 5px;
		font-size: 30px;
		color: red;
	}

	.input-form {
		width: 100%;
	}

	/* username */

	.input-form.name input[type="text"] {
		width: 100%;
		font-size: 1.2rem;
		line-height: 3rem;
		padding: 0 10px;
		background: #ffffff;
		border: 3px solid #008277;
		border-radius: 10px;
	}

	/* job */
	.input-form job {
		display: flex;
		flex-direction: row;
		flex-wrap: nowrap;
		overflow-x: scroll;
		align-items: center;
		column-gap: 10px;
		justify-content: space-between;
	}

	/* born_pref */
	.input-form.from-pref {
		width: 100%;
	}

	.modal-button {
		width: 100%;
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: space-between;
		font-size: 1.2rem;
		color: #808080;
		background-color: #eeeeee;
		border: 0px solid transparent;
		border-radius: 10px;
		cursor: pointer;
		padding: 10px 20px;
	}

	.modal-button.selected {
		color: white;
		font-weight: bold;
		background-color: #008277;
	}

	/*アイコンを表示*/
	.modal-button:after {
		font-family: "Font Awesome 5 Free";
		content: "▶";
	}

	/*ラベルホバー時*/
	.modal-button:hover {
		color: #ffffff;
		background-color: #008277;
		transition: 0.6s;
	}

	.modal {
		position: fixed;
		top: 0;
		left: 0;
		z-index: 99;
		width: 100%;
		height: 100vh;
		height: 100dvh; /* for iOS */
		display: flex;
		align-items: center;
		justify-content: center;
		padding: 30px;
		background-color: rgba(60, 60, 60, 0.4);
	}

	.send-button {
		position: relative;
		font-size: 20px;
		font-weight: bold;
		width: 100%;
		padding: 1em;
		cursor: pointer;
		line-height: 1.4;
		color: #ffffff;
		border: 0 solid transparent;
		border-radius: 100px;
		background: #009688;
	}

	.send-button:active {
		opacity: 0.5;
	}

	.send-button-field {
		width: 100%;
	}

	/* loading */

	.loading {
		position: absolute;
		top: 50%;
		left: 50%;
		width: 68px;
		height: 50px;
		-webkit-transform: translate(-50%, -50%);
		transform: translate(-50%, -50%);
	}

	.loading:before,
	.loading:after,
	.loading span {
		position: absolute;
		top: 0;
		left: 0;
		display: block;
		width: 14px;
		height: 50px;
		content: "";
		-webkit-animation: loading20 1.5s ease-in-out infinite;
		animation: loading20 1.5s ease-in-out infinite;
		-webkit-transform-origin: 100% 100%;
		transform-origin: 100% 100%;
	}

	.loading:before {
		background-color: #d81b60;
	}

	.loading:after {
		left: 18px;
		-webkit-animation-delay: -0.3s;
		animation-delay: -0.3s;
		background-color: #3949ab;
	}

	.loading span {
		left: 36px;
		-webkit-animation-delay: -0.6s;
		animation-delay: -0.6s;
		background-color: #00acc1;
	}

	.loading span:nth-child(2) {
		left: 54px;
		-webkit-animation-delay: -1.2s;
		animation-delay: -1.2s;
		background-color: #fb8c00;
	}

	@-webkit-keyframes loading20 {
		0% {
			-webkit-transform: scaleY(0);
			transform: scaleY(0);
			opacity: 0;
		}

		50% {
			-webkit-transform: scaleY(1);
			transform: scaleY(1);
			opacity: 1;
		}

		100% {
			-webkit-transform: scaleY(0);
			transform: scaleY(0);
			opacity: 0;
		}
	}

	@keyframes loading20 {
		0% {
			-webkit-transform: scaleY(0);
			transform: scaleY(0);
			opacity: 0;
		}

		50% {
			-webkit-transform: scaleY(1);
			transform: scaleY(1);
			opacity: 1;
		}

		100% {
			-webkit-transform: scaleY(0);
			transform: scaleY(0);
			opacity: 0;
		}
	}

	/* error */

	.error-msg {
		position: relative;
		border: 3px double #da4033;
		border-radius: 5px;
		margin: 20px 0;
		padding: 20px 20px 5px 20px;
	}

	.error-msg::before {
		content: "入力が正しくありません";
		position: absolute;
		background-color: white;
		color: #da4033;
		font-weight: bold;
		left: 20px;
		top: -23px;
		padding: 10px;
	}
</style>
