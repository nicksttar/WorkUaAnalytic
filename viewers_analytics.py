from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from wup import WorkUaParcing


def viewers_analytic(user_input):

    work = WorkUaParcing(user_input)
    viewers = work.get_viewers()

    if viewers == []:
        print("No information")
    else:
        print("Please Wait, your response in querry")
        keys = list(set(viewers))
        keys_normal = sorted([int(i) for i in keys])

        count = [viewers.count(str(i)) for i in keys_normal]

        plt.style.use("ggplot")
        fig, ax = plt.subplots()

        ax.scatter(keys_normal, count)

        ax.set_title(f"{user_input.title()} viewers")
        ax.set_ylabel("viewers")
        ax.set_xlabel("vacansies")

        ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))

        plt.show()


