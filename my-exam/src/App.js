import "./App.css";
import Signup from "./pages/SignUp/signup";
import NavBar from "./components/NavBar/NavBar";
import SignIn from "./pages/SignIn/SignIn";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

function App() {
  return (
    <div className="">
      <Router>
        <Switch>
          <Route exact path="/signup">
            <Signup />
          </Route>
          <Route exact path="/signin">
            <SignIn />
          </Route>
          <Route path="*">
            <SignIn />
          </Route>
        </Switch>
      </Router>
      {/* <NavBar /> */}
    </div>
  );
}

export default App;
