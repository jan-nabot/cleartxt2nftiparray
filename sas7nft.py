#!/usr/bin/python3

sourcepath = 'pinput'
destpath = '/var/ipss4nft'
setname = 'ipss'

def main():
    inp = open(sourcepath)
    out = open(destpath, 'w')
    out.write('define ' + setname.strip() + ' = { ')
    
    for line in inp:
        ips = line.split()[1:]
        for ip in ips:
            out.write(ip + ', ')
    
    out.seek(out.tell() -2)
    out.write(' }\n')
    inp.close()
    out.close()
    with open(destpath) as out:
        for line in out:
            print(line)
    return 0
        
main()
    
