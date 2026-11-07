# docs/status/long.md   (chỉ Long sửa)

> Cập nhật sau mỗi thẻ (kế hoạch §4.2). Mọi người – và mọi phiên AI – đọc hết `docs/status/` trước khi sửa code.

- Xong:
  - C2-01 – khung repo đã đủ theo mục 7.1–7.2:
    - FastAPI tự nạp router: mọi module trong `app/api/` có biến `router` được gắn vào `/api/v1`. Thêm router mới không cần sửa `main.py`.
    - `/health` không cần token.
    - CI chạy ruff, pytest, tsc, build.
    - Có AGENTS.md, CODEOWNERS (còn chờ username), mẫu PR (thêm mục "Đụng file ngoài phạm vi", "Thư viện mới").
    - README có mục "Chạy bằng một lệnh".
    - Test: `backend/tests/test_app_skeleton.py`.
- Phát sự kiện / hợp đồng đã chốt: —
- Đang làm: C2-01 – port scaffold vào repository đích; chưa chuyển sang C2-02.
- Cần từ người khác:
  - Cả đội: gửi username GitHub để bật `.github/CODEOWNERS` (hiện mọi dòng đang là chú thích).
  - Người điều phối: bật bảo vệ nhánh `main` (bắt buộc PR + CI xanh).

## Port lượt 1 – C2-01 (2026-11-07)

- Nhánh: `port/c2-01`. Nguồn scaffold: `d3fea19aaef335177441bcfe0e3a2dddf65ba753`, nằm trong lịch sử snapshot `35869040bee02e7f75390221a1e379f5062cae70`.
- Nhập khung backend/frontend, Docker/Nginx, CI và tài liệu nền; không nhập các tính năng hoàn thiện ở các thẻ sau. Xem `docs/port-c2-01.md`.
- Kiểm tra local: backend ruff check/format đạt, pytest 42 đạt (1 cảnh báo deprecation từ Starlette/httpx); frontend typecheck đạt, 2 test đạt, build đạt; script port 2 test đạt và `sh -n` đạt; `docker compose config --quiet` đạt.
- Chưa kiểm chứng migration và stack Docker: Docker Engine chưa chạy. Chưa có kết quả CI trên PR hoặc xác nhận chạy trên 4 máy. CODEOWNERS vẫn cần username thật; không thay đổi bảo vệ nhánh.
