import React from 'react'
import { Link, withRouter } from 'react-router-dom'
import Auth from '../../lib/Auth'
import axios from 'axios'


class Add extends React.Component {


  constructor() {
    super()

    this.state = {
      ad: {


      }

    }

  }


  componentDidMount() {
    console.log(this.props.match)
    axios.get(`/api/ads/${this.props.match.params.id}`)
      .then(res => this.setState({ad: res.data}))

    axios.get('/api/works')
      .then(works => this.setState({work: works.data}))

  }

  render(){
    console.log(this)

    return(

      <div className='container'>
        <div className='columns is-multiline'>
          <div className='column'>
            <h1 className='title'> {this.state.ad.name}</h1>
          </div>
          <div className='column'>
            <img src={this.state.ad.picture}></img>
          </div>
          <div className='column'>
            <h2 className='title-2'> {this.state.ad.description}</h2>
          </div>

          <div className='column'>
            <h2 className='title-2'> Type</h2>
          </div>
        </div>
        <div>




          <pre>
            <code>

            </code>

          </pre>

        </div>




      </div>


    )
  }
}
export default Add
