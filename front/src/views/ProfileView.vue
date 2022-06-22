<template src="./ProfileView.html"></template>
<style src="./ProfileView.css"></style>
<script>
import { prefectures as prefs } from "./prefectures.js";
import { regionPrefs } from "./prefectures.js";
import axios from "axios";

export default {
  name: "ProfileView",
  data: function () {
    return {
      hobbies: [],
      selectedHobbies: [],
      username: "",
      job: "",
      prefs,
      born: "",
      regionPrefs,
      desiredPrefNum: 0,
      born_pref: "",
      first_pref: "",
      second_pref: "",
      third_pref: "",
      selectedPrefs: [],
      isClicked: false,
      hobbies_list: [
        {
          emoji: "🍻",
          name: "飲み会",
        },
        {
          emoji: "☕",
          name: "カフェ",
        },
        {
          emoji: "🎮",
          name: "ゲーム",
        },
        {
          emoji: "📷",
          name: "カメラ",
        },
        {
          emoji: "⚾",
          name: "野球",
        },
        {
          emoji: "⚽",
          name: "サッカー",
        },
        {
          emoji: "🏀",
          name: "バスケットボール",
        },
        {
          emoji: "🎹",
          name: "ピアノ",
        },
        {
          emoji: "💃",
          name: "ダンス",
        },
        {
          emoji: "🚗",
          name: "ドライブ",
        },
        {
          emoji: "✈️",
          name: "旅行",
        },
      ],
      checkedHobbies: [],
    };
  },
  computed: {
    born_prefNum: {
      get: function () {
        return this.prefs.indexOf(this.born_pref);
      },
    },
    getPrefIndex: function () {
      return function (pref) {
        return this.prefs.indexOf(pref);
      };
    },
  },
  methods: {
    sendUserInfo: function () {
      var params;

      // for deactivate submit button
      this.isClicked = true;

      params = this.makeParams();
      axios
        .post("/user", this.params)
        .then(function (res) {
          this.resData = res;
          console.log(res);
        })
        .catch(function (err) {
          console.log(err);
        });
    },
    makeParams: function () {
      var params = {
        id: 1234,
        username: this.username,
        job: this.job,
        born_pref: this.getPrefIndex(this.born_pref),
        first_pref: 1,
        second_pref: 1,
        third_pref: 1,
        hobbies: this.hobbies,
      };
      console.log(params["born_pref"]);
    },
    printPrefs: function (prefs) {
      if (prefs.length == 1) {
        return prefs[0];
      }
      var ret = prefs[0];
      for (let i = 1; i < prefs.length; i++) {
        ret += ", " + prefs[i];
      }
      return ret;
    },
  },
};
</script>
