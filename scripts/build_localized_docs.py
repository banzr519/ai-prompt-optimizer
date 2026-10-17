#!/usr/bin/env python3
"""Render localized entry pages from the checked-in catalog; no network or model calls."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START = "<!-- language-navigation:start -->"
END = "<!-- language-navigation:end -->"


def navigation(text, nav):
    block = START + "\n" + nav + "\n" + END
    if START in text:
        return re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, text, count=1, flags=re.S)
    first, rest = text.split("\n", 1)
    return first + "\n\n" + block + "\n" + rest


def wrap_direction(text, locale):
    if locale["direction"] == "rtl":
        return '<div dir="rtl">\n\n' + text + '\n</div>\n'
    return text


def render(catalog):
    version = catalog["release_version"]
    locales = catalog["locales"]
    output = {}
    install = catalog["installation_entry"]
    links = [f'[{x["native"]}]({x["readme"]})' for x in locales]
    nav = "\n\n".join(" · ".join(links[i:i + 6]) for i in range(0, len(links), 6))
    nav += "\n\n[Language coverage / 语言覆盖](docs/LANGUAGES.md)"
    for loc in locales:
        if loc.get("primary"):
            f = ROOT / loc["readme"]
            output[f] = navigation(f.read_text(), nav)
            f = ROOT / loc["guide"]
            output[f] = navigation(f.read_text(), "[Language coverage / 语言覆盖](LANGUAGES.md)")
            continue
        h, t, tag = loc["headings"], loc["strings"], loc["tag"]
        readme = f'# AI Prompt Optimizer · {loc["native"]}\n\n'
        readme += f'[English](README.md) · [简体中文](README.zh-CN.md) · [🌐 Languages / 语言](docs/LANGUAGES.md)\n\n'
        readme += f'**v{version} · MIT · {tag}**\n\n**{t["tagline"]}**\n\n{t["overview"]}\n\n'
        readme += f'**{install["label"]}:** {install["readme_links"]}\n\n'
        readme += f'## {h["install"]}\n\n{t["install"]}\n\n'
        paths = ('```text\n~/.agents/skills/ai-prompt-optimizer/\n'
                 '<project>/.agents/skills/ai-prompt-optimizer/\n'
                 '%USERPROFILE%\\.agents\\skills\\ai-prompt-optimizer\\\n```\n\n')
        readme += ('<div dir="ltr">\n\n' + paths + '</div>\n\n') if loc["direction"] == "rtl" else paths
        readme += f'## {h["modes"]}\n\n- {t["refine"]}\n- {t["execute"]}\n- {t["audit"]}\n\n'
        readme += f'## {h["example"]}\n\n'
        example = f'```text\n$ai-prompt-optimizer {t["example"]}\n```\n\n'
        readme += ('<div dir="ltr">\n\n' + example + '</div>\n\n') if loc["direction"] == "rtl" else example
        readme += f'[{h["guide"]}]({loc["guide"]}) · [🌐 Languages / 语言](docs/LANGUAGES.md)\n\n'
        readme += f'## {h["limits"]}\n\n{t["limits"]}\n\n[MIT](LICENSE)\n'
        output[ROOT / loc["readme"]] = wrap_direction(readme, loc)
        guide = f'# {h["guide"]} · AI Prompt Optimizer\n\n'
        guide += f'[{loc["native"]}](../{loc["readme"]}) · [English](USER_GUIDE.md) · [简体中文](USER_GUIDE.zh-CN.md) · [🌐 Languages / 语言](LANGUAGES.md)\n\n'
        guide += f'**v{version} · {tag}**\n\n'
        guide += f'**{install["label"]}:** {install["guide_links"]}\n\n'
        for k in ["inputs", "advanced", "language", "fallback", "troubleshooting", "limits"]:
            guide += f'## {h[k]}\n\n{t[k]}\n\n'
        guide += f'## {h["docs"]}\n\n'
        guide += '- [English — full user guide](USER_GUIDE.md) · [简体中文 — 完整使用指南](USER_GUIDE.zh-CN.md)\n'
        guide += '- [English — models](MODEL_COMPATIBILITY.md) · [简体中文 — 模型说明](MODEL_COMPATIBILITY.zh-CN.md)\n'
        guide += '- [English — publishing](PUBLISHING.md) · [简体中文 — 发布指南](PUBLISHING.zh-CN.md)\n'
        guide += '- [English — research](RESEARCH.md) · [简体中文 — 研究记录](RESEARCH.zh-CN.md)\n'
        guide += '- [Language validation / 语言验证](../evals/RESULTS-v2.3.0.md)\n'
        output[ROOT / loc["guide"]] = wrap_direction(guide, loc)
    index = '# Languages / 语言\n\n[English](../README.md) · [简体中文](../README.zh-CN.md)\n\n'
    index += f'**v{version} · {len(locales)} documentation entries / 个语言及地区入口**\n\n'
    index += ('Choose a local introduction and starter guide below. Full research, publishing and historical evaluations remain English/Chinese unless otherwise stated. Pāli is an experimental bilingual starter. Added translations are AI-authored and have not received professional native-speaker review.\n\n'
              '选择对应语言的介绍及入门指南。详细研究、发布及历史评测文件主要保留英文／简体中文；巴利语为实验双语入门页。新增翻译由 AI 编写，尚未经母语专业审校。\n\n'
              'Documentation coverage, instruction-language behavior and model proficiency are different. This catalog is not a model certification or a runtime restriction. Other languages may work according to the host model. No English fallback is silently forced.\n\n'
              '文档覆盖、技能的语言规则与模型语言能力分别记录。此目录不证明所有模型均已实测，也不限制其他语言使用。技能不会静默改用英语。\n\n'
              '| Language / 语言 | Tag | README | Guide / 指南 | Coverage / 覆盖 |\n| --- | --- | --- | --- | --- |\n')
    labels = {"primary-full": "Primary full / 主维护版", "experimental-bilingual-starter": "Experimental bilingual / 实验双语", "localized-starter-and-guide": "Localized starter / 本地化入门"}
    for x in locales:
        index += f'| {x["native"]} | `{x["tag"]}` | [README](../{x["readme"]}) | [Guide](../{x["guide"]}) | {labels[x["documentation_level"]]} |\n'
    index += ('\n## Locale rules / 地区与语言规则\n\n'
              '- Simplified and Traditional Chinese stay distinct; Traditional does not automatically imply a particular region. / 保留简繁体区别，不把繁体自动绑定某地区。\n'
              '- pt-BR and pt-PT have separate entries; generic Portuguese follows the user’s preference. / 巴西与欧洲葡萄牙语分别提供入口。\n'
              '- Pāli (`pi`), Balinese (`ban`) and Bengali (`bn`) are distinct. / 巴利语、巴厘语和孟加拉语分别处理。\n'
              '- Commands, placeholders, JSON keys and exact required text remain unchanged. / 命令、变量、JSON 字段及指定原文不随语言自动翻译。\n'
              '- [IANA language registry](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) · [Rules](../references/languages.md) · [Validation](../evals/RESULTS-v2.3.0.md)\n\n'
              'To maintain translations, edit [the catalog](../locales/catalog.json) and run `python3 scripts/build_localized_docs.py` from the repository. Use `--check` to detect drift. / 维护时修改目录数据，再运行脚本；使用 `--check` 检查生成文件是否一致。\n')
    output[ROOT / "docs/LANGUAGES.md"] = index
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report drift without writing files")
    args = parser.parse_args()
    catalog = json.loads((ROOT / "locales/catalog.json").read_text())
    assert len({x["tag"] for x in catalog["locales"]}) == len(catalog["locales"]), "duplicate locale"
    changes = []
    for path, content in render(catalog).items():
        assert path.resolve().is_relative_to(ROOT), "path outside repository"
        if not path.exists() or path.read_text() != content:
            changes.append(str(path.relative_to(ROOT)))
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
    if args.check and changes:
        print("Out of date:\n" + "\n".join(changes))
        return 1
    print(f'{len(catalog["locales"])} locales; {len(changes)} changed; ' + ("check passed" if args.check else "render complete"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
