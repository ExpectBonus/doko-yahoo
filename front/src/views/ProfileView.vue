<template src="./ProfileView.html"></template>
<style src="./ProfileView.css"></style>
<script>
import { prefectures as prefs } from "./prefectures.js";
import { hobbies_list } from "./hobbies.js";
import { regionPrefs } from "./prefectures.js";
import axios from "axios";

export default {
  name: "ProfileView",
  data: function () {
    return {
      // import prefs
      regionPrefs,
      hobbies_list,
      // input
      username: "",
      job: "",
      prefs,
      born_pref: "",
      first_pref: "",
      second_pref: "",
      third_pref: "",
      selectedPrefs: [],
      checkedHobbies: [],
      params: {},
      // button
      isClicked: false,
      // error flag
      errorMsg: [],
      isError: false,
      shortName_f: false,
      selectJob_f: false,
      selectBorn_f: false,
      selectFirst_f: false,
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
        if (pref == null) {
          return null;
        }
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
        .post("http://localhost:5001/api/user/", this.params)
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
      var born;
      var first;
      var err_f = false;

      name = this.params["username"].length;
      job = this.params["job"].length;
      born = this.params["born_pref"];
      first = this.params["first_pref"];
      if (name == 0) {
        this.shortName_f = true;
        err_f = true;
      }
      if (job == 0) {
        this.selectJob_f = true;
        err_f = true;
      }
      if (born == -1) {
        this.selectBorn_f = true;
        err_f = true;
      }
      if (first == -1) {
        this.selectFirst_f = true;
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
    isAllPrefs: function (pref) {
      if (this.selectedPrefs.length >= 3) {
        if (this.selectedPrefs.indexOf(pref) == -1) {
          return true;
        }
      }
      return false;
    },
    setErrorMsg: function () {
      if (this.shortName_f) {
        this.errorMsg[this.errorMsg.length] = "名前を入力してください。";
      }
      if (this.selectJob_f) {
        this.errorMsg[this.errorMsg.length] = "職業を選んでください。";
      }
      if (this.selectBorn_f) {
        this.errorMsg[this.errorMsg.length] = "出身地を選んでください。";
      }
      if (this.selectFirst_f) {
        this.errorMsg[this.errorMsg.length] =
          "住みたい都道府県の第1希望を選んでください。";
      }
    },
    initFlag: function () {
      this.isClicked = true;
      this.errorMsg = [];
      this.isError = false;
      this.shortName_f = false;
      this.selectJob_f = false;
      this.shortBorn_f = false;
      this.selectFirst_f = false;
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
