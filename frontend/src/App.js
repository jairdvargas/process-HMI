import 'bootstrap/dist/css/bootstrap.min.css';
import Cabecera from './componentes/Cabecera';
import Variableanalogica from './componentes/Variableanalogica';
import Variabledigital from './componentes/Variabledigital';
import axios from 'axios';
import { useState, useEffect } from 'react';

const API_URL = 'http://127.0.0.1:5051';

const App = () => {

  const [variable, definirVariable] = useState([]);

  //solo se ejecutara una sola vez
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


  return (
    <div className="App">
      <Cabecera titulo="Variables de proceso" />
      <Variableanalogica nombretag="Variable Simulacion: " valortag={AuxValor1} unidadtag=" PSI" />
      <Variableanalogica nombretag="Flujo de balanza: " valortag="86" unidadtag=" Kg/h" />
      <Variableanalogica  nombretag="Temperatura tolva extractor: " valortag="64" unidadtag=" °C" />
      <Variabledigital  nombretag="Estado del RD1 " valortag="ON" />
    </div>
  );
}

export default App;
