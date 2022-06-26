<template>
	<div id="home">
		<img src="@/assets/DokoYahooLogo.png" alt="どこヤフ" />
		<div class="text">
			<span>🤔</span>
			<p><span>どこでヤフー社員が</span><span>働いているかな</span></p>
			<p><span>自分もどこで</span><span>働こうかな</span></p>
		</div>
		<button class="login">Googleアカウントで始める</button>
	</div>
</template>

<script>
	export default {
		name: "HomeView",
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
	.login {
		width: 90%;
		padding: 10px 20px;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 1.2rem;
		font-weight: bold;
		color: #ffffff;
		background-color: #008277;
		border-radius: 10px;
		box-shadow: inset -3px -3px 4px rgba(0, 0, 0, 0.25);
	}
</style>
