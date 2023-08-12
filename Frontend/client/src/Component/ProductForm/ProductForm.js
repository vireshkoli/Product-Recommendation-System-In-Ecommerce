import React, { useCallback, useEffect, useState } from 'react'

import ProductDetail from '../ProductDetail/ProductDetail';
import ErrorModel from '../ErrorModel/ErrorModel';
import classes from "./ProductForm.module.css";

const ProductForm = (props) => {
  console.log("Hello displaying first data");

  // setting the obtained data for a product 
  const [data1,setData1]=useState(props?.apiData)
  // console.log(props.apiData[0]);

  // setting the obtained data
  useEffect(()=>{
    console.log(props?.apiData,'filter')
    setData1(props?.apiData);
  },[props?.apiData])


  return (
    <>
      <form onSubmit={props.onFormSubmit}>
        <label className={classes["form-label"]}>Enter Product Name: </label>
        <input 
            type="text" 
            ref={props.inputRef} 
            className={classes["form-input"]}
        />
        <button type="submit" value="Submit" className={classes["form-button"]}>Submit</button>
      </form>

      {/* below code contains dummy value which will show the result if product has been found or not found
          basically used for styling purpose
      */}
      {/* <ProductDetail api = {{
        ProductName: "Apple iPhone 12 (64GB) - White",
        ProductPrice: '53,999',
        ProductRating: "4.5 stars out of 5",
        ProductSRC: "https://m.media-amazon.com/images/I/317JiGToz-L._SY445_SX342_QL70_FMwebp_.jpg"
      }} 
        site = "Amazon Data"
      />
      <ProductDetail api = {{
        ProductName: "APPLE iPhone 12 (Black, 64 GB)",
        ProductPrice: "53,999",
        ProductRating: "4 stars out of 5",
        ProductSRC: "https://rukminim1.flixcart.com/image/416/416/kg8avm80/mobile/r/h/z/apple-iphone-12-dummyapplefsn-original-imafwg8duby8qbn4.jpeg?q=70"
      }} 
        site = "Filpkart Data"
      />
      <ProductDetail api = {{
        ProductName: "APPLE iPhone 12 (Black, 64 GB)",
        ProductPrice: "53,999",
        ProductRating: "4 stars out of 5",
        ProductSRC: "https://rukminim1.flixcart.com/image/416/416/kg8avm80/mobile/j/f/9/apple-iphone-12-dummyapplefsn-original-imafwg8dkyh2zgrh.jpeg?q=70"
      }} 
        site = "Reliance Data"
      /> */}

      {/* If error is not there then only show product otherwise show error */}
      {
        !props.isError ? 
        <>
          <ProductDetail api={data1[0]} />
          <ProductDetail api={data1[1]} />
          <ProductDetail api={data1[2]} />
        </> : <><ErrorModel></ErrorModel></>
      }
      
    </>
  )
}

export default ProductForm