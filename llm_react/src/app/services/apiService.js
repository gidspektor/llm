import axios from 'axios';

const API_KEY = process.env.NEXT_PUBLIC_API_KEY;
const API_URL = process.env.NEXT_PUBLIC_API_URL;

const axiosInstance = axios.create({
    baseURL: API_URL,
    headers: {
      'x-api-key': API_KEY,
    },
  }
);

export const fetchArticles = async () => {
  try {
    const response = await axiosInstance.post('/articles');
    return response.data;
  } catch (error) {
    console.error('Error fetching articles:', error);
    throw error;
  }
};

export const createArticle = async (articleData) => {
  try {
    const response = await axiosInstance.post('/create', {'text': articleData});
    return response.data;
  } catch (error) {
    console.error('Error creating article:', error);
    throw error;
  }
};

export const searchArticle = async (text) => {
    try {
      const response = await axiosInstance.post('/search', {'text': text});
      return response.data;
    } catch (error) {
      console.error('Error searching article:', error);
      throw error;
    }
  };