import React, {useEffect, useRef, useState} from 'react';
import style from './AsideAboutCourse.module.scss'
import asidePhoto from '../../../image/asidePhoto.jpg'
import contentCourseIcon from '../../../image/icons/contentCourseIcon.svg'
import contentCourseIconActive from '../../../image/iconsActive/contentCourseIconActive.svg'
import personal from '../../../image/icons/Personnel.svg'
import {NavLink} from "react-router-dom";
import login from "../../pages/Login/Login";

const AsideAboutCourse = ({users}) => {

    const [imageState, setImageState] = useState(false)
    let get_email_from_access = () => {
        fetch('http://127.0.0.1:8000/auth/get_all_users', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                // 'Set-Cookie': localStorage.getItem('access')
                // 'Cookie': document.cookie,
                'Authorization': localStorage.getItem('access')
            },
            credentials: "include"

        })
            .then((resp) => {
                if (resp.status !== 401) {
                    return resp.json()
                } else {
                    fetch('http://127.0.0.1:8000/auth/refresh/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify( {"refresh": localStorage.getItem('refresh')})
                    }).then(resp => {
                        if (resp.status === 200){
                        return resp.json()}
                    else {
                        window.location.assign('http://localhost:3000')
                        }})
                        .then((tokens) => {
                        localStorage.setItem('access', tokens.access_token)
                        localStorage.setItem('refresh', tokens.refresh_token)
                        console.log(localStorage.getItem('access'))
                    })
                }
            })
            .then(data => users(data))
            .catch()
        {
            users([{'email': 'hello'}])
            console.log('error')
        }
    }

    return (
        <div className={style.asideWrapper}>
            <div className={style.asideImageWrapper}>
                <img src={asidePhoto} alt=""/>
            </div>
            <div className={style.asideContent}>
                <div className={style.asideTitle}>
                    Крутой Чэл
                </div>
                <div className={style.asideProgressBar}>
                    <div className={style.progress}></div>
                </div>
                <div className={style.progressTitle}>
                    <span>45%</span> завершено
                </div>
                <div className={style.progressSubTitle}>
                    Доступно до ...
                </div>
            </div>
            <div className={style.asideContentLine}></div>
            <div className={style.asideService}>
                <ul className={style.asideServiceList}>
                    <li className={style.asideListItem}>
                        <NavLink to={'/'} onClick={get_email_from_access}>
                            <div className={style.asideListItemWrapper} onMouseOver={(e) => {
                                setImageState(true)
                                console.log(imageState)
                            }}>
                                <div className={style.listItemImage}>
                                    <img src={contentCourseIcon} alt={contentCourseIcon}/>
                                </div>
                                <div className={style.listItemTitle}>
                                    Содержание курса
                                </div>
                            </div>
                        </NavLink>
                    </li>
                    <li className={style.asideListItem}>
                        <NavLink to={'/'}>
                            <div className={style.asideListItemWrapper}>
                                <div className={style.listItemImage}>
                                    <img src={personal} alt={personal}/>
                                </div>
                                <div className={style.listItemTitle}>
                                    Твой YODA
                                </div>
                            </div>
                        </NavLink>
                    </li>
                </ul>
            </div>
        </div>
    );
};

export default AsideAboutCourse;