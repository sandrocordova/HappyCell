import React from 'react';
import './styles.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button } from "reactstrap";


export default class Rows extends React.Component {
    constructor() {
        super()
    }
    render() {
        return (
            <div class="boton-regresar">
                <Button color="primary" size="sm">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-caret-left-fill" viewBox="0 0 16 16">
                        <path d="m3.86 8.753 5.482 4.796c.646.566 1.658.106 1.658-.753V3.204a1 1 0 0 0-1.659-.753l-5.48 4.796a1 1 0 0 0 0 1.506z" />
                    </svg> Regresar
                </Button>
            </div>
        )
    }
};
