import 'bootstrap/dist/css/bootstrap.min.css';
import { Button, Form, FormGroup, Label, Input, FormText, Col, Row, InputGroup, InputGroupAddon, InputGroupText } from 'reactstrap';
import { Link } from 'react-router-dom';

const Clientes = () => {


    return (

        <div>
            <div className="headerClientes">
                Clientes
                <br />
                Mantenimiento Clientes
            </div>

            <div className="opcionesCuadradas">

                <Link to="/clientes/vistaclientes">

                    <Button className="buttonImages" title="Clientes" size="large" variant="contained" alt="Clientes">
                        <p>Clientes</p>
                        <img className="imgButton" src="https://cdn-icons-png.flaticon.com/128/3126/3126589.png" alt="Clientes" />

                    </Button>
                </Link>
                <Link to="/clientes/direcciones">
                <Button className="buttonImages" title="Direcciones" size="large" variant="contained" alt="Direcciones">
                    <p>Direcciones</p>
                    <img className="imgButton" src="https://cdn-icons.flaticon.com/png/128/2500/premium/2500132.png?token=exp=1659586952~hmac=ec66b069f5beb3b424f92f487abf6305" alt="Direcciones" />
                    </Button>
                </Link>
                <Button className="buttonImages" title="Asesor" size="large" variant="contained" alt="Asesor">
                    <p>Asesor</p>
                    <img className="imgButton" src="https://cdn-icons-png.flaticon.com/128/3721/3721123.png" alt="Asesor" />
                </Button>
                <Button className="buttonImages" title="Documentos" size="large" variant="contained">
                    <p>Documentos</p>
                    <img className="imgButton" src="https://cdn-icons-png.flaticon.com/128/548/548479.png" />
                </Button>
                <br/>
                <Button className="buttonImages" title="Referencias Comerciales" size="large" variant="contained" alt="Referencias Comerciales">
                    <p>Referencias Comerciales</p>
                    <img className="imgButton" src="https://cdn-icons.flaticon.com/png/128/2117/premium/2117291.png?token=exp=1659587243~hmac=784fe0c2a06369e73f08417f8f807a83" />
                </Button>
               
                <Button className="buttonImages" title="Referencias Bancarias" size="large" variant="contained">
                    <p>Referencias Bancarias</p>
                    <img className="imgButton" src="https://cdn-icons.flaticon.com/png/128/2202/premium/2202967.png?token=exp=1659587138~hmac=90f963cd17ec37f4da8460c86c89f9bc" />
                </Button>
                <Button className="buttonImages" title="Situacion Financiera" size="large" variant="contained">
                    <p>Situacion Financiera</p>
                    <img className="imgButton" src="https://cdn-icons-png.flaticon.com/128/649/649001.png" />
                </Button>


            </div>

        </div>


    )

};

export default Clientes;
