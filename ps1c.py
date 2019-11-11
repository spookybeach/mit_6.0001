# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 21:49:20 2019

@author: dvdsm
"""
annual_salary = float(input('Enter your starting salary: '))
x = annual_salary
total_cost = 1000000
semi_annual_raise = 0.07
current_savings = 0
portion_down_payment = 0.25 * total_cost
months = 0
epsilon = 100
low = 0
high = 10000
step = 0

while True:
    portion_saved = (low + high) / 2
    annual_salary = x
    current_savings = 0
    for mo in range(0, 36):
        monthly_salary = annual_salary / 12
        current_savings = current_savings + float((monthly_salary * portion_saved) / 10000) + (current_savings * 0.04) / 12
        if mo % 6 == 0:
            annual_salary = annual_salary + (annual_salary * semi_annual_raise)
    if abs(current_savings - portion_down_payment) <= epsilon:
        print('Best saving rate: ', '%.2f' % (portion_saved / 100), '%')
        print('Step in binary search: ', step)
        print(current_savings)
        break
    # decrease portion_save
    elif abs(current_savings - portion_down_payment) > epsilon and current_savings > portion_down_payment:
        high = portion_saved
    # increase portion_save
    elif abs(current_savings - portion_down_payment) > epsilon and current_savings < portion_down_payment:
        low = portion_saved
    if low == high:
        print('It is not possible to pay the down payment in three years.')
        break
    step = step + 1