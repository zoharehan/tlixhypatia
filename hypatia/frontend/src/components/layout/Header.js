import React, { Component } from "react";

export class Header extends Component {
  render() {
    return (
      <nav
        className="navbar navbar-expand-sm navbar-light "
        style={{ backgroundColor: "#e3f2fd" }}
      >
        <a class="navbar-brand" href="#">
          <img
            src={
              "https://media-exp1.licdn.com/dms/image/C560BAQF52G6bbpxtXw/company-logo_200_200/0?e=1614211200&v=beta&t=hFVLYANyVQxNIi8iq295kaFq6e_7W0O52Jzkp7abmWg"
            }
            style={{
              width: 25,
              height: 25,
              marginLeft: "10px",
              marginRight: "10px",
            }}
            stclassName="img-responsive"
          />
          Hypatia Student Summary
        </a>
        <button
          className="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>

        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav mr-auto"></ul>
        </div>
      </nav>
    );
  }
}

export default Header;
