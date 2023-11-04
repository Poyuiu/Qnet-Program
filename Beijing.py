from qcompute_qnet.core.des import DESEnv
from qcompute_qnet.topology.network import Network

env = DESEnv("QKD Network Simulation", default=True)  # 创建用以模拟的仿真环境
network = Network("Beijing QMAN")  # 创建北京城域网

filename = "data/beijing_qman_topology.json"  # 设置 JSON 配置文件的路径
network.load_topology_from(filename)  # 从 JSON 标准文件加载网络中的节点和链路
network.print_quantum_topology(geo=True)  # 根据节点地理位置打印量子网络拓扑结构

# 根据节点名字找到想要建立密钥的两位端节点用户
en13 = env.get_node("EN13")
en15 = env.get_node("EN15")

# EN13 发起 QKD 请求，指定请求的密钥数量和长度
en13.key_request(dst=en15, key_num=10, key_length=256)  