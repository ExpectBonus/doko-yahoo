import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";
import axios from "axios";
Vue.use(Vuex);

export default new Vuex.Store({
	// `createPersistedState()`でインスタンス作成。引数に設定を書く
	plugins: [
		createPersistedState({
			// ストレージのキーを指定。デフォルトではvuex
			key: "dokoYahooVuex",
			// 管理対象のステートを指定
			paths: ["userIdToken", "userInfo"],
			// ストレージの種類を指定する
			storage: window.sessionStorage,
		}),
	],

	state: {
		userIdToken: "",
		userInfo: {},
	},
	mutations: {
		setUserIdToken(state, token) {
			state.userIdToken = token;
		},
		setUserInfo(state, data) {
			state.userInfo = data;
		},
		resetUser(state) {
			state.isLoggedIn = false;
			state.userIdToken = "";
			state.userInfo = {};
			sessionStorage.removeItem("dokoYahooVuex");
		},
	},
	actions: {
		async getUserInfo({ commit }, token) {
			await axios
				.get(`/api/user/${token}`)
				.then((response) => {
					commit("setUserIdToken", token);
					commit("setUserInfo", response.data);
				})
				.catch((error) => {
					console.log(error);
					if (error.request.status == 404) {
						//	User does not exist yet
						commit("setUserIdToken", token);
					} else {
						commit("resetUser");
					}
				});
		},
	},
});
