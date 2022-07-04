# This script generates the whole list of private and public keys for the subgroups + its seven cosets
# we have chosen to investigate

import AddressGeneration

p1 = 107361793816595537
p2 = 174723607534414371449
p3 = 341948486974166000522343609283189
base = 7
h = (2 ** 6) * 3 * 149 * 631


privateSet = AddressGeneration.CosetPrivateKeyComputation(p1, p2, p3, base, h)
PublicSet = AddressGeneration.CosetKeysFile(h, privateSet)
