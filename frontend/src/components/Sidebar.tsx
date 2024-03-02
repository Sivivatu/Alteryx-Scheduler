import { BsFillLightningFill, BsGearFill, BsPlus } from 'react-icons/bs';
import { FaFire, FaPoo } from 'react-icons/fa';

const Sidebar = () => {
  return (
    <div className="fixed left-0 top-0 m-0 flex h-screen w-16 flex-col bg-slate-200 text-black shadow-lg dark:bg-slate-900 dark:text-white">
      <h1>SideBar</h1>

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
