# Port C2-01 – lượt đầu của Long

Repository đích ban đầu chưa có commit. Thẻ C2-01 yêu cầu scaffold FastAPI tự nạp router, React/TypeScript/Vite, healthcheck, CI và cấu hình review.

Snapshot được cung cấp là `35869040bee02e7f75390221a1e379f5062cae70` của `dangpham-work/whybi-ai`, đã chứa toàn bộ các lượt sau. Để khởi đầu theo đúng trình tự, bản port này lấy scaffold tại commit C2-01 gốc `d3fea19aaef335177441bcfe0e3a2dddf65ba753` trong lịch sử snapshot đó.

Danh sách 172 file nhập từ nguồn được lưu ở `docs/port-c2-01-files.txt`. Backend có router/service giữ chỗ, schema và migration nền theo scaffold gốc; frontend có khung màn và router. Các phần này là nền để các thẻ tiếp theo triển khai. Không nhập ảnh, biểu đồ, kết quả đánh giá hay tính năng hoàn thiện ở snapshot cuối.

Kèm theo là `port-the.sh`, kiểm thử script và `thu-tu.md` đã chuẩn bị trong chat. Script vẫn mặc định lấy snapshot cuối; danh sách lịch sử ở tài liệu này không phải manifest để chạy lại script đó.

README đã đổi URL clone sang repository đích. Các thay đổi khác so với file nguồn chỉ gồm bỏ khoảng trắng cuối dòng và cập nhật trạng thái kiểm chứng của Long.

Chưa push, tạo PR hay thay đổi bảo vệ nhánh. Kết quả kiểm tra local và những phần chưa kiểm chứng được ghi ở `docs/status/long.md`.
