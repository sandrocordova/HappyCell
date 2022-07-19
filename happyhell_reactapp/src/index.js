import React from 'react'; // importamos react
import ReactDOM from 'react-dom'; // nos permite renderizar en el DOM
import './index.css';
import App from './App';
const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
    <React.StrictMode>
        <form>
            <div style="border-radius: 10px;">
                <label>Cedula:
                    <input type="Cedula" />
                </label>
                <br>
                    <input type="Nombre" />
                </br>
           </div>
            <App />
        </form>
    </React.StrictMode>
);



//selecionamos el id donde se renderizara el componente

