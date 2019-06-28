# Interstitial
project-04


<img width="1439" alt="Screenshot 2019-06-28 at 07 08 49" src="https://user-images.githubusercontent.com/44926628/60321070-9c0e9180-9973-11e9-90a8-eded2bafc036.png">


### Timeframe
7 days

## Technologies used

* React
* SQL
* Python
* Flask
* Pony ORM
* JavaScript (ES6)
* HTML5
* CSS
* Bulma
* Ajax
* React Select
* Webpack
* Git/GitHub


### Installation
Download the folders and files into a local directory.

From within the directory in your CLI:

```
yarn install
```

or

```
npm install
```

to install the dependencies.


### Introduction

The brief was to create a full-stack web app with a RESTful API. The API was to be made with a Flask app and a PostgreSQL database and it was to be consumed by a React front end.

I made Interstitial a site designed for the sharing of creative projects made with code.


## Process
_Describe the process of building the game. How did you get started? How did you manage your time? How would you do things next time?_

I wanted to create a site where users could login and post either work they had created with code or to post and advert to say they were looking for someone to do some work. This meant creating forms for registration and creating both types of post. Integrating a form with a SQL backend was something that I'd not done before and getting the data to be passed back and forth in the right format took a bit of work.

With each piece I wanted the option to display a picture of the work, a description of it, examples of the code used to create it and to embed it in a way that could effectively showcase it.

Retaining the formatting in the descriptions after it has gone into and been pulled out of the database was an issue that I'd had to deal with before.

I had to split the string at any  ```\n``` and insert a ```<br/>``` to retain line breaks.

```
<div className='column'>
  {this.state.work.description && <p className="comment-body">
    {this.state.work.description.split('\n').map((text, i) =>
      <span key={i}>
        {text}<br />
      </span>
    )}
  </p>}

</div>
```


### Challenges and wins
_Describe the biggest challenges.
  How did you overcome them?
  Did you decide to pivot because of time constraints?
  What did you learn from these problems?_

  The biggest challenge was working with a SQL database and using Python on the backend for the first time. It proved quite a shift from using Node.js because of the need to consider entity relationships.





## Future features
I would like to add in interaction between users. To allow them to message each other and to save work that they liked.
