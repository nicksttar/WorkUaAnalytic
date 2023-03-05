import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from wup import WorkUaParcing



def reponse_analitic(user_input):
    work = WorkUaParcing(user_input)
    responses = work.get_responses()

    if responses == []:
        print("No information")
    else:

        print("Please Wait, your response in querry")
        responses_categories = {"Полная занятость.": {}, "Полная занятость.\nС опытом": {}, 
                                "Неполная занятость.\nС опытом": {}, "Неполная занятость" : {}}


        index = 0
        for j,i in enumerate(responses):
            if i[index] in "Полная занятость" and "Опыт" in i[index+1]:
                responses_categories['Полная занятость.\nС опытом'][j] = i
            elif i[index] in "Полная занятость" and "Опыт" not in i[index+1]:
                responses_categories['Полная занятость.'][j] = i
            elif i[index] in "Неполная занятость" and "Опыт" in i[index+1]:
                responses_categories['Неполная занятость.\nС опытом'][j] = i
            elif i[index] in "Неполная занятость" and "Опыт" not in i[index+1]:
                responses_categories['Неполная занятость'][j] = i
                

        keys = [response for response in responses_categories.keys()]
        counts = [len(value) for value in responses_categories.values()]

        fig, ax = plt.subplots()

        ax.barh(keys, counts)

        ax.set_title(f"{user_input.title()} response analytic", fontsize=18)
        ax.set_ylabel("responses", fontsize=12)
        ax.set_xlabel("vacansies", fontsize=12)

        ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

        plt.show()
