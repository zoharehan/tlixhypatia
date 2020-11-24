import React, { Component } from "react";
import { ProgressBar } from "react-bootstrap";

export class Progress extends Component {
  
  constructor(){
    super();
    this.state = {
      percentage:0   
      // Change this to sth in the database. Django has to have some way to pass to react. 
    }
  }

  percentageLimits = (min,value,max) => {
    return Math.min(Math.max(min,value),max);
  }

  clickMe = () => {
    
    this.setState({percentage: this.state.percentage + 25});
    const requestOptions = {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' }
      // body: JSON.stringify({ title: 'StudentName' })
    };
      fetch('/progressapi/progress/')
      .then(handleRedirect);    
}
  handleRedirect = (res)=> {
    if( res.status === 200 ){
      // redirect here
      window.location.href = '/progressapi/progress/';
    }else {
      
    // Something went wrong here
    }
  }

  render() {
    return (
      <div style={{ marginBottom: 30, marginTop: 30 }}>
        <ProgressBar striped variant="info" now={this.percentageLimits(0,this.state.percentage,100)} style={{ height: 25 }} />
        <button onClick={this.clickMe}>Next</button>
        
      </div>
    );
  }
}


export default Progress;
