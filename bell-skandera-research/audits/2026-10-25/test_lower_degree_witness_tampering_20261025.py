"""Adversarial negative controls for the degree-16 untrusted frontier witness."""
import gzip,json,subprocess,sys,tempfile
from pathlib import Path

source=Path('frontier_cover_d16_20261025.jsonl.gz')
with gzip.open(source,'rt') as f:
    rows=[json.loads(line) for line in f]

def expect_rejection(name,modified):
    with tempfile.TemporaryDirectory() as tmp:
        p=Path(tmp)/'bad.jsonl.gz'
        with gzip.open(p,'wt') as out:
            for row in modified:out.write(json.dumps(row)+'\n')
        proc=subprocess.run([sys.executable,'frontier_checker_all_degrees_20261025.py',str(p),'16'],capture_output=True,text=True)
        assert proc.returncode!=0,(name,proc.stdout)
        print('REJECTED',name)

expect_rejection('missing interval',rows[1:])
expect_rejection('duplicated interval',rows[:1]+rows)
for original,new_kind,name in [(0,1,'false trace for no-pair'),(1,0,'false no-pair for trace'),(2,0,'false no-pair for singleton')]:
    modified=[r.copy() for r in rows]
    i=next(i for i,r in enumerate(modified) if r[3]==original)
    modified[i][3]=new_kind
    expect_rejection(name,modified)
modified=[r.copy() for r in rows]
modified[0][1]+=1
expect_rejection('boundary shift',modified)
print('PASS six adversarial witness corruptions rejected')
