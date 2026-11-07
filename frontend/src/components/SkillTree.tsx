/**
 * SkillTree – vẽ DAG bằng React Flow, tự sắp xếp theo tầng, tô màu theo trạng thái.
 * Dùng chung cho GV-04 (sửa kéo thả), GV-05 (bản đồ nhiệt), SV-02 (bản đồ học tập).
 * Thẻ: GD-03 (Thắng). Dữ liệu: TreeVersion – backend/app/models/schemas/tree.py.
 */
export interface SkillTreeProps {
  mode: "edit" | "heatmap" | "learner";
}

export function SkillTree({ mode }: SkillTreeProps) {
  // TODO(GD-03): import { ReactFlow } from "@xyflow/react"; nút dùng StatusBadge (màu + biểu tượng)
  return <div className="rounded-lg border border-line-soft bg-surface p-6 text-ink-500">SkillTree ({mode}) – thẻ GD-03</div>;
}
