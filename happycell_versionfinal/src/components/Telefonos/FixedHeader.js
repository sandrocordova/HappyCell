import React, { Fragment, useState } from "react";
import { CSSTransition, TransitionGroup } from 'react-transition-group';

import { Row, Col, Card, CardBody, Button ,Label,Input} from "reactstrap";

import DataTable from 'react-data-table-component';

import Search from "./../Search"


const FixedHeader = () => {


    const [postResult, setPostResult] = useState(null);
    const [pagina, setPagina] = useState(1); /*Pagina*/
    const [texto, setTexto] = useState(null); /*Input de la busqueda*/
    const { cliente } = postResult || [];
    console.log(cliente);
    var arrayEnviar = [];
    const paginasOpciones = {
        rowsPerPageText: 'Filas por Pagina',
        rangeSeparatorText: 'de',
        selectAllRowsItem: true,
        selectAllRowsItemText: "Todos"
    }
    const columns = [
        {
            name: "Codigo Cliente",
            selector: row => row.CLIE_CODIGO,
            sortable: true,
        },
        {
            name: "Tipo de identificacion",
            selector: row => row.TIDO_CODIGO,
            sortable: true,
        },
        {
            name: "Identificacion",

            selector: row => row.CLIE_IDENTIFICACION,
            sortable: true,
        },

        {
            name: "Nombre",
            selector: row => row.CLIE_NOMBRE,
            sortable: true,
        },
        {
            name: "Tipo Cliente",
            selector: row => row.TICL_CODIGO,
            sortable: true,
        },


    ];



    console.log(texto);
    console.log(postResult);
    const [selectedData, setSelectedData] = React.useState();

    const handleChange = (state) => {
        setSelectedData(state.selectedRows);
        console.log(selectedData);
        console.log("hola mundo");
    };




    return (
        <Fragment>
            <TransitionGroup>
                <CSSTransition component="div" classNames="TabsAnimation" appear={true}
                    timeout={1500} enter={false} exit={false}>
                    <div>

                        <Row>

                            <Col sm={2}>

                                <Label for="exampleEmail">Tipo de cliente</Label>
                                <Input type="email" name="email" id="exampleEmail" />

                            </Col>

                            <Col sm={2}>
                                <Label for="exampleEmail">Codigo cliente</Label>
                                <Input type="email" name="email" id="exampleEmail" />
                            </Col>
                            <Col sm={2}>
                                <Label for="exampleEmail">Tipo de identificacion</Label>
                                <Input type="email" name="email" id="exampleEmail" />

                            </Col>
                            <Col sm={2}>


                                <Label for="exampleEmail">Identificacion</Label>
                                <Input type="email" name="email" id="exampleEmail" />


                            </Col>

                            <Col sm={4}>


                                <Label for="exampleEmail">Nombre</Label>
                                <Input type="email" name="email" id="exampleEmail" />


                            </Col>




                        </Row>

                        <Row>

                            <Col sm={1}>

                                <Label for="exampleEmail">Secuencia</Label>
                                <Input type="email" name="email" id="exampleEmail" />

                            </Col>

                            <Col sm={2}>
                                <Label for="exampleEmail">Ciudad</Label>
                                <Input type="email" name="email" id="exampleEmail" />
                            </Col>
                            <Col sm={6}>
                                <Label for="exampleEmail">Direccion</Label>
                                <Input type="email" name="email" id="exampleEmail" />

                            </Col>
 



                        </Row>
                        <Row>

                            <Col sm={1}>

                                <Label for="exampleEmail">Secuencia</Label>
                                <Input type="email" name="email" id="exampleEmail" />

                            </Col>






                        </Row>
                        <br />

                        <Row>
                            <Col md="12">
                                <Card className="main-card mb-3">
                                    <CardBody>
                                        <DataTable data={cliente}
                                            columns={columns}
                                            pagination
                                            paginationComponentOptions={paginasOpciones}
                                            selectableRows
                                            fixedHeader
                                            paginationTotalRows={1}
                                            onSelectedRowsChange={handleChange}
                                            fixedHeaderScrollHeight="400px"
                                        />
                                    </CardBody>
                                </Card>
                            </Col>
                        </Row>
                    </div>
                </CSSTransition>
            </TransitionGroup>
        </Fragment>
    );



}
export default FixedHeader;
