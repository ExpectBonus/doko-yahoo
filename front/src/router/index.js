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
	},
	{
		path: "/map",
		name: "map",
		component: MapView,
		beforeEnter: (to, from, next) => {
			if (!store.state.userInfo) {
				store.dispatch("getUserInfo", $store.state.userIdToken);
			}
			store.state.userInfo ? next() : next({ name: home });
		},
	},
];

const router = new VueRouter({
	mode: "history",
	base: process.env.BASE_URL,
	routes,
});

router.beforeEach(async (to, from, next) => {
	if (to.name !== "home" && !store.state.userIdToken) {
		// 認証前のユーザは問答無用でトップに飛ばす
		next({ name: "home" });
	} else {
		next();
	}
});

export default router;
