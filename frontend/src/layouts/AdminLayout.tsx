import { NavLink, Outlet } from "react-router";
import { Logo } from "../components/Logo";
import { SCREENS } from "../screens";

/** Khung Quản trị (bổ sung – chưa có trong Figma, thẻ GD-15). Dựng theo mẫu khung GV. */
export function AdminLayout() {
  return (
    <div className="flex min-h-screen">
      <aside className="w-62 shrink-0 bg-ink-900 p-4 text-white">
        <div className="mb-6 flex items-center gap-3 px-2 py-2">
          <Logo />
          <div>
            <p className="text-h3 font-bold">Whybi AI</p>
            <p className="caps !text-ink-300">Quản trị viên</p>
          </div>
        </div>
        {SCREENS.filter((s) => s.role === "ADMIN").map((s) => (
          <NavLink
            key={s.code}
            to={s.path}
            className={({ isActive }) => `block rounded-md px-4 py-2.5 text-body-m ${isActive ? "bg-white/10 font-semibold" : "text-ink-300"}`}
          >
            {s.title}
          </NavLink>
        ))}
      </aside>
      <main className="flex-1 p-7">
        <Outlet />
      </main>
    </div>
  );
}
