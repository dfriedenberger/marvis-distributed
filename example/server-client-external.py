#!/usr/bin/env python3

import os
from marvis import ArgumentParser, Network, DockerNode, InterfaceNode, ExternalNode, SwitchNode, Scenario
from remote import Device
def main():
    scenario = Scenario()

    net = Network("10.116.115.0", "255.255.255.0")
    bridge = SwitchNode('br-1')

    device = Device('192.168.2.206', username = 'pirate')
    device.transfer('./docker/simple-server','/home/pirate/marvis')
    device.build_docker('simple-server','/home/pirate/marvis/simple-server')
    device.run_docker('simple-server','marvis-simple-server')
    

    node1 = DockerNode('client', docker_build_dir='./docker/curl-client')
    channel1 = net.create_channel('channel1',delay='10ms')
    channel1.connect(node1)
    channel1.connect(bridge)

    node2 = InterfaceNode('server', ifname='eth0')



    channel2 = net.create_channel('channel2',delay='10ms')
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
