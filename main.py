import requests
from bs4 import BeautifulSoup

all_jobs = []


# def scrape_page(url):
#     print(f"Scraping {url}...")
#     response = requests.get(url)

#     soup = BeautifulSoup(response.content, "html.parser")

#     jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

#     for job in jobs:
#         title = job.find("span", class_="title").text
#         company, position, region = job.find_all("span", class_="company")[0:3]
#         job_data = {
#             "title": title,
#             "company": company.text,
#             "position": position.text,
#             "region": region.text,
#         }
#         all_jobs.append(job_data)


# def get_pages(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
#     return len(soup.find("div", class_="pagination").find_all("span", class_="page"))


# total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")

# for x in range(total_pages):
#     url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
#     scrape_page(url)

# print(len(all_jobs))

keywords = ["flutter", "python", "golang"]


def scrape_jobs_by_keyword(keyword):
    r = requests.get(
        f"https://remoteok.com/remote-{keyword}-jobs",
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        },
    )

    soup = BeautifulSoup(r.content, "html.parser")

    jobs = soup.find("table", id="jobsboard").find_all("tr", class_="job")

    for job in jobs:
        company = job.find("td", class_="company")
        title = company.find("h2", itemprop="title").text
        company_name = company.find("h3", itemprop="name").text
        job_data = {
            "title": title,
            "company": company_name,
        }
        all_jobs.append(job_data)

    print(f"Scraped {len(jobs)} {keyword} jobs")
    print(all_jobs)


scrape_jobs_by_keyword("flutter")
scrape_jobs_by_keyword("python")
scrape_jobs_by_keyword("golang")
