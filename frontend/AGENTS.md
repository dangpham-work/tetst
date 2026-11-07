# frontend/ – hướng dẫn cho phiên AI

> Bổ sung cho `AGENTS.md` ở gốc. React 19 · Vite · TypeScript 5.9 · Tailwind CSS 4 · React Router · @xyflow/react · lucide-react · Vitest.

## Chạy

```bash
cd frontend
npm ci
npm run dev            # http://localhost:5173, proxy /api → http://localhost:8000
npm run typecheck && npm test && npm run build
npm run gen:api        # sinh src/lib/api-types.ts từ OpenAPI (backend phải đang chạy)
```

Thêm thư viện → báo nhóm, một người `npm install <gói>` và commit `package-lock.json`.

## Làm một màn hình

1. Tra màn trong `src/screens.ts` (mã, vai, đường dẫn, thẻ việc, node Figma) và ảnh `docs/design/screens/<MÃ>.png`.
2. Tạo `src/pages/<vai>/<MÃ bỏ gạch>.tsx` với `export default` (vd. `lecturer/GV05.tsx`) – router tự nạp, không sửa `router.tsx`.
3. Lấy thiết kế bằng plugin **figma**: “dựng màn GV-05 theo node `<node-id>` trong `src/screens.ts`, dùng token trong `src/styles/index.css`”.
   Kết quả Figma chỉ là **tham chiếu** – chuyển sang component có sẵn trong `src/components/`.
4. Dữ liệu: gọi `api<T>(path)` trong `src/lib/api.ts` với kiểu từ `api-types.ts`; realtime dùng `RealtimeClient` (`src/lib/ws.ts`).
   Backend chưa xong (501) → hiện trạng thái “đang phát triển”, không giả lập ngầm.

## Luật giao diện

- Chỉ dùng token màu/chữ trong `@theme` của `src/styles/index.css` (`ink-*`, `honey`, `teal`, `st-*`) – không mã màu hex rải rác.
- Trạng thái thành thạo / màu bản đồ nhiệt **luôn** qua `MASTERY`, `HEAT`, `ROOT_CAUSE` trong `src/lib/status.ts` (màu + biểu tượng + chữ – NFR-12).
- Chữ hiển thị bằng tiếng Việt, font Be Vietnam Pro. Thông báo lỗi lấy từ `FRIENDLY` trong `lib/api.ts`.
- Hỗ trợ bàn phím, `aria-label` cho nút chỉ có biểu tượng; màn SV dùng được trên điện thoại (≥ 360 px).
- Component dùng lại: `Button`, `StatusBadge`, `SkillTree`, `HeatGrid`, `Recorder`, `Waveform`, `Logo`, layout theo vai trong `src/layouts/`.

## Test

- Vitest + Testing Library: `src/**/*.test.ts(x)`. Test hành vi người dùng thấy (chữ, vai trò), không test chi tiết CSS.
- Luồng nhiều màn → e2e Playwright trong `e2e/` (của Quyền).
