import datetime as dt

DAYS = 30

cutoff = (dt.date.today() - dt.timedelta(days=DAYS)).strftime('%Y-%m-%d')
User.query.filter_by(date_added<=cutoff).delete()
db.session.commit()