import './App.css';
import Sidebar from './components/Sidebar';
import TopNavigation from './components/TopNavigation';

function App() {
  return (
    <div className="flex">
      <TopNavigation />
      <Sidebar />
    </div>
  );
}

export default App;
