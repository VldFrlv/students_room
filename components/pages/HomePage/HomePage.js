import React, {useState} from 'react';
import style from './HomePage.module.scss'
import AsideAboutCourse from "../../Aside/AsideAboutCourse/AsideAboutCourse";
import Header from "../../Header/Header";
import Main from "../../Main/Main";
import login from "../Login/Login";

const HomePage = () => {
    const [users, setUsers] = useState([{email: 'hello'}])
    // const [mainState, setMainState] = useState(false)
    // if (users){
    //     setMainState(true)
    // }
    console.log(users)
    let get_email_from_access =()=>{
        console.log(localStorage.getItem('access'))

        fetch('http://127.0.0.1:8000/auth/get_all_users',{
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                // 'Set-Cookie': localStorage.getItem('access')
                // 'Cookie': document.cookie,
                'Authorization': localStorage.getItem('access')
            },
            credentials: "include"

    }).then(resp=>resp.json()).then(users => console.log(users))}
    let get_new_refresh_token =()=>{
        fetch('http://127.0.0.1:8000/auth/authorization', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
        },
            body: JSON.stringify('refresh', localStorage.getItem('refresh'))
        }).then()}
    return (
        <div className={style.homePage}>
            <Header />
            <div className={style.homePageWrapper}>
                <AsideAboutCourse users={setUsers} />
                {
                    users ?
                        <Main>
                            {users.map((item, index)=><p key={index} style={{'color': 'black'}}>{item.email}</p>)}
                        </Main>
                        :
                        <Main>
                            <p style={{'color': 'black'}}>False</p>
                        </Main>
                }
            </div>
        </div>
    );
};

export default HomePage;