priorProb =[1,0]
stateTransProb=[[0.6,0.4],[0,1]]
symbEmsProb = [[0.8,0.2],[0.3,0.7]]
symbol = [0,0,1]
p = priorProb
for i in range(len(symbol)):
    a = p[0]*symbEmsProb[0][symbol[i]]*stateTransProb[0][0] + p[1]*symbEmsProb[1][symbol[i]]*stateTransProb[1][0]
    b = p[0]*symbEmsProb[0][symbol[i]]*stateTransProb[0][1] + p[1]*symbEmsProb[1][symbol[i]]*stateTransProb[1][1]
    p[0] = a
    p[1] = b
    print("Alpha values for iteration "+str(i+1))
    print(p)
print("The total probability of the sequence is " + str(p[0]+p[1]))
