def id_checking(course_id):
    if len(course_id)>12 or len(course_id)<12:
        raise ValueError("length of id must be 12")


