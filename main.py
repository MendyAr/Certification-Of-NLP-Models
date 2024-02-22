# import pip
# pip install transformers

from Request import Model, Questionnaire, Request
from Result import Result
from Storage import Storage


def main():
    print("-------testing the project-shir:-------------")
    s = Storage()

    # storage- users
    # name = input("Please enter your name: ")
    # print(s.add_user(name))
    # print(s.get_user("shira"))
    # print(s.users)

    # storage- results
    # model = Model("Model5", "http://example.com/model1", "v1")
    # questionnaire = Questionnaire("Questionnaire1", "v1")
    # request = Request(model, questionnaire)
    # result = Result(request, 0.5)
    # print(s.add_result(result))
    # print(s.get_result(request))


if __name__ == '__main__':
    main()
