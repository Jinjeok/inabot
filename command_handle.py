import data
import random
from datetime import datetime

class color: # print 색 지정
   purple = '\033[95m'
   cyan = '\033[96m'
   darkcyan = '\033[36m'
   blue = '\033[94m'
   green = '\033[92m'
   yellow = '\033[93m'
   red = '\033[91m'
   bold = '\033[1m'
   underline = '\033[4m'
   end = '\033[0m'

def command(): # 명령어 목록 출력 명령어
    print(chr(27) + "[2J") # screen clear code

    for i in data.command_list: # 명령어 목록 값을 반복
        print(color.bold + i['name'] + color.end) # 명령어 이름 출력
        print(': '+i['desc'] + '\n') # 명령어 설명 출력

    input('계속하려면 Enter를 입력해주세요.')

def selector(info:list): #selector 함수는 3가지의 info를 받음: 대분류(type), 이름(name), 명령어 이름(command)
    #'대분류'는 data.py에 있는 locaList 값에 저장된 최상위 key 값을 뜻 합니다: 'cafe', 'food', 'play', 'pub'가 있습니다.
    #'데이터'는 '대분류' 밑에 있는 locaList 값을 뜻합니다.
    #'타입'은 data.py에 있는 locaList list, type key의 value 값을 뜻합니다.

    def typeExtractor(li): # '데이터'의 '타입'을 return 하는 함수. 예) 양식, 양식, 일식, 일식 -> 양식 일식
        returnList = [] # return 할 'returnList' 변수 지정
        
        for i in li:
            if i['type'] in returnList: # 만약 'returnList'에 중복되는 '타입'값이 있다면 skip
                continue
            returnList.append(i['type']) # 새로운 type 값일 때 값을 'returnList' 추가

        return returnList # '타입' 값이 저장된 'returnList' return

    def numToType(nums,typelist): # 입력받은 '답변'값을 '타입' 문자열로 변환해주는 함수
        returnList = [] # return 할 'returnList' 변수 지정
        
        if(nums == '0'): # 입력받은 값이 '0.전부'일 때
            returnList = typelist # 'returnList'에 모든 '타입' 삽입

        else:
            nums = [int(n) for n in nums.split()] # '답변'값이 여러개일 수 있으므로, 공백을 기준으로 list로 나눈 후 int값으로 변경 
            for i in nums: # '답변' list 반복
                returnList.append(typelist[i-1]) # '답변'숫자와 '타입'의 index가 동일 할 경우, 그 '타입'값을 'returnList'에 저장

        return returnList # '답변'에 맞게 추출된 '타입'을 return

    def reduceNSelect(list, types): # '데이터'를 '답변''타입'에 맞게 추출해서 random을 return 하는 함수
        returnList = [] # return 할 'returnList' 변수 지정
        for val in list: # '데이터' 값을 기준으로 반복
            if val['type'] in types: # '답변''타입'에 포함된 '데이터' 값만 returnList에 저장
                returnList.append(val)

        return returnList[random.randint(0,len(returnList)-1)] # '답변''데이터' 중 무작위 하나를 골라서 return
    
    print(chr(27) + "[2J") # screen clear code

    print(info['command'] + ' 명령어 - 인하대 근처 '+ info['name'] +'을(를) 무작위로 하나 골라줍니다.') # 안내문 출력
    print('원하는 분류를 골라주세요. 다수 선택 시 공백을 포함해주세요.') # 안내문 출력
    print('예) 2번과 3번 = 2 3') # 안내문 출력

    print('0. 전부') # 
    typelist = typeExtractor(data.locaList[info['type']]) # typelist는 '데이터'의 '타입'을 저장합니다 
    for i, val in enumerate(typelist):
        print("%d. %s"%(i+1,val)) # '타입' 출력
    answer = input(':') # '답변' 입력

    try: # 다수 선택 처리 시작
        answer = numToType(answer, typelist) # '답변'을 '타입' string 으로 변경

        print(chr(27) + "[2J") # screen clear code
        result=reduceNSelect(data.locaList[info['type']], answer) #결과값 출력
        print(
            color.bold + '-----무작위 선택 결과----- \n' + color.end + \
            '이름: ' + color.red + result['name'] + color.end + '\n'\
            '종류: ' + color.darkcyan + result['type'] + color.end + '\n'\
            '네이버 지도 링크: ' + color.blue + result['link'] + color.end + '\n'\
            '설명: ' + color.green + result['desc'] + color.end 
        )

        input('\nEnter를 눌러 돌아갑니다.')
    except: # 만약 입력값이 1 2 같은게 아닌 잘못된 값일 경우 예외처리
        input('올바르지 않은 입력값입니다. 재시도하려면 Enter를 눌러주세요.') # 예외가 될 때는 '답변'이 올바르지 않을때 밖에 없으니 한가지 처리만 해주면 됨
        return selector(info) # 함수 재시작
    return 0

def food():
    selector({
        'type': 'food',
        'command': '식당',
        'name': '식당'
    })

def cafe(): 
    selector({
        'type': 'cafe',
        'command': '카페',
        'name': '카페'
    })

def play(): 
    selector({
        'type': 'play',
        'command': '여가',
        'name': '여가 시설'
    })

def pub(): 
    selector({
        'type': 'pub',
        'command': '술집',
        'name': '주점'
    })

def subway(recursion=False): 

    print(chr(27) + "[2J") # screen clear code

    def timesearch(timelist,format): # 시간을 비교하는 함수
        now = datetime.now().strftime(format) # 지금 시간을 now 변수에 저장, 지금 timestamp를 문자화 후 timestamp로 변경하는 이유는 년월일을 초기화하기 위해서
        for j, val in enumerate(timelist): # 시간표 값으로 반복문 시작

            if(datetime.strptime(val,format) > datetime.strptime(now,format)): # 반복 중 현재 시각보다 큰 시간일 때
                
                if(j == len(timelist)-1): # 배열의 마지막 처리
                    return [timelist[j]]
                elif(j == len(timelist)-2): # 배열의 마지막-1 처리
                    return [timelist[j], timelist[j+1]]
                else: # 평상시
                    return [timelist[j], timelist[j+1], timelist[j+2]] 
                
    def format(datalist): # 배열 개수에 따른 결과값 변경
        string = '곧 도착하는 열차 시간 : ' + color.red # return string 선언
        for i, val in enumerate(datalist):
            string = string + val # 배열 값 추가
            if(i != len(datalist)-1): # 마지막 배열이 아닐때 , 추가
                string = string + ', '
        string = string + color.end
        return string # 열차 도착 시간 list 출력 함수

    formatdata = '%H:%M' #시간:분 타임 포매팅 지정

    dow = datetime.now().weekday() # 오늘 요일을 0~6으로 출력 0이 월요일
    if(recursion==True): # 공휴일 일 때
        dow=['sunday', '공휴일']
    elif(dow==5):
        dow=['saturday', '토요일']
    elif(dow==6):
        dow=['sunday', '일요일']
    else:
        dow=['weekday', '평일']
    print(color.bold +'\n*' + dow[1]+ ' 시간표*' + color.end) # 시간표 출력
    print(color.bold + '현재 시각 : ' + color.end + color.blue + datetime.now().strftime('%H:%M') + color.end )
    print(color.bold + '상행 (인천 -> 오이도 방향)' + color.end)
    print(format(timesearch(data.inhaMetroTimetable[dow[0]]['up'],formatdata))) # 시간을 비교하는 함수 호출
    print(color.bold + '하행 (오이도 -> 인천 방향)' + color.end)
    print(format(timesearch(data.inhaMetroTimetable[dow[0]]['down'],formatdata))) # 시간을 비교하는 함수 호출
    t=input('\nEnter를 눌러 종료합니다. 만약 공휴일시간표가 필요하다면, x를 입력해주세요 : ')
    if(t=='x'): # 공휴일 일때
        subway(True)
    else:
        return 0

def end():
    print('봇을 종료합니다.')
    quit()