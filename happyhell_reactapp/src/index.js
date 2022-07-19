import React from 'react'; // importamos react
import ReactDOM from 'react-dom'; // nos permite renderizar en el DOM
import './index.css';
import App from './App';
const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
    <React.StrictMode>
        <form>
                <label>Cedula:
                <input type="Cedula" />
                
                </label>
                <input type="Nombre" />
                    
          
            <App />
        </form>
    </React.StrictMode>
);



//selecionamos el id donde se renderizara el componente

