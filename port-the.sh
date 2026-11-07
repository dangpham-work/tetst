#!/bin/sh
# Dùng: sh port-the.sh <MÃ-THẺ>
# Tùy chọn: TIEUDE="Tiêu đề commit" sh port-the.sh C1-05
set -eu
SHA=35869040bee02e7f75390221a1e379f5062cae70
DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
THE=${1:?Thiếu mã thẻ, ví dụ C1-05}
TIEUDE=${TIEUDE:-"Port $THE"}
LIST="$DIR/files/$THE.txt"
[ -s "$LIST" ] || { echo "Không có danh sách file cho $THE" >&2; exit 1; }
[ -n "$(git config user.email || :)" ] || { echo "Chưa đặt git user.email" >&2; exit 1; }
[ -z "$(git status --porcelain)" ] || { echo "Còn thay đổi chưa commit" >&2; exit 1; }
git remote get-url whybi-ai >/dev/null 2>&1 || git remote add whybi-ai "${SRC_URL:-https://github.com/dangpham-work/whybi-ai.git}"
git cat-file -e "$SHA^{commit}" 2>/dev/null || git fetch -q whybi-ai main
git fetch -q origin
NHANH="port/$(printf '%s' "$THE" | tr 'A-Z' 'a-z')"
if git rev-parse -q --verify origin/main >/dev/null; then
    git switch -q -c "$NHANH" origin/main
else
    git switch -q -c "$NHANH"
fi
git --literal-pathspecs checkout "$SHA" --pathspec-from-file="$LIST"
git add -A
git commit -q -m "$TIEUDE" -m "Nguồn: dangpham-work/whybi-ai@$SHA"
echo "Xong $THE trên nhánh $NHANH. Đọc lại: git show --stat HEAD. Rồi: git push -u origin $NHANH và mở PR."
