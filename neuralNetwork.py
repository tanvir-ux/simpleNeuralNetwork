weight = 0.1
def neural_network(input,weight):
    prediction = input*weight;
    return prediction

number_of_toes = [8.5,9.5,10,9]
input = number_of_toes[0]
pred = neural_network(input,weight)
print(pred)

# output should be 0.8500000000000001
#because pred = 8.5 * 0.1

#multiple inputs
def w_sum(a,b):
    assert(len(a) == len(b))
    output = 0
    for i in range(len(a)):
        output += (a[i] * b[i])
    return output
weights = [0.1,0.2,0]
def neural_network(input,weights):
    pred = w_sum(input,weights)
    return pred
toes = [8.5,9.5,9.9,9.0]
wlrec = [0.65,0.8,0.8,0.9]
nfans = [1.2,1.3,0.5,1.0]
input = [toes[0],wlrec[0],nfans[0]]
pred = neural_network(input,weights)
print(pred)