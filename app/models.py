from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from . import db

class Leitura(db.Model):
    __tablename__ = 'leituras'

    id: Mapped[int] = mapped_column(primary_key=True)
    topico: Mapped[str] = mapped_column(db.String(256), nullable=False)
    valor: Mapped[str] = mapped_column(db.String(256))
    data_registro: Mapped[DateTime] = mapped_column(DateTime, nullable=False)

    def __repr__(self) -> str:
        return f'<Leitura {self.id}>'

