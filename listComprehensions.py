#listComprehensions 列表生成式
list(range(1, 11))

[x * x for x in range(1, 11) if x % 2 == 0]

[m + n + l for m in 'xyz' for n in 'ABC' for l in 'jkl']

import os
[d for d in os.listdir('\\.')]

d={'x':'A','y':'B','z':'c'}
[k + '=' + v for k,v in d.items()]

L=['HIASH','Kjafio','asjdf','jHfjkHajsHOJDKj',123]
[l.lower() for l in L if isinstance(l,str)]