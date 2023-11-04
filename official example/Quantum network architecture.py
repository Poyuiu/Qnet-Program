import os
from qcompute_qnet.core.des import DESEnv
from qcompute_qnet.topology.network import Network


# Create an environment for simulation
env = DESEnv("QKD Network Architecture", default=True)
# Create the network for Beijing quantum metropolitan area network
network = Network("Beijing QMAN")

# Set path of the JSON file for network topology configuration
filename = "data/beijing_qman_topology.json"
filename = os.path.abspath(filename)
# Load the network topology from the file
network.load_topology_from(filename)
# Print the quantum network topology by the geographical locations of the nodes
network.print_quantum_topology(geo=True)

# Get end nodes by their names
en13 = env.get_node("EN13")
en15 = env.get_node("EN15")
# EN13 sends a QKD request to EN15
en13.key_request(dst=en15, key_num=1, key_length=256)
# en13.receive_quantum_msg(en15, )
# en13.set_key_generation()


# Initialize and run the simulation
env.init()
env.run(logging=True)