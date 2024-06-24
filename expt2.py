#!/usr/bin/python

from mininet.node import Controller, OVSSwitch
from mininet.log import setLogLevel, info
from mn_wifi.net import Mininet_wifi
from mn_wifi.cli import CLI

def myNetwork():
    net = Mininet_wifi(switch=OVSSwitch, controller=Controller)

    info('* Adding controller\n')
    net.addController('c0')

    info('* Add switches/APs\n')
    ap1 = net.addAccessPoint('ap1', mode='g', position='350.0,207.0,0', range='500')
    ap2 = net.addAccessPoint('ap2', mode='g', position='487.0,208.0,0', range='500')

    info('* Add hosts/stations\n')
    sta1 = net.addStation('sta1', position='255.0,361.0,0', range='300')
    sta2 = net.addStation('sta2', position='347.0,360.0,0', range='300')
    sta3 = net.addStation('sta3', position='471.0,360.0,0', range='300')
    sta4 = net.addStation('sta4', position='563.0,360.0,0', range='300')

    net.configureWifiNodes()

    info('* Add links\n')
    net.addLink(ap1, ap2)
    net.addLink(ap1, sta1)
    net.addLink(ap1, sta2)
    net.addLink(ap2, sta3)
    net.addLink(ap2, sta4)

    net.plotGraph(max_x=1000, max_y=1000)
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()
