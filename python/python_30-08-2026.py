import sys
sugar_amount = 2
print(f"sugar amount is:{sugar_amount}")
cheetah = set()
cheetah.add("sher")
cheetah.add("systum")
cheetah.add("raja")
print(cheetah)
print(id(cheetah))
hello = ()
print(f"lets see:{bool(hello)}")
print(sys.float_info)
hellosir = "special shit"
hellosir_encoded = hellosir.encode("utf-8")
hellosir_decoded = hellosir_encoded.decode("utf-8")
print(hellosir_encoded)
systum  = ('hello','idk','what_to_say')
(hello1,hello2,hello3) = systum
print(systum)
print({hello1},{hello2},{hello3})
print('hello' in systum)
listed = ["ya","no","yes","no"]
count = listed.count
print(count)
listed.insert(3,"yesBitch")
print(listed)
listed.reverse()
print(listed)
a = listed.index("yesBitch")
print(a)