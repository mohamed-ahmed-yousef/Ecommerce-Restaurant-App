import './App.css'
import Register from './pages/Register/Register'
import {Route, Routes} from 'react-router-dom'
import Login from './pages/Login/Login'
import Home from './pages/Home/Home'
import PageNotFound from './pages/NotFoundPage/PageNotFound'
import Test from './Components/Test/AllSideBar'
function App() {

  return (
    <>
    
    <Routes>
      {/* remove when final test */}
        <Route path = "/test" element = {<Test />} />


        <Route path = '/' element = {<Home />} />

        <Route path = '/register'  element = {<Register/>} />
        <Route path = '/login' element = {<Login />} />
        <Route path = '*' element = {<PageNotFound />} />
    </Routes>
    </>
  )
}

export default App
