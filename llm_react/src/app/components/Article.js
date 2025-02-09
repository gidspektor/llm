import React from 'react';
import styles from '@/app/components/Article.module.css';

const ArticleDisplayer = ({ article }) => {
  return (
    <div className={styles.article}>
      <h2>{article.title}</h2>
      <p>{article.body}</p>
    </div>
  );
};

export default ArticleDisplayer;
