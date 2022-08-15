import React from 'react';
import './styles.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button, ListGroup, ListGroupItem, UncontrolledCollapse, CardBody, Card, Row, InputGroup, InputGroupAddon, InputGroupText, Collapse } from 'reactstrap';
import { Link } from 'react-router-dom';

export default class FormMain extends React.Component {
    constructor() {
        super()
    }

    render() {
        return (
            <div className='contenedor-principal'><div className='texto-titulo'><b className=''>Menú principal</b> </div>
                <div className='contenedor-secundario'>
                    <ListGroup>
                        <ListGroupItem className='grupo-lista' href='#' id='toggler1' action><b>Menú 1</b></ListGroupItem>
                        <UncontrolledCollapse className='colapse' toggler="#toggler1">
                            <ListGroup>
                                <ListGroupItem className='item-lista' tag="button" action><b className='item-texto'>Sub Menú</b></ListGroupItem>
                                <ListGroupItem className='item-lista' tag="button" action><b className='item-texto'>Sub Menú</b></ListGroupItem>
                                <ListGroupItem className='item-lista' tag="button" action><b className='item-texto'>Sub Menú</b></ListGroupItem>
                                <ListGroupItem className='item-lista' tag="button" action><b className='item-texto'>Sub Menú</b></ListGroupItem>
                            </ListGroup>
                        </UncontrolledCollapse>
                        <ListGroupItem className='grupo-lista' href='#' id='toggler2' action><b>Menú 2</b></ListGroupItem>
                        <UncontrolledCollapse className='colapse' toggler="#toggler2">
                            <ListGroup>
                                <ListGroupItem className='item-lista' tag="button" action><b className='item-texto'>Sub Menú</b></ListGroupItem>
                                <ListGroupItem className='item-lista' tag="button" action><b className='item-texto'>Sub Menú</b></ListGroupItem>
                                <ListGroupItem className='item-lista' tag="button" action><b className='item-texto'>Sub Menú</b></ListGroupItem>
                                <ListGroupItem className='item-lista' tag="button" action><b className='item-texto'>Sub Menú</b></ListGroupItem>
                            </ListGroup>
                        </UncontrolledCollapse>
                        <ListGroupItem className='grupo-lista' href='#' id='toggler3' action><b>Menú 3</b></ListGroupItem>
                        <UncontrolledCollapse className='colapse' toggler="#toggler3">
                            <ListGroup>
                                <ListGroupItem className='item-lista' tag="button" action><b className='item-texto'>Sub Menú</b></ListGroupItem>
                                <ListGroupItem className='item-lista' tag="button" action><b className='item-texto'>Sub Menú</b></ListGroupItem>
                                <ListGroupItem className='item-lista' tag="button" action><b className='item-texto'>Sub Menú</b></ListGroupItem>
                                <ListGroupItem className='item-lista' tag="button" action><b className='item-texto'>Sub Menú</b></ListGroupItem>
                            </ListGroup>
                        </UncontrolledCollapse>
                        <ListGroupItem className='grupo-lista' href='#' id='toggler4' action><b>Menú 4</b></ListGroupItem>
                        <UncontrolledCollapse className='colapse' toggler="#toggler4">
                            <ListGroup>
                                <ListGroupItem className='item-lista' tag="button" action><b className='item-texto'>Sub Menú</b></ListGroupItem>
                                <ListGroupItem className='item-lista' tag="button" action><b className='item-texto'>Sub Menú</b></ListGroupItem>
                                <ListGroupItem className='item-lista' tag="button" action><b className='item-texto'>Sub Menú</b></ListGroupItem>
                                <ListGroupItem className='item-lista' tag="button" action><b className='item-texto'>Sub Menú</b></ListGroupItem>
                            </ListGroup>
                        </UncontrolledCollapse>
                    </ListGroup>
                    <div>
                    </div>
                </div >
            </div>

        )
    }

};