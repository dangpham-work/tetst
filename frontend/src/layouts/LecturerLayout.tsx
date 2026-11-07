import { Bell, Flame, LayoutGrid, Network, Search, Settings, Users } from "lucide-react";
import { NavLink, Outlet, useParams } from "react-router";
import { Logo } from "../components/Logo";

/** Khung web GV 1440px (Figma GV-01…GV-10): sidebar mực đậm 248px + thanh trên có breadcrumb. */
export function LecturerLayout() {
  const { classId } = useParams();
  const c = classId ? `/gv/classes/${classId}` : null;
  const items = [
    { to: "/gv/classes", label: "Lớp của tôi", icon: LayoutGrid, end: true },
    { to: c ? `${c}/tree` : null, label: "Cây kỹ năng", icon: Network },
    { to: c ? `${c}/heatmap` : null, label: "Bản đồ nhiệt", icon: Flame },
    { to: c ? `${c}/matching` : null, label: "Ghép cặp", icon: Users },
    { to: c ? `${c}/settings` : null, label: "Cấu hình", icon: Settings },
  ];
  return (
    <div className="flex min-h-screen">
      <aside className="flex w-62 shrink-0 flex-col bg-ink-900 text-white">
        <div className="flex items-center gap-3 px-6 py-6">
          <Logo />
          <div>
            <p className="text-h3 font-bold">Whybi AI</p>
            <p className="caps !text-ink-300">Giảng viên</p>
          </div>
        </div>
        <nav className="flex flex-col gap-1 px-4">
          {items.map(({ to, label, icon: Icon, end }) =>
            to ? (
              <NavLink
                key={label}
                to={to}
                end={end}
                className={({ isActive }) =>
                  `flex items-center gap-3 rounded-md px-4 py-2.5 text-body-m ${isActive ? "bg-white/10 font-semibold" : "text-ink-300 hover:bg-white/5"}`
                }
              >
                <Icon size={18} /> {label}
              </NavLink>
            ) : (
              <span key={label} className="flex items-center gap-3 px-4 py-2.5 text-body-m text-ink-500" title="Chọn một lớp trước">
                <Icon size={18} /> {label}
              </span>
            ),
          )}
        </nav>
      </aside>
      <div className="flex min-w-0 flex-1 flex-col">
        <header className="flex h-16 items-center justify-between border-b border-line-soft bg-surface px-7">
          <p className="text-body-m text-ink-500">Whybi AI</p>
          <div className="flex items-center gap-3">
            <label className="flex w-64 items-center gap-2 rounded-md border border-line-strong px-3 py-2 text-body-m text-ink-300">
              <Search size={16} /> <input className="w-full bg-transparent outline-none" placeholder="Tìm lớp, sinh viên, nút…" />
            </label>
            <button className="rounded-md border border-line-soft p-2" aria-label="Thông báo">
              <Bell size={18} />
            </button>
          </div>
        </header>
        <main className="flex-1 p-7">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
