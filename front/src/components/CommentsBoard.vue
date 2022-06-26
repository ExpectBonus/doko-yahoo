<template>
	<div id="comments-board" :class="{ shrink: !prefecture.prefName }">
		<div class="drawer-header">
			<p>{{ prefecture.prefName || "みんなはどこで働くつもりだろう？" }}</p>
		</div>
		<div class="comments" v-show="prefecture.prefName">
			<PrefComment
				v-for="(comment, index) in comments"
				:key="index"
				:userComment="comment"
			/>
			<div v-if="!comments.length" class="no-comment">No Comment👺</div>
		</div>
		<CommentForm
			v-show="prefecture.prefName"
			class="comment-form"
			@emit-input-comment="postComment"
		/>
	</div>
</template>

<script>
	import axios from "axios";
	import PrefComment from "@/components/PrefComment.vue";
	import CommentForm from "@/interfaces/CommentForm.vue";
	export default {
		name: "CommentsBoard",
		components: {
			PrefComment,
			CommentForm,
		},
		props: {
			prefecture: {
				type: Object,
				default: () => ({
					prefName: "",
					prefCode: null,
				}),
			},
			comments: {
				type: Array,
				default: () => [],
			},
		},
		methods: {
			async postComment(comment) {
				const result = await axios
					.post(`/api/comments/${this.prefecture.prefCode}`, {
						id: 1, //TODO: this.userId,
						comment: comment,
					})
					.then((response) => {
						if ((response.status = 201)) {
							/** 成功処理 */
							console.log(response);
							this.$emit("postComment", comment);
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
		height: 100dvh; /* for iOS */
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
	#comments-board.shrink {
		height: 80px;
	}
	#comments-board.shrink::before {
		display: none;
	}

	.drawer-header {
		width: 100%;
		height: 80px;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		font-size: 20px;
		font-weight: bold;
	}
	.comments {
		width: 100%;
		max-height: calc(100% - 160px);
		display: flex;
		flex-direction: row;
		align-content: flex-start;
		justify-content: space-evenly;
		flex-wrap: wrap;
		gap: 15px;
		overflow-y: scroll;
		padding: 10px 20px;
	}
	.no-comment {
		width: 100%;
		height: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 3rem;
	}
	.comment-form {
		position: absolute;
		bottom: 0;
	}
</style>
