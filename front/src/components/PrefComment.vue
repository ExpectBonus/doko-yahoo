<template>
  <div class="comment">
    <div class="comment-container-left">
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
  </div>
</template>
<script>
export default {
  name: "HelloWorld",
  props: {
    userComment: {
      type: "",
      default: function () {
        return {
          comment: "",
          born_pref: 0,
          job: "",
        };
      },
    },
  },
};
</script>
<style scoped>
.comment {
  text-align: center;
}
.comment-container-left {
  background: rgb(177, 174, 174);
  border-radius: 30px;
  color: black;
  padding: 30px 30px 10px 30px;
  max-width: 50%;
  margin: 0px auto 40px 0px;
}

.comment-container-left::after {
  content: "";
  position: absolute;
  margin: 0;
  border-top: 40px solid rgb(177, 174, 174);
  border-left: 12px solid transparent;
  border-right: 12px solid transparent;
  transform: rotate(30deg);
  left: 30px;
}

.comment-container-right {
  background: rgb(177, 174, 174);
  border-radius: 30px;
  color: black;
  max-width: 50%;
  padding: 30px 30px 10px 30px;
  margin: 0px 0px 40px auto;
}

.comment-container-right::after {
  content: "";
  position: absolute;
  margin: 0;
  border-top: 40px solid rgb(177, 174, 174);
  border-left: 12px solid transparent;
  border-right: 12px solid transparent;
  transform: rotate(-30deg);
  right: 30px;
}

.comment-text {
  font-family: "Courier New", Courier, monospace;
  font-size: 25px;
}

.comment-userinfo {
  display: flex;
  justify-content: flex-end;
  padding-top: 10px;
  color: rgb(86, 83, 83);
}

.comment-job-text {
  padding: 10px;
}

.comment-born-text {
  padding: 10px;
}
@media screen and (max-width: 500px) {
  .comment-container-left {
    position: relative;
    background: rgb(177, 174, 174);
    border-radius: 30px;
    color: black;
    text-align: center;
    padding: 30px 30px 10px 30px;
    max-width: 90%;
    margin-right: auto;
  }
  .comment-container-right {
    position: relative;
    background: rgb(177, 174, 174);
    border-radius: 30px;
    color: black;
    text-align: left;
    max-width: 90%;
    padding: 30px 30px 10px 30px;
    margin-left: auto;
  }
  .comment-text {
    font-family: "Courier New", Courier, monospace;
    font-size: 15px;
  }
  .comment-job-text {
    padding: 10px;
    font-size: 13px;
  }

  .comment-born-text {
    padding: 10px;
    font-size: 13px;
  }
}
</style>
