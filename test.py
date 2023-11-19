import modPia
import apicon


#modPia.verOpc("curr.txt")
de = input()
a = input()
link = apicon.crearlinkCurr(de, a)
data = apicon.makeRequest(link)
apicon.writeFILE(data, "currMX_CAD")