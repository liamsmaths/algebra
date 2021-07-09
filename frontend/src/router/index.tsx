import React from "react";
import { Redirect, Route, Switch, withRouter } from "react-router";
import moment from "moment";
import LoginPage from "../Page/Login";
import Home from "../Page/Home";
import PracticeBoard from "../Page/PracticeBoard";
function Routes() {
  return (
    <Switch>
      <Route exact path="/" component={LoginPage} />
      <PrivateRoute exact path="/home">
        <Home />
      </PrivateRoute>
      <PrivateRoute path="/practiceboard" exact>
        <PracticeBoard />
      </PrivateRoute>
    </Switch>
  );
}

function auth() {
  const token: any = localStorage.getItem("token");
  if (token) {
    return true;
  }
  return false;
}

function PrivateRoute({ children, ...rest }: any) {
  return (
    <Route
      {...rest}
      render={({ location }) =>
        auth() ? (
          children
        ) : (
          <Redirect
            to={{
              pathname: "/",
              state: { from: location },
            }}
          />
        )
      }
    />
  );
}

export default withRouter(Routes);
