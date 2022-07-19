import React from 'react';
import './App.css';
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
    return (
        <>
            <div className="table-responsive">
            <table className="table table-hover">
                <thead>
                    <tr>
                        <th>Nro. Credito</th>
                        <th>Fecha Concesion</th>
                        <th>Monto Financiado</th>
                        <th>Saldo Adeudado</th>
                        <th>Estado</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>1234-00</td>
                        <td>31-12-2021</td>
                        <td>$400</td>
                        <td>$100</td>
                        <td>DESEMBOLSADO</td>
                    </tr>
                    <tr>
                        <td>1567-00</td>
                        <td>31-12-2021</td>
                        <td>$300</td>
                        <td>$100</td>
                        <td>DESEMBOLSADO</td>
                    </tr>
                </tbody>
                </table>
            </div>
        </>

    )
}

export default App;
