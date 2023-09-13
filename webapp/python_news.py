import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except (requests.RequestException, ValueError):
        print ("Сетевая ошибка")
        return False

def get_python_news():
    html = get_html("https://www.python.org/")
    if html:
        soup = BeautifulSoup(html, "html.parser")
        all_news = soup.find("div", class_= "shrubbery").find_all("li")
        result_news = []
        for new_list in all_news:
            title = new_list.find("a").text
            url = new_list.find("a")["href"]
            published = new_list.find("time").text
            result_news.append({
                "title":title,
                "url":url ,
                "published": published
            })
        return result_news
    return False    

print(type(get_python_news()))