import json,time,secrets
from pathlib import Path
from genlayer_py import create_client,create_account
from genlayer_py.chains import studionet
R=Path(__file__).parents[1];E=(R.parents[3]/'accounts.env').read_text();key=next(x.split('=',1)[1].strip().strip('"').strip("'") for x in E.splitlines() if x.startswith('ACCOUNT_5_GENLAYER_PRIVATE_KEY='));reg=create_account(account_private_key=key);holder=create_account(account_private_key='0x'+secrets.token_hex(32));cr=create_client(chain=studionet,account=reg);ch=create_client(chain=studionet,account=holder);a='0x0DBA7BB7B4B996151CC6AfC56049db8D063735Cc';i='LIVE-'+str(int(time.time()));url='https://raw.githubusercontent.com/abolkaram/expiry-atlas/d6c1b91/evidence/renewal.txt';tx=[]
def send(cl,fn,args):
 h=cl.write_contract(address=a,function_name=fn,args=args);r=cl.wait_for_transaction_receipt(transaction_hash=h,status='FINALIZED',retries=180,interval=5000);assert r.get('status_name')=='FINALIZED';tx.append(h)
exp=int(time.time())+905;send(cr,'register',[i,holder.address,'Coastal works permit','Operate one bounded coastal sensor',url,['Keep public readings','Preserve the declared footprint'],exp,900]);time.sleep(7);send(cr,'open_renewal',[i]);send(ch,'renew',[i,url,exp+86400]);print(json.dumps({'id':i,'state':'RENEWED','transactions':tx}),flush=True)
