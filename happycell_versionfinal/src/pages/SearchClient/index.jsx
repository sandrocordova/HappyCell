import React, { Fragment, useState } from 'react';
import ReactPaginate from 'react-paginate';
import { useHistory } from "react-router-dom";
import { useDispatch } from 'react-redux';
import PageTitle from "../../Layout/AppMain/PageTitle";
import {
    Row,
    Col,
    Button,
    Container,
    Card,
    CardBody,
    Input,
    CardHeader,
} from "reactstrap";
import DataTable from 'react-data-table-component';
import { searchClient } from '../../Api/apicall_search';
import { addClient } from '../../features/clients/clientsSlice';
import LoadingOverlay from "react-loading-overlay-ts";
import { Loader } from "react-loaders";
import SweetAlert from 'react-bootstrap-sweetalert';


const Index = () => {

    const history = useHistory();
    const dispatch = useDispatch();

    const [data, setData] = useState([]);
    const [pagina, setPagina] = useState(1);
    const [searchText, setSearchText] = useState("");
    const { cliente } = data || [];
    const [selectedData, setSelectedData] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");
    const [isSelected, setIsSelected] = useState(false);

    const handleChange = (state) => {
        setSelectedData(state.selectedRows);
    };

    const handlePageClick = async (event) => {
        setError("")
        setLoading(true)
        setPagina(event.selected + 1)
        try {
            const result = await searchClient(searchText, pagina);
            setLoading(false)
            if (result?.status === '400') {
                setError(result.message)
            } else {
                setData(result);
            }
        } catch (err) {
            setError("Ha ocurrido un error")
            setLoading(false)
        }
    };

    const postSearch = async () => {
        setError("")
        setLoading(true)
        setPagina(1)
        try {
            const result = await searchClient(searchText, pagina);
            setLoading(false)
            if (result?.status === '400') {
                setError(result.message)
            } else {
                setData(result);
            }
        } catch (err) {
            setError("Ha ocurrido un error")
            setLoading(false)
        }
    }

    const redirectPage = () => {
        if (selectedData.length === 0) {
            setIsSelected(true)
        } else {
            if (selectedData[0].TICL_CODIGO === "N") {
                dispatch(addClient(selectedData[0]))
                history.push(`/clients/clientsnat/${selectedData[0].CLIE_CODIGO}`)
            } else if (selectedData[0].TICL_CODIGO === "J") {
                history.push(`/clients/clientsjur/${selectedData[0].CLIE_CODIGO}`)
            }
        }
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

    return (
        <Fragment>
            <PageTitle
                heading="Buscar cliente"
                icon="lnr-earth icon-gradient bg-tempting-azure"
            />
            <SweetAlert
                type="info"
                title="Debe de seleccionar un cliente para continuar"
                show={isSelected}
                onConfirm={() => setIsSelected(false)}
                timeout={2000}
            />

            <SweetAlert title={error} show={error ? true : false}
                type="warning" onConfirm={() => setError("")} />

            <Container fluid>
                <Row>
                    <Card>
                        <CardHeader>
                            <Row>
                                <Col md={10}>
                                    <Input type="search" className="form-control" placeholder="Ingrese cedula o nombre" onChange={e => setSearchText(e.target.value)} />
                                </Col>
                                <Col md={2}>
                                    <Button className="info" onClick={postSearch}>Buscar</Button>
                                </Col>
                            </Row>
                        </CardHeader>
                        <CardBody>
                            <Row>
                                <Col md={12}>
                                    <LoadingOverlay tag="div" active={loading}
                                        styles={{
                                            overlay: (base) => ({
                                                ...base,
                                                background: "#fff",
                                                opacity: 0.5,
                                            }),
                                        }}
                                        spinner={
                                            <Loader color="#ffffff" active type={"ball-clip-rotate"} />
                                        }>
                                        <DataTable
                                            data={cliente}
                                            columns={columns}
                                            selectableRows
                                            fixedHeader
                                            paginationTotalRows={1}
                                            fixedHeaderScrollHeight="400px"
                                            selectableRowsSingle
                                            onSelectedRowsChange={handleChange}
                                        />
                                    </LoadingOverlay>
                                </Col>
                            </Row>
                            <Row>
                                <Col md={12} className="mt-2">
                                    <ReactPaginate
                                        className='list-unstyled d-flex mx-2'
                                        previousClassName='btn btn-outline-primary'
                                        nextClassName='btn btn-outline-primary'
                                        pageClassName='btn btn-outline-secondary mx-1'
                                        breakClassName='btn btn-outline-secondary mx-1'
                                        activeClassName='btn btn-primary text-white'
                                        breakLabel="..."
                                        nextLabel="siguiente >"
                                        previousLabel="< anterior"
                                        onPageChange={handlePageClick}
                                        pageCount={Math.ceil(data?.paginas)}
                                    />
                                </Col>
                            </Row>
                            <Row>
                                <Col md={12} className="mt-2">
                                    <div className='d-flex justify-content-end'>
                                        <Button className="mb-2 me-2" color="success" onClick={redirectPage}>
                                            Seleccionar
                                        </Button>
                                    </div>
                                </Col>
                            </Row>
                        </CardBody>
                    </Card>
                </Row>
            </Container>
        </Fragment>
    );
}

export default Index;