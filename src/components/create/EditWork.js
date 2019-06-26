import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'
import DOMPurify from 'dompurify'






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





class EditWork extends React.Component {

  constructor() {
    super()

    this.state = {
      data: {
        medium_ids: []



      },
      errors: {

      }

    }
    this.handleChange = this.handleChange.bind(this)
    this.handleSelectChange = this.handleSelectChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.dangerous = this.dangerous.bind(this)
    this.handleMediumSelect = this.handleMediumSelect.bind(this)
    //this.insertTab = this.insertTab.bind(this)

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

    axios.get(`/api/works/${this.props.match.params.id}`)
      .then(res => this.setState({data: res.data}))

  }

  handleSelectChange(e) {
    console.log(e)
    console.log(this)
    const data = { ...this.state.data, [this.Classname]: e }
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
    axios.put(`/api/works/${this.state.data.id}`, this.state.data, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
      .then(res  => this.props.history.push(`/works/${res.data._id}`))
      .catch(err => this.setState({ errors: err.response.data.errors }))

  }

  dangerous(){

    return {__html: this.state.errors.embed}
  }

  render() {
    console.log(this.state)
    console.log(DOMPurify.sanitize(this.state.data.embed))
    return (

      <div className ='container'>
        <section className="section">

          <div className="title">Share Your Work</div>




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
            {this.state.data &&
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
                      placeholder="A description of your event"
                      onChange={this.handleChange}
                      value={this.state.data.name || ''}
                      onKeyDown={this.insertTab}
                    />
                  </div>
                  {this.state.errors.description && <div className="help is-danger">{this.state.errors.description}</div>}
                </div>
              </div>




              <div className="column">
                <div className="field">
                  <label className="label">Share Your Code</label>
                  <div className="control">
                    <textarea
                      className="textarea"
                      name="code"
                      placeholder="Show The Code"
                      onChange={this.handleChange}
                      value={this.state.data.code || ''}
                      onKeyDown={this.insertTab}
                    />
                  </div>
                  {this.state.errors.code && <div className="help is-danger">{this.state.errors.code}</div>}
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


              <div className="column">
                <div className="field">
                  <label className="label">Upload a photo or video of your work</label>
                  <div className="control">
                    <input name="file" type="file"
                      className="file-upload" data-cloudinary-field="image_id"
                      data-form-data="{ 'transformation': {'crop':'limit','tags':'samples','width':3000,'height':2000}}"/>
                  </div>
                  {this.state.errors.file && <div className="help is-danger">{this.state.errors.file}</div>}
                </div>
              </div>

            </div>}
            <button>Submit</button>
          </form>


        </section>
      </div>
    )
  }
}

export default EditWork
