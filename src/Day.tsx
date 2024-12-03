import * as React from "react";
import Card from "@mui/material/Card";
import { styled } from "@mui/material/styles";
import CardContent from "@mui/material/CardContent";
import CardActions from "@mui/material/CardActions";
import Collapse from "@mui/material/Collapse";
import IconButton, { IconButtonProps } from "@mui/material/IconButton";
import Typography from "@mui/material/Typography";
import { red, green } from "@mui/material/colors";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import Link from "@mui/material/Link";

interface ExpandMoreProps extends IconButtonProps {
  expand: boolean;
}

const ExpandMore = styled((props: ExpandMoreProps) => {
  const { expand, ...other } = props;
  return <IconButton {...other} />;
})(({ theme }) => ({
  marginLeft: "auto",
  transition: theme.transitions.create("transform", {
    duration: theme.transitions.duration.shortest,
  }),
  variants: [
    {
      props: ({ expand }) => !expand,
      style: {
        transform: "rotate(0deg)",
      },
    },
    {
      props: ({ expand }) => !!expand,
      style: {
        transform: "rotate(180deg)",
      },
    },
  ],
}));

interface DayCardProps {
  day: number;
}

function DayCardText(props: DayCardProps) {
  let color;
  if (props.day % 2 === 0) {
    color = red[500];
  } else {
    color = green[500];
  }
  return (
    <Typography variant="h3" color={color}>
      {props.day}
    </Typography>
  );
}

function DayCard(props: DayCardProps) {
  const [expanded, setExpanded] = React.useState(false);

  const handleExpandClick = () => {
    setExpanded(!expanded);
  };
  const aoc_link = `https://adventofcode.com/2024/day/${props.day}`;
  return (
    <Card sx={{ maxWidth: 345, minWidth: 150, minHeight: 150, maxHeight: 345 }}>
      <CardContent>
        <DayCardText day={props.day} />
      </CardContent>
      <CardActions disableSpacing>
        <ExpandMore
          expand={expanded}
          onClick={handleExpandClick}
          aria-expanded={expanded}
          aria-label="show link"
        >
          <ExpandMoreIcon />
        </ExpandMore>
      </CardActions>
      <Collapse in={expanded} timeout="auto" unmountOnExit>
        <CardContent>
          <Link href={aoc_link} variant={"caption"}>
            Advent of Code Day {props.day}
          </Link>
        </CardContent>
      </Collapse>
    </Card>
  );
}

export default DayCard;
