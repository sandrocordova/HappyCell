import React from 'react';
import './styles.css';
import Formcampos from './mensajeria.form';
import FormMenu from '../mensajeria.menu';
import { Link } from 'react-router-dom';

export default class FormMain extends React.Component {
    constructor() {
        super()
    }
    render() {

        return (
            <body>
                <div class="contenedor-br-3">
                    <div class="contenedor-br-3-int">
                            <Link to="/mensajeria">
                                <a>Mensajería</a>
                            </Link>/<Link to="/mensajeria/plantillas">
                                <a>Mensajería Plantilla</a>
                            </Link>
                    </div>
                </div>
                <div>
                    <Formcampos />
                </div>

            </body>

        )
    }
};
