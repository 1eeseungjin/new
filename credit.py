all_credit = int(input("총 이수학점을 말해봐:")) #163
score = float(input("졸업평점을 말해봐:")) #3.34

#print("이수학점:",all_credit,"\n졸업평점:",score)

add_credit = int(input("앞으로 몇 학점 들을겨:"))
possible_score = float(input("예상 학기 평점은:"))
new_credit = all_credit+add_credit
new_score = (((all_credit*score)+add_credit*possible_score)/(all_credit+add_credit))

print("이수학점:",new_credit,"\n졸업평점:",round(new_score,3))
cnt = 0
jae = 0
while 1:
    retaking = input("재수강 해볼텨? 0.아니 1.응")
    cnt+=1

    if retaking == '0':
        cnt=cnt-1
        repeat = cnt
        updated_score = new_score
        print("재수강 과목",repeat,"개",jae,"학점")
        print("응 니 졸업평점",round(updated_score,3))
        break
    elif retaking == '1':
        re_credit = int(input("그 과목 몇 학점짜리임:"))
        last_score = float(input("기존점수 말해봐(ex-2.0):"))
        re_score = float(input("예상점수 말해봐(ex-4.0):"))
        updated_score = ((new_credit*new_score+re_score-last_score)/new_credit)
        print("최종 졸업평점",round(updated_score,3))
        new_score = updated_score
        jae += re_credit
    else:
        print('잘못눌렀어 임마')
        cnt=cnt-1


        continue
