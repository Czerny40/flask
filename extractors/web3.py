from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

def extract_web3_jobs(keyword):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    current_page = 1
    job_datas = []

    while current_page < 5:
        time.sleep(0.5)
        page.goto(f"https://web3.career/{keyword}-jobs?page={current_page}")
        time.sleep(0.5)
        
        rows = page.locator("tr.table_row:not([id^='sponsor'])")
        count = rows.count()

        if count == 0:
            break

        # print(f"페이지 {current_page} 크롤링 중...")

        for i in range(count):
            rows.nth(i).click()
            time.sleep(0.5)
            
            content = page.content()
            soup = BeautifulSoup(content, "html.parser")
        
            job_status = soup.select_one('#job > div > div > header > div.mt-2 > div > div > p')
            if job_status:
                continue
            
            position = soup.select_one('#job > div > div > header > div.d-flex.justify-content-between > div.d-flex.justify-content-start.gap-3 > div:nth-child(2) > a > h2')
            company = soup.select_one('#job > div > div > header > div.mt-2 > div > a')
            location = soup.select_one('#job > div > div > header > div.mt-2 > div > div > div.text-start.my-1.d-md-flex.justify-content-start.gap-3.d-none > div')
            link = soup.select_one('#job > div > div > header > div.d-flex.justify-content-between > div:nth-child(2) > a')

            # 하나라도 None이면 건너뛰기
            if not all([position, company, location, link]):
                continue

            job_info = {
                'position': position.text.strip(),
                'company': company.text.strip(),
                'location': location.text.strip().replace(',', '/'),
                'link': link['href'].strip(),
            }

            # print(job_info)
            job_datas.append(job_info)
            time.sleep(0.5)
            
        current_page += 1

    browser.close()
    return job_datas
