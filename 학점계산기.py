# 각 학점에 대한 등급과 점수
GRADE_POINT = {"A+": 4.5, "A": 4.0, "B+": 3.5, "B": 3.0, "C+": 2.5, "C": 2.0, "D+": 1.5, "D": 1.0, "F": 0.0}

def get_input():
    """사용자로부터 학점과 평점을 입력받아 반환하는 함수"""
    credit = int(input("학점을 입력하세요: "))
    grade = input("평점을 입력하세요: ")
    return credit, grade

def calculate_total_grade(subj_list, include_f_grade=True):
    """주어진 과목 리스트에서 제출용 또는 열람용 학점 총합과 평균(GPA)을 계산하는 함수"""
    total_credit = 0
    total_grade_point = 0
    for subj in subj_list:
        credit, grade = subj
        # 열람용 학점에 F학점이 포함되는 경우
        if include_f_grade or grade != "F":
            total_credit += credit
            total_grade_point += credit * GRADE_POINT[grade]
    if total_credit == 0:
        gpa = 0
    else:
        gpa = round(total_grade_point / total_credit, 2)
    return total_credit, gpa


def main():
    subj_list = []
    while True:
        print("작업을 선택하세요. 1. 입력 2. 계산")
        menu = int(input())
        if menu == 1:
            credit, grade = get_input()
            subj_list.append((credit, grade))
            print("입력되었습니다.")
        elif menu == 2:
            submit_credit, submit_gpa = calculate_total_grade(subj_list, False)
            view_credit, view_gpa = calculate_total_grade(subj_list, True)
            print(f"제출용: {submit_credit}학점 (GPA: {submit_gpa}) 열람용: {view_credit}학점 (GPA: {view_gpa})")
            break
        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")


if __name__ == "__main__":
    main()