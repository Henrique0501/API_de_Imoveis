from app.database import db
from app import ma
from sqlalchemy import true


class Imovel(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    place = db.Column(db.String(255), nullable=False)
    area = db.Column(db.Integer, nullable=False)
    rooms = db.Column(db.Integer, nullable=False)
    garages = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    @classmethod
    def all_or_equal(cls, attribute, value):
        return true() if not value else attribute == value

    @classmethod
    def all_or_bigger(cls, attribute, value):
        return true() if not value else attribute > value

    @classmethod
    def all_or_smaller(cls, attribute, value):
        return true() if not value else attribute < value


class ImovelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Imovel
        sqla_session = db.session
        load_instance = True
