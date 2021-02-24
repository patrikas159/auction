from .import db
import datetime
class Auction(db.Model):

    __tablename__ = "Auction"
    id = db.Column(db.Intager, primary_key=True)
    title = db.Column(db.VARCHAR(50), nullable=False)
    category = db.Column(db.VARCHAR(50), nullable=False)
    description = db.Column(db.VARCHAR(200), nullable=False)
    city = db.Column(db.VARCHAR(50), nullable=False)
    minimal_price = db.Column(db.Intager, nullable=False)
    image = db.Column(db.VARCHAR(256), nullable=False)
    end_day = db.Column(db.Date, default=datetime.datetime.now())
    end_hour = db.Column(db.Time, default=datetime.time())
    offer = db.relationship('Offer', backref='auction', lazy=True)
    views = db.Column(db.Intager, default=0)
    user_id = db.Column(db.Intager, db.ForeignKey('User.id'), nullable=False)

