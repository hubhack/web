import React from 'react';

//css
import '../css/login.css' //当一个资源打包
import UserService from '../service/user';
import { resolve } from 'path';



const userService = new UserService()

export default class Login extends React.Component {

    render(){
        return <_Login service={userService} />;
    }
}


class _Login extends React.Component {

    

    handleSubmit(event){//view层, 关系人机交互
        event.preventDefault();
        console.log(event.target);
        console.log(event.target.form);
        let fm = event.target.form;
        console.log(fm[0], fm[1]);
        console.log(fm[0].value, fm[1].value);

        //validate
        this.props.service.login(fm[0].value, fm[1].value);
        // let ret = this.props.service.handle();// 同步行为
        this.props.service.handle(this);// 同步行为
        

    }


    render() {
        return (
            <div className="login-page">
                <div className="form">
                    <form className="register-form">
                        {/* <input type="text" placeholder="姓名" /> */}
                        <input type="text" placeholder="邮箱" />  
                        <input type="password" placeholder="密码" />
                        <button onClick={this.handleSubmit.bind(this)}>登录</button>
                        <p className="message">还未注册<a href="/reg/">请登录</a></p>
                    </form>
                    
                </div>
            </div>
        )
    }
}