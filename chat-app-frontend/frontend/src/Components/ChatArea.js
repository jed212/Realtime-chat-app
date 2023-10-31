import React from 'react'
import Message from './Message'
import Messageinput from './Messageinput'
import withAuthentication from '../utils/withAuthentication'

function ChatArea() {
  return (
    <div className='chat-area'>
        <div className='chat-header'></div>
        <div className='messages'>
            <Message text="Hey, how's it goin" sent/>
            <Message text="I'm good, thanks" received/>
        </div>
        <Messageinput/>
    </div>
  )
}
export default withAuthentication(ChatArea)