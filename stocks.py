#Manar Elkader
#CS175-1
#stocks

COMMISSION_RATE = 0.03
NUM_SHARES = 2000
PURCHASE_PRICE = 40.0
SELLING_PRICE = 42.75

amountPaidForStock = NUM_SHARES*PURCHASE_PRICE
purchaseCommission = COMMISSION_RATE*amountPaidForStock
totalPaid = amountPaidForStock+purchaseCommission
stockSoldFor = NUM_SHARES*SELLING_PRICE
sellingCommission = COMMISSION_RATE*stockSoldFor
totalReceived = stockSoldFor-sellingCommission
profitOrLoss = totalReceived-totalPaid

print ('Amount paid for stock: $' + str(amountPaidForStock))
print ('Commission paid on the purchase: $' + str(purchaseCommission))
print ('Amount the stock sold for: $' + str(stockSoldFor))
print ('Commission paid on the sale: $' + str(sellingCommission))
print ('Profit (or loss if negative): $' + str (profitOrLoss))
