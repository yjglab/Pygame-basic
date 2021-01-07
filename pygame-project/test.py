lst = ["a", "b", "c"]

for lst_idx, lst_val in enumerate(lst):
    print(lst_idx, lst_val)



### for 문과 else

for ball_idx, ball_val in enumerate(balls):
    print("ball :", ball_val)
    for weapon_idx, weapon_val in enumerate(weapons):
        print("weapons :", weapon_val)
        if ball_val == weapon_val:
            print("공과 무기가 충돌")
            break # 이 break 없으면 else로 이동할 수 없음
    
    else:
        continue # 2번째 for문 탈출
    break