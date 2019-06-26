import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'







const selectStyles = {
  control: (styles, state) => ({
    ...styles,
    backgroundColor: 'white',
    color: 'black',
    borderRadius: '0',
    border: state.isFocused ? 0:0,
    boxShadow: state.isFocused ? 0:0,
    borderBottom: '0.5px solid rgb(223, 231, 236)',
    '&:hover': {
      borderBottom: '0.5px solid rgb(223, 231, 236)'
    }
  })
}




const date = new Date()
class Recruit extends React.Component {





  constructor() {
    super()

    this.state = {
      data: {
        created: date.toLocaleDateString(),
        medium_ids: []

      },
      errors: {

      }

    }
    this.handleChange = this.handleChange.bind(this)
    this.handleSelectChange = this.handleSelectChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.handleMediumSelect = this.handleMediumSelect.bind(this)

  }





  handleChange(e) {
    const data = { ...this.state.data, [e.target.name]: e.target.value }
    console.log(data)
    this.setState({ data })

  }


  componentDidMount() {
    console.log(this.props.match)
    axios.get('/api/mediums')
      .then(res => this.setState({mediums: res.data}))

  }


  handleSelectChange(e) {
    console.log(e)
    const data = { ...this.state.data, [this.name]: e }
    //console.log(data)
    this.setState({ data })
    console.log(this)
    console.log(e)

  }

  handleMediumSelect(e){
    this.setState({
      data: {
        ...this.state.data,
        medium_ids: [ ...this.state.data.medium_ids, parseInt(e.target.value) ]
      }
    })
  }


  handleSubmit(e) {
    e.preventDefault()
    const token = Auth.getToken()
    axios.post('/api/ads', this.state.data, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
      .then(res  => console.log(res))
      .catch(err => this.setState({ errors: err.response.data.errors }))

  }


  render() {
    console.log(this.state.data)
    return (

      <div className ='container'>
        <section className="section">

          <div className="title">Recruit people for a project</div>

          <form>
            <div className="field">
              <label className="label">Type of Work</label>
            </div>
            <div className="select is-multiple"
              onChange={this.handleMediumSelect}>
              {this.state.mediums &&<select>
                {this.state.mediums.map(medium => {
                  return <option key={medium.id} value={medium.id}> {medium.name}</option>
                })}
              </select>}
            </div>
          </form>

          <form className="event-form" onSubmit={this.handleSubmit}>

            <div className="columns">



              <div className="column">
                <div className="field">
                  <label className="label">Description</label>
                  <div className="control">
                    <textarea
                      className="textarea"
                      name="description"
                      placeholder="What are you looking for someone to make?"
                      onChange={this.handleChange}
                      value={this.state.data.description || ''}
                      onKeyDown={this.insertTab}
                    />
                  </div>
                  {this.state.errors.description && <div className="help is-danger">{this.state.errors.description}</div>}
                </div>
              </div>




              <div className="column">
                <div className="field">
                  <label className="label">Title</label>
                  <div className="control">
                    <textarea
                      className="textarea"
                      name="name"
                      placeholder="Name of the project."
                      onChange={this.handleChange}
                      value={this.state.data.name || ''}
                      onKeyDown={this.insertTab}
                    />
                  </div>
                  {this.state.errors.name && <div className="help is-danger">{this.state.errors.name}</div>}
                </div>
              </div>





            </div>
            <button>Submit</button>

          </form>


        </section>
      </div>
    )
  }
}

export default Recruit
