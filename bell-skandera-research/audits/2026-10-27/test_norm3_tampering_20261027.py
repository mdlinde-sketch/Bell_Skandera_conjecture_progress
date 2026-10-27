"""Adversarial input controls for the 27 Oct norm-three certificate."""
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from norm3_rational_obstruction_20261027 import check


def test():
    with TemporaryDirectory() as tmp:
        root=Path(tmp)
        originals={}
        for d in range(14,18):
            filename=f'frontier_checked_d{d}_20261025.json'
            originals[filename]=json.loads(Path(filename).read_text())
            (root/filename).write_text(json.dumps(originals[filename]))
        # Baseline control, then 5 distinct certificate corruptions.
        check(root)
        mutations=[
            (17, lambda a:a['suspect'].pop()),
            (17, lambda a:a['suspect'][0].__setitem__(3,4)),
            (16, lambda a:a['suspect'][0].__setitem__(4,999)),
            (15, lambda a:a['suspect'][0].__setitem__(0,10)),
            (14, lambda a:a['suspect'][0].__setitem__(2,100)),
        ]
        for d,mutate in mutations:
            filename=f'frontier_checked_d{d}_20261025.json'
            corrupted=json.loads(json.dumps(originals[filename]))
            mutate(corrupted)
            (root/filename).write_text(json.dumps(corrupted))
            try:
                check(root)
            except AssertionError:
                print('REJECTED',d,mutate.__code__.co_consts)
            else:
                raise AssertionError('Failed to reject corrupted input')
            (root/filename).write_text(json.dumps(originals[filename]))
    print('PASS 5 adversarial corruptions rejected')


if __name__=='__main__':test()
