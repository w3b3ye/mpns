def find_proto(proto):
    protolist = ['SSH', 'HTTP', 'SNMP']

    try:
        pos = protolist.index(proto)
        print(f"{proto} found at  {pos}")
    except:
        print(f"{proto} not in the list.")

find_proto('SNMP')
find_proto('Telnet')