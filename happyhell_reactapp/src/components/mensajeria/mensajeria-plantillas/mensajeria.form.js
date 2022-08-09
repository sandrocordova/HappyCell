import React from 'react';
import './styles.css';
import FormBuscar from './mensajeria.form.buscar';
import FormPlantilla from './mensajeria.form.plantilla';

export default class SearchBar extends React.Component {
    constructor() {
        super()
    }
    render() {
        return (
            <div>
            
                    <FormBuscar />
            
                <div className="contenedor-tabla">
                    <div className="contenedor-plantilla-edit">
                        <FormPlantilla />
                    </div>
                </div>
            </div>

        )
    }

};