from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from wup import WorkUaParcing
from statistics import mean


def analytics_salary(user_input):


    work = WorkUaParcing(user_input)
    salary = work.get_salaries()

    print(work.job)

    if salary == []:
        print("No information")
    else:
        print("Please Wait, your response in querry")
        salary_categories = {"no salary": {}, "<10 000": {}, ">10 000": {}, ">12 000": {}, ">15 000" : {}, ">20 000": {}}


        for j, i in enumerate(range(salary.count("no salary"))):
            salary_categories["no salary"][j] = i

        salary = [g for g in salary if g != "no salary"]


        result = []
        for item in salary:
            item = item.replace('грн', '')  
            if '-' in item:  
                start, end = item.split('-')
                result.append((int(start), int(end))) 
            else:
                result.append((int(item),))  


        for n, i in enumerate(result):
            if mean(i) <= 10000:
                salary_categories['<10 000'][n] = i
            elif 10000 < mean(i) < 12000:
                salary_categories['>10 000'][n] = i
            elif 15000 > mean(i) >= 12000:
                salary_categories['>12 000'][n] = i
            elif 20000> mean(i) >= 15000:
                salary_categories['>15 000'][n] = i
            elif mean(i) >= 20000:
                salary_categories['>20 000'][n] = i


        counts = [len(i) for i in salary_categories.values()]
        keys = [i for i in salary_categories.keys()]


        fig, ax = plt.subplots()

        ax.barh(keys, counts)
        ax.set_title(f"{user_input.title()} salaries analytic", fontsize=18)


        ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))


        plt.show()