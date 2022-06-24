<template>
	<div id="comments-board">
		<div class="drawer-header">
			<p>{{ prefectureName || "みんなはどこで働くつもりだろう？" }}</p>
		</div>
		<div class="comments"></div>
		<form></form>
	</div>
</template>

<script>
	export default {
		name: "CommentsBoard",
		props: {
			prefectureName: {
				type: String,
			},
			comments: {
				type: Array || Object,
				default: () => {},
			},
		},
	};
</script>
<style scoped>
	#comments-board {
		position: relative;
		width: 100%;
		height: 100vh;
		display: flex;
		flex-direction: column;
		align-items: center;
		background-color: #d9d9d9;
		border: 1px solid #d9d9d9;
		border-radius: 20px 20px 0px 0px;
	}
	#comments-board::before {
		content: "";
		display: block;
		width: 20%;
		border: 2px solid #878787;
		border-radius: 2px;
		position: absolute;
		top: 5px;
		left: 40%;
	}
	.drawer-header {
		width: 100%;
		height: 80px;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		font-weight: bold;
	}
	.comments {
		width: 100%;
		height: calc(85% - 80px);
	}
</style>
