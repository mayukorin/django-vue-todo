module.exports = {
  transpileDependencies: ["vuetify"],
  outputDir: "../static",
  indexPath: "../templates/index.html",
  publicPath: process.env.NODE_ENV === "production" ? "/static" : "/",
  configureWebpack: {
    devServer: {
      watchOptions: {
        poll: true,
      },
    },
  },
  pages: {
    index: {
      entry: "src/main.js",
      title: "TODO",
    }
  }
};
