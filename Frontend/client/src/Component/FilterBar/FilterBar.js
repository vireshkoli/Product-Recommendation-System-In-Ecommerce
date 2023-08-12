import React from 'react'

import classes from './FilterBar.module.css';

const FilterBar = (props) => {

    // to get if the user selects price or rating
    const handleChange = (event) => {
        props.onFilterData(event.target.value);
    }

  return (
    <nav className={classes['filter-bar']}>
        <div className={classes['filter-data']}>
            <label htmlFor='parameter'>Filter According to: </label>
            <select name='parameter' id='parameter' className={classes.select} onChange={handleChange}>
                <option>Parameter</option>
                <option value="price">Price</option>  
                <option value="rating">Rating</option>  
            </select>
        </div>
    </nav>
  )
}

export default FilterBar