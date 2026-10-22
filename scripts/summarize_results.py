"""Produce descriptive results from preserved judgments; never infer missing scores."""
import json
from pathlib import Path

from exam_cheat_sheet.compile import verify_freeze
from exam_cheat_sheet.evaluate import score_grading

ROOT = Path(__file__).resolve().parents[1]
BENCH = ROOT / 'benchmarks/mit-6041-quiz1'


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def main():
    frozen = verify_freeze(BENCH / 'freeze.json')
    scores = {}
    runs = {}
    for group in ['A', 'B']:
        grading = read(BENCH / f'runs/final-grade-{group}/grading.json')
        scores[group] = score_grading({**grading, 'benchmark': 'mit-6041-final', 'group': group}, BENCH / f'scores/{group}')
        runs[group] = read(BENCH / f'runs/final-{group}/run.json')
        if not runs[group].get('valid'):
            raise ValueError(f'Invalid final run {group}')
    for key in ['actual_models', 'permissions', 'output_budget', 'timeout_seconds', 'agent_config_sha256']:
        if runs['A'][key] != runs['B'][key]:
            raise ValueError(f'Conditions differ: {key}')
    delta = scores['B']['weighted_points'] - scores['A']['weighted_points']
    coverage = read(BENCH / 'coverage.json')
    dev = read(BENCH / 'runs/dev-grade/grading.json')
    result = {
        'status': 'completed', 'repository_created': True, 'sheet_generated': True,
        'baseline_score': scores['A']['weighted_points'], 'assisted_score': scores['B']['weighted_points'],
        'max_points': 105, 'baseline_correct_subparts': scores['A']['correct_count'],
        'assisted_correct_subparts': scores['B']['correct_count'], 'total_subparts': 11,
        'score_improvement': delta, 'replicates_per_group': 1,
        'final_test_validated': True, 'generalization_proven': False,
        'model': runs['A']['actual_models'], 'sheet_code_version': frozen['code_version'],
        'coverage': coverage, 'development': {'points': dev['total_points'], 'max_points': dev['max_points'],
                                            'correct_subparts': dev['correct_subparts'], 'total_subparts': dev['total_subparts']},
    }
    (BENCH / 'results.json').write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    lines = ['# 实测报告 / Evaluation report', '',
             '## 最终测试：Fall 2010 Quiz 1', '',
             '| 条件 | 严格正确分 | 完全正确子题 | 独立运行次数 |', '| --- | ---: | ---: | ---: |',
             f'| A：原卷及自带公式页 | {scores["A"]["weighted_points"]}/105 | {scores["A"]["correct_count"]}/11 | 1 |',
             f'| B：相同原卷 + 冻结 v2 速查表 | {scores["B"]["weighted_points"]}/105 | {scores["B"]["correct_count"]}/11 | 1 |',
             '', f'**B−A：{delta:+g} 分。** 严格分为每子题全对才给满分，否则 0；不混入部分分。', '',
             '## 逐题结果', '', '| 子题 | 满分 | A | B |', '| --- | ---: | ---: | ---: |']
    for a, b in zip(scores['A']['items'], scores['B']['items']):
        if a['item_id'] != b['item_id']:
            raise ValueError('Item order differs; normalize before tabulation')
        lines.append(f'| {a["item_id"]} | {a["max_points"]} | {a["awarded_points"]} | {b["awarded_points"]} |')
    lines += ['', '逐题判定理由与官方解答定位见 [A 评分](scores/A/score.md) 和 [B 评分](scores/B/score.md)。',
              '', '## 覆盖、开发和产物质量', '',
              f'- C 独立覆盖审计：{coverage["full"]}/11 完全覆盖，{coverage["partial"]}/11 部分覆盖，{coverage["absent"]}/11 未覆盖。详见 [原始审计](runs/final-C/response.md)。',
              f'- 开发卷：Fall 2009 所提供 Problem B，{dev["total_points"]}/{dev["max_points"]} 分，{dev["correct_subparts"]}/{dev["total_subparts"]} 子题。原卷分母确为 98，不冒称 100。',
              '- 开发后只做可检索性/步骤明确化修订；保留 [v1→v2 记录](../../examples/mit-6041/revision-log.md)，未把开发重测当成新测试。',
              '- 10 份训练来源、70 页逐页账本；23 个概念、35 条公式记录均有来源和条件/变量。来源完整性不等于所有原始页面已逐字核验。',
              '- v2 PDF：A4、6 页、最低 9 pt、无检测到的越界；6 页预览均已目视检查。公式使用纯文本表达，未声称 LaTeX 排版。',
              '', '## 隔离及可审计记录', '',
              '- v2、概念数据、训练清单、代码/脚本/schema/依赖和协议先冻结，之后才下载 final 问题；A/B 完成后才下载官方答案。',
              '- A/B 使用相同 `openai/gpt-6-astra#high`、全新上下文、全部工具拒绝、相同 8000-word 软输出预算和 1800 秒进程超时；均可使用数学先验。',
              '- 每组保留原始 prompt、response、事件、session 元数据和输入哈希；全部 12 张题面图片含原卷公式摘要同等提供。官方答案仅交给新评分上下文。',
              '- [冻结记录](freeze.json)、[A 作答](runs/final-A/response.md)、[B 作答](runs/final-B/response.md)、[C 审计](runs/final-C/response.md)。',
              '', '## 局限与结论', '',
              '- 一种模型、每组一次；无统计显著性或跨课程泛化结论。公开试卷可能出现在模型预训练中；只能说未用于本次资料构建。',
              '- 评分由隔离的模型参照官方答案执行，使用研究者规定的严格整题规则，不是官方细粒度 marking scheme 或人工考官评分。',
              '- 工具权限与上下文隔离不等于操作系统沙箱；普通工具使用者能够绕开此流程，冻结验证不能阻止有权修改代码和冻结记录的操作者。',
              '- 无自动 OCR/手写识别；公式图形有审阅账本和待核验标记。未提供的教材、练习册等内容不冒称已覆盖。']
    if min(scores[g]['weighted_points'] for g in ['A', 'B']) >= 100:
        lines.append('- **存在明显天花板效应，不能据此证明速查表提高了模型作答分数。**')
    lines += ['', '课程派生内容依据 [CC BY-NC-SA 4.0 署名说明](ATTRIBUTION.md) 发布。']
    (BENCH / 'evaluation-report.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
