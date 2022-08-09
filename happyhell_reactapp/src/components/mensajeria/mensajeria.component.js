import { Link } from 'react-router-dom';
import { Button } from 'reactstrap';

const Clientes = () => {


    return (

        <div>


            <div className="opcionesCuadradas">

                <Link to="/mensajeria/parametros">
                    <Button className="buttonImages" title="Clientes" size="large" variant="contained" alt="Clientes">
                        <p>Mensajería <br></br> Parametros</p>
                        <img className="imgButton" src="https://cdn-icons-png.flaticon.com/128/3126/3126589.png" alt="Clientes" />

                    </Button>
                </Link>
                <Link to="/mensajeria/plantillas">
                <Button className="buttonImages" title="Direcciones" size="large" variant="contained" alt="Direcciones">
                    <p>Mensajería <br></br> Plantilla</p>
                    <img className="imgButton" src="https://cdn-icons-png.flaticon.com/128/548/548479.png" alt="Direcciones" />
                </Button>
                </Link>
                <Link to="/mensajeria/ejecucion">
                <Button className="buttonImages" title="Asesor" size="large" variant="contained" alt="Asesor">
                    <p>Mensajería <br></br> Ejecución</p>
                    <img className="imgButton" src="https://cdn-icons-png.flaticon.com/128/3721/3721123.png" alt="Asesor" />
                </Button>
                </Link>

            </div>

        </div>


    )

};

export default Clientes;
