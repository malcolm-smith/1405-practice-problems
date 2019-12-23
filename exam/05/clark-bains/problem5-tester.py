
import copy
import importlib

modname = "problem5"
funcname = "isprime"
information = [[[1], True], [[2], True], [[3], True], [[4], False], [[5], True], [[6], False], [[7], True], [[8], False], [[9], False], [[10], False], [[11], True], [[12], False], [[13], True], [[14], False], [[15], False], [[16], False], [[17], True], [[18], False], [[19], True], [[20], False], [[21], False], [[22], False], [[23], True], [[24], False], [[25], False], [[26], False], [[27], False], [[28], False], [[29], True], [[30], False], [[31], True], [[32], False], [[33], False], [[34], False], [[35], False], [[36], False], [[37], True], [[38], False], [[39], False], [[40], False]]

resulttype = "bool"

try:
    module = importlib.import_module(modname)
    func = getattr(module,funcname)
except:
    print("Error loading module and/or function - check the names?")
    quit()

correct = 0
incorrect = []
print("Checking function with test inputs...")
print()
for info in information:
    inputs = copy.deepcopy(info[0])
    goal = info[1]
    print("Inputs:", str(inputs)[1:-1])
    print("Goal:",goal)
    result = func(*inputs)
    print("Your Result:", result)
    success = False
    if resulttype == "int" and isinstance(result, int):
        success = goal == result
    elif resulttype == "float" and isinstance(result, (int,float)):
        success = abs(goal - result) < 0.001
    elif resulttype == "bool" and isinstance(result, (int,bool)):
        success = goal == result
    elif resulttype == "string" and isinstance(result, str):
        success = goal.lower() == result.lower()
    elif resulttype == "orderedlist" and isinstance(result, list):
        success = False
        if len(goal) == len(result):
            success = True
            for i in range(len(goal)):
                if goal[i] != result[i]:
                    success = False

    if success:
        correct += 1
        print("Good!")
    else:
        incorrect.append([inputs,goal,result])
        print("Incorrect!")
    print()
	
print()
print("Your code produced",correct,"out of", len(information),"correct results.")
print()

if len(incorrect) > 0:
    input("Hit enter to see the incorrect cases...")
    print("The inputs for which your program failed were:")
    print()
    for info in incorrect:
        print("Inputs:", str(info[0])[1:-1])
        print("Goal:", info[1])
        print("Your Result:", info[2])
        print()
		