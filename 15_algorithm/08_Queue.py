## 함수

## 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

## 메인
#1. enqueue()
rear += 1
queue[rear] = '화사'
rear += 1
queue[rear] = '솔라'
rear += 1
queue[rear] = '문별'
print('출구<--',queue,'<--입구')

#2. dequeue() : 추출
front += 1
data = queue[front]
queue[front] = None
print('식사 손님: ',data)
front += 1
data = queue[front]
queue[front] = None
print('식사 손님: ',data)
front += 1
data = queue[front]
queue[front] = None
print('식사 손님: ',data)
print('출구<--',queue,'<--입구')