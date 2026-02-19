import pandas as pd
import numpy as np
import random

# 데이터 생성 설정
np.random.seed(42)
n_samples = 2000

# 1. 기본 데이터 생성
data = {
    'RID': [f'R{i:05d}' for i in range(n_samples)],
    'Time_Departure': pd.date_range(start='2023-01-01', periods=n_samples, freq='h').astype(str),
    'Distance': np.random.uniform(1000, 300000, n_samples),  # 1km ~ 300km
    'Weekday': np.random.choice(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], n_samples),
    'Hour': np.random.randint(0, 24, n_samples),
    'Day': np.random.randint(1, 31, n_samples),
    'Signaltype': np.random.randint(0, 50, n_samples)
}

df = pd.DataFrame(data)

# 2. Time_Arrival 생성 (의미 없는 데이터지만 형식 맞춤)
df['Time_Arrival'] = pd.to_datetime(df['Time_Departure']) + pd.to_timedelta(np.random.randint(30, 300, n_samples), unit='m')

# 3. Speed_Per_Hour (평균 시속) 생성 - 정규분포
df['Speed_Per_Hour'] = np.random.normal(60, 20, n_samples)
df['Speed_Per_Hour'] = df['Speed_Per_Hour'].clip(10, 150) # 10~150 사이로 제한

# 4. 이상치 주입 (문제 6번: 시속 300 초과)
outlier_indices = np.random.choice(df.index, 5, replace=False)
df.loc[outlier_indices, 'Speed_Per_Hour'] = np.random.uniform(310, 400, 5)

# 5. Time_Driving (실주행시간) 계산 = 거리 / 속도 (초 단위 변환)
# (Distance는 m, Speed는 km/h -> m/s 변환 필요)
# Speed(m/s) = Speed(km/h) / 3.6
speed_ms = df['Speed_Per_Hour'] / 3.6
df['Time_Driving'] = df['Distance'] / speed_ms
df['Time_Driving'] = df['Time_Driving'].astype(int)

# 6. Address1 생성 (문제 3번: 경기도가 가장 많음, '-' 존재)
add1_choices = ['경기도', '서울특별시', '인천광역시', '충청남도', '강원도', '-']
add1_probs = [0.4, 0.3, 0.1, 0.1, 0.05, 0.05] # 경기도가 제일 많게 설정
df['Address1'] = np.random.choice(add1_choices, n_samples, p=add1_probs)

# 7. Address2 (더미 데이터)
df['Address2'] = ['상세주소' + str(i) for i in range(n_samples)]

# 8. 결측치 주입 (문제 7번)
# Distance 컬럼 등에 결측치 임의 삽입
df.loc[np.random.choice(df.index, 20), 'Distance'] = np.nan
df.loc[np.random.choice(df.index, 10), 'Time_Driving'] = np.nan

# CSV 저장
df.to_csv('signal_data.csv', index=False)
print("signal_data.csv 파일이 생성되었습니다.")