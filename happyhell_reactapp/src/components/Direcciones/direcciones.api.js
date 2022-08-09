import React, { useEffect, useState } from 'react';

const Direccionesapi = () => {
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
export default Direccionesapi;