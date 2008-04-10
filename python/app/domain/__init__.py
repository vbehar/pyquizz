#!/usr/bin/env python

from google.appengine.ext import db

class Quizz(db.Model):
    # key name = quizz name (unique)
    name = db.StringProperty()
    description = db.TextProperty()
    password_access = db.StringProperty()
    password_results = db.StringProperty()
    password_admin = db.StringProperty()
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)

class Question(db.Model):
    quizz = db.ReferenceProperty(reference_class=Quizz, collection_name="questions")
    question = db.StringProperty()
    items = db.StringListProperty()
    answer = db.IntegerProperty()
    more_infos = db.StringProperty()
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)

class Participant(db.Model):
    # key name = uuid - stored in a cookie (unique)
    name = db.StringProperty(default = "Anonyme")
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)

class QuizzParticipation(db.Model):
    participant = db.ReferenceProperty(reference_class=Participant, collection_name="participations")
    quizz = db.ReferenceProperty(reference_class=Quizz, collection_name="participations")
    started_at = db.DateTimeProperty(auto_now_add=True)
    finished_at = db.DateTimeProperty(auto_now=True)
    duration = db.IntegerProperty(default = 0)
    right_answers = db.IntegerProperty(default = 0)
    finished = db.BooleanProperty(default = False)

class QuestionParticipation(db.Model):
    question = db.ReferenceProperty(reference_class=Question, collection_name="participations")
    quizz_participation = db.ReferenceProperty(reference_class=QuizzParticipation, collection_name="questions")
    answer = db.IntegerProperty()
    right_answer = db.BooleanProperty(default = False)
    answered_at = db.DateTimeProperty(auto_now_add=True)
