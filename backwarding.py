priorProb =[1,0]
stateTransProb=[[0.6,0.4],[0,1]]
symbEmsProb = [[0.8,0.2],[0.3,0.7]]
symbol = [0,0,1]
p = [1,1]
for i in range(len(symbol)):
    a = stateTransProb[0][0]*symbEmsProb[0][symbol[len(symbol)-i-1]]*p[0]+stateTransProb[0][1]*p[1]*symbEmsProb[0][symbol[len(symbol)-i-1]]
    b = stateTransProb[1][0]*symbEmsProb[1][symbol[len(symbol)-i-1]]*p[0]+stateTransProb[1][1]*p[1]*symbEmsProb[1][symbol[len(symbol)-1-i]]
    p[0]=a
    p[1]=b
    print("Beta Value for iteration "+str(i+1))
    print(p)
    
print("The probability of given sequence is "+str(p[0]*priorProb[0]+p[1]*priorProb[1]))
