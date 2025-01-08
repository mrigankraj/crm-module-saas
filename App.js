import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import OnboardingProgress from './components/OnboardingProgress';
import CommunicationDashboard from './components/CommunicationDashboard';
import AnalyticsDashboard from './components/AnalyticsDashboard';
import { AuthProvider, useAuth } from './contexts/AuthContext';

const PrivateRoute = ({ children }) => {
  const { isAuthenticated } = useAuth();
  return isAuthenticated ? children : <Navigate to="/login" />;
};

function App() {
  return (
    <AuthProvider>
      <Router>
        <div className="min-h-screen bg-gray-100">
          <nav className="bg-white shadow-lg">
            {/* Navigation implementation */}
          </nav>
          
          <main className="container mx-auto px-4 py-8">
            <Routes>
              <Route path="/login" element={<LoginPage />} />
              <Route path="/register" element={<RegisterPage />} />
              
              <Route
                path="/onboarding"
                element={
                  <PrivateRoute>
                    <OnboardingProgress />
                  </PrivateRoute>
                }
              />
              
              <Route
                path="/communication"
                element={
                  <PrivateRoute>
                    <CommunicationDashboard />
                  </PrivateRoute>
                }
              />
              
              <Route
                path="/analytics"
                element={
                  <PrivateRoute>
                    <AnalyticsDashboard />
                  </PrivateRoute>
                }
              />
              
              <Route path="/" element={<Navigate to="/onboarding" />} />
            </Routes>
          </main>
        </div>
      </Router>
    </AuthProvider>
  );
}

export default App;
