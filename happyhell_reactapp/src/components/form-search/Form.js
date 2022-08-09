import React, { useEffect, useState } from 'react';
import './styles.css';
import Row from './Row';



export default class Rows extends React.Component {
  constructor() {
    super()
  }
  render() {
    return (
      <div>
        <form method="get" action="javascript: void(0);" id="login-form" class="login-form" autocomplete="off" role="main">
          <div>
            <div>
              <label>
                <input class="text" name="email" placeholder="Nombres" tabindex="1" required />
                <span class="required">Nombres</span>
              </label>
              <label>
                <input class="text" name="email" placeholder="Apellidos" tabindex="1" required />
                <span class="required">Apellidos</span>
              </label>
            </div>
            <label>
              <input class="text" type="email" name="email" placeholder="Nombres" tabindex="1" required />
              <span class="required">Correo</span>
            </label>
            <label>
              <input class="text" name="email" placeholder="Dirección" tabindex="1" required />
              <span class="required">Dirección</span>
            </label>
          </div>
          <input type="submit" value="Guardar" />
        </form>
      </div>
    )
  }
};
