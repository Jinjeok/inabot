import command_handle # 명령어 처리용 파일 import
command_list={'명령어':'command','식당':'food', '카페':'cafe', '여가':'play', '술집':'pub', '지하철': 'subway', '종료': 'end'}
# 명령어 목록 선언

while(1):
    print(chr(27) + "[2J")
    print("명령어 목록은 '명령어'를 입력하시면 확인하실 수 있습니다.")
    inputs=input("명령어를 입력해주세요: ") # 명령어를 입력받음

    process = command_list.get(inputs,"unknown") 
    # 입력받은 명령어가 command_list dictionary 내에 존재하는지, 
    # 만약 존재하면 그 key의 value를 return

    if(process == 'unknown') : # command_list에 입력받은 명령어가 없을 때 예외처리
        input('\n⚠올바르지 않은 명령어입니다.⚠ \n계속하려면 Enter를 누르세요.') 
        continue # 명령어를 재입력 받음
    
    commandFunction = getattr(command_handle, process) # command_list에 존재하는 value를 함수명으로 사용함 예) food(), cafe()
    commandFunction() # 함수 실행