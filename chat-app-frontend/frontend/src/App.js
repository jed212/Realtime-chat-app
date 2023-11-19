import React from 'react';
import './App.css';
import Login from './Components/Login';
import Register from './Components/Register';
import Navigate from './Components/Navigate';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import Chat from './Components/Chat';


function App() {
  return (
    <BrowserRouter>
      <Navigate/>
      <Routes>
        <Route path='/Login' element={<Login/>}></Route>
        <Route path='/Register' element={<Register/>}></Route>
        <Route path='/chat' element={<Chat/>}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
