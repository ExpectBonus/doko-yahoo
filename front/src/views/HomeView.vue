<template>
	<div id="home">
		<img src="@/assets/DokoYahooLogo.png" alt="どこヤフ" />
		<div class="text">
			<span>🤔</span>
			<p><span>どこでヤフー社員が</span><span>働いているかな</span></p>
			<p><span>自分もどこで</span><span>働こうかな</span></p>
		</div>
		<div id="google-login"></div>
	</div>
</template>

<script>
	export default {
		name: "HomeView",
		mounted() {
			google.accounts.id.initialize({
				client_id: process.env.VUE_APP_GOAUTH_CLIENT_ID,
				callback: this.handleCredentialResponse,
			});
			google.accounts.id.renderButton(
				document.getElementById("google-login"),
				{
					theme: "outline",
					shape: "pill",
					size: "large",
				} // customization attributes
			);
			//google.accounts.id.prompt(); // also display the One Tap dialog
		},
		methods: {
			handleCredentialResponse(response) {
				this.$store.commit("setUserIdToken", response);
				this.$router.push({ name: "profile" });
			},
		},
	};
</script>

<style scoped>
	#home {
		width: 100%;
		max-width: 1024px;
		min-height: 100vh;
		min-height: 100dvh; /* for iOS */
		display: flex;
		flex-direction: column;
		row-gap: 10px;
		align-items: center;
		justify-content: space-evenly;
		padding: 10px;
	}
	img {
		width: 100%;
		max-width: 300px;
		height: auto;
	}
	.text {
		width: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		text-align: center;
		font-size: 1.5rem;
		font-weight: bold;
	}
	span {
		display: inline-block;
	}
</style>
