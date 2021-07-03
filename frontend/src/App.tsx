import React from "react";
import "./App.css";
import LoginPage from "./Page/Login";
import { BrowserRouter, Route, Link } from "react-router-dom";
import Home from "./Page/Home";

function App() {
  return (
    <React.Fragment>
      <BrowserRouter>
        <Route path="/home" exact>
          <Home />
        </Route>
        <LoginPage />
      </BrowserRouter>
    </React.Fragment>
  );
}

export default App;
