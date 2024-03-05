import { ThemeProvider } from '@/components/theme-provider';
import './App.css';
import DashboardPage from './dashboard/page';

function App() {
  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <div className="flex h-screen">
        <DashboardPage />
      </div>
    </ThemeProvider>
  );
}

export default App;
