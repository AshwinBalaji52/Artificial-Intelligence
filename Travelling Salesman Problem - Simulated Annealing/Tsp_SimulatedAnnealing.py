import numpy as np
import random
import matplotlib.pyplot as plt
'''
Simulated Annealing gives a near optimal solution
main advantge is tht it does't get stuck in local maxima
'''
'''
Swap function to find neighbours
'''
def swap (Cities, Element1, Element):
    Cities[Element], Cities[Element1] = Cities[min(Element, Element1)], Cities[max(Element, Element1)]
    New_Cities = Cities.copy()
    return New_Cities

def TSP_SimulatedAnnealing(Graph):
    
   Cities = list(range(len(Graph)))
   random.shuffle(Cities)
   Epochlist = []
   Temperaturelist = []
   
   #Calculating cost of the shuffles city order
   Old_Cost = cost(Graph, Cities)
   Epoch = 1 #loop start
   Temperature = 5000 #initial temperature for annealing
   Cool = 0.99995 #cooling factor to reduce temperature effect
   
   while Epoch <= 500:
      Element = np.random.randint(0, len(Graph))
      
      while True:
         Element1 = np.random.randint(0, len(Graph))
         if Element != Element1:
            break
    
      #swapping cities to find neighbours, i.e, getting new permutated cities
      New_Cities = swap(Cities, Element1, Element) 
      #calculating cost of swapped cities
      New_Cost = cost(Graph, New_Cities)
      
      #Optimisation to get the minimum cost tour
      if New_Cost < Old_Cost:
         Tour, Cost = New_Cities, New_Cost
      
      #Annealing procedure to avoid stucking in local maxima
      elif np.random.rand() < np.exp((New_Cost - Old_Cost)/Temperature):
            Tour, Cost = New_Cities, New_Cost
      
      #Cooling procedure. here cooling fucntion taken as anything as we want to reduce temperature at each iteration
      Temperature = Temperature * pow(Cool,Epoch) 
      #Temperature = Temperature / math.log(Cool,10)
      
      if(Temperature>=0):
          Epochlist.append(Epoch)
          Temperaturelist.append(Temperature)
          Epoch += 1
   if(Epoch >= 499):
     plt.plot(Epochlist, Temperaturelist, linewidth = 4)
     plt.xlabel('Iteration')
     plt.ylabel('Temperature Variation') 
     plt.title('Annealing (Cooling) - pow(Cool,Epoch) Function')
     plt.show() 
   return Tour,Cost
'''
Cost() to calculate tour's travel cost
'''
def cost(Graph, Cities):
    
   Traversal_cost = 0
   
   for itr in range(len(Cities)-1):
      Traversal_cost += Graph[Cities[itr]][Cities[itr+1]]
      
   Traversal_cost += Graph[Cities[len(Cities)-1]][Cities[0]] 
   return Traversal_cost

def main():
    Graph = [[0, 400, 200, 300],
             [400, 0, 300, 200],
             [200, 300, 0, 400],
             [300, 200, 400, 0]]
    
    result = TSP_SimulatedAnnealing(Graph)
    
    print("\n\tTravelling Salesman Problem using Simulated Annealing\n")
    print("Salesman Tour:", "City -->" , result[0][0] , "City -->" , result[0][1] , 
          "City -->" , result[0][2] , "City -->" , result[0][3])
    print("Traversal Cost:" , result[1])
    

if __name__ == "__main__":
    main()