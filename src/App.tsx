import React from "react";
import Grid from "@mui/material/Grid2";
import DayCard from "./Day";
import "./App.css";
import Container from "@mui/material/Container";

function App() {
  const components = [];
  for (let i = 0; i < 25; i++) {
    components.push(
      <Grid key={i} size={{ xs: 1, sm: 1, md: 2 }}>
        <DayCard day={i + 1} />
      </Grid>,
    );
  }
  return (
    <div className="App">
      <header className="App-header">
        <Container>
          <Grid
            container
            spacing={{ xs: 2, md: 3 }}
            columns={{ xs: 4, sm: 7, md: 11 }}
          >
            {components}
          </Grid>
        </Container>
      </header>
    </div>
  );
}

export default App;
