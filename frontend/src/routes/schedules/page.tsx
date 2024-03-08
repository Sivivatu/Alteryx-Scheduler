import { Button } from '@/components/ui/button';
import { useNavigate } from 'react-router-dom';

export default function SchedulesPage() {
  const navigate = useNavigate();
  const routeChange = () => {
    const path = `/dashboard`;
    navigate(path);
  };

  return (
    <>
      <div className="max-h-full">
        <h1 className="flex-col content-center items-center text-center text-3xl">Initial Schedules Page</h1>

        <Button onClick={routeChange}>Home</Button>
      </div>
    </>
  );
}
