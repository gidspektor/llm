'use client';

import { useState } from 'react';
import { createArticle } from '@/app/services/apiService';
import styles from '@/app/create/Create.module.css';

export default function CreatePage() {
  const [articleText, setArticleText] = useState('');
  const [createdArticle, setCreatedArticle] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    try {
      const result = await createArticle(articleText);
      setCreatedArticle(result);
    } catch (error) {
      console.error('Failed to create article:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Create Article</h1>
      <p className={styles.description}>
        Use me to help you create an article, add as much or
        as little information as you would like e.g. make me
        an article about tariffs being imposed on the eu by the us.
      </p>
      <form onSubmit={handleSubmit} className={styles.form}>
        <textarea
          value={articleText}
          onChange={(e) => setArticleText(e.target.value)}
          placeholder="Write your article here..."
          className={styles.textarea}
        />
        <button type="submit" className={styles.button} disabled={loading}>
          {loading ? 'Loading...' : 'Submit'}
        </button>
      </form>

      {loading && <div className={styles.loading}>Loading...</div>}

      {createdArticle && (
        <div className={styles.article}>
          <h2>{createdArticle.title}</h2>
          <p>{createdArticle.body}</p>
        </div>
      )}
    </div>
  );
}