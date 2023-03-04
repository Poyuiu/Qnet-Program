from qcompute_qnet.core.des import DESEnv
from qcompute_qnet.topology import Network, Node, Link

# create a simulaton environment
env = DESEnv("Simulation Environment", default=True)
# create a network
network = Network("First Network")
# create a node named Alice
alice = Node("Alice")
# create a node named Bob
bob = Node("Bob")
# create a link between Alice and Bob
link = Link("Alice_Bob", ends=(alice, bob))
# build up a network from nodes and links
network.install([alice, bob, link])
# initialize the simulation environment
env.init()
# run the network simulation
env.run()
