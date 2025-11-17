import React, { useEffect } from 'react';
import AppNavigator from './navigation/AppNavigator';
import { PaperProvider } from 'react-native-paper';
import { AuthProvider } from './context/AuthContext';
import { API_URL } from './config/api';

export default function App() {
  useEffect(() => {
    const testBackend = async () => {
      try {
        const response = await fetch(`${API_URL}/docs`);
        console.log('✅ Backend reachable:', response.status);
      } catch (error) {
        console.log('❌ Backend connection failed:', error.message);
      }
    };
    testBackend();
  }, []);

  return (
    <AuthProvider>
      <PaperProvider>
        <AppNavigator />
      </PaperProvider>
    </AuthProvider>
  );
}
