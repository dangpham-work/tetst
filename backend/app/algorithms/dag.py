"""DagValidator – BR-01, mục 5.2.5 & 6.1.4. Chủ: Long (C2-09).

Mã giả `sanitize(G)` ở mục 6.1.4: phá chu trình tại cạnh AI yếu nhất → rút gọn bắc cầu → xếp tầng.
Kiểm tra mỗi thao tác thêm cạnh < 200 ms (UC07); cây ≤ 200 nút.
"""

import networkx as nx


def would_create_cycle(g: nx.DiGraph, from_key: str, to_key: str) -> list[str] | None:
    """Trả đường đi chu trình (theo key) nếu thêm from→to tạo chu trình, ngược lại None.
    Cách làm: DFS từ `to` xem có tới được `from` không – O(V + E). TC03: N6→N5 khi đã có N5→N6."""
    raise NotImplementedError("C2-09")


def break_cycles(g: nx.DiGraph) -> nx.DiGraph:
    """Xóa cạnh confidence thấp nhất (ưu tiên cạnh source=AI) cho tới khi hết chu trình."""
    raise NotImplementedError("C2-09")


def transitive_reduction(g: nx.DiGraph) -> nx.DiGraph:
    """Bỏ A→C khi đã có A→…→C, giữ thuộc tính nút và cạnh."""
    raise NotImplementedError("C2-09")


def layers(g: nx.DiGraph) -> dict[str, int]:
    """Tầng hiển thị theo nx.topological_generations."""
    raise NotImplementedError("C2-09")


def frontier(g: nx.DiGraph, mastered: set[str]) -> set[str]:
    """Biên: nút chưa Đạt nhưng mọi tiên quyết đã Đạt (mục 2.2.1).
    Ví dụ Hình 2.2: mastered={N1,N3,N5} ⇒ {N2,N4,N6}."""
    raise NotImplementedError("C2-09")
