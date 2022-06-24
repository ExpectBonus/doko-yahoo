<template>
	<div id="comments-board">
		<div class="drawer-header">
			<p>{{ prefectureName || "みんなはどこで働くつもりだろう？" }}</p>
		</div>
		<div class="comments"></div>

		<div class="message-setter">
			<div class="text-input-container">
				<textarea v-model="inputText"></textarea>
			</div>

			<button
				class="send-button"
				:disabled="!inputText"
				@click="postNewComment()"
			>
				<svg xmlns="http://www.w3.org/2000/svg" height="50" width="50">
					<path
						d="M5 41.05V6.9L45.35 24ZM9.05 34.8 34.8 24 9.05 13.1V20.4L21.65 24L9.05 27.55ZM9.05 34.8V24V13.1V20.4V27.55Z"
					/>
				</svg>
			</button>
		</div>
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
		data() {
			return {
				inputText: "",
			};
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

	.message-setter {
		width: 100%;
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: space-between;
		column-gap: 10px;
		padding: 20px;
	}
	.text-input-container {
		position: relative;
		width: calc(100% - 50px);
		display: flex;
		justify-content: center;
		align-items: center;
		background-color: #ffffff;
		border: 3px solid #008277;
		box-sizing: border-box;
		border-radius: 10px;
	}
	.text-input-container:before {
		/* 左ふきだしの左三角を描画 */
		content: "";
		position: absolute;
		top: 15px;
		left: -27px; /* 下記のborder値の合計 */
		border: 12px solid transparent;
		border-right: 15px solid #008277;
	}
	.text-input-container textarea {
		width: 100%;
		resize: none;
		margin: 5px 10px;
		border: none;
		text-align: left;
		font-weight: bold;
		overflow-y: auto;
	}
	.text-input-container textarea:focus {
		outline: none;
	}
	.send-button {
		width: 50px;
		height: 50px;
		background: transparent;
		border: none;
		padding: 0;
	}
	.send-button:active {
		position: relative;
		top: 5px;
	}
	.send-button svg {
		fill: #008277;
	}
	.send-button:disabled svg {
		fill-opacity: 0.4;
	}
</style>
