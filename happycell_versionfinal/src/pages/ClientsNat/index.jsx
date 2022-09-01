import React, { Fragment, useState, useEffect } from "react";
import Select from "react-select";
import { useParams } from "react-router-dom";
import { useSelector } from "react-redux";
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
import swal from "sweetalert";
import Loader from "react-loaders";
import PageTitle from "../../Layout/AppMain/PageTitle";
import ClientInfo from "../../components/ClientInfo";
import ClientMoreInfo from "../../components/ClientMoreInfo";
import { getCatalogos, updateClienteNatural } from "../../Api/apicall_cliente";
import {
  buscarNacionalidad,
  buscarTipoClase,
  buscarActividadEconomica,
  buscarCategoriaCliente,
  buscarTipoRol,
  buscarTipoSexo,
  buscarProfesion,
  buscarEstadoCivil,
  buscarSituLaboral,
  buscarTipoVivienda,
} from "../../utilities/searchCatalogType";
import { formatDateZone } from "../../utilities/utilities";
import { useHistory } from "react-router-dom";

const Index = () => {
  const params = useParams();
  const history = useHistory();

  const dreir = () => {
    history.push(`/`);
  };

  // statados para almacenar las listas de los catalogos
  const [tipoRolList, setTipoRolList] = useState(null);
  const [tipoProyectoList, setTipoProyectoList] = useState(null);
  const [tipoClaseList, setTipoClaseList] = useState(null);
  const [profesionList, setProfesionList] = useState(null);
  const [nacionalidadList, setNacionalidadList] = useState(null);
  const [actividadEcList, setActividadEcList] = useState(null);
  const [sexoList, setSexoList] = useState(null);
  const [viviendaList, setViviendaList] = useState(null);
  const [estadoCivilList, setEstadoCivilList] = useState(null);
  const [sitLaboralList, setSitLaboralList] = useState(null);
  // estados de utilidad
  const [isOpen, setIsOpen] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(false);
  // estado para guardar los datos del formulario
  const [values, setValues] = useState(null);
  /**
   * Estado para almacenar los datos del cliente
   */
  const client = useSelector((state) => state.client);

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
        updateClienteNatural(client.CLIE_CODIGO, values)
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
        res?.data?.forEach((cat) => {
          if (cat.profesion) setProfesionList(cat.profesion);
          if (cat.nacionalidad) setNacionalidadList(cat.nacionalidad);
          if (cat.actividad_economica)
            setActividadEcList(cat.actividad_economica);
          if (cat.sexo) setSexoList(cat.sexo);
          if (cat.vivienda) setViviendaList(cat.vivienda);
          if (cat.estado_civil) setEstadoCivilList(cat.estado_civil);
          if (cat.situacion_laboral) setSitLaboralList(cat.situacion_laboral);
          if (cat.tipo_clase) setTipoClaseList(cat.tipo_clase);
          if (cat.tipo_proyecto) setTipoProyectoList(cat.tipo_proyecto);
          if (cat.tipo_rol) setTipoRolList(cat.tipo_rol);
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
        heading="Mantenimiento de Cliente Natural"
        icon="lnr-user icon-gradient bg-tempting-azure"
      />

      <Container fluid>
        {error && showAlert()}

        {values && (
          <>
            <ClientInfo
              clientCode={values?.CLIE_CODIGO}
              typeClient={"NATURAL"}
              typeIdentification={"CEDULA"}
              identification={values?.CLIE_IDENTIFICACION}
              nameClient={values?.CLIE_NOMBRE_CORRESPONDENCIA}
              className="bg-primary"
              onChange={handleChange}
            />

            <div className="card no-shadow rm-border bg-transparent widget-chart text-start mb-1">
              <Button onClick={dreir}>Direcciones</Button>
            </div>

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
                        <Label for="category" sm={4}>
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
                    <Col md={3}>
                      <FormGroup row>
                        <Label for="firstName" sm={4}>
                          Primer nombre:
                        </Label>
                        <Col sm={8}>
                          <Input
                            type="text"
                            name="firstName"
                            id="firstName"
                            value={values?.CLNA_NOMBRE1}
                            onChange={handleChange("CLNA_NOMBRE1")}
                          />
                        </Col>
                      </FormGroup>
                    </Col>
                    <Col md={3}>
                      <FormGroup row>
                        <Label for="secondName" sm={4}>
                          Segundo nombre:
                        </Label>
                        <Col sm={8}>
                          <Input
                            type="text"
                            name="secondName"
                            id="secondName"
                            value={values?.CLNA_NOMBRE2}
                            onChange={handleChange("CLNA_NOMBRE2")}
                          />
                        </Col>
                      </FormGroup>
                    </Col>
                    <Col md={3}>
                      <FormGroup row>
                        <Label for="firtsName" sm={4}>
                          Primer apellido:
                        </Label>
                        <Col sm={8}>
                          <Input
                            type="text"
                            name="firtsName"
                            id="firtsName"
                            value={values?.CLNA_APELLIDO1}
                            onChange={handleChange("CLNA_APELLIDO1")}
                          />
                        </Col>
                      </FormGroup>
                    </Col>
                    <Col md={3}>
                      <FormGroup row>
                        <Label for="secondSurname" sm={4}>
                          Segundo apellido:
                        </Label>
                        <Col sm={8}>
                          <Input
                            type="text"
                            name="secondSurname"
                            id="secondSurname"
                            value={values?.CLNA_APELLIDO2}
                            onChange={handleChange("CLNA_APELLIDO2")}
                          />
                        </Col>
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col md={3}>
                      <FormGroup row>
                        <Label for="sex" sm={4}>
                          Sexo:
                        </Label>
                        <Col sm={8}>
                          {sexoList && (
                            <Select
                              defaultValue={buscarTipoSexo(
                                values?.SEXO_CODIGO,
                                sexoList
                              )}
                              options={sexoList?.map((item) => ({
                                value: item.SEXO_CODIGO,
                                label: item.SEXO_DESCRIPCION,
                              }))}
                              onChange={handleSelectChange("SEXO_CODIGO")}
                            />
                          )}
                        </Col>
                      </FormGroup>
                    </Col>
                    <Col md={3}>
                      <FormGroup row>
                        <Label for="profession" sm={4}>
                          Profesion:
                        </Label>
                        <Col sm={8}>
                          {profesionList && (
                            <Select
                              defaultValue={buscarProfesion(
                                values?.PROF_CODIGO,
                                profesionList
                              )}
                              options={profesionList?.map((item) => ({
                                value: item.PROF_CODIGO,
                                label: item.PROF_DESCRIPCION,
                              }))}
                              onChange={handleSelectChange("PROF_CODIGO")}
                            />
                          )}
                        </Col>
                      </FormGroup>
                    </Col>
                    <Col md={3}>
                      <FormGroup row>
                        <Label for="maritalStatus" sm={4}>
                          Estado civil:
                        </Label>
                        <Col sm={8}>
                          {estadoCivilList && (
                            <Select
                              defaultValue={buscarEstadoCivil(
                                values?.ESCI_CODIGO,
                                estadoCivilList
                              )}
                              options={estadoCivilList?.map((item) => ({
                                value: item.ESCI_CODIGO,
                                label: item.ESCI_DESCRIPCION,
                              }))}
                              onChange={handleSelectChange("ESCI_CODIGO")}
                            />
                          )}
                        </Col>
                      </FormGroup>
                    </Col>
                    <Col md={3}>
                      <FormGroup row>
                        <Label for="employmentSituation" sm={4}>
                          Situación laboral:
                        </Label>
                        <Col sm={8}>
                          {sitLaboralList && (
                            <Select
                              defaultValue={buscarSituLaboral(
                                values?.CLIE_SITUACION_LABORAL,
                                sitLaboralList
                              )}
                              options={sitLaboralList?.map((item) => ({
                                value: item.SITL_CODIGO,
                                label: item.SITL_DESCRIPCION,
                              }))}
                              onChange={handleSelectChange(
                                "CLIE_SITUACION_LABORAL"
                              )}
                            />
                          )}
                        </Col>
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col md={3}>
                      <FormGroup row>
                        <Label for="typeHousing" sm={4}>
                          Tipo de vivienda:
                        </Label>
                        <Col sm={8}>
                          {viviendaList && (
                            <Select
                              defaultValue={buscarTipoVivienda(
                                values?.CLIE_TIPO_VIVIENDA,
                                viviendaList
                              )}
                              options={viviendaList?.map((item) => ({
                                value: item.VIVI_CODIGO,
                                label: item.VIVI_DESCRIPCION,
                              }))}
                              onChange={handleSelectChange(
                                "CLIE_TIPO_VIVIENDA"
                              )}
                            />
                          )}
                        </Col>
                      </FormGroup>
                    </Col>
                    <Col md={3}>
                      <FormGroup row>
                        <Label for="placeBirth" sm={4}>
                          Lugar de nacimiento:
                        </Label>
                        <Col sm={8}>
                          <Input
                            type="text"
                            name="placeBirth"
                            id="placeBirth"
                            value={values?.CLNA_LUGAR_NACIMIENTO}
                            onChange={handleChange("CLNA_LUGAR_NACIMIENTO")}
                          />
                        </Col>
                      </FormGroup>
                    </Col>
                    <Col md={3}>
                      <FormGroup row>
                        <Label for="numberLoads" sm={4}>
                          Número de cargas:
                        </Label>
                        <Col sm={8}>
                          <Input
                            type="number"
                            name="numberLoads"
                            id="numberLoads"
                            value={values?.CLNA_NUM_CARGAS}
                            onChange={handleChange("CLNA_NUM_CARGAS")}
                            min={0}
                          />
                        </Col>
                      </FormGroup>
                    </Col>
                    <Col md={3}>
                      <FormGroup row>
                        <Label for="dateBirth" sm={4}>
                          Fecha nacimiento:
                        </Label>
                        <Col sm={8}>
                          <Input
                            type="date"
                            name="dateBirth"
                            id="dateBirth"
                            defaultValue={formatDateZone(
                              values?.CLNA_FECHA_NACIMIENTO
                            )}
                            onChange={handleChange("CLNA_FECHA_NACIMIENTO")}
                          />
                        </Col>
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col md={3}>
                      <FormGroup row>
                        <Label for="workCompany" sm={4}>
                          Empresa trabajo:
                        </Label>
                        <Col sm={8}>
                          <Input
                            type="text"
                            name="workCompany"
                            id="workCompany"
                            value={values?.CLNA_EMPRESA_TRABAJA}
                            onChange={handleChange("CLNA_EMPRESA_TRABAJA")}
                          />
                        </Col>
                      </FormGroup>
                    </Col>
                    <Col md={3}>
                      <FormGroup row>
                        <Label for="passportExp" sm={4}>
                          Exp. pasaporte:
                        </Label>
                        <Col sm={8}>
                          <Input
                            type="date"
                            name="passportExp"
                            id="passportExp"
                            defaultValue={formatDateZone(
                              values?.CLNA_EXPIRA_PASAPORTE
                            )}
                            onChange={handleChange("CLNA_EXPIRA_PASAPORTE")}
                          />
                        </Col>
                      </FormGroup>
                    </Col>
                    <Col md={3}>
                      <FormGroup row>
                        <Label for="homeRevenues" sm={4}>
                          Inicio ingresos:
                        </Label>
                        <Col sm={8}>
                          <Input
                            type="date"
                            name="homeRevenues"
                            id="homeRevenues"
                            defaultValue={formatDateZone(
                              values?.CLNA_INICIO_INGRESOS
                            )}
                            onChange={handleChange("CLNA_INICIO_INGRESOS")}
                          />
                        </Col>
                      </FormGroup>
                    </Col>
                    <Col md={3}>
                      <FormGroup row>
                        <Label for="startResidency" sm={4}>
                          Inicio recidencia:
                        </Label>
                        <Col sm={8}>
                          <Input
                            type="date"
                            name="startResidency"
                            id="startResidency"
                            defaultValue={formatDateZone(
                              values?.CLNA_INICIO_RESIDENCIA
                            )}
                            onChange={handleChange("CLNA_INICIO_RESIDENCIA")}
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
