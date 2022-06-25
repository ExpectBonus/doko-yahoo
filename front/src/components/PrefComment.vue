<template>
	<div class="comment">
		<span class="comment-text">
			{{ userComment.comment }}
		</span>
		<div class="comment-userinfo">
			<div class="comment-job">
				<span class="comment-job-text">{{ userComment.job }}</span>
			</div>
			<div class="comment-born">
				<span class="comment-born-text">{{ userComment.born_pref }}</span>
			</div>
		</div>
	</div>
</template>
<script>
	export default {
		name: "PrefComment",
		props: {
			userComment: {
				type: Object,
				default: () => {},
				required: true,
			},
		},
	};
</script>
<style scoped>
	.comment {
		position: relative;
		display: flex;
		flex-direction: column;
		align-items: center;
		row-gap: 10px;
		background: #cccccc;
		border-radius: 10px;
		padding: 10px 30px;
	}

	.comment-text {
		width: 100%;
		font-size: 18px;
		text-align: left;
	}

	.comment-userinfo {
		width: 100%;
		display: flex;
		flex-direction: row;
		column-gap: 10px;
		justify-content: flex-end;
		color: #5f5f5f;
	}
</style>
