import React from 'react';

//css
import '../css/login.css' //当一个资源打包
export default class Reg extends React.Component {
    


    render() {
        return (
            <div className="login-page">
                <div className="form">
                    <form className="login-form">
                        <input type="text" placeholder="用户名" />
                        <input type="password" placeholder="密码" />
                        <input type="password" placeholder="确认密码" />
                        <button >注册</button>
                        <p className="message">没有注册 <a href="#">创建用户</a></p>
                    </form>

                </div>
            </div>
        )
    }
}