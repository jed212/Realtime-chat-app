import React from 'react'
import withAuthentication from '../utils/withAuthentication'

function Sidebar() {
  return (
    <div className='sidebar'></div>
  )
}

export default withAuthentication(Sidebar)