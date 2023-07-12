import React from 'react'
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import {capitalize} from "./Functions"

const MainComponent = ({content, Icon, open}) => {
    const commonStyleOne = {
        minHeight: 48,
        justifyContent: open ? 'initial' : 'center',
        px: 2.5,
    }
    const commonStyleTwo = {
        minWidth: 0,
        mr: open ? 3 : 'auto',
        justifyContent: 'center',
    }

    return (
        <List>
            {content.map((text,index) =>
                <ListItem key={text} disablePadding sx={{ display: 'block' }}>
                    <ListItemButton sx={commonStyleOne} >
                    <ListItemIcon sx={commonStyleTwo} >
                        {Icon[index]}
                    </ListItemIcon>

                    <ListItemText primary={capitalize(text)} sx={{ opacity: open ? 1 : 0 }} primaryTypographyProps = {{fontSize:15, fontWeight:"bold"}} />
                    </ListItemButton>
            </ListItem>)}
        </List>
    )
}

export default MainComponent
