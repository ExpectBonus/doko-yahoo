const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: ["vuetify"],
  devServer: {
    port: 8080,
    proxy: {
      "^/api/": {
        target: "http://doko-yahoo_back_1:5001",
        changeOrigin: true,
        pathRewrite: { "^/api/": "/api/" },
        logLevel: "debug",
      },
    },
  },
});
