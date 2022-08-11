import React, { useEffect, useState,useRef } from 'react';
import './styles.css';
import { Link } from 'react-router-dom'



const Navmenopc = () => {
    const [opcs, setOpcs] = useState([]);
    useEffect(() => {
        obtainData()
    }, []);
    const obtainData = async () => {

        const data = await fetch('http://192.168.88.103:8080/api/usernavdos');
        const opc = await data.json()

        setOpcs(opc)

    }

    const validacion = Object.values(opcs.map(item => (item.opme_descripcion)))
    const validacion2 = [...new Set(validacion)]
    const ref = useRef(null);
    const scroll = (scrollOffset) => {
        ref.current.scrollLeft += scrollOffset;
    };
    return (


        <>
            <div >
                <button onClick={() => scroll(-20)}>LEFT</button>
                <Link to="/mensajeria" className="CarouselStyle">
                    Mensajeria
                </Link>
                <div className="id='slider'
          className='w-full h-full overflow-x-scroll scroll whitespace-nowrap scroll-smooth scrollbar-hide'" >
                    {validacion2.map((item) => (

                        <Link to="/clientes" className="CarouselStyle">
                            {item}
                        </Link>

                    ))}
                </div>
                <button onClick={() => scroll(20)}>RIGHT</button>
            </div>

        </>

    )
};
export default Navmenopc;