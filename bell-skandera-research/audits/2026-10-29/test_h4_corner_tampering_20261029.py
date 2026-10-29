"""29 Oct: five deliberately corrupted norm-one case lists must be rejected."""
import copy,json
from pathlib import Path
from tempfile import TemporaryDirectory
from h4_monotone_corner_certificate_20261029 import verify

def test():
    source=json.loads(Path('frontier_checked_d17_20261025.json').read_text())
    assert len(source['residual'])==2142 and len(source['suspect'])==37
    with TemporaryDirectory() as folder:
        path=Path(folder)/'tampered.json'
        for i in range(5):
            x=copy.deepcopy(source)
            if i==0:x['residual'].pop()
            if i==1:x['residual'][0][1]+=1
            if i==2:x['suspect'][0][2]+=1
            if i==3:x['degree']=16
            if i==4:x['suspect'].append(x['suspect'][0])
            path.write_text(json.dumps(x))
            try:verify(path)
            except (AssertionError,KeyError,ValueError):pass
            else:raise AssertionError('Tamper accepted: '+str(i))
    print('PASS 5 deliberately corrupted norm-one frontier case lists rejected')

if __name__=='__main__':test()
