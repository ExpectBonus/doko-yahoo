import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
	state: {
		userIdToken: "",
		userInfo: {},
	},
	mutations: {
		setUserIdToken(state, googleInfo) {
			state.userIdToken = googleInfo.credential;
		},
		setUserInfo(state, data) {
			state.userInfo = data;
		},
		resetUser(state) {
			state.userIdToken = "";
			state.userInfo = {};
		},
	},
	actions: {
		async getUserInfo(commit, token) {
			await axios
				.get(`/api/user/${token}`)
				.then((response) => {
					commit("setUserIdToken", token);
					commit("setUserInfo", response.data);
				})
				.catch((error) => {
					console.error(error);
				});
		},
	},
});
