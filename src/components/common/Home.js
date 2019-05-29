import React from 'react'
import axios from 'axios'

import Auth from '../../lib/Auth'
import Flash from '../../lib/Flash'

class Login extends React.Component{
  constructor(){
    super()
    this.state = {
      data: {},
      error: ''
    }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleChange(e) {


}

  handleSubmit(e) {

  }
  render() {
    console.log(this.state)
    return (
      <div className='container'>
      HOME
      </div>


    )
  }
}
export default Login
