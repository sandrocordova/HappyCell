import 'bootstrap/dist/css/bootstrap.min.css';
import { Button, Form, FormGroup, Label, Input, FormText, Col, Row, InputGroup, InputGroupAddon, InputGroupText } from 'reactstrap';
import { Link } from 'react-router-dom';

const Clientes = () => {


    return (

        <>
            <div className="headerClientes">
                Clientes
                <br />
                Mantenimiento Clientes
            </div>

            <div className="opcionesCuadradas">
                <div className="contenedor-imagen-icono">
                    <Link to="/clientes/vistaclientes">

                        <Button className="buttonImages" title="Clientes" size="large" variant="contained" alt="Clientes">

                            <Row>
                                <Col sm={3}>
                                    <div className="contenedor-imagen">
                                        <img className="imgButton" src="https://cdn-icons-png.flaticon.com/128/3126/3126589.png" alt="Clientes" />
                                    </div></Col>
                                <Col sm={9}>
                                    <div className="contenedor-icono">
                                        CLIENTES
                                    </div>
                                </Col>
                            </Row>



                        </Button>

                    </Link>
                </div>
                <div className="contenedor-imagen-icono">
                    <Link to="/clientes/direcciones">

                        <Button className="buttonImages" title="Clientes" size="large" variant="contained" alt="Clientes">

                            <Row>
                                <Col sm={3}>
                                    <div className="contenedor-imagen">
                                        <img className="imgButton" src="https://cdn-icons.flaticon.com/png/128/2500/premium/2500132.png?token=exp=1659586952~hmac=ec66b069f5beb3b424f92f487abf6305" alt="Direcciones" />
                                    </div></Col>
                                <Col sm={9}>
                                    <div className="contenedor-icono">
                                        DIRECCIONES
                                    </div>
                                </Col>
                            </Row>



                        </Button>

                    </Link>
                </div>
                <div className="contenedor-imagen-icono">
                    <Link to="/clientes/direcciones">

                        <Button className="buttonImages" title="Clientes" size="large" variant="contained" alt="Clientes">

                            <Row>
                                <Col sm={3}>
                                    <div className="contenedor-imagen">
                                        <img className="imgButton" src="https://cdn-icons-png.flaticon.com/128/3721/3721123.png" alt="Asesor" />
                                    </div></Col>
                                <Col sm={9}>
                                    <div className="contenedor-icono">
                                        Asesor
                                    </div>
                                </Col>
                            </Row>



                        </Button>

                    </Link>
                </div>
                <div className="contenedor-imagen-icono">
                    <Link to="/clientes/direcciones">

                        <Button className="buttonImages" title="Clientes" size="large" variant="contained" alt="Clientes">

                            <Row>
                                <Col sm={3}>
                                    <div className="contenedor-imagen">
                                        <img className="imgButton" src="https://cdn-icons-png.flaticon.com/128/548/548479.png" />
                                    </div></Col>
                                <Col sm={9}>
                                    <div className="contenedor-icono">
                                        Documentos
                                    </div>
                                </Col>
                            </Row>



                        </Button>

                    </Link>
                </div>
                <div className="contenedor-imagen-icono">
                    <Link to="/clientes/direcciones">

                        <Button className="buttonImages" title="Clientes" size="large" variant="contained" alt="Clientes">

                            <Row>
                                <Col sm={3}>
                                    <div className="contenedor-imagen">
                                        <img className="imgButton" src="https://cdn-icons.flaticon.com/png/128/2117/premium/2117291.png?token=exp=1659587243~hmac=784fe0c2a06369e73f08417f8f807a83" />
                                    </div></Col>
                                <Col sm={9}>
                                    <div className="contenedor-icono">
                                        Referencias Comerciales
                                    </div>
                                </Col>
                            </Row>



                        </Button>

                    </Link>
                </div>


                <div className="contenedor-imagen-icono">
                    <Link to="/clientes/direcciones">

                        <Button className="buttonImages" title="Clientes" size="large" variant="contained" alt="Clientes">

                            <Row>
                                <Col sm={3}>
                                    <div className="contenedor-imagen">
                                        <img className="imgButton" src="https://cdn-icons.flaticon.com/png/128/2202/premium/2202967.png?token=exp=1659587138~hmac=90f963cd17ec37f4da8460c86c89f9bc" />
                                    </div></Col>
                                <Col sm={9}>
                                    <div className="contenedor-icono">
                                        Referencias Bancarias
                                    </div>
                                </Col>
                            </Row>



                        </Button>

                    </Link>
                </div>
                <div className="contenedor-imagen-icono">
                    <Link to="/clientes/direcciones">

                        <Button className="buttonImages" title="Clientes" size="large" variant="contained" alt="Clientes">

                            <Row>
                                <Col sm={3}>
                                    <div className="contenedor-imagen">
                                        <img className="imgButton" src="https://cdn-icons-png.flaticon.com/128/649/649001.png" />
                                    </div></Col>
                                <Col sm={9}>
                                    <div className="contenedor-icono">
                                        Situacion Financiera
                                    </div>
                                </Col>
                            </Row>



                        </Button>

                    </Link>
                </div>




            </div>



        </>
    )

};

export default Clientes;
