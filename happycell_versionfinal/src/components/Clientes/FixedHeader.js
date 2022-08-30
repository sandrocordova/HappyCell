import React, { Fragment, useState } from "react";
import { CSSTransition, TransitionGroup } from 'react-transition-group';

import { Row, Col, Card, CardBody, Button } from "reactstrap";

import DataTable from 'react-data-table-component';

import Search from "./../Search"


const FixedHeader = () => {


    const [postResult, setPostResult] = useState(null);
    const [pagina, setPagina] = useState(1); /*Pagina*/
    const [texto, setTexto] = useState(null); /*Input de la busqueda*/
    const { cliente } = postResult || [];
    console.log(cliente);

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




    return (
        <Fragment>
            <TransitionGroup>
                <CSSTransition component="div" classNames="TabsAnimation" appear={true}
                    timeout={1500} enter={false} exit={false}>
                    <div>
                        <Search pagina={1} texto={texto} setTexto={setTexto} setPostResult={setPostResult} />
                        <div style={{ textAlign: "right" }}>

                            <br />
                            {/*<Button className="mb-2 me-2" color="info">*/}
                            {/*    Crear Cliente*/}
                            {/*</Button>*/}


                        </div>
                       

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
