artifacts = ["Vase","Statue","Coin"]
artifacts.append("Tablet")
artifacts.insert(0, "Mask")
artifacts.sort(key=str.lower)
print("Final arrangement of artifacts:",artifacts)