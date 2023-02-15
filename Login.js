import React, {useState} from 'react';
import style from './Login.module.scss';
import Input from "../../common/Input/Input";
import Button from "../../common/Button/Button";
import Logo from '../../../image/itecLogo.png'
import {NavLink} from "react-router-dom";
import {logDOM} from "@testing-library/react";
import HomePage from "../HomePage/HomePage";

const Login = () => {
    const [email, setEmail] = useState(null)
    const [password, setPassword] = useState()
    const [auth, setAuth] = useState(null)
    const [status_error, setStatusError] = useState(null)
    const send_data = () => {
        fetch('http://127.0.0.1:8000/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                'email': email,
                'password': password
            })
        }).then(resp => {
            if (resp.status === 401) {
                setStatusError("Error")
            }
            else {
                setStatusError(null)
            }
            return resp.json()}).then(a => {
            document.cookie = `access = ${a.access_token}`
            document.cookie = `refresh = ${a.refresh_token}`
            localStorage.setItem('access', a.access_token)
            localStorage.setItem('refresh', a.refresh_token)
            if (a.access_token && a.refresh_token){
                setAuth(true)
            }
            else {
                setAuth(null)
            }}
            // console.log(localStorage.getItem('access'), localStorage.getItem('refresh'))
        )}

        const set_value_email = (e) => {
            let email = e.target.value
            setEmail(email)
        }
        const set_value_password = (e) => {
            let password = e.target.value
            setPassword(password)
        }
        if (auth) {
            return <div>
                <HomePage/>
            </div>
        }
        else {
        return (
            <div className={style.formWrapper}>
                <div className={style.formLogo}>
                    <img src={Logo} alt={Logo}/>
                </div>
                <form method={'POST'} className={style.loginForm}>
                    <input type="text" placeholder={"Введи email"} onChange={set_value_email}/>
                    <input type="password" placeholder={"Введи пароль"} onChange={set_value_password}/>
                    <input type="button" value={'Войти'} onClick={send_data}/>
                    {/*</NavLink>*/}
                </form>
                <p style={{'color':'red'}}>{status_error}</p>

            </div>
        );}
    };
    export default Login;