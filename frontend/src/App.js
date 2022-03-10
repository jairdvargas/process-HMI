import 'bootstrap/dist/css/bootstrap.min.css';
import Cabecera from './componentes/Cabecera';
import Variableanalogica from './componentes/Variableanalogica';
import Variabledigital from './componentes/Variabledigital';
import axios from 'axios';
import { useState, useEffect } from 'react';
import Actualizar from './componentes/Actualizar';
import { Container, Row, Col, Tab } from 'react-bootstrap';


const API_URL = 'http://127.0.0.1:5051';

const App = () => {

  const [variable, definirVariable] = useState([]);
  const [tagshistorian, definirTagshistorian] = useState([]);

  //Ejecucion de una sola vez para recuperar tags y valores de servidor
  const getTagsHistorian = async () => {
    try {
      const resultado = await axios.get(`${API_URL}/variables`);
      definirTagshistorian(resultado.data || []);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(()=> getTagsHistorian(),[]);

  //solo se ejecutara una sola vez para leer un solo tag simulado
  const getVariableInstantanea = async () => {
    try {
      const resultado = await axios.get(`${API_URL}/tag-sim/VariableHistorian`);
      definirVariable(resultado.data || []);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => getVariableInstantanea(), []);
  //console.log(variable);
  //console.log(variable.Valor);

  const AuxValor1 = variable.Valor ? variable.Valor.toPrecision(4) : 0.0000;

  //-----------Boton de actualizar valor
  const Actualiza1Variable = async (id) => {
    console.log("click detectado")
    try {
      const resultado = await axios.get(`${API_URL}/tag-sim/${id}`);
      console.log(resultado)
        definirVariable(resultado.data || []);
    } catch (error) {
      console.log(error);
    }
  };


  return (
    <div className="App">
      <Cabecera titulo="Variables de proceso" />
      <Actualizar eliminarValorAnterior={Actualiza1Variable}/>
      <Variableanalogica nombretag="Flujo de balanza: " valortag={AuxValor1} unidadtag=" Kg/h" />
      <Variabledigital  nombretag="Estado de Planta " valortag="Funcionando" />
      <Container className="mt-4">
      {tagshistorian.length ? (
          <Row sd={1} md={2} lg={3}>
            {tagshistorian.map((imagen, i) => (
              <Col key={i} className="pb-3">
                {imagen.tag}
                <Variableanalogica nombretag={imagen.descripcion} valortag={imagen.valor} unidadtag={imagen.EGU} />
              </Col>
            ))}
          </Row>
        ) : (
          <br />
        )}
      </Container>
    </div>
  );
}

export default App;
