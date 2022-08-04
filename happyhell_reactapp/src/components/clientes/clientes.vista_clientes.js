import './styles_clientes.css'
import { Link } from 'react-router-dom';

const Clientesvista_clientes = () => {


    return (
        <div>
            <div className="opcionesCuadradas">
                <div className="headerClientes">
                    <Link to="/clientes">
                        <button className="buttonIcon" title="Clientes" size="large" variant="contained" alt="Clientes">

                          
                                Clientes
                                <img className="imgIcon" src="https://cdn-icons.flaticon.com/png/128/3936/premium/3936751.png?token=exp=1659593203~hmac=4b7dd15d13b93caf41c2566c56231078" alt="Clientes" />
                                
                           
                        </button>
                    </Link>
                </div>
                <table striped bordered hover variant="dark">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>First Name</th>
                            <th>Last Name</th>
                            <th>Username</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>1</td>
                            <td>Mark</td>
                            <td>Otto</td>
                            <td>@mdo</td>
                        </tr>
                        <tr>
                            <td>2</td>
                            <td>Jacob</td>
                            <td>Thornton</td>
                            <td>@fat</td>
                        </tr>
                        <tr>
                            <td>3</td>
                            <td colSpan={2}>Larry the Bird</td>
                            <td>@twitter</td>
                        </tr>
                    </tbody>
                </table>

               


            </div>

        </div>

    )
};
export default Clientesvista_clientes;