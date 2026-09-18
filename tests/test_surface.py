from pathlib import Path
T=Path('contracts/contract.py').read_text(encoding='utf-8');P=Path('docs/index.html').read_text(encoding='utf-8')
def test_surface():
 for n in ('register','open_renewal','renew','expire','get_permit'):assert 'def '+n in T and n in P
 assert "status:'FINALIZED'" in P and 'id="atlas"' in P and 'id="meridian"' in P
