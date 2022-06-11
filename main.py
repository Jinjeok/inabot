import command_handle
command_list={'명령어':'command','식당':'food', '카페':'cafe', '여가':'play', '술집':'pub', '지하철': 'subway', '종료': 'end'}

while(1):
    print(chr(27) + "[2J")
    print("명령어 목록은 '명령어'를 입력하시면 확인하실 수 있습니다.")
    inputs=input("명령어를 입력해주세요: ") # 명령어 입력받음

    process = command_list.get(inputs,"unknown") # 입력받은 string이 object 내에 존재하는지, 만약 존재하면 그 key의 value를 return

    if(process == 'unknown') :
        input('\n⚠올바르지 않은 명령어입니다.⚠ \n계속하려면 Enter를 누르세요.')
        continue
    
    commandFunction = getattr(command_handle, process) # food(), command()
    commandFunction() # food()