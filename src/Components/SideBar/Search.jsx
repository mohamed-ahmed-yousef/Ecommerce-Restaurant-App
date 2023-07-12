import { Container, TextField } from "@mui/material";
import SearchIcon from '@mui/icons-material/Search';
import {useRef} from 'react'

export default function SearchBar({open, Filtering}) {
    const input = useRef(null)
   
    const handleClick = () => {
        input.current.focus()
    }
  return (
    <>
    {open &&
      <Container   >

        <TextField  
        type="search" id="search" label="Search" 
        sx={{ width: 260, marginTop:"15px", marginBottom:"10px"}}
        inputRef = {input}
        InputProps={{
            startAdornment: (
                <SearchIcon onClick = {handleClick}
                sx={{ mr: 1, cursor: 'pointer' }} />
            )
        }} 
        onChange = {(e) => Filtering(e.target.value)}
        
        />
      </Container>}
    </>
  );
}