#!/usr/bin/env python3

import os
from marvis import ArgumentParser, Network, DockerNode, InterfaceNode, ExternalNode, SwitchNode, Scenario

def main():
    scenario = Scenario()

    net = Network("10.116.115.0", "255.255.255.0")
    bridge = SwitchNode('br-1')



    node1 = DockerNode('ping', docker_build_dir='./docker/ping')
    channel1 = net.create_channel('channel1',delay='10ms')
    channel1.connect(node1)
    channel1.connect(bridge)

    #node2 = DockerNode('pong', docker_build_dir='./docker/pong')
    node2 = InterfaceNode('pong', ifname='eth0')
    #node2 = ExternalNode('pong', bridge='ns3-ping', ifname='eth0')

    #ip link add name ns3-ping type bridge
    #ip link set dev ns3-ping up
    #ip link set dev eth0 master ns3-ping

    channel2 = net.create_channel('channel2',delay='50ms')
    #channel2.connect(node2)
    channel2.connect(node2, '192.168.2.206')

    channel2.connect(bridge)

    #emily = ExternalNode('emily',bridge='ns3-ping', ifname='enp3s0.116');
    #channel1 = net.create_channel('channel1',delay='10ms')
    #channel1.connect(emily,'10.116.115.53')
    #channel1.connect(bridge)



    #def make_node(name,ports=None):
    #    return DockerNode(f'{name}',
    #        docker_image='prellblock-trdp-benchmarking-test',
    #        command=f'/app/start_node.sh -n {name} -i eth0',
    #        exposed_ports=ports
    #    )

    


    #james = make_node('james',{9002:9002})
    #channel2 = net.create_channel('channel2',delay='10ms')
    #channel2.connect(james)
    #channel2.connect(bridge)

#    @scenario.workflow
#    def insert_value(workflow):
#        while True:
#            workflow.sleep(2)
#            node1.execute_command('/app/target/release/prellblock-client config/temperature-1/temperature-1.key thomas:3130 set temp 100')


    scenario.add_network(net)
    with scenario as sim:
        sim.simulate(simulation_time=60)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.run(main)
