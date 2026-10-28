# UEFA Champions League 2023/24 — Group-Stage Performance Analysis

A reproducible, group-stage-only football outcome analysis built from official UEFA fixture results. The project focuses on team outcomes and attacking/defensive output. It does not claim to measure tactical processes, player contributions, expected goals, pressing, or causality because those event-level data are not included.

## Scope and headline checks

- 32 teams, 8 groups, 96 fixtures, 6 matches per team.
- 296 total goals (goals for and goals against both sum to 296).
- Manchester City and Real Madrid each finished the group stage with 18 points.
- Manchester City scored the most group-stage goals (18); Arsenal recorded the best goal difference (+12).
- These are descriptive group-stage results, not estimates of underlying performance quality or predictions.

## Files

- `match_results.csv`: 96 match-level scores with season, stage and group labels.
- `team_summary_powerbi.csv`: Power BI-ready team outcomes and per-match rates.
- `analyze_group_stage.py`: rebuilds the team summary from the match file using Python 3 standard library only.
- `ucl_group_stage_dashboard.png` and SVG charts: performance visuals.

## Reproduce

From this repository folder, run:

```bash
python analyze_group_stage.py
```

The script validates match count, season/stage, team count, six matches per club, and total goals before writing the Power BI-ready summary.

## Measures

Points = 3 × wins + draws. Goal difference = goals for − goals against. Per-match rates divide the corresponding team totals by six group fixtures. These are team outcome measures; they do not establish why a team achieved those outcomes.

## Data source and limitations

Scores were transcribed and checked against [UEFA’s published 2023/24 group-stage fixtures and results](https://www.uefa.com/uefachampionsleague/news/0285-18e1b226cae3-4bbfb31dc1f7-1000--all-the-group-stage-fixtures-and-results/). The dataset is limited to final scores. It has no shots, xG, possession, pressure events, line-ups, player minutes, match-state events, or contextual covariates. Do not interpret this as a full tactical or player performance model.

## Power BI

Load `team_summary_powerbi.csv` as a table and `match_results.csv` as the match-level fact table. A useful first page can show points, goals for/against and goal difference cards; points and goal-difference rankings; a goals-for versus goals-against scatterplot; and group/team filters.