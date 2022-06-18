<template>
	<div class="home">
		<img alt="Vue logo" src="../assets/logo.png" />

		<button @click="apiTest">APIテスト</button>
		<div>
			{{ result }}
		</div>

		<HelloWorld msg="Welcome to Your Vue.js App" />
	</div>
</template>

<script>
	// @ is an alias to /src
	import HelloWorld from "@/components/HelloWorld.vue";
	import axios from "axios";
	export default {
		name: "HomeView",
		components: {
			HelloWorld,
		},
		data() {
			return {
				result: null,
			};
		},
		methods: {
			async apiTest() {
				await axios
					.get("/api/user/some_id_from_google_or_something")
					.then((response) => (this.result = response.data))
					.catch((error) => console.log(error));
			},
		},
	};
</script>
