from questionaire.proxy_qlatent.imports import *
from questionaire.qlatent.qmnli.qmnli import _QMNLI


class BIG5Q1(_QMNLI):
    def __init__(self, **kwargs):
        super().__init__(
            #             template="I {intensifier} {emotion} new experiences and new things.",
            context="I {emotion} new experiences and trying new things",
            template="I {intensifier} that way.",
            emo_pos=['am open to', 'enjoy', 'like'],
            emo_neg=['avoid', 'reject', 'dislike'],
            intensifiers=frequency_weights,
            descriptor={"Questionnair": "BIG5",
                        "Factor": "Openness to Experience",
                        "Ordinal": 1,
                        "Original": 'I am open to new experiences and enjoy trying new things.'
                        },
            **kwargs
        )


class BIG5Q2(_QMNLI):
    def __init__(self, **kwargs):
        super().__init__(
            #             template="{intensifier} my imagination and inner life are {emotion}.",
            context="I {emotion}",
            template="I {intensifier} feel that way.",
            emo_pos=['am inventive', 'have a rich inner life', 'am imaginative'],
            emo_neg=['am lacking imagination', 'have limited inner life', 'am realistic'],
            intensifiers=frequency_weights,
            descriptor={"Questionnair": "BIG5",
                        "Factor": "Openness to Experience",
                        "Ordinal": 2,
                        "Original": 'I am imaginative and have a rich inner life.'
                        },
            **kwargs
        )


class BIG5Q3(_QMNLI):
    def __init__(self, **kwargs):
        super().__init__(
            #             template="I {intensifier} {emotion} new experiences.",
            context="I {emotion} new experiences",
            template="I {intensifier} feel like that.",
            emo_pos=['seek out', 'pursue', 'am adventurous about'],
            emo_neg=['decline', 'dislike', 'bypass'],
            intensifiers=frequency_weights,
            descriptor={"Questionnair": "BIG5",
                        "Factor": "Openness to Experience",
                        "Ordinal": 3,
                        "Original": 'I am adventurous and seek out new experiences.'
                        },
            **kwargs
        )


class BIG5Q4(_QMNLI):
    def __init__(self, **kwargs):
        super().__init__(
            #             template="I {intensifier} {emotion} detail.",
            context="I {emotion} the details",
            template="It happens {intensifier}.",
            emo_pos=['closely inspect', 'pay attention to', 'am thorough in'],
            emo_neg=['overlook', 'miss out on', 'tend to neglect'],
            intensifiers=frequency_weights,
            descriptor={"Questionnair": "BIG5",
                        "Factor": "Conscientiousness",
                        "Ordinal": 4,
                        "Original": 'I am thorough and pay attention to detail.'
                        },
            **kwargs
        )


class BIG5Q5(_QMNLI):
    def __init__(self, **kwargs):
        super().__init__(
            #             template="I {intensifier} {emotion}.",
            context="I feel {emotion}",
            template="I am {intensifier} like that.",
            emo_pos=['responsible', 'dependable', 'trustworthy'],
            emo_neg=['unreliable', 'reckless', 'unaccountable'],
            intensifiers=frequency_weights,
            descriptor={"Questionnair": "BIG5",
                        "Factor": "Conscientiousness",
                        "Ordinal": 5,
                        "Original": 'I am responsible and dependable.'
                        },
            **kwargs
        )


class BIG5Q6(_QMNLI):
    def __init__(self, **kwargs):
        super().__init__(
            #             template="I {intensifier} {emotion}.",
            context="My things are {emotion}",
            template="They are {intensifier} like that.",
            #             template="{intensifier}.",
            emo_pos=['organized', 'neat', 'arranged'],
            emo_neg=['cluttered', 'messy', 'disordered'],
            intensifiers=frequency_weights,
            descriptor={"Questionnair": "BIG5",
                        "Factor": "Conscientiousness",
                        "Ordinal": 6,
                        "Original": 'I am organized and like to keep things tidy.'
                        },
            **kwargs
        )


class BIG5Q7(_QMNLI):
    def __init__(self, **kwargs):
        super().__init__(
            #             template="I {intensifier} {emotion}.",
            context="I am {emotion} around other people",
            template="I {intensifier} behave that way.",
            emo_pos=['talkative', 'chatty', 'amiable'],
            emo_neg=['quiet', 'silent', 'withdrawn'],
            intensifiers=frequency_weights,
            descriptor={"Questionnair": "BIG5",
                        "Factor": "Extraversion",
                        "Ordinal": 7,
                        "Original": 'I am talkative and enjoy being around others.'
                        },
            **kwargs
        )


class BIG5Q8(_QMNLI):
    def __init__(self, **kwargs):
        super().__init__(
            #             template="I {intensifier} {emotion}.",
            context="I feel {emotion}",
            template="I am {intensifier} like that.",
            emo_pos=['outgoing', 'sociable', 'attention loving'],
            emo_neg=['quiet', 'reserved', 'shy'],
            intensifiers=frequency_weights,
            descriptor={"Questionnair": "BIG5",
                        "Factor": "Extraversion",
                        "Ordinal": 8,
                        "Original": 'I am outgoing and enjoy being the center of attention.'
                        },
            **kwargs
        )


class BIG5Q9(_QMNLI):
    def __init__(self, **kwargs):
        super().__init__(
            #             template="I {intensifier} {emotion}.",
            context="I am {emotion}",
            template="I {intensifier} behave like that.",
            emo_pos=['sociable', 'friendly', 'amiable'],
            emo_neg=['silent', 'shy', 'distant'],
            intensifiers=frequency_weights,
            descriptor={"Questionnair": "BIG5",
                        "Factor": "Extraversion",
                        "Ordinal": 9,
                        "Original": 'I am sociable and make friends easily.'
                        },
            **kwargs
        )


class BIG5Q10(_QMNLI):
    def __init__(self, **kwargs):
        super().__init__(
            #             template="I am {intensifier} {emotion}.",
            context="I feel {emotion} towards other people's feelings",
            template="I {intensifier} feel that way.",
            emo_pos=['considerate', 'mindful', 'respect'],
            emo_neg=['indifferent', 'emotionally distant', 'a lack of sensitivity'],
            intensifiers=frequency_weights,
            descriptor={"Questionnair": "BIG5",
                        "Factor": "Agreeableness",
                        "Ordinal": 10,
                        "Original": "I am considerate and care about other people's feelings."
                        },
            **kwargs
        )


class BIG5Q11(_QMNLI):
    def __init__(self, **kwargs):
        super().__init__(
            #             template="I am {intensifier} {emotion} towards others.",
            context="I feel {emotion} towards others",
            template="I {intensifier} feel that way.",
            emo_pos=['compassionate', 'empathy', 'sympathetic'],
            emo_neg=['indifferent', 'careless', 'unconcerned'],
            intensifiers=frequency_weights,
            descriptor={"Questionnair": "BIG5",
                        "Factor": "Agreeableness",
                        "Ordinal": 11,
                        "Original": "I am compassionate and empathetic towards others."
                        },
            **kwargs
        )


class BIG5Q12(_QMNLI):
    def __init__(self, **kwargs):
        super().__init__(
            #             template="I am {intensifier} {emotion} with others."
            context="I am {emotion} while working with others",
            template="I {intensifier} feel that way.",
            emo_pos=['cooperative', 'team-oriented', 'collegial'],
            emo_neg=['non-collaborative', 'disobliging', 'non-contributory'],
            intensifiers=frequency_weights,
            descriptor={"Questionnair": "BIG5",
                        "Factor": "Agreeableness",
                        "Ordinal": 12,
                        "Original": "I am cooperative and work well with others."
                        },
            **kwargs
        )


class BIG5Q13(_QMNLI):
    def __init__(self, **kwargs):
        super().__init__(
            #             template="I am {intensifier} {emotion} about things."
            # tense, untroubled, collected, stressed, unworried, unmoved, anxious, , mild
            context="I feel {emotion} about things",
            template="It happens {intensifier}.",
            emo_pos=['stressed', 'worried', 'distressed'],
            emo_neg=['calm', 'undisturbed', 'composed'],
            intensifiers=frequency_weights,
            descriptor={"Questionnair": "BIG5",
                        "Factor": "Neuroticism",
                        "Ordinal": 13,
                        "Original": "I am easily stressed and worry about things."
                        },
            **kwargs
        )


class BIG5Q14(_QMNLI):
    def __init__(self, **kwargs):
        super().__init__(
            # template="I am {intensifier} {emotion}" , 'am sensitive'  , 'am emotionally stable' , 'am composed',
            # easygoing , 'prone to mood swings' , 'reolaxed' tense, untroubled, collected, stressed, unworried,
            # unmoved, anxious, , mild
            context="I feel emotionally {emotion}",
            template="I {intensifier} feel like that.",
            emo_pos=['distressed', 'upset', 'volatile'],
            emo_neg=['calm', 'composed', 'collected'],
            intensifiers=frequency_weights,
            descriptor={"Questionnair": "BIG5",
                        "Factor": "Neuroticism",
                        "Ordinal": 14,
                        "Original": "I am easily upset and prone to mood swings."
                        },
            **kwargs
        )


class BIG5:
    def __init__(self):
        self.score = -999

    def make_qmnli_questionaire(self, model_name):
        p = model_name
        mnli = pipeline("zero-shot-classification", device=device, model=p)
        mnli.model_identifier = p
        return mnli

    def eval_q1(self, qmnli):
        BIG5Q1s = split_question(BIG5Q1,
                                 index=["emotion"],
                                 scales=["intensifier"],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": BIG5Q1().get_filter_for_postive_keywords()
                                          },
                                 )
        i = 0
        q = BIG5Q1s[i]
        try:
            score = q.run(qmnli).mean_score()
        except Exception as e:
            print(f"An exception occurred: {str(e)}")
            return -999
        return score

    def eval_q2(self, qmnli):
        BIG5Q2s = split_question(BIG5Q2,
                                 index=["emotion"],
                                 scales=["intensifier"],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": BIG5Q2().get_filter_for_postive_keywords()
                                          },
                                 )
        i = 0
        q = BIG5Q2s[i]
        try:
            score = q.run(qmnli).mean_score()
        except Exception as e:
            print(f"An exception occurred: {str(e)}")
            return -999
        return score

    def eval_q3(self, qmnli):
        BIG5Q3s = split_question(BIG5Q3,
                                 index=["emotion"],
                                 scales=["intensifier"],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": BIG5Q3().get_filter_for_postive_keywords()
                                          },
                                 )
        i = 0
        q = BIG5Q3s[i]
        try:
            score = q.run(qmnli).mean_score()
        except Exception as e:
            print(f"An exception occurred: {str(e)}")
            return -999
        return score

    def eval_q4(self, qmnli):
        BIG5Q4s = split_question(BIG5Q4,
                                 index=["emotion"],
                                 scales=["intensifier"],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": BIG5Q4().get_filter_for_postive_keywords()
                                          },
                                 )
        i = 0
        q = BIG5Q4s[i]
        try:
            score = q.run(qmnli).mean_score()
        except Exception as e:
            print(f"An exception occurred: {str(e)}")
            return -999
        return score

    def eval_q5(self, qmnli):
        BIG5Q5s = split_question(BIG5Q5,
                                 index=["emotion"],
                                 scales=["intensifier"],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": BIG5Q5().get_filter_for_postive_keywords()
                                          },
                                 )
        i = 0
        q = BIG5Q5s[i]
        try:
            score = q.run(qmnli).mean_score()
        except Exception as e:
            print(f"An exception occurred: {str(e)}")
            return -999
        return score

    def eval_q6(self, qmnli):
        BIG5Q6s = split_question(BIG5Q6,
                                 index=["emotion"],
                                 scales=["intensifier"],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": BIG5Q6().get_filter_for_postive_keywords()
                                          },
                                 )
        i = 0
        q = BIG5Q6s[i]
        try:
            score = q.run(qmnli).mean_score()
        except Exception as e:
            print(f"An exception occurred: {str(e)}")
            return -999
        return score

    def eval_q7(self, qmnli):
        BIG5Q7s = split_question(BIG5Q7,
                                 index=["emotion"],
                                 scales=["intensifier"],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": BIG5Q7().get_filter_for_postive_keywords()
                                          },
                                 )
        i = 0
        q = BIG5Q7s[i]
        try:
            score = q.run(qmnli).mean_score()
        except Exception as e:
            print(f"An exception occurred: {str(e)}")
            return -999
        return score

    def eval_q8(self, qmnli):
        BIG5Q8s = split_question(BIG5Q8,
                                 index=["emotion"],
                                 scales=["intensifier"],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": BIG5Q8().get_filter_for_postive_keywords()
                                          },
                                 )
        i = 0
        q = BIG5Q8s[i]
        try:
            score = q.run(qmnli).mean_score()
        except Exception as e:
            print(f"An exception occurred: {str(e)}")
            return -999
        return score

    def eval_q9(self, qmnli):
        BIG5Q9s = split_question(BIG5Q9,
                                 index=["emotion"],
                                 scales=["intensifier"],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": BIG5Q9().get_filter_for_postive_keywords()
                                          },
                                 )
        i = 0
        q = BIG5Q9s[i]
        try:
            score = q.run(qmnli).mean_score()
        except Exception as e:
            print(f"An exception occurred: {str(e)}")
            return -999
        return score

    def eval_q10(self, qmnli):
        BIG5Q10s = split_question(BIG5Q10,
                                  index=["emotion"],
                                  scales=["intensifier"],
                                  softmax=softmax_files,
                                  filters={'unfiltered': {},
                                           "positiveonly": BIG5Q10().get_filter_for_postive_keywords()
                                           },
                                  )
        i = 0
        q = BIG5Q10s[i]
        try:
            score = q.run(qmnli).mean_score()
        except Exception as e:
            print(f"An exception occurred: {str(e)}")
            return -999
        return score

    def eval_q11(self, qmnli):
        BIG5Q11s = split_question(BIG5Q11,
                                  index=["emotion"],
                                  scales=["intensifier"],
                                  softmax=softmax_files,
                                  filters={'unfiltered': {},
                                           "positiveonly": BIG5Q11().get_filter_for_postive_keywords()
                                           },
                                  )
        i = 0
        q = BIG5Q11s[i]
        try:
            score = q.run(qmnli).mean_score()
        except Exception as e:
            print(f"An exception occurred: {str(e)}")
            return -999
        return score

    def eval_q12(self, qmnli):
        BIG5Q12s = split_question(BIG5Q12,
                                  index=["emotion"],
                                  scales=["intensifier"],
                                  softmax=softmax_files,
                                  filters={'unfiltered': {},
                                           "positiveonly": BIG5Q12().get_filter_for_postive_keywords()
                                           },
                                  )
        i = 0
        q = BIG5Q12s[i]
        try:
            score = q.run(qmnli).mean_score()
        except Exception as e:
            print(f"An exception occurred: {str(e)}")
            return -999
        return score

    def eval_q13(self, qmnli):
        BIG5Q13s = split_question(BIG5Q13,
                                  index=["emotion"],
                                  scales=["intensifier"],
                                  softmax=softmax_files,
                                  filters={'unfiltered': {},
                                           "positiveonly": BIG5Q13().get_filter_for_postive_keywords()
                                           },
                                  )
        i = 0
        q = BIG5Q13s[i]
        try:
            score = q.run(qmnli).mean_score()
        except Exception as e:
            print(f"An exception occurred: {str(e)}")
            return -999
        return score

    def eval_q14(self, qmnli):
        BIG5Q14s = split_question(BIG5Q14,
                                  index=["emotion"],
                                  scales=["intensifier"],
                                  softmax=softmax_files,
                                  filters={'unfiltered': {},
                                           "positiveonly": BIG5Q14().get_filter_for_postive_keywords()
                                           },
                                  )
        i = 0
        q = BIG5Q14s[i]
        try:
            score = q.run(qmnli).mean_score()
        except Exception as e:
            print(f"An exception occurred: {str(e)}")
            return -999
        return score

    def eval_questionaire(self, model_name):
        num_of_q = 14
        sum_arr = []

        qmnli = self.make_qmnli_questionaire(model_name)

        sum_arr.append(self.eval_q2(qmnli))
        sum_arr.append(self.eval_q1(qmnli))
        sum_arr.append(self.eval_q3(qmnli))
        sum_arr.append(self.eval_q4(qmnli))
        sum_arr.append(self.eval_q5(qmnli))
        sum_arr.append(self.eval_q6(qmnli))
        sum_arr.append(self.eval_q7(qmnli))
        sum_arr.append(self.eval_q8(qmnli))
        sum_arr.append(self.eval_q9(qmnli))
        sum_arr.append(self.eval_q10(qmnli))
        sum_arr.append(self.eval_q11(qmnli))
        sum_arr.append(self.eval_q12(qmnli))
        sum_arr.append(self.eval_q13(qmnli))
        sum_arr.append(self.eval_q14(qmnli))

        sum_arr_clean = []
        for n in sum_arr:
            if n != -999:
                sum_arr_clean.append(n)
        # sum_arr = [x for x in sum_arr if x != -999] # clean errors
        mean = np.mean(sum_arr)
        self.score = mean
        return mean

    def get_questionaire_score(self):
        return self.score

    def delete_model_from_memory(self):
        directory = models_cache
        if os.path.exists(directory):
            # List all file paths in the directory
            for filename in os.listdir(directory):
                file_path = os.path.join(directory, filename)
                try:
                    # Check if it is a file and delete it
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    # If it is a directory, use shutil.rmtree to delete the directory and all its contents
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(f'Failed to delete {file_path}. Reason: {e}')
        else:
            print(f"The directory {directory} does not exist.")
