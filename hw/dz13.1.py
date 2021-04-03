file = open('data.txt', 'r')
ans_t = open('answer.txt', 'w')
b = ''
ans = 0
znak = ''
data = file.read()

if data[-1] != ' ':
    data += ' '

for i in range(len(data)):
    if data[i].isdigit() and not data[i+1].isdigit():
        b += data[i]
        ans += int(b)
        if len(data)-2 == i:
            znak = '='
        else:
            znak = '+'
        ans_t.write(f'{b}{znak}')
        b = ''
    elif data[i].isdigit():
        b += data[i]
    if znak == '=':
        ans_t.write(str(ans))

file.close()
ans_t.close
