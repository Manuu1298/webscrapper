import csv
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def parse_web_page(url):
    options = Options()
    options.add_argument('--headless')
    driver_path = './chromedriver'
    driver = webdriver.Chrome(options=options, executable_path=driver_path)
    driver.get(url)
    page_source = driver.page_source
    driver.quit()
    soup = BeautifulSoup(page_source, 'html.parser')
    text = ' '.join([element.get_text() for element in soup.find_all(text=True)])
    return text

def find_keywords(parsed_text, keywords, url):
    found_keywords = []
    parsed_text = parsed_text.lower()
    keywords = [keyword.lower() for keyword in keywords]
    for keyword in keywords:
        if keyword in parsed_text:
            found_keywords.append(keyword)
    return found_keywords

def process_url(url):
    parsed_text = parse_web_page(url)
    found_keywords = find_keywords(parsed_text, keyword_list, url)
    if found_keywords:
        output_row = [url, ', '.join(found_keywords)]
    else:
        output_row = [url, 'No openings found']
    return output_row

# URLs to search for job openings
urls = [


]



# Positions to search for
keyword_list = [    
    "software developer",
    "software engineer",
    "software architect",
    "application developer",
    "systems developer",
    "web developer",
    "mobile app developer",
    "front-end engineer",
    "back-end engineer",
    "full-stack engineer",
    "frontend engineer",
    "backend engineer",
    "fullstack engineer",
    "front end engineer",
    "back end engineer",
    "full stack engineer",
    "front-end developer",
    "back-end developer",
    "full-stack developer",
    "frontend developer",
    "backend developer",
    "fullstack developer",
    "front end developer",
    "back end developer",
    "full stack developer",
    "UI/UX developer",
    "database developer",
    "game developer",
    "AI/ML developer",
    "machine learning developer",
    "artificial intelligence developer",
    "data scientist",
    "cloud developer",
    "cloud Engineer",
    "DevOps engineer",
    "software analyst",
    "software tester",
    "software consultant",
    "software development specialist",
    "software development engineer",
    "software development manager",
    "data analyst",
    "data architect",
    "big data",
    "database engineer",
    "database administrator",
    "database architect",
    "database manager",
    "database specialist",
    "database programmer",
    "database designer",
]


output_rows = []

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(process_url, urls)
    for result in results:
        output_rows.append(result)

filename = 'jobopenings_HPS.csv'
header = ['Companies', 'Possible Job Openings']

with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(output_rows)

print(f"Output saved to {filename} file.")