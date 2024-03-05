import { BsFillLightningFill, BsGearFill, BsPlus } from 'react-icons/bs';
import { FaFire, FaPoo } from 'react-icons/fa';

const Sidebar = () => {
  return (
    <div className="fixed left-0 top-0 m-0 flex h-screen w-16 flex-col bg-primary text-primeText shadow-lg dark:bg-secondary dark:text-primeText-dark">
      <h1>SideBar</h1>

      <nav className="flex sm:justify-center space-x-4">
  {[
    ['Home', '/dashboard'],
    ['Team', '/team'],
    ['Projects', '/projects'],
    ['Reports', '/reports'],
  ].map(([title, url]) => (
    <a href={url} className="rounded-lg px-3 py-2 text-slate-700 font-medium hover:bg-slate-100 hover:text-slate-900">{title}</a>
  ))}
</nav>
      

      <SidebarIcon icon={<FaFire size="28" />} />
      <Divider />
      <SidebarIcon icon={<BsPlus size="28" />} />
      <SidebarIcon icon={<BsFillLightningFill size="28" />} />
      <SidebarIcon icon={<FaPoo size="28" />} />
      <Divider />
      <SidebarIcon icon={<BsGearFill size="22" />} />
    </div>
  );
};

const SidebarIcon = ({ icon, text = 'tooltip 💡' }) => (
  <div className="sidebar-icon group">
    {icon}

    <span className="sidebar-tooltip group-hover:scale-100">{text}</span>
  </div>
);

const Divider = () => <hr className="sidebar-hr" />;

export default Sidebar;
