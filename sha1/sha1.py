# bits per input character. 8 - ASCII; 16 - Unicode
sha1chrsz = 8
#hex output format. 0 - lowercase; 1 - uppercase
sha1hexcase = 1
#intlen
intlenbit = 32

hex_sha1 = lambda s: binb2hex(core_sha1(str2binb(s),len(s) * sha1chrsz))
 
#Bitwise rotate a  number to the left.
rol = lambda num, cnt:\
  ((num << cnt % intlenbit) & (2**intlenbit - 1))\
  | (((num & (2**intlenbit - 1)) >> (intlenbit - cnt % intlenbit)) & (2**intlenbit - 1))
  
#Add integers, wrapping at 2^32. This uses 16-bit operations internally
def safe_add(x, y):
  lsw = (x & 0xFFFF) + (y & 0xFFFF)
  msw = (((x & (2**intlenbit - 1)) >> 16) + ((y & (2**intlenbit - 1)) >> 16)  + (lsw >> 16)) & (2**intlenbit - 1)
  return ((msw << 16) | (lsw & 0xFFFF)) & (2**intlenbit - 1)

# Perform the appropriate triplet combination function for the current iteration
def sha1_ft(t, b, c, d):
  if t < 20:
    return (b & c) | ((~b) & d)
  if t < 40:
    return b ^ c ^ d
  if t < 60:
    return (b & c) | (b & d) | (c & d)
  return b ^ c ^ d;

# Determine the appropriate additive constant for the current iteration
def sha1_kt(t):
  if t < 20:
    return 1518500249
  if t < 40:
    return 1859775393
  if t < 60:
    return -1894007588
  return -899497514

def core_sha1(x, l):
# padding
  x[l >> 5] |= 0x80 << (24 - l % intlenbit)
  x[((l + 64 >> 9) << 4) + 15] = l

  w,a,b,c,d,e,i =  {}, 1732584193, -271733879, -1732584194,  271733878, -1009589776, 0
  
  while i < len(x):
    olda, oldb, oldc, oldd, olde, j = a, b, c, d, e, 0

    while j < 80:
      if j < 16:
        w[j] = x.get(i+j,0)
      else:
        w[j] = rol(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1)
      t = safe_add(safe_add(rol(a,5), sha1_ft(j,b,c,d)), safe_add(safe_add(e, w[j]), sha1_kt(j)))
      e, d, c, b, a = d, c, rol(b,30), a, t
      j += 1
	  
    a,b,c,d,e = safe_add(a, olda),safe_add(b,oldb),safe_add(c,oldc),safe_add(d,oldd),safe_add(e,olde)
    i += 16

  return {0:a,1:b,2:c,3:d,4:e}  

# Convert an array of big-endian words to a hex string.
def binb2hex(binarray):
  if sha1hexcase == 1:
    hex_tab = "0123456789ABCDEF"
  else: 
    hex_tab = "0123456789abcdef"
  str = ""
  i = 0
  while i < len(binarray) * 4:
    str += hex_tab[(binarray[i>>2] >> ((3 - i % 4) * 8 + 4)) & 0xF] + hex_tab[(binarray[i>>2] >> ((3 - i % 4) * 8)) & 0xF]
    i+=1
  return str

# Convert an 8-bit or 16-bit string to an array of big-endian words
# In 8-bit function, characters >255 have their hi-byte silently ignored.
def str2binb(str):
  bin = {}
  mask = (1 << sha1chrsz) - 1
  i = 0
  while i < len(str) * sha1chrsz:
    ind = i >> 5
    if ind not in bin:
      bin[ind] = 0
    sdv = intlenbit - sha1chrsz - i % intlenbit
    str_c = ord(str[int(i/sha1chrsz)]) & mask
    bin[ind] |= str_c << sdv
    i+=sha1chrsz
  return bin

s = 'abc'
print(hex_sha1(s))