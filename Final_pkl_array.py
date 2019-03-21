import pickle
import pandas as pd
import numpy

def sig(x):
    # print(type(x))
    if x>51:
        return 1
    else:
        return 1/(1+numpy.exp(-x))

def evaluatestack(stack):
    elem = stack.pop(0)

    if (elem == '-'):
        return evaluatestack(stack) - evaluatestack(stack)
    elif (elem == '+'):
        return evaluatestack(stack) + evaluatestack(stack)
    elif (elem == '/'):
        try:
            return evaluatestack(stack) / evaluatestack(stack)
        except:
            return 0
    elif (elem == '*'):
        return evaluatestack(stack) * evaluatestack(stack)
    elif(elem=='P'):
         return sig(evaluatestack(stack)+evaluatestack(stack))
    elif(elem=="W"):
        return evaluatestack(stack)*evaluatestack(stack)
    else:
        # print(type(elem))
        return int(elem)
    
infile = open('finalized_model_long.pkl','rb')
new_dict = pickle.load(infile)
a = 0
data= pd.read_csv("training01.csv")
data=data.iloc[:,:-1]
classifier=new_dict[0]
aa=[]
aa.append(data.values[1000])
print(classifier)
for i in range(len(classifier)):
    print(classifier[i])
    if isinstance(classifier[i], int):
        #print("ambuje")
        classifier[i]=aa[0][classifier[i]]
        #print(classifier)
ww=evaluatestack(classifier)
            
if(ww > 0.9):
    print('3')
elif(ww > 0.5 and ww < 0.8):
    print('2')
elif(ww > 0.8 and ww < 0.9):
    print('1')
else:
    print('0')
