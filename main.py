import numpy as np 
import pandas as pd

class Environment():
    #for simulating the supermarket environment
    def __init__(self, shelfsize = 20): 
        self.shelfsize = shelfsize #number of items to fill a shelf
        self.runstatus = False
        self.inventory = pd.DataFrame({'batchID':[0],'cost':[2], 'quantity':[200],'import_date':0, 'throwout_date':5}) #schema of inventory
        self.ledger = pd.DataFrame({'timestamp','customerID','p_transaction','batch_cost','q_purchased'}) #schema of ledger
        self.finance = pd.DataFrame()
    
    def spoiling(t_spoil = 5):




    def restocking(Q_restock, thresh_restock):
        #orders for restock next day if inventory falls below threshold level

    def foot_traffic(h_open = 9, h_close = 18, avgTraffic = 2000):
        #governs the foot traffic profile of a given day
        return list_traffic #list of time series traffic data during business hours

    def sales():
        #tracks sales data in terms of when an item is sold, at what transaction price and what input cost, updates sales ledger to keep tally of net profit and total Q sold
        

    def time_simulation(runstatus = True):
        #initiates time step and begins simulation

        #samples customer profile based on group breakdown

        # output final tallies

    def plot_results(): 
        # Creates time series plots of price, profit, profit velocity (moving average 30 periods)

class Agent(Environment):
    #for the actions of the user
    def __init__(self):
        

    def set_price():
        # sets price for good

    def pause():
        # pauses simulation
        runstatus = False
    def start():
        # starts simulation
        runstatus = True


class Customer(Environment):
    #for simulating the customers and their behaviour
    def __init__(): 
    
    def archetypes():
        #governs the b, w of a customer archetype, allows tailoring to specific customer profiles and breakdowns of a given region. Here we are using 4 random profiles at an arbituary breakdown (e.g. 30% archetype A, 20% archetype B, 40% archetype C, 10% archetype D)

    def demand_function(need, b, w):
        #governs how mean number of the products the person needs (sampled from truncated normal distribution

        #governs likelihood of purchasing product at given price

