from flask import Flask, render_template, request, redirect, send_file
from extractors.wwr import extract_wwr_jobs
from extractors.bsj import extract_bsj_jobs
from extractors.web3 import extract_web3_jobs
from file import save_to_file

'''
  web3의 경우 VSCode에서 크롤링 후 파일로 저장되는것까지 확인했는데 replit 상에서 사용하려하면
  페이지 오류가 발생해서 일단 검색 결과에서 제외시켰습니다.
  근데 web3의 경우 크롤링을 위해서는 셀레니움이나 playwright를 쓰는게 맞는거같긴한데
  일정 페이지가 넘어가면 특정 항목의 selector가 바뀐다던지, 마감이 된 공고가 존재한다던지, 광고가 껴있어
  어려움이 있었습니다.
  일단 none값이 하나라도 존재하거나 마감 혹은 광고인 경우 제외시키는 방법으로(selector 사용) 진행했습니다.
  또한 5페이지가 넘어가는 항목들의 경우 위의 문제들에 대부분 해당하기도하고, 
  크롤링하는데 너무 많은 시간이 걸려 web3의 경우 4페이지까지만 크롤링하도록 했습니다.
'''

app = Flask("JobScrapper")


@app.route("/")
def home():
  return render_template("home.html")


db = {}


@app.route("/search")
def search():
  try:
    keyword = request.args.get("keyword", "").strip()
    if not keyword:
      return redirect("/")
    if keyword in db:
      jobs = db[keyword]
    else:
      bsj = extract_bsj_jobs(keyword)
      wwr = extract_wwr_jobs(keyword)
      web3 = extract_web3_jobs(keyword)
      jobs = bsj + wwr + web3
      db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)
  except Exception as e:
    return render_template("error.html", error=str(e))


@app.route("/export")
def export():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")
  if keyword not in db:
    return redirect(f"/search?keyword={keyword}")
  save_to_file(keyword, db[keyword])
  return send_file(f"{keyword}.csv", as_attachment=True)


if __name__ == "__main__":
  app.run("0.0.0.0", debug=False)
