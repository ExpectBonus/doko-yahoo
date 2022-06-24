<template>
	<div id="comments-board">
		<div class="drawer-header">
			<p>{{ prefecture.name || "みんなはどこで働くつもりだろう？" }}</p>
		</div>
		<div class="comments"></div>
		<CommentForm @emit-input-comment="postComment" />
	</div>
</template>

<script>
	import axios from "axios";
	import commentForm from "@/interfaces/CommentForm.vue";
	export default {
		name: "CommentsBoard",
		components: {
			CommentForm: commentForm,
		},
		props: {
			prefecture: {
				type: Object,
				default: () => {
					return { id: null, name: "" };
				},
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
		methods: {
			async postComment(comment) {
				const result = await axios
					.post(`/api/comments/${this.prefecture.id}`, {
						id: 999, //TODO: this.userId,
						comment: comment,
					})
					.then((response) => {
						if ((response.status = 201)) {
							/** 成功処理 */
						}
					})
					.catch((error) => {
						console.error(error);
						/**エラー処理 */
					});
				console.log(result);
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
