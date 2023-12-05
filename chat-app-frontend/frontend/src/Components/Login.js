import { useState } from "react";
import React from 'react'
import {TextField, Button} from '@mui/material';

export default function Login() {
    const BASE_URL = "http://127.0.0.1:8000/";
    const [formData, setFormData] = useState({
        "email": "",
        "password": "",
    })
    const handleFormSubmit = () =>{
        fetch(`${BASE_URL}login/`,{
        method: 'POST',
        headers: {
            'Content-Type':'application/json'
        },
        body: JSON.stringify(formData)

        })
        .then(response => response.json())
        .then(data => {
        console.log(data);
        const token = data.token;
        document.cookie = `token=${token}; path=/`
        })
        .catch(error => {
        console.log(error);
        })
    }
  return (
    <>
      <div className='container text-center'>
        <div className='mt-3'>
          <TextField id="email" type="email" label="Email" onChange={e => setFormData({...formData, email: e.target.value})} variant="outlined" />
        </div>
        <div className='mt-3'>
        <TextField id="password" type="password" label="Password"  onChange={e => setFormData({...formData, password: e.target.value})} variant="outlined" />
        </div>
        <div className='mt-3'>
        <Button variant='contained' onClick={handleFormSubmit}>Login</Button>
        </div>
      </div>
    </>
  )
}
