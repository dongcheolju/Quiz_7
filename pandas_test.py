import pandas as pd
data = {
    '학번' : range(2000, 2010)
    , '성적' : [85, 95, 75, 70, 100, 100, 95, 85, 80, 85]
}
print('일반')
print(pd.DataFrame(data))
print('----------------------------')
print('프레임 컬럼 순서 변경')
print(pd.DataFrame(data, columns = ['성적', '학번']))
print('----------------------------')
print('프레임 인덱스 나열 변경')
print(pd.DataFrame(data, columns = ['성적', '학번'], index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']))
print('행렬 변환')
print(pd.DataFrame(data, columns = ['성적', '학번'], index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']).transpose())

data = {
    '학번' : range(2000, 2010)
    , '성적' : [85, 95, 75, 70, 100, 100, 95, 85, 80, 85]
}

# 주요 통계 지표
frame = pd.DataFrame(data)
print(frame.describe())
print('---------------------------')
# 데이터 구조
print(frame.info())
print('---------------------------')
# 중복 제거
print(frame['성적'].unique())
print('---------------------------')
# Group by
print(frame['성적'].value_counts())

