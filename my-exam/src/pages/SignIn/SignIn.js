import React, { useState } from "react";
import "./signin.css";
import { Link } from "react-router-dom";

const SignIn = () => {
  const [email, setEmail] = useState("");
  const [pass, setPass] = useState("");
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(email, pass);
    setEmail("");
    setPass("");
  };
  return (
    <div>
      <section className="container">
        <article className="leftSide">
          <h3>ExamGen</h3>
          <div className="subContainer">
            <div className="para-center">
              <h2>Hello, Friends</h2>
              <p>
                lorem IpIpsum proident Laboris voluptate Lorem laborum minim
                culpa enim consectetur minim veniam. Qui Lorem sunt occaecat do
                tempor velit dolor ut ex anim sint dolore
              </p>
              <button className="btn" type="submit">
                <Link to="/signup">Sign Up</Link>
              </button>
            </div>
          </div>
        </article>

        <article className="form">
          <h3>Sign in</h3>

          <form className="form-action" onSubmit={handleSubmit}>
            <section className="">
              <label htmlFor="email">Email Address</label>
              <input
                type="text"
                id="email"
                name="email"
                onChange={(e) => setEmail(e.target.value)}
                className="form-item"
                value={email}
              />
            </section>
            <section className="">
              <label htmlFor="password">Password</label>
              <input
                type="password"
                id="password"
                name="password"
                onChange={(e) => setPass(e.target.value)}
                className="form-item"
                value={pass}
              />
            </section>
            <button className="btn-sign" type="submit">
              Sign In
            </button>
          </form>
          <a href="https://www.github.com" className="btn-forgot">
            Forgot pasword? Reset Here
          </a>
        </article>
      </section>
    </div>
  );
};

export default SignIn;
