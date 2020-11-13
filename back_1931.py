meeting = []                     # 회의 시간 목록 저장소
for i in range(int(input())):
    start,end = map(int,input().split())
    meet=[start,end]
    meeting.append(meet)         # 이중 리스트 형식으로 시간 저장

meeting.sort(key=lambda x:x[0])   # [2,2] 같이 시작시간과 끝시간이 똑같은 경우를 대비해서 시작시간 기준 정렬도 진행
meeting.sort(key=lambda x:x[1])   # 끝나는 시간으로 정렬할 경우 최단 알고리즘 만들기 가능

point = 0  # 다음 회의를 찾아줄 지표(끝나는 시간을 저장)
count = 0  # 총 회의 개수 

for i in meeting:
    if i[0] >= point: # 앞서 진행한 회의가 끝나는 시간보다 같거나 클 때 카운트해주고 지표를 바꿈
        point = i[1]
        count += 1
print(count)
