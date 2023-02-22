class Student:
    schoolName = None
    schoolAddress = None

    def __init__(self, roll_no=None, name=None, mail_id=None, percentage=None):
        self.student_roll_no = roll_no
        self.student_name = name
        self.student_mail_id = mail_id
        self.student_percentage = percentage

    def display_data(self):
        print('\n', '*'*5, 'Student Data', '*'*5,
              '\nStudent Roll No:', self.student_roll_no,
              '\nStudent Name:', self.student_name,
              '\nStudent Mail Id:', self.student_mail_id,
              '\nStudent Percentage:', self.student_percentage,
              '\nSchool Name:', Student.schoolName,
              '\nSchool Address:', Student.schoolAddress)

    @property
    def get_email(self):
        return self.student_mail_id
