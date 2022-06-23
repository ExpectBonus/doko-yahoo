<template>
  <div class="comment"></div>
</template>
<script>
export default {
  name: "PrefComment",
  props: {
    userComment: {
      type: "object",
      default: function () {
        return {
          comment: "仮のコメント",
          born_pref: 12, //←テスト用
          job: "エンジニア",
        };
      },
    },
  },
};
</script>
<style scoped></style>
