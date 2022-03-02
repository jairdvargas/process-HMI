import 'bootstrap/dist/css/bootstrap.min.css';
import Cabecera from './componentes/Cabecera';
import Variableanalogica from './componentes/Variableanalogica';
import Variabledigital from './componentes/Variabledigital';

const App = () => {
  return (
    <div className="App">
      <Cabecera titulo="Variables de proceso" />
      <Variableanalogica nombretag="Flujo de balanza" valortag="86" unidadtag="Kg/h" />
      <Variableanalogica  nombretag="Temperatura tolva extractor" valortag="64" unidadtag="°C" />
      <Variabledigital  nombretag="Estado del RD1" valortag="ON" />
    </div>
  );
}

export default App;
