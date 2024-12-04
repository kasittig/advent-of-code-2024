import * as React from "react";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardActions from "@mui/material/CardActions";
import Typography from "@mui/material/Typography";
import { red, green } from "@mui/material/colors";
import StarIcon from "@mui/icons-material/Star";
import { IconButton } from "@mui/material";
import Grid from "@mui/material/Grid2";

interface DayCardProps {
  day: number;
}

function getCardColor(day: number) {
  if (day % 2 === 0) {
    return red[500];
  } else {
    return green[500];
  }
}

const today = new Date();

function getCardIcon(day: number) {
  const buttonDate = new Date(`2024-12-${day}`);
  const aoc_url = `https://adventofcode.com/2024/day/${day}`;
  if (buttonDate <= today) {
    return (
      <IconButton aria-label="Advent of Code puzzle" href={aoc_url}>
        <StarIcon />
      </IconButton>
    );
  } else {
    return (
      <IconButton>
        <StarIcon color="disabled" />
      </IconButton>
    );
  }
}

function DayCard(props: DayCardProps) {
  const color = getCardColor(props.day);
  return (
    <Card sx={{ borderRadius: "16px", bgcolor: color }} variant="outlined">
      <CardContent>
        <Grid display="flex" justifyContent="center" alignItems="center">
          <Typography variant="h3" color="#FFFFFF" fontFamily="monospace">
            {props.day}
          </Typography>
        </Grid>
      </CardContent>
      <CardActions sx={{ justifyContent: "right" }}>
        {getCardIcon(props.day)}
      </CardActions>
    </Card>
  );
}

export default DayCard;
