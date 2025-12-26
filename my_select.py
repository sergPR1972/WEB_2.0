from sqlalchemy import func, desc, select, and_

from src.models import Teacher, Student, Discipline, Grade, Group
from src.db import session


def select_one():
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return result


def select_two(discipline_id: int):
    r = session.query(Discipline.name,
                      Student.fullname,
                      func.round(func.avg(Grade.grade), 2).label('avg_grade')
                      ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .filter(Discipline.id == discipline_id) \
        .group_by(Student.id, Discipline.name) \
        .order_by(desc('avg_grade')) \
        .limit(1).all()
    return r


def select_three(discipline_id: int):
    r = session.query(Discipline.name,
                      Group.name,
                      func.round(func.avg(Grade.grade), 2).label('avg_grade')
                      ) \
        .select_from(Grade) \
        .join(Discipline) \
        .join(Student) \
        .join(Group) \
        .filter(Discipline.id == discipline_id) \
        .group_by(Group.id, Discipline.name) \
        .order_by(desc('avg_grade')) \
        .all()
    return r


def select_four():
    r = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade) \
        .all()
    return r


def select_five(teacher_id: int):
    r = session.query(Discipline.name,
                      Teacher.fullname
                      ) \
        .select_from(Discipline) \
        .join(Teacher) \
        .filter(Teacher.id == teacher_id) \
        .order_by(Discipline.name) \
        .all()
    return r


def select_six(group_id: int):
    r = session.query(Group.name,
                      Student.fullname) \
        .select_from(Student) \
        .join(Group) \
        .filter(Group.id == group_id) \
        .order_by(Student.fullname) \
        .all()
    return r


def select_seven(group_id: int, discipline_id: int):
    r = session.query(Discipline.name,
                      Group.name,
                      Grade.grade
                      ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Group) \
        .filter(Group.id == group_id, Discipline.id == discipline_id) \
        .all()
    return r


def select_eight(teacher_id: int):
    r = session.query(Teacher.fullname,
                      Discipline.name,
                      func.round(func.avg(Grade.grade), 2).label('avg_grade')
                      ) \
        .select_from(Teacher) \
        .join(Discipline) \
        .join(Grade) \
        .filter(Teacher.id == teacher_id) \
        .group_by(Teacher.fullname, Discipline.name) \
        .order_by(desc('avg_grade')) \
        .all()
    return r


def select_nine(student_id: int):
    r = session.query(Student.fullname,
                      Discipline.name
                      ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .filter(Student.id == student_id) \
        .group_by(Discipline.name, Student.fullname) \
        .order_by(Discipline.name) \
        .all()
    return r


def select_ten(student_id: int, teacher_id: int):
    r = session.query(Discipline.name,
                      Student.fullname,
                      Teacher.fullname
                      ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Teacher) \
        .filter(Student.id == student_id, Teacher.id == teacher_id) \
        .group_by(Discipline.name, Student.fullname, Teacher.fullname) \
        .all()

    return r


def select_first(teacher_id: int, student_id: int):
    r = session.query(Teacher.fullname,
                      Student.fullname,
                      func.round(func.avg(Grade.grade), 2)
                      ) \
        .select_from(Student) \
        .join(Grade) \
        .join(Discipline) \
        .join(Teacher) \
        .filter(Teacher.id == teacher_id, Student.id == student_id) \
        .group_by(Teacher.id, Student.id, Discipline.teacher_id) \
        .all()

    return r


def select_last(discipline_id, group_id):
    subquery = (select(Grade.date_of).join(Student).join(Group).where(
        and_(Grade.discipline_id == discipline_id, Group.id == group_id)
    ).order_by(desc(Grade.date_of)).limit(1).scalar_subquery())

    r = session.query(Discipline.name,
                      Student.fullname,
                      Group.name,
                      Grade.date_of,
                      Grade.grade
                      ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Group) \
        .filter(and_(Discipline.id == discipline_id, Group.id == group_id, Grade.date_of == subquery)) \
        .order_by(desc(Grade.date_of)) \
        .all()
    return r


if __name__ == '__main__':
    # print(select_one())
    # print(select_two(1))
    # print(select_three(8))
    # print(select_four())
    # print(select_five(1))
    # print(select_six(3))
    # print(select_seven(3, 8))
    # print(select_eight(3))
    # print(select_nine(44))
    # print(select_ten(40, 2))
    # print(select_first(5, 20))
    print(select_last(1, 2))
