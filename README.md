# Exam Cheat Sheet Skill

把课件、教材、考试范围和历年试卷整理成**可溯源、有重点、能检查遗漏**的复习资料。

这是一个可移植 Agent Skill + Python 工具包。Agent 负责阅读、数学核验与概念编写；
工具负责逐页摄取、来源与数据隔离、可解释优先级、同源生成、排版和评测记录。
工具不会把“抽取到文字”冒充“已经理解教材”。

## 安装

需要 Python 3.11+、[uv](https://docs.astral.sh/uv/)。课程下载还需要 `curl`。

```sh
git clone https://github.com/ReedZhu37/Exam-Cheat-Sheet-Skill.git
cd Exam-Cheat-Sheet-Skill
uv sync --locked
uv run python -m exam_cheat_sheet --help
```

将 `skills/exam-cheat-sheet/` 整个目录复制到你的 Agent 支持的 skills 目录，
或直接让 Agent 阅读其中的 `SKILL.md`。使用示例：

> 使用 exam-cheat-sheet。材料在 materials/，考试范围见 scope.md。
> 请生成中文复习指南与最多 6 页的速查表，保留公式条件、变量定义和来源页码，
> 把缺失、待核验及压缩掉的内容单独列出。

命令从本仓库根目录运行；Skill 的工具资源路径需要指向本仓库。
扫描件没有文本层时会明确标记待 OCR，不会假称已识别。

## 使用流程

1. 清点来源：角色、训练/开发/最终测试拆分、许可、页码、SHA-256。
2. 摄取并逐页记账；保存完整页图，核验公式和题面图表。
3. 按 Skill 编写概念 JSON：定义、条件、变量、前置知识、解题步骤、易错点、来源。
4. 编译复习指南、证据版、速查版、优先级和缺失报告。
5. 用开发题检查实际可用性；只针对有证据的缺陷修订。
6. 冻结资料后再做独立最终评测。

```sh
uv run python -m exam_cheat_sheet ingest manifest.json --root materials --out extracted
uv run python -m exam_cheat_sheet compile concepts.json --out output --budget-words 3000
uv run python -m exam_cheat_sheet render output/cheatsheet.md --out output/cheatsheet.pdf --max-pages 6 --min-font 9
```

生成文件：`review-guide.md`、`cheatsheet-expanded.md`、`cheatsheet.md`、
`priority-report.json`、`coverage-report.md`；PDF 另附渲染检查记录。
范围与必要前置知识优先于历史题频率。预算不足时明确报告，不能无限缩小字号。

## 真实示例与评测

示例使用 MIT OCW 6.041SC 的 Quiz 1 离散概率范围：

| 用途 | 材料 |
| --- | --- |
| 训练 | Lectures 1–7、Quiz 1 review、Spring 2009 Quiz 1 |
| 开发 | Fall 2009 Quiz 1 |
| 最终测试 | Fall 2010 Quiz 1：105 分，11 个子题 |

- [课程示例](examples/mit-6041/)
- [第二版速查表](examples/mit-6041/v2/cheatsheet.md) · [6 页 PDF](examples/mit-6041/v2/cheatsheet.pdf)
- [复习指南](examples/mit-6041/v2/review-guide.md) · [开发集修订记录](examples/mit-6041/revision-log.md)
- [预注册方案](benchmarks/mit-6041-quiz1/protocol.md)
- [下载清单与哈希](benchmarks/mit-6041-quiz1/downloads.json)

```sh
uv run python scripts/fetch_benchmark.py --stage train
uv run python -m exam_cheat_sheet compile examples/mit-6041/concepts-v1.json --out examples/mit-6041/v1 --budget-words 3000
```

最终题与解答不会随训练下载混入。评测执行器依赖已登录的 OpenCode V2；
普通摄取、编译、PDF 和测试不依赖 OpenCode，也不需要 API key。
独立作答采用全新 session，工具权限全部拒绝，原卷每页图片与公式摘要等量提供。
冻结前构建者不读取最终题；解答另在评分阶段下载并交给评分上下文。
这属于工具权限与上下文隔离，不是操作系统沙箱。

## 测试与边界

```sh
uv run pytest -q --basetemp .local/pytest
```

支持 PDF、PPTX、DOCX、Markdown、纯文本。未承诺 OCR、手写识别、旧版 `.doc/.ppt`、
复杂公式自动重建。PDF 用可读的文本公式排版，不是完整 LaTeX 引擎。
自动测试通过、公式核验、排版检查、考试得分与泛化结论分别报告。

## 文档与许可

- [架构](docs/architecture.md) · [命令与 JSON 格式](docs/cli.md) · [许可边界](docs/licensing.md)
- [第三方说明](THIRD_PARTY_NOTICES.md) · [课程内容署名](examples/mit-6041/ATTRIBUTION.md)

原创代码与通用 Skill：MIT。MIT OCW 原始材料及派生课程示例：
**CC BY-NC-SA 4.0**，不得因软件使用 MIT 许可而将课程内容改授 MIT。
本项目不代表 MIT 或 Anthropic，也不包含 Anthropic 受限文档 Skill 的复制内容。
