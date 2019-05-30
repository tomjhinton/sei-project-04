import React from 'react'
import axios from 'axios'
import Link from 'react-router-dom'


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
  componentDidMount(){
    axios.get('/api/works')
      .then(res => this.setState({ works: res.data }))
    axios.get('/api/ads')
      .then(adsList => this.setState({ ads: adsList.data }))

  }

  render() {
    console.log(this.state)
    return (
      <div className='container'>
      HOME
      <div className='columns'>
        {this.state.works && <div className='column'>
          {this.state.works.map(work => {
            return <div  key={work.id} className="home-rec-event">{work.name}</div>
          })}
        </div>}

        {this.state.ads &&  <div className ='column is-half'>
          {this.state.ads.map(ad => {
            return <div  key={ad.id} className="home-rec-event">{ad.description}</div>
          })}
        </div>}
      </div>
      </div>



    )
  }
}
export default Login
