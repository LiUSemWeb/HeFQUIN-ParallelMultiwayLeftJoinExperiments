"""
This script generates a synthetic dataset to test the parallel multiway join operator.

It creates instances for one superclass, and additional subclasses (taking as an input the percentage of instances in the superclass that belong to each subclass).
This way it is possible to control the join selectivity between the sequence of OPTIONALs and the non-OPTIONAL part of the queries.

It then generates properties for the classes considering different cardinalities for the properties. Specifically, it generates 10 properties for each
member in the federation and for each property cardinality (provided as an input parameter).
"""

# Number of members in the federation. For each member, a N-Triples file will be generated
fed_members = 10

# Subclasses given by the percentage of instances of the superclass belonging to the subclass
# IMPORTANT NOTE: 1 must always be in the list as it will generate the instances for the superclass
subclass_cards = [0.25, 0.5, 0.75, 1]

# Cardinalities for each property as a percentage of instances of the superclass having a value for them
prop_cards = [0.25, 0.5, 0.75, 1]

# Number of properties to generate for each property cardinality
prop_number = 10

# Number of instances to generate for the superclass
number_of_instances = 1000


import os
import shutil
import random


# the datasets are generated in the fed/ directory
try:
    # remove fed/ directory if it exists
    shutil.rmtree('fed/')
except:
    pass

# create a fed/ directory with one directory for each federation member
os.mkdir('fed/')
for fed_member in range(fed_members):
    os.mkdir('fed/member_'+str(fed_member))


instances = list(range(number_of_instances))


for fed_member in range(fed_members):
    f = open('fed/member_'+str(fed_member)+'/member_'+str(fed_member)+'.nt', 'a')

    for subclass_card in subclass_cards:
        # the subset of instances for a subclass are picked from the superclass by shuffling the list instances and then selecting
        # the a number of instances from the beginning of the list (based on the percentage)
        random.shuffle(instances)
        for i in instances[:int(len(instances)*subclass_card)]:
            f.write('<http://example.com/instance_'+str(i)+'> a <http://example.com/class_'+str(subclass_card)+'> .\n')

    f.close()



for fed_member in range(fed_members):
    f = open('fed/member_'+str(fed_member)+'/member_'+str(fed_member)+'.nt', 'a')

    for prop_card in prop_cards:
        for num_prop in range(prop_number):
            random.shuffle(instances)
            for i in instances[:int(len(instances)*prop_card)]:
                f.write('<http://example.com/instance_'+str(i)+'> <http://example.com/property_card'+str(prop_card)+'_prop'+str(num_prop)+'_member'+str(fed_member)+'> "'+str(random.randint(0,100000000000))+'" .\n')

    f.close()
