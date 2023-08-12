import React, {useState} from 'react'

import classes from "./ProductDetail.module.css";

const ProductDetail = (props) => {
  console.log(typeof(props.api));
  console.log(props.api);
  return (
    <>
      {props.api.ProductSRC ? <><h1 className={classes.heading}>{props.api.SiteName}</h1>
      <div className={classes["product-box"]}>
          <img src={props.api.ProductSRC} alt="product-image" className={classes["product-img"]}/>
          <div className={classes.detail}>
            <p>{props.api.ProductName}</p>
            <p>{props.api.ProductPrice}</p>
            <p>{props.api.ProductRating} stars of 5</p>
            <a href={props.api.ProductLink} target='_blank'>Link for Product</a>
          </div>
      </div></> : <></>}
      {/* below code was made for testing purpose can be ignored */}
      {/* <h1 className={classes.heading}>Displaying Data</h1>
      <div className={classes["product-box"]}>
          <img src="https://m.media-amazon.com/images/I/317JiGToz-L._SY445_SX342_QL70_FMwebp_.jpg" alt="product-image" />
          <div className={classes.detail}>
            <p>fdjklsfj</p>
            <p>₹fjklsdajf</p>
            <p>flksdafl </p>
          </div>
      </div> */}
      {/* <h1 className={classes.heading}>{props.site}</h1>
      <div className={classes["product-box"]}>
          <img src={props.api["ProductSRC"]} alt="product-image"
               class = {classes["product-img"]}
          />
          <div className={classes.detail}>
            <p>{props.api.ProductName}</p>
            <p>₹{props.api.ProductPrice}</p>
            <p>{props.api.ProductRating}</p>
          </div>
      </div> */}
    </>
  )
}

export default ProductDetail