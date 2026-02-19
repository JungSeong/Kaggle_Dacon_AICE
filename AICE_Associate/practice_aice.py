import nbformat as nbf

# 빈 노트북 생성
nb = nbf.v4.new_notebook()

# 문제 및 코드 셀 정의
cells = []

# --- 제목 ---
cells.append(nbf.v4.new_markdown_cell("""# AICE Associate 자격인증 샘플문항
이 노트북은 AICE Associate 샘플문항의 문제 풀이용 파일입니다.
각 문항의 가이드를 읽고 답안 코드를 작성하세요.
"""))

# --- 문제 1 ---
cells.append(nbf.v4.new_markdown_cell("""### [문항 1]
Pandas는 데이터 분석을 위해 널리 사용되는 파이썬 라이브러리입니다.
[cite_start]Pandas를 사용할 수 있도록 별칭(alias)을 pd로 해서 불러오세요. [cite: 25, 26]
"""))
cells.append(nbf.v4.new_code_cell("# 여기에 답안코드를 작성하세요.\n"))

# --- 문제 2 ---
cells.append(nbf.v4.new_markdown_cell("""### [문항 2]
AI 모델링을 위해 분석 및 처리할 데이터 파일을 읽어오려고 합니다.
[cite_start]Pandas 함수로 데이터 파일을 읽어 데이터프레임 변수 **df**에 할당하는 코드를 작성하세요. [cite: 28, 29]

* **데이터프레임 변수명:** df
* [cite_start]**데이터 파일명:** signal_data.csv (csv 파일은 본 문제/답안지와 동일한 경로에 있습니다.) [cite: 30, 31]
"""))
cells.append(nbf.v4.new_code_cell("# 여기에 답안코드를 작성하세요.\n"))

# --- 사전 설정 코드 (실행 필요) ---
cells.append(nbf.v4.new_markdown_cell("""### [필수 실행]
[cite_start]다음 문항을 풀기 전에 아래 코드를 반드시 실행하세요. [cite: 33]
"""))
code_setup = """import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 폰트 설정 (환경에 맞게 변경 가능, 예: NanumGothicCoding, Malgun Gothic 등)
plt.rc('font', family='Malgun Gothic') 
plt.rcParams['axes.unicode_minus'] = False

import warnings
warnings.filterwarnings('ignore')"""
cells.append(nbf.v4.new_code_cell(code_setup))

# --- 문제 3 ---
cells.append(nbf.v4.new_markdown_cell("""### [문항 3]
Address1(주소1)에 대한 분포도를 알아 보려고 합니다.
[cite_start]Address1(주소1)에 대해 countplot그래프로 만드는 코드와 답안을 작성하세요. [cite: 39, 40]

* **대상 데이터프레임:** df
* [cite_start]**Seaborn을 활용하세요.** [cite: 42]
* [cite_start]첫번째, Address1(주소1)에 대해서 분포를 보여주는 countplot 그래프 그리세요. [cite: 43]
* [cite_start]두번째, Address1(주소1)에 지역명이 없는 '-'에 해당되는 row(행)을 삭제하세요. [cite: 44]
* [cite_start]출력된 그래프를 보고 해석한 것으로 옳지 않은 선택지를 아래에서 골라 '**답안03**' 변수에 저장하세요.(예. 답안03 = 4) [cite: 45]

**[보기]**
1. [cite_start]Countplot 그래프에서 Address1(주소1) 분포를 확인시 '경기도' 분포가 제일 크다. [cite: 47]
2. [cite_start]Address1(주소1) 분포를 보면 '인천광역시' 보다 '서울특별시'가 더 크다. [cite: 48]
3. [cite_start]지역명이 없는 '-'에 해당되는 row(행)가 2개 있다. [cite: 49]
"""))
cells.append(nbf.v4.new_code_cell("# 여기에 답안코드를 작성하세요.\n"))

# --- 문제 4 ---
cells.append(nbf.v4.new_markdown_cell("""### [문항 4]
컬럼들간의 상관관계를 파악하고자 합니다.
[cite_start]가이드에 따라 컬럼들의 상관관계를 구하는 코드의 빈칸을 채우고 답안을 작성하세요. [cite: 51, 52]

* **대상 데이터프레임:** df
* 특정 컬럼에 대한 상관관계를 구하는 코드는 주어집니다.
* [cite_start]코드의 빈칸 **'< blank1 >'**을 채우고, 반드시 코드를 실행하세요. [cite: 55]
* 코드의 빈칸 **'< blank1 >'** 값을 '**답안04_1**' 변수에 저장하세요. [cite_start]예) 답안04_1 = '함수명' [cite: 56]
* 출력된 상관관계 테이블을 보고 이동 거리(Distance) 컬럼과 상관관계가 가장 높은 컬럼을 '**답안04_2**' 변수에 저장하세요. [cite_start]예) 답안04_2 = 'Distance' [cite: 57]
"""))
code_q4 = """# 여기에 질문답안과 답안코드를 작성하세요. 그리고 '<blank>' 채우고 코드를 실행하세요.
column_list = ['Distance', 'Time_Driving', 'Speed_Per_Hour', 'Weekday', 'Hour', 'Day', 'Signaltype']

# df[column_list].< blank1 >  <-- 이 부분을 채워서 실행하세요."""
cells.append(nbf.v4.new_code_cell(code_q4))

# --- 문제 5 ---
cells.append(nbf.v4.new_markdown_cell("""### [문항 5]
실주행시간과 평균시속의 분포를 같이 확인하려고 합니다.
[cite_start]Time_Driving(실주행시간)과 Speed_Per_Hour(평균시속)을 jointplot그래프로 만드세요. [cite: 60, 61]

* **대상 데이터프레임:** df
* [cite_start]**Seaborn을 활용하세요.** [cite: 63]
* [cite_start]X축에는 Time_Driving(실주행시간)을 표시하고 Y축에는 Speed_Per_Hour(평균시속)을 표시하세요. [cite: 64]
"""))
cells.append(nbf.v4.new_code_cell("# 여기에 답안코드를 작성하세요.\n"))

# --- 문제 6 ---
cells.append(nbf.v4.new_markdown_cell("""### [문항 6]
위의 jointplot 그래프에서 시속 300이 넘는 이상치를 발견할수 있습니다.
[cite_start]가이드에 따라서 전처리를 수행하고 저장하세요. [cite: 66, 67]

* **대상 데이터프레임:** df
* [cite_start]jointplot 그래프를 보고 시속 300 초과하는 이상치를 찾아 해당 행(Row)을 삭제하세요. [cite: 69]
* [cite_start]불필요한 'RID' 컬럼을 삭제 하세요. [cite: 70]
* [cite_start]전처리 반영 후에 데이터프레임 변수명 **df_temp** 에 저장하세요. [cite: 71]
"""))
cells.append(nbf.v4.new_code_cell("# 여기에 답안코드를 작성하세요.\n"))

# --- 문제 7 ---
cells.append(nbf.v4.new_markdown_cell("""### [문항 7]
모델링 성능을 제대로 얻기 위해서 결측치 처리는 필수입니다.
[cite_start]아래 가이드를 따라 결측치 처리하세요. [cite: 73, 74]

* **대상 데이터프레임:** df_temp
* [cite_start]각 컬럼의 결측치 개수를 확인하는 코드를 작성하세요. [cite: 76]
* [cite_start]결측치가 있는 행(row)를 삭제 하세요. [cite: 77]
* [cite_start]전처리 반영된 결과를 데이터프레임 변수명 **df_na**에 저장하세요. [cite: 78]
* [cite_start]결측치 개수를 '**답안07**' 변수에 저장하세요.(예. 답안07 = 5) [cite: 79]
"""))
cells.append(nbf.v4.new_code_cell("# 여기에 답안코드를 작성하세요.\n"))

# --- 문제 8 ---
cells.append(nbf.v4.new_markdown_cell("""### [문항 8]
모델링 성능을 제대로 얻기 위해서 불필요한 변수는 삭제해야 합니다.
[cite_start]아래 가이드를 따라 불필요 데이터를 삭제 처리하세요. [cite: 81, 82]

* **대상 데이터프레임:** df_na
* [cite_start]'Time_Departure', 'Time_Arrival' 2개 컬럼을 삭제하세요. [cite: 84]
* [cite_start]전처리 반영된 결과를 새로운 데이터프레임 변수명 **df_del** 에 저장하세요. [cite: 85]
"""))
cells.append(nbf.v4.new_code_cell("# 여기에 답안코드를 작성하세요.\n"))

# --- 문제 9 ---
cells.append(nbf.v4.new_markdown_cell("""### [문항 9]
원-핫 인코딩(One-hot encoding)은 범주형 변수를 1과 0의 이진형 벡터로 변환하기 위하여 사용하는 방법입니다.
[cite_start]원-핫 인코딩으로 아래 조건에 해당하는 컬럼 데이터를 변환하세요. [cite: 87, 88]

* **대상 데이터프레임:** df_del
* [cite_start]**원-핫 인코딩 대상:** object 타입의 전체 컬럼 [cite: 90]
* [cite_start]**활용 함수:** Pandas의 get_dummies [cite: 91]
* [cite_start]해당 전처리가 반영된 결과를 데이터프레임 변수 **df_preset**에 저장해 주세요. [cite: 92]
"""))
cells.append(nbf.v4.new_code_cell("# 여기에 답안코드를 작성하세요.\n"))

# --- 문제 10 ---
cells.append(nbf.v4.new_markdown_cell("""### [문항 10]
훈련과 검증 각각에 사용할 데이터셋을 분리하려고 합니다.
[cite_start]Time_Driving(실주행시간) 컬럼을 label값 y로, 나머지 컬럼을 feature값 X로 할당한 후 훈련데이터셋과 검증데이터셋으로 분리하세요(대소문자 유의). [cite: 94-96]
[cite_start]추가로, 가이드 따라서 훈련데이터셋과 검증데이터셋에 스케일링을 수행하세요. [cite: 97]

* **대상 데이터프레임:** df_preset
* **훈련과 검증 데이터셋 분리**
    * [cite_start]훈련 데이터셋 label: y_train, 훈련 데이터셋 Feature: X_train [cite: 100]
    * [cite_start]검증 데이터셋 label: y_valid, 검증 데이터셋 Feature: X_valid [cite: 101]
    * [cite_start]훈련 데이터셋과 검증데이터셋 비율은 80:20 [cite: 102]
    * [cite_start]random_state: 42 [cite: 103]
    * [cite_start]Scikit-learn의 train_test_split 함수를 활용하세요. [cite: 104]
* [cite_start]**RobustScaler 스케일링 수행** [cite: 105]
    * [cite_start]sklearn.preprocessing의 RobustScaler 함수 사용 [cite: 106]
    * [cite_start]훈련데이터셋의 Feature는 RobustScaler의 fit_transform 함수를 활용하여 X_train 변수로 할당 [cite: 107]
    * [cite_start]검증데이터셋의 Feature는 RobustScaler의 transform 함수를 활용하여 X_valid 변수로 할당 [cite: 108]
"""))
cells.append(nbf.v4.new_code_cell("# 여기에 답안코드를 작성하세요.\n"))

# --- 문제 11 ---
cells.append(nbf.v4.new_markdown_cell("""### [문항 11]
Time_Driving(실주행시간)을 예측하는 머신러닝 모델을 만들려고 합니다.
[cite_start]아래 가이드에 따라 의사결정나무(decision tree)와 랜덤포레스트(Random Forest) 모델 만들고 학습을 진행하세요. [cite: 110-114]

* **의사결정나무(decision tree)**
    * [cite_start]트리의 최대 깊이: 5로 설정 [cite: 116]
    * [cite_start]노드를 분할하기 위한 최소한의 샘플 데이터수(min_samples_split): 3로 설정 [cite: 117]
    * [cite_start]random_state: 120로 설정 [cite: 118]
    * [cite_start]의사결정나무(decision tree) 모델을 **dt** 변수에 저장해 주세요. [cite: 119]
* **랜덤포레스트(Random Forest)**
    * [cite_start]트리의 최대 깊이: 5로 설정 [cite: 121]
    * [cite_start]노드를 분할하기 위한 최소한의 샘플 데이터수(min_samples_split): 3로 설정 [cite: 122]
    * [cite_start]random_state: 120로 설정 [cite: 122]
    * [cite_start]랜덤포레스트(Random Forest) 모델을 **rf** 변수에 저장해 주세요. [cite: 123]
* **위의 2개의 모델에 대해 fit을 활용해 모델을 학습해 주세요. [cite_start]학습 시 훈련데이터 셋을 활용해 주세요.** [cite: 124]
"""))
cells.append(nbf.v4.new_code_cell("# 여기에 답안코드를 작성하세요.\n"))

# --- 문제 12 ---
cells.append(nbf.v4.new_markdown_cell("""### [문항 12]
위 의사결정나무(decision tree)와 랜덤포레스트(RandomForest) 모델의 성능을 평가하려고 합니다.
[cite_start]아래 가이드에 따라 예측 결과의 mae(Mean Absolute Error)를 구하고 평가하세요. [cite: 126, 127]

* [cite_start]**성능 평가는 검증 데이터셋을 활용하세요.** [cite: 128]
* [cite_start]11번 문제에서 만든 의사결정나무(decision tree) 모델로 y값을 예측(predict)하여 y_pred_dt에 저장하세요. [cite: 129]
* [cite_start]검증 정답(y_valid)과 예측값(y_pred_dt)의 mae(Mean Absolute Error)를 구하고 **dt_mae** 변수에 저장하세요. [cite: 130]
* [cite_start]11번 문제에서 만든 랜덤포레스트(Random Forest) 모델로 y값을 예측(predict)하여 y_pred_rf에 저장하세요. [cite: 131]
* [cite_start]검증 정답(y_valid)과 예측값(y_pred_rf)의 mae(Mean Absolute Error)를 구하고 **rf_mae** 변수에 저장하세요. [cite: 132]
* [cite_start]2개의 모델에 대한 mae 성능평가 결과을 확인하여 성능좋은 모델 이름을 '**답안12**' 변수에 저장하세요. [cite: 133]
    * [cite_start]예) 답안12 = 'decisiontree' 혹은 답안12 = 'randomforest' [cite: 134]
"""))
cells.append(nbf.v4.new_code_cell("# 여기에 답안코드를 작성하세요.\n"))

# --- 사전 설정 코드 (DL) ---
cells.append(nbf.v4.new_markdown_cell("""### [필수 실행]
[cite_start]다음 문항을 풀기 전에 아래 코드를 반드시 실행하세요. [cite: 137]
"""))
code_dl_setup = """import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Activation, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.utils import to_categorical

tf.random.set_seed(1)"""
cells.append(nbf.v4.new_code_cell(code_dl_setup))

# --- 문제 13 ---
cells.append(nbf.v4.new_markdown_cell("""### [문항 13]
Time_Driving(실주행시간)을 예측하는 딥러닝 모델을 만들려고 합니다.
[cite_start]아래 토폴로지 그림과 가이드에 따라 모델링하고 학습을 진행하는 코드를 작성하세요. [cite: 144, 145]

* [cite_start]Tensorflow framework를 사용하고 하단의 토폴로지 그림과 동일한 딥러닝 모델을 구현하세요. [cite: 146]
* [cite_start]히든 레이어의 activation 함수는 'selu'를 사용하고, 마지막 아웃풋 레이어의 activation 함수는 'linear'를 사용하세요. [cite: 147]
* [cite_start]EarlyStopping 콜백으로 9번 epoch 동안 모니터링 지표(val_loss)가 향상되지 않을 때 훈련을 중지하도록 설정하고 **estop** 변수에 저장하세요. [cite: 148]
* [cite_start]optimizer는 adam, metrics는 mse, loss는 mean_squared_error로 설정하여 모델 컴파일을 설정하세요. [cite: 149]
* [cite_start]다음 조건에 따라 모델을 학습하고 학습정보는 **history** 변수에 저장해 주세요. [cite: 150]
    * [cite_start]batch_size: 128 [cite: 151]
    * [cite_start]epoch: 50 [cite: 152]
* [cite_start]안내된 내용 외 별도의 파라미터를 입력하지 마시기 바랍니다. [cite: 153]

**[딥러닝 모델 토폴로지]**
* Input Layer
* [cite_start]Dense Layer (64 unit, selu) [cite: 158]
* [cite_start]Drop Out Layer [cite: 159]
* [cite_start]Dense Layer (32 unit, selu) [cite: 161]
* [cite_start]Dense Layer (16 unit, selu) [cite: 162]
* [cite_start]Output Layer (Dense, 1 unit, linear) [cite: 163]
"""))
cells.append(nbf.v4.new_code_cell("# 여기에 답안코드를 작성하세요.\n"))

# --- 문제 14 ---
cells.append(nbf.v4.new_markdown_cell("""### [문항 14]
위 딥러닝 모델의 성능을 평가하려고 합니다.
[cite_start]Matplotlib 라이브러리 활용해서 학습 mse와 검증 mse를 그래프로 표시하세요. [cite: 167, 168]

* [cite_start]1개의 그래프에 학습 mse과 검증 mse 2가지를 모두 표시하세요. [cite: 169]
* [cite_start]위 2가지 각각의 범례를 'mse', 'val_mse'로 표시하세요. [cite: 170]
* [cite_start]그래프의 타이틀은 'Model MSE'로 표시하세요. [cite: 171]
* [cite_start]X축에는 'Epochs'라고 표시하고 Y축에는 'MSE'라고 표시하세요. [cite: 172]
"""))
cells.append(nbf.v4.new_code_cell("# 여기에 답안코드를 작성하세요.\n"))

# --- 종료 ---
cells.append(nbf.v4.new_markdown_cell("""### 종료
1번부터 14번까지 모든 문제를 풀었습니다. 수고하셨습니다.
[cite_start]'최종제출 및 종료'를 클릭하셔서 답안을 제출해 주시기 바랍니다. [cite: 174, 175]
"""))

# 노트북에 셀 추가
nb['cells'] = cells

# 파일 저장
with open('AICE_Associate_Sample_Exam.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print("AICE_Associate_Sample_Exam.ipynb 파일이 생성되었습니다.")