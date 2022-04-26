from arbre_ROBDD import table,cons_abr, luka, compression, compression_bdd

import random
import time

from matplotlib import pyplot as plt
#################################          Partie IV  Exprimental        #################################

nbNode=[]


def size(tree):
    if tree == None:
        return

    if tree.id not in nbNode:
        nbNode.append(tree.id)
    size(tree.get_gauche())
    size(tree.get_droit())

tableVertie=[]


def newTest1():
    resultDic = {}
    for value in range(0, 4):
        tableVertie.append(table(value, 2))
    for i in range(0, 4):
        nbNode.clear()
        tree = cons_abr(tableVertie[i])
        luka(tree)
        tree = compression({},tree)
        tree = compression_bdd(tree)  # transformer l'arbre en ROBDD
        size(tree)
        nbNoeud = len(nbNode)
        if nbNoeud in resultDic:  # resultDic.has_key(nbNoeud):
            resultDic[nbNoeud] = resultDic[nbNoeud] + 1
        else:
            resultDic[nbNoeud] = 1
    return resultDic


def newTest2():
    resultDic = {}
    for value in range(0, 16):
        tableVertie.append(table(value, 4))
    for i in range(0, 16):
        nbNode.clear()
        tree = cons_abr(tableVertie[i])
        luka(tree)
        tree = compression({},tree)
        tree = compression_bdd(tree)  # transformer l'arbre en ROBDD
        size(tree)
        nbNoeud = len(nbNode)
        if nbNoeud in resultDic:  # resultDic.has_key(nbNoeud):
            resultDic[nbNoeud] = resultDic[nbNoeud] + 1
        else:
            resultDic[nbNoeud] = 1
    return resultDic


def newTest3():
    resultDic = {}
    for value in range(0, 256):
        tableVertie.append(table(value, 8))
    for i in range(0, 256):
        nbNode.clear()
        tree = cons_abr(tableVertie[i])
        luka(tree)
        tree = compression({},tree)
        tree = compression_bdd(tree)  # transformer l'arbre en ROBDD
        size(tree)
        nbNoeud = len(nbNode)
        if nbNoeud in resultDic:  # resultDic.has_key(nbNoeud):
            resultDic[nbNoeud] = resultDic[nbNoeud] + 1
        else:
            resultDic[nbNoeud] = 1
    return resultDic


def newTest4():
    resultDic = {}
    for value in range(0, 65536):
        tableVertie.append(table(value, 16))
    for i in range(0, 65536):
        print(i)
        nbNode.clear()
        tree = cons_abr(tableVertie[i])
        luka(tree)
        tree = compression({},tree)
        tree = compression_bdd(tree)  # transformer l'arbre en ROBDD
        size(tree)
        nbNoeud = len(nbNode)
        if nbNoeud in resultDic:  # resultDic.has_key(nbNoeud):
            resultDic[nbNoeud] = resultDic[nbNoeud] + 1
        else:
            resultDic[nbNoeud] = 1
    return resultDic


def newTest5():
    resultDic = {}
    for simple in range(0, 500003):
        randomNum = random.randint(0,pow(2,32)-1)
        tableVertie.append(table(randomNum, 32))
    for i in range(0, 500003):
        print(i)
        nbNode.clear()
        tree = cons_abr(tableVertie[i])
        luka(tree)
        tree = compression({},tree)
        tree = compression_bdd(tree)  # transformer l'arbre en ROBDD
        size(tree)
        nbNoeud = len(nbNode)
        if nbNoeud in resultDic:  # resultDic.has_key(nbNoeud):
            resultDic[nbNoeud] = resultDic[nbNoeud] + 1
        else:
            resultDic[nbNoeud] = 1
    return resultDic


def newTest6():
    resultDic = {}
    for simple in range(0, 400003):
        randomNum = random.randint(0,pow(2,64)-1)
        tableVertie.append(table(randomNum, 64))
    for i in range(0, 400003):
        print(i)
        nbNode.clear()
        tree = cons_abr(tableVertie[i])
        luka(tree)
        tree = compression({},tree)
        tree = compression_bdd(tree)  # transformer l'arbre en ROBDD
        size(tree)
        nbNoeud = len(nbNode)
        if nbNoeud in resultDic:  # resultDic.has_key(nbNoeud):
            resultDic[nbNoeud] = resultDic[nbNoeud] + 1
        else:
            resultDic[nbNoeud] = 1
    return resultDic


def newTest7():
    resultDic = {}
    for simple in range(0, 486892):
        randomNum = random.randint(0,pow(2,128)-1)
        tableVertie.append(table(randomNum, 128))
    for i in range(0, 486892):
        print(i)
        nbNode.clear()
        tree = cons_abr(tableVertie[i])
        luka(tree)
        tree = compression({},tree)
        tree = compression_bdd(tree)  # transformer l'arbre en ROBDD
        size(tree)
        nbNoeud = len(nbNode)
        if nbNoeud in resultDic:  # resultDic.has_key(nbNoeud):
            resultDic[nbNoeud] = resultDic[nbNoeud] + 1
        else:
            resultDic[nbNoeud] = 1
    return resultDic


def newTest8():
    resultDic = {}
    for simple in range(0, 56343):
        randomNum = random.randint(0,pow(2,256)-1)
        tableVertie.append(table(randomNum, 256))
    for i in range(0, 56343):
        print(i)
        nbNode.clear()
        tree = cons_abr(tableVertie[i])
        luka(tree)
        tree = compression({},tree)
        tree = compression_bdd(tree)  # transformer l'arbre en ROBDD
        size(tree)
        nbNoeud = len(nbNode)
        if nbNoeud in resultDic:  # resultDic.has_key(nbNoeud):
            resultDic[nbNoeud] = resultDic[nbNoeud] + 1
        else:
            resultDic[nbNoeud] = 1
    return resultDic


def newTest9():
    resultDic = {}
    for simple in range(0, 94999):
        randomNum = random.randint(0,pow(2,512)-1)
        tableVertie.append(table(randomNum, 512))
    for i in range(0, 94999):
        print(i)
        nbNode.clear()
        tree = cons_abr(tableVertie[i])
        luka(tree)
        tree = compression({},tree)
        tree = compression_bdd(tree)  # transformer l'arbre en ROBDD
        size(tree)
        nbNoeud = len(nbNode)
        if nbNoeud in resultDic:  # resultDic.has_key(nbNoeud):
            resultDic[nbNoeud] = resultDic[nbNoeud] + 1
        else:
            resultDic[nbNoeud] = 1
    return resultDic


def newTest10():
    resultDic = {}
    for simple in range(0, 17975):
        randomNum = random.randint(0,pow(2,1024)-1)
        tableVertie.append(table(randomNum, 1024))
    for i in range(0, 17975):
        print(i)
        nbNode.clear()
        tree = cons_abr(tableVertie[i])
        luka(tree)
        tree = compression({},tree)
        tree = compression_bdd(tree)  # transformer l'arbre en ROBDD
        size(tree)
        nbNoeud = len(nbNode)
        if nbNoeud in resultDic:  # resultDic.has_key(nbNoeud):
            resultDic[nbNoeud] = resultDic[nbNoeud] + 1
        else:
            resultDic[nbNoeud] = 1
    return resultDic


def graphy_test_1():
    dicRes = newTest1()
    sorted(dicRes)
    keylist = dicRes.keys()
    newd = {}
    for key in sorted(keylist):
        newd[key] = dicRes[key]
    print(newd)
    all_keys = newd.keys()
    all_values = newd.values()

    plt.plot(list(all_keys), list(all_values), 'b-o')
    plt.xlabel("ROBDD node count for 1 variable")
    plt.ylabel("Number of Boolean functions")
    plt.grid()
    plt.axis([0, 4, 0, 5])
    plt.show()


def graphy_test_2():
    dicRes = newTest2()
    sorted(dicRes)
    keylist = dicRes.keys()
    newd = {}
    for key in sorted(keylist):
        newd[key] = dicRes[key]
    print(newd)
    all_keys = newd.keys()
    all_values = newd.values()

    plt.plot(list(all_keys), list(all_values), 'b-o')
    plt.xlabel("ROBDD node count for 2 variable")
    plt.ylabel("Number of Boolean functions")
    plt.grid()
    plt.axis([0, 6, 0, 10])
    plt.show()


def graphy_test_3():
    dicRes = newTest3()
    sorted(dicRes)
    keylist = dicRes.keys()
    newd = {}
    for key in sorted(keylist):
        newd[key] = dicRes[key]
    print(newd)
    all_keys = newd.keys()
    all_values = newd.values()

    plt.plot(list(all_keys), list(all_values), 'b-o')
    plt.xlabel("ROBDD node count for 3 variable")
    plt.ylabel("Number of Boolean functions")
    plt.grid()
    plt.axis([0, 10, 0, 100])
    plt.show()


def graphy_test_4():
    dicRes = newTest4()
    sorted(dicRes)
    keylist = dicRes.keys()
    newd = {}
    for key in sorted(keylist):
        newd[key] = dicRes[key]
    print(newd)
    all_keys = newd.keys()
    all_values = newd.values()

    plt.plot(list(all_keys), list(all_values), 'b-o')
    plt.xlabel("ROBDD node count for 4 variable")
    plt.ylabel("Number of Boolean functions")
    plt.grid()
    plt.axis([0, 12, 0, 25000])
    plt.show()


def graphy_test_5():
    dicRes = newTest5()
    sorted(dicRes)
    keylist = dicRes.keys()
    newd = {}
    for key in sorted(keylist):
        newd[key] = dicRes[key]
    print(newd)
    nbKey = list(newd.keys())
    print("unique size:"+str(len(nbKey)))
    all_keys = list(newd.keys())
    all_values = list(newd.values())
    all_values_new = [i * 8589 for i in all_values]

    plt.plot(all_keys, all_values_new, 'b-o')
    plt.xlabel("ROBDD node count for 5 variable")
    plt.ylabel("Number of Boolean functions")
    plt.grid()
    plt.axis([0, 20, 0, 2*pow(10, 9)])
    plt.show()


def graphy_test_6():
    dicRes = newTest6()
    sorted(dicRes)
    keylist = dicRes.keys()
    newd = {}
    for key in sorted(keylist):
        newd[key] = dicRes[key]
    print(newd)
    nbKey = list(newd.keys())
    print("unique size:"+str(len(nbKey)))
    all_keys = list(newd.keys())
    all_values = list(newd.values())
    all_values_new = [i * (pow(2, 64) / 400003) for i in all_values]

    plt.plot(all_keys, all_values_new, 'b-o')
    plt.xlabel("ROBDD node count for 6 variable")
    plt.ylabel("Number of Boolean functions")
    plt.grid()
    plt.axis([0, 35, 0, 5*pow(10,18)])
    plt.show()


def graphy_test_7():
    dicRes = newTest7()
    sorted(dicRes)
    keylist = dicRes.keys()
    newd = {}
    for key in sorted(keylist):
        newd[key] = dicRes[key]
    print(newd)
    nbKey = list(newd.keys())
    print("unique size:"+str(len(nbKey)))
    all_keys = list(newd.keys())
    all_values = list(newd.values())
    all_values_new = [i * 6.988 for i in all_values]

    plt.plot(all_keys, all_values_new, 'b-o')
    plt.xlabel("ROBDD node count for 7 variable")
    plt.ylabel("Number of Boolean functions(10^32)")
    plt.grid()
    plt.axis([0, 50, 0, 9*pow(10, 5)])
    plt.show()


def graphy_test_8():
    dicRes = newTest8()
    sorted(dicRes)
    keylist = dicRes.keys()
    newd = {}
    for key in sorted(keylist):
        newd[key] = dicRes[key]
    print(newd)
    nbKey = list(newd.keys())
    print("unique size:"+str(len(nbKey)))
    all_keys = list(newd.keys())
    all_values = list(newd.values())
    all_values_new = [i * 2.055  for i in all_values]

    plt.plot(all_keys, all_values_new, 'b-o')
    plt.xlabel("ROBDD node count for 8 variable")
    plt.ylabel("Number of Boolean functions(*10^72)")
    plt.grid()
    plt.axis([0, 90, 0, 3*pow(10,4)])
    plt.show()


def graphy_test_9():
    dicRes = newTest9()
    sorted(dicRes)
    keylist = dicRes.keys()
    newd = {}
    for key in sorted(keylist):
        newd[key] = dicRes[key]
    print(newd)
    nbKey = list(newd.keys())
    print("unique size:"+str(len(nbKey)))
    all_keys = list(newd.keys())
    all_values = list(newd.values())
    all_values_new = [i * 1.411363 for i in all_values]

    plt.plot(all_keys, all_values_new, 'b-o')
    plt.xlabel("ROBDD node count for 9 variable")
    plt.ylabel("Number of Boolean functions(*10^149)")
    plt.grid()
    plt.axis([0, 160, 0, 2.5*pow(10,4)])
    plt.show()


def graphy_test_10():
    dicRes = newTest10()
    sorted(dicRes)
    keylist = dicRes.keys()
    newd = {}
    for key in sorted(keylist):
        newd[key] = dicRes[key]
    print(newd)
    nbKey = list(newd.keys())
    print("unique size:"+str(len(nbKey)))
    all_keys = list(newd.keys())
    all_values = list(newd.values())
    all_values_new = [i * 1.000107 for i in all_values]

    plt.plot(all_keys, all_values_new, 'b-o')
    plt.xlabel("ROBDD node count for 10 variable")
    plt.ylabel("Number of Boolean functions(*10^304")
    plt.grid()
    plt.axis([0, 300, 0, 2*pow(10, 3)])
    plt.show()

##################################         Fin  Partie IV  Exprimental    ##############################

#################################          Partie  Exprimental  TEST     #################################

start =time.perf_counter()

# graphy_test_1()
# graphy_test_2()
# graphy_test_3()
# graphy_test_4()
# graphy_test_5()
# graphy_test_6()
# graphy_test_7()
# graphy_test_8()
# graphy_test_9()
# graphy_test_10()

end = time.perf_counter()

print('Running time: %s Seconds'%(end-start))
