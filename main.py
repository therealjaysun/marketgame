import numpy as np 




class Agent():
    #for the actions of the user
    def set_price():
        
    def set_restock():

    def inventory():
        # tracks inventory and updates inventory ledger


class Customer():
    #for simulating the customers and their behaviour
    def __init__(): 
    
    def archetypes():
        #governs the b, w of a customer archetype, allows tailoring to specific customer profiles and breakdowns of a given region. Here we are using 4 random profiles at an arbituary breakdown (e.g. 30% archetype A, 20% archetype B, 40% archetype C, 10% archetype D)

    def demand_function(need, b, w):
        #governs if person is looking for this product when entering

        #governs likelihood of purchasing product at given price

class Environment:
    #for simulating the supermarket environment
    def __init__(self, selfsize = 20):
        self.shelfsize = shelfsize #number of items to fill a shelf

    def restocking(Q_restock, thresh_restock):
        #orders for restock next day if inventory falls below threshold level
    
    def foot_traffic(h_open = 9, h_close = 18, avgTraffic = 2000):
        #governs the foot traffic profile of a given day
        return list_traffic #list of time series traffic data during business hours

    def sales():
        #tracks sales data in terms of when an item is sold, at what transaction price and what input cost, updates sales ledger to keep tally of net profit and total Q sold
        

    def time_simulation():
        #initiates time step and begins simulation

        #samples customer profile based on group breakdown

        # output final tallies

    def plot_results(): 
        # Creates time series plots of price, profit, profit velocity (moving average 30 periods)

