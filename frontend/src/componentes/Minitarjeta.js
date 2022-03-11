import React from 'react';
import Accordion from 'react-bootstrap/Accordion';


const Minitarjeta = ({variableHist}) => {
    return (
        <Accordion defaultActiveKey="0" flush>
            <Accordion.Item eventKey="0">
                <Accordion.Header>
                    <strong className="me-auto">{variableHist.descripcion?.toUpperCase()}</strong>
                </Accordion.Header>
                <Accordion.Body>
                    <strong className="me-auto">
                        {variableHist.valor}
                        {' '}
                        {variableHist.EGU}
                    </strong>   
                </Accordion.Body>
            </Accordion.Item>
        </Accordion>
    )
};

export default Minitarjeta;