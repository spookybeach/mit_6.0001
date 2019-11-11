# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 21:40:03 2019

@author: dvdsm
"""

def saving_for_house():
    total_cost = float(input('What is the cost of your dream home? '))
    annual_salary = float(input('What is your salary? '))
    portion_saved = float(input('What portion of your salary would you like to save? '))
    semi_annual_raise = float(input('What percentage raise do you get semi-annually? '))
    portion_down_payment = 0.25
    current_savings = 0
    r = 0.04
    month_counter = 0
    while current_savings < total_cost*portion_down_payment:
        current_savings += ((annual_salary/12)*portion_saved)+(current_savings*r)/12
        month_counter += 1
        if month_counter%6==0:
            annual_salary += annual_salary*semi_annual_raise
    print('It will take you '+str(month_counter)+' months to save enough money.')

saving_for_house()