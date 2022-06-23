<template>
	<div id="app">
		<router-view />
	</div>
</template>

<script>
import ProfileView from "./views/ProfileView.vue";

export default {
  name: "App",
  components: {
    ProfileView,
  },
};
</script>

<style>
	#app {
		width: 100%;
		height: 100%;
		position: relative;
	}
</style>
