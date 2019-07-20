// import Login from "../component/login";

//业务调用,
import axios from 'axios';
import store from 'store';
// import { observable } from 'mobx';
// import {expire}from 'store/plugins/expire'

// store.addPlugin(expire);

export default class UserService{


    login(email, password){
        console.log('----------------');
        console.log(email);
        console.log(password);
        console.log('-------------');
        axios.post('/api/users/login', {
            email,password
          })
          .then(response => {
            console.log(response);
            console.log(response.status)
            console.log(response.statusText)
            console.log(response.data)
            let token = response.data.token;
            store.set('token',token, new Date().getTime() + (8 * 3600 *1000));
            
            // 假过期, 服务端验证过期时间.//不要cookile
          })
          .catch(function (error) {
            console.log(error);
          });
    }
}