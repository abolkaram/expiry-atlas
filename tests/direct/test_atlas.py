from conftest import CONTRACT
def setup(vm,dep,a,b):vm.warp('2035-01-01T00:00:00+00:00');vm.sender=a;x=dep(CONTRACT);x.register('p-1','0x'+b.hex(),'Coastal works permit','Operate one bounded coastal sensor','https://authority.example/base',['Keep public readings','Preserve the declared footprint'],2051233200,7200);return x
def test_window_and_renewal(direct_vm,direct_deploy,direct_alice,direct_bob):
 x=setup(direct_vm,direct_deploy,direct_alice,direct_bob);direct_vm.warp('2035-01-01T01:10:01+00:00');x.open_renewal('p-1');direct_vm.sender=direct_bob;direct_vm.mock_web(r'authority\.example',{'status':200,'body':'Scope unchanged; all conditions met.'});direct_vm.mock_llm(r'.*ExpiryAtlas renewal check.*','{"scope_preserved":true,"conditions_met":true}');x.renew('p-1','https://authority.example/renewal',2052000000);assert x.get_permit('p-1')['state']=='RENEWED'
def test_frozen_origin(direct_vm,direct_deploy,direct_alice,direct_bob):
 x=setup(direct_vm,direct_deploy,direct_alice,direct_bob);direct_vm.warp('2035-01-01T01:10:01+00:00');x.open_renewal('p-1');direct_vm.sender=direct_bob
 with direct_vm.expect_revert('frozen authority'):x.renew('p-1','https://other.example/renewal',2052000000)
