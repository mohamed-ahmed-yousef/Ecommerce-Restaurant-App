import React from 'react'
import { useNavigate } from 'react-router-dom'
import {Button} from "@mui/material"
const PageNotFound = () => {
    const navigate = useNavigate()
    const sytle = {
        color:"#b52e2e",
        marginTop:"100px",
        fontFamily:"sans-serif",
        backgroundColor:"#504d4d",
        width:"fit-content",
        margin:"100px auto",
        padding:"30px",
        borderRadius:"30px",
        textAlign:"center"
    }
    const returnStyle = {
        cursor:"pointer",
        marginTop:"10px"
        

    }
  return (
    <div style = {sytle}>
      <h1 >page Not Found</h1>
      <Button onClick={() => navigate(-1)} style = {returnStyle} variant='contained'>Go Back</Button>
    </div>
  )
}

export default PageNotFound
