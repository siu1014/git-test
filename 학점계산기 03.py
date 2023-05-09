class CourseHistory:
    def __init__(self):
        self.history = []
        self.course_id_map = {'id': 10000}
        self.submit_grade = {}
        self.archive_grade = {}

    # 점수 변환 함수
    @classmethod
    def get_gpa_score(cls, gpa):
        match gpa:
            case 'A+':
                return 4.5
            case 'A':
                return 4
            case 'B+':
                return 3.5
            case 'B':
                return 3
            case 'C+':
                return 2.5
            case 'C':
                return 2
            case 'D+':
                return 1.5
            case 'D':
                return 1
            case 'F':
                return 0

    # 과목코드 부여 함수
    def allocate_course_id(self, course_name):
        if course_name not in self.course_id_map:
            new_id = str(int(self.course_id_map['id']) + 1)
            self.course_id_map['id'] = new_id
            self.course_id_map[course_name] = new_id
            self.course_id_map[new_id] = course_name

            return new_id

        else:
            return self.course_id_map[course_name]

    # 입력 함수
    def input_process(self):
        course_name = input('과목명을 입력하세요: ')
        course_id = self.allocate_course_id(course_name)

        credit = input('학점을 입력하세요: ')
        credit = int(credit)

        gpa = input('평점을 입력하세요: ')
        gpa_score = self.get_gpa_score(gpa)

        # 열람용 학점 처리
        if course_id in self.archive_grade:
            # 재수강 처리
            if gpa_score > self.archive_grade[course_id][1]:
                self.archive_grade[course_id] = (credit, gpa_score)
        else:
            self.archive_grade[course_id] = (credit, gpa_score)

        # 제출용 학점 처리
        if gpa_score > 0.0:
            if course_id in self.submit_grade:
                # 재수강 처리
                if gpa_score > self.submit_grade[course_id][1]:
                    self.submit_grade[course_id] = (credit, gpa_score)
            else:
                self.submit_grade[course_id] = (credit, gpa_score)

        self.history.append((course_id, credit, gpa))

        print('입력되었습니다.')

    # 출력 함수
    def print_process(self):
        for course in self.history:
            print('[' + self.course_id_map[course[0]] + '] ', end='')
            print(str(course[1]) + '학점: ' + course[2])

    # 조회 함수
    def query_process(self):
        course_name = input('과목명을 입력하세요: ')

        for course in self.history:
            if course_name == self.course_id_map[course[0]]:
                print('[' + self.course_id_map[course[0]] + '] ', end='')
                print(str(course[1]) + '학점: ' + course[2])
                break
        else:
            print('해당하는 과목이 없습니다.')

    # 계산 함수
    def calculate_process(self):
        submit_gpa, archive_gpa = 0.0, 0.0
        submit_credit, archive_credit = 0, 0

        for course_id in self.submit_grade:
            submit_gpa += self.submit_grade[course_id][0] * self.submit_grade[course_id][1]
            submit_credit += self.submit_grade[course_id][0]

        for course_id in self.archive_grade:
            archive_gpa += self.archive_grade[course_id][0] * self.archive_grade[course_id][1]
            archive_credit += self.archive_grade[course_id][0]

        submit_gpa /= submit_credit
        archive_gpa /= archive_credit

        print('제출용: ' + str(submit_credit) + '학점' + '(GPA: ' + str(submit_gpa) + ')')
        print('열람용: ' + str(archive_credit) + '학점' + '(GPA: ' + str(archive_gpa) + ')')


# 실행 코드
course_history = CourseHistory()

# 무한 루프
while True:
    # 출력
    print('작업을 선택하세요')
    print('    1. 입력')
    print('    2. 출력')
    print('    3. 조회')
    print('    4. 계산')
    print('    5. 종료')

    # 사용자 입력
    user_input = input()

    # 입력값별 작업
    if user_input == '1':
        course_history.input_process()

    elif user_input == '2':
        course_history.print_process()

    elif user_input == '3':
        course_history.query_process()

    elif user_input == '4':
        course_history.calculate_process()

    elif user_input == '5':
        break

    else:
        continue

print('프로그램을 종료합니다.')