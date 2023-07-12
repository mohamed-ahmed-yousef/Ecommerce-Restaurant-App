import { useState, useRef } from 'react';
import { TextField, IconButton } from '@mui/material';
import { Search } from '@mui/icons-material';

function Try() {
  const [searchText, setSearchText] = useState('');
  const inputRef = useRef(null);

  const handleSearch = () => {
    inputRef.current.focus();
  };

  return (
    <div>
      <TextField
        label="Search"
        value={searchText}
        inputRef={inputRef}
      />
      <IconButton onClick={handleSearch}>
        <Search />
      </IconButton>
    </div>
  );
}
export default Try