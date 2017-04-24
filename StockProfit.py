import random
import sys
import os


from pprint import pprint

print "Enter the following details:"
TickerSymbol = raw_input("Ticker Symbol: ");
Allotment = raw_input("Allotment(number of shares): ");
FinalSharePrice = float(raw_input("Final Share Price: "))
Sell_Commission = raw_input("Sell Commission: ");
InitialSharePrice = raw_input("Initial Share Price: ");
Buy_Commission = raw_input("Buy Commission: ");
CapitalGainTaxRate = raw_input("Capital Gain Tax Rate is")


dicts_from_file = {"TURN": "1.44", "FLWS": "10.5", "FCCY": "18.45", "SRCE": "48.65",
"VNET": "5.54",
"TWOU": "43.3",
"JOBS": "39.75",
"CAFD": "12.18",
"EGHT": "14.45",
"AVHI": "16.6",
"SHLM": "29.95"
}

TS = dicts_from_file[TickerSymbol]
print TS

Proceeds = Allotment*FinalSharePrice
CapitalGainTax = Allotment*(FinalSharePrice-InitialSharePrice)*CapitalGainTaxRate
Cost = Allotment*InitialSharePrice+Sell_Commission+Buy_Commission+CapitalGainTax
NetProfit = Proceeds - Cost
ROI = (NetProfit/Cost) * 100
BEP = InitialSharePrice+Sell_Commission+Buy_Commission

print ("Your Proceeds are %.2f", Proceeds)
print ("Costs were %.2f", Cost)
print ("Cost details")
print ("Total Purchase price %d X $%.2f = ", Allotment, Allotment*InitialSharePrice)
print ("Buy Commission = %.2f", Buy_Commission)
print ("Sell Commission = %.2f", Sell_Commission)
print ("Tax on Capital Gain = %.2f", CapitalGainTax)

print ("Net Profit = %.2f", NetProfit)
print ("Return on Investment = %.2f", ROI)
print ("To break even, you must have a final price of %.2f", BEP)








