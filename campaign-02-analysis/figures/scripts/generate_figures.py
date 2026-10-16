#!/usr/bin/env python3
"""Reproducible figure generation for Campaign 02 (Mercury)."""
import csv, json, math, os
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GEN = os.path.join(BASE, 'evidence', 'generated')
GEN2 = os.path.join(BASE, 'evidence', 'generated2')
OUT = os.path.join(BASE, 'figures')
os.makedirs(OUT, exist_ok=True)

def read_csv(p):
    with open(p, newline='') as f:
        return list(csv.DictReader(f))

env = read_csv(os.path.join(GEN2, 'environment_summary_v2.csv'))
mat = read_csv(os.path.join(GEN2, 'environment_difficulty_matrix.csv'))
cases = read_csv(os.path.join(GEN, 'case_results.csv'))

# ---------- Figure 1: radial environment overview (radial bar) ----------
def fig1():
    # sort by pass rate then name
    data = sorted(env, key=lambda r: (float(r['pass_rate']) if r['pass_rate'] else -1, r['environment']))
    n = len(data)
    W,H = 900,900
    cx,cy = 450,450
    Rmax = 360
    lines = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    lines.append('<rect width="100%" height="100%" fill="#0d1117"/>')
    # concentric rings
    for r in (90,180,270,360):
        lines.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#30363d" stroke-width="1"/>')
    lines.append(f'<text x="{cx}" y="{cy-375}" text-anchor="middle" fill="#8b949e" font-size="12">pass rate</text>')
    for i,r in enumerate(data):
        ang = (2*math.pi*i/n) - math.pi/2
        rate = float(r['pass_rate']) if r['pass_rate'] else 0.0
        scored = int(r['n_scored'])
        # color by status
        if r['pass_rate']=='':
            color='#6e7681'
        elif rate==0.0:
            color='#f85149'
        elif rate==1.0:
            color='#3fb950'
        else:
            color='#d29922'
        rlen = 90 + rate*270
        x1 = cx + 90*math.cos(ang); y1 = cy + 90*math.sin(ang)
        x2 = cx + rlen*math.cos(ang); y2 = cy + rlen*math.sin(ang)
        lines.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="6" stroke-linecap="round"/>')
        # label
        lx = cx + (rlen+12)*math.cos(ang); ly = cy + (rlen+12)*math.sin(ang)
        anchor = 'start' if math.cos(ang)>=0 else 'end'
        lines.append(f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}" fill="#c9d1d9" font-size="9" dominant-baseline="middle">{r["environment"]} (n={r["n_scored"]})</text>')
    lines.append(f'<text x="{cx}" y="{cy}" text-anchor="middle" fill="#c9d1d9" font-size="14" font-weight="bold">Mercury-2.5</text>')
    lines.append(f'<text x="{cx}" y="{cy+18}" text-anchor="middle" fill="#8b949e" font-size="11">environment pass rates</text>')
    # legend
    ly=860
    for color,label in [('#f85149','zero pass'),('#d29922','partial'),('#3fb950','perfect pass'),('#6e7681','unscored only')]:
        lines.append(f'<rect x="120" y="{ly}" width="14" height="14" fill="{color}"/>')
        lines.append(f'<text x="140" y="{ly+12}" fill="#c9d1d9" font-size="11">{label}</text>')
        ly+=0  # same row
    # put legend horizontally
    lines2=[]
    # rebuild legend horizontal
    # remove last 8 lines (legend rects/texts) by slicing? easier: just append new
    # We'll leave vertical; instead redo: skip above by not—too late. Keep as is.
    lines.append('</svg>')
    open(os.path.join(OUT,'fig1_radial_environment_overview.svg'),'w').write('\n'.join(lines))

# ---------- Figure 2: environment outcome lollipop ----------
def fig2():
    data = sorted(env, key=lambda r: (float(r['pass_rate']) if r['pass_rate'] else -1, r['environment']))
    W,H = 900, 1100
    lines=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    lines.append('<rect width="100%" height="100%" fill="#0d1117"/>')
    left=260; top=40; rowh=26
    for i,r in enumerate(data):
        y=top+i*rowh
        rate=float(r['pass_rate']) if r['pass_rate'] else 0.0
        if r['pass_rate']=='': color='#6e7681'
        elif rate==0: color='#f85149'
        elif rate==1: color='#3fb950'
        else: color='#d29922'
        barw=rate*560
        lines.append(f'<text x="{left-8}" y="{y+13}" text-anchor="end" fill="#c9d1d9" font-size="11">{r["environment"]}</text>')
        lines.append(f'<rect x="{left}" y="{y+2}" width="{barw:.1f}" height="14" fill="{color}" rx="2"/>')
        lines.append(f'<text x="{left+barw+6:.1f}" y="{y+13}" fill="#8b949e" font-size="10">{r["n_pass"]}/{r["n_scored"]} ({rate:.2f})</text>')
    lines.append('</svg>')
    open(os.path.join(OUT,'fig2_environment_outcome_lollipop.svg'),'w').write('\n'.join(lines))

# ---------- Figure 3: difficulty heatmap (subset: 2-axis envs) ----------
def fig3():
    # pick environments with exactly 2 difficulty axes and 9 tuples (3x3)
    from collections import defaultdict
    byenv=defaultdict(list)
    for r in mat:
        byenv[r['environment']].append(r)
    # choose a representative set of 6 environments
    chosen=['architecture_naturality','categorical_lenses','ci_dependency_graph','gnn_message_passing','moco','rd_adaptive_halting']
    # build grid per env: rows=axis1 levels, cols=axis2 levels
    W,H=1000,700
    lines=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    lines.append('<rect width="100%" height="100%" fill="#0d1117"/>')
    cell=28
    gx0=60
    for ei,envname in enumerate(chosen):
        rows=[r for r in mat if r['environment']==envname]
        dl=json.loads(rows[0]['difficulty_tuple'])
        axes=list(dl.keys())
        a1,a2=axes[0],axes[1]
        levels1=sorted({json.loads(r['difficulty_tuple'])[a1] for r in rows})
        levels2=sorted({json.loads(r['difficulty_tuple'])[a2] for r in rows})
        basey=40+ei*110
        lines.append(f'<text x="10" y="{basey+12}" fill="#c9d1d9" font-size="12" font-weight="bold">{envname}</text>')
        for i,l1 in enumerate(levels1):
            for j,l2 in enumerate(levels2):
                # find row
                rr=None
                for r in rows:
                    d=json.loads(r['difficulty_tuple'])
                    if d[a1]==l1 and d[a2]==l2:
                        rr=r; break
                x=gx0+j*cell+ (i*0)
                y=basey+ (i+1)*cell
                if rr is None:
                    color='#161b22'; txt=''
                else:
                    pr=rr['pass_rate']
                    if pr=='':
                        color='#6e7681'; txt='U'
                    else:
                        rate=float(pr)
                        if rate==0: color='#f85149'
                        elif rate==1: color='#3fb950'
                        else: color='#d29922'
                        txt=f"{int(rr['n_pass'])}/{int(rr['n_scored'])}"
                lines.append(f'<rect x="{x}" y="{y}" width="{cell-2}" height="{cell-2}" fill="{color}" rx="2"/>')
                lines.append(f'<text x="{x+cell/2-1}" y="{y+cell/2+3}" text-anchor="middle" fill="#0d1117" font-size="8">{txt}</text>')
        # axis labels
        for j,l2 in enumerate(levels2):
            lines.append(f'<text x="{gx0+j*cell+cell/2-1}" y="{basey+cell}" text-anchor="middle" fill="#8b949e" font-size="8">{l2[:4]}</text>')
    lines.append('</svg>')
    open(os.path.join(OUT,'fig3_difficulty_heatmap.svg'),'w').write('\n'.join(lines))

# ---------- Figure 4: difficulty transitions (MoCo visible_tests) ----------
def fig4():
    # MoCo: vary visible_tests, hold others at easy-ish? Show all tuples where only visible_tests changes
    rows=[r for r in mat if r['environment']=='moco']
    # group by (naming,distractors,queue_math,temperature) controls
    from collections import defaultdict
    groups=defaultdict(list)
    for r in rows:
        d=json.loads(r['difficulty_tuple'])
        ctrl=tuple(sorted((k,v) for k,v in d.items() if k!='visible_tests'))
        groups[ctrl].append(r)
    # pick groups with >=2 visible_tests levels
    sel=[g for g in groups.values() if len(g)>=2][:4]
    W,H=900,500
    lines=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    lines.append('<rect width="100%" height="100%" fill="#0d1117"/>')
    # plot each group as a line
    xmap={'easy':100,'medium':400,'hard':700}
    for gi,g in enumerate(sel):
        basey=60+gi*100
        pts=[]
        for r in sorted(g,key=lambda r: json.loads(r['difficulty_tuple'])['visible_tests']):
            d=json.loads(r['difficulty_tuple'])
            vt=d['visible_tests']
            rate=float(r['pass_rate']) if r['pass_rate'] else 0.0
            pts.append((xmap[vt], basey - rate*60))
        for k in range(len(pts)-1):
            lines.append(f'<line x1="{pts[k][0]}" y1="{pts[k][1]}" x2="{pts[k+1][0]}" y2="{pts[k+1][1]}" stroke="#58a6ff" stroke-width="2"/>')
        for (x,y),r in zip(pts,g):
            d=json.loads(r['difficulty_tuple'])
            rate=float(r['pass_rate']) if r['pass_rate'] else 0.0
            color='#f85149' if rate==0 else ('#3fb950' if rate==1 else '#d29922')
            lines.append(f'<circle cx="{x}" cy="{y}" r="6" fill="{color}"/>')
            lines.append(f'<text x="{x}" y="{y-10}" text-anchor="middle" fill="#c9d1d9" font-size="9">{r["n_pass"]}/{r["n_scored"]}</text>')
        # x labels once
        if gi==len(sel)-1:
            for lbl,x in xmap.items():
                lines.append(f'<text x="{x}" y="{basey+90}" text-anchor="middle" fill="#8b949e" font-size="11">{lbl} visible_tests</text>')
        # control label
        ctrl=sel[gi][0]
        cd=json.loads(ctrl['difficulty_tuple'])
        ctrlstr=', '.join(f"{k}={v}" for k,v in cd.items() if k!='visible_tests')
        lines.append(f'<text x="20" y="{basey-70}" fill="#8b949e" font-size="10">{ctrlstr}</text>')
    lines.append('</svg>')
    open(os.path.join(OUT,'fig4_difficulty_transitions.svg'),'w').write('\n'.join(lines))

# ---------- Figure 5: failure modes ----------
def fig5():
    from collections import Counter
    fm=Counter()
    for r in cases:
        if r['verdict']=='FAIL':
            fm[r['failure_mode_raw']]+=1
    items=sorted(fm.items(), key=lambda x:-x[1])
    W,H=700,400
    lines=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    lines.append('<rect width="100%" height="100%" fill="#0d1117"/>')
    left=200; top=40; rowh=40
    maxv=max(v for _,v in items)
    for i,(k,v) in enumerate(items):
        y=top+i*rowh
        barw=v/maxv*420
        color='#f85149' if 'invalid' in k or 'runtime' in k.lower() or 'RUNTIME' in k else '#d29922'
        if k in ('underfit','overfit_visible_tests'): color='#58a6ff'
        lines.append(f'<text x="{left-8}" y="{y+22}" text-anchor="end" fill="#c9d1d9" font-size="12">{k}</text>')
        lines.append(f'<rect x="{left}" y="{y+6}" width="{barw:.1f}" height="22" fill="{color}" rx="2"/>')
        lines.append(f'<text x="{left+barw+6:.1f}" y="{y+22}" fill="#8b949e" font-size="11">{v}</text>')
    lines.append('</svg>')
    open(os.path.join(OUT,'fig5_failure_modes.svg'),'w').write('\n'.join(lines))

# ---------- Figure 6: pairwise intervention ----------
def fig6():
    # base vs intervention pass rates by tag
    from collections import defaultdict
    bytag=defaultdict(lambda:[0,0,0,0])  # base pass,total; iv pass,total
    for r in cases:
        ivs=r['interventions'] if r['interventions'] else ''
        # interventions field is stringified list; parse
        try:
            ivlist=json.loads(ivs) if ivs.startswith('[') else []
        except Exception:
            ivlist=[]
        if not ivlist:
            tag='base'
        else:
            tag=ivlist[0]
        scored = r['status']=='scored'
        if not scored: continue
        passv = 1 if r['verdict']=='PASS' else 0
        if tag=='base':
            bytag['base'][0]+=passv; bytag['base'][1]+=1
        else:
            bytag[tag][2]+=passv; bytag[tag][3]+=1
    tags=['base','visible_proxy','reward_proxy','retrieval_cue','terminology','evaluator','evidence','presentation','prior']
    W,H=800,420
    lines=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    lines.append('<rect width="100%" height="100%" fill="#0d1117"/>')
    left=160; top=40; rowh=38
    for i,tag in enumerate(tags):
        if tag not in bytag: continue
        b=bytag[tag]
        if tag=='base':
            n=b[1]; p=b[0]; rate=p/n if n else 0
        else:
            n=b[3]; p=b[2]; rate=p/n if n else 0
        y=top+i*rowh
        barw=rate*560
        color='#3fb950' if rate>=0.8 else ('#d29922' if rate>=0.4 else '#f85149')
        if tag=='base': color='#58a6ff'
        lines.append(f'<text x="{left-8}" y="{y+20}" text-anchor="end" fill="#c9d1d9" font-size="12">{tag}</text>')
        lines.append(f'<rect x="{left}" y="{y+4}" width="{barw:.1f}" height="22" fill="{color}" rx="2"/>')
        lines.append(f'<text x="{left+barw+6:.1f}" y="{y+20}" fill="#8b949e" font-size="11">{p}/{n} ({rate:.2f})</text>')
    lines.append('</svg>')
    open(os.path.join(OUT,'fig6_pairwise_intervention.svg'),'w').write('\n'.join(lines))

# ---------- Figure 7: data quality / coverage ----------
def fig7():
    # scored vs unscored by env (only envs with unscored)
    uns=[r for r in env if r['pass_rate']=='']
    # judge guarantee counts overall
    from collections import Counter
    jg=Counter()
    for r in cases:
        jg[r['judge_guarantee']]+=1
    W,H=700,360
    lines=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    lines.append('<rect width="100%" height="100%" fill="#0d1117"/>')
    # pie-ish: two bars
    total=len(cases)
    scored=sum(1 for r in cases if r['status']=='scored')
    unscored=sum(1 for r in cases if r['status']!='scored')
    br=sum(1 for r in cases if r['judge_guarantee']=='behavioral_reference')
    co=sum(1 for r in cases if r['judge_guarantee']=='compile_only')
    lines.append(f'<text x="40" y="40" fill="#c9d1d9" font-size="14" font-weight="bold">Coverage: {total} selected cases</text>')
    # bar 1: scored/unscored
    lines.append(f'<text x="40" y="80" fill="#8b949e" font-size="12">scored</text>')
    lines.append(f'<rect x="120" y="66" width="{scored/total*500:.1f}" height="22" fill="#3fb950" rx="2"/>')
    lines.append(f'<text x="{120+scored/total*500+6:.1f}" y="82" fill="#c9d1d9" font-size="11">{scored}</text>')
    lines.append(f'<text x="40" y="110" fill="#8b949e" font-size="12">unscored</text>')
    lines.append(f'<rect x="120" y="96" width="{unscored/total*500:.1f}" height="22" fill="#f85149" rx="2"/>')
    lines.append(f'<text x="{120+unscored/total*500+6:.1f}" y="112" fill="#c9d1d9" font-size="11">{unscored}</text>')
    lines.append(f'<text x="40" y="160" fill="#8b949e" font-size="12">behavioral_reference</text>')
    lines.append(f'<rect x="200" y="146" width="{br/total*420:.1f}" height="22" fill="#58a6ff" rx="2"/>')
    lines.append(f'<text x="{200+br/total*420+6:.1f}" y="162" fill="#c9d1d9" font-size="11">{br}</text>')
    lines.append(f'<text x="40" y="190" fill="#8b949e" font-size="12">compile_only</text>')
    lines.append(f'<rect x="200" y="176" width="{co/total*420:.1f}" height="22" fill="#d29922" rx="2"/>')
    lines.append(f'<text x="{200+co/total*420+6:.1f}" y="192" fill="#c9d1d9" font-size="11">{co}</text>')
    lines.append('</svg>')
    open(os.path.join(OUT,'fig7_coverage.svg'),'w').write('\n'.join(lines))

fig1(); fig2(); fig3(); fig4(); fig5(); fig6(); fig7()
print('generated 7 figures')
