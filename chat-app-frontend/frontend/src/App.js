import React from 'react';
import './App.css';
import Login from './Components/Login';
import Register from './Components/Register';
import Navigate from './Components/Navigate';
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import ChatArea from './Components/ChatArea';
import Sidebar from './Components/Sidebar';

function App() {
  return (
    // <>
    //   <div className='chat-container'>
    //     <Sidebar/>
    //     <ChatArea/>
    //   </div>
    // </>
    <BrowserRouter>
      <Navigate/>
      <Routes>
        <Route path='/Login' element={<Login/>}></Route>
        <Route path='/Register' element={<Register/>}></Route>
        <Route path='/chat' element={<><Sidebar/><ChatArea/></>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
