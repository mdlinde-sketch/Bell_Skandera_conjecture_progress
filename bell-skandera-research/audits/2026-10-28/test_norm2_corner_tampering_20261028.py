"""Adversarial checks for the independent 28 October corner certificate."""
import copy
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from norm2_corner_certificate_20261028 import check_file


def run():
    original=json.loads(Path('norm2_special_cases_degree17_20261024.json').read_text())
    with TemporaryDirectory() as directory:
        path=Path(directory)/'tampered.json'
        assert check_file(Path('norm2_special_cases_degree17_20261024.json'))['rows']==37
        for i in range(5):
            obj=copy.deepcopy(original)
            if i==0:obj['suspect'].pop()
            if i==1:obj['suspect'][0][1]+=1
            if i==2:obj['suspect'][0][2]+=1
            if i==3:obj['suspect'][0][3]=2
            if i==4:obj['degree']=16
            path.write_text(json.dumps(obj))
            try:check_file(path)
            except (AssertionError,KeyError,ValueError):pass
            else:raise AssertionError(f'Corrupted certificate {i} was accepted')
    print('PASS five deliberate case-list corruptions rejected')

if __name__=='__main__':run()
