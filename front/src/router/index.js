import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import TopView from "../views/TopView.vue";
import ProfileView from "../views/ProfileView.vue";
import MapView from "../views/MapView.vue";

Vue.use(VueRouter);

const routes = [
	{
		path: "/",
		name: "home",
		component: HomeView,
	},
	{
		path: "/top",
		name: "top",
		component: TopView,
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
	},
];

const router = new VueRouter({
	mode: "history",
	base: process.env.BASE_URL,
	routes,
});

router.beforeEach((to, from, next) => {
	// TODO: ログイン認証
	/* if(!isAuth){
		// 認証前のユーザは問答無用でトップに飛ばす
		next({ name: 'top'})
	}else{
		next();
	} */

	next();
});

export default router;
