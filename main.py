from salaries_analytics import analytics_salary
from responses_analytics import reponse_analitic
from viewers_analytics import viewers_analytic



print("""░██╗░░░░░░░██╗░█████╗░██████╗░██╗░░██╗  ██╗░░░██╗░█████╗░  ██████╗░░█████╗░██████╗░░██████╗███████╗██████╗░
░██║░░██╗░░██║██╔══██╗██╔══██╗██║░██╔╝  ██║░░░██║██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
░╚██╗████╗██╔╝██║░░██║██████╔╝█████═╝░  ██║░░░██║███████║  ██████╔╝███████║██████╔╝╚█████╗░█████╗░░██████╔╝
░░████╔═████║░██║░░██║██╔══██╗██╔═██╗░  ██║░░░██║██╔══██║  ██╔═══╝░██╔══██║██╔══██╗░╚═══██╗██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██║░╚██╗  ╚██████╔╝██║░░██║  ██║░░░░░██║░░██║██║░░██║██████╔╝███████╗██║░░██║
░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ░╚═════╝░╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
by nicksttar
""")

text_of_user = "Choose way to analise job: 1-money, 2-need, 3-viewers: "
wait_text = "Working, still waiting..."


user_input = input(text_of_user)
while user_input not in "123":
    user_input = input(text_of_user)

if user_input == "1":
    analytics_salary(input("Input your job: "))
elif user_input == "2":
    reponse_analitic(input("Input your job: "))
elif user_input == "3":
    viewers_analytic(input("Input your job: "))
