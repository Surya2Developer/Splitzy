import { API_BASE_URL } from '@env';

export const API_URL = API_BASE_URL || 'http://localhost:8000';

export const endpoints = {
  login: `${API_URL}/api/auth/login`,
  register: `${API_URL}/api/auth/register`,
  refreshToken: `${API_URL}/api/auth/refresh`,
};
