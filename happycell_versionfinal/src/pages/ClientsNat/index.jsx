import React from 'react';
import {
    useParams
} from "react-router-dom";

const Index = () => {
    let { id } = useParams();
    return (
        <div>
            <h1>Cliente Natural</h1>
            <h2>{id}</h2>
        </div>
    );
}

export default Index;