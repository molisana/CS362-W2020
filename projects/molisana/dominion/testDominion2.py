# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:39:32 2020

@author: molisana
"""

import testUtility as refactor

#Get player names
player_names = ["Annie","*Ben","*Carla"]

supply_order = {0:['Curse','Copper'],2:['Estate','Cellar','Chapel','Moat'],
                3:['Silver','Chancellor','Village','Woodcutter','Workshop'],
                4:['Gardens','Bureaucrat','Feast','Militia','Moneylender','Remodel','Smithy','Spy','Thief','Throne Room'],
                5:['Duchy','Market','Council Room','Festival','Laboratory','Library','Mine','Witch'],
                6:['Gold','Adventurer'],8:['Province']}

nC, nV = refactor.numCursesVictory(player_names)

#Define box
box = {}
supply = refactor.getSupply(nV, box)
box["Chapel"]=[Dominion.Chapel()]*1

refactor.addSupplyStandard(supply, player_names, nV, nC)

trash, players = refactor.initializeGame(player_names)

refactor.playGame(supply_order, players, supply, trash)
            
refactor.calcFinalScore(players)