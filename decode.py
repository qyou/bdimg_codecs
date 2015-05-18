__author__ = 'qyou'

marks = {
    '_z&e3B': '.',
    'AzdH3F': '/',
    '_z2C$q': ':',
        }
dictionary = {
    'o': 'w',
    'v': 'c',
    'g': 'n',
    '5': 'o',
    '4': 'm',
    'i': 'h',
    'p': 't',
    'r': 'p',
    'j': 'e',
    'f': 's',
    '8': '1',
    '0': '7',
    'l': '9',
    'x': 'x',
    't': 'i',
    'z': 'z',
    'w': 'a',
    '2': 'g',
    '7': 'u',
    'g': 'n',
    'b': '8',
    '6': 'r',
    'k': 'b',
    'c': '5',
    'm': '6',
    'y': 'y',
    'n': '3',
    'q': 'q',
    '1': 'd',
    'a': '0',
    'u': 'f',
    '3': 'j',
    's': 'l',
    'e': 'v',
    '9': '4',
    'd': '2',
    'h': 'k'
}

import string
encode_str = string.digits + string.lowercase
decode_str = ''
for letter in encode_str:
    decode_str += dictionary[letter]
print encode_str
print decode_str
trans = string.maketrans(encode_str, decode_str)


import json

json_path = r'rwh.json'

with open(json_path, 'r') as fin:
    json_obj = json.load(fin, encoding='GBK')
    data_list =  json_obj['data']
    encodeURLs = []
    for data in data_list:
        encodeURLs.append(data['objURL'])
        encodeURLs.append(data['fromURL'])
        

filepath = r'result.txt'        
fout = open(filepath, 'w+')

for encodeURL in encodeURLs:
    print >> fout, encodeURL
    for k, v in marks.iteritems():
        encodeURL = encodeURL.replace(k, v)
    print >> fout, encodeURL
    print >> fout, encodeURL.__str__().translate(trans)
    print >> fout, '\n'
    
fout.close()
