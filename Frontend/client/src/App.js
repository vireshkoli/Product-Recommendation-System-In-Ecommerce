import { useState, useRef, useEffect } from "react"; 

import './App.css';
import ProductForm from './Component/ProductForm/ProductForm';
import FilterBar from './Component/FilterBar/FilterBar';

function App() {

  // state for maintaning data throught API
  const [data , setData] = useState([{
    SiteName: '',
    ProductLink: '',
    ProductName: '',
    ProductPrice: '',
    ProductRating: '',
    ProductSRC: ''
  },
  {
    SiteName: '',
    ProductLink: '',
    ProductName: '',
    ProductPrice: '',
    ProductRating: '',
    ProductSRC: ''
  },
  {
    SiteName: '',
    ProductLink: '',
    ProductName: '',
    ProductPrice: '',
    ProductRating: '',
    ProductSRC: ''
  }]);

  // state which tells whether error has occured or not, i.e was able find data or not
  const [isError, setIsError] = useState(false);

  // A refernce is created was input field
  const productRef = useRef('');

  // const validate_data = (amazon_data, flipkart_data) => {

  // }

  const getData = async () => {
    await fetch("/data").then((res) => {
      res.json().then((data) => {
        console.log(typeof(data))
        console.log(data)
        setData(data)
      })
    })
  }

  // copy of the original data used when filter is used
  const [copyData,setcopydata]=useState([{
    SiteName: '',
    ProductLink: '',
    ProductName: '',
    ProductPrice: '',
    ProductRating: '',
    ProductSRC: ''
  },
  {
    SiteName: '',
    ProductLink: '',
    ProductName: '',
    ProductPrice: '',
    ProductRating: '',
    ProductSRC: ''
  },
  {
    SiteName: '',
    ProductLink: '',
    ProductName: '',
    ProductPrice: '',
    ProductRating: '',
    ProductSRC: ''
  }]);

  // used to filter the data according to price and rating
  const filterParameter = (parameter) => {
    console.log(parameter);
    const copyData = data;
    if (parameter == 'price') {
      copyData.sort((a, b) => {
        return a.ProductPrice - b.ProductPrice
      })
      
    } else if (parameter == 'rating') {
      copyData.sort((a, b) => {
        return a.ProductRating - b.ProductRating
      })
      copyData.reverse();
    }
    setcopydata(copyData);
    console.log(copyData);
    
  }

  // when the form is submitted
  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log(productRef.current.value);

    const res = await fetch('/GetInput', {
      method: "POST", 
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        ProductName: productRef.current.value,
      })
    })
    
    if (res.ok) {
      getData();
      productRef.current.value = '';
      setIsError(false);
    } else {
      console.log("Something went wrong")
      setIsError(true);
    }
  }

  // for setting the copy data as the original data
  useEffect(()=>{
    setData(copyData);
  },[copyData])

  return (
    <div className="App">
      <span className="main-title-1">COMPARY</span>
      <span className="main-title-2">ZONE</span>
      {/* below code displayes filter  */}
      {
        data[0].ProductSRC && data[1].ProductSRC && data[2].ProductSRC ? 
          <FilterBar 
            onFilterData = {filterParameter}
          /> : <></>
      }
      {/* below code displayes input feild and products */}
      <ProductForm 
        onFormSubmit={handleSubmit}
        inputRef = {productRef}
        apiData = {data}
        isError = {isError}
      />
    </div>
  );
}

export default App;
