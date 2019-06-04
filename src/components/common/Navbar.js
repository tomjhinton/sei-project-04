import React from 'react'
import { Link, withRouter } from 'react-router-dom'
import Auth from '../../lib/Auth'


class Navbar extends React.Component{

  constructor(props){
    super(props)
    this.state ={ active: false}
    this.logout = this.logout.bind(this)
    this.toggleActive = this.toggleActive.bind(this)
  }
  logout() {
    Auth.removeToken()
    this.props.history.push('/')
  }

  toggleActive() {
    this.setState({ active: !this.state.active })
  }

  componentDidUpdate(prevProps) {
    if(prevProps.location.pathname !== this.props.location.pathname) {
      this.setState({ active: false })
    }
  }
  render(){
    return(
      <div className='container'>
        <nav className="navbar">
          <div className="navbar-brand">
            <Link to="/" className="logo is-size-4">Title</Link>
            <a role="button"
              className={`navbar-burger${this.state.active ? ' is-active' : ''}`} onClick={this.toggleActive}>
              <span aria-hidden="true"></span>
              <span aria-hidden="true"></span>
              <span aria-hidden="true"></span>
            </a>
          </div>

          <div className={`navbar-menu${this.state.active ? ' is-active' : ''}`}>
            <div className="navbar-start">

              {Auth.isAuthenticated() &&<Link to="/new" className={`navbar-item ${this.state.active ? ' is-active' : ''} `}>Add a piece</Link>}
            </div>

            <div className="navbar-start">

              {Auth.isAuthenticated() &&<Link to="/recruit" className={`navbar-item ${this.state.active ? ' is-active' : ''} `}>Recruit people for a project</Link>}
            </div>

            <div className="navbar-end">
              {!Auth.isAuthenticated() && <Link to="/register" className="navbar-item">Register</Link>}
              {!Auth.isAuthenticated() && <Link to="/login" className="navbar-item">Login</Link>}
              {Auth.isAuthenticated() && <a className="navbar-item" onClick={this.logout}><strong>Logout</strong></a>}
              {Auth.isAuthenticated() && <Link to="/myprofile" className={'navbar-item'}>Profile</Link>}

            </div>
          </div>
        </nav>
      </div>
    )
  }
}

export default withRouter(Navbar)
