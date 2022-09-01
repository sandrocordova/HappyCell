import React, { Fragment, useState, useEffect } from "react";
import Select from "react-select";
import { useParams } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import {
  Row,
  Col,
  Button,
  Container,
  Card,
  CardBody,
  Input,
  FormGroup,
  Label,
  Modal,
  Form,
  Alert,
} from "reactstrap";
import PageTitle from "../../Layout/AppMain/PageTitle";
import swal from "sweetalert";
import Loader from "react-loaders";
import ClientInfo from "../../components/ClientInfo";
import ClientMoreInfo from "../../components/ClientMoreInfo";
import { getCatalogos, updateClienteJuridico } from "../../Api/apicall_cliente";
import { addCatalogos } from "../../features/catalogs/catalogsSlice";
import {
  buscarNacionalidad,
  buscarTipoClase,
  buscarActividadEconomica,
  buscarCategoriaCliente,
  buscarTipoRol,
  buscarTipoEmpresa,
} from "../../utilities/searchCatalogType";
import { formatDateZone } from "../../utilities/utilities";

const Index = () => {
  const params = useParams();
  const dispatch = useDispatch();

  // statados para almacenar las listas de los catalogos
  const [nacionalidadList, setNacionalidadList] = useState(null);
  const [tipoClaseList, setTipoClaseList] = useState(null);
  const [actividadEcList, setActividadEcList] = useState(null);
  const [tipoProyectoList, setTipoProyectoList] = useState(null);
  const [tipoRolList, setTipoRolList] = useState(null);
  const [tipoEmpresaList, setTipoEmpresaList] = useState(null);
  // estados de utilidad
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(false);
  const [isOpen, setIsOpen] = useState(false);
  // estado para guardar los datos del formulario
  const [values, setValues] = useState(null);
  /**
   * * El estado debe de guardar los datos que vienen de la busqueda o simplemente utilizar axios
   */
  const client = useSelector((state) => state.client);
  const catalogs = useSelector((state) => state.catalogs);

  // Funcion que escucha los cambios en los formularios de los imputs tipo texto y date
  const handleChange = (name) => (event) => {
    setValues({ ...values, [name]: event.target.value });
  };

  // Funcion que escucha los cambios en los formularios de los selects
  const handleSelectChange = (name) => (event) => {
    setValues({ ...values, [name]: event.value });
  };

  // Funcion para actualizar datos del cliente en la API
  const clickSubmit = (e) => {
    e.preventDefault();
    swal({
      title: "¿Estas seguro?",
      text: "¡No podrás revertir esto!",
      icon: "info",
      buttons: ["Cancelar", "Si, actualizar!"],
      infoMode: true,
    }).then((value) => {
      if (value) {
        setError(false);
        setLoading(true);
        updateClienteJuridico(client.CLIE_CODIGO, values)
          .then((data) => {
            setLoading(false);
            if (data.status === 400 || data.status === 409) {
              swal(data.message, {
                icon: "error",
              });
            } else if (data.status === 200) {
              swal(data.message, {
                icon: "success",
              });
            } else {
              swal("Lo sentimos, hubo un error inesperado. Intente de nuevo.", {
                icon: "error",
              });
            }
          })
          .catch(() => {
            swal("Lo sentimos, hubo un error inesperado. Intente de nuevo.", {
              icon: "error",
            });
          });
      }
    });
  };

  // Funcionalidad para obtener los datos de catalogos desde la API
  const loadCatalogos = () => {
    getCatalogos().then((res) => {
      if (res.error) {
        setError(res.error);
      } else {
        dispatch(addCatalogos(res?.data));
        res?.data?.forEach((cat) => {
          if (cat.nacionalidad) setNacionalidadList(cat.nacionalidad);
          if (cat.actividad_economica)
            setActividadEcList(cat.actividad_economica);
          if (cat.tipo_clase) setTipoClaseList(cat.tipo_clase);
          if (cat.tipo_proyecto) setTipoProyectoList(cat.tipo_proyecto);
          if (cat.tipo_rol) setTipoRolList(cat.tipo_rol);
          if (cat.tipo_empresa) setTipoEmpresaList(cat.tipo_empresa);
        });
      }
    });
  };

  // Funcion inicializadora
  useEffect(() => {
    loadCatalogos();
    if (params.id) {
      const resul = client?.find((c) => c.cliente?.CLIE_CODIGO == params.id);
      const { cliente, detalle } = resul;
      setValues({ ...cliente, ...detalle });
    }
  }, []);

  // funcion que retorna la alerta de error
  const showAlert = () => <Alert color="danger">{error}</Alert>;

  return (
    <Fragment>
      <Modal
        isOpen={loading}
        backdrop={"static"}
        centered
        className="shadow-none text-center"
        contentClassName={"bg-transparent shadow-none border border-0"}
      >
        <Loader type="ball-pulse" />
      </Modal>

      <PageTitle
        heading="Mantenimiento de Cliente Jurídico"
        icon="lnr-user icon-gradient bg-tempting-azure"
      />

      <Container fluid>
        {error && showAlert()}

        {values && (
          <>
            <ClientInfo
              clientCode={values?.CLIE_CODIGO}
              typeClient={"JURIDICO"}
              typeIdentification={"CEDULA"}
              identification={values?.CLIE_IDENTIFICACION}
              nameClient={values?.CLIE_NOMBRE_CORRESPONDENCIA}
              className="bg-primary"
              onChange={handleChange}
            />

            <Card className="mt-4 mb-4">
              <CardBody>
                <Form>
                  <Row>
                    <Col md={4}>
                      <FormGroup row>
                        <Label for="nationality" sm={4}>
                          Nacionalidad
                        </Label>
                        <Col sm={8}>
                          {nacionalidadList && (
                            <Select
                              defaultValue={buscarNacionalidad(
                                values?.NACI_CODIGO,
                                nacionalidadList
                              )}
                              options={nacionalidadList?.map((item) => ({
                                value: item.NACI_CODIGO,
                                label: item.NACI_DESCRIPCION,
                              }))}
                              onChange={handleSelectChange("NACI_CODIGO")}
                            />
                          )}
                        </Col>
                      </FormGroup>
                    </Col>
                    <Col md={4}>
                      <FormGroup row>
                        <Label for="name" sm={4}>
                          Nombre:
                        </Label>
                        <Col sm={8}>
                          <Input
                            type="text"
                            name="name"
                            id="name"
                            value={values?.CLIE_NOMBRE}
                            onChange={handleChange("CLIE_NOMBRE")}
                          />
                        </Col>
                      </FormGroup>
                    </Col>
                    <Col md={4}>
                      <FormGroup row>
                        <Label for="state" sm={4}>
                          Estado:
                        </Label>
                        <Col sm={8}>
                          {tipoClaseList && (
                            <Select
                              defaultValue={buscarTipoClase(
                                values?.clie_tipo,
                                tipoClaseList
                              )}
                              options={tipoClaseList?.map((item) => ({
                                value: item.CLIE_TIPO,
                                label: item.DESC_TIPO,
                              }))}
                              onChange={handleSelectChange("TIDO_CODIGO")}
                            />
                          )}
                        </Col>
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col md={4}>
                      <FormGroup row>
                        <Label for="economicActivity" sm={4}>
                          Actividad Económica:
                        </Label>
                        <Col sm={8}>
                          {actividadEcList && (
                            <Select
                              defaultValue={buscarActividadEconomica(
                                values?.ACTI_CODIGO,
                                actividadEcList
                              )}
                              options={actividadEcList?.map((item) => ({
                                value: item.ACTI_CODIGO,
                                label: item.ACTI_DESCRIPCION,
                              }))}
                              onChange={handleSelectChange("ACTI_CODIGO")}
                            />
                          )}
                        </Col>
                      </FormGroup>
                    </Col>
                    <Col md={4}>
                      <FormGroup row>
                        <Label for="categoryClient" sm={4}>
                          Categoría cliente:
                        </Label>
                        <Col sm={8}>
                          {tipoProyectoList && (
                            <Select
                              defaultValue={buscarCategoriaCliente(
                                values?.CLIE_TIPO_PROYECTO,
                                tipoProyectoList
                              )}
                              options={tipoProyectoList?.map((item) => ({
                                value: item.COD_TIPO_PROYECTO,
                                label: item.DESC_TIPO_PROYECTO,
                              }))}
                              onChange={handleSelectChange(
                                "CLIE_TIPO_PROYECTO"
                              )}
                            />
                          )}
                        </Col>
                      </FormGroup>
                    </Col>
                    <Col md={4}>
                      <FormGroup row>
                        <Label for="rol" sm={4}>
                          Tipo rol:
                        </Label>
                        <Col sm={8}>
                          {tipoRolList && (
                            <Select
                              defaultValue={buscarTipoRol(
                                values?.CLIE_TIPO_ROL,
                                tipoRolList
                              )}
                              options={tipoRolList?.map((item) => ({
                                value: item.TIRO_CODIGO,
                                label: item.TIROL_DESCRIPCION,
                              }))}
                            />
                          )}
                        </Col>
                      </FormGroup>
                    </Col>
                  </Row>

                  <div className="d-flex align-items-center">
                    <div className="mx-auto">
                      <Button
                        outline
                        className="mb-2 me-2 btn-icon btn-pill"
                        color="link"
                        onClick={() => setIsOpen(!isOpen)}
                      >
                        {isOpen ? (
                          <>
                            <i className="pe-7s-angle-down btn-icon-wrapper">
                              {" "}
                            </i>
                            Ocultar información
                          </>
                        ) : (
                          <>
                            <i className="pe-7s-angle-right btn-icon-wrapper">
                              {" "}
                            </i>
                            Más Información
                          </>
                        )}
                      </Button>
                    </div>
                  </div>

                  <Row className="d-flex flex-column justify-content-center align-items-center">
                    <Col sm={6}>
                      <div className="d-flex align-items-center">
                        <div className="mx-auto">
                          <ClientMoreInfo
                            isOpen={isOpen}
                            setIsOpen={setIsOpen}
                          />
                        </div>
                      </div>
                    </Col>
                  </Row>

                  <Row className="divider"></Row>

                  <Row>
                    <Col md={4}>
                      <FormGroup row>
                        <Label for="typeCompany" sm={4}>
                          Tipo empresa:
                        </Label>
                        <Col sm={8}>
                          {tipoEmpresaList && (
                            <Select
                              defaultValue={buscarTipoEmpresa(
                                values?.TIEM_CODIGO,
                                tipoEmpresaList
                              )}
                              options={tipoEmpresaList?.map((item) => ({
                                value: item.TIEM_CODIGO,
                                label: item.TIEM_DESCRIPCION,
                              }))}
                            />
                          )}
                        </Col>
                      </FormGroup>
                    </Col>
                    <Col md={4}>
                      <FormGroup row>
                        <Label for="businessName" sm={4}>
                          Razón social:
                        </Label>
                        <Col sm={8}>
                          <Input
                            type="text"
                            name="businessName"
                            id="businessName"
                            value={values?.CLJU_RAZON_SOCIAL}
                            onChange={handleChange("CLJU_RAZON_SOCIAL")}
                          />
                        </Col>
                      </FormGroup>
                    </Col>
                    <Col md={4}>
                      <FormGroup row>
                        <Label for="advertisingName" sm={4}>
                          Nombre publicitario:
                        </Label>
                        <Col sm={8}>
                          <Input
                            type="text"
                            name="advertisingName"
                            id="advertisingName"
                            value={values?.CLJU_NOMBRE_PUBLICITARIO}
                            onChange={handleChange("CLJU_NOMBRE_PUBLICITARIO")}
                          />
                        </Col>
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col md={4}>
                      <FormGroup row>
                        <Label for="subscribedCapital" sm={4}>
                          Capital suscrito:
                        </Label>
                        <Col sm={8}>
                          <Input
                            type="number"
                            min={0}
                            name="subscribedCapital"
                            id="subscribedCapital"
                            value={values?.CLJU_CAPITAL_SUS}
                            onChange={handleChange("CLJU_CAPITAL_SUS")}
                          />
                        </Col>
                      </FormGroup>
                    </Col>
                    <Col md={4}>
                      <FormGroup row>
                        <Label for="paidCapital" sm={4}>
                          Capital pagado:
                        </Label>
                        <Col sm={8}>
                          <Input
                            type="number"
                            min={0}
                            name="paidCapital"
                            id="paidCapital"
                            value={values?.CLJU_CAPITAL_PAG}
                            onChange={handleChange("CLJU_CAPITAL_PAG")}
                          />
                        </Col>
                      </FormGroup>
                    </Col>
                    <Col md={4}>
                      <FormGroup row>
                        <Label for="reservaLegal" sm={4}>
                          Reserva legal:
                        </Label>
                        <Col sm={8}>
                          <Input
                            type="number"
                            min={0}
                            name="reservaLegal"
                            id="reservaLegal"
                            value={values?.CLJU_RESERVA_LEG}
                            onChange={handleChange("CLJU_RESERVA_LEG")}
                          />
                        </Col>
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col md={4}>
                      <FormGroup row>
                        <Label for="economicGroup" sm={4}>
                          Grupo económico:
                        </Label>
                        <Col sm={8}>
                          <Input
                            type="text"
                            name="economicGroup"
                            id="economicGroup"
                            value={values?.GREC_CODIGO}
                            onChange={handleChange("GREC_CODIGO")}
                          />
                        </Col>
                      </FormGroup>
                    </Col>
                    <Col md={5}>
                      <FormGroup row>
                        <Label for="statutesDate" sm={6}>
                          Fecha reforma estatutos:
                        </Label>
                        <Col sm={6}>
                          <Input
                            type="date"
                            name="statutesDate"
                            id="statutesDate"
                          />
                        </Col>
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row className="d-flex flex-column justify-content-center align-items-center">
                    <div className="d-flex align-items-center">
                      <div className="mx-auto">
                        <Button
                          onClick={clickSubmit}
                          color="primary"
                          className="mt-2"
                          size="lg"
                        >
                          Grabar
                        </Button>
                      </div>
                    </div>
                  </Row>
                </Form>
              </CardBody>
            </Card>
          </>
        )}
      </Container>
    </Fragment>
  );
};

export default Index;
