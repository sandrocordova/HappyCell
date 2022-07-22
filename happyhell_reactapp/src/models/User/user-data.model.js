export class User {
  constructor(id, name, logoPicture, role, city, agency, department) {
    this.USUA_LOGIN = id;
    this.USUA_NOMBRE = name;
    this.EMPR_IMAGEN = logoPicture;
    this.TIPE_DESCRIPCION = role;
    this.ZONA_DESCRIPCION = city;
    this.AGEN_DESCRIPCION = agency;
    this.CETC_CODIGO_DESCRIPCION = department;
  }
}