
import transformers as transformers

from Request import Model, Questionnaire, Request
from Result import Result
from Scheduler import UserRequest
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

    #sorage- user_requests
    model = Model("Model5", "http://example.com/model1", "v1")
    questionnaire = Questionnaire("Questionnaire1", "v1")
    request = Request(model, questionnaire)
    user_request1 = UserRequest(["user1", "user2"], request, "2024-02-22 10:00:00", 0.2)
    user_request2 = UserRequest(["user3", "user4"], request, "2024-02-22 11:00:00", 0.2)
    s.user_requests_scheduler_list.append(user_request1)
    s.user_requests_scheduler_list.append(user_request2)
    # user_requests_list2 =[]
    # user_request3 = UserRequest(["user1", "user2"], request, "2024-02-22 10:00:00", 0.5)
    # user_request4 = UserRequest(["user3", "user4"], request, "2024-02-22 11:00:00", 0.5)
    # user_requests_list2.append(user_request3)
    # user_requests_list2.append(user_request4)
    # s.save_user_requests_to_file(user_requests_list2)
    s.user_requests_scheduler_list.clear()
    s.user_requests_scheduler_list = s.load_user_requests_from_file()

    # storage- agent_request
    model1 = Model("Model1", "http://example.com/model1", "v1")
    model2 = Model("Model2", "http://example.com/model1", "v1")
    questionnaire = Questionnaire("Questionnaire1", "v1")
    agent_request1 = Request(model1, questionnaire)
    agent_request2 = Request(model2, questionnaire)
    s.agent_requests_scheduler_list.append(agent_request1)
    s.user_requests_scheduler_list.append(agent_request2)

    agent_requests_list2 =[]
    model3 = Model("Model3", "http://example.com/model1", "v1")
    model4 = Model("Model4", "http://example.com/model1", "v1")
    agent_request3 = Request(model3, questionnaire)
    agent_request4 = Request(model4, questionnaire)
    agent_requests_list2.append(agent_request3)
    agent_requests_list2.append(agent_request4)
    s.save_agent_requests_to_file(agent_requests_list2)

    s.agent_requests_scheduler_list.clear()
    s.agent_requests_scheduler_list = s.load_agent_requests_from_file()
    print(s.agent_requests_scheduler_list)


if __name__ == '__main__':
    main()
