import 'bootstrap/dist/css/bootstrap.min.css';
import Cabecera from './componentes/Cabecera';
import Variableanalogica from './componentes/Variableanalogica';
import Variabledigital from './componentes/Variabledigital';
import axios from 'axios';
import { useState, useEffect, useRef } from 'react';
import Actualizar from './componentes/Actualizar';
import { Container, Row, Col, Tab, Tabs} from 'react-bootstrap';
import Minitarjeta from './componentes/Minitarjeta';

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
  useInterval(() => {
    // Se lee cada 1000 milisegundos osea 1 segundo los datos del servidor
    getTagsHistorian();
  }, 1000);

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
  //------ inicio
  //---------- Funcion para actualizar cada x segundos
  //https://overreacted.io/making-setinterval-declarative-with-react-hooks/
  function useInterval(callback, delay) {
    const savedCallback = useRef();
  
    // Remember the latest callback.
    useEffect(() => {
      savedCallback.current = callback;
    }, [callback]);
  
    // Set up the interval.
    useEffect(() => {
      function tick() {
        savedCallback.current();
      }
      if (delay !== null) {
        let id = setInterval(tick, delay);
        return () => clearInterval(id);
      }
    }, [delay]);
  }
  //------- fin
  return (
    <div className="App">
      <Cabecera titulo="Variables de proceso" />
      <Tabs defaultActiveKey="home" id="uncontrolled-tab-example" className="mb-3">
        <Tab eventKey="home" title="Home">
            <Container className="mt-4">
              {tagshistorian.length ? (
                <Row sd={1} md={2} lg={3}>
                  {tagshistorian.map((imagen, i) => (
                    <Col key={i} className="pb-3">
                      <Minitarjeta variableHist={imagen} />
                    </Col>
                  ))}
                </Row>
              ) : (
                <br />
              )}
            </Container>
        </Tab>
        <Tab eventKey="profile" title="Profile">
          <Actualizar eliminarValorAnterior={Actualiza1Variable}/>
          <Variableanalogica nombretag="Flujo de balanza: " valortag={AuxValor1} unidadtag=" Kg/h" />
        </Tab>
        <Tab eventKey="contact" title="Contact" disabled>
          <Variabledigital  nombretag="Estado de Planta " valortag="Funcionando" />
        </Tab>
      </Tabs>
      
      
      
      
    </div>
  );
}

export default App;
