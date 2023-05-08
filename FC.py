#   Игра
def future_price(actual_price, inflation, years_to_target):
    inflation = int(inflation/100)
    future_price = int(actual_price * (1 + inflation) ** years_to_target)
    monthly_payment = int(future_price / years_to_target / 12)
    return future_price, monthly_payment

#   Параметры
def parametres(actual_price, inflation, years_to_target):
    actual_price = input('How much is your target now?     ')
    inflation = input('Enter the inflation rate     ')
    years_to_target = input('Enter the number of years to goal      ')
    print(actual_price)
    print(inflation)
    print(years_to_target)
    return actual_price, inflation, years_to_target


#   Старт и приветствие
def start(answer_for_start):
    answer_for_start = input('The ME4TALculator will answer these questions :) Are you ready to get started?      ')
    print('Hello, dear friend!')
    print('Would you like to know how much your goal will be worth in 2, 3, 10 years (for example, education for your child)?   ')
    print('How much do you have to save every month to save in time?    ' )
    return answer_for_start

if answer_for_start == 'Yes' or 'yes' or 'Y' or 'y':
    print(parametres())
print(future_price())



