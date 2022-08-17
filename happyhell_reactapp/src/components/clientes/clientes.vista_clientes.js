import 'bootstrap/dist/css/bootstrap.min.css';
import { Link } from 'react-router-dom';
import './../../styled-components/styles_generales.css';
import React, { useEffect, useState, useRef } from 'react';
import { Button, Table, Form, FormGroup, Label, Input, FormText, Col, Row, InputGroup, InputGroupAddon, InputGroupText } from 'reactstrap';



const Clientesvista_clientes = () => {
    const [opcs, setOpcs] = useState([]);
    useEffect(() => {
        obtainData()
    }, []);
    const obtainData = async () => {

        const data = await fetch('http://192.168.88.103:8080/api/cliente');
        const opc = await data.json()

        setOpcs(opc)

    }




    return (
        <div>
            <div className="headerClientesSub">

                <Label style={{ color: '#c7f900' }}>
                    Mantenimiento de Clientes/Clientes
                </Label>
            </div>
            <div className="containerSearch">
                <Row>

                    <Col sm={3} style={{ marginLeft: "2%", marginRight:"10%" }}>
                        <Label for="Identificacion" style={{ color: '#c7f900' }}>Identificacion</Label>
                        <Col sm={12}>
                            <Input style={{ border: '1px solid #003462', width: "100%", height: "1%"}} type="id" name="identificacion" id="identificacion" />
                        </Col>
                    </Col>
                    <Col sm={3}>
                        <Label for="exampleEmail" style={{ color: '#c7f900' }}>Nombre</Label>
                        <Col sm={12}>
                            <Input style={{ border: '1px solid #003462', width: "100%", height:"1%" }} type="nombre" name="nombre" id="nombre" />
                        </Col>

                    </Col>
                    <Col sm={3}>
                        <Col sm={12}>
                            <Button className="buttonSearch" style={{ background: '#003462', color: "#ffffff", marginTop: "5%", marginLeft:"100%" }}>Buscar</Button>
                        </Col>

                    </Col>

                </Row>
                
            </div>
            <div className="divTable">
                <Form>


                    <div className='contenedorEstiloEnlaces'>
                        <Link to="nueva" style={{color:'#c7f900'}}>
                        <a >Crear</a>
                        </Link>
                    </div>
                    <div className='contenedor-div-tabla' >
                    <Table hover bordered className="table" style={{ border: '1px solid #003462' }} striped bordered hover>
                        <thead>
                            <tr>
                                <th>
                                    
                                </th>
                                <th>Codigo Cliente</th>
                                <th>Identificacion</th>
                                <th>Nombre</th>
                                <th>Tipo Cliente</th>
                            </tr>
                        </thead>
                        <tbody >
                            {
                                opcs.map(item=>{
                                    return (
                                        <tr key={item.CLIE_CODIGO}>
                                            <td>
                                                <Input type="checkbox" name={item.CLIE_NOMBRE} id={item.CLIE_CODIGO} />
                                            </td>
                                            <td>{item.CLIE_CODIGO}</td>
                                            <td>{item.CLIE_IDENTIFICACION}</td>
                                            <td>{item.CLIE_NOMBRE}</td>
                                            <td>{item.TICL_CODIGO}</td>
                                        </tr>
                                        );
                            })
                            

                     }
                         

                        </tbody>
                    </Table>

                    </div>
                </Form>
                <div className="containerButtonStyleFooter">
                    <Link to="/clientes/vistaclientes/clientesnaturales">
                        <Button className="buttonStyleFooter" id="select" >Seleccionar</Button>
                    
                    </Link>
                    <Link to="/clientes/vistaclientes/clientesjuridicos">
                        <Button className="buttonStyleFooter" >Cerrar</Button>
                    </Link>
                </div>

            </div >

        </div >

    )
};
export default Clientesvista_clientes;