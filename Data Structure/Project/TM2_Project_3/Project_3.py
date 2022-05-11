mark_dict = {"Krishna":[67,68,69],"Arjun":[70,98,63],"Malika":[52,56,60]}
name = input("Enter Name you want average of:")
val = mark_dict[name]
print("Average percentage mark:",sum(val)/len(val))