#!/usr/bin/env python3
"""補齊 README.md「全部頁面」那一節的目錄。

為什麼要這支程式：`index.md` 叫讀者「要點開某一頁請開 README」，但那份目錄是手寫的，
每批收錄之後就會落後（2026-11-21 時缺 57 頁）。這支程式只補缺、不改既有的行，
所以人工寫過的說明文字都會留著。

用法：
    python3 tools/toc.py            # 只檢查，印出缺哪幾頁
    python3 tools/toc.py --write    # 寫回 README.md

排序規則與原本的手寫目錄一致：來源頁依發表年（檔名裡的年份），其餘依檔名。
說明文字取自各頁 frontmatter 的 title；來源頁的 title 通常是論文標題，
所以改成「citation 的前段 ── title」那種既有寫法太容易出錯，一律只放 title。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

# 區段標題 → 資料夾
SECTIONS = [
    ("**主題**", "wiki/topics"),
    ("**來源（論文，依發表年）**", "wiki/sources"),
    ("**概念**", "wiki/concepts"),
    ("**實體**", "wiki/entities"),
    ("**綜述與登記簿**", "wiki/synthesis"),
]


def _frontmatter(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    return text[3:end if end > 0 else 200]


def _field(fm: str, name: str) -> str:
    m = re.search(rf'^{name}:\s*"?(.*?)"?\s*$', fm, re.M)
    return m.group(1) if m else ""


def describe(path: Path) -> str:
    """目錄裡那一行冒號後面的字。

    來源頁沿用手寫目錄的「姓氏 年份, *期刊*」格式（姓氏取自檔名，期刊取自 citation
    開頭到第一個數字之前）。作者是一人、兩人還是 et al. 在 frontmatter 裡查不到，
    所以這裡一律只寫姓氏，必要時由人補成「A & B」或「A et al.」。
    其餘頁型用 title。
    """
    fm = _frontmatter(path)
    if path.parent.name == "sources":
        m = re.match(r"s-([a-z]+)-(\d{4})-", path.name)
        cite = _field(fm, "citation")
        journal = re.split(r"\s*\d", cite, maxsplit=1)[0].strip(" ,.") if cite else ""
        if m:
            who = m.group(1).capitalize() + " " + m.group(2)
            return f"{who}, *{journal}*" if journal else who
    return _field(fm, "title") or path.stem


def year_key(path: Path):
    m = re.search(r"-(\d{4})-", path.name)
    return (int(m.group(1)) if m else 9999, path.name)


def main() -> int:
    write = "--write" in sys.argv
    lines = README.read_text(encoding="utf-8").split("\n")
    missing_total = []

    for header, folder in SECTIONS:
        d = ROOT / folder
        if not d.is_dir():
            continue
        files = sorted(d.glob("*.md"), key=year_key if "sources" in folder else lambda p: p.name)

        try:
            start = lines.index(header)
        except ValueError:
            print(f"README 裡找不到區段標題 {header}，跳過", file=sys.stderr)
            continue
        end = start + 1
        while end < len(lines) and lines[end].startswith("- ["):
            end += 1

        listed = {m.group(1) for line in lines[start + 1:end]
                  if (m := re.search(r"\((wiki/[a-z]+/[^)]+)\)", line))}
        missing = [f for f in files if f"{folder}/{f.name}" not in listed]
        if not missing:
            continue
        missing_total += [f"{folder}/{f.name}" for f in missing]
        if write:
            new = [f"- [{f.stem}]({folder}/{f.name})：{describe(f)}" for f in missing]
            lines[end:end] = new

    if not missing_total:
        print("README 目錄已完整，沒有缺頁。")
        return 0

    print(f"缺 {len(missing_total)} 頁：")
    for p in missing_total:
        print("  " + p)
    if write:
        README.write_text("\n".join(lines), encoding="utf-8")
        print("已寫回 README.md（既有的行與說明文字未改動；新加的行排在各區段末尾）。")
    else:
        print("加 --write 才會寫回 README.md。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
