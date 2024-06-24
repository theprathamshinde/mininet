#!/usr/bin/python

from mininet.node import Controller, OVSSwitch
from mininet.log import setLogLevel, info
from mn_wifi.net import Mininet_wifi
from mn_wifi.cli import CLI
import subprocess

def start_wireshark(interface):
    # Start Wireshark to capture traffic on the specified interface
    command = ['wireshark', '-i', interface]
    try:
        subprocess.Popen(command)
    except FileNotFoundError:
        info('Wireshark not found. Please ensure Wireshark is installed and in your PATH.\n')

def myNetwork():
    net = Mininet_wifi(switch=OVSSwitch, controller=Controller)
    
    info('* Adding controller\n')
    net.addController('c0')
    
    info('* Add switches/APs\n')
    ap1 = net.addAccessPoint('ap1', mode='g', position='358.0,127.0,0', range='300')
    ap2 = net.addAccessPoint('ap2', mode='g', position='443.0,123.0,0', range='300')
    
    info('* Add hosts/stations\n')
    sta1 = net.addStation('sta1', position='278.0,241.0,0', range='300')
    sta2 = net.addStation('sta2', position='368.0,248.0,0', range='300')
    sta3 = net.addStation('sta3', position='453.0,252.0,0', range='300')
    sta4 = net.addStation('sta4', position='520.0,250.0,0', range='300')
    
    info('* Configuring wifi nodes\n')
    net.configureWifiNodes()
    
    info('* Add links\n')
    net.addLink(ap1, ap2)
    net.addLink(ap1, sta1)
    net.addLink(ap1, sta2)
    net.addLink(ap2, sta3)
    net.addLink(ap2, sta4)
    
    net.plotGraph(max_x=1000, max_y=1000)
    net.start()
    
    interface = 'ap1-wlan1'
    start_wireshark(interface)
    
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()
