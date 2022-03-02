import React from 'react';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';

const Cabecera = ({titulo}) => {
    return (
        <Navbar bg="dark" variant="dark">
            <Navbar.Brand href="#home"> {titulo} </Navbar.Brand>
            <Nav className="me-auto">
              <Nav.Link href="#proceso1">Proceso Linea 1</Nav.Link>
              <Nav.Link href="#proceso2">Proceso Linea 2</Nav.Link>
              <Nav.Link href="#proceso3">Estacion Metereologica</Nav.Link>
            </Nav>
        </Navbar>
    )
};

export default Cabecera;