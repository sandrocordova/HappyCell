import React from 'react';
import './styles.css';
import FormBuscar from './mensajeria.form.buscar';
import FormPlantilla from './mensajeria.form.plantilla';

export default class SearchBar extends React.Component{
    constructor(){
        super()
    }
    render(){
        return (
            <div className="contenedor-general">
                <div className="contenedor-buscar-edit">
                    <FormBuscar/>
                </div>
                <div className="contenedor-plantilla-edit">
                    <FormPlantilla/>
                </div>
            </div>

            )
    }

};