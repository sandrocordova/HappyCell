import React from 'react';
import {
    Link,
} from "react-router-dom";

const Index = () => {
    return (
        <div>
            <h1>Buscar cliente</h1>
            <p>Jonathan: <Link to="clientsnat/jonnathan">Modificar</Link></p>
            <p>Sandro: <Link to="clientsnat/Sandro">Modificar</Link></p>
            <p>Carlos: <Link to="clientsnat/Carlos">Modificar</Link></p>
        </div>
    );
}

export default Index;