import React from 'react';
import ChatArea from './ChatArea';
import Sidebar from './Sidebar';

function Chat() {
    return (
      <>
        <div className='chat-container'>
          <Sidebar/>
          <ChatArea/>
        </div>
      </>
    );
}

export default Chat;