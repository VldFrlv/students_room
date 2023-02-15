import React from 'react';
import style from './HomePage.module.scss'
import AsideAboutCourse from "../../Aside/AsideAboutCourse/AsideAboutCourse";
import Header from "../../Header/Header";

const HomePage = () => {
    let get_email_from_access =()=>{
        console.log(localStorage.getItem('access'))

        fetch('http://127.0.0.1:8000/auth/authorization',{
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                // 'Set-Cookie': localStorage.getItem('access')
                'Cookie': {'dsds': 'dsd'},
                'Hui': 'jdj'
            },
            credentials: "include"

    }).then()}
    return (
        <div className={style.homePage}>
            <Header />
            <div className={style.homePageWrapper}>
                <AsideAboutCourse />
                <h1 style={{'color': 'red'}} onClick={get_email_from_access}>Get by actual access</h1>
                <h1 style={{'color': 'black'}}>Refresh</h1>
            </div>


        </div>
    );
};

export default HomePage;