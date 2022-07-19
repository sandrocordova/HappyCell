import React from 'react'; // importamos react
//import ReactDOM from 'react-dom'; // nos permite renderizar en el DOM
import './index.css';
import App from './App';
const root = document.getElementById('root'); // hay un div con id root en index.html
function VistaInicial(){
        return (
            <form>
                <label>Cedula:
                    <input type="Cedula" />
                    <input type="Nombre" />
                </label>
                <App />
            </form>
            
            )
}


//selecionamos el id donde se renderizara el componente

