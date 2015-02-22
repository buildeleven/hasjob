# -*- coding: utf-8 -*-

from datetime import datetime
from . import db
from .user import User
from .jobpost import JobPost
from .reportcode import ReportCode

__all__ = ['JobPostReport']


# No BaseMixin here because this is a legacy class (datetime serves the purpose of created_at and updated_at)
class JobPostReport(db.Model):
    __tablename__ = 'jobpostreport'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(None, db.ForeignKey('user.id'), nullable=True)
    user = db.relationship(User)
    datetime = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('jobpost.id'), nullable=False)
    post = db.relation(JobPost, primaryjoin=post_id == JobPost.id,
        backref=db.backref('flags', cascade='all, delete-orphan'))
    reportcode_id = db.Column(db.Integer, db.ForeignKey('reportcode.id'), nullable=False)
    reportcode = db.relation(ReportCode, primaryjoin=reportcode_id == ReportCode.id)
    report_code = db.synonym('reportcode_id')

    ipaddr = db.Column(db.String(45), nullable=False)
    useragent = db.Column(db.Unicode(250), nullable=True)
