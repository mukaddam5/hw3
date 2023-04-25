from MethodDemo import ParentClass, ParentClass3


class ChildClass(ParentClass, ParentClass3):
    child = ParentClass()
    child3 = ParentClass3()
    print(child3.academy(10, 20))
    print(child3.university(10, 5))
    print(child.school(10, 50))



























