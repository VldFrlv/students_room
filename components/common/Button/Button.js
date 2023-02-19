import React from 'react';
import style from './Button.module.scss'

const Button = ({type, text}) => {
    return (
        <button type={type} className={style.button}>
            {text}
        </button>
    );
};

export default Button;