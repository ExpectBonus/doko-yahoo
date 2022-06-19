import Vue from "vue";
import Vuetify from "vuetify/lib/framework";
import colors from "vuetify/lib/util/colors";

Vue.use(Vuetify);

export default new Vuetify({
	theme: {
		themes: {
			light: {
				primary: colors.lightGreen.darken4, // #33691E
				secondary: colors.blueGrey.lighten4, // #CFD8DC
				accent: colors.red.accent3, // #FF1744
				yahoo: "#FF0033",
			},
		},
	},
});
