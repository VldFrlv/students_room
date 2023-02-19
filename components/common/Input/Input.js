import React from 'react';
import style from './Input.module.scss'

const Input = ({placeholder}) => {
    return (
        <>
            <input type="text" className={style.input} placeholder={placeholder}/>
        </>
    );
};

export default Input;