import React, { useEffect, useState } from 'react'
// 
import UserItem from './UserItem'
import List from '@mui/material/List';
import LinearProgress from '@mui/material/LinearProgress';
import Box from '@mui/material/Box';
import axios from 'axios';

export default function Sidebar() {
  const BASE_URL = `http://127.0.0.1:8000/`
  const [userList, setuserList] = useState([])
  const [userLoader, setuserloader] = useState(true)
  const getAuthTokenFromCookie = () =>{
    const cookies = document.cookie.split(';')
    for (const cookie in cookies) {
      const [name, value] = cookie.trim().split("=");
      if(name === "token"){
        return value
      }
    }
    return null
}

useEffect(() => {
  const authToken = getAuthTokenFromCookie()
  if (authToken){
    axios.get(`${BASE_URL}api/users/`, {
      headers:{
        Authorization:`Bearer ${authToken}`
      }
    }).then(response => {
      console.log("API response:", response.data);
      setuserList(response.data.data)
      setuserloader(false)
      console.log(userList);
    }).catch(error => {
      console.log("Error making API request:", error)
    })
  }
}, [BASE_URL, userList]);
  return (
    <div className='sidebar'>
      {userLoader ? (<Box sx={{width: '100%'}}>
        <LinearProgress/>
      </Box>):
      (<List sx={{width: '100%', maxWidth: 360, bgcolor: 'background.paper'}}>
        {userList.map((user, index) => (
          <UserItem key={index} email={user.email} name={`${user.first_name} ${user.last_name}`} id={user.id}></UserItem>
        ) )}
      </List>)
      }      
    </div>
  )
}
