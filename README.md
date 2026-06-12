# 🚀 Init Harness — Memory Bank + AI Skills Setup

Biến bất kỳ repo nào thành workspace sẵn sàng cho AI Agents chỉ với **1 lệnh**.

Hệ thống này tích hợp:
- **Karpathy Core Principles** — 4 nguyên tắc vàng ép AI code chuẩn chỉnh
- **Matt Pocock Skills** — 4 bộ kỹ năng thực chiến (TDD, Diagnose, Refactor, Grill)
- **Memory Bank** — Bộ nhớ dự án để AI hiểu context qua nhiều phiên

## ⚡ Cài đặt nhanh (30 giây)

Yêu cầu: Đã cài [uv](https://docs.astral.sh/uv/getting-started/installation/).

Mở Terminal **tại thư mục gốc dự án** của bạn và chạy:

```bash
uv run https://raw.githubusercontent.com/namdo1983/mem001/main/init_harness.py
```

Script sẽ:
1. Hỏi bạn đang dùng AI Agent nào (Codex, Antigravity, Claude, OpenCode).
2. Tạo `AGENTS.md` tại root.
3. Tạo `memory-bank/` chứa toàn bộ hệ thống harness + playbooks.

> **An toàn:** Chạy lại bao nhiêu lần cũng được. File đã tồn tại sẽ bị bỏ qua, không ghi đè.

## 📁 Cấu trúc sau khi cài

```
your-project/
├── AGENTS.md                              ← Cổng vào cho mọi AI Agent
└── memory-bank/
    ├── 00-HARNESS.md                      ← Luật thép (Karpathy + Baby Steps)
    ├── projectBrief.md                    ← Dự án là gì?
    ├── productContext.md                  ← Giải quyết vấn đề gì?
    ├── techContext.md                     ← Stack, setup, constraints
    ├── systemPatterns.md                  ← Kiến trúc & Design Patterns
    ├── activeContext.md                   ← Đang làm gì? Kẹt ở đâu?
    ├── progress.md                        ← Tiến độ (xong gì, còn gì)
    ├── verificationMatrix.md             ← Sửa X → phải test Y
    ├── consolidated_learnings.md         ← Bài học xuyên phiên
    ├── decisions/
    │   └── _template.md                   ← Mẫu ADR
    └── playbooks/
        ├── diagnose.md                    ← Skill: Chẩn đoán bug
        ├── tdd.md                         ← Skill: Test-Driven Dev
        ├── improve-codebase-architecture.md ← Skill: Refactor kiến trúc
        └── grill-with-docs.md             ← Skill: Phỏng vấn & lên kế hoạch
```

## 🎯 Cách sử dụng

### Bước 1: Cài harness
```bash
cd /path/to/your-project
uv run https://raw.githubusercontent.com/namdo1983/mem001/main/init_harness.py
```

### Bước 2: Mở dự án bằng AI Agent
Khi AI Agent (Antigravity, Claude Code, Codex...) mở dự án, nó sẽ tự động:
1. Đọc `AGENTS.md` → Biết phải đọc `memory-bank/00-HARNESS.md`.
2. Đọc `00-HARNESS.md` → Bị ép tuân thủ Karpathy + Baby Steps.
3. Khi cần skill → Tự load đúng playbook từ `memory-bank/playbooks/`.

### Bước 3: AI tự điền Memory Bank
Trong quá trình làm việc, AI sẽ tự cập nhật các file trong `memory-bank/`:
- `activeContext.md` — Trạng thái hiện tại
- `progress.md` — Tiến độ
- `consolidated_learnings.md` — Bài học rút ra
- `decisions/` — Quyết định kiến trúc quan trọng

## 🧠 Triết lý

| Thành phần | Nguồn cảm hứng | Vai trò |
|---|---|---|
| Core Principles | [Andrej Karpathy](https://x.com/karpathy/status/2015883857489522876) | Ép AI code đơn giản, chính xác, không làm lố |
| Skills/Playbooks | [Matt Pocock](https://github.com/mattpocock/skills) | Kỹ năng thực chiến: TDD, Debug, Refactor |
| Memory Bank | [Cline Memory Bank](https://github.com/cline/cline) | Bộ nhớ dài hạn cho AI qua nhiều phiên |
| Baby Steps | [Cline Baby Steps](https://github.com/cline/prompts) | Làm từng bước nhỏ, test sau mỗi bước |

## 📝 License

MIT
