#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch, Host
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def myNetwork():
    net = Mininet(switch=OVSKernelSwitch, controller=Controller)
    
    info('* Adding controller\n')
    net.addController('c0')
    
    info('* Add switches\n')
    s5 = net.addSwitch('s5')
    s6 = net.addSwitch('s6')
    s7 = net.addSwitch('s7')
    
    info('* Add hosts\n')
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')
    h5 = net.addHost('h5')
    h6 = net.addHost('h6')
    
    info('* Add links\n')
    net.addLink(h1, s5)
    net.addLink(h2, s5)
    net.addLink(h3, s6)
    net.addLink(h4, s6)
    net.addLink(h5, s7)
    net.addLink(h6, s7)
    net.addLink(s5, s6)
    net.addLink(s6, s7)
    
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()
