import React, { useState, useEffect } from 'react'
import Divider from '@mui/material/Divider';


const DividerMessage = ({message, isOpen}) => {
    const [currMessage, setCurrMessage] = useState(message)
    const styleOpen = { 
        fontSize:"14px",
        color:"#6f6c6c",
        textAlign:"center",
        
    };
    const styleClose = {
        fontSize:"40px",
        textAlign:"center",

    }
    useEffect(() => {
        if (!isOpen) {
          setCurrMessage('...');
        } else {
          setCurrMessage(message);
        }
      }, [isOpen, message]);
      

  return (
    <div>
       
      <Divider style  ={{display:"none"}}/>

        <div style={isOpen?styleOpen:styleClose} >{currMessage}</div>

      <Divider style  ={{display:"none"}}/>
    </div>
  )
}

export default DividerMessage
