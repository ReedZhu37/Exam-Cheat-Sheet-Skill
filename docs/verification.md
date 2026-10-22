# 验证记录

## 自动测试

- 本机：Windows，CPython 3.14.7，锁定依赖 `uv.lock`。
- 完整套件：**187 passed, 3 skipped**，无失败。
- 三项跳过是本机无法创建符号链接的测试，未将跳过记为通过。
- 实际本地命令：`uv run pytest -q --basetemp .local/pytest-final --junitxml=.local/test-results.xml`。
- 推荐新克隆命令：`uv run pytest -q --basetemp .pytest-tmp`，临时目录无需预建父目录。
- [GitHub Actions 四平台组合验证](https://github.com/ReedZhu37/Exam-Cheat-Sheet-Skill/actions/runs/39704895565)：
  Ubuntu / Windows × Python 3.11 / 3.14 均 success。

测试覆盖：权限/真实路径边界、伪造分类、重复与缺页、损坏 PDF、公式待核验、
Office 图片保存、范围/前置闭包、试卷频率去重、跨概念分值守恒、来源页码、
schema 对齐、PDF 实际字号/边界/公式条件同页、冻结漂移及可迁移性、
严格评分、最终资产替换/残页/归一化重复题号、已存在作答覆盖保护。

首次远端 CI 因测试临时目录父路径未创建而失败，随后将测试目录改为仓库根下
`.pytest-tmp` 后四组通过。该 CI/文档修改发生在冻结之后，没有修改冻结内容、
概念、优先级、解析器、评分程序或模型设置。

## 实际材料与排版

- 10 份训练文件下载、SHA-256 和字节数校验；70 页逐页账本。
- 原课件公式页逐项目视核验记录：`examples/mit-6041/source-review.md`。
- v2：23 概念、35 公式记录；A4 六页，PDFium 实测最低 9 pt，无越界。
- 六页截图全部已检查；只在屏幕验收，没有宣称物理打印测试。
- 未摄取指定教材和全部 recitations/problem sets/tutorials；23/23 是本示例
  有依据的概念清单覆盖数，不是整份官方范围已穷尽的证明。

## 冻结与运行完整性

- 冻结提交：`b9522f9ae2e73f4fdd230d68dd62d922e7460ef5`，先于最终题下载。
- 另建独立 Git 克隆后验证成功：14 个输出、21 个实现/依赖文件，及记录的输入清单。
- Git 对 `benchmarks/`、`examples/` 保留原始字节，避免换行转换破坏记录哈希。
- A/B 的 12 张图片输入及顺序逐一相同；提示文本比较确认，唯一内容差异为冻结表。
- A、B、C：各 12 张原卷图片；A/B 评分者：各 18 张（12 题面 + 6 官方解答）。
- 五次最终作答/审计/评分运行均确认实际模型 `openai/gpt-6-astra#high`，
  无工具事件；原始 prompt/response 与运行记录的 SHA-256 全部一致。
- 每次回答独立 session；仅在 A/B/C 作答全部结束后才下载官方解答。
- 文件级隔离与工具拒绝属于本次执行协议，不是对任意恶意操作者的 OS 沙箱承诺。

## 分开解释验证结论

自动测试证明已覆盖的软件性质；渲染检查证明实际布局边界；内容审阅检查指定来源；
独立作答记录本次模型成绩。四者不能互相替代。

最终 A/B 都是 105/105，因此没有观察到分数提升；没有统计显著性或跨课泛化结论。
原始答案与逐题理由见 `benchmarks/mit-6041-quiz1/evaluation-report.md`。
