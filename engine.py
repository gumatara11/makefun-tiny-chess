import json,os,random,sys,urllib.request as w
E=os.environ.get("MAKEFUN_ENV_URL")or sys.exit("x")
V=[0,100,320,330,500,900,20000]
A=[-33,-31,-18,-14,14,18,31,33]
K=[-17,-16,-15,-1,1,15,16,17]
B=[-17,-15,15,17]
R=[-16,-1,1,16]
M=100000
F=["::::;<<6;98::::>;;<?<<>@DDDD::::","024426:;4;<=4:=>4;=>4:<=26::0244","68888;::8<<<8:<<8;;<8:;<8:::6888",":::;9:::9:::9:::9:::9:::;<<<::::","68898:;:8;;;::;;9:;;8:;;8:::6889",">@<:>>::866664424220422042204220"]
T=[[0]*128 for _ in range(7)]
for t,s in enumerate(F):
 for q in range(128):
  if q&136:continue
  r,f=q>>4,q&7
  if f>3:f=7-f
  T[t+1][q]=(ord(s[r*4+f])-58)*5
g=random.Random(20261113)
Z=[[g.getrandbits(64) for _ in range(128)] for _ in range(13)]
Y=g.getrandbits(64)
C=[g.getrandbits(64) for _ in range(16)]
P=[g.getrandbits(64) for _ in range(8)]
class X(Exception):pass
b=[0]*128;s=1;c=0;e=-1;h=0;z=0;W=4;J=116;T2={};N=0;L=80000;G=[];Q=[];C2=0
def F2(f):
 global b,s,c,e,h,z,W,J,Q,C2
 p=f.split();b=[0]*128;W=J=-1
 for i,r in enumerate(p[0].split("/")):
  q=(7-i)*16;u=0
  for a in r:
   if a.isdigit():u+=int(a)
   else:
    t="PNBRQK".index(a.upper())+1
    if a.islower():t=-t
    b[q+u]=t
    if t==6:W=q+u
    elif t==-6:J=q+u
    u+=1
 s=1 if p[1]=="w" else -1;c=0
 if len(p)>2:
  for a in p[2]:
   if a=="K":c|=1
   elif a=="Q":c|=2
   elif a=="k":c|=4
   elif a=="q":c|=8
 e=-1
 if len(p)>3 and p[3]!="-":e=(ord(p[3][1])-49)*16+(ord(p[3][0])-97)
 h=int(p[4]) if len(p)>4 else 0
 z=0;C2=0
 for q in range(128):
  if q&136:continue
  if b[q]:z^=Z[b[q]+6][q]
  if b[q] and 2<=abs(b[q])<=5:C2+=1
 if s==-1:z^=Y
 z^=C[c]
 if e!=-1:z^=P[e&7]
 Q=[]
def a(q,y):
 if y:
  for d in(-15,-17):
   t=q+d
   if 0<=t<128 and not t&136 and b[t]==1:return 1
 else:
  for d in(15,17):
   t=q+d
   if 0<=t<128 and not t&136 and b[t]==-1:return 1
 for d in A:
  t=q+d
  if 0<=t<128 and not t&136 and b[t]==(2 if y else -2):return 1
 for d in K:
  t=q+d
  if 0<=t<128 and not t&136 and b[t]==(6 if y else -6):return 1
 for d in B:
  t=q+d
  while 0<=t<128 and not t&136:
   p=b[t]
   if p:
    if p==(3 if y else -3)or p==(5 if y else -5):return 1
    break
   t+=d
 for d in R:
  t=q+d
  while 0<=t<128 and not t&136:
   p=b[t]
   if p:
    if p==(4 if y else -4)or p==(5 if y else -5):return 1
    break
   t+=d
 return 0
def m(o):
 r=[]
 for q in range(128):
  if q&136:continue
  p=b[q]
  if not p or(p>0)!=(s>0):continue
  t=abs(p)
  if t==1:
   d=16 if p>0 else -16;u=1 if p>0 else 6;l=7 if p>0 else 0;v=q+d
   if b[v]==0:
    if(v>>4)==l:
     for k in(5,4,3,2):r.append(q|(v<<7)|(k<<14))
    else:
     if not o:
      r.append(q|(v<<7))
      if(q>>4)==u:
       x=q+2*d
       if b[x]==0:r.append(q|(x<<7))
     elif(v>>4)==l:
      for k in(5,4,3,2):r.append(q|(v<<7)|(k<<14))
   for j in(d-1,d+1):
    v=q+j
    if v&136 or v<0 or v>=128:continue
    y=b[v]
    if y and(y>0)!=(p>0):
     if(v>>4)==l:
      for k in(5,4,3,2):r.append(q|(v<<7)|(k<<14))
     else:r.append(q|(v<<7))
    elif v==e and e!=-1:r.append(q|(v<<7))
  elif t==2 or t==6:
   for d in A if t==2 else K:
    v=q+d
    if v&136 or v<0 or v>=128:continue
    y=b[v]
    if not y:
     if not o:r.append(q|(v<<7))
    elif(y>0)!=(p>0):r.append(q|(v<<7))
  else:
   for d in B if t==3 else R if t==4 else K:
    v=q+d
    while not(v&136)and 0<=v<128:
     y=b[v]
     if not y:
      if not o:r.append(q|(v<<7))
     else:
      if(y>0)!=(p>0):r.append(q|(v<<7))
      break
     v+=d
 if not o:
  if s>0:
   if c&1 and b[5]==0 and b[6]==0 and b[7]==4 and b[4]==6 and not a(4,0)and not a(5,0)and not a(6,0):r.append(4|(6<<7))
   if c&2 and b[3]==0 and b[2]==0 and b[1]==0 and b[0]==4 and b[4]==6 and not a(4,0)and not a(3,0)and not a(2,0):r.append(4|(2<<7))
  else:
   if c&4 and b[117]==0 and b[118]==0 and b[119]==-4 and b[116]==-6 and not a(116,1)and not a(117,1)and not a(118,1):r.append(116|(118<<7))
   if c&8 and b[115]==0 and b[114]==0 and b[113]==0 and b[112]==-4 and b[116]==-6 and not a(116,1)and not a(115,1)and not a(114,1):r.append(116|(114<<7))
 return r
def d(n):
 global s,c,e,h,z,W,J,C2
 f=n&127;t=(n>>7)&127;k=(n>>14)&7;p=b[f];v=b[t];x=t
 if abs(p)==1 and t==e and e!=-1:x=t-16 if p>0 else t+16;v=b[x]
 u=(v,x,c,e,h,z,W,J,C2)
 if v and 2<=abs(v)<=5:C2-=1
 if k:C2+=1
 z^=Z[p+6][f]
 if v:z^=Z[v+6][x]
 z^=C[c]
 if e!=-1:z^=P[e&7]
 b[f]=0;q=p
 if k:q=k if p>0 else -k
 b[t]=q;z^=Z[q+6][t]
 if x!=t:b[x]=0
 if abs(p)==6 and abs(t-f)==2:
  if t>f:j,l=f+3,f+1
  else:j,l=f-4,f-1
  o=b[j];b[j]=0;b[l]=o;z^=Z[o+6][j]^Z[o+6][l]
  if p>0:W=t
  else:J=t
 elif abs(p)==6:
  if p>0:W=t
  else:J=t
 if abs(p)==6:c&=~3 if p>0 else ~12
 if f==0 or t==0:c&=~2
 if f==7 or t==7:c&=~1
 if f==112 or t==112:c&=~8
 if f==119 or t==119:c&=~4
 z^=C[c];e=-1
 if abs(p)==1 and abs(t-f)==32:e=(f+t)//2;z^=P[e&7]
 h=0 if abs(p)==1 or v else h+1
 z^=Y;s=-s;Q.append(z)
 return u
def u(n,o):
 global s,c,e,h,z,W,J,C2
 v,x,c,e,h,z,W,J,C2=o
 Q.pop()
 f=n&127;t=(n>>7)&127;k=(n>>14)&7
 p=b[t]
 if k:p=1 if p>0 else -1
 b[f]=p;b[t]=0
 if v:b[x]=v
 if abs(p)==6 and abs(t-f)==2:
  if t>f:j,l=f+3,f+1
  else:j,l=f-4,f-1
  b[j]=b[l];b[l]=0
 s=-s
def dn():
 global s,e,h,z
 o=(e,h,z)
 z^=Y
 if e!=-1:z^=P[e&7]
 e=-1;h+=1;s=-s;Q.append(z)
 return o
def un(o):
 global s,e,h,z
 e,h,z=o;Q.pop();s=-s
def l(o):
 r=[]
 for n in m(o):
  u2=d(n);j=W if s==-1 else J
  if not a(j,s==1):r.append(n)
  u(n,u2)
 return r
def v():
 t=0
 for q in range(128):
  if q&136:continue
  p=b[q]
  if not p:continue
  if p>0:t+=V[p]+T[p][q]
  else:t-=V[-p]+T[-p][q^119]
 return t if s==1 else -t
def o(n,y,p):
 def f2(n):
  if n==y:return 1<<20
  f=n&127;e2=(n>>7)&127;v=b[e2]
  if v:return 10000+V[abs(v)]*10-V[abs(b[f])]//10
  k=(n>>14)&7
  if k:return 9000+V[k]
  return 0
 n.sort(key=f2,reverse=True)
 return n
def q(al,be,p):
 global N
 N+=1
 if N>=L:raise X
 if h>=100:return 0
 t=v()
 if t>=be:return be
 if t>al:al=t
 i=a(W if s==1 else J,s==-1)
 if i:
  r=l(0)
  if not r:return -M+p
 else:r=l(1)
 o(r,0,p)
 for n in r:
  u2=d(n);x=-q(-be,-al,p+1);u(n,u2)
  if x>=be:return be
  if x>al:al=x
 return al
def r(dp,al,be,p):
 global N
 N+=1
 if N>=L:raise X
 if h>=100:return 0
 if Q.count(z)>1 or z in G:return 0
 i=a(W if s==1 else J,s==-1)
 y=T2.get(z)
 if y and y[0]>=dp:
  if y[1]==0:return y[2]
  if y[1]==1 and y[2]>=be:return y[2]
  if y[1]==2 and y[2]<=al:return y[2]
  t=y[3]
 else:t=0
 if dp<=0:return q(al,be,p)
 if dp>=3 and not i and C2 and be<M-1000:
  o2=dn();x=-r(dp-4,-be,-be+1,p+1);un(o2)
  if x>=be:return be
 n=l(0)
 if not n:return -M+p if i else 0
 o(n,t,p)
 w=-M;g=n[0];f=2
 for j,m2 in enumerate(n):
  u2=d(m2)
  if j==0:x=-r(dp-1,-be,-al,p+1)
  elif j>=3 and dp>=3 and not i and not u2[0] and not(m2>>14):
   x=-r(dp-2,-al-1,-al,p+1)
   if al<x<be:x=-r(dp-1,-be,-al,p+1)
  else:
   x=-r(dp-1,-al-1,-al,p+1)
   if al<x<be:x=-r(dp-1,-be,-al,p+1)
  u(m2,u2)
  if x>w:w=x;g=m2
  if x>al:al=x;f=0
  if al>=be:f=1;break
 if len(T2)>=300000:T2.clear()
 T2[z]=(dp,f,w,g)
 return w
def t(l2,f):
 global N
 N=0
 y=l2[0];o2={}
 for dp in range(1,20):
  try:
   o3=sorted(l2,key=lambda n:o2.get(n,0),reverse=True)
   a2=-M;g=o3[0];o4={}
   for j,m2 in enumerate(o3):
    u2=d(m2)
    if j==0:x=-r(dp-1,-M,-a2,1)
    else:
     x=-r(dp-1,-a2-1,-a2,1)
     if a2<x<M:x=-r(dp-1,-M,-a2,1)
    u(m2,u2)
    o4[m2]=x
    if x>a2:a2=x;g=m2
   y=g;o2=o4
   if a2>=M-1000:break
  except X:break
 F2(f)
 return y
def i(x):
 f=(ord(x[1])-49)*16+(ord(x[0])-97)
 t=(ord(x[3])-49)*16+(ord(x[2])-97)
 k=0
 if len(x)==5:k={"n":2,"b":3,"r":4,"q":5}[x[4]]
 return f|(t<<7)|(k<<14)
def j(n):
 f=n&127;t=(n>>7)&127;k=(n>>14)&7
 s2=chr(97+(f&7))+chr(49+(f>>4))+chr(97+(t&7))+chr(49+(t>>4))
 if k:s2+="nbrq"[k-2]
 return s2
def p(q,B2):
 r=w.Request(E+q,data=json.dumps(B2).encode(),headers={"content-type":"application/json"})
 try:
  with w.urlopen(r) as s2:return json.load(s2)
 except Exception as e:sys.exit(q+": "+str(e))
def main():
 n=-1
 while 1:
  g=p("/game",{})
  if g["status"]=="done":break
  while g["status"]=="your_move":
   if g["game"]!=n:n=g["game"];del G[:]
   f=g["fen"];F2(f);G.append(z)
   y=[i(u2) for u2 in g["legal_moves"]]
   m2=t(y,f)
   u2=d(m2);G.append(z);u(m2,u2)
   g=p("/move",{"game":g["game"],"move":j(m2)})
  print("game "+str(g["game"])+": "+str(g["outcome"])+" by "+str(g["reason"]),file=sys.stderr)
 print("done: "+str(g.get("wins"))+" won, "+str(g.get("draws"))+" drawn, "+str(g.get("losses"))+" lost",file=sys.stderr)
if __name__=="__main__":main()
