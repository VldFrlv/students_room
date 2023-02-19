import React from 'react';
import style from './Header.module.scss'
import {NavLink} from "react-router-dom";
import headerArrow from '../../image/icons/headerArrow.svg'
import headerAvatar from '../../image/headerProfileAvatar.png'

const Header = () => {
    return (
        <div className={style.header}>
            <div className={style.headerWrapper}>
                <div className={style.headerAction}>
                    <NavLink to={'/'}>
                        <div className={style.headerActionBackArrow}>
                            <img src={headerArrow} alt={headerArrow}/>
                        </div>
                    </NavLink>
                </div>
                <NavLink to={'/profile'}>
                    <div className={style.headerProfileIcon}>
                        <img src={headerAvatar} alt={headerAvatar}/>
                    </div>
                </NavLink>
            </div>
        </div>
    );
};

export default Header;