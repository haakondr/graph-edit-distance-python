from collections import defaultdict

class knn():
    def __init__(self, k, instances, dist_fn, filtering_fn=None):
        self.k = k
        self.instances = instances
        self.distance_fn = dist_fn
        self.filtering_fn = filtering_fn

    def classify(self, case):
        nn = self.nearest_neighbours(case)
        most = weighted_sum_voting(nn)

        return most

    def nearest_neighbours(self, case):
        nearest_neighbours = []
         
        for instance in self.get_instances(case):
            dist = self.distance_fn(case, instance[1])
            nearest_neighbours.append((dist, instance[2]))
        
        nearest_neighbours.sort() 
        
        return nearest_neighbours[:self.k]
    
    def get_instances(self, case):
        if self.filtering_fn:
            return self.filtering_fn(case, self.instances)
        else:
            return self.instances

def weighted_sum_voting(neighbours):
    max_dist = neighbours[-1][0]
    distances = defaultdict(float)
     
    for n in neighbours:
        try:
            weight = 1. / (n[0] / max_dist)
        except ZeroDivisionError:
            weight = 1. 
        label = n[1]
        distances[label] += weight
    return max([(distances[x],x) for x in distances])[1] 
