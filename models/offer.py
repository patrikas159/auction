from . import db

class Offer(db.Model):

    __tablename__ = "Offer"
    id = db.Column(db.Intager, primary_key=True)
    auction_id = db.Column(db.Intager, db.ForeignKey('Auction.id'), nullable=False)
    user_id = db.Column(db.VARCHAR(50), nullable=False)
    price = db.Column(db.Intager, nullable=False)