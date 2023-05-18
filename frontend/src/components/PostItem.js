import CardHeader from "@mui/material/CardHeader";
import Avatar from "@mui/material/Avatar";
import IconButton from "@mui/material/IconButton";
import MoreVertIcon from "@mui/icons-material/MoreVert";
import CardMedia from "@mui/material/CardMedia";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
import CardActions from "@mui/material/CardActions";
import FavoriteIcon from "@mui/icons-material/Favorite";
import ShareIcon from "@mui/icons-material/Share";
import classes from "../styles/PostList.module.css";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import Collapse from "@mui/material/Collapse";
import Card from "@mui/material/Card";
import * as React from "react";
import {useState} from "react";
import {styled} from "@mui/material/styles";


const ExpandMore = styled((props) => {
  const {expand, ...other} = props;
  return <IconButton {...other} />;
})(({theme, expand}) => ({
  transform: !expand ? 'rotate(0deg)' : 'rotate(180deg)',
  marginLeft: 'auto',
  transition: theme.transitions.create('transform', {
    duration: theme.transitions.duration.shortest,
  }),
}));

const PostItem = ({post, handleOpen}) => {
  const [expanded, setExpanded] = useState(false);
  const handleExpandClick = () => {
    setExpanded(!expanded);
  };

  return (
    <Card sx={{mb: 1}}>
      <CardHeader
        avatar={<Avatar aria-label="recipe"/>}
        action={
          <IconButton aria-label="settings">
            <MoreVertIcon/>
          </IconButton>
        }
        title={post.author}
        subheader={post.created}
      />
      {post.image &&
        <CardMedia
          component="img"
          height="194"
          image={post.image}
          alt="Картинка"
          onClick={() => handleOpen(post)}
        />}

      <CardContent>
        <Typography variant="body2" color="text.secondary">
          {post.text}
        </Typography>
      </CardContent>

      <CardActions disableSpacing>
        <Typography variant="body2" color="text.secondrary">
          {post.likes}
        </Typography>
        <IconButton aria-label="add to favorites">
          <FavoriteIcon/>
        </IconButton>
        <IconButton aria-label="share">
          <ShareIcon/>
        </IconButton>
        <Typography
          color="text.secondary"
          className={classes.commentText}>
          Комментарии
        </Typography>
        <ExpandMore
          expand={expanded}
          onClick={handleExpandClick}
          aria-expanded={expanded}
          aria-label="show more"
        >
          <ExpandMoreIcon/>
        </ExpandMore>
      </CardActions>
      <Collapse in={expanded} timeout="auto" unmountOnExit>
        <CardContent>
          {post.comments.length <= 0
            ? <Typography paragraph>Комментариев нет!</Typography>
            : post.comments.map(comment =>
              <div key={comment.id} style={{marginBottom: 20}}>
                <div>Автор: {comment.author}</div>
                <div>Комментарий: {comment.text}</div>
              </div>
            )}
        </CardContent>
      </Collapse>
    </Card>
  );
};

export default PostItem;

