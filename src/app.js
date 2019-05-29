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
import Work from './components/show/Work'
import Add from './components/show/Add'



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
            <Route path="/add/id:" component={Add} />
            <Route path="/work" component={Work} />
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
