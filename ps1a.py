# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:27:33 2019

@author: dvdsm
"""

def saving_for_house():
    total_cost = float(input('What is the cost of your dream home? '))
    annual_salary = float(input('What is your salary? '))
    portion_saved = float(input('What portion of your salary would you like to save? '))
    portion_down_payment = 0.25
    current_savings = 0
    r = 0.04
    month_counter = 0
    if current_savings >= total_cost*portion_down_payment:
        print('It will take you '+str(month_counter)+' months to save enough money.')
    else:
        while current_savings < total_cost*portion_down_payment:
            current_savings += ((annual_salary/12)*portion_saved)+(current_savings*r)/12
            month_counter += 1
        print('It will take you '+str(month_counter)+' months to save enough money.')

saving_for_house()