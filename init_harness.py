# /// script
# requires-python = ">=3.8"
# dependencies = []
# ///
"""
init_harness.py — Khởi tạo hệ thống Harness + Memory Bank + Playbooks cho AI Agents.

Cách dùng:
    uv run https://raw.githubusercontent.com/namdo1983/mem001/main/init_harness.py

Cấu trúc tạo ra:
    project-root/
    ├── AGENTS.md                              ← Cổng vào (nằm ngoài root)
    └── memory-bank/                           ← Toàn bộ hệ thống nằm gọn bên trong
        ├── 00-HARNESS.md
        ├── projectBrief.md
        ├── productContext.md
        ├── techContext.md
        ├── systemPatterns.md
        ├── activeContext.md
        ├── progress.md
        ├── verificationMatrix.md
        ├── consolidated_learnings.md
        ├── decisions/
        │   └── _template.md
        └── playbooks/
            ├── diagnose.md
            ├── tdd.md
            ├── improve-codebase-architecture.md
            └── grill-with-docs.md
"""

import os
import sys
from urllib.request import urlopen, Request
from urllib.error import URLError

# ============================================================
# CẤU HÌNH
# ============================================================

MEMORY_BANK_DIR = "memory-bank"

SKILL_URLS = {
    "diagnose.md": "https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/diagnose/SKILL.md",
    "tdd.md": "https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/tdd/SKILL.md",
    "improve-codebase-architecture.md": "https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/improve-codebase-architecture/SKILL.md",
    "grill-with-docs.md": "https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/grill-with-docs/SKILL.md",
}

AGENTS_MAP = {
    "1": "Codex",
    "2": "Antigravity",
    "3": "Claude (Cline / RooCode)",
    "4": "OpenCode",
}


# ============================================================
# TEMPLATES
# ============================================================

def get_agents_md(agents_str: str) -> str:
    return f"""# AGENTS.md

**Active AI Agents:** {agents_str}

## Highest-priority project instruction for ALL Agents:

Regardless of whether you are {agents_str}, you MUST:

1. Read `memory-bank/00-HARNESS.md` FIRST.
2. Follow its load order exactly.
3. Keep this adapter thin; durable guidance belongs in `memory-bank/`.
4. Coordinate via the `memory-bank/` to ensure no conflicting changes.
"""


HARNESS_MD = r"""# 00-HARNESS.md — Project Harness

This is the single entry point for every AI agent working in this repository.
Read this file completely before touching any code.

---

## 1. Karpathy-Inspired Core Principles (ALWAYS ACTIVE)

These four rules apply to **every** interaction, **every** file change,
**every** terminal command. No exceptions.

### 1.1 Think Before Coding
- State your assumptions explicitly. If uncertain, **ask**.
- If multiple interpretations exist, present them — don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, **stop**. Name what's confusing. Ask.

### 1.2 Simplicity First
- Minimum code that solves the problem. Nothing speculative.
- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- If you write 200 lines and it could be 50, rewrite it.
- Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

### 1.3 Surgical Changes
- Touch only what you must. Clean up only your own mess.
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it — don't delete it.

### 1.4 Goal-Driven Execution
- Define verifiable success criteria before starting.
- Leverage tests-first thinking: what proof will show the work is done?
- Stay focused on the user's stated goal. Don't wander.

---

## 2. Mandatory Reasoning Gate

Before executing any file change, risky command, or non-trivial implementation:

1. Use `sequential-thinking` MCP (or equivalent structured reasoning) to plan.
2. Identify:
   - **Clarification Gate:** Any ambiguities, assumptions, or missing requirements. Stop and ask the user if critical details are missing.
   - **Consistency Check:** How the plan and tasks align with the project brief and tech constraints without introducing duplicate plans.
   - The requested outcome.
   - The smallest meaningful next step.
   - Relevant risks, affected files, and validation shape.
3. Classify the task complexity:
   - **Fast Track** (trivial, single-file fix) → proceed directly.
   - **Standard** (multi-file, moderate risk) → lightweight plan, then implement.
   - **Full Lifecycle** (architectural, high risk) → full design before code.

If sequential-thinking MCP is unavailable, report that limitation explicitly
and use a short written reasoning substitute. Do NOT silently skip the gate.

---

## 3. Baby-Step Contract

All execution uses Baby Steps:

1. Break the task into the smallest meaningful step.
2. Complete one substantive accomplishment at a time.
3. Validate after each step with the cheapest reliable check.
4. Document progress when durable project knowledge or harness state changed.
5. Start the next step only after the current step is complete or explicitly blocked.

---

## 4. Capability Router — Playbook Selection

Load the relevant playbook from `memory-bank/playbooks/` based on the user's intent.
**Load ONLY the matching playbook(s). Do NOT read all playbooks.**

| User Intent                                      | Playbook to Load                                       |
|--------------------------------------------------|--------------------------------------------------------|
| Bug fixing, test failure, flaky tests             | `memory-bank/playbooks/diagnose.md`                    |
| Structural refactoring, code duplication cleanup  | `memory-bank/playbooks/improve-codebase-architecture.md` |
| Writing new features or utilities with tests      | `memory-bank/playbooks/tdd.md`                         |
| Planning, domain modeling, ambiguous requirements | `memory-bank/playbooks/grill-with-docs.md`             |

---

## 5. Memory Bank — Context Files

This folder holds the project's living context.
Update these files when project facts, decisions, or progress change.

| File                          | Purpose                                          |
|-------------------------------|--------------------------------------------------|
| `projectBrief.md`            | Core requirements and goals                       |
| `productContext.md`          | Why this project exists, what problems it solves   |
| `techContext.md`             | Tech stack, dev setup, constraints                 |
| `systemPatterns.md`          | Architecture, design patterns, conventions         |
| `activeContext.md`           | Current focus, recent changes, what's blocked      |
| `progress.md`               | What works, what's left, cumulative status         |
| `verificationMatrix.md`     | Change X → must run test Y (proof requirements)    |
| `consolidated_learnings.md` | Cross-session lessons (long-term AI memory)         |
| `decisions/`                | Architecture Decision Records (ADRs)               |

---

## 6. Error Recovery Loop

When a command, test, edit, or validation step fails:

1. Stop broad implementation and inspect the failure signal.
2. Increment the retry counter for the current failing step.
3. Re-run reasoning to re-break the task around the observed failure.
4. Pick the next smallest baby step that can test one hypothesis.
5. If the same step fails 3 times, stop and ask the user for guidance.

---

## 7. End-of-Task Protocol

Before reporting task completion:

1. Run the cheapest reliable verification command set.
2. Update `activeContext.md` and `progress.md`.
3. If new lessons were learned, append to `consolidated_learnings.md`.
4. If an architectural decision was made, create an ADR in `decisions/`.
"""


MEMORY_BANK_TEMPLATES = {
    "projectBrief.md": """# Project Brief

Core requirements and goals of this project.

## Requirements
- [ ] Requirement 1
- [ ] Requirement 2

## Goals
- What is the primary goal of this project?
""",

    "productContext.md": """# Product Context

Why does this project exist? What problems does it solve?

## Problems Solved
-

## User Experience Goals
-
""",

    "techContext.md": """# Tech Context

Technologies, development environment, and constraints.

## Tech Stack
- Language / Framework:
- Database:
- Testing:

## Development Setup
- How to run:
- How to test:

## Constraints
-
""",

    "systemPatterns.md": """# System Patterns

Architecture, design patterns, and coding conventions.

## Architecture Overview
-

## Design Patterns in Use
-

## Naming Conventions
-
""",

    "activeContext.md": """# Active Context

Current working state — what's happening right now.

## Current Focus
-

## Recent Changes
-

## What's Blocked
-

## Next Steps
-
""",

    "progress.md": """# Progress

Cumulative project status.

## What Works
-

## What's Left
-

## Current Status
- [ ] New | [ ] In Progress | [ ] Nearly Done
""",

    "verificationMatrix.md": """# Verification Matrix

When you change X, you MUST run Y to prove it didn't break.

| Change Area | Required Verification | Command |
|---|---|---|
| Example: BasePage class | Run all smoke tests | `npx playwright test --grep @smoke` |
""",

    "consolidated_learnings.md": """# Consolidated Learnings

Cross-session lessons and insights. AI agents append here after each task.
Keep entries concise and actionable.

---
""",
}

ADR_TEMPLATE = """# ADR-NNNN: [Decision Title]

## Status
Proposed | Accepted | Deprecated | Superseded

## Context
What is the issue that we're seeing that is motivating this decision?

## Decision
What is the change that we're proposing and/or doing?

## Consequences
What becomes easier or more difficult to do because of this change?
"""


# ============================================================
# LOGIC
# ============================================================

def get_selected_agents() -> str:
    """Hiển thị menu chọn Agent và trả về chuỗi tên agents."""
    print("\n🤖 BẠN ĐANG DÙNG NHỮNG AI AGENTS NÀO?")
    print("-" * 50)
    for key, name in AGENTS_MAP.items():
        print(f"  [{key}] {name}")
    print("-" * 50)

    while True:
        choices = input("👉 Nhập số (VD: 1,2,3) hoặc Enter để chọn tất cả: ").strip()
        if not choices:
            return "All AI Agents"

        selected_keys = [c.strip() for c in choices.split(",")]
        selected = [AGENTS_MAP[k] for k in selected_keys if k in AGENTS_MAP]

        if selected:
            return ", ".join(selected)
        print("❌ Lựa chọn không hợp lệ, vui lòng nhập lại!")


def write_file_safe(filepath: str, content: str) -> bool:
    """Ghi file nếu chưa tồn tại. Trả về True nếu đã tạo mới."""
    if os.path.exists(filepath):
        print(f"  ⏭  Bỏ qua (đã tồn tại): {filepath}")
        return False

    parent = os.path.dirname(filepath)
    if parent and not os.path.exists(parent):
        os.makedirs(parent)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"  ✅ Đã tạo: {filepath}")
    return True


def fetch_url(url: str) -> str:
    """Tải nội dung từ URL. Trả về chuỗi rỗng nếu thất bại."""
    try:
        req = Request(url, headers={"User-Agent": "init-harness/1.0"})
        with urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8")
    except (URLError, OSError) as e:
        print(f"  ⚠️  Không tải được: {url}")
        print(f"      Lỗi: {e}")
        return ""


def create_root_files(agents_str: str) -> None:
    """Tạo AGENTS.md tại thư mục hiện tại (root)."""
    print("\n📁 [1/3] Khởi tạo AGENTS.md (Root)...")
    write_file_safe("AGENTS.md", get_agents_md(agents_str))


def create_memory_bank() -> None:
    """Tạo thư mục memory-bank/ với 00-HARNESS.md + các file context."""
    print("\n📁 [2/3] Khởi tạo Memory Bank...")

    # 00-HARNESS.md nằm trong memory-bank/
    write_file_safe(os.path.join(MEMORY_BANK_DIR, "00-HARNESS.md"), HARNESS_MD)

    # Các file context
    for filename, content in MEMORY_BANK_TEMPLATES.items():
        write_file_safe(os.path.join(MEMORY_BANK_DIR, filename), content)

    # decisions/ với template ADR
    write_file_safe(
        os.path.join(MEMORY_BANK_DIR, "decisions", "_template.md"),
        ADR_TEMPLATE,
    )


def create_playbooks() -> None:
    """Tải 4 Skills gốc của Matt Pocock từ GitHub vào memory-bank/playbooks/."""
    print("\n📁 [3/3] Khởi tạo Playbooks (Skills by Matt Pocock)...")

    playbooks_dir = os.path.join(MEMORY_BANK_DIR, "playbooks")
    fetched = 0
    failed = 0

    for filename, url in SKILL_URLS.items():
        filepath = os.path.join(playbooks_dir, filename)

        if os.path.exists(filepath):
            print(f"  ⏭  Bỏ qua (đã tồn tại): {filepath}")
            continue

        print(f"  📥 Đang tải: {filename}...", end=" ", flush=True)
        content = fetch_url(url)

        if content:
            write_file_safe(filepath, content)
            fetched += 1
        else:
            fallback = f"# {filename}\n\n> ⚠️ Không tải được từ GitHub.\n> Tải thủ công tại: {url}\n"
            write_file_safe(filepath, fallback)
            failed += 1

    if failed:
        print(f"\n  ⚠️  {failed} file không tải được. Kiểm tra kết nối mạng.")
    if fetched:
        print(f"  🎯 Đã tải thành công {fetched} playbook(s) nguyên bản từ Matt Pocock.")


def print_summary() -> None:
    """In cấu trúc thư mục cuối cùng."""
    print("\n" + "=" * 60)
    print("🎉 HOÀN TẤT! Cấu trúc Harness đã sẵn sàng:")
    print("=" * 60)
    print("""
  project-root/
  ├── AGENTS.md                              ← Cổng vào (root)
  └── memory-bank/                           ← Toàn bộ hệ thống
      ├── 00-HARNESS.md                      ← Luật thép
      ├── projectBrief.md
      ├── productContext.md
      ├── techContext.md
      ├── systemPatterns.md
      ├── activeContext.md
      ├── progress.md
      ├── verificationMatrix.md
      ├── consolidated_learnings.md
      ├── decisions/
      │   └── _template.md
      └── playbooks/
          ├── diagnose.md
          ├── tdd.md
          ├── improve-codebase-architecture.md
          └── grill-with-docs.md
""")
    print("💡 Mở dự án bằng AI Agent → AI tự đọc AGENTS.md → memory-bank/")
    print("   → Load skills khi cần. Bắt đầu code!\n")


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("  🚀 INIT HARNESS — Memory Bank + Skills Setup v1.0")
    print("  Karpathy Core Principles + Matt Pocock Skills")
    print("=" * 60)

    agents_str = get_selected_agents()

    create_root_files(agents_str)
    create_memory_bank()
    create_playbooks()
    print_summary()


if __name__ == "__main__":
    main()
