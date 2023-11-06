import os
from qcompute_qnet.core.des import DESEnv
from qcompute_qnet.topology.network import Network
from qcompute_qnet.models.qkd.node import EndNode
# discreate event simulation environment
env = DESEnv("Qnet Benchmark", default=True)

# Beijing quantum metropolitan area network
beijing_qman = Network("Beijing QMAN")
topology_file = "data/beijing_qman_topology.json"
topology_file = os.path.abspath(topology_file)
beijing_qman.load_topology_from(topology_file)
# beijing_qman.print_quantum_topology(geo=True)

# Get 18 end nodes
end_nodes = [None]
for i in range(1, 19):
    end_nodes.append(env.get_node("EN" + str(i)))

print(type(end_nodes[13]))

# Each end node sends a QKD request to all the other end nodes
end_nodes[13].key_request(dst=end_nodes[15], key_num=10, key_length=256)
# end_nodes[2].key_request(dst=end_nodes[3], key_num=10, key_length=256)
# end_nodes[5].key_request(dst=end_nodes[14], key_num=10, key_length=256)

env.init()
env.run(logging=True)
