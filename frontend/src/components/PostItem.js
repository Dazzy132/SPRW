import React from 'react';

const PostItem = ({data}) => {
  return (
    <div>
      <div>Автор: {data.author}</div>
      <div>Текст: {data.text}</div>
    </div>
  );
};

export default PostItem;