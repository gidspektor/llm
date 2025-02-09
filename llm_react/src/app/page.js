'use client';

import { useEffect, useState } from 'react';
import { fetchArticles, searchArticle } from '@/app/services/apiService';
import ArticleDisplayer from '@/app/components/Article';
import styles from './HomePage.module.css';

export default function HomePage() {
  const [articles, setArticles] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResult, setSearchResult] = useState(null);

  useEffect(() => {
    const getArticles = async () => {
      try {
        setLoadingHeadlines(true);
        const data = await fetchArticles();
        setArticles(data['articles']);
        setLoadingHeadlines(false);
      } catch (error) {
        console.error('Failed to fetch articles:', error);
      }
    };

    getArticles();
  }, []);

  const handleSearch = async (event) => {
    event.preventDefault();
    try {
      const result = await searchArticle(searchQuery);
      setSearchResult(result);
    } catch (error) {
      console.error('Failed to search article:', error);
    }
  };

  const [loading, setLoading] = useState(false);
  const [loadingHeadlines, setLoadingHeadlines] = useState(false);

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>AI News</h1>
      <p className={styles.description}>
        I am your AI news search assistant.
        Tell me what kind of news you want to see
        e.g. I want to see a news article about the spanish economy.
      </p>
      <form
        onSubmit={async (event) => {
          setLoading(true);
          await handleSearch(event);
          setLoading(false);
        }}
        className={styles.form}
      >
        <input
          type="text"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          placeholder="Search for an article"
          className={styles.input}
        />
        <button type="submit" className={styles.button} disabled={loading}>
          {loading ? 'Loading...' : 'Search'}
        </button>
      </form>

      {searchResult && (
        <div className={styles.searchResult}>
          <h2>Search Result:</h2>
          <ArticleDisplayer article={searchResult} />
        </div>
      )}

      <div className={styles.articles}>
        <h1 className={styles.subHeader}>Headline Articles:</h1>
        {loadingHeadlines && <p className={styles.loadingHeadlines}>Loading Headlines...</p>}
        {articles.map((article, index) => (
          <ArticleDisplayer key={article.id || index} article={article} />
        ))}
      </div>
    </div>
  );
}
