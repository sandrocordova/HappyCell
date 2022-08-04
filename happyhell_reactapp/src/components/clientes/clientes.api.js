import React, { useEffect, useState } from 'react';

const Clientesapi = () => {
    const [opcs, setOpcs] = useState([]);
    useEffect(() => {
        obtainData()
    }, []);
    const obtainData = async () => {

        const data = await fetch('urldelaAPI');
        const opc = await data.json()

        setOpcs(opc)

    }


    return (

        <>
        </>


    )
};
export default Clientesapi;