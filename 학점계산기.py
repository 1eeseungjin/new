all_credit = int(input("총 이수학점을 말해봐:")) #163
score = float(input("졸업평점을 말해봐:")) #3.34

#print("이수학점:",all_credit,"\n졸업평점:",score)


cnt = 0
jae = 0
while 1:
    retaking = input("재수강 해볼텨? 0.아니 1.응")
    cnt+=1

    if retaking == '0':
       cnt= cnt-1
       passmain2.py

        # cnt=cnt-1

        # repeat = cnt
        # updated_score = new_score
        # print("재수강 과목",repeat,"개",jae,"학점")
        # # print("비재수강 과목",add_credit,"학점")
        # print("* 최종 졸업평점:",round(updated_score,3),"\n* 총 이수학점:",new_credit)
        #
        # break

    elif retaking == '1':
        re_credit = int(input("그 과목 몇 학점짜리임:"))
        if re_credit>0 :
            last_score = float(input("기존점수 말해봐(ex-2.0):"))
            re_score = float(input("예상점수 말해봐(ex-4.0):"))
            updated_score = ((all_credit * score+(re_score-last_score) * re_credit) / all_credit)
            print("* 재수강 후 졸업평점:", round(updated_score, 3), "\n* 이수학점:", all_credit)
            new_score = updated_score
            # new_credit = all_credit
            jae += re_credit
        else:
            cnt = cnt - 1
            repeat = cnt
            updated_score = new_score
            print("재수강 과목", repeat, "개", jae, "학점")
            print("* 최종 졸업평점:", round(updated_score, 3), "\n* 총 이수학점:", new_credit)
            break


    else:
        print('잘못눌렀어 임마')
        cnt=cnt-1


        continue

    # print(new_score)
    # print(new_credit)

    add_credit = int(input("그럼 앞으로 몇 학점 들을겨:"))
    if (cnt==0 and add_credit<0):

     break

    else:
        if add_credit>0 :
            if cnt>0:
                possible_score = float(input("예상 학기 평점은:"))
                new_credit = all_credit+add_credit
                new_score = ((all_credit*new_score)+(add_credit*possible_score))/(all_credit+add_credit)
                print("이수학점:",new_credit,"\n졸업평점:",round(new_score,3))
                all_credit = new_credit
                old_score = score
                score = new_score
            else:
                possible_score = float(input("예상 학기 평점은:"))
                old_score = score
                all_credit = all_credit+add_credit
                score = ((all_credit * score) + (add_credit * possible_score)) / (all_credit + add_credit)
                print("* 재수강",cnt,"개","\n* 추가 이수학점:",add_credit,"학점")
                print("* 최종 졸업평점:", round(score, 3),"\n* 졸업평점 상승:",score- old_score,"\n* 총 이수학점:", all_credit)
                print(old_score)
                print(score)

        else :
            new_credit = all_credit
            repeat = cnt
            updated_score = new_score
            print("재수강 과목", repeat, "개", jae, "학점")
            print("* 최종 졸업평점:", round(updated_score, 3),"\n* 졸업평점 상승:",updated_score-score, "\n* 총 이수학점:", new_credit)
            break


