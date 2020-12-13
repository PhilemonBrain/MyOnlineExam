import React, { useState } from "react";
import "./signup.css";
import { Link } from "react-router-dom";

const Signup = () => {
  const [details, setDetails] = useState({
    userName: "",
    email: "",
    lastName: "",
    firstName: "",
    location: "",
    examNumber: "",
    password: "",
    confirmPass: "",
    abtMe: "",
  });
  const handleChange = (e) => {
    const name = e.target.name;
    const value = e.target.value;
    const newDetail = { ...details, [name]: value };
    setDetails(newDetail);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (
      details.userName &&
      details.lastName &&
      details.email &&
      details.examNumber &&
      details.password
    ) {
      console.log(details);
      setDetails({
        userName: "",
        email: "",
        lastName: "",
        firstName: "",
        location: "Lagos",
        examNumber: "",
        password: "",
        confirmPass: "",
        abtMe: "",
      });
    } else {
      alert("Please fill all details");
    }
  };
  return (
    <div>
      <section className="container">
        <article className="leftSide">
          <h3>ExamGen</h3>
          <div className="subContainer">
            <div className="para-center">
              <h2>Welcome Onboard</h2>
              <p>
                lorem IpIpsum proident Laboris voluptate Lorem laborum minim
                culpa enim consectetur minim veniam
              </p>
              <button className="btn" type="submit">
                <Link to="/signin">Sign In</Link>
              </button>
            </div>
          </div>
        </article>

        <article className="rightside">
          <h3>Sign Up</h3>
          <div className="forms">
            <form className="form-group" onSubmit={handleSubmit}>
              <div className="form-guide">
                <section className="">
                  <label htmlFor="userName">User Name</label>
                  <input
                    type="text"
                    id="userName"
                    name="userName"
                    onChange={handleChange}
                    className="form-item"
                  />
                </section>
                <section className="">
                  <label htmlFor="email">Email Address</label>
                  <input
                    type="text"
                    id="email"
                    name="email"
                    onChange={handleChange}
                    className="form-item"
                  />
                </section>
                <section className="">
                  <label htmlFor="lastName">Last Name</label>
                  <input
                    type="text"
                    id="lastName"
                    name="lastName"
                    onChange={handleChange}
                    className="form-item"
                  />
                </section>
                <section className="">
                  <label htmlFor="email">First Name</label>
                  <input
                    type="text"
                    id="firstName"
                    name="firstName"
                    onChange={handleChange}
                    className="form-item"
                  />
                </section>
                <section className="">
                  <label htmlFor="location">Location</label>
                  <select
                    id="location"
                    name="location"
                    onChange={handleChange}
                    className="form-item"
                  >
                    <option>Lagos</option>
                    <option>Abuja</option>
                    <option>Akure</option>
                    <option>Delta</option>
                    <option>Edo</option>
                  </select>
                </section>
                <section className="">
                  <label htmlFor="examNumber">Exam number</label>
                  <input
                    type="number"
                    id="examNumber"
                    name="examNumber"
                    onChange={handleChange}
                    className="form-item"
                  />
                </section>
                <section className="">
                  <label htmlFor="email">Password</label>
                  <input
                    type="password"
                    id="password"
                    name="password"
                    onChange={handleChange}
                    className="form-item"
                  />
                </section>
                <section className="">
                  <label htmlFor="confirmPass">Confirm Password</label>
                  <input
                    type="password"
                    id="confirmPass"
                    name="confirmPass"
                    onChange={handleChange}
                    className="form-item"
                  />
                </section>
                <section className="">
                  <label htmlFor="abtMe">About Me</label>
                  <textarea
                    type="textbox"
                    id="abtMe"
                    name="abtMe"
                    onChange={handleChange}
                    className="form-item"
                  />
                </section>
              </div>
              <button className="btn-sign" type="submit">
                Sign Up
              </button>
            </form>
          </div>
        </article>
      </section>
    </div>
  );
};

export default Signup;
