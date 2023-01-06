from typing import List

def maxIceCream(costs: List[int], coins: int) -> int:
    costs.sort()
    num_icecreams = 0
    for price in costs:
        if price <= coins:
            num_icecreams += 1
            coins -= price
        else:
            break
    
    return num_icecreams     
            
        
