#           ------------------ :   STRING ENCODING FUNCTIONS  : ---------------                     #

#  1. ENCODE : ------------

s = "PythÖn"
r = s.encode('ascii')
print(r)
r = s.encode('ascii', 'ignore')
print(r)
r = s.encode('ascii', 'replace')
print(r)
r = s.encode('ascii', 'strict')
print(r)

#  2. ZFILL : -----------

s = 'Hello'
r = s.zfill(10)
print(r)
s= '123'
r = s.zfill(10)
print(r)
s = '-120'
r= s.zfill(5)
print(r)

# 3. JOIN : ---------

s = {'1','2','3','4','5'}
sep = '->'
r = sep.join(s)
print(r)

s = ('1','2','3','4','5')
sep = '-'
r = sep.join(s)
print(r)
print(type(r))

#  MAKETRANS : --------
# TRANSTALE :---------
fs = 'abc'
ss = 'def'
table = fs.maketrans(fs,ss)


print('ba'.translate(table))