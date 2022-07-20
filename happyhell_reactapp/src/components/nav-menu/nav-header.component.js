import './../../styled-components/nav-bar/nav-bar.css';
import logo from './../../assets/images/logo.jpg'
import { useState, useEffect } from 'react';
import { User } from '../../models/User/user-data.model';

const NavBarHeader = () => {
    const [user, setUser] = useState(new User);

    useEffect(() => {
        setUser({
            id: 1, 
            name: "Edison", 
            lastname: "Saavedraa", 
            picture: "https://i.pinimg.com/originals/29/47/9b/29479ba0435741580ca9f4a467be6207.png",
            role: "Admin",
            city: "Quito, Ecuador",
            agency: "0001 cam internacional km 23"
        });
      });

    return (
        <div className='nav-header'>
            <div className='logo'>
                <img className='image' src={logo} alt='Happy cel logo'/>
            </div>
            <div className='title'>
                <span>SISTEMA DE ADMINISTRACIÓN DE CARTERA</span>
            </div>
            <div className='location'>
                <span>Ciudad: {user.city} </span>
                <span>Agencia: {user.agency}</span>
            </div>
            <div className='userSession'>
                <div className='userPicture'>
                    <img className='image' src={user.picture} alt='User profile picture'/>
                </div>
                <br/>
                <div className='userData'>
                    <span>{user.name} {user.lastname}</span>
                    <span className='userRole'>{user.role}</span>
                </div>
            </div>
        </div>
    )
}

export default NavBarHeader;