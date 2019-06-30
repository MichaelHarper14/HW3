import os
import csv

import statistics



budget_df= os.path.join('budget_data.csv')

with open(budget_df, newline="") as csvfile:
        csvreader = csv.reader(budget_df, delimiter=',')
      
        csv_header = next(csvfile)
        tp_data = tuple(csvfile)



total_month = 0
total_revenue  = 0
total_variance = 0
prev = 0
biggest_gain = 0
biggest_loss = 0
csvfile = []


        

for row in tp_data:    

          
        total_month = total_month + 1
        total_revenue = total_revenue + billy
        variance = revenue - prev
        if variance > biggest_gain:
                biggest_gain = variance
                gain_month = row[0]
        if variance < biggest_loss:
                        loss_month = row[0]
        total_variance = total_variance + variance
        prev = revenue

        total_variance = total_variance - int(tp_data[0][1])
        print(total_variance)
        avg_variance = total_variance/(total_month-1)
        billy = int(row[1])
        revenue = int(row([1])


        bid = (f"Financial Analysis\n\
                        ----------------------------\n\
                total_month: {total_month}\n\
                total_revenue: {total_revenue}\n\
                variance: {variance}\n\
                biggest_gain: {gain_month} (${biggest_gain})\n\
                biggest_loss: {loss_month} (${biggest_loss})")
        print(bid)              