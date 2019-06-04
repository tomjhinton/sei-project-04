import React from 'react'
import { Link, withRouter } from 'react-router-dom'
import Auth from '../../lib/Auth'
import axios from 'axios'

class Work extends React.Component {






  render(){
    return(

      <div className='container'>
        <div className='columns'>
          <div className='column'>
            <h1 className='title'> Title</h1>
          </div>
          <div className='column'>
            <h2 className='title-2'> CreatedBy</h2>
          </div>
          <div className='column'>
            <h2 className='title-2'> Languages</h2>
          </div>

          <div className='column'>
            <h2 className='title-2'> Type</h2>
          </div>
        </div>
        <div>

          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vulputate dapibus eros, et ultricies augue suscipit at. Aliquam a placerat diam, in faucibus eros. Aliquam eu neque tellus. Quisque blandit ultricies consequat. Ut sodales, odio in vulputate tincidunt, eros elit ullamcorper velit, in blandit odio ligula sed ex. Proin molestie eu sapien in tincidunt. Quisque eget urna vehicula, gravida arcu non, consequat sem.
            <br />
      Quisque nisl ante, pharetra nec augue sed, tempus tincidunt velit. Nullam vel nibh tempor nulla tristique blandit. Duis varius dictum interdum. Vivamus congue mattis ipsum, sit amet convallis risus porttitor ac. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla id orci varius sapien rutrum molestie et a ex. Nulla convallis felis risus, non eleifend dui venenatis eget. Vivamus ac ligula vel odio viverra dapibus et sodales odio. Vivamus vitae imperdiet felis, ut ullamcorper nibh.
          </p>

          <iframe src='https://tomjhinton.dev/comic.html'> </iframe>

          <pre>
            <code>

            </code>

          </pre>

        </div>


      </div>


    )
  }
}
export default withRouter(Work)
