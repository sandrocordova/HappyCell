import React from 'react';
import './styles.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import FormBuscar from './mensajeria.form.buscar';
import FormPlantilla from './mensajeria.form.plantilla';

export default class SearchBar extends React.Component{
    constructor(){
        super()
    }
    render(){
        return (
            <div className="contenedor-general">
                    <FormBuscar/>
                <div className="contenedor-plantilla-edit">
                    <FormPlantilla/>
                </div>
            </div>

            )
    }

};