import React, { Fragment } from "react";
import { CSSTransition, TransitionGroup } from 'react-transition-group';

import { Row, Col, Card, CardBody, Button, Table, Form, FormGroup, Label, Input, FormText, InputGroup, InputGroupAddon, InputGroupText } from "reactstrap";


import DataTable from 'react-data-table-component';

import PageTitle from "../../Layout/AppMain/PageTitle";



export default class DataTableFixedHeader extends React.Component {


    state = {
        data: []

    }
    async componentDidMount() {
        await this.fetchDataTableFixedHeader()
    }

    fetchDataTableFixedHeader = async () => {
        let res = await fetch("{/cliente/view");
        let data = await res.json();
        this.setState({
            data
        })

    }


    render() {
        const { data } = this.state;
        console.log(data);
        const columns = [
            {
                name: "Tipo de direccion",
                selector: row => row.firstName,
                sortable: true,
            },
            {
                name: "Secuencia",
                selector: row => row.status,
                sortable: true,
            },
            {
                name: "Ciudad",
                id: "lastName",
                selector: row => row.lastName,
                sortable: true,
            },

            {
                name: "Direccion",
                selector: row => row.age,
                sortable: true,
            },
            {
                name: "Provincia",
                id: "lastName",
                selector: row => row.lastName,
                sortable: true,
            },

            {
                name: "Canton",
                selector: row => row.age,
                sortable: true,
            },
            {
                name: "Parroquia",
                selector: row => row.age,
                sortable: true,
            },


        ];

        return (
            <Fragment>
                <TransitionGroup>

                    <CSSTransition component="div" classNames="TabsAnimation" appear={true}
                        timeout={1500} enter={false} exit={false}>
                        <div>
                            <PageTitle
                                heading="Direcciones"

                                icon="pe-7s-medal icon-gradient bg-tempting-azure"
                            />


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
                                        <Input type="email" name="email" id="exampleEmail"  />
                                   

                                </Col>

                                <Col sm={4}>
                                 
                                    
                                        <Label for="exampleEmail">Nombre</Label>
                                        <Input type="email" name="email" id="exampleEmail"  />
                                  

                                </Col>




                            </Row>
                            <br/>
                            <Row>
                                <Col md="12">
                                    <Card className="main-card mb-3">
                                        <CardBody>
                                            <DataTable data={data}
                                                columns={columns}
                                                pagination
                                                selectableRows
                                                fixedHeader
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
}
