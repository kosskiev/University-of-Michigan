#Read in the contents of the file SP500.txt which has monthly data for 2016 and 2017 about the S&P 500 closing prices as well as some other financial indicators, 
#including the “Long Term Interest Rate”, which is interest rate paid on 10-year U.S. government bonds.

#Write a program that computes the average closing price (the second column, labeled SP500) and the highest long-term interest rate. 
#Both should be computed only for the period from June 2016 through May 2017. Save the results in the variables mean_SP and max_interest.

with open("SP500.txt", "r") as file:
    new = file.readlines()
    closing_price = []
    interest_rate = []
    
    for x in new[6:18]: # Убираю строки из текста не соответствующие критерию с Июня 2016 по Май 2017 результаты
        y = x.split(",") # Разделяю список по ,
        closing_price.append(y[1]) # Добавляю второе значение в новый список
        interest_rate.append(y[5]) # Добавляю шестое значение в новый список
          
    sum_of_numbers = 0 
    for each in closing_price:
        sum_of_numbers = sum_of_numbers + float(each) # Суммирую все значения closing_price
   
    mean_SP = sum_of_numbers/len(closing_price) # Нахожу среднее значение
    print(float(mean_SP))
    max_interest = 0
    for i in interest_rate: # Нахожу максимальное значение interest_rate
        if float(i) > max_interest:
            max_interest = float(i)
    print(max_interest)
