import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import App from './App';
import { ThemeProvider } from './components/theme-provider';
// import DashboardPage from './dashboard/page';
import Contact from '@/routes/Contact';
import Login from '@/routes/Login/Login';
import './index.css';

const router = createBrowserRouter([
  { path: '/', element: <Login /> },
  { path: '/dashboard', element: <App /> },
  // { path: '/dashboard', element: <DashboardPage /> },
  { path: '/contact', element: <Contact /> },
]);

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <RouterProvider router={router} />
    </ThemeProvider>
  </React.StrictMode>
);
