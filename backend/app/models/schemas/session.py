"""HỢP ĐỒNG DỮ LIỆU #2 – phiên giảng lại (Bảng 7 kế hoạch phân công).
Người chốt: Đăng + Long (C1-01) · Bên dùng: Long, Thắng, Quyền · Hạn: H1.
Ví dụ JSON tham chiếu: mục 5.4.4 của đề cương.
"""

from datetime import datetime
from uuid import UUID

from pydantic import Field

from app.models.enums import (
    CriterionCode,
    FlagType,
    InputMode,
    MasteryState,
    QuestionStrategy,
    SessionStatus,
    TurnType,
    Verdict,
)
from app.models.schemas.common import ApiModel


class SessionStart(ApiModel):
    """POST /sessions"""

    node_id: UUID
    input_mode: InputMode = InputMode.TEXT
    tts_enabled: bool = False
    peer_match_item_id: UUID | None = None  # phiên xác nhận lại sau học cặp (FR-PM-07)


class Question(ApiModel):
    """Câu hỏi của Tutee (kênh session:{id} → session.question)."""

    text: str
    strategy: QuestionStrategy | None = None
    target_point_id: str | None = None
    audio_url: str | None = None
    deadline: datetime | None = None  # FR-TB-11


class SessionCreated(ApiModel):
    session_id: UUID
    status: SessionStatus
    opening: Question


class Turn(ApiModel):
    """POST /sessions/{id}/turns – lời giảng hoặc câu trả lời."""

    turn_type: TurnType = TurnType.EXPLANATION
    input_mode: InputMode = InputMode.TEXT
    text: str
    audio_ref: str | None = None
    stt_confidence: float | None = Field(None, ge=0, le=1)
    transcript_edited: bool = False
    paste_ratio: float | None = Field(None, ge=0, le=1)  # FR-TB-04
    typing_cps: float | None = None
    response_time_ms: int | None = None


class TurnReply(ApiModel):
    status: SessionStatus
    question: Question | None = None  # None khi vòng phản biện kết thúc
    notice: str | None = None  # phản hồi trung lập khi Guard gắn cờ
    questions_asked: int = 0
    questions_total: int = 0


class Transcript(ApiModel):
    """POST /sessions/{id}/audio → bản chép lời (FR-TB-06, FR-TB-07)."""

    text: str
    confidence: float
    low_confidence_words: list[str] = []
    audio_ref: str
    needs_confirmation: bool = False


class CriterionResult(ApiModel):
    code: CriterionCode
    weight: float
    score: float
    max: float
    rationale: str | None = None


class JudgeResult(ApiModel):
    """Đầu ra của Judge (mục 6.3) trước khi áp BR-03."""

    criteria: list[CriterionResult]  # đúng 5 tiêu chí
    covered_points: list[str]
    missing_points: list[str]
    misconceptions: list[dict] = []  # [{id, corrected: bool}]
    passed_challenges: int
    judge_runs: int = 2


class SessionResult(ApiModel):
    """GET /sessions/{id}/result và payload sự kiện session.completed (Redis Pub/Sub)."""

    session_id: UUID
    student_id: UUID
    node_id: UUID
    class_id: UUID
    state: MasteryState  # trạng thái ô ma trận sau phiên
    verdict: Verdict
    total_score: float
    pass_threshold: int = 70
    criteria: list[CriterionResult]
    strengths: list[str] = []
    review_hints: list[str] = []  # câu hỏi gợi mở, KHÔNG chứa đáp án
    source_pages: list[int] = []
    unlocked_nodes: list[str] = []
    flags: list[FlagType] = []
    is_peer_followup: bool = False
    detected_misconceptions: list[str] = []
