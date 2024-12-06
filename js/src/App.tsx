import React from "react";
import Grid from "@mui/material/Grid2";
import DayCard from "./Day";
import "./App.css";
import Container from "@mui/material/Container";
import { Paper } from "@mui/material";

import { styled } from "@mui/material/styles";

const StyledPaper = styled(Paper)(({ theme }) => ({
  padding: theme.spacing(2),
  ...theme.typography.body2,
  textAlign: "center",
  alignItems: "center",
  display: "flex",
}));

function App() {
  const components = [];
  for (let i = 0; i < 25; i++) {
    components.push(
      <Grid key={i} size={{ xs: 1, sm: 1.2, md: 2.4 }}>
        <DayCard day={i + 1} />
      </Grid>,
    );
  }
  return (
    <div className="App">
      <header className="App-header">
        <Container sx={{ margin: 4 }}>
          <StyledPaper>
            <Grid
              container
              spacing={{ xs: 2, md: 3 }}
              columns={{ xs: 3, sm: 6, md: 12 }}
            >
              {components}
            </Grid>
          </StyledPaper>
        </Container>
      </header>
    </div>
  );
}

export default App;
