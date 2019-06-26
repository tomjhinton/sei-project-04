import React from 'react'
import ReactDOM from 'react-dom'
import { HashRouter as Router, Switch, Route } from 'react-router-dom'
import 'bulma'
import './style.scss'
import Login from './components/auth/Login'
import Register from './components/auth/Register'
import CreatePost from './components/create/CreatePost'
import Recruit from './components/create/Recruit'
import Home from './components/common/Home'
import Navbar from './components/common/Navbar'
import EditWork from './components/create/EditWork'
import WorkShow from './components/show/WorkShow'
import Add from './components/show/Add'
import MyProfile from './components/show/MyProfile'
import Profile from './components/show/Profile'
import SecureRoute from './components/common/SecureRoute'

class App extends React.Component {
  constructor(){
    super()

    this.state = {
    }
  }

  componentDidMount() {

  }

  render() {
    return (

      <Router>
        <main>
          <Navbar />
          <Switch>
            <Route path="/profiles/:id" component={Profile}/>
            <SecureRoute path="/MyProfile/" component={MyProfile} />
            <Route path="/adverts/:id" component={Add} />
            <Route path="/works/:id/edit" component={EditWork}/>
            <Route path="/works/:id" component={WorkShow}/>
            <Route path="/new" component={CreatePost} />
            <Route path="/register" component={Register} />
            <Route path="/recruit" component={Recruit} />
            <Route path="/login" component={Login} />
            <Route path="/" component={Home} />


          </Switch>
        </main>
      </Router>


    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
