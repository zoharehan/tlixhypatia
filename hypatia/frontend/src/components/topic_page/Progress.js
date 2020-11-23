import React, { Component } from "react";
import { ProgressBar } from "react-bootstrap";

export class Progress extends Component {
  render() {
    return (
      <div style={{ marginBottom: 30, marginTop: 30 }}>
        <ProgressBar
          animated
          striped
          now={50}
          style={{
            height: 25,
            boxShadow: "2px 2px lightgrey",
            borderRadius: 25,
          }}
        />
      </div>
    );
  }
}
export default Progress;
