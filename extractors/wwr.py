import requests
from bs4 import BeautifulSoup


def extract_wwr_jobs(keyword):
    try:
        url = f"https://weworkremotely.com/remote-jobs/search?term={keyword}"
        response = requests.get(
            url,
            headers={
                "User-Agent":
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            },
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("li", class_="feature")

        if not jobs:
            return []

        job_datas = []

        for job in jobs:
            try:
                if "feature--ad" in job.get("class", []):
                    continue

                job_data = {
                    "position":
                    job.find("span", class_="title").text.replace(',', '/'),
                    "company":
                    job.find("span", class_="company").text.replace(',', '/'),
                    "location":
                    job.find("span",
                             class_="region company").text.replace(',', '/'),
                    "link":
                    f"https://weworkremotely.com{job.find('a').get('href')}"
                }
                job_datas.append(job_data)
            except AttributeError:
                continue

        return job_datas

    except requests.RequestException:
        return []
