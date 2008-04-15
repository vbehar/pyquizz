#!/usr/bin/env python

from google.appengine.ext import db

class Quizz(db.Model):
    # key name = quizz short_name (unique)
    short_name = db.StringProperty()
    full_name = db.StringProperty()
    description = db.TextProperty()
    lang = db.TextProperty()
    public = db.BooleanProperty(default = True)
    active = db.BooleanProperty(default = False)
    password_participation = db.StringProperty()
    password_results = db.StringProperty()
    password_admin = db.StringProperty()
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)

class Question(db.Model):
    quizz = db.ReferenceProperty(reference_class=Quizz, collection_name="questions")
    id = db.IntegerProperty()
    question = db.StringProperty()
    items = db.StringListProperty()
    answer = db.IntegerProperty()
    more_infos = db.StringProperty()
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)

class User(db.Model):
    # key name = uuid - stored in a cookie (unique)
    uuid = db.StringProperty()
    name = db.StringProperty
    lang = db.TextProperty()
    quizz = db.ReferenceProperty(reference_class=Quizz, collection_name="users")
    has_participation_access = db.BooleanProperty(default = False)
    has_results_access = db.BooleanProperty(default = False)
    has_admin_access = db.BooleanProperty(default = False)
    started_at = db.DateTimeProperty(auto_now_add=True)
    finished_at = db.DateTimeProperty(auto_now=True)
    duration = db.IntegerProperty(default = 0)
    right_answers = db.IntegerProperty(default = 0)
    finished = db.BooleanProperty(default = False)
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)

class UserAnswer(db.Model):
    question = db.ReferenceProperty(reference_class=Question, collection_name="users_answers")
    user = db.ReferenceProperty(reference_class=User, collection_name="quizz_answers")
    answer = db.IntegerProperty()
    right_answer = db.BooleanProperty(default = False)
    time_to_answer = db.IntegerProperty(default = 0)
    answered_at = db.DateTimeProperty(auto_now_add=True)


class Tag(db.Model):
    # key name = tag name (unique)
    name = db.StringProperty()
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)

class Tagging(db.Model):
    tag = db.ReferenceProperty(reference_class=Tag, collection_name="taggings")
    quizz = db.ReferenceProperty(reference_class=Quizz, collection_name="taggings")
    tagged_at = db.DateTimeProperty(auto_now_add=True)
