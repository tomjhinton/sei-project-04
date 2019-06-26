import React from 'react'
import { Route, Redirect } from 'react-router-dom'
import Auth from '../../lib/Auth'


const SecureRoute = ({ component: Component, ...otherProps }) => {

  // if we have a token, return a normal route with Component and the otherProps set
  if(Auth.isAuthenticated()) return <Route {...otherProps} component={Component} />

  // otherwise redirect the user to `/login`

  return <Redirect to="/login" />
}

export default SecureRoute
