import React from 'react'
import axios from 'axios'
import {Link} from 'react-router-dom'


import Auth from '../../lib/Auth'
import Flash from '../../lib/Flash'

class Login extends React.Component{
  constructor(){
    super()
    this.state = {
      data: {},
      error: ''
    }
    
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
        <div className='columns'>
          {this.state.works && <div className='column'>
            {this.state.works.map(work => {
              return <div key={work.id} className="card">
                <Link to={`/works/${work.id}`}>
                  <div className= 'card-header-title'>
                    {work.name}
                  </div>
                  <div className='card-image'><img src={work.picture}></img></div>
                </Link>
                <Link to={`profiles/${work.createdBy.id}`}>
                  {work.createdBy.username}
                </Link>
              </div>
            })}
          </div>}

          {this.state.ads &&  <div className ='column is-half'>
            {this.state.ads.map(ad => {
              return <div  key={ad.id} className="card">
                <Link to={`/adverts/${ad.id}`}>
                  <div className='card-header-title'>{ad.name}</div>
                  <div className='card-image'><img src={ad.createdBy.photo}></img></div>
                  {ad.description}
                </Link>
              </div>
            })}
          </div>}
        </div>
      </div>



    )
  }
}
export default Login
