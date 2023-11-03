# 10주차 정리

import os

if not os.path.exists('./results'):
    os.makedirs('./results')

#### Line Chart
import matplotlib.pyplot as plt

#데이터 생성
x=[1,2,3,4,5]
y=[10,15,13,18,20]

plt.plot(x,y,marker='o',linestyle='-',color='b',label='temperature')
# marker : 데이터 점에 마커 표시
# linestyle : 선 스타일 (옵션)
# color : 선 색상 (옵션)
# label : 범례에 표시 될 이름

# #그래프에 제목 추가
plt.title('Daily temperature tread')
#
# 축 레이블 추가
plt.xlabel('Time (hour)')
plt.ylabel('Temperature(C)')
#
# 범례 표시
plt.legend
#
# 그래프 표시
plt.grid(True)
#plt.show()
plt.savefig("./results/linechart.png")



#### Bar chart
import matplotlib.pyplot as plt

# 데이터 생성
categories =['Apple','Banana','Orange','Strawberry','Grape']
values = [25,30,15,20,35]

plt.clf()

plt.bar(categories,values,color='skyblue')

plt.title('Fruit Sales')

plt.xlabel('Fruit')
plt.ylabel('Sales')

plt.savefig("./results/bar_chart.png")


#### Histogram chart
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

plt.clf()

plt.hist(data,bins=20, color='skyblue',edgecolor='black')

plt.title('Histogram chart')

plt.xlabel('Values')
plt.ylabel('Frequency')

plt.savefig('./results/histogram.png')

#### Pie chart
import matplotlib.pyplot as plt

#데이터 생성
labels = ['English','Math','Science','History']
sizes = [45,30,15,10]

plt.clf()

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightcoral', 'lightgreen', 'lightyellow'])

plt.title('subjects Distribution')

plt.savefig("./results/piechart.png")


#### Scatter chart
import matplotlib.pyplot as plt
import random

x=[random.uniform(0,100) for _ in range(1000)]
y=[random.uniform(0,100) for _ in range(1000)]

plt.clf()

plt.scatter(x,y,label='Random Data Points',color='green',marker='o',s=30, alpha=0.5)

plt.title('Scatter Plot Example')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()

plt.savefig("./results/scatter.png")

plt.close()

#### Scatter chart #2
import matplotlib.pyplot as plt
import random

x = [random.uniform(0, 100) for _ in range(200)]
y=[ 2 * val + 1 + random.uniform (-10,10) for val in x]

plt.clf()

plt.scatter(x,y,label='Scatter Plot', color ='blue', marker='o', s=30, alpha=0.5)

plt.title('Scatter Plot Example')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()

plt.savefig("./results/scatter_2.png")


#### Scatter chart with line
import matplotlib.pyplot as plt
import random

x= [random.uniform(0,100) for _ in range(200)]
y= [2 * val + 1 + random.uniform(-10,10) for val in x]

plt.clf()

plt.scatter(x,y,label='Scatter Plot', color='blue',marker='o',s=30,alpha=0.5)

x_line = range(101)
y_line = [2*val+1 for val in x_line]
plt.plot(x_line,y_line,label='y=2x+1',color='red')

plt.title('Scatter Plot Example')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()

plt.savefig("./results/scatter_with_line.png")

#### Boxplot
import matplotlib.pyplot as plt
import random
data = [random.gauss(0,1) for _ in range(100)]
outliers = [10,-10]

plt.clf()

plt.boxplot(data + outliers, vert=False, patch_artist=True)

plt.title('Values')

plt.xticks(range(-15,16,5))

plt.savefig("./results/boxplot.png")


#### Heatmap
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10,10)

plt.clf()

heatmap = plt.imshow(data, cmap='YlGnBu',aspect='auto')

plt.colorbar(heatmap)

plt.title('heatmap Example')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.savefig("./results/Heatmap.png")
