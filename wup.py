import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
headers = {"User-Agent": ua.chrome}


class WorkUaParcing:
    """Class which parcing information in vacancies from work ua"""

    def __init__(self, job):
        """Init job"""
        self.job = "+".join(job.split())


    def get_max_pages(self):
        """Returns max pages of choosen job"""
        data = [1]
        counter = 1
        while data != []:
            counter += 1
            url = f"https://www.work.ua/ru/jobs-kyiv-{self.job}/?page={counter}"
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "lxml")
            data = soup.find_all("div", class_="card card-hover card-visited wordwrap job-link")
        return counter-1

    def get_salaries(self):
        """Resturns list of all salaries from all pages"""
        salary = []
        func = self.get_max_pages()+1
        for page in range(1, func):

            url = f"https://www.work.ua/ru/jobs-kyiv-{self.job}/?page{page}"
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "lxml")
            data = soup.find_all("div", class_="card card-hover card-visited wordwrap job-link")
            
            for salary_un in data:
                try:
                    text = salary_un.find("b").text.strip()
                    text = text.replace("\u202f", "")
                    text = text.replace("\u2009", "")
                    text = text.replace("\xa0", "")
                    text = text.replace('–', '-')
                except AttributeError:
                    continue
                else:
                    if "грн" in text:
                        salary.append(text)
                    else:
                        salary.append("no salary")
        return salary
    
    def get_responses(self):
        """Returns all responses from each vacancy"""
        func = self.get_max_pages()

        all_information = []    
        for page in range(1, func+1):
            url = f"https://www.work.ua/ru/jobs-kyiv-{self.job}/?page={page}"
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "lxml")

            data = soup.find_all("div", class_="card card-hover card-visited wordwrap job-link")

            urles = []
            for card in data:
                url = "https://www.work.ua" + card.find("a").get("href")
                urles.append(url)


            for inf in urles:
                response = requests.get(inf)
                soup = BeautifulSoup(response.text, "lxml") 
                inform = soup.find_all("p", class_="text-indent add-top-sm")[1].text.strip().split(".")
                all_information.append(inform)

        return all_information

    def get_viewers(self):
        """Returns all viewers from each vacancy"""
        func = self.get_max_pages()

        all_information = []    
        for page in range(1, func+1):
            url = f"https://www.work.ua/ru/jobs-kyiv-{self.job}/?page={page}"
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "lxml")

            data = soup.find_all("div", class_="card card-hover card-visited wordwrap job-link")

            urles = []
            for card in data:
                url = "https://www.work.ua" + card.find("a").get("href")
                urles.append(url)

            for inf in urles:
                response = requests.get(inf, headers=headers)
                soup = BeautifulSoup(response.text, "lxml") 
                inform = soup.find("h5", class_="cut-top cut-bottom").text.split()
                all_information.append(inform[3])

        return all_information


# If you need to analytic from all country all only your city
# You have to change link in methods like this example:
    # https://www.work.ua/ru/jobs-kyiv-data+analyst/
    # https://www.work.ua/ru/jobs-data+analyst/
