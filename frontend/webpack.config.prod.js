/**
 * Created by magedu on 2017/4/20.
 */

const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    devtool: 'source-map',
    entry: {
        'app': [
            './src/index'
        ]
    },
    output: {
        path: path.join(__dirname, 'dist'),
        filename: '[name]-[hash:8].js',
        publicPath: '/assets/'
    },
    resolve: {
        extensions: ['.js']
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/, // 不编译第三方包
                use: [
                    //{ loader: 'react-hot-loader/webpack' }, //4.0不需要这一项了
                    { loader: 'babel-loader' }
                ]
            },
            {
                test: /\.css$/,
                use: [
                    { loader: "style-loader" },
                    { loader: "css-loader" }
                ]
            },
            {
                test: /\.less$/,
                use: [
                    { loader: "style-loader" },
                    { loader: "css-loader" },
                    { loader: "less-loader" }
                ]
            }
        ]
    },
    plugins: [
        new webpack.optimize.OccurrenceOrderPlugin(true),
        new webpack.DefinePlugin({ 'process.env': { NODE_ENV: JSON.stringify('production') } }),
        new webpack.optimize.UglifyJsPlugin({
            compress: {
                warnings: false
            },
            sourceMap: true
        }),
        new HtmlWebpackPlugin({
            filename: 'index.html', //html的输出路径和文件名
            template: 'src/index.html',//不用自动生成h5模板页，使用指定的模板
            inject: true 
            //true || 'head' || 'body' || false，指定模板位置，把打包好的js的引用加入到模板的位置
            //true和'body'表示<script>加body元素的底部
            //'head'表示<script>加载head中
        })
    ]
};