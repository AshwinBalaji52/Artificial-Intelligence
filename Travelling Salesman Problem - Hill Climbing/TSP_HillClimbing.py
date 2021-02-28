import numpy as np
import random
import matplotlib.pyplot as plt

Traversal = []

'''
Swap function to find neighbours
'''
def swap (Cities, Element1, Element):
    #print("Stuck in local maxima/minima")
    Cities[Element], Cities[Element1] = Cities[min(Element, Element1)], Cities[max(Element, Element1)]
    New_Cities = Cities.copy()
    return New_Cities

def TSP_HillClimbing(Graph):
   global Traversal
   Cities = list(range(len(Graph)))
   random.shuffle(Cities)
   
   #Calculating cost of the shuffles city order
   Old_Cost = cost(Graph, Cities)
   Epoch = 1 #loop start
   
   while Epoch <= 1000:
      Element = np.random.randint(0, len(Graph))
      while True:
         Element1 = np.random.randint(0, len(Graph))
         if Element != Element1:
            break
        
      #swapping cities to find neighbours, i.e, getting new permutated cities
      New_Cities = swap(Cities, Element1, Element)
      #calculating cost of swapped cities
      New_Cost = cost(Graph, New_Cities)
      
      #Optimisation to get the minimum cost tour such that to eagerly find an optimal solution
      #Rejects bad cases accepts good cases only
      if New_Cost < Old_Cost:
         Tour, Cost = New_Cities, New_Cost
      else:
          continue
      Epoch += 1
      
   '''
   Plot graphs to visualize
   '''  
   if(Epoch >= 999):
       
     x_iteration = []
     y_cost = []
     Iteration = list(range(len(Traversal)))
     
     curve = np.polyfit(Iteration, Traversal, 10)
     poly = np.poly1d(curve)
     
     for itr in range (len(Traversal)):
         x_iteration.append(itr+1)
         calc = poly(itr+1)
         y_cost.append(calc)
         
     plt.plot(x_iteration, y_cost, color = 'yellow', linewidth = 2, label = "Polynomial Plot")
     plt.scatter(x_iteration, y_cost, color = 'red', label = "Scatter Plot")
     plt.xlabel('#Possible cases considered (Including accepted/unaccepted cases)')
     plt.ylabel('Travel Cost')
     plt.legend()
     plt.title('Hill Climbing')
     plt.show() 
     
   return Tour,Cost

'''
Cost() to calculate tour's travel cost
'''  
def cost(Graph, Cities):
    
   Traversal_cost = 0
   global Traversal
   
   for itr in range(len(Cities)-1):
      
      Traversal_cost += Graph[Cities[itr]][Cities[itr+1]]
      Traversal.append(Traversal_cost)
   Traversal_cost += Graph[Cities[len(Cities)-1]][Cities[0]] 
   
   #This part below is just to gather possible values right from min to max travel cost paths
   #It will be easy to plot graph
   Traversal.append(Traversal_cost)
   
   return Traversal_cost

def main():
    Graph = [[0, 2, 5, 3, 6],
             [2, 0, 4, 3, 3],
             [5, 4, 0, 7, 3],
             [3, 3, 7, 0, 3],
             [6, 3, 3, 3, 0]]
    
    result = TSP_HillClimbing(Graph)
    
    print("\n\tTravelling Salesman Problem using Hill-Climbing \n")
    print("Salesman Tour:", "City -->" , result[0][0]+1 , "City -->" , result[0][1]+1 , 
          "City -->" , result[0][2]+1 , "City -->" , result[0][3]+1 , "City -->" , result[0][4]+1 , 
          "City -->" , result[0][0]+1)
    print("Traversal Cost:" , result[1])

if __name__ == "__main__":
    main()