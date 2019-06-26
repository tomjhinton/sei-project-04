import React from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'


class Add extends React.Component {


  constructor() {
    super()

    this.state = {
      ad: {
        medium: []

      },
      work: {
        medium: []
      }

    }
    this.checkMedium = this.checkMedium.bind(this)
  }


  checkMedium(work) {
    return work.medium[0].name === this.state.ad.medium[0].name
  }


  componentDidMount() {
    console.log(this.props.match)
    axios.get(`/api/ads/${this.props.match.params.id}`)
      .then(res => this.setState({ad: res.data}))

    axios.get('/api/works')
      .then(works => this.setState({work: works.data.filter(this.checkMedium)}))

  }

  render(){
    console.log(this)

    return(

      <div className='container'>
        <div className='columns is-multiline'>
          <div className='column'>
            <h1 className='title'> {this.state.ad.name}</h1>
          </div>
        </div>
        <div className='columns is-multiline'>
          <div className='column'>
            {this.state.ad.createdBy &&<img src={this.state.ad.createdBy.photo}></img>}
          </div>
          <div className='column'>
            <div className='columns is-multiline'>
              {this.state.ad.medium &&  <div className='column'>
              Medium: {this.state.ad.medium.map(ad => {
                  return  <h2 key={ad.id}  className='title-2'> {ad.name}</h2>
                }           )}
              </div>}
              {this.state.ad.description && <p className="comment-body">
                {this.state.ad.description.split('\n').map((text, i) =>
                  <span key={i}>
                    {text}<br />
                  </span>
                )}
              </p>}

            </div>


          </div>
          <div>



          </div>
        </div>


        {this.state.work[0] && <div className='column'>
          <h1> Here are some works that might match your advert.</h1>
          {this.state.work.map(work => {
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

      </div>


    )
  }
}
export default Add
