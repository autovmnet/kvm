from __future__ import print_function
import sys
import libvirt
from xml.dom import minidom

domName = 'test'

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

dom = conn.lookupByName(domName)
if dom == None:
    print('Failed to find the domain '+domName, file=sys.stderr)
    exit(1)

flag = dom.isActive()


conn.close()
exit(0)
