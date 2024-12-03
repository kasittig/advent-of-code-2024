import React from "react";
import Grid from "@mui/material/Grid2";
import DayCard from "./Day";
import "./App.css";

function App() {
  const components = [];
  for (let i = 1; i <= 25; i++) {
    components.push(
      <Grid key={i}>
        <DayCard day={i} />
      </Grid>,
    );
  }
  return (
    <div className="App">
      <header className="App-header">
        <Grid
          container
          spacing={{ xs: 2, md: 3 }}
          columns={{ xs: 4, sm: 8, md: 12 }}
        >
          {components}
        </Grid>
      </header>
    </div>
  );
}

export default App;
