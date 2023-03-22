from qcompute_qnet.core.des import DESEnv

env = DESEnv('Simulation Env', default=True)

from qcompute_qnet.topology.link import Link
from qcompute_qnet.topology.network import Network
from qcompute_qnet.topology.node import Node

alice = Node('Alice')
bob = Node('Bob')

repeater = Node('Repeater')

link1 = Link('Alice to Repeater')
# link1.connect(alice, repeater)

link2 = Link('Bob to Repeater', ends=(bob, repeater), distance=50)

network = Network('Simple Network')
network.install(alice)
network.install(repeater)
link1.connect(alice, repeater)

network.install(link1)
network.print_classical_topology()
# network.print_quantum_topology()