import random
import sys
import os


from pprint import pprint

print "Enter the following details:"
TickerSymbol = raw_input("Ticker Symbol: ")
Allotment = float(raw_input("Allotment(number of shares): "))
FinalSharePrice = float(raw_input("Final Share Price: "))
Sell_Commission = float(raw_input("Sell Commission: "))
InitialSharePrice = float(raw_input("Initial Share Price: "))
Buy_Commission = float(raw_input("Buy Commission: "))
CapitalGainTaxRate = float(raw_input("Capital Gain Tax Rate is"))


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
CapitalGainTax = Allotment*(FinalSharePrice-InitialSharePrice)*CapitalGainTaxRate/100
Cost = Allotment*InitialSharePrice+Sell_Commission+Buy_Commission+CapitalGainTax
NetProfit = Proceeds - Cost
ROI = (NetProfit/Cost) * 100
BEP = InitialSharePrice+Sell_Commission+Buy_Commission

print "Your Proceeds are ", Proceeds
print "Costs were ", Cost
print "Cost details"
print "Total Purchase price = ", Allotment*InitialSharePrice
print "Buy Commission = ", Buy_Commission
print "Sell Commission = ", Sell_Commission
print "Tax on Capital Gain = ", CapitalGainTax

print "Net Profit = ", NetProfit
print "Return on Investment = ", ROI
print "To break even, you must have a final price of ", BEP








