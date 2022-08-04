import React from 'react';
import './styles.css';
import Formcampos from './mensajeria.form.ejecucion';
import FormMenu from '../mensajeria.menu';

export default class FormMain extends React.Component {
    constructor() {
        super()
    }
    render() {

        return (
            <body>
                <div class="backbutton">
                    <FormMenu/>
                </div>
                <div class="backbutton">
                    <Formcampos/>
                </div>

            </body>

        )
    }
};
