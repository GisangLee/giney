import React from "react";
import {
  Route,
  Redirect,
  Switch,
  HashRouter as Router,
} from "react-router-dom";
import Home from "../Routes/Home";
import Account from "../Routes/Account";

export default () => (
  <Router>
    <>
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/accouts" exact component={Account} />
      </Switch>
    </>
  </Router>
);
