def solution(new_id):
    answer = ''
    s = new_id.lower()
    import re
    s = re.findall(r'[a-zA-Z0-9\.\_\-\.]', s)
    s = ''.join(i for i in [s[i] for i in range(len(s)) if s[i] != s [i-1]])
    if s == '':
        s += 'a'
    s = s.lstrip('.').rstrip('.')
    while len(s) < 3:
        s += s[-1]
    if len(s) > 15:
        s = s[0:15]
    s = s.lstrip('.').rstrip('.')
    return s 


print(solution("...!@BaT#*..y.abcdefghijklm")) #	"bat.y.abcdefghi"
print(solution("z-+.^.")) # "z--"
print(solution("=.=")) # "aaa"
print(solution("123_.def")) # "123_.def"
print(solution("abcdefghijklmn.p")) # "abcdefghijklmn"