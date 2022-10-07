import math

if __name__ == '__main__':
    hourly_wage = 10

    percent_incr = 3 / 100

    percent_decr = -3 / 100

    # DETERMINE NEW HOURLY WAGE AFTER 5YEARS OF GOOD REVIEW:
    # using formular given

    new_hourly_wage = hourly_wage * math.pow(1 + percent_incr, 5)

    print(f' An employee earns %.2f' % new_hourly_wage, '$ wages after 5 years of GOOD review ')


    # DETERMINE NEW HOURLY WAGE AFTER 3YEARS OF BAD REVIEW:

    updated_hourly_wage = new_hourly_wage * math.pow(1 + percent_decr, 2)

    print(f'An employee gets %.2f' % updated_hourly_wage, '$ wages after 2 years of BAD review ')

