"""Read only MCP server confined to one immutable benchmark snapshot."""
import json,sys
from pathlib import Path
ROOT=Path(sys.argv[1]).resolve()
TOOLS=[{'name':'list_files','description':'List files in the frozen benchmark repository. No other filesystem is accessible.','inputSchema':{'type':'object','properties':{},'additionalProperties':False}}, {'name':'read_file','description':'Read text from a repository file, with line numbers. Binary files cannot be read.','inputSchema':{'type':'object','properties':{'path':{'type':'string'},'start_line':{'type':'integer','minimum':1},'line_count':{'type':'integer','minimum':1}},'required':['path'],'additionalProperties':False}}]
for tool in TOOLS: tool['annotations']={'readOnlyHint':True,'destructiveHint':False,'idempotentHint':True,'openWorldHint':False}
def call(name,args):
 if name=='list_files':return '\n'.join(str(p.relative_to(ROOT)) for p in sorted(ROOT.rglob('*')) if p.is_file() and not p.is_symlink())
 if name!='read_file':raise ValueError('unknown tool')
 p=(ROOT/args['path']).resolve()
 if not p.is_relative_to(ROOT) or not p.is_file() or p.is_symlink():raise ValueError('path outside source set or not a regular file')
 data=p.read_bytes()
 if b'\0' in data:raise ValueError('binary file; not available as text')
 lines=data.decode('utf-8').splitlines();start=args.get('start_line',1);n=args.get('line_count',200)
 return '\n'.join(f'{i+1}: {line}' for i,line in enumerate(lines) if start<=i+1<start+n)
def main():
 for line in sys.stdin:
  try:
   q=json.loads(line);method=q.get('method');rid=q.get('id')
   if rid is None:continue
   if method=='initialize':result={'protocolVersion':'2024-11-05','capabilities':{'tools':{}},'serverInfo':{'name':'benchmark','version':'1'}}
   elif method=='tools/list':result={'tools':TOOLS}
   elif method=='tools/call':
    try:result={'content':[{'type':'text','text':call(q['params']['name'],q['params'].get('arguments',{}))}]}
    except Exception as e:result={'isError':True,'content':[{'type':'text','text':str(e)}]}
   elif method=='ping':result={}
   else:result={}
   print(json.dumps({'jsonrpc':'2.0','id':rid,'result':result}),flush=True)
  except Exception as e:print(str(e),file=sys.stderr,flush=True)
if __name__=='__main__':main()
