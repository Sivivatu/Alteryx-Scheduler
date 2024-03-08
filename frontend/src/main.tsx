import Contact from '@/routes/Contact';
import Login from '@/routes/Login/Login';
import SchedulesPage from '@/routes/schedules/page';
import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import App from './App';
import { ThemeProvider } from './components/theme-provider';
import './index.css';

const router = createBrowserRouter([
  { path: '/', element: <Login /> },
  { path: '/dashboard', element: <App /> },
  { path: '/schedules', element: <SchedulesPage /> },
  { path: '/contact', element: <Contact /> },
]);

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <RouterProvider router={router} />
    </ThemeProvider>
  </React.StrictMode>
);
