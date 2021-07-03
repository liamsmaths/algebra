import React from "react";
import "./App.css";
import LoginPage from "./Page/Login";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import Home from "./Page/Home";
import PracticeBoard from "./Page/PracticeBoard";

function App() {
  return (
    <React.Fragment>
      <BrowserRouter>
        <Route path="/" exact>
          <LoginPage />
        </Route>
        <Route path="/home" exact>
          <Home />
        </Route>
        <Route path="/practiceboard" exact>
          <PracticeBoard />
        </Route>
      </BrowserRouter>
    </React.Fragment>
  );
}

export default App;
