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
   Temperature = 150 #initial temperature for annealing
   Cool = 10 #cooling factor to reduce temperature effect
   
   while Epoch <= 15:
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
      Temperature = Temperature - Cool
      #Temperature = Temperature / math.log(Cool,10)
      
      if(Temperature>=0):
          Epochlist.append(Epoch)
          Temperaturelist.append(Temperature)
          Epoch += 1
   if(Epoch >= 14):
     plt.plot(Epochlist, Temperaturelist, linewidth = 4)
     plt.xlabel('Iteration')
     plt.ylabel('Temperature Variation') 
     plt.title('Annealing (Cooling) by T = T-10 Function')
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
    Graph = [[0, 2, 5, 3, 6],
             [2, 0, 4, 3, 3],
             [5, 4, 0, 7, 3],
             [3, 3, 7, 0, 3],
             [6, 3, 3, 3, 0]]
    
    result = TSP_SimulatedAnnealing(Graph)
    
    print("\n\tTravelling Salesman Problem using Hill-Climbing \n")
    print("Salesman Tour:", "City -->" , result[0][0]+1 , "City -->" , result[0][1]+1 , 
          "City -->" , result[0][2]+1 , "City -->" , result[0][3]+1 , "City -->" , result[0][4]+1 , 
          "City -->" , result[0][0]+1)
    print("Traversal Cost:" , result[1])
    

if __name__ == "__main__":
    main()