import * as React from 'react';
import List from '@mui/material/List';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import Collapse from '@mui/material/Collapse';
import ExpandLess from '@mui/icons-material/ExpandLess';
import ExpandMore from '@mui/icons-material/ExpandMore';
import FiberManualRecordIcon from '@mui/icons-material/FiberManualRecord';
import {capitalize} from "./Functions"

export default function DropDown({main, nested, Icon, isOpen, special}) {
  const [open, setOpen] = React.useState(false);

  const handleClick = () => {
    setOpen(!open);
  };
  const commonStyleOne = {
      minHeight: 48,
      justifyContent: isOpen ? 'initial' : 'center',
      px: 2.5,
  }
  const commonStyleTwo = {
      minWidth: 0,
      mr: isOpen ? 3 : 'auto',
      justifyContent: 'center',
  }


  return (
    <List 
       component="nav"
        aria-labelledby="nested-list-subheader" >
      <ListItemButton onClick={handleClick}  sx={commonStyleOne} key = {`${main-nested}- ${ Math.random() * 1000}`} >
        <ListItemIcon sx={commonStyleTwo} >
          {Icon} 
        </ListItemIcon>
        <ListItemText primary={capitalize(main)} sx={{ opacity: isOpen ? 1 : 0 }}  primaryTypographyProps = {{fontSize:15, fontWeight:"bold"}}/>
        {isOpen ? (open  ?  <ExpandLess   /> : <ExpandMore />):null}
      </ListItemButton>
      <Collapse in={open} timeout="auto" unmountOnExit>

      {nested.map((ele, indx ) =>
        <List component="span" disablePadding sx={{ display: 'block' }} key = {`${ele }-${indx * nested.length * Math.random() * 1000}`}>
        <ListItemButton >
          {(!special || indx == 0 )&& <ListItemIcon sx  = {{pl:5, fontSize:"10px",opacity: isOpen ? 1 : 0  }} >
              <FiberManualRecordIcon fontSize='10px'/>
          </ListItemIcon>}
          <ListItemText primary={capitalize(ele)}   sx={{pl:1,opacity: isOpen ? 1 : 0 }}   primaryTypographyProps = {{fontSize:14, fontWeight:"bold"}}/>
        </ListItemButton>
      </List>
      )}
     
    
      </Collapse>
    </List>
  );
}