# Job Scrapper

![image](https://github.com/user-attachments/assets/3f4d2b2d-4745-438b-8dd8-7b0d5993dba6)


## 소개
- 구직 정보를 편리하게 모아서 확인할 수 있는 간단한 웹 애플리케이션입니다.

## 주요 기능
- 사용자가 입력한 키워드와 관련된 구직 정보를 3개의 구직 사이트([We Work Remotely](https://weworkremotely.com/), [Berlin Startup Jobs](https://berlinstartupjobs.com/), [Web3.career](https://web3.career/))에서 스크래핑합니다.
- 검색 결과를 CSV 파일로 저장할 수 있습니다.

## 디렉토리 구성
```
├── main.py           # Flask 서버의 메인 엔트리 포인트
├── file.py           # 검색 결과를 CSV로 저장하는 유틸리티 함수
├── bsj.py            # Berlin Startup Jobs 스크래퍼
├── wwr.py            # We Work Remotely 스크래퍼
├── web3.py           # Web3.career 스크래퍼(Playwright 사용)
├── requirements.txt  
└── templates
    ├── home.html     # 홈(키워드 입력) 페이지
    ├── search.html   # 검색 결과 페이지
    └── error.html    # 에러 발생 시 렌더링되는 페이지
```

## 테스트
- [replit 주소](https://replit.com/@castellina/AjarTrainedCable#main.py)에서 App Remix 후 실행

![image](https://github.com/user-attachments/assets/1cbdd87f-99b0-4544-884e-afa786e8f0a3)
