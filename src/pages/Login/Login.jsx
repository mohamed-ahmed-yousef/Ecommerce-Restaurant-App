import {useForm} from 'react-hook-form'
import {TextField, Button, IconButton} from '@mui/material'
import ErrorIcon from '@mui/icons-material/Error';
import "../Register/Register.css"
import '../Register/mediaQuery.css'
import registerPhoto from '../../assets/register2.jpg';
import EmailIcon from '@mui/icons-material/Email';
import LockIcon from '@mui/icons-material/Lock';
import { useRef } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faEyeSlash, faEye } from '@fortawesome/free-solid-svg-icons'
import { useState } from 'react';
import {Link, useNavigate} from 'react-router-dom'

const style = {
    padding: "10px",
    backgroundColor:"#363b41",
    fontSize:"50px",
    borderRadius:"3px"
}

const Register= () => {
    const navigate = useNavigate() 
    const see = <FontAwesomeIcon icon={faEye} />
    const notsee = <FontAwesomeIcon icon= {faEyeSlash} />
    const [show, setShow]  = useState(false)
    const form = useForm()
    const {register, control, handleSubmit, formState} = form
    const {errors} = formState
    const onSubmit = (data) => {
        navigate("/")
    }
    const inputEmail = useRef(null)
    const inputPassWord = useRef(null)
    const handleClickEmail = () => {
        inputEmail.current.focus()
    }
    const handleClickPassWord = () => {
        inputPassWord.current.focus()
    }

  

    return (
    <>
        <div className = "parent">
            {/* food */}
            <div className="container">
         
            <img src={registerPhoto} alt="register photo" />

            {/* form */}    
            <form action="" onSubmit={handleSubmit(onSubmit)} noValidate >
            <h3 style={{color:"#4caf50", fontWeight:"bold", textAlign:'center'}}>Log in</h3>
                
          

            {/* email */}
            <div className="email">


                {/* <label htmlFor="email">Email</label> */}
                    <IconButton onClick={handleClickEmail}>
                        <EmailIcon  style = {style}/>

                    </IconButton>
                <div>
                <TextField inputRef={inputEmail}  id="email" label="email" variant="outlined" type = 'email' {...register('email', {
                        required :
                        {
                            value:true,
                            message: "Email is Required"
                        },
                        pattern : {
                            value: /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/,
                            message:"not valid email formate"
                        }

                })} />
            <p className = 'error'>{errors.email?.message && (
                    <>
                    <ErrorIcon color="warning"/> {errors.email?.message}
                    </>

            )}</p>
                
                </div>

            </div>

           {/* password */}
           <div className="password">
                {/* <label htmlFor="password">password</label> */}
                    <IconButton  onClick={handleClickPassWord} >
                        <LockIcon  style = {style} />
                    </IconButton>
                <div>
                    <div className="see-not">
                        <TextField inputRef = {inputPassWord} id="password" label="password" variant="outlined" type={show?"text":'password'} {...register('password', {
                                required :
                                {
                                    value:true,
                                    message: "Password Is Required"
                                },  
                                pattern:
                                {
                                    value: /^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=\S+$).{8,}$/,
                                    message: "Please include at least one lowercase letter, one uppercase letter, one digit, and be at least 8 characters long."
                                }

                        })} />
                        <div onClick={() =>setShow(!show)}  className="mainsee">
                            {show? see: notsee}
                        </div>
                    </div>

                    <p className = 'error'>{errors.password?.message && (
                        <>
                            <ErrorIcon color="warning"/> {errors.password?.message}
                        </>
                    )
                    
                    }</p>
                    </div>
           </div >
            <Button variant='contained' type='submit' sx = {{
            color:"#eee ",
            backgroundColor:"black",
            marginTop:"10px",
            marginBottom:"10px;"
            

          }}>submit</Button>
            {/* submit */}
            
        <Link to= "/register" className = "loginLink">sign Up</Link>
           </form>
           
        </div>
               
        </div>


    </>
    )

}
export default Register
