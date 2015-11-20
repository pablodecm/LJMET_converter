
from ROOT import vector


def pu_weight( data_pu, mc_pu, return_std_vector = True ):
    print "sum(data_pu) - {}".format(sum(data_pu))
    print "sum(mc_pu) - {}".format(sum(mc_pu))
    weight = []
    for i in range(min(len(data_pu),len(mc_pu))):
        weight.append(data_pu[i]/mc_pu[i])
    if return_std_vector:
        v = vector('double')()    
        v += weight
        return v 
    else:
        return weight


        
        


