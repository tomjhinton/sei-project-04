import React from 'react'
import axios from 'axios'

class Register extends React.Component{
  constructor(){
    super()
    this.state ={
      data: {},
      errors: {}
    }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }


  handleChange(e) {
    const data = { ...this.state.data, [e.target.name]: e.target.value }
    console.log(data)
    this.setState({ data })

  }

  handleSubmit(e) {
    e.preventDefault()

    axios.post('/api/register', this.state.data)
      .then(() => this.props.history.push('/login')) // redirect the user to the login page...
      .catch(err => console.log(err))
  }




  render(){

    return(

      <section>
        <div className='container'>
          <div className="title section form-title">Register</div>
          <div className="user-form">
            <form onSubmit={this.handleSubmit}>
              <div className="field">
                <label className="label">Username</label>
                <div className="control">
                  <input
                    className="input"
                    name="username"
                    placeholder="eg: username"
                    onChange={this.handleChange}
                  />
                </div>
                {this.state.errors && <div className="help is-danger">{this.state.errors.username}</div>}
              </div>
              <div className="field">
                <label className="label">Email</label>
                <div className="control">
                  <input
                    className="input"
                    name="email"
                    placeholder="eg: jack@hotmail.com"
                    onChange={this.handleChange}
                  />
                </div>

              </div>
              <div className="field">
                <label className="label">Profile Image</label>
                <div className="control">
                  <input
                    className="input"
                    name="photo"
                    type="text"
                    placeholder="eg: https:myimages.com"
                    onChange={this.handleChange}
                  />
                </div>
                {this.state.errors.image && <div className="help is-danger">{this.state.errors.image}</div>}
              </div>
              
              <div className="field">
                <label className="label">lookingforwork</label>
                <div className="control">
                  <input
                    className="input"
                    name="lookingforwork"
                    type="text"
                    placeholder="eg: https:mygithubs.com"
                    onChange={this.handleChange}
                  />
                </div>
                {this.state.errors.github && <div className="help is-danger">{this.state.errors.github}</div>}
              </div>
              <div className="field">
                <label className="label">Password</label>
                <div className="control">
                  <input
                    className="input"
                    name="password"
                    type="password"
                    placeholder="eg: ••••••••"
                    onChange={this.handleChange}
                  />
                </div>
                {this.state.errors.password && <div className="help is-danger">{this.state.errors.password}</div>}
              </div>
              <div className="field">
                <label className="label">Password Confirmation</label>
                <div className="control">
                  <input
                    className="input"
                    name="password_confirmation"
                    type="password"
                    placeholder="eg: ••••••••"
                    onChange={this.handleChange}
                  />
                </div>
                {this.state.errors.passwordConfirmation && <div className="help is-danger">{this.state.errors.passwordConfirmation}</div>}
              </div>
              <button>Submit</button>
            </form>
          </div>
        </div>
      </section>
    )
  }
}
export default Register
