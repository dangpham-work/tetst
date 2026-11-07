import { Bell, History, Network, User, Users } from "lucide-react";
import { NavLink, Outlet, useParams } from "react-router";
import { Logo } from "../components/Logo";

/** Khung mobile SV 390px (Figma SV-01…SV-08): header trắng + thanh tab dưới. Responsive từ 360px (NFR-11). */
export function StudentLayout() {
  const { classId } = useParams();
  const tabs = [
    { to: classId ? `/sv/classes/${classId}` : "/sv/classes", label: "Bản đồ", icon: Network },
    { to: classId ? `/sv/classes/${classId}/peers` : "/sv/classes", label: "Bạn cùng tiến", icon: Users },
    { to: "/sv/history", label: "Lịch sử", icon: History },
    { to: "/me", label: "Hồ sơ", icon: User },
  ];
  return (
    <div className="mx-auto flex min-h-screen max-w-[480px] min-w-[360px] flex-col bg-app">
      <header className="flex items-center justify-between border-b border-line-soft bg-surface px-4 py-3">
        <div className="flex items-center gap-2">
          <Logo size={28} />
          <p className="text-h3 font-bold">Whybi AI</p>
        </div>
        <button className="rounded-full bg-app p-2" aria-label="Thông báo">
          <Bell size={18} />
        </button>
      </header>
      <main className="flex-1 p-4 pb-24">
        <Outlet />
      </main>
      <nav className="fixed inset-x-0 bottom-0 mx-auto grid max-w-[480px] grid-cols-4 border-t border-line-soft bg-surface py-2">
        {tabs.map(({ to, label, icon: Icon }) => (
          <NavLink
            key={label}
            to={to}
            end
            className={({ isActive }) => `flex flex-col items-center gap-1 text-caps ${isActive ? "font-semibold text-teal" : "text-ink-300"}`}
          >
            <Icon size={20} />
            {label}
          </NavLink>
        ))}
      </nav>
    </div>
  );
}
