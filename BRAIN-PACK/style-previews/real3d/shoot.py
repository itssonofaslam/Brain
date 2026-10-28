import sys,time,subprocess,threading,http.server,socketserver,os
from playwright.sync_api import sync_playwright
w=int(sys.argv[1]) if len(sys.argv)>1 else 640
os.chdir('/home/claude/stickman/style-previews/real3d')
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
srv=socketserver.TCPServer.allow_reuse_address=True
srv=socketserver.TCPServer(('127.0.0.1',8791),Q); threading.Thread(target=srv.serve_forever,daemon=True).start()
with sync_playwright() as pw:
    br=pw.chromium.launch(args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'])
    pg=br.new_page(viewport={'width':w,'height':round(w*9/16)})
    pg.on('console',lambda m:print('console:',m.text[:300]))
    pg.on('pageerror',lambda e:print('err:',str(e)[:400]))
    t=time.time(); pg.goto(f'http://127.0.0.1:8791/render3d.html?w={w}')
    try:
        pg.wait_for_function('window.DONE===true || window.ERR',timeout=500000)
    except Exception as e: print('timeout',e)
    print('err',pg.evaluate('window.ERR||null'),'t',round(time.time()-t,1))
    pg.locator('#c').screenshot(path=f'raw_{w}.png'); br.close()
