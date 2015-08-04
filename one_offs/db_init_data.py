"""
JUST A SAMPLE SCRIPT.
NEEDS TO BE MODIFIED FOR YOUR PARTICULAR DB/MODEL STRUCTURE.
"""

from app import app
from app.db_models import db # RELEVANT TABLES, Centre, Member


def init_data():
    'Centres first, Administrators second'
    if db.session.query(Centre).count() == 0:
        nowhere = Centre(name="nowhere", addr="nowhere", appr=True)
        db.session.add(nowhere)
    if db.session.query(Member).count() == 0:
        donal = Member(first='donal', surnm='carville', email='d@gmail.com',
                       password='dash', sttr=False, appr=True, adminr=True, staff_at=1)
        matt = Member(first='matt', surnm='sheridan', email='m@gmail.com',
                      password='mash', sttr=True, appr=True, adminr=True, staff_at=1)
        db.session.add_all([donal, matt])
    db.session.commit()


if __name__ == '__main__':
    init_data()
