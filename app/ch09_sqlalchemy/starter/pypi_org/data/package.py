import sqlalchemy as sa
import sqlalchemy.orm as orm
import datetime

from pypi_org.data.modelbase import SqlAlchemyBase
from pypi_org.data.releases import Release


class Package(SqlAlchemyBase):
    __tablename__ = "packages"

    id = sa.Column(sa.String, primary_key=True)
    created_date = sa.Column(sa.Date, default=datetime.datetime.now, index=True)
    summary = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.Text, nullable=True)
    home_page = sa.Column(sa.Text)
    docs_url = sa.Column(sa.Text)
    package_url = sa.Column(sa.Text)

    author_name = sa.Column(sa.String)
    author_email = sa.Column(sa.String, index=True)

    license = sa.Column(sa.String, index=True)
    #maintainers
    releases = orm.relationship("Release", order_by=[
        Release.major_ver,
        Release.minor_ver,
        Release.build_ver,
        ],
        back_populates="package")

    def __repr__(self):
        return f"<Package(id={self.id}, created_date={self.created_date})>"