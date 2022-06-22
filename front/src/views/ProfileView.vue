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
      isError: false,
      errorMsg: [],
      shortName_f: false,
      selectName_f: false,
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
      params: {},
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
      var err_f;

      // for deactivate submit button
      this.initFlag();

      this.makeParams();
      err_f = this.checkParams();
      if (err_f) {
        // for resubmit
        this.isClicked = false;
        this.isError = true;
        this.setErrorMsg();
        return;
      }
      axios
        .post("http://localhost:5001/user/", this.params)
        .then(function (res) {
          this.resData = res;
          console.log(res);
        })
        .catch(function (err) {
          console.log(err);
        });
    },
    makeParams: function () {
      var uid;

      uid = 1234;
      var params = {
        id: uid,
        username: this.username,
        job: this.job,
        born_pref: this.getPrefIndex(this.born_pref),
        first_pref: this.getPrefIndex(this.selectedPrefs[0]),
        second_pref: this.getPrefIndex(this.selectedPrefs[1]),
        third_pref: this.getPrefIndex(this.selectedPrefs[2]),
        hobbies: this.checkedHobbies,
      };
      this.params = params;
      console.log(params);
    },
    checkParams: function () {
      // if (!isUniqueId(params["id"])) {
      //   return true;
      // }
      var name;
      var job;
      var err_f = false;

      name = this.params["username"].length;
      job = this.params["job"].length;
      if (name == 0) {
        this.shortName_f = true;
        err_f = true;
      }
      if (job == 0) {
        this.selectJob_f = true;
        err_f = true;
      }
      // if (name <= 0 && 30 <= name && isUniqueName(name)) {
      //   return true;
      // }
      if (err_f) {
        return true;
      }
      return false;
    },
    isSelectedPrefs: function () {
      if (this.selectedPrefs.length == 0) {
        return false;
      }
      return true;
    },
    isAllPrefs: function () {
      if (this.selectedPrefs.length >= 3) {
        return true;
      }
      return false;
    },
    setErrorMsg: function () {
      if (this.shortName_f) {
        this.errorMsg[this.errorMsg.length] =
          "名前を入力してください。（必須）";
      }
      if (this.selectJob_f) {
        this.errorMsg[this.errorMsg.length] = "職業を選んでください。（必須）";
      }
    },
    initFlag: function () {
      this.isClicked = true;
      this.errorMsg = [];
      this.isError = false;
      this.shortName_f = false;
      this.selectJob_f = false;
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
