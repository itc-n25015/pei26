ip_address = '192.168.3..1'
ip_sp1 = ip_address.split('.')
bin_exp = ''
for num in ip_sp1:
    bin_exp += bin(int(num))[2:] + '.'
print(bin_exp[:-1])