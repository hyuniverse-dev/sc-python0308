'''
파일명: csv_prac.py

<공공데이터를 활용해 월별 쵀대 승하차 인원을 가진 역 찾기>
    - 서울 지하철 월별 승하차 데이터를 분석하여 각 달에 가장 많은 승하차 인원을 가진 역을 찾는 프로그램입니다.
    - /data/subway.csv 파일을 사용합니다.
'''
import csv

# csv 파일 읽기
with open("../data/subway.csv", "r", encoding="utf-8") as file:
    # csv 모듈을 사용해서 파일 읽어오기
    csv_reader = csv.reader(file)

    # 헤더 삭제 - next() 함수 사용
    next(csv_reader)

    # 1. 파일 전체 데이터 읽기
    # for row in csv_reader:
    #     # 수송연월 데이터
    #     transport_date = row[4]
    #     # 역 이름
    #     station_name = row[3]
    #     # 승하차 인원수
    #     passenger_count = row[5]

    # print(f"연월: {transport_date}, 역명: {station_name}, 승하차 인원수: {passenger_count}")

    # 2. 특정 월의 최대 승하차 인원 역 찾기 (2023-01)

    max_station_name = ""
    max_count = 0
    user_input = int(input("검색할 월을 입력하세요 >>> "))

    # 1 ~ 9월까지는 앞에 0을 붙여주고 그게 아니면 2자리 수를 그대로 사용
    if 1 <= user_input <= 9:
        user_input = f"0{user_input}"

    for row in csv_reader:
        # 수송연월 데이터
        transport_date = row[4]
        # 역 이름
        station_name = row[3]
        # 승하차 인원수
        passenger_count = int(row[5])

        # 특정 월 조건
        if transport_date == f"2023-{user_input}" and passenger_count > max_count:
            # 직전 역보다 현재 역이 더 많은 승하차 인원을 가지고 있는 확인
            max_count = passenger_count
            max_station_name = station_name

    print(f"2023-{user_input}월에 가장 많은 승하차 인원을 가진 역: {max_station_name}({max_count}명)")

# 3. 모든 월에 대해 최대 승하차 인원을 가진 역 찾기

monthly_max_station = {}
monthly_max_station_list = []

with open("../data/subway.csv", "r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader:
        station_name = row[3]
        transport_date = row[4]
        passenger_count = int(row[5])

        # 각 월에 대해 최대 승하차 역 찾기
        if transport_date not in monthly_max_station or passenger_count > monthly_max_station[transport_date][
            "passenger"]:
            monthly_max_station[transport_date] = {
                "station": station_name,
                "passenger": passenger_count
            }
            monthly_max_station_list.append({
                "station": station_name,
                "passenger": passenger_count
            })
    
    # 딕셔너리 내부의 값을 언패킹하여 사용하기
    for month, data in monthly_max_station.items():
        print(f"{month}월: {data['station']}({data['passenger']})")
