import React from 'react'

import classes from './ErrorModel.module.css';
// just a container showing error
const ErrorModel = () => {
  return (
    <div className={classes["error-box"]}>
      <h2>Not able to find for given input</h2>
      <p>Please write specific product name</p>
    </div>
  )
}

export default ErrorModel