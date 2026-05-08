import { BrowserRouter as Router, Route, Routes, useLocation } from "react-router-dom";
import store from "./store";
import { Provider } from "react-redux";
import { Helmet, HelmetProvider } from "react-helmet-async";
import AnimatedRoutes from "./Routes";

function App() {
  
  return (
    <HelmetProvider>
      <Helmet>
        <title>AIET | Portal de procesamiento de la información</title>
      </Helmet>
      <Provider store={store}>
        <Router basename="/pc-isla">
          <AnimatedRoutes />         
        </Router>
      </Provider>
    </HelmetProvider>
    );
}

export default App;
