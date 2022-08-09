import React, { useEffect, useState } from 'react';
import './styles.css';
import SearchBar from './SearchBar';
import Rows from './Rows';
import Row from './Row';
import Form from './Form';

export default class FormMain extends React.Component{
    constructor(){
        super()
    }
    render(){

    return (
        
            <div class="contenedorPrincipal">
                <div class = "searchBar">
                    <SearchBar/>
                    <Rows/>
                </div>
                <div class='tableSearch' id="uno">
                    <Form/>
                </div>
                
            </div>

    )
    }
};
