import React from 'react'; // importamos react
import ReactDOM from 'react-dom'; // nos permite renderizar en el DOM
import './index.css';
import App from './App';
const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
    <React.StrictMode>
        <form>
            <div class="h2">
                <h2>
                    SISTEMA DE ADMINISTRACION DE CARTERA
                </h2>
                <h2>
                    Ciudad:Quito
                    AGENCIA VILLAFLORA-COSTOS CAJA
                </h2>
            </div>
            <div class="redondeado">
                <redondeado>
                    <label>Cedula:
                    <input type="Cedula" />
                        </label>
               
                </redondeado>
            </div>
             <div class="redondeado">
                <input type="Nombre" />
            </div>
            <App />
        </form>
    </React.StrictMode>
);



//selecionamos el id donde se renderizara el componente

