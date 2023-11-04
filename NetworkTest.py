from qcompute_qnet.core.des import DESEnv

env = DESEnv("Simulation Env", default=True)
env.set_log(".NetworkTest.log", level="INFO")
env.init()
env.run(end_time=1e9, logging=True)

from qcompute_qnet.topology.link import Link
from qcompute_qnet.topology.network import Network
from qcompute_qnet.topology.node import Node

alice = Node("Alice")
bob = Node("Bob")

# repeater = Node('Repeater')

# link1 = Link('Alice to Repeater')
# link1.connect(alice, repeater)

link = Link("Alice to Bob", ends=(alice, bob, 10))

# link2 = Link('Bob to Repeater', ends=(bob, repeater), distance=50)

network = Network("Simple Network")
network.install([alice, bob, link])
# link1.connect(alice, repeater)

# network.install(alice)
# network.install(repeater)


# network.install(link1)
network.print_classical_topology()
# network.print_quantum_topology()
