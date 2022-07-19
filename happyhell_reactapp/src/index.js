import React from 'react'; // importamos react
import ReactDOM from 'react-dom'; // nos permite renderizar en el DOM
import './index.css';
import App from './App';
const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
    <React.StrictMode>
        <form>
            HAPPY
            <div class="cabecera">
                <cabecera>
                    SISTEMA DE ADMINISTRACION DE CARTERA
                </cabecera>
                <cabecera>
                    Ciudad:Quito Agencia Villaflora

                </cabecera>

            </div>
            <div class="sizeLetra">
                <div class="redondeado">
                    <redondeado>
                        <sizeLetra>
                            <label>Cedula:
                                <input type="Cedula" />
                            </label>
                        </sizeLetra>
                    </redondeado>
                </div>
            </div>
            <div class="sizeLetra">
                <div class="redondeado">
                    <input type="Nombre" />
                </div>
            </div>
            <App />
        </form>
    </React.StrictMode>
);



//selecionamos el id donde se renderizara el componente

