import React from 'react';
import './styles.css';
import FormPlantilla from './mensajeria.form.plantilla';

export default class SearchBar extends React.Component{
    constructor(){
        super()
    }
    render(){
        return (
                <div>
                    <FormPlantilla/>
                </div>

            )
    }

};