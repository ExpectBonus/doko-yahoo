<template src="./ProfileView.html"></template>
<style src="./ProfileView.css"></style>
<script>
import { prefectures as prefs } from "./prefectures.js";
import axios from "axios";

export default {
  name: "ProfileView",
  data: function () {
    return {
      hobbies: [],
      name: "",
      work: "",
      prefs,
      desiredPrefNum: 0,
      fromPrefNum: 0,
      resData: [],
      params: {
        id: 10,
        username: this.name,
        job: this.work,
        born_pref: this.fromPrefNum,
        first_pref: this.desiredPrefNum,
        second_pref: 1,
        third_pref: 1,
        hobbies: this.hobbies,
      },
    };
  },
  computed: {
    desiredPref: {
      get: function () {
        return this.prefs[this.desiredPrefNum];
      },
    },
    fromPref: {
      get: function () {
        return this.prefs[this.fromPrefNum];
      },
    },
  },
  methods: {
    sendUserInfo: function () {
      axios
        .post("/user", this.params)
        .then(function (res) {
          console.log(res);
        })
        .catch(function (err) {
          console.log(err);
        });
    },
  },
};
</script>
