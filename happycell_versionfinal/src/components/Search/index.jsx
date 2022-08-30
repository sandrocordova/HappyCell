import React, { useRef, useState } from "react";

import {Button, Input } from "reactstrap";

import { searchClient } from "../../Api/apicall_search";

const Index = ({ pagina, texto, setTexto, result,setPostResult }) => {
    

    async function postData() {


        try {
            const data = await searchClient(texto,pagina);

            setPostResult(data);

        } catch (err) {

            
        }
    }



    return (
        <div className="card">
            <div className="card-body">
                <div className="form-group">
                    <Input type="search" className="form-control" onChange={(e) => setTexto(e.target.value)} placeholder="Ingrese cedula o nombre" />
                </div>
                <br/>
                <Button className="info" onClick={postData}>Buscar</Button>
          
                {/*{*/}
                {/*    postResult && <div className="alert alert-secondary mt-2" role="alert"><pre>{postResult}</pre></div>*/}

                {/*}*/}
            </div>
        </div>
    );
}
export default Index;