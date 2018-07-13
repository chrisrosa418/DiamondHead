#Setup win variables
MG_bout = False
MW_bout = True

#Set odds
mg_ko = 5
mw_dc = 1.75

#Set bets
mg_ko_bet = 100
mw_dc_bet = 300
total_bet = mg_ko_bet + mw_dc_bet

#Run the GROSS simulation
mg_gross = mg_ko * mg_ko_bet
mw_gross = mw_dc * mw_dc_bet

#Net calculation
if MG_bout == True:
    gross = total_bet - mg_gross
if MW_bout == True:
    gross = total_bet - mw_gross

#Net Payout
if MG_bout == True:
    print 'The winner is McGreggor by KO'
if MW_bout == True:
    print 'The winner is Mayweather by Decision'
#pprint("Your total winnings were", float(mg_gross - mw_gross))

print 'Your total bet was {0}'.format(total_bet)

print 'Your total winnings were {0}'.format(abs(gross))
