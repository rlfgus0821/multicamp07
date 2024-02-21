# list 메소드(함수)

#1. appemd() : 리스트 맨 뒤에 항목을 추가

a = []
a.append('apple')
a.append('hotdog')
a.append('banana')
a.append('melon')
print(f'alist = {a}')

#2. pop([idex]) : 리스트 index를 사용하지 않으면 맨 마지막 요소를 추출, 제거 (꺼내다)
value = a.pop()
print(f'alist : pop 적용 {a}', f'value={value}')
a.pop(0)
print(f'alist : a.pop(0) {a.pop(0)}', f'pop적용 후{a}')

#3. sort() : 리스트의 요소들을 정렬하여 정렬된 리스트로 변경
b = [6,3,5,1,-3]
print(f'blist : {b}')
b.sort()
print(f'sort적용 후 : {b}')

#4. reverse() : 리스트를 역순으로 변경
b.reverse()
print(f'reverse적용 후 : {b}')
print(f'reverse적용 후 : {a}')

#5. index() : 리스트에서 지정한 값의 위치를 반환, 값이 없는 경우 에러 발생
c = ['김','장','최','박','정','김']
idx = c.index('장')
print(idx)

#6. insert(위치, 값) : 리스트에 값(요소) 삽입
print(f'insert 전 {c}')
c.insert(-2, '원')
print(f'insert 후 {c}')

#7. remove(값) : 리스트에서 지정한 값을 제거, 첫번째 값만 제거
print(f'remove("김") 전 {c}')
c.remove('김')
print(f'remove("김") 후  {c}')

#8. count(값) : 리스트에서 해당 값의 개수를 반환
for i in range(c.count('김')):
    c.remove('김')
    print(f'김 삭제 {c}')
print(f'c.remove("김") 후 {c}')

#9. extend() : 리스트와 리스트를 합쳐 => 하나의 리스트로 변경
print(f'alist = {a}, blist = {b}')
b.extend([10,11,12])
print(f'b.extend([10,11,12]) 적용 후 blist = {b}')
b.append([10,11,12])
print(f'b.append([10,11,12]) 적용 후 blist = {b}')
b.insert(3,[10,11,12])
print(f'b.insert(3,[10,11,12]) 적용 후 blist = {b}')

#10. sorted(기본값: reverse=False) 내장함수 : 리스트를 정렬한 새로운 리스트 반환
b = [1,2,3,6,5,4]
print(f'sorted(b)전 {b}')
newb = sorted(b, reverse=True) # reverse=True -> 역순
print(f'sorted(b)후 {b}')
print(f'sorted(b)로 생성된 {newb}')

#11. copy() : 리스트 복사
cpb= b.copy()
print(cpb)
cpb.sort()
print(cpb)

#12. clear() : 리스트를 비우기 == a[:] = []
cpb.clear()
print(cpb)

#13. del() : 리스트 요소 지우기, 리스트 전체 지우기
cpa = a.copy()
print(f'cpa')
del(cpa[1:3])
print(f'del(cpa[1:3])한 후 {cpa}')
del cpa #메모리에서 제거

#14. len() : 리스트의 길이
c = [1,2,3,4,5,6,7,8,9]
c.append('5,4,3,2,1')
print(c)
print(len(c))