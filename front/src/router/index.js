import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import ProfileView from "../views/ProfileView.vue";
import MapView from "../views/MapView.vue";
import store from "../store";

Vue.use(VueRouter);

const routes = [
	{
		path: "/",
		name: "home",
		component: HomeView,
	},
	{
		path: "/profile",
		name: "profile",
		component: ProfileView,
		beforeEnter: (to, from, next) => {
			if (!store.state.userIdToken) {
				const sessionVuex = sessionStorage.getItem("dokoYahooVuex");
				sessionVuex.userIdToken &&
					store.commit("setUserIdToken", sessionVuex.userIdToken);
				sessionVuex.userInfo &&
					store.commit("setUserInfo", sessionVuex.userInfo);
			}
			store.state.userIdToken ? next() : next({ name: "home" });
		},
	},
	{
		path: "/map",
		name: "map",
		component: MapView,
		beforeEnter: (to, from, next) => {
			if (!store.state.userIdToken) {
				const sessionVuex = sessionStorage.getItem("dokoYahooVuex");
				sessionVuex.userIdToken &&
					store.commit("setUserIdToken", sessionVuex.userIdToken);
				sessionVuex.userInfo &&
					store.commit("setUserInfo", sessionVuex.userInfo);
			}
			if (store.state.userIdToken) {
				store.state.userInfo.id ? next() : next({ name: "profile" });
			} else {
				next({ name: "home" });
			}
		},
	},
];

const router = new VueRouter({
	mode: "history",
	base: process.env.BASE_URL,
	routes,
});

export default router;
