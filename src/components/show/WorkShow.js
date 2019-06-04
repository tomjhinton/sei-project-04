import React from 'react'
import { Link, withRouter } from 'react-router-dom'
import Auth from '../../lib/Auth'
import axios from 'axios'


class WorkShow extends React.Component {


  constructor() {
    super()

    this.state = {
      work: {


      }

    }

  }


  componentDidMount() {
    console.log(this.props.match)
    axios.get(`/api/works/${this.props.match.params.id}`)
      .then(res => this.setState({work: res.data}))

  }

  render(){
    console.log(this)

    return(

      <div className='container'>
        <div className='columns is-multiline'>
          <div className='column'>
            <h1 className='title'> {this.state.work.name}</h1>
          </div>
        </div>
        <div className='column'>
          <img src={this.state.work.picture}></img>
        </div>
        <div className='column'>
          {this.state.work.description && <p className="comment-body">
            {this.state.work.description.split('\n').map((text, i) =>
              <span key={i}>
                {text}<br />
              </span>
            )}
          </p>}

        </div>

        <div className='columns is-multiline'>
          {this.state.work.medium &&  <div className='column'>
            Medium: {this.state.work.medium.map(medium => {
              return  <h2 key={medium.id}  className='title-2'> {medium.name}</h2>
            }           )}
          </div>}
        </div>
        <div>
          {this.state.work.embed && (this.state.work.embed.includes('soundcloud') || this.state.work.embed.includes('youtube') || this.state.work.embed.includes('vimeo')) &&<div dangerouslySetInnerHTML={{__html: this.state.work.embed}}></div>}


          {this.state.work.code &&
          <pre>
            <code>
              {this.state.work.code}
            </code>

          </pre>}
          {this.state.work.iframe &&
          <iframe src={this.state.work.iframe}/>}
        </div>




      </div>


    )
  }
}
export default WorkShow
