module.exports = {
    publicPath: "./",
    outputDir: "dist",
    assetsDir:"static",
    devServer: {
        proxy: {
            '/api': {
                target: 'http://localhost:8000',
                changeOrigin: true,
                pathRewrite: {
                    '^/api': '',
                },
            },
            '/weather': {
                target: 'https://restapi.amap.com/v3/weather',
                changeOrigin: true,
                pathRewrite: {
                    '^/weather': '',
                },
            }
        },
    },
};