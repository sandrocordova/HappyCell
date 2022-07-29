import React, { useEffect, useState } from 'react';
import './styles.css';
import Row from './Row';



export default class Rows extends React.Component {
    constructor() {
        super()
    }
    render() {
        return (
            <div class = "contenTable">
                <table id="customers">
                    <Row/>
                </table>
            </div>
        )
    }
};
