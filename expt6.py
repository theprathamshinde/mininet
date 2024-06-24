#!/usr/bin/python

import sys
from mininet.node import Controller
from mininet.log import setLogLevel, info
from mn_wifi.net import Mininet_wifi
from mn_wifi.cli import CLI

def myNetwork():
    net = Mininet_wifi()
    
    info('* Adding controller\n')
    net.addController('c0')
    
    info('* Add switches/APs\n')
    ap1 = net.addAccessPoint('ap1', ssid='ap1-ssid', channel='1', mode='g', position='377.0,100.0,0')
    ap2 = net.addAccessPoint('ap2', ssid='ap2-ssid', channel='1', mode='g', position='453.0,101.0,0')
    ap3 = net.addAccessPoint('ap3', ssid='ap3-ssid', channel='1', mode='g', position='527.0,102.0,0')
    
    info('* Add hosts/stations\n')
    sta1 = net.addStation('sta1', position='217.0,242.0,0')
    sta2 = net.addStation('sta2', position='303.0,241.0,0')
    sta3 = net.addStation('sta3', position='387.0,246.0,0')
    sta4 = net.addStation('sta4', position='462.0,247.0,0')
    sta5 = net.addStation('sta5', position='568.0,235.0,0')
    sta6 = net.addStation('sta6', position='643.0,235.0,0')
    
    info("* Configuring Propagation Model\n")
    net.setPropagationModel(model="logDistance", exp=3)
    
    info("* Configuring wifi nodes\n")
    net.configureWifiNodes()
    
    info('* Add links\n')
    net.addLink(ap1, ap2)
    net.addLink(ap2, ap3)
    
    net.plotGraph(max_x=1000, max_y=1000)
    net.pingAll()
    
    net.startMobility(time=0)
    net.mobility(sta1, 'start', time=1, position='217.0,242.0,0')
    net.mobility(sta2, 'start', time=2, position='303.0,241.0,0')
    net.mobility(sta3, 'start', time=3, position='387.0,246.0,0')
    net.mobility(sta4, 'start', time=4, position='462.0,247.0,0')
    net.mobility(sta5, 'start', time=5, position='568.0,235.0,0')
    net.mobility(sta6, 'start', time=6, position='643.0,235.0,0')
    net.mobility(sta1, 'stop', time=11, position='655.0,235.0,0')
    net.mobility(sta2, 'stop', time=12, position='655.0,235.0,0')
    net.mobility(sta3, 'stop', time=13, position='655.0,235.0,0')
    net.mobility(sta4, 'stop', time=14, position='655.0,235.0,0')
    net.mobility(sta5, 'stop', time=15, position='255.0,242.0,0')
    net.mobility(sta6, 'stop', time=16, position='217.0,242.0,0')
    net.stopMobility(time=18)
    
    net.start()
    info('* Post configure nodes\n')
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()
