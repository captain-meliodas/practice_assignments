import React from 'react';
import ReactDom from 'react-dom'

import Books from './components/Books'
import './index.css'

function Maincomponent() {
  return (
    <React.Fragment>
      <Books/>
    </React.Fragment>
  )
}

ReactDom.render(<Maincomponent />,document.getElementById('root'))