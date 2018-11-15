import sys
inFile = sys.argv[1]

with open(inFile, 'r') as ip:
    data = ip.readlines()
    data = [x.replace('\n', '').strip() for x in data]
    data = [x for x in data if x]

def count_at_begin(sentence, char):
    count = 0
    for x in sentence:
        if x==char:
            count +=1
        else:
            break
    return count   

def find_next_valid_line(i, len_data):
    for x in data[i+1 : len_data - 1]:
        if x[0] == '*':
            return x
        elif x[0] == '.':
            return x
        else:
            continue


star_op = []
star_ip = [0]

l = []

for i in range(0,len(data)):
    try:
        if data[i][0] == '.':
            no_of_dots = count_at_begin(data[i], '.')
            nextline_no_of_dots = count_at_begin(find_next_valid_line(i, len(data)), '.') if i < len(data)-1 else 0
            if no_of_dots < nextline_no_of_dots:
                l.append(' '*no_of_dots + '+ ' + data[i].lstrip('.* ')+'\n')
            else:
                l.append(' '*no_of_dots + '- ' + data[i].lstrip('.* ')+'\n')
        elif data[i][0] not in ['*', '.']:
            if data[i-1].startswith('.'):
                PNOD = count_at_begin(data[i-1], '.') + 2
                l.append(' '*PNOD + data[i].lstrip('.')+'\n')
            else:
                PNOS = count_at_begin(data[i-1], ' ') + 2
                l.append(' '*PNOS + data[i].lstrip('.* ') + '\n')
        elif data[i][0] in ['*']:
            no_of_stars = count_at_begin(data[i], '*')
            while len(star_ip)< no_of_stars:
                star_ip.append(0)
            while no_of_stars < len(star_ip):
                star_ip.pop()
            star_ip[-1] += 1
            star_op.append('.'.join(map(str, star_ip)))
            l.append(star_op[-1]+' ' + data[i].lstrip('.* ') + '\n')            
    except Exception as e:
        print('Exception is :: ', e)

for i in l:
  sys.stdout.write(i)
        
        
        
        

