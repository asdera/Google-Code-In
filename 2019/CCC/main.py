from math import *
from copy import *
from itertools import *

gates = []

class Gate:
  def __init__(self, ss, p):
    self.ss = ss
    self.p = p

pens = []

class Pen:
  def __init__(self, m, s):
    self.ii = m
    self.ga = []
    self.co = []
    self.w = []
    self.t = False
    x = [int(i) for i in s.split()]
    a = x.pop(0)
    c = x[:a]
    d = x[a:]
    for i, e in enumerate(c):
      ss = "".join(list(map(str, sorted([c[(i+1)%a]] + [e]))))
      p = d[i]
      oa = Gate(ss, p)
      self.ga.append(oa)


def compare(a, b):
  for i in a.ga:
    for j in b.ga:
      if i.ss == j.ss:
        a.co.append(b)
        a.w.append(i.p)
        b.co.append(a)
        b.w.append(i.p)




mmm = int(input())

for m in range(mmm):
  pens.append(Pen(m, input()))

for a, b in combinations(pens, 2):
  compare(a, b)

for i in pens:
  for h, x in enumerate(i.co):
    pass

lll = pens.pop(0)
lll.t = True
ccc = lll.co
www = lll.w
ccin = 0
gud = [lll.ii]

while mmm > 0:
  cin = min(www)
  kill = ccc[www.index(cin)]
  gud.append(kill.ii)
  for i, e in reversed(list(enumerate(kill.co))):
    if e.ii not in gud:
      ccc.append(e)
      www.append(kill.w[i])
  for i, e in reversed(list(enumerate(ccc))):
    if e.ii == kill.ii:
      ccc.pop(i)
      www.pop(i)
      mmm -= 1
  ccin += cin

print(ccin)
  









