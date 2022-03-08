import React from 'react';
import { Form, Button } from 'react-bootstrap';

const Actualizar = ({ manejadorSubmit }) => {
    return (
        <Form onSubmit={manejadorSubmit}>
            <Form.Group
                className="mb-3"
                controlId="formHorizontalEmail"
            >
            
            <Button variant="primary" type="submit">
                    {' '}
                    Buscar
            </Button>
                
              </Form.Group>
        </Form>
          
        
      
    );
  };
  
  export default Actualizar;
  