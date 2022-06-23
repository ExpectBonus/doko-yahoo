<template>
  <div>
    <div v-if="isError" class="error-msg">
      <span v-for="(err, index) in errorMsg" :key="index">
        {{ err }}
        <br />
      </span>
    </div>
    <div class="profile">
      <span v-if="isClicked" class="loading">
        <span> </span>
        <span> </span>
      </span>
      <div v-else class="content">
        <img src="../assets/profile_icon.jpeg" />
        <div class="input-form">
          <div class="label-form">
            <img class="label-icon" src="../assets/badge.png" />
            <span class="label-name">名前</span
            ><span class="required-mark">＊</span>
          </div>
          <div class="input-username">
            <label class="input-username-label">
              <input
                v-if="username"
                type="text"
                class="filled-username-field"
                v-model="username"
                placeholder="矢風 太郎"
                required
              />
              <input
                v-else
                type="text"
                class="input-username-field"
                v-model="username"
                placeholder="矢風 太郎"
                required
              />
            </label>
          </div>
        </div>
        <div class="input-form">
          <div class="label-form">
            <img class="label-icon" src="../assets/business_center.png" />
            <span class="label-name">職種</span
            ><span class="required-mark">＊</span>
          </div>
          <div class="select-jobs">
            <input
              type="radio"
              class="input-job-field"
              id="engineer"
              name="job"
              value="エンジニア"
              v-model="job"
            />
            <label for="engineer" class="label-job">エンジニア</label>
            <input
              type="radio"
              class="input-job-field"
              id="designer"
              name="job"
              value="デザイナー"
              v-model="job"
            />
            <label for="designer" class="label-job">デザイン</label>
            <input
              type="radio"
              class="input-job-field"
              id="business"
              name="job"
              value="ビジネス"
              v-model="job"
            />
            <label for="business" class="label-job">ビジネス</label>
          </div>
        </div>

        <div class="input-form">
          <div class="label-form">
            <img class="label-icon" src="../assets/home.png" />
            <span class="label-name">今、どこに住んでいる？</span
            ><span class="required-mark">＊</span>
          </div>
          <div class="modal-button-field">
            <a
              href="#select-born-pref"
              v-if="born_pref"
              class="modal-button-selected"
            >
              <div class="show-selected-pref">
                {{ born_pref }}<span class="arrow-icon">▶️</span>
              </div>
            </a>
            <a href="#select-born-pref" v-else class="modal-button">
              <span class="modal-button-text">都道府県を選ぶ</span>
            </a>
          </div>
          <div class="modal-wrapper" id="select-born-pref">
            <a href="#!" class="modal-overlay"></a>
            <div class="modal-window">
              <div class="modal-content">
                <p class="modal-title">1つ選んでください</p>
                <span v-if="born_pref" class="selected-born">{{
                  born_pref
                }}</span>
                <div
                  class="section-container"
                  v-for="(value, key) in regionPrefs"
                  :key="key"
                  :value="value"
                >
                  <div class="label-section">
                    <span class="label-born-field">{{ value.section }}</span>
                    <div class="prefs-container">
                      <span
                        v-for="(pref, key) in value.prefs"
                        :key="key"
                        :value="pref"
                      >
                        <input
                          type="radio"
                          class="input-born-field"
                          :id="pref"
                          name="born"
                          :value="pref"
                          v-model="born_pref"
                        />
                        <label :for="pref" class="label-born"
                          ><span class="pref-field">{{ pref }}</span></label
                        >
                      </span>
                    </div>
                  </div>
                </div>
              </div>
              <a href="#!" class="modal-close"
                >✖️<i class="far fa-times-circle"></i
              ></a>
            </div>
          </div>
        </div>

        <div class="input-form">
          <div class="label-form">
            <img class="label-icon" src="../assets/home_work.png" />
            <span class="label-name">就職後はどこに住みたい？</span
            ><span class="required-mark">＊</span>
          </div>

          <div class="modal-button-field">
            <a
              href="#select-three-pref"
              v-if="selectedPrefs.length"
              class="modal-button-selected"
            >
              <div class="show-selected-pref">
                <span class="three-pref">{{ printPrefs(selectedPrefs) }}</span
                ><span class="arrow-icon">▶️</span>
              </div>
            </a>
            <a href="#select-three-pref" v-else class="modal-button">
              <span class="modal-button-text">都道府県を選ぶ</span>
            </a>
          </div>
          <div class="modal-wrapper" id="select-three-pref">
            <a href="#!" class="modal-overlay"></a>
            <div class="modal-window">
              <div class="modal-content">
                <p class="modal-title">最大3つまで選んでください</p>
                <div v-if="isSelectedPrefs()" class="show-prefs-container">
                  <div v-for="(pref, index) in selectedPrefs" :key="index">
                    <span class="selected-born"
                      >第{{ index + 1 }}希望：{{ pref }}</span
                    >
                  </div>
                </div>
                <div
                  class="section-container"
                  v-for="(regionPref, sectionIndex) in regionPrefs"
                >
                  <div class="label-section">
                    <span class="label-born-field">{{
                      regionPref.section
                    }}</span>
                    <div class="prefs-container">
                      <span v-for="(pref, prefIndex) in regionPref.prefs">
                        <!-- <input type="checkbox" class="input-born-field" :id="getPrefIndex(pref)"
										name="three" :value="pref" v-model="selectedPrefs" @click="clickPref"
										v-bind:disabled="isSelected"> -->
                        <input
                          type="checkbox"
                          class="input-born-field"
                          :id="getPrefIndex(pref)"
                          name="three"
                          :value="pref"
                          v-model="selectedPrefs"
                          :disabled="isAllPrefs(pref)"
                        />
                        <label :for="getPrefIndex(pref)" class="label-born">
                          <span class="pref-field">{{ pref }}</span>
                        </label>
                      </span>
                    </div>
                  </div>
                </div>
              </div>
              <a href="#!" class="modal-close"
                >✖️<i class="far fa-times-circle"></i
              ></a>
            </div>
          </div>
        </div>

        <div class="input-form">
          <div class="label-form">
            <img class="label-icon" src="../assets/interests.png" />
            <span class="label-name">趣味</span>
          </div>
          <!-- <HobbiesSelector @selectedHobbies="selectedHobbies = $event" /> -->
          <div id="hobbies-selector">
            <div
              class="hobby"
              v-for="(hobby, index) in hobbies_list"
              :key="index"
            >
              <input
                type="checkbox"
                :id="'hobby' + index"
                :value="hobby.name"
                v-model="checkedHobbies"
              />
              <label class="label-hobbies" :for="'hobby' + index">
                <span class="emoji">{{ hobby.emoji }}</span>
                {{ hobby.name }}
              </label>
            </div>
          </div>
        </div>
        <div class="send-button-field">
          <a href="#">
            <button v-if="!isClicked" class="send-button" @click="sendUserInfo">
              利用を始める
            </button>
            <button v-else class="send-button-clicked">利用を始める</button>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { prefectures as prefs } from "./prefectures.js"
import { hobbies_list } from "./hobbies.js"
import { regionPrefs } from "./prefectures.js"
import axios from "axios"

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
    }
  },
  computed: {
    getPrefIndex: function () {
      return function (pref) {
        if (pref == null) {
          return null
        }
        return this.prefs.indexOf(pref)
      }
    },
  },
  methods: {
    sendUserInfo: function () {
      let err_f

      // for deactivate submit button
      this.initFlag()

      err_f = this.checkParams()
      if (err_f) {
        // for resubmit
        this.isClicked = false
        this.isError = true
        this.setErrorMsg()
        return
      }
      this.makeParams()
      axios
        .post("http://localhost:5001/api/user/", this.params)
        .then(function (res) {
          this.resData = res
          console.log(res)
        })
        .catch(function (err) {
          console.log(err)
        })
    },
    makeParams: function () {
      let uid

      uid = 1234
      let params = {
        id: uid,
        username: this.username,
        job: this.job,
        born_pref: this.getPrefIndex(this.born_pref),
        first_pref: this.getPrefIndex(this.selectedPrefs[0]),
        second_pref: this.getPrefIndex(this.selectedPrefs[1]),
        third_pref: this.getPrefIndex(this.selectedPrefs[2]),
        hobbies: this.checkedHobbies,
      }
      this.params = params
      console.log(params)
    },
    checkParams: function () {
      // if (!isUniqueId(params["id"])) {
      //   return true;
      // }

      let name
      let err_f = false
      let errorColumns = []

      name = this.name.length
      born = this.born
      if (name == 0) {
        this.shortName_f = true
        err_f = true
      }
      if (!this.job) {
        this.selectJob_f = true
        err_f = true
      }
      if (!this.born) {
        this.selectBorn_f = true
        err_f = true
      }
      if (!this.first) {
        this.selectFirst_f = true
        err_f = true
      }

      // if (name <= 0 && 30 <= name && isUniqueName(name)) {
      //   return true;
      // }
      if (err_f) {
        return true
      }
      return false
    },
    isSelectedPrefs: function () {
      if (this.selectedPrefs.length == 0) {
        return false
      }
      return true
    },
    isAllPrefs: function (pref) {
      if (this.selectedPrefs.length >= 3) {
        if (this.selectedPrefs.indexOf(pref) == -1) {
          return true
        }
      }
      return false
    },
    setErrorMsg: function () {
      if (this.shortName_f) {
        this.errorMsg[this.errorMsg.length] = "名前を入力してください。"
      }
      if (this.selectJob_f) {
        this.errorMsg[this.errorMsg.length] = "職業を選んでください。"
      }
      if (this.selectBorn_f) {
        this.errorMsg[this.errorMsg.length] = "出身地を選んでください。"
      }
      if (this.selectFirst_f) {
        this.errorMsg[this.errorMsg.length] =
          "住みたい都道府県の第1希望を選んでください。"
      }
    },
    initFlag: function () {
      this.isClicked = true
      this.errorMsg = []
      this.isError = false
      this.shortName_f = false
      this.selectJob_f = false
      this.shortBorn_f = false
      this.selectFirst_f = false
    },
    printPrefs: function (prefs) {
      if (prefs.length == 1) {
        return prefs[0]
      }
      let ret = prefs[0]
      for (let i = 1; i < prefs.length; i++) {
        ret += ", " + prefs[i]
      }
      return ret
    },
  },
}
</script>
<style scoped>
/* common css */

* {
  text-align: center;
}

.content {
  border-radius: 20px;
  min-height: 1000px;
}

.profile {
  position: relative;
  z-index: 1;
  background: #ffffff;
  min-height: 850px;
  max-width: 60%;
  margin: 0 auto 100px;
  text-align: center;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.6), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
}

@media screen and (max-width: 959px) {
  .profile {
    position: relative;
    z-index: 1;
    background: #ffffff;
    min-height: 1000px;
    margin: 0 auto 100px;
    max-width: 100%;
    text-align: center;
    box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
  }

  .send-button-field {
    margin-top: 80px !important;
  }

  .content {
    border-radius: 20px;
    min-height: 1100px;
  }
}

.input-form {
  padding: 10px;
  min-height: 94px;
  display: flex;
  flex-direction: column;
}

.label-form {
  /* margin-right: 200px; */
  /* width: 80%; */
}

.required-mark {
  padding: 10px;
  font-size: 15px;
  color: red;
}

.label-name {
  margin-left: 10px;
  margin-bottom: 15px;
  font-family: "Hiragino Kaku Gothic ProN";
  font-style: normal;
  font-weight: 400;
  font-size: 25px;
  line-height: 27px;
  align-items: center;
  letter-spacing: 0.01em;
}

.label-icon {
  vertical-align: bottom;
}

/* username */

.input-username-field {
  width: 300px;
  height: 40px;
  background: #eeeeee !important;
  border: 1px solid black;
  border-radius: 10px !important;
}

.filled-username-field {
  width: 300px;
  height: 40px;
  background: white;
  border: 3px solid #008277 !important;
  border-radius: 10px !important;
}

/* .input-username-field:hover {
	border: 1px solid #0094ff;
	background-color: #cbe9ff;
} */

.input-username {
  height: 40px;
  margin: 10px;
}

.input-username input[type="text"] {
  font: 18px/24px sans-serif;
  box-sizing: border-box;
  padding: 0.3em;
  transition: 0.3s;
  letter-spacing: 1px;
  color: black;
  border: 1px solid #1b2538;
  border-radius: 4px;
  background-color: white;
}

.input-username-label input[type="text"]:focus {
  border: 1px solid #16998e;
  outline: none;
  box-shadow: 0 0 5px 1px #16998e;
}

/* job */

.select-jobs {
  margin: 10px;
}

.input-job-field {
  /* border: 1px solid #1b2538; */
  clip: rect(1px, 1px, 1px, 1px);
  position: absolute !important;
}

.label-job {
  display: inline-block;
  padding: 0.5rem 1rem;
  margin-right: 18px;
  border-radius: 7px;
  border: 2px solid grey;
  transition: all 0.3s;
}

.input-job-field:checked + .label-job {
  background: #008277;
  color: #fff;
  border-radius: 10px;
  text-shadow: 0 0 1px rgba(0, 0, 0, 0.7);
}

.input-job-field:focus + .label-job {
  box-shadow: 0 0 5px 1px #16998e;
  outline-color: #16998e;
  outline-offset: 0px;
  outline-style: auto;
  outline-width: 5px;
}

/* dialog */

.select-born {
  margin: 10px;
}

.label-section {
  font-family: "Hiragino Kaku Gothic ProN";
  font-style: normal;
  font-weight: 400;
  font-size: 30px;
  /* line-height: 27px; */
  letter-spacing: 0.01em;
  text-align: left;
  margin: 20px;
}

.section-container {
  min-width: 150px;
}

.prefs-container {
  /* width: 100%;
	min-height: 50px; */
}

.input-born-field {
  /* border: 1px solid #1b2538; */
  clip: rect(1px, 1px, 1px, 1px);
  position: absolute !important;
  margin: 20px;
}

.prefs-container {
  /* この要素はflexコンテナとなり、子要素は自動的にflexアイテムとなる */
  display: flex;

  /* 横並びに表示する */
  flex-direction: row;

  /* 画面幅に収まらない場合は折り返す */
  flex-wrap: wrap;
}

.pref-field {
  font-size: 20px;
  text-align: center;
  vertical-align: middle;
  padding: 20px;
}

.label-born {
  margin: 6px;
  padding: 5px;
  border-radius: 7px;
  border: 2px solid grey;
  background-color: #d9d9d9;
  transition: all 0.3s;
}

.label-born-field {
}

.selected-born {
  font-size: 20px;
  background-color: #008277;
  color: white;
  /* padding: 10px 50px 15px 50px; */
  padding: 10px 60px 15px 60px;
  border-radius: 7px;
}

.show-prefs-container {
  height: 110px;
  padding: 10px;
  width: 350px;
  margin: 0% auto;
  background-color: #008277;
  border-radius: 20px;
}

.input-born-field:checked + .label-born {
  background: #008277;
  color: white;
  border-radius: 10px;
  text-shadow: 0 0 1px rgba(0, 0, 0, 0.7);
}

.input-born-field:focus + .label-born {
  /* outline-color: #4D90FE; */
  outline-offset: 0px;
  outline-style: auto;
  outline-width: 5px;
}

.modal-button-field {
  padding: 20px;
  min-width: 200px;
  max-width: 350px;
  text-align: center;
  margin: 0 auto;
}

.modal-button a {
  background: #eee;
  border-radius: 3px;
  justify-content: space-around;
  align-items: center;
  margin: 0 auto;
  max-width: 280px;
  padding: 10px 25px;
  color: #313131;
  transition: 0.3s ease-in-out;
  font-weight: 500;
}

.modal-button a:hover {
  background: #313131;
  color: #fff;
}

.modal-button a:after {
  content: "";
  width: 5px;
  height: 5px;
  border-top: 3px solid #313131;
  border-right: 3px solid #313131;
  transform: rotate(45deg) translateY(-50%);
  position: absolute;
  top: 50%;
  right: 20px;
  border-radius: 1px;
  transition: 0.3s ease-in-out;
}

.modal-button a:hover:after {
  border-color: #fff;
}

.modal-wrapper {
  z-index: 999;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  padding: 40px 10px;
  text-align: center;
}

.modal-button {
  color: grey;
  background-color: #eeeeee;
  font-weight: bold;
  text-align: center;
  cursor: pointer;
  padding: 20px;
  margin: 20px;
  /* padding: 12px 2px; */
  max-width: 300px;
  left: 200px;
  text-decoration: none;
}

.modal-button-selected {
  color: white;
  background-color: #008277;
  font-weight: bold;
  text-align: center;
  cursor: pointer;
  font-size: 30px;
  max-width: 300px;
  /* padding: 10px 10px 14px 200px; */
  border-radius: 20px;
  left: 200px;
  text-decoration: none;
}

.modal-button-text {
  padding: 20px;
  font-size: 20px;
}

.modal-button:active {
  /*ボタンを押したとき*/
  -webkit-transform: translateY(2px);
  transform: translateY(2px);
  /*下に動く*/
}

/*アイコンを表示*/
.modal-button:after {
  font-family: "Font Awesome 5 Free";
  content: ">";
  padding-left: 8px;
}

/*ラベルホバー時*/
.modal-button:hover {
  color: #ffffff;
  background-color: #008277;
  transition: 0.6s;
}

.modal-wrapper:not(:target) {
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.3s, visibility 0.3s;
}

.modal-wrapper:target {
  opacity: 1;
  visibility: visible;
  transition: opacity 0.4s, visibility 0.4s;
}

.modal-wrapper::after {
  display: inline-block;
  height: 100%;
  margin-left: -0.05em;
  vertical-align: middle;
  content: "";
}

.modal-wrapper .modal-window {
  box-sizing: border-box;
  display: inline-block;
  z-index: 20;
  position: relative;
  max-width: 700px;
  padding: 10px 30px 25px;
  border-radius: 2px;
  background: #fff;
  box-shadow: 0 0 30px rgba(0, 0, 0, 0.6);
  vertical-align: middle;
}

.modal-wrapper .modal-window .modal-content {
  max-height: 80vh;
  overflow-y: auto;
  /* text-align: left */
}

.modal-title {
  position: relative;
  font-size: 25px;
  padding: 20px;
  height: 70px;
  background: #e6f4ff;
  color: #5c98d4;
  font-weight: bold;
  vertical-align: middle;
}

.modal-title:after {
  position: absolute;
  content: "";
  top: 100%;
  border: 15px solid transparent;
  border-top: 15px solid #e6f4ff;
  width: 0;
  height: 0;
}

.modal-title p {
  margin: 0;
  padding: 0;
}

/* .modal-content p {
	margin: 10px 0 0 0;
} */

.modal-overlay {
  z-index: 10;
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background: rgba(0, 0, 0, 0.8);
}

.modal-wrapper .modal-close {
  z-index: 20;
  position: absolute;
  top: 5px;
  right: 5px;
  width: 35px;
  color: #95979c !important;
  font-size: 30px;
  font-weight: 700;
  line-height: 35px;
  text-align: center;
  text-decoration: none;
  text-indent: 0;
}

.modal-wrapper .modal-close:hover {
  color: #2b2e38 !important;
}

.show-selected-pref {
  font-size: 20px;
  display: flex;
  justify-content: space-between !important;
  background-color: #008277;
  color: white;
  padding: 10px 30px 15px 30px;
  border-radius: 7px;
}

.three-pref {
  margin-right: 5px;
}

/* hobiies */
#hobbies-selector {
  font-family: MyFontFamily, sans-serif;
  position: relative;
  width: 100%;
  height: 100px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
  gap: 10px;
  flex-wrap: wrap;
  max-width: 400px;
  margin: 0 auto;
  padding-top: 20px;
}

.hobby {
  position: relative;
}

input[type="checkbox"] {
  opacity: 0;
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  margin: 0;
  cursor: pointer;
}

.label-hobbies {
  width: 100%;
  height: 100%;
  text-align: center;
  font-weight: bold;
  color: #292929;
  background-color: #d9d9d9;
  border-radius: 10px;
  border: 1px solid #d9d9d9;
  padding: 0.3rem;
  transition: all 0.3s ease-out;
}

input[type="checkbox"]:checked + label {
  color: #ffffff;
  background-color: #008277;
  border-color: #008277;
}

@font-face {
  font-family: MyFontFamily;
  src: local("Hiragino Kaku Gothic ProN"), local("Meiryo");
}

@font-face {
  font-family: MyFontFamily;
  src: local("Segoe UI Emoji"), local("Segoe UI Symbol"),
    local("Apple Color Emoji"), local("Noto Color Emoji"), local("Noto Emoji");
  unicode-range:
		/*U+23, U+2A, U+30-39,*/ U+A9, U+AE, U+200D, U+203C, U+2049,
    U+20E3, U+2122, U+2139, U+2194-2199, U+21A9-21AA, U+231A-231B, U+2328,
    U+23CF, U+23E9-23F3, U+23F8-23FA, U+24C2, U+25AA-25AB, U+25B6, U+25C0,
    U+25FB-25FE, U+2600-2604, U+260E, U+2611, U+2614-2615, U+2618, U+261D,
    U+2620, U+2622-2623, U+2626, U+262A, U+262E-262F, U+2638-263A, U+2640,
    U+2642, U+2648-2653, U+2660, U+2663, U+2665-2666, U+2668, U+267B, U+267F,
    U+2692-2697, U+2699, U+269B-269C, U+26A0-26A1, U+26AA-26AB, U+26B0-26B1,
    U+26BD-26BE, U+26C4-26C5, U+26C8, U+26CE-26CF, U+26D1, U+26D3-26D4,
    U+26E9-26EA, U+26F0-26F5, U+26F7-26FA, U+26FD, U+2702, U+2705, U+2708-270D,
    U+270F, U+2712, U+2714, U+2716, U+271D, U+2721, U+2728, U+2733-2734, U+2744,
    U+2747, U+274C, U+274E, U+2753-2755, U+2757, U+2763-2764, U+2795-2797,
    U+27A1, U+27B0, U+27BF, U+2934-2935, U+2B05-2B07, U+2B1B-2B1C, U+2B50,
    U+2B55, U+3030, U+303D, U+3297, U+3299, U+FE0F, U+1F004, U+1F0CF,
    U+1F170-1F171, U+1F17E-1F17F, U+1F18E, U+1F191-1F19A, U+1F1E6-1F1FF,
    U+1F201-1F202, U+1F21A, U+1F22F, U+1F232-1F23A, U+1F250-1F251, U+1F300-1F321,
    U+1F324-1F393, U+1F396-1F397, U+1F399-1F39B, U+1F39E-1F3F0, U+1F3F3-1F3F5,
    U+1F3F7-1F4FD, U+1F4FF-1F53D, U+1F549-1F54E, U+1F550-1F567, U+1F56F-1F570,
    U+1F573-1F57A, U+1F587, U+1F58A-1F58D, U+1F590, U+1F595-1F596, U+1F5A4-1F5A5,
    U+1F5A8, U+1F5B1-1F5B2, U+1F5BC, U+1F5C2-1F5C4, U+1F5D1-1F5D3, U+1F5DC-1F5DE,
    U+1F5E1, U+1F5E3, U+1F5E8, U+1F5EF, U+1F5F3, U+1F5FA-1F64F, U+1F680-1F6C5,
    U+1F6CB-1F6D2, U+1F6E0-1F6E5, U+1F6E9, U+1F6EB-1F6EC, U+1F6F0, U+1F6F3-1F6F8,
    U+1F910-1F93A, U+1F93C-1F93E, U+1F940-1F945, U+1F947-1F94C, U+1F950-1F96B,
    U+1F980-1F997, U+1F9C0, U+1F9D0-1F9E6, U+E0062-E0063, U+E0065, U+E0067,
    U+E006C, U+E006E, U+E0073-E0074, U+E0077, U+E007F;
}

.emoji {
  font-weight: normal;
}

.send-button {
  /* margin-top: 30px; */
  position: relative;
  z-index: 1;
  font-size: 18px;
  overflow: hidden;
  width: 320px;
  padding: 1em;
  cursor: pointer;
  line-height: 1.4;
  transition: color 0.3s cubic-bezier(0.02, 0.01, 0.47, 1),
    transform 0.3s cubic-bezier(0.02, 0.01, 0.47, 1);
  color: #ffffff;
  border: none;
  border-width: 0;
  border-color: transparent;
  border-radius: 100px;
  background: #009688;
}

.send-button-clicked {
  margin-top: 30px;
  position: relative;
  z-index: 1;
  font-size: 18px;
  overflow: hidden;
  width: 320px;
  padding: 1em;
  cursor: pointer;
  line-height: 1.4;
  transition: color 0.3s cubic-bezier(0.02, 0.01, 0.47, 1),
    transform 0.3s cubic-bezier(0.02, 0.01, 0.47, 1);
  color: #ffffff;
  border: none;
  border-width: 0;
  border-color: transparent;
  border-radius: 100px;
  background: grey;
}

.send-button:after,
.send-button:before {
  position: absolute;
  z-index: -1;
  right: 0;
  bottom: 0;
  width: 100px;
  height: 100px;
  content: "";
  transition: transform 0.15s cubic-bezier(0.02, 0.01, 0.47, 1),
    opacity 0.15s cubic-bezier(0.02, 0.01, 0.47, 1);
  -webkit-transform: translate(100%, -25%) translateZ(0);
  transform: translate(100%, -25%) translateZ(0);
  opacity: 0;
  border-radius: 50%;
  background: #009688;
}

.send-button:after,
.send-button:before {
  background: #ffffff;
}

.send-button:hover {
  transition: all 0.5s cubic-bezier(0.02, 0.01, 0.47, 1);
  -webkit-transform: scale(1.1) translateZ(0);
  transform: scale(1.1) translateZ(0);
  color: #ffffff;
  box-shadow: 0 1px 8px rgba(0, 0, 0, 0.3);
}

.send-button:hover:before {
  transition: transform 0.2s cubic-bezier(0.02, 0.01, 0.47, 1),
    opacity 0.2s cubic-bezier(0.02, 0.01, 0.47, 1);
  -webkit-transform: translate3d(50%, 0, 0) scale(0.9);
  transform: translate3d(50%, 0, 0) scale(0.9);
  opacity: 0.15;
}

.send-button:hover:after {
  transition: transform 0.2s cubic-bezier(0.02, 0.01, 0.47, 1) 0.05s,
    opacity 0.2s cubic-bezier(0.02, 0.01, 0.47, 1) 0.05s;
  -webkit-transform: translate(50%) scale(1.1);
  transform: translate(50%) scale(1.1);
  opacity: 0.25;
}

.send-button:active {
  opacity: 0.5;
}

.send-button:focus {
  color: #ffffff;
}

.send-button-field {
  margin-top: 40px;
  /* margin-bottom: 20px; */
}

/* loading */
*,
*:before,
*:after {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}

.loading {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 68px;
  height: 50px;
  -webkit-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}

.loading:before,
.loading:after,
.loading span {
  position: absolute;
  top: 0;
  left: 0;
  display: block;
  width: 14px;
  height: 50px;
  content: "";
  -webkit-animation: loading20 1.5s ease-in-out infinite;
  animation: loading20 1.5s ease-in-out infinite;
  -webkit-transform-origin: 100% 100%;
  transform-origin: 100% 100%;
}

.loading:before {
  background-color: #d81b60;
}

.loading:after {
  left: 18px;
  -webkit-animation-delay: -0.3s;
  animation-delay: -0.3s;
  background-color: #3949ab;
}

.loading span {
  left: 36px;
  -webkit-animation-delay: -0.6s;
  animation-delay: -0.6s;
  background-color: #00acc1;
}

.loading span:nth-child(2) {
  left: 54px;
  -webkit-animation-delay: -1.2s;
  animation-delay: -1.2s;
  background-color: #fb8c00;
}

@-webkit-keyframes loading20 {
  0% {
    -webkit-transform: scaleY(0);
    transform: scaleY(0);
    opacity: 0;
  }

  50% {
    -webkit-transform: scaleY(1);
    transform: scaleY(1);
    opacity: 1;
  }

  100% {
    -webkit-transform: scaleY(0);
    transform: scaleY(0);
    opacity: 0;
  }
}

@keyframes loading20 {
  0% {
    -webkit-transform: scaleY(0);
    transform: scaleY(0);
    opacity: 0;
  }

  50% {
    -webkit-transform: scaleY(1);
    transform: scaleY(1);
    opacity: 1;
  }

  100% {
    -webkit-transform: scaleY(0);
    transform: scaleY(0);
    opacity: 0;
  }
}

/* error */

.error-msg {
  position: relative;
  border: 3px double #da4033;
  border-radius: 5px;
  margin: 20px 0;
  padding: 20px 20px 5px 20px;
}

.error-msg::before {
  content: "入力が正しくありません";
  position: absolute;
  background-color: white;
  color: #da4033;
  font-weight: bold;
  left: 20px;
  top: -23px;
  padding: 10px;
}
</style>
