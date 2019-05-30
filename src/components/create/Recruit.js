import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'
import CreatableSelect from 'react-select/lib/Creatable'






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
        created: date.toLocaleDateString()


      },
      errors: {

      }

    }
    this.handleChange = this.handleChange.bind(this)
    this.handleSelectChange = this.handleSelectChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    //this.insertTab = this.insertTab.bind(this)

  }





  handleChange(e) {
    const data = { ...this.state.data, [e.target.name]: e.target.value }
    console.log(data)
    this.setState({ data })

  }



  handleSelectChange(e) {
    console.log(e)
    const data = { ...this.state.data, [this.name]: e }
    //console.log(data)
    this.setState({ data })
    console.log(this)
    console.log(e)

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
            <CreatableSelect
              className='Work'
              onChange={this.handleSelectChange}
              styles={selectStyles}
              isMulti
            />
          </form>


          <form>
            <div className="field">
              <label className="label">Languages</label>
            </div>
            <CreatableSelect
              onChange={this.handleSelectChange}
              styles={selectStyles}
              isMulti
            />
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
                      placeholder="A description of your event"
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
                  <label className="label">Name</label>
                  <div className="control">
                    <textarea
                      className="textarea"
                      name="name"
                      placeholder="Show The Code"
                      onChange={this.handleChange}
                      value={this.state.data.name || ''}
                      onKeyDown={this.insertTab}
                    />
                  </div>
                  {this.state.errors.name && <div className="help is-danger">{this.state.errors.name}</div>}
                </div>
              </div>



              <div className="column">
                <div className="field">
                  <label className="label">Embed an example</label>
                  <div className="control">
                    <textarea
                      className="textarea"
                      name="embed"
                      placeholder="Embed something from elsewhere"
                      onChange={this.handleChange}
                      value={ this.state.data.embed  || ''}
                      onKeyDown={this.insertTab}
                    />
                  </div>
                  {this.state.errors.embed && <div className="help is-danger">{this.state.errors.embed}</div>}
                </div>
              </div>
              <div className="column">
                <div className="field">
                  <label className="label">Embed Your site</label>
                  <div className="control">
                    <textarea
                      className="textarea"
                      name="site"
                      placeholder="Embed something from elsewhere"
                      onChange={this.handleChange}
                      value={ this.state.data.site  || ''}
                      onKeyDown={this.insertTab}
                    />
                  </div>
                  {this.state.errors.embed && <div className="help is-danger">{this.state.errors.embed}</div>}
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
