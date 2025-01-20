import requests
from bs4 import BeautifulSoup


def extract_bsj_jobs(keyword):
    try:
        url = f"https://berlinstartupjobs.com/skill-areas/{keyword}"
        response = requests.get(
            url,
            headers={
                "User-Agent":
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            },
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        jobs_list = soup.find("ul", class_="jobs-list-items")

        if not jobs_list:
            return []

        jobs = soup.find("ul", class_="jobs-list-items").find_all("li")
        job_datas = []

        for job in jobs:
            try:
                position = job.find("h4", class_="bjs-jlid__h")
                if not position:
                    continue

                job_data = {
                    "position":
                    position.text.replace(',', '/'),
                    "company":
                    job.find("a", class_="bjs-jlid__b").text.replace(',', '/'),
                    "location":
                    "Berlin",
                    "link":
                    position.find("a").get("href")
                }
                job_datas.append(job_data)
            except AttributeError:
                continue

        return job_datas

    except requests.RequestException:
        return []
