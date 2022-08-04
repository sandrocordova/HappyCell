import React, { useEffect, useState } from 'react';
import './styles.css';
import { Dropdown, DropdownItem, DropdownMenu, DropdownToggle } from 'reactstrap'
import { MDBCol, MDBInput } from "reactstrap";


export default class SearchBar extends React.Component{
    constructor(){
        super()
    }
    render(){
        return (
            <div>
                <form action="/" method="get">
                 
                    <div class="itemsSearchBar">

                    
                    <label htmlFor="header-search" >
                        <span className="visually-hidden">Buscar cliente </span>
                    </label>
                    <input
                        type="text"
                        id="header-search"
                        placeholder="Nombre del cliente"
                        name="s"
                    />
                    <a class="boton_buscar" href="#" type='submit'>Buscar</a>
                    </div>
                </form>

                
                
            </div>

            )
    }

};