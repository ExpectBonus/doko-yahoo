import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
	// `createPersistedState()`でインスタンス作成。引数に設定を書く
  plugins: [createPersistedState(
    { // ストレージのキーを指定。デフォルトではvuex
      key: 'dokoYahooVuex',
      // 管理対象のステートを指定
      paths: [
        'userIdToken',
        'userInfo'
      ],
      // ストレージの種類を指定する
      storage: window.sessionStorage
    }
  )],

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
