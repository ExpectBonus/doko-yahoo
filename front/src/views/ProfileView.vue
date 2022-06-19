<template>
  <v-main>
    <v-container>
      <v-row>
        <v-text-field
          label="名前"
          hide-details="auto"
          v-model="name"
        ></v-text-field>
      </v-row>

      <v-radio-group v-model="work" row>
        <v-radio label="エンジニア" value="エンジニア"></v-radio>
        <v-radio label="デザイナー" value="デザイナー"></v-radio>
        <v-radio label="ビジネス" value="ビジネス"></v-radio>
      </v-radio-group>

      <div>
        <v-checkbox v-model="hobbies" label="運動" value="運動"></v-checkbox>
        <v-checkbox v-model="hobbies" label="読書" value="読書"></v-checkbox>
        <v-checkbox v-model="hobbies" label="お酒" value="お酒"></v-checkbox>
      </div>
      <div>===================================</div>
      <div>希望地域</div>
      <select v-model="desiredPrefNum">
        <option v-for="(pref, index) in prefs" :key="pref" :value="index">
          {{ pref }}
        </option>
      </select>

      <v-row justify="center">
        <v-dialog
          v-model="dialog"
          fullscreen
          hide-overlay
          transition="dialog-bottom-transition"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="primary" dark v-bind="attrs" v-on="on">
              Open Dialog
            </v-btn>
          </template>
          <v-card>
            <v-toolbar dark color="primary">
              <v-btn icon dark @click="dialog = false">
                <v-icon>mdi-close</v-icon>
              </v-btn>
              <v-toolbar-title>希望地域</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-toolbar-items>
                <v-btn dark text @click="dialog = false"> Save </v-btn>
              </v-toolbar-items>
            </v-toolbar>
            <v-divider></v-divider>

            <v-list three-line subheader>
              <v-subheader>住みたい地域を複数選んでください</v-subheader>
              <v-card-title>北海道</v-card-title>
              <v-btn
                v-for="(pref, index) in hokkaidouPrefs"
                :key="index"
                :value="pref"
                outline
                rounded
                @click="clickPref"
                :class="colorPref"
                >{{ pref }}</v-btn
              >
              <v-card-title>東北地方</v-card-title>
              <v-btn
                v-for="(pref, index) in touhokuPrefs"
                :key="index"
                :value="pref"
                outline
                rounded
                @click="clickPref"
                :class="colorPref"
                >{{ pref }}</v-btn
              >
            </v-list>
          </v-card>
        </v-dialog>
      </v-row>

      <div>===================================</div>
      <div>出身地</div>
      <select v-model="fromPrefNum">
        <option v-for="(pref, index) in prefs" :key="pref" :value="index">
          {{ pref }}
        </option>
      </select>

      <div>===================================</div>

      <button @click="sendUserInfo">送信！</button>

      <!-- getのテスト -->
      <!-- <button @click="test">adviceをもらう</button> -->

      <div>=============== for debug =================</div>
      <div>名前：{{ name }}</div>
      <div>職種：{{ work }}</div>
      趣味：<span v-for="(hobby, index) in hobbies" :key="index" :value="hobby"
        >{{ hobby }},
      </span>
      <div>希望地域：{{ desiredPref }}</div>
      <div>出身地：{{ fromPref }}</div>
      <div>{{ resData }}</div>
      <div>===================================</div>
    </v-container>
  </v-main>
</template>

<script>
import axios from "axios";

const prefs = [
  null,
  "北海道",
  "青森県",
  "岩手県",
  "宮城県",
  "秋田県",
  "山形県",
  "福島県",
  "茨城県",
  "栃木県",
  "群馬県",
  "埼玉県",
  "千葉県",
  "東京都",
  "神奈川県",
  "新潟県",
  "富山県",
  "石川県",
  "福井県",
  "山梨県",
  "長野県",
  "岐阜県",
  "静岡県",
  "愛知県",
  "三重県",
  "滋賀県",
  "京都府",
  "大阪府",
  "兵庫県",
  "奈良県",
  "和歌山県",
  "鳥取県",
  "島根県",
  "岡山県",
  "広島県",
  "山口県",
  "徳島県",
  "香川県",
  "愛媛県",
  "高知県",
  "福岡県",
  "佐賀県",
  "長崎県",
  "熊本県",
  "大分県",
  "宮崎県",
  "鹿児島県",
  "沖縄県",
];
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
      selectedPrefs: [],
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
    hokkaidouPrefs: {
      get: function () {
        return this.prefs.slice(1, 2);
      },
    },
    touhokuPrefs: {
      get: function () {
        return this.prefs.slice(2, 8);
      },
    },
    kantouPrefs: {
      get: function () {
        return this.prefs.slice(7, 10);
      },
    },
    colorPref: {
      get: function (pref) {
        if (pref in this.selectedPrefs) {
          return "green";
        } else {
          return "";
        }
      },
    },
  },
  methods: {
    // HTTP get methods for test
    test: function () {
      var api = "https://api.adviceslip.com/advice";
      let self = this;

      axios
        .get(api)
        .then(function (res) {
          self.resData = res.data;
        })
        .catch(function (err) {
          console.log(err);
        });
    },
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
    clickPref: function (value) {
      if (value in this.selectedPrefs) {
        this.selectedPrefs.splice(selectedPrefs.indexOf(value), 1);
      } else {
        this.selectedPrefs += value;
      }
    },
  },
};
</script>

<style scoped></style>
