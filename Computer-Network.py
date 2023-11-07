#!/usr/bin/env python
# coding: utf-8

# In[3]:


import ipaddress

def calculate_subnets(base_network, subnet_bits):
    base_ip = ipaddress.ip_network(base_network)
    
    if subnet_bits <= base_ip.prefixlen:
        print("Error: Subnet bits should be larger than the base network prefix.")
        return
    
    subnets = list(base_ip.subnets(new_prefix=subnet_bits))
    
    print(f"Base Network: {base_ip}")
    print(f"Subnets with {subnet_bits} subnet bits:")
    for subnet in subnets:
        print(f"Subnet: {subnet}  Network Address: {subnet.network_address}  Subnet Mask: {subnet.netmask}")

# Example usage:
base_network_address = '192.168.1.0/24'  # Base network address in CIDR notation
subnet_bits = 28  # Number of bits to allocate for each subnet

calculate_subnets(base_network_address, subnet_bits)


# In[4]:


import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
    
    def add_edge(self, node1, node2, weight):
        self.nodes.add(node1)
        self.nodes.add(node2)
        if node1 not in self.edges:
            self.edges[node1] = []
        if node2 not in self.edges:
            self.edges[node2] = []
        self.edges[node1].append((node2, weight))
        self.edges[node2].append((node1, weight))  # For bidirectional connections
    
    def dijkstra(self, start_node):
        distances = {node: float('inf') for node in self.nodes}
        distances[start_node] = 0
        queue = [(0, start_node)]
        
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            if current_distance > distances[current_node]:
                continue
            
            for neighbor, weight in self.edges[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))
        
        return distances

# Example usage:
network = Graph()
network.add_edge('A', 'B', 5)
network.add_edge('B', 'C', 4)
network.add_edge('C', 'D', 8)
network.add_edge('D', 'A', 7)
network.add_edge('A', 'C', 2)

start_node = 'A'
shortest_paths = network.dijkstra(start_node)

for node, distance in shortest_paths.items():
    print(f"Shortest distance from {start_node} to {node}: {distance}")


# In[1]:


ip=input(f"Enter the IP address : ").split(".")
c=0
for i in ip:
    c=c+1
if c==4:
    if ip[0]>"0" and ip[0]<"127":
        print("IP Address is valid and belongs to class A \nSubnet mask: 255.0.0.0")
    elif ip[0]=="0" or ip[0]=="127":
        print("0 and 127 are reserved and cannot be used as a network address.")
    elif ip[0]>"127" and ip[0]<"192":
        print("IP Address is valid and belongs to class B \nSubnet mask: 255.255.0.0")
    elif ip[0]>"192" and ip[0]<"224":
        print("IP Address is valid and belongs to class C \nSubnet mask: 255.255.255.0")
    else:
        print("IP Address is valid and belongs to class D or E")
else :
    print("IP ADDRESS IS INVALID !! ")


# In[ ]:




