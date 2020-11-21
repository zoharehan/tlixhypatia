import React, { Component } from "react";
import { ProgressBar } from "react-bootstrap";

export class Progress extends Component {
  render() {
    return (
      <div style={{ marginBottom: 30, marginTop: 30 }}>
        <ProgressBar striped variant="info" now={50} style={{ height: 25 }} />
      </div>
    );
  }
}
export default Progress;
