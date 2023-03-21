from qcompute_qnet.core.des import DESEnv
from qcompute_qnet.topology.network import Network
from qcompute_qnet.models.qkd.node import QKDNode
from qcompute_qnet.topology.link import Link
from qcompute_qnet.devices.channel import ClassicalFiberChannel, QuantumFiberChannel
from qcompute_qnet.models.qkd.key_generation import PrepareAndMeasure

# 1. 创建环境并设置其为默认环境
env = DESEnv("BB84", default=True)

# 2. 创建量子网络
network = Network("BB84 Network")

# 3. 创建 QKD 节点并加载协议栈
alice = QKDNode("Alice")
bob = QKDNode("Bob")

# 设置协议并添加到协议栈中
bb84_alice = alice.set_key_generation(bob)
alice.protocol_stack.build(bb84_alice)

bb84_bob = bob.set_key_generation(alice)
bob.protocol_stack.build(bb84_bob)

# 4. 创建并连接通信链路
link_ab = Link("A_B", ends=(alice, bob))

# 4.1 创建通信信道并装入链路
cchannel1 = ClassicalFiberChannel("c_A2B", sender=alice, receiver=bob, distance=1e3)
cchannel2 = ClassicalFiberChannel("c_B2A", sender=bob, receiver=alice, distance=1e3)
qchannel = QuantumFiberChannel("q_A2B", sender=alice, receiver=bob, distance=1e3)

# 4.2 将物理信道装入通信链路中
link_ab.install([cchannel1, cchannel2, qchannel])

# 5. 将通信节点和链路都装入网络
network.install([alice, bob, link_ab])

# 6. 分别选定 Alice 与 Bob 在协议中的角色并指定密钥数量和长度，启动协议栈
alice.protocol_stack.start(
    role=PrepareAndMeasure.Role.TRANSMITTER, key_num=2, key_length=256
)
bob.protocol_stack.start(
    role=PrepareAndMeasure.Role.RECEIVER, key_num=2, key_length=256
)

# 7. 仿真环境初始化，运行并保存日志记录
env.init()
env.run(logging=True)
