import React, { useEffect, useState } from 'react';
import './styles.css';

function CargarJson() {
    const [opcs, setOpcs] = useState([]);
    useEffect(() => {
        obtainData()
    }, []);
    const obtainData = async () => {

        const data = await fetch('http://192.168.88.103:8080/api/usernavdos');
        const opc = await data.json()

        setOpcs(opc)

    }
    const validacion = Object.values(opcs.map(item => (item.opme_descripcion)))

    return (
        
        <div>

            {
                opcs.map(item => (
                    <tr>
                    <td>{item.vent_descripcion}</td>
                    <td>{item.tipe_descripcion}</td>
                    <td>{item.vent_descripcion}</td>
                    </tr>
                ))
            }
            
        </div>

   
    )
}


export default class Row extends React.Component {

    constructor() {
        super()
        
    }

    render() {
        return (
            <div>
                <tr>
                    <th>Identificador</th>
                    <th>Nombre del Cliente</th>
                    <th>Fecha de Ingreso</th>
                </tr>
                
                <CargarJson/>
            </div>
        )
    }
};
