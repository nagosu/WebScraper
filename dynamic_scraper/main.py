import time
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import csv

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

# page.click(
#     "button.Aside_searchButton__Xhqq3.Aside_isNotMobileDevice__WuwWh"
# )  # 검색창 클릭
# page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")  # 검색어 입력
# page.keyboard.down("Enter")  # 엔터키 입력

# time.sleep(5)

# page.click(
#     "a#search_tab_position",
# )  # 포지션 탭 클릭


# 키워드로 구인공고 정보 가져오기
def get_jobs_csv_by_keyword(keyword):
    page.goto(
        f"https://www.wanted.co.kr/search?query={keyword}&tab=position"
    )  # 원하는 페이지로 이동

    for x in range(4):
        page.keyboard.down("End")  # 페이지 끝까지 스크롤
        time.sleep(1.5)  # 1.5초 대기

    page_content = page.content()  # 페이지 소스 가져오기

    time.sleep(5)  # 5초 대기

    # browser.close()  # 브라우저 종료

    # p.stop()  # Playwright 종료

    soup = BeautifulSoup(page_content, "html.parser")  # BeautifulSoup 객체 생성

    jobs = soup.find_all(
        "div", class_="JobCard_container__FqChn"
    )  # 구인공고 정보가 담긴 div 태그 찾기

    jobs_db = []  # 구인공고 정보를 담을 리스트

    for job in jobs:
        link = f"https://www.wanted.co.kr/{job.find('a')['href']}"  # 구인공고 링크
        title = job.find("strong", class_="JobCard_title__ddkwM").text  # 제목
        company = job.find("span", class_="JobCard_companyName__vZMqJ").text  # 회사명
        reward = job.find("span", class_="JobCard_reward__sdyHn").text  # 보상
        job = {
            "title": title,
            "company": company,
            "reward": reward,
            "link": link,
        }
        jobs_db.append(job)  # 구인공고 정보를 리스트에 추가

    file = open(f"{keyword}_jobs.csv", "w")  # csv 파일 생성
    writer = csv.writer(file)  # csv writer 객체 생성
    writer.writerow(
        [
            "Title",
            "Company",
            "Reward",
            "Link",
        ]
    )  # csv 파일 헤더 추가

    for job in jobs_db:
        writer.writerow(job.values())  # 구인공고 정보를 csv 파일에 추가

    file.close()  # csv 파일 닫기


keywords = ["flutter", "nextjs", "kotlin"]

for keyword in keywords:
    get_jobs_csv_by_keyword(keyword)  # 키워드로 구인공고 정보 가져오기

browser.close()

p.stop()
