#!/usr/bin/env python3

from marvis import ArgumentParser, Network, DockerNode, Scenario

def main():
    scenario = Scenario()

    net = Network("10.0.0.0", "255.255.255.0", base="0.0.0.2")
    net.block_ip_address("10.0.0.1")

    node1 = DockerNode('client', docker_build_dir='./docker/curl-client')
    node2 = DockerNode('server', docker_build_dir='./docker/simple-server')
    channel = net.create_channel(delay="10ms")
    channel.connect(node1)
    channel.connect(node2)

    scenario.add_network(net)

    with scenario as sim:
        # To simulate forever, just do not specifiy the simulation_time parameter.
        sim.simulate(simulation_time=60)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.run(main)
