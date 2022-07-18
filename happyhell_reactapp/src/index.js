import React from 'react'; // importamos react
import ReactDOM from 'react-dom'; // nos permite renderizar en el DOM
const HolaMundo = <h1>Hola Mundo</h1>
//selecionamos el id donde se renderizara el componente
const root =  document.getElementById('root'); // hay un div con id root en index.html
ReactDOM.render(HolaMundo, root); // pinta en la pantalla la constante HolaMundo en el div con id root
