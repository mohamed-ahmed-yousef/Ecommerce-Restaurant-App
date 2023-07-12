import React from 'react'
import LogoImage from "../../assets/LogoImage.png"

const Logo = ({open}) => {
    const LogoStyle = {
        width:"170px",
        marginLeft:"-209px",
        cursor:"pointer",


    }
const handleClick = () => {
    console.log("clicked");
}
  return (
    <div>
    {open && <img src={LogoImage} alt="Logo image" style={LogoStyle} onClick={handleClick}/>}
    </div>
  )
}

export default Logo
