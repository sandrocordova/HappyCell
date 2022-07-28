import Dropdown from "./Dropdown";

const MenuItems = ({ opcs }) => {
    return (
        <li className="menu-items">
            {
                opcs ? (
                    <>
                        <button type="button" aria-haspopup="menu">
                            {opcs.vent_descripcion}{" "}
                        </button>
                        <Dropdown submenus={opcs.vent_descripcion} />
                    </>
                ) : (
                    <a href="/#">{opcs.opme_descripcion}</a>
                )}
        </li>
    );
};

export default MenuItems;