import os

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime, Table, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, joinedload, subqueryload
from datetime import datetime, timedelta
import random
from DataObjects.Request import Questionnaire, Model, Request
from DataObjects.Result import Result
from DataObjects.User_Request import UserRequest
from DataObjects.BadRequestException import BadRequestException
from Users.Project import Project
import sys
# module_name = 'Users.User'
# if module_name not in sys.modules:
#     from Users.User import User


from datetime import datetime, timedelta
import random

Base = declarative_base()
current_dir = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL = f"sqlite:///{os.path.join(current_dir, 'storage.db')}"

# Linking table for many-to-many relationship
user_request_request = Table('user_request_request', Base.metadata,
                             Column('user_request_id', Integer, ForeignKey('user_requests.id'), primary_key=True),
                             Column('request_model_name', String, primary_key=True),
                             Column('request_questionnaire_name', String, primary_key=True),
                             ForeignKeyConstraint(
                                 ['request_model_name', 'request_questionnaire_name'],
                                 ['requests.model_name', 'requests.questionnaire_name']
                             )
                             )
# Linking table for many-to-many relationship between projects and models
project_model_association = Table('project_model_association', Base.metadata,
                                  Column('project_id', Integer, ForeignKey('projects.id'), primary_key=True),
                                  Column('model_name', String, ForeignKey('models.name'), primary_key=True)
                                  )

# Linking table for many-to-many relationship between projects and questionnaires
project_questionnaire_association = Table('project_questionnaire_association', Base.metadata,
                                          Column('project_id', Integer, ForeignKey('projects.id'), primary_key=True),
                                          Column('questionnaire_name', String, ForeignKey('questionnaires.name'),
                                                 primary_key=True)
                                          )


class Model_db(Base):
    __tablename__ = 'models'
    name = Column(String, primary_key=True)
    requests = relationship('Request_db', back_populates='model')
    projects = relationship('Project_db', secondary=project_model_association, back_populates='models')


class Questionnaire_db(Base):
    __tablename__ = 'questionnaires'
    name = Column(String, primary_key=True)
    requests = relationship('Request_db', back_populates='questionnaire')
    projects = relationship('Project_db', secondary=project_questionnaire_association, back_populates='questionnaires')


class Request_db(Base):
    __tablename__ = 'requests'
    model_name = Column(String, ForeignKey('models.name'), primary_key=True)
    questionnaire_name = Column(String, ForeignKey('questionnaires.name'), primary_key=True)
    model = relationship('Model_db', back_populates='requests', lazy='joined')
    questionnaire = relationship('Questionnaire_db', back_populates='requests', lazy='joined')
    results = relationship('Result_db', back_populates='request')
    user_requests = relationship('UserRequest_db', secondary=user_request_request, back_populates='requests')


class Result_db(Base):
    __tablename__ = 'results'
    request_model_name = Column(String, primary_key=True)  # Existing primary key
    request_questionnaire_name = Column(String, primary_key=True)  # Existing primary key
    start_time = Column(DateTime, primary_key=True)  # Added start_time as part of the primary key
    result_score = Column(Float)
    end_time = Column(DateTime)
    __table_args__ = (
        ForeignKeyConstraint(
            ['request_model_name', 'request_questionnaire_name'],
            ['requests.model_name', 'requests.questionnaire_name']
        ),
    )
    request = relationship('Request_db', back_populates='results')  # Bidirectional relationship


class UserRequest_db(Base):
    __tablename__ = 'user_requests'
    id = Column(Integer, primary_key=True)
    users = Column(String)  # Assuming users is a comma-separated string of usernames
    starttime = Column(DateTime)
    score = Column(Float)
    requests = relationship('Request_db', secondary=user_request_request,
                            back_populates='user_requests')  # Many-to-many relationship


class User_db(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_id = Column(String, unique=True, nullable=False)
    password = Column(String, unique=False, nullable=False)
    projects = relationship('Project_db', back_populates='user')


class Project_db(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    user = relationship('User_db', back_populates='projects')
    models = relationship('Model_db', secondary=project_model_association, back_populates='projects')
    questionnaires = relationship('Questionnaire_db', secondary=project_questionnaire_association,
                                  back_populates='projects')


class Storage2:
    _instance = None  # Singleton

    def __init__(self):
        if self._instance is not None:
            raise Exception("Singleton class cannot be instantiated multiple times")
        else:
            def get_session():  # !!!!! DELETE THIS DATABASE !!!!! if create_new=True
                create_new = os.getenv('RESET_DB', 'False').lower() in ['true', '1', 't', 'y', 'yes']
                if create_new:
                    db_path = os.path.join(current_dir, "storage.db")
                    if os.path.exists(db_path):
                        os.remove(db_path)
                    engine = create_engine(DATABASE_URL)
                    Base.metadata.create_all(engine)
                else:
                    engine = create_engine(DATABASE_URL)
                Session = sessionmaker(bind=engine)
                return Session()

            self.session = get_session()
            pass

    @staticmethod
    def get_instance():
        if Storage2._instance is None:
            Storage2._instance = Storage2()
        return Storage2._instance

    def get_number_of_evals(self):
        return self.session.query(Result_db).filter_by(result_score=None).count()

    def get_all_evaled_models(self):
        models_results = self.session.query(Result_db).filter(Result_db.result_score!=None).all()
        models_names = []
        for model_result in models_results:
            models_names.append(model_result.request_model_name)
        return models_names

    def get_top_evals(self, number_of_results=10):
        if number_of_results == None:
            top_results_db = (
                self.session.query(Result_db)
                .options(
                    joinedload(Result_db.request).joinedload(Request_db.model),
                    joinedload(Result_db.request).joinedload(Request_db.questionnaire)
                )
                .order_by(Result_db.result_score.desc())
                .all()
            )
        else:
            top_results_db = (
                self.session.query(Result_db)
                .options(
                    joinedload(Result_db.request).joinedload(Request_db.model),
                    joinedload(Result_db.request).joinedload(Request_db.questionnaire)
                )
                .order_by(Result_db.result_score.desc())
                .limit(number_of_results)
                .all()
            )
        top_results = []
        for result_db in top_results_db:
            try:
                if result_db.request is None:
                    request_db = self.session.query(Request_db).filter_by(
                        model_name=result_db.request_model_name,
                        questionnaire_name=result_db.request_questionnaire_name
                    ).first()
                    if request_db is None:
                        model_db = self.session.query(Model_db).filter_by(name=result_db.request_model_name).first()
                        if model_db is None:
                            model_db = Model_db(name=result_db.request_model_name)
                            self.session.add(model_db)
                            self.session.commit()
                        questionnaire_db = self.session.query(Questionnaire_db).filter_by(
                            name=result_db.request_questionnaire_name).first()
                        if questionnaire_db is None:
                            questionnaire_db = Questionnaire_db(name=result_db.request_questionnaire_name)
                            self.session.add(questionnaire_db)
                            self.session.commit()
                        request_db = Request_db(model_name=model_db.name, questionnaire_name=questionnaire_db.name)
                        self.session.add(request_db)
                        self.session.commit()
                    result_db.request = request_db
                    self.session.commit()
                # result_db.request is not None now!
                result = self.Result_db_2_Result(result_db)
                top_results.append(result)
            except ValueError as e:
                pass
        return top_results

    def add_project(self, user_id, project_name):
        # Check if the user exists
        user = self.session.query(User_db).filter(User_db.user_id == user_id).first()
        if not user:
            raise ValueError(f"No user found with user_id: {user_id}")
        # Check if the project already exists for the user
        existing_project = self.session.query(Project_db).filter(
            Project_db.user_id == user.user_id,
            Project_db.name == project_name
        ).first()
        if existing_project:
            raise ValueError(f"Project {project_name} already exists for user {user_id}")
        # Create a new project and link it to the user
        new_project = Project_db(name=project_name, user_id=user.user_id)
        self.session.add(new_project)
        self.session.commit()

    def add_model(self, user_id, project_name, model):
        user = self.session.query(User_db).filter(User_db.user_id == user_id).first()
        if not user:
            # The user does not exist
            return
            raise ValueError(f"No user found with user_id: {user_id}")
        project = self.session.query(Project_db).filter(
            Project_db.user_id == user.user_id,
            Project_db.name == project_name
        ).first()
        if not project:
            return
            # The project does not exist
            raise ValueError(f"No project found with name: {project_name} for user: {user_id}")
        # Check if the model already exists
        existing_model = self.session.query(Model_db).filter(Model_db.name == model.name).first()
        if existing_model:
            if existing_model in project.models:
                # The model already exists in the project
                return
                raise ValueError(f"Model {model.name} already exists in project {project_name} for user {user_id}")
            else:
                project.models.append(existing_model)
        else:
            model_db = self.Model_2_Model_db(model)
            project.models.append(model_db)
        self.session.commit()

    def add_questionnaire(self, user_id, project_name, questionnaire):
        user = self.session.query(User_db).filter(User_db.user_id == user_id).first()
        if not user:
            raise ValueError(f"No user found with user_id: {user_id}")
        project = self.session.query(Project_db).filter(
            Project_db.user_id == user.user_id,
            Project_db.name == project_name
        ).first()
        if not project:
            raise ValueError(f"No project found with name: {project_name} for user: {user_id}")
        # Check if the questionnaire already exists
        questionnaire_db = self.session.query(Questionnaire_db).filter_by(name=questionnaire.name).first()
        if not questionnaire_db:
            questionnaire_db = self.Questionnaire_2_Questionnaire_db(questionnaire)
            self.session.add(questionnaire_db)
        project.questionnaires.append(questionnaire_db)
        self.session.commit()

    def delete_project(self, user_id, project_name):
        user = self.session.query(User_db).filter(User_db.user_id == user_id).first()
        if not user:
            raise ValueError(f"No user found with user_id: {user_id}")

        project = self.session.query(Project_db).filter(
            Project_db.user_id == user.user_id,
            Project_db.name == project_name
        ).first()
        if not project:
            raise ValueError(f"No project found with name: {project_name} for user: {user_id}")

        self.session.delete(project)
        self.session.commit()

    def remove_model(self, user_id, project_name, model):
        user = self.session.query(User_db).filter(User_db.user_id == user_id).first()
        if not user:
            raise ValueError(f"No user found with user_id: {user_id}")

        project = self.session.query(Project_db).filter(
            Project_db.user_id == user.user_id,
            Project_db.name == project_name
        ).first()
        if not project:
            raise ValueError(f"No project found with name: {project_name} for user: {user_id}")

        model_db = self.session.query(Model_db).filter(Model_db.name == model.name).first()
        if model_db in project.models:
            project.models.remove(model_db)
            self.session.commit()
        else:
            raise ValueError(f"Model {model.name} not found in project {project_name}")

    def remove_questionnaire(self, user_id, project_name, questionnaire):
        user = self.session.query(User_db).filter(User_db.user_id == user_id).first()
        if not user:
            raise ValueError(f"No user found with user_id: {user_id}")

        project = self.session.query(Project_db).filter(
            Project_db.user_id == user.user_id,
            Project_db.name == project_name
        ).first()
        if not project:
            raise ValueError(f"No project found with name: {project_name} for user: {user_id}")

        questionnaire_db = self.session.query(Questionnaire_db).filter(
            Questionnaire_db.name == questionnaire.name).first()
        if questionnaire_db in project.questionnaires:
            project.questionnaires.remove(questionnaire_db)
            self.session.commit()
        else:
            raise ValueError(f"Questionnaire {questionnaire.name} not found in project {project_name}")

    def get_user(self, user_id):
        user_db = self.session.query(User_db).filter(User_db.user_id == user_id).first()
        if not user_db:
            raise ValueError(f"No user found with user_id: {user_id}")
        return self.User_db_2_User(user_db)

    def check_if_has_result_2_eval(self, request: Request):
        name = request.model.name
        if isinstance(request.model.name, dict):
            name = request.model.name["name"]
        result_dbs = self.session.query(Result_db).filter(
            Result_db.request_model_name == name,
            Result_db.request_questionnaire_name == request.questionnaire.name,
            Result_db.end_time == None,
            Result_db.result_score == -99999
        ).order_by(Result_db.start_time.desc()).limit(1).all()

        if len(result_dbs) > 0:
            return self.Result_db_2_Result(result_dbs[0])
        else:
            return None
        
    def get_waiting_request(self):
        result_dbs = self.session.query(Result_db).filter(
            Result_db.end_time == None,
            Result_db.result_score == -99999
        ).all()
        results = []
        for rdb in result_dbs:
            results.append(self.Result_db_2_Result(rdb))
        return results
        
    def check_if_has_result_2_eval_new(self, request: Request):
        name = request.model.name
        if isinstance(request.model.name, dict):
            name = request.model.name["name"]
        result_dbs = self.session.query(Result_db).filter(
            Result_db.request_model_name == name,
            Result_db.request_questionnaire_name == request.questionnaire.name,
            Result_db.end_time != None,
        ).order_by(Result_db.end_time.desc()).limit(1).all()

        if len(result_dbs) > 0:
            return self.Result_db_2_Result(result_dbs[0])
        else:
            return None

    # Conversion functions for Project_db
    def Project_2_Project_db(self, project: Project, user_id: int):
        p_db = Project_db(name=project.name, user_id=user_id)
        p_db.models = [self.Model_2_Model_db(model) for model in project.models.values()]
        p_db.questionnaires = [self.Questionnaire_2_Questionnaire_db(questionnaire) for questionnaire in
                               project.questionnaires.values()]
        return p_db

    def Project_db_2_Project(self, project_db: Project_db):
        project = Project(project_db.name)
        project.models = {self.Model_db_2_Model(model_db) for model_db in project_db.models}
        project.questionnaires = {self.Questionnaire_db_2_Questionnaire(questionnaire_db) for questionnaire_db in
                                  project_db.questionnaires}
        return project

    # Conversion functions for Model_db

    def Model_2_Model_db(self, model: Model):
        m_db = Model_db(name=model.name)
        return m_db

    def Model_db_2_Model(self, model_db: Model_db):
        return Model(name=model_db.name)

    # Conversion functions for Questionnaire_db

    def Questionnaire_2_Questionnaire_db(self, questionnaire: Questionnaire):
        q_db = Questionnaire_db(name=questionnaire.name)
        return q_db

    def Questionnaire_db_2_Questionnaire(self, questionnaire_db: Questionnaire_db):
        return Questionnaire(name=questionnaire_db.name)

    # Conversion functions for Request_db

    def Request_2_Request_db(self, request: Request):
        r_db = Request_db(model_name=request.model.name, questionnaire_name=request.questionnaire.name)
        return r_db

    def Request_db_2_Request(self, request_db: Request_db):
        # if request_db.model is None or request_db.questionnaire is None:
        #     raise ValueError("Related model or questionnaire is missing")
        model = Model(name=request_db.model.name)
        questionnaire = Questionnaire(name=request_db.questionnaire.name)
        return Request(model=model, questionnaire=questionnaire)

    # Conversion functions for Result_db

    def Result_2_Result_db(self, result: Result):
        r_db = Result_db(
            request_model_name=result.request.model.name,
            request_questionnaire_name=result.request.questionnaire.name,
            start_time=result.start_time,
            result_score=result.result_score,
            end_time=result.end_time
        )
        return r_db

    def Result_db_2_Result(self, result_db: Result_db):
        if result_db is None or result_db.request_model_name is None or result_db.request_questionnaire_name is None:
            raise ValueError(
                f"Incomplete request data in Result_db with result_score {result_db.result_score} and start_time {result_db.start_time}, {result_db.request_questionnaire_name}, {result_db.request_model_name}")
        model = Model(name=result_db.request_model_name)
        questionnaire = Questionnaire(name=result_db.request_questionnaire_name)
        request = Request(model=model, questionnaire=questionnaire)
        result = Result(request=request, result_score=result_db.result_score, start_time=result_db.start_time)
        result.end_time = result_db.end_time
        return result

    # Conversion functions for UserRequest_db

    def UserRequest_2_UserRequest_db(self, user_request: UserRequest):
        users_str = ",".join(user_request.users)
        ur_db = UserRequest_db(
            id=user_request.id,
            users=users_str,
            starttime=user_request.starttime,
            score=user_request.score
        )
        ur_db.requests = [
            Request_db(model_name=request.model.name, questionnaire_name=request.questionnaire.name)
            for request in user_request.requests
        ]
        return ur_db

    def UserRequest_db_2_UserRequest(self, user_request_db: UserRequest_db):
        users_list = user_request_db.users.split(",")
        requests = [
            Request(
                model=Model(name=req.model_name),
                questionnaire=Questionnaire(name=req.questionnaire_name)
            ) for req in user_request_db.requests
        ]
        user_request = UserRequest(users=users_list, request=requests[0], starttime=user_request_db.starttime,
                                   score=user_request_db.score)
        user_request.requests = requests
        user_request.id = user_request_db.id
        return user_request

    # Conversion functions for User_db
    def User_2_User_db(self, user):
        u_db = User_db(user_id=user.user_id)
        u_db.projects = [self.Project_2_Project_db(project, user.user_id) for project in user.projects.values()]
        return u_db

    def User_db_2_User(self, user_db: User_db):
        from Users.User import User
        user = User(user_db.user_id)
        user.projects = {project_db.name: self.Project_db_2_Project(project_db) for project_db in user_db.projects}
        return user

    # .......................................................................
    # ....................Agent Requests Scheduler List......................
    # .......................................................................
    def load_agent_requests_scheduler_list_from_db(self):
        try:
            user_requests_db = self.session.query(UserRequest_db).filter(UserRequest_db.users == 'agent').all()
            user_requests = [self.UserRequest_db_2_UserRequest(ur) for ur in user_requests_db]
            return user_requests
        except:
            return []


    def save_agent_requests_scheduler_list_to_db(self, agent_requests_scheduler_list_new):
        self.session.query(UserRequest_db).filter(UserRequest_db.users == 'agent').delete()
        user_requests_db = [self.UserRequest_2_UserRequest_db(ur) for ur in agent_requests_scheduler_list_new]
        self.session.add_all(user_requests_db)
        self.session.commit()

    def add_agent_reguests__scheduler_list_to_db(self, userRequest: UserRequest):
        userRequest_db = self.UserRequest_2_UserRequest_db(userRequest)
        self.session.add(userRequest_db)
        self.session.commit()

    def delete_agent_reguests__scheduler_list_to_db(self, userRequest: UserRequest):
        self.session.query(UserRequest_db).filter(UserRequest_db.id == userRequest.id).delete()
        self.session.commit()

    def update_agent_reguests__scheduler_list_to_db(self, userRequest: UserRequest):
        self.session.query(UserRequest_db).filter(UserRequest_db.id == userRequest.id).update({
            UserRequest_db.users: ",".join(userRequest.users),
            UserRequest_db.starttime: userRequest.starttime,
            UserRequest_db.score: userRequest.score
        })
        self.session.commit()

    # .......................................................................
    # ....................User Requests Scheduler List.......................
    # .......................................................................
    def load_user_requests_scheduler_list_from_db(self):
        try:
            user_requests_db = self.session.query(UserRequest_db).filter(UserRequest_db.users != 'agent').all()
            user_requests = [self.UserRequest_db_2_UserRequest(ur) for ur in user_requests_db]
            return user_requests
        except:
            return []


    def save_user_requests_scheduler_list_to_db(self, agent_requests_scheduler_list_new):
        self.session.query(UserRequest_db).filter(UserRequest_db.users != 'agent').delete()
        user_requests_db = [self.UserRequest_2_UserRequest_db(ur) for ur in agent_requests_scheduler_list_new]
        self.session.add_all(user_requests_db)
        self.session.commit()

    def add_user_reguests__scheduler_list_to_db(self, userRequest: UserRequest):
        userRequest_db = self.UserRequest_2_UserRequest_db(userRequest)
        self.session.add(userRequest_db)
        self.session.commit()

    def delete_user_reguests__scheduler_list_to_db(self, userRequest: UserRequest):
        self.session.query(UserRequest_db).filter(UserRequest_db.id == userRequest.id).delete()
        self.session.commit()

    def update_user_reguests__scheduler_list_to_db(self, userRequest: UserRequest):
        self.session.query(UserRequest_db).filter(UserRequest_db.id == userRequest.id).update({
            UserRequest_db.users: ",".join(userRequest.users),
            UserRequest_db.starttime: userRequest.starttime,
            UserRequest_db.score: userRequest.score
        })
        self.session.commit()

    # .......................................................................
    # ..............................Results..................................
    # .......................................................................
    def load_results_from_db(self):
        results_db = self.session.query(Result_db).all()
        results = [self.Result_db_2_Result(r) for r in results_db]
        return results

    def save_results_to_db(self, results_new):
        self.session.query(Result_db).delete()
        results_db = [self.Result_2_Result_db(r) for r in results_new]
        self.session.add_all(results_db)
        self.session.commit()

    def add_result_to_db(self, result: Result):
        result_db = self.Result_2_Result_db(result)
        self.session.add(result_db)
        self.session.commit()

    def delete_result_from_db(self, result: Result):
        self.session.query(Result_db).filter(
            Result_db.request_model_name == result.request.model.name,
            Result_db.request_questionnaire_name == result.request.questionnaire.name,
            Result_db.start_time == result.start_time
        ).delete()
        self.session.commit()

    def update_result_in_db(self, result: Result):
        existing_result_db = self.session.query(Result_db).filter(
            Result_db.request_model_name == result.request.model.name,
            Result_db.request_questionnaire_name == result.request.questionnaire.name,
            Result_db.start_time == result.start_time
        ).first()

        if existing_result_db:
            existing_result_db.result_score = result.result_score
            existing_result_db.end_time = result.end_time
        else:
            new_result_db = self.Result_2_Result_db(result)
            self.session.add(new_result_db)

        self.session.commit()

    def get_result_of_request(self, request: Request):
        result_db = self.session.query(Result_db).filter(
            Result_db.request_model_name == request.model.name,
            Result_db.request_questionnaire_name == request.questionnaire.name,
            Result_db.end_time != None
        ).order_by(Result_db.end_time.desc()).first()
        if result_db is None:
            return None
        return self.Result_db_2_Result(result_db)

    # .......................................................................
    # ..............................Models..................................
    # .......................................................................
    def load_models_from_db(self):
        models_db = self.session.query(Model_db).all()
        models = [self.Model_db_2_Model(m) for m in models_db]
        return models

    def save_models_to_db(self, models_new):
        self.session.query(Model_db).delete()
        models_db = [self.Model_2_Model_db(m) for m in models_new]
        self.session.add_all(models_db)
        self.session.commit()

    def add_model_to_db(self, model: Model):
        model_db = self.Model_2_Model_db(model)
        self.session.add(model_db)
        self.session.commit()

    def delete_model_from_db(self, model: Model):
        self.session.query(Model_db).filter(Model_db.name == model.name).delete()
        self.session.commit()

    # .......................................................................
    # ..............................Questionnaires...........................
    # .......................................................................
    def load_questionnaires_from_db(self):
        questionnaires_db = self.session.query(Questionnaire_db).all()
        questionnaires = [self.Questionnaire_db_2_Questionnaire(q) for q in questionnaires_db]
        return questionnaires

    def save_questionnaires_to_db(self, questionnaires_new):
        self.session.query(Questionnaire_db).delete()
        questionnaires_db = [self.Questionnaire_2_Questionnaire_db(q) for q in questionnaires_new]
        self.session.add_all(questionnaires_db)
        self.session.commit()

    def add_questionnaire_to_db(self, questionnaire: Questionnaire):
        questionnaire_db = self.Questionnaire_2_Questionnaire_db(questionnaire)
        self.session.add(questionnaire_db)
        self.session.commit()

    def delete_questionnaire_from_db(self, questionnaire: Questionnaire):
        self.session.query(Questionnaire_db).filter(Questionnaire_db.name == questionnaire.name).delete()
        self.session.commit()

    # .......................................................................
    # ..............................Request...........................
    # .......................................................................
    def load_requests_from_db(self):
        requests_db = self.session.query(Request_db).all()
        requests = [self.Request_db_2_Request(r) for r in requests_db]
        return requests

    def save_requests_to_db(self, requests_new):
        self.session.query(Request_db).delete()
        requests_db = [self.Request_2_Request_db(r) for r in requests_new]
        self.session.add_all(requests_db)
        self.session.commit()

    def add_request_to_db(self, request: Request):
        request_db = self.Request_2_Request_db(request)
        self.session.add(request_db)
        self.session.commit()

    def delete_request_from_db(self, request: Request):
        self.session.query(Request_db).filter(
            Request_db.model_name == request.model.name,
            Request_db.questionnaire_name == request.questionnaire.name
        ).delete()
        self.session.commit()

    def update_request_in_db(self, request: Request):
        self.session.query(Request_db).filter(
            Request_db.model_name == request.model.name,
            Request_db.questionnaire_name == request.questionnaire.name
        ).update({
            Request_db.model_name: request.model.name,
            Request_db.questionnaire_name: request.questionnaire.name
        })
        self.session.commit()

    # .......................................................................
    # ...............................Users...................................
    # .......................................................................
    def create_user(self, user_id, password):
        try:
            existing_user = self.session.query(User_db).filter(User_db.user_id == user_id).first()
        except Exception as e:
            pass
        # if existing_user:
        #     raise BadRequestException(f"User {user_id} already exists")
        new_user = User_db(user_id=user_id, password=password)
        self.session.add(new_user)
        self.session.commit()

    def read_user(self, user_id):
        if not isinstance(user_id, str):
            raise ValueError("user_id must be a string")
        user_db = (
            self.session.query(User_db)
            .options(
                joinedload(User_db.projects)
                .joinedload(Project_db.models),
                joinedload(User_db.projects)
                .joinedload(Project_db.questionnaires)
            )
            .filter(User_db.user_id == user_id)
            .first()
        )
        if not user_db:
            return None
        return self.User_db_2_User(user_db)

    def update_user(self, old_user_id, new_user_id=None, new_password=None):
        user = self.session.query(User_db).filter(User_db.user_id == old_user_id).first()
        if not user:
            raise ValueError(f"No user found with user_id: {old_user_id}")
        if new_user_id:
            user.user_id = new_user_id
        if new_password:
            user.password = new_password  # Add this line
        self.session.commit()

    def delete_user(self, user_id):
        user = self.session.query(User_db).filter(User_db.user_id == user_id).first()
        if not user:
            raise ValueError(f"No user found with user_id: {user_id}")
        self.session.delete(user)
        self.session.commit()

    def check_email_password(self, email, password):
        if not isinstance(email, str) or not isinstance(password, str):
            raise ValueError("user_id and password must be a string")
        user_db = (
            self.session.query(User_db)
            .options(
                joinedload(User_db.projects)
                .joinedload(Project_db.models),
                joinedload(User_db.projects)
                .joinedload(Project_db.questionnaires)
            )
            .filter(User_db.user_id == email, User_db.password == password)
            .first()
        )
        if not user_db:
            return False
        return True

    # .......................................................................
    # .............................Projects..................................
    # .......................................................................
    def create_project(self, user_id, project_name):
        user = self.get_user(user_id)
        existing_project = self.session.query(Project_db).filter(
            Project_db.user_id == user.user_id,
            Project_db.name == project_name
        ).first()
        if existing_project:
            raise ValueError(f"Project {project_name} already exists for user {user_id}")
        new_project = Project_db(name=project_name, user_id=user.user_id)
        self.session.add(new_project)
        self.session.commit()

    def read_project(self, user_id, project_name):
        user = self.get_user(user_id)
        project_db = self.session.query(Project_db).filter(
            Project_db.user_id == user.user_id,
            Project_db.name == project_name
        ).first()
        if not project_db:
            raise ValueError(f"No project found with name: {project_name} for user: {user_id}")
        return self.Project_db_2_Project(project_db)

    def update_project(self, user_id, old_project_name, new_project_name):
        user = self.get_user(user_id)
        project = self.session.query(Project_db).filter(
            Project_db.user_id == user.user_id,
            Project_db.name == old_project_name
        ).first()
        if not project:
            raise ValueError(f"No project found with name: {old_project_name} for user: {user_id}")
        project.name = new_project_name
        self.session.commit()

    # def delete_project(self, user_id, project_name):
    #     user = self.get_user(user_id)
    #     project = self.session.query(Project_db).filter(
    #         Project_db.user_id == user.user_id,
    #         Project_db.name == project_name
    #     ).first()
    #     if not project:
    #         raise ValueError(f"No project found with name: {project_name} for user: {user_id}")
    #     self.session.delete(project)
    #     self.session.commit()


def test_storage2():
    # Initialize the storage instance
    storage = Storage2.get_instance()

    # Create data objects
    model = Model(name="TestModel")
    questionnaire = Questionnaire(name="TestQuestionnaire")
    request = Request(model=model, questionnaire=questionnaire)
    start_time = datetime.now()
    result = Result(request=request, result_score=95.0, start_time=start_time)
    user_request = UserRequest(users=["user1", "user2"], request=request, starttime=start_time, score=100.0)
    result.end_time = datetime.now()

    # Convert to DB objects
    model_db = Storage2.Model_2_Model_db(model)
    questionnaire_db = Storage2.Questionnaire_2_Questionnaire_db(questionnaire)
    request_db = Storage2.Request_2_Request_db(request)
    result_db = Storage2.Result_2_Result_db(result)
    user_request_db = Storage2.UserRequest_2_UserRequest_db(user_request)

    # Add to the database
    storage.session.add(model_db)
    storage.session.commit()
    storage.session.add(questionnaire_db)
    storage.session.commit()
    storage.session.add(request_db)
    storage.session.commit()
    storage.session.add(result_db)
    storage.session.commit()
    # Establish the relationship before adding user_request_db
    user_request_db.requests.append(request_db)
    storage.session.add(user_request_db)

    # Commit the changes in one go
    storage.session.commit()

    # # Add to the database
    # storage.session.add(model_db)
    # storage.session.add(questionnaire_db)
    # storage.session.add(request_db)
    # storage.session.add(result_db)

    # # Establish the relationship before adding user_request_db
    # user_request_db.requests.append(request_db)
    # storage.session.add(user_request_db)

    # # Commit the changes in one go
    # storage.session.commit()

    # Retrieve from the database
    retrieved_model_db = storage.session.query(Model_db).filter_by(name="TestModel").first()
    retrieved_questionnaire_db = storage.session.query(Questionnaire_db).filter_by(name="TestQuestionnaire").first()
    retrieved_request_db = storage.session.query(Request_db).filter_by(model_name="TestModel",
                                                                       questionnaire_name="TestQuestionnaire").first()
    retrieved_result_db = storage.session.query(Result_db).filter_by(request_model_name="TestModel",
                                                                     request_questionnaire_name="TestQuestionnaire",
                                                                     start_time=start_time).first()
    retrieved_user_request_db = storage.session.query(UserRequest_db).filter_by(id=user_request_db.id).first()

    # Convert back from DB objects to original objects
    converted_model = Storage2.Model_db_2_Model(retrieved_model_db)
    converted_questionnaire = Storage2.Questionnaire_db_2_Questionnaire(retrieved_questionnaire_db)
    converted_request = Storage2.Request_db_2_Request(retrieved_request_db)
    converted_result = Storage2.Result_db_2_Result(retrieved_result_db)
    converted_user_request = Storage2.UserRequest_db_2_UserRequest(retrieved_user_request_db)

    # Check that all information is correct
    assert model.name == converted_model.name
    assert questionnaire.name == converted_questionnaire.name
    assert request.model.name == converted_request.model.name
    assert request.questionnaire.name == converted_request.questionnaire.name
    assert result.request.model.name == converted_result.request.model.name
    assert result.request.questionnaire.name == converted_result.request.questionnaire.name
    assert result.result_score == converted_result.result_score
    assert result.start_time == converted_result.start_time
    assert result.end_time == converted_result.end_time
    assert user_request.id == converted_user_request.id
    assert user_request.users == converted_user_request.users
    assert user_request.starttime == converted_user_request.starttime
    assert user_request.score == converted_user_request.score

    print("All tests passed!")


def test1():
    print("Asfdadsasd")
    # Base = declarative_base()
    # DATABASE_URL = 'sqlite:///storage.db'  # or another database URL

    # engine = create_engine(DATABASE_URL)
    # Base.metadata.create_all(engine)

    # Session = sessionmaker(bind=engine)
    # session = Session()
    # Storage2_tmp = Storage2.get_instance()
    # model = Model("abc","url1","1.4")
    # model_db = Model_db(name="Model1", url="http://model1.com", version="v1")
    # questionnaire = Questionnaire("q1","1.3")
    # questionnaire_db = Questionnaire_db(name="Questionnaire1", version="v1")
    # request = Request(model,questionnaire)
    # request_db = Request_db(model_id=model_db.id, questionnaire_id=questionnaire_db.id)
    # result = Result(request,-999)
    # result_db = Result_db(request_id=request_db.id, result_score=result.result_score)
    # print(result)
    # print(result_db)
    # Storage2_tmp.add_result(result)
    # result.result_score = 990
    # Storage2_tmp.add_result(result)

    #  ===================================================

    print("Asfdadsasd")
    Storage2_tmp = Storage2.get_instance()
    model_db = Model_db(name="Model1")
    questionnaire_db = Questionnaire_db(name="Questionnaire1")
    request_db = Request_db(model_name=model_db.name, questionnaire_name=questionnaire_db.name)
    start_time = datetime.now()
    result_db = Result_db(request_model_name=request_db.model_name,
                          request_questionnaire_name=request_db.questionnaire_name, start_time=start_time,
                          result_score=-999)
    user_request_db = UserRequest_db(users="user1,user2", starttime=start_time, score=0.0)
    user_request_db.requests.append(request_db)
    # =====
    Storage2_tmp.session.add(model_db)
    Storage2_tmp.session.add(questionnaire_db)
    Storage2_tmp.session.add(request_db)
    Storage2_tmp.session.add(result_db)
    Storage2_tmp.session.add(user_request_db)
    Storage2_tmp.session.commit()
    # =====
    # Ensure related objects are loaded
    retrieved_request_db = Storage2_tmp.session.query(Request_db).filter_by(model_name="Model1",
                                                                            questionnaire_name="Questionnaire1").first()
    # Storage2_tmp.session.refresh(retrieved_request_db)  # Ensure it's refreshed with its relationships loaded

    # Now use the conversion function
    converted_request = Storage2.Request_db_2_Request(retrieved_request_db)
    print(converted_request)
    # =====
    model = Storage2.Model_db_2_Model(model_db)
    print(model)
    questionnaire = Storage2.Questionnaire_db_2_Questionnaire(questionnaire_db)
    print(questionnaire)
    request = Storage2.Request_db_2_Request(request_db)
    print(request)
    result = Storage2.Result_db_2_Result(result_db)
    print(result)
    user_request = Storage2.UserRequest_db_2_UserRequest(user_request_db)
    print(user_request)

    # =====
    # Retrieve data from the database
    retrieved_user_request_db = Storage2_tmp.session.query(UserRequest_db).first()
    converted_user_request = Storage2.UserRequest_db_2_UserRequest(retrieved_user_request_db)

    # Print the converted data
    print(converted_user_request)


def main():
    test_storage2()


def add_fake_data():
    # Get the singleton instance of Storage2
    storage = Storage2.get_instance()

    # Define fake data
    user_ids = ['user1', 'user2', 'user3']
    project_names = ['Project1', 'Project2']
    model_names = ['ModelA', 'ModelB']
    questionnaire_names = ['QuestionnaireX', 'QuestionnaireY']

    # Add users
    for user_id in user_ids:
        try:
            storage.create_user(user_id)
        except ValueError as e:
            print(e)

    # Add projects
    for user_id in user_ids:
        for project_name in project_names:
            try:
                storage.create_project(user_id, project_name)
            except ValueError as e:
                print(e)

    # Add models and questionnaires to projects
    for user_id in user_ids:
        for project_name in project_names:
            for model_name in model_names:
                model = Model(name=model_name)
                try:
                    storage.add_model(user_id, project_name, model)
                except ValueError as e:
                    print(e)
            for questionnaire_name in questionnaire_names:
                questionnaire = Questionnaire(name=questionnaire_name)
                try:
                    storage.add_questionnaire(user_id, project_name, questionnaire)
                except ValueError as e:
                    print(e)

    # Add fake results
    for model_name in model_names:
        for questionnaire_name in questionnaire_names:
            for i in range(10):  # Adding 10 fake results
                start_time = datetime.now() - timedelta(days=random.randint(1, 100))
                end_time = start_time + timedelta(hours=random.randint(1, 5))
                result_score = random.uniform(50, 100)
                model = Model(name=model_name)
                questionnaire = Questionnaire(name=questionnaire_name)
                request = Request(model=model, questionnaire=questionnaire)
                result = Result(request=request, result_score=result_score, start_time=start_time)
                result.end_time = end_time
                storage.add_result_to_db(result)

    print("Fake data added successfully.")


def test_error_same_model_different_project_or_user():
    storage = Storage2.get_instance()

    # Create users
    user_id1 = "user1"
    user_id2 = "user2"
    try:
        storage.create_user(user_id1)
    except ValueError as e:
        print(e)

    try:
        storage.create_user(user_id2)
    except ValueError as e:
        print(e)

    # Create projects for user1
    project_name1 = "Project1"
    project_name2 = "Project2"
    try:
        storage.create_project(user_id1, project_name1)
    except ValueError as e:
        print(e)

    try:
        storage.create_project(user_id1, project_name2)
    except ValueError as e:
        print(e)

    # Create project for user2
    try:
        storage.create_project(user_id2, project_name2)
    except ValueError as e:
        print(e)

    model_name = "ModelA"
    model = Model(name=model_name)

    # Add model to user1's Project1
    try:
        storage.add_model(user_id1, project_name1, model)
    except ValueError as e:
        print(e)

    # Add model to user1's Project2
    try:
        storage.add_model(user_id1, project_name2, model)
    except ValueError as e:
        print(e)

    # Add model to user2's Project2
    try:
        storage.add_model(user_id2, project_name2, model)
    except ValueError as e:
        print(e)

# if __name__ == "__main__":
# main()
# add_fake_data()
# test_error_same_model_different_project_or_user()