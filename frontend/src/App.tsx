import { ThemeProvider } from './components/theme-provider';
import DashboardPage from './dashboard/page';

export default function App() {
  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <DashboardPage />
    </ThemeProvider>
  );
}
