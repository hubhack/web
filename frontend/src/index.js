import React from "react";
import ReactDom from 'react-dom'
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import Login from "./component/login";
import Reg from "./component/reg";
import { Menu, Icon, message, Layout } from 'antd';
import 'antd/lib/menu/style';
import 'antd/lib/icon/style';
import 'antd/lib/Layout/style';
function Index() {
    return <h2>Home</h2>;
}

function About() {
    return <h2>About</h2>;
}

function Users() {
    return <h2>Users</h2>;
}


function Always() {
    return <div>copyright 1999 </div>
}

const { Header, Footer, Sider, Content } = Layout;
function Root() {
    return (
        <Router>
            <div>

                <Layout>

                    <Header>
                        
                        <Menu selectedKeys={['home']} mode="horizontal" theme="dark" style={{ lineHeight: '64px' }}>
                            <Menu.Item key="home"><Link to="/"><Icon type="home" />首页</Link></Menu.Item>
                            <Menu.Item key="home"><Link to="/about/"><Icon type="setting" />关于</Link></Menu.Item>
                            <Menu.Item key="home"><Link to="reg"><Icon type="smile" />注册</Link></Menu.Item>
                            <Menu.Item key="home"><Link to="/login"><Icon type="login" />登录</Link></Menu.Item>
                        </Menu></Header>


                    <Content style={{ padding: '0 50px' }}>
                        <Route path="/" exact component={Index} />
                        <Route path="/login/" component={Login} />
                        <Route path="/reg/" component={Reg} />
                        <Route path="/about/" component={About} />
                        <Route path="/users/" component={Users} />
                    </Content>

                    <Footer><Route component={Always} /></Footer>
                </Layout>




                
            </div>
        </Router>
    );
}

// export default Root;
ReactDom.render(<Root />, document.getElementById('root'));
