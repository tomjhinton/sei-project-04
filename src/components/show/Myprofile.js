import React from 'react'
import axios from 'axios'
import { Link, withRouter } from 'react-router-dom'
import Auth from '../../lib/Auth'



const user = Auth.getPayload()
console.log(Auth.getPayload())
class MyProfile extends React.Component {


  constructor() {
    super()

    this.state = {



    }

  }


  componentDidMount() {
    console.log(this.props.match)
    axios.get(`/api/users/${user.sub}`)
      .then(res => this.setState({user: res.data}))

  }



  render(){
    console.log(this.state)
    return(



      <div className='container'>
        {this.state.user &&
          <div className='columns'>
            <div className='column'>
              <h1 className='title'>{this.state.user.username} </h1>
            </div>
            {this.state.user.works.map(work => {
              return <div key={work.id} className="card">
                <Link to={`/works/${work.id}`}>
                  <div className= 'card-header-title'>
                    {work.name}
                  </div>
                  <div className='card-image'><img src={work.picture}></img></div>
                </Link>
              </div>
            })}

          </div>}
        {this.state.user && <p className="comment-body">
          {this.state.user.bio.split('\n').map((text, i) =>
            <span key={i}>
              {text}<br />
            </span>
          )}
        </p>}





      </div>


    )
  }
}
export default withRouter(MyProfile)
