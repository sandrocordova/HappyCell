import React from 'react';
import './styles.css';
import FormPlantilla from './mensajeria.form.plantilla.editar';

export default class SearchBar extends React.Component {
    constructor() {
        super()
    }
    render() {
        return (
            <div className="contenedor-plantilla-edit">
                <FormPlantilla/>
            </div>
        )
    }

};