import React from 'react';
import {
    Nav,
    NavLink,
    Bars,
    NavMenu,
} from './navbar-menu.component';

const Navbar = () => {
    return (
        const jsonData = requiere('./')
        var opcMenu=[requiere()]
        <>
            <Nav>
                <Bars />
                
                <NavMenu>
                    <NavLink to="/Administracion" activeStyle>
                        Administracion
                    </NavLink>
                    <NavLink to="/Politicas" activeStyle>
                        Politicas
                    </NavLink>
                    <NavLink to="/Pagos" activeStyle>
                        Pagos
                    </NavLink>
                    <NavLink to="/ProcesosECRE" activeStyle>
                        Procesos especiales de credito
                    </NavLink>
                    <NavLink to="/DocumentosC" activeStyle>
                        Documentos de credito
                    </NavLink>
                    <NavLink to="/FabricaDCRE" activeStyle>
                        Fabrica de Credito
                    </NavLink>
                    <NavLink to="/MotorMensajeria" activeStyle>
                        Motor Mensajeria
                    </NavLink>
                    <NavLink to="/Consultas" activeStyle>
                        Consultas
                    </NavLink>
                    <NavLink to="/ProcesosMA" activeStyle>
                        Procesos Masivos
                    </NavLink>
                    <NavLink to="/Soporte" activeStyle>
                        Soporte
                    </NavLink>
                </NavMenu>
            </Nav>
        </>

    )
}
export default Navbar;