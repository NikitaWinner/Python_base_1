from pprint import pprint
def pars(line: str) -> tuple:
    ls = line.split(' ')
    return ls[0], ls[5][1:4], ls[6]


list_out = list()
with open('nginx_logs.txt' , 'r', encoding= 'utf-8') as tx:
    for line in tx:
        list_out.append(pars(line))
pprint(list_out)