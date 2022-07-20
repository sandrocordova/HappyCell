import React from 'react';
import {
    Nav,
    NavLink,
    Bars,
    NavMenu,
    NavBtn,
    NavBtnLink
} from './navbar-menu.component';

const Navbar = () => {
    return (
        <>
            <Nav>
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
                    <NavLink to="/Motor Mensajeria" activeStyle>
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