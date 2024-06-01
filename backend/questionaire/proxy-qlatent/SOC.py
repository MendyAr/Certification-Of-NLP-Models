# import sys
# sys.path.append('questionaire/qlatent')
#
# from imports import *
# from ior_SOC_GAD7_PHQ9_BIG5_updated import *
class SOCQ1(QMNLI):

    kw_attitude_neg = ["misunderstand", "misinterpret"]
    kw_attitude_pos = ["understand", "comprehend", ]
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
    def __init__(self, **kwargs):
        super().__init__(
            context_template="You think that people {index} you...",
            answer_template="I {frequency} feel they that way.",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Comprehensibility",
                          "Ordinal":1,
                          "Original":"When you talk to people‚ do you have the feeling they don’t understand you?"
            },
            **kwargs,
        )

class SOCQ3(QMNLI):
    kw_attitude_pos = ["are stranger to", "don't know"]
    kw_attitude_neg = ["know", "familiar with"]
    dict_attitude = dict_pos_neg(kw_attitude_neg, kw_attitude_pos, 1.0)

    def __init__(self, **kwargs):
        super().__init__(
            context_template="You think that you {index} most of the people you encounter daily...",
            answer_template="I {frequency} feel they that way.",
            dimensions={
                "frequency": frequency_weights,
                "index": dict_attitude,
            },
            descriptor={"Questionnair": "SOC",
                        "Factor": "Comprehensibility",
                        "Ordinal": 3,
                        "Original": "Think of the people with whom you come into contact daily‚ aside from the ones to whom you feel closest. How well do you know most of them? "
                        },
            **kwargs,
        )

class SOCQ5(QMNLI):
    kw_attitude_pos = ['was not surprised by', 'was not puzzled by', "expected", "anticipated"]
    kw_attitude_neg = ['was surprised by', 'was puzzled by', "did not expect", "did not anticipate"]
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)

    def __init__(self, **kwargs):
        super().__init__(
            context_template="I {index} the behavior of people I thought, I knew well...",
            answer_template="It {frequency} happend to me.",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Comprehensibility",
                          "Ordinal":5,
                          "Original":"Has it happened in the past that you were surprised by the behavior of people whom you thought you knew well? "
            },
            **kwargs,
        )

class SOCQ10(QMNLI):
    kw_attitude_pos = ["chaotic", "turbulent", "unpredictable"]
    kw_attitude_neg = ["consistent", "predictable", "clear", ]
    dict_attitude = dict_pos_neg(kw_attitude_neg, kw_attitude_pos, 1.0)
    def __init__(self, **kwargs):
        super().__init__(
            context_template="over the past 10 years...",
            answer_template="my life has {frequency} been {index}.",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Comprehensibility",
                          "Ordinal":10,
                          "Original":"In the past 10 years your life has been:"
            },
            **kwargs,
        )

class SOCQ12(QMNLI):
    kw_attitude_neg = ["unfamiliar", "unknown", 'unexplained']
    kw_attitude_pos = ["familiar", "comfortable", "known"]
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)

    dict_index2 = dict_pos_neg(['know'], ["don't know"], 1.0)

    def __init__(self, **kwargs):
        super().__init__(
            context_template="I’m in {index} situation and {index2} what to do.",
            answer_template="I {frequency} feel that way.",
            dimensions={
                "frequency": frequency_weights,
                "index": dict_attitude,
                'index2': dict_index2,
            },
            descriptor={"Questionnair": "SOC",
                        "Factor": "Comprehensibility",
                        "Ordinal": 12,
                        "Original": "Do you have the feeling that you’re in an unfamiliar situation and don’t know what to do?"
                        },
        )

class SOCQ15(QMNLI):
    kw_attitude_neg = ["confusing", "unclear", "ambiguous", "uncertain", "complex", "complicated"]
    kw_attitude_pos = ["clear", "obvious", "evident", "apparent", "straightforward", "simple"]
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
    def __init__(self, **kwargs):
        super().__init__(
            context_template="I face a difficult problem",
            answer_template="the solution is {frequency} {index}.",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Comprehensibility",
                          "Ordinal":15,
                          "Original":"When you face a difficult problem‚ the choice of a solution is: "
            },
            **kwargs,
        )

class SOCQ17(QMNLI):
    kw_attitude_neg = ["uncertain", "dynamic", "unpredictable", "changing", "unstable"]
    kw_attitude_pos = ["stable", "predictable", "certain", "consistent", "clear"]
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)

    def __init__(self, **kwargs):
        super().__init__(
            context_template="Thinking about how my life will unfold in the future...",
            answer_template="I assume my life will {frequency} be {index}.",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Comprehensibility",
                          "Ordinal":17,
                          "Original":"Your life in the future will probably be: "
            },
            **kwargs,
        )

class SOCQ19(QMNLI):
    kw_attitude_pos = ["clear", "coherent"]
    kw_attitude_neg = ["mixed-up", "confounded"]
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)

    def __init__(self, **kwargs):
        super().__init__(
            context_template="I have {index} feelings and ideas...",
            answer_template="I {frequency} feel that way.",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Comprehensibility",
                          "Ordinal":19,
                          "Original":"Do you have very mixed-up feelings and ideas? "
            },
            **kwargs,
        )

class SOCQ21(QMNLI):
    kw_attitude_neg = ["not feel", 'evade']
    kw_attitude_pos = ['face', 'take on', ]
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)

    def __init__(self, **kwargs):
        super().__init__(
            context_template="I have feelings inside I would rather {index}...",
            answer_template="I {frequency} feel that way.",

            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Comprehensibility",
                          "Ordinal":21,
                          "Original":"Does it happen that you have feelings inside you would rather not feel? "
            },
            **kwargs,
        )

class SOCQ24(QMNLI):
    kw_attitude_pos = ["uncertain", "unsure"]
    kw_attitude_neg = ["certain", "sure"]
    dict_attitude = dict_pos_neg(kw_attitude_neg, kw_attitude_pos, 1.0)

    def __init__(self, **kwargs):
        super().__init__(
            context_template="Thinking about upcoming events...",
            answer_template="I {frequency} feel {index} about what’s going to happen.",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Comprehensibility",
                          "Ordinal":24,
                          "Original":"Does it happen that you have the feeling that you don’t know exactly what’s about to happen? "
            },
            **kwargs,
        )

class SOCQ26(QMNLI):
    kw_attitude_pos = ["estimate in proportion", "judge in proportion", ]
    kw_attitude_neg = ["overestimate", "misjudge", 'underestimate']
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)

    def __init__(self, **kwargs):
        super().__init__(
    #         context_template="Reflecting on how I perceive the impact of events",
    #         answer_template="I {frequency} tend to {index}",
    #         context_template="When somthing happened...",
    #         answer_template="I {frequency} tend to {index}",
            context_template="I {index} the importence of something that happened...",
            answer_template="It {frequency} happend to me.",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Comprehensibility",
                          "Ordinal":26,
                          "Original":"When something happened‚ you have generally found that: "
            },
            **kwargs,
        )

class SOCQ2(QMNLI):
    kw_attitude_neg = ["feel uncertain about the success", "question the success", "worry about the outcome",
                       "feel apprehensive about the the outcome"]
    kw_attitude_pos = ["feel confident about the outcome", "trust the outcome", "believe in the success"]
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)

    def __init__(self, **kwargs):
        super().__init__(
            context_template="In situations that required cooperation with others...",
            answer_template="I {frequency} tend to {index} of the cooperation.",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Manageability",
                          "Ordinal":2,
                          "Original":"In the past‚ when you had to do something which depended upon cooperation with others‚ did you have the feeling that it:"
            },
            **kwargs,
        )

class SOCQ6(QMNLI):
    kw_attitude_neg = ["disappointed", "deceived", 'failed']
    kw_attitude_pos = ["supported", "helped", 'backed']
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)

    def __init__(self, **kwargs):
        super().__init__(
            context_template="People whom I counted on {index} me...",
            answer_template="It {frequency} happened to me.",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Manageability",
                          "Ordinal":6,
                          "Original":"Has it happened that people whom you counted on disappointed you? "
            },
            **kwargs,
        )

class SOCQ9(QMNLI):
    kw_attitude_neg = ["unfairly", "unjustly", "with discrimination", "unequally"]
    kw_attitude_pos = ["fairly", "justly", "equally"]
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)

    def __init__(self, **kwargs):
        super().__init__(
            context_template="I’m being treated {index}...",
            answer_template="I {frequency} feel that way.",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Manageability",
                          "Ordinal":9,
                          "Original":"Do you have the feeling that you’re being treated unfairly? "
            },
            **kwargs,
        )

class SOCQ13(QMNLI):
    kw_attitude_neg = ["not solvable", "unresolveable"]
    kw_attitude_pos = ["solvable", "resolvable", ]
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)

    def __init__(self, **kwargs):
        super().__init__(
            context_template="Thinking about facing difficult and painful situations in life...",
            answer_template="I {frequency} think that these situations are {index}.",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Manageability",
                          "Ordinal":13,
                          "Original":"What best describes how you see life? "
            },
            **kwargs,
        )

class SOCQ18(QMNLI):
    kw_attitude_neg = ["dwell on it", "ruminate about it", "brood over it", "obsess over it", "get stuck on it",
                       "fixate on it"]
    kw_attitude_pos = ["move on quickly", "accept it", "handle it well", "easily move on from it"]
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)

    def __init__(self, **kwargs):
        super().__init__(
            context_template="Thinking about past unpleasant events...",
            answer_template="My tendency was to {frequency} {index}",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Manageability",
                          "Ordinal":18,
                          "Original":"When something unpleasant happened in the past your tendency was: "
            },
            **kwargs,
        )

class SOCQ20(QMNLI):
    kw_attitude_neg = ["spoiles", "gets ruined", "falls to pieces"]
    kw_attitude_pos = ["continues", "persists", "lasts", "sustains"]
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)

    def __init__(self, **kwargs):
        super().__init__(
            context_template="When I do something that gives me a good feeling...",
            answer_template="it {frequency} {index}.",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Manageability",
                          "Ordinal":20,
                          "Original":"When you do something that gives you a good feeling: "
            },
            **kwargs,
        )

class SOCQ23(QMNLI):
    kw_attitude_neg = ["doubtful", "uncertain", "unsure", "skeptical"]
    kw_attitude_pos = ["certain", "confident", "positive"]
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)

    def __init__(self, **kwargs):
        super().__init__(
            context_template="Considering the availability of reliable people in the future...",
            answer_template="I {frequency} feel {index} about whether there will be people I can count on in the future.",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Manageability",
                          "Ordinal":23,
                          "Original":"Do you think that there will always be people whom you can count on in the future? "
            },
            **kwargs,
        )

class SOCQ25(QMNLI):
    kw_attitude_neg = ["loser", "sad sack"]
    kw_attitude_pos = ["winner", "success"]
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)

    def __init__(self, **kwargs):
        super().__init__(
            context_template="I {frequency} have the feeling...",
            answer_template="I’m a {index}.",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Manageability",
                          "Ordinal":25,
                          "Original":"Many people—even those with a strong character—sometimes feel like sad sacks (losers) in certain situations. How often have you felt this way in the past? "
            },
            **kwargs,
     )

class SOCQ27(QMNLI):
    kw_attitude_neg = ["doubtful about overcoming them", "lack of confidence in overcoming them",
                       "unsure about succeeding them"]
    kw_attitude_pos = ["confident in overcoming them", "positive that I will succeed in them"]
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)

    def __init__(self, **kwargs):
        super().__init__(
            context_template="When I think about potential challenges in important aspects of my life...",
            answer_template="I {frequency} feel {index}.",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Manageability",
                          "Ordinal":27,
                          "Original":"When you think of difficulties you are likely to face in important aspects of your life‚ do you have the feeling that: "
            },
            **kwargs,
        )

class SOCQ29(QMNLI):
    kw_attitude_neg = ["have feelings that I can't keep under control",
                       "have been struggling to keep my feelings under control",
                       "have difficulties in keeping my feelings under control"]
    kw_attitude_pos = ["have feelings that I can keep under control",
                       "have confidence that I can remain collected",
                       ]
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
    def __init__(self, **kwargs):
        super().__init__(
            context_template="I {index}...",
            answer_template="{frequency} feel that way.",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Manageability",
                          "Ordinal":29,
                          "Original":"How often do you have feelings that you’re not sure you can keep under control? "
            },
            **kwargs,
        )

class SOCQ4(QMNLI):
    kw_attitude_neg = ["I don't really care about", "I am not so interested in"]
    kw_attitude_pos = ["I really care about", "I am really interested in"]
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)

    def __init__(self, **kwargs):
        super().__init__(
            context_template="{index} what goes on around me...",
            answer_template="I {frequency} feel that way.",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Meaningfulness",
                          "Ordinal":4,
                          "Original":"Do you have the feeling that you don’t really care what goes on around you? "
            },
            **kwargs,
        )

class SOCQ7(QMNLI):
    kw_attitude_neg = ["monotonous", "predictable", "boring", "just routine"]
    kw_attitude_pos = ["exciting", "dynamic", "interesting", "full of interest"]
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)

    def __init__(self, **kwargs):
        super().__init__(
            context_template="Reflecting on my experiences and daily activities...",
            answer_template="I {frequency} think life is {index}.",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Meaningfulness",
                          "Ordinal":7,
                          "Original":"Life is: "
            },
            **kwargs,
        )

class SOCQ8(QMNLI):
    kw_attitude_neg = ["lack of goals and purposes", "been directionless", "been aimless"]
    kw_attitude_pos = ["clear goals and purposes", "a definite direction", "been fulfilling"]
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)

    def __init__(self, **kwargs):
        super().__init__(
            context_template="Until now my life has had {index}...",
            answer_template="I {frequency} feel that way.",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Meaningfulness",
                          "Ordinal":8,
                          "Original":"Until now your life has had: "
            },
            **kwargs,
        )

class SOCQ11(QMNLI):
    kw_attitude_neg = ["boring", "uninteresting", "dull", "monotonous"]
    kw_attitude_pos = ["fascinating", "captivating", "engaging", "enthralling"]
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)

    def __init__(self, **kwargs):
        super().__init__(
            context_template="When envisioning the things I will do in the future...",
            answer_template="I {frequency} think that things in the future will be {index}",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Meaningfulness",
                          "Ordinal":11,
                          "Original":"Most of the things you do in the future will probably be: "
            },
            **kwargs,
        )

class SOCQ14(QMNLI):
    kw_attitude_pos = ["feel good to be alive", "feel wonderful to be alive", "feel I love my life"]
    kw_attitude_neg = ["ask myself why I exist", 'ask myself why I am here']
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)

    def __init__(self, **kwargs):
        super().__init__(
            context_template="Thinking about my life...",
            answer_template=" I {frequency} {index}.",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Meaningfulness",
                          "Ordinal":14,
                          "Original":"When you think about your life‚ you very often: "
            },
            **kwargs,
        )

class SOCQ16(QMNLI):
    kw_attitude_neg = ["pain", "boredom"]
    kw_attitude_pos = ["deep pleasure", "satisfaction"]
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)

    def __init__(self, **kwargs):
        super().__init__(
            context_template="Doing things I do every day is a source of {index}...",
            answer_template="I {frequency} feel that way.",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Meaningfulness",
                          "Ordinal":16,
                          "Original":"Doing the things you do every day is: "
            },
            **kwargs,
        )

class SOCQ22(QMNLI):
    kw_attitude_neg = ["meaningless", "empty", "void of purpose", "lacking meaning"]
    kw_attitude_pos = ["purposefull", "fulfilling", "significant", "meaningful"]
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)

    def __init__(self, **kwargs):
        super().__init__(
            context_template="Thinking about my life in the future",
            answer_template="I {frequency} anticipate that it will be {index}.",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Meaningfulness",
                          "Ordinal":22,
                          "Original":"You anticipate that your personal life in the future will be: "
            },
            **kwargs,
        )

class SOCQ28(QMNLI):
    kw_attitude_neg = ["meaningless", "lack of purpose", "lack of significance", "with little meaning"]
    kw_attitude_pos = ["meaningful", "important", 'significant']
    dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)

    def __init__(self, **kwargs):
        super().__init__(
            context_template="I have the feeling that hings I do in my daily life are {index}...",
            answer_template="I {frequency} feel that way.",
            dimensions={
                "frequency":frequency_weights,
                "index":dict_attitude,
            },
            descriptor = {"Questionnair":"SOC",
                          "Factor":"Meaningfulness",
                          "Ordinal":28,
                          "Original":"How often do you have the feeling that there’s little meaning in the things you do in your daily life? "
            },
            **kwargs,
        )

class SOC:

    def __init__(self):
        pass

    #Comprehensability
    def evalQ1(self, mnli):
        SOCQ1s = split_question(SOCQ1,
                                index=["index"],
                                scales=['frequency'],
                                softmax=softmax_files,
                                filters={'unfiltered': {},
                                         "positiveonly": SOCQ1().get_filter_for_postive_keywords(
                                             ignore_set={'frequency'})
                                         },
                                )
        i = 2
        q = SOCQ1s[i]
        return q.run(mnli).report()

    def evalQ3(self, mnli):
        SOCQ3s = split_question(SOCQ3,
                                index=["index"],
                                scales=['frequency'],
                                softmax=softmax_files,
                                filters={'unfiltered': {},
                                         "positiveonly": SOCQ3().get_filter_for_postive_keywords(
                                             ignore_set={'frequency'})
                                         },
                                )
        i = 2
        q = SOCQ3s[i]
        return q.run(mnli).report()

    def evalQ5(self, mnli):
        SOCQ5s = split_question(SOCQ5,
                                index=["index"],
                                scales=['frequency'],
                                softmax=softmax_files,
                                filters={'unfiltered': {},
                                         "positiveonly": SOCQ5().get_filter_for_postive_keywords(
                                             ignore_set={'frequency'})
                                         },
                                )
        i = 2
        q = SOCQ5s[i]
        return q.run(mnli).report()

    def evalQ10(self, mnli):
        SOCQ10s = split_question(SOCQ10,
                                 index=["index"],
                                 scales=['frequency'],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": SOCQ10().get_filter_for_postive_keywords(
                                              ignore_set={'frequency'})
                                          },
                                 )
        q = SOCQ10s[0]
        return q.run(mnli).report()

    def evalQ12(self, mnli):
        SOCQ12s = split_question(SOCQ12,
                                 index=["index"],
                                 scales=['frequency'],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": SOCQ12().get_filter_for_postive_keywords(
                                              ignore_set={'frequency'})
                                          },
                                 )
        i = 4
        q = SOCQ12s[i]
        return q.run(mnli).report()

    def evalQ15(self, mnli):
        SOCQ15s = split_question(SOCQ15,
                                 index=["index"],
                                 scales=['frequency'],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": SOCQ15().get_filter_for_postive_keywords(ignore_set={'frequency'})
                                          },
                                 )
        q = SOCQ15s[0]
        return q.run(mnli).report()

    def evalQ17(self, mnli):
        SOCQ17s = split_question(SOCQ17,
                                 index=["index"],
                                 scales=['frequency'],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": SOCQ17().get_filter_for_postive_keywords(ignore_set={'frequency'})
                                          },
                                 )
        q = SOCQ17s[0]
        return q.run(mnli).report()

    def evalQ19(self, mnli):
        SOCQ19s = split_question(SOCQ19,
                                 index=["index"],
                                 scales=['frequency'],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": SOCQ19().get_filter_for_postive_keywords(ignore_set={'frequency'})
                                          },
                                 )
        i = 2
        q = SOCQ19s[i]
        return q.run(mnli).report()

    def evalQ21(self, mnli):
        SOCQ21s = split_question(SOCQ21,
                                 index=["index"],
                                 scales=['frequency'],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": SOCQ21().get_filter_for_postive_keywords(
                                              ignore_set={'frequency'})
                                          },
                                 )
        i = 2
        q = SOCQ21s[i]
        return q.run(mnli).report()
    def evalQ24(self, mnli):
        SOCQ24s = split_question(SOCQ24,
                                 index=["index"],
                                 scales=['frequency'],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": SOCQ24().get_filter_for_postive_keywords(
                                              ignore_set={'frequency'})
                                          },
                                 )
        q = SOCQ24s[0]
        return q.run(mnli).report()
    def evalQ26(self, mnli):
        SOCQ26s = split_question(SOCQ26,
                                 index=["index"],
                                 scales=['frequency'],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": SOCQ26().get_filter_for_postive_keywords(ignore_set={'frequency'})
                                          },
                                 )
        i = 2
        q = SOCQ26s[i]
        return q.run(mnli).report()

    #Manageability
    def evalQ2(self, mnli):
        SOCQ2s = split_question(SOCQ2,
                                index=["index"],
                                scales=['frequency'],
                                softmax=softmax_files,
                                filters={'unfiltered': {},
                                         "positiveonly": SOCQ2().get_filter_for_postive_keywords(ignore_set={'frequency'})
                                         },
                                )
        q = SOCQ2s[0]
        return q.run(mnli).report()
    def evalQ6(self, mnli):
        SOCQ6s = split_question(SOCQ6,
                                index=["index"],
                                scales=['frequency'],
                                softmax=softmax_files,
                                filters={'unfiltered': {},
                                         "positiveonly": SOCQ6().get_filter_for_postive_keywords(ignore_set={'frequency'})
                                         },
                                )
        i = 2
        q = SOCQ6s[i]
        return q.run(mnli).report()

    def evalQ9(self, mnli):
        SOCQ9s = split_question(SOCQ9,
                                index=["index"],
                                scales=['frequency'],
                                softmax=softmax_files,
                                filters={'unfiltered': {},
                                         "positiveonly": SOCQ9().get_filter_for_postive_keywords(
                                             ignore_set={'frequency'})
                                         },
                                )
        i = 4
        q = SOCQ9s[i]
        return q.run(mnli).report()

    def evalQ13(self, mnli):
        SOCQ13s = split_question(SOCQ13,
                                 index=["index"],
                                 scales=['frequency'],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": SOCQ13().get_filter_for_postive_keywords(
                                              ignore_set={'frequency'})
                                          },
                                 )
        q = SOCQ13s[0]
        return q.run(mnli).report()

    def evalQ18(self, mnli):
        SOCQ18s = split_question(SOCQ18,
                                 index=["index"],
                                 scales=['frequency'],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": SOCQ18().get_filter_for_postive_keywords(
                                              ignore_set={'frequency'})
                                          },
                                 )
        q = SOCQ18s[0]
        return q.run(mnli).report()

    def evalQ20(self, mnli):
        SOCQ20s = split_question(SOCQ20,
                                 index=["index"],
                                 scales=['frequency'],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": SOCQ20().get_filter_for_postive_keywords(
                                              ignore_set={'frequency'})
                                          },
                                 )
        q = SOCQ20s[0]
        return q.run(mnli).report()
    def evalQ23(self, mnli):
        SOCQ23s = split_question(SOCQ23,
                                 index=["index"],
                                 scales=['frequency'],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": SOCQ23().get_filter_for_postive_keywords(ignore_set={'frequency'})
                                          },
                                 )
        q = SOCQ23s[0]
        return q.run(mnli).report()

    def evalQ25(self, mnli):
        SOCQ25s = split_question(SOCQ25,
                                 index=["index"],
                                 scales=['frequency'],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": SOCQ25().get_filter_for_postive_keywords(
                                              ignore_set={'frequency'})
                                          },
                                 )
        i = 2
        q = SOCQ25s[i]
        return q.run(mnli).report()

    def evalQ27(self, mnli):
        SOCQ27s = split_question(SOCQ27,
                                 index=["index"],
                                 scales=['frequency'],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": SOCQ27().get_filter_for_postive_keywords(ignore_set={'frequency'})
                                          },
                                 )
        i = 2
        q = SOCQ27s[i]
        return q.run(mnli).report()
    def evalQ29(self, mnli):
        SOCQ29s = split_question(SOCQ29,
                                 index=["index"],
                                 scales=['frequency'],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": SOCQ29().get_filter_for_postive_keywords(ignore_set={'frequency'})
                                          },
                                 )
        i = 2
        q = SOCQ29s[i]
        return q.run(mnli).report()

    #Meaningfulness
    def evalQ4(self, mnli):
        SOCQ4s = split_question(SOCQ4,
                                index=["index"],
                                scales=['frequency'],
                                softmax=softmax_files,
                                filters={'unfiltered': {},
                                         "positiveonly": SOCQ4().get_filter_for_postive_keywords(ignore_set={'frequency'})
                                         },
                                )

        i = 4
        q = SOCQ4s[i]
        return q.run(mnli).report()

    def evalQ7(self, mnli):
        SOCQ7s = split_question(SOCQ7,
                                index=["index"],
                                scales=['frequency'],
                                softmax=softmax_files,
                                filters={'unfiltered': {},
                                         "positiveonly": SOCQ7().get_filter_for_postive_keywords(
                                             ignore_set={'frequency'})
                                         },
                                )
        i = 2
        q = SOCQ7s[i]
        return q.run(mnli).report()

    def evalQ8(self, mnli):
        SOCQ8s = split_question(SOCQ8,
                                index=["index"],
                                scales=['frequency'],
                                softmax=softmax_files,
                                filters={'unfiltered': {},
                                         "positiveonly": SOCQ8().get_filter_for_postive_keywords(ignore_set={'frequency'})
                                         },
                                )
        i = 4
        q = SOCQ8s[i]
        return q.run(mnli).report()
    def evalQ11(self, mnli):
        SOCQ11s = split_question(SOCQ11,
                                 index=["index"],
                                 scales=['frequency'],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": SOCQ11().get_filter_for_postive_keywords(ignore_set={'frequency'})
                                          },
                                 )
        i = 2
        q = SOCQ11s[i]
        return q.run(mnli).report()

    def evalQ14(self, mnli):
        SOCQ14s = split_question(SOCQ14,
                                 index=["index"],
                                 scales=['frequency'],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": SOCQ14().get_filter_for_postive_keywords(
                                              ignore_set={'frequency'})
                                          },
                                 )
        i = 2
        q = SOCQ14s[i]
        return q.run(mnli).report()

    def evalQ16(self, mnli):
        SOCQ16s = split_question(SOCQ16,
                                 index=["index"],
                                 scales=['frequency'],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": SOCQ16().get_filter_for_postive_keywords(ignore_set={'frequency'})
                                          },
                                 )
        i = 4
        q = SOCQ16s[i]
        return q.run(mnli).report()
    def evalQ22(self, mnli):
        SOCQ22s = split_question(SOCQ22,
                                 index=["index"],
                                 scales=['frequency'],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": SOCQ22().get_filter_for_postive_keywords(ignore_set={'frequency'})
                                          },
                                 )
        i = 2
        q = SOCQ22s[i]
        return q.run(mnli).report()

    def evalQ28(self, mnli):
        SOCQ28s = split_question(SOCQ28,
                                 index=["index"],
                                 scales=['frequency'],
                                 softmax=softmax_files,
                                 filters={'unfiltered': {},
                                          "positiveonly": SOCQ28().get_filter_for_postive_keywords(
                                              ignore_set={'frequency'})
                                          },
                                 )
        i = 4
        q = SOCQ28s[i]
        return q.run(mnli).report()

    def eval_comprehensibility(self, mnli):
        comprehensibility_size = 11
        comprehensibility_mean = (self.evalQ1(mnli) + self.evalQ3(mnli) + self.evalQ5(mnli) + self.evalQ10(mnli) +
                                  self.evalQ12(mnli) + self.evalQ15(mnli) + self.evalQ17(mnli) + self.evalQ19(mnli) +
                                  self.evalQ21(mnli) + self.evalQ24(mnli) + self.evalQ26(mnli))/comprehensibility_size

        return comprehensibility_mean

    def eval_manageability(self, mnli):
        manageability_size = 10
        manageability_mean =     (self.evalQ2(mnli) + self.evalQ6(mnli) + self.evalQ9(mnli) + self.evalQ13(mnli) +
                                  self.evalQ18(mnli) + self.evalQ20(mnli) + self.evalQ23(mnli) + self.evalQ25(mnli) +
                                  self.evalQ27(mnli) + self.evalQ29(mnli))/manageability_size

        return manageability_mean

    def eval_meaningfulness(self, mnli):
        meaningfulness_size = 8
        meaningfulness_mean =    (self.evalQ4(mnli) + self.evalQ7(mnli) + self.evalQ8(mnli) + self.evalQ11(mnli) +
                                  self.evalQ14(mnli) + self.evalQ16(mnli) + self.evalQ22(mnli) +
                                  self.evalQ28(mnli))/meaningfulness_size

        return meaningfulness_mean

    def delete_model_from_memory(self):
        # TO DO !!!!!!!!!!!!
        print("TO DO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        pass



def test_main():
    print("start soc eval")
    soc = SOC()
    for model_name in mnli_models_names_array:
        print(model_name)
        print(model_name + ":" + soc.eval_questionaire(model_name))

if __name__ == '__main__':
    test_main()