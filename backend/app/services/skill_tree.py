"""SkillTreeService – Sinh cây nháp, sửa cây, duyệt rubric, phát hành (UC06–UC09). Chủ: Long (C2-09), Đăng
(C1-10, C1-11).
"""


class SkillTreeService:
    def build_draft_tree(self, document_id):
        raise NotImplementedError("C1-10")

    def add_edge(self, version_id, from_key, to_key):
        raise NotImplementedError("C2-09")

    def approve_rubric(self, node_id, rubric):
        raise NotImplementedError("C2-09")

    def publish(self, version_id):
        raise NotImplementedError("C2-09")
