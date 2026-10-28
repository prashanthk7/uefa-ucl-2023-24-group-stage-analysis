"""Rebuild 2023/24 UCL group-stage team outcomes from data/match_results.csv (Python 3, stdlib only)."""
import csv
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parent
INPUT=ROOT/"match_results.csv"
OUTPUT=ROOT/"team_summary_powerbi.csv"
fields=["season","stage","group","team","matches_played","wins","draws","losses","goals_for","goals_against","goal_difference","points","win_rate_pct","draw_rate_pct","loss_rate_pct","goals_for_per_match","goals_against_per_match","goal_difference_per_match","points_per_match","source_url"]
SOURCE="https://www.uefa.com/uefachampionsleague/news/0285-18e1b226cae3-4bbfb31dc1f7-1000--all-the-group-stage-fixtures-and-results/"
with INPUT.open(encoding="utf-8-sig",newline="") as f: matches=list(csv.DictReader(f))
assert len(matches)==96, f"Expected 96 fixtures, got {len(matches)}"
clubs=defaultdict(lambda:dict(mp=0,w=0,d=0,l=0,gf=0,ga=0,group=None))
for m in matches:
    h,a=m["home_team"],m["away_team"]; hg,ag=int(m["home_goals"]),int(m["away_goals"])
    assert hg>=0 and ag>=0 and m["stage"]=="Group stage" and m["season"]=="2023/24"
    assert m["group"] in "ABCDEFGH"
    for team,gf,ga in ((h,hg,ag),(a,ag,hg)):
        x=clubs[team]; assert x["group"] in (None,m["group"]); x["group"]=m["group"]
        x["mp"]+=1; x["gf"]+=gf; x["ga"]+=ga
        if gf>ga:x["w"]+=1
        elif gf==ga:x["d"]+=1
        else:x["l"]+=1
assert len(clubs)==32 and all(x["mp"]==6 for x in clubs.values())
assert sum(x["gf"] for x in clubs.values())==296 and sum(x["gf"] for x in clubs.values())==sum(x["ga"] for x in clubs.values())
rows=[]
for team,x in sorted(clubs.items(),key=lambda kv:(kv[1]["group"],-3*kv[1]["w"]-kv[1]["d"],-(kv[1]["gf"]-kv[1]["ga"]),-kv[1]["gf"],kv[0])):
    mp=x["mp"]; pts=3*x["w"]+x["d"]; gd=x["gf"]-x["ga"]
    rows.append(dict(season="2023/24",stage="Group stage",group=x["group"],team=team,matches_played=mp,wins=x["w"],draws=x["d"],losses=x["l"],goals_for=x["gf"],goals_against=x["ga"],goal_difference=gd,points=pts,win_rate_pct=round(x["w"]/mp*100,2),draw_rate_pct=round(x["d"]/mp*100,2),loss_rate_pct=round(x["l"]/mp*100,2),goals_for_per_match=round(x["gf"]/mp,3),goals_against_per_match=round(x["ga"]/mp,3),goal_difference_per_match=round(gd/mp,3),points_per_match=round(pts/mp,3),source_url=SOURCE))
with OUTPUT.open("w",encoding="utf-8-sig",newline="") as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
print(f"Wrote {len(rows)} teams from {len(matches)} fixtures; {sum(x['gf'] for x in clubs.values())} goals.")
