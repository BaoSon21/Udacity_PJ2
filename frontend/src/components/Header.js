import React, { Component } from "react";
import { Link, Router } from "react-router-dom";
import "../stylesheets/Header.css";

class Header extends Component {
  render() {
    return (
      <div className="App-header">
        <Link to="/">Udacitrivia</Link>
        <Link to="/">List</Link>
        <Link to="/add">Add</Link>
        <Link to="/play">Play</Link>
      </div>
    );
  }
}

export default Header;
