import React from 'react';
import ReactDOM from 'react-dom'
import {TextField, Button} from '@mui/material';

export default function Register() {
  return (
    <>
      <div className='container text-center'>
        <div className='mt-3'>
          <TextField id="email" type="email" label="Email" variant="outlined" />
        </div>
        <div className='mt-3'>
        <TextField id="first_name" type="text" label="First Name" variant="outlined" />
        </div>
        <div className='mt-3'>
        <TextField id="last_name" type="text" label="Last Name" variant="outlined" />
        </div>
        <div className='mt-3'>
        <TextField id="password" type="password" label="Password" variant="outlined" />
        </div>
        <div className='mt-3'>
        <Button variant='contained'>Save</Button>
        </div>
      </div>
    </>
  );
}
