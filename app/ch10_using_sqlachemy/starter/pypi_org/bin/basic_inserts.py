import os
import pypi_org
from pypi_org.data import db_session
import sqlalchemy.orm as orm

from pypi_org.data.package import Package
from pypi_org.data.releases import Release


def insert_a_package():
    p = Package()
    p.id = input('Package id / name: ').strip().lower()
    p.summary = input('Package summary: ').strip()
    p.author = input('Package author: ').strip()
    p.license = input('License: ').strip()

    print("Release 1")
    r = Release()
    r.major_ver = int(input('Major version: ').strip())
    r.minor_ver = int(input('Minor version: ').strip())
    r.build_ver = int(input('Build version: ').strip())
    r.size = int(input('Size in bytes: ').strip())
    p.releases.append(r)

    print("Release 2")
    r = Release()
    r.major_ver = int(input('Major version: ').strip())
    r.minor_ver = int(input('Minor version: ').strip())
    r.build_ver = int(input('Build version: ').strip())
    r.size = int(input('Size in bytes: ').strip())
    p.releases.append(r)


    session = db_session.create_session()
    session.add(p)
    session.commit()

def main():
    init_db()
    while True:
        insert_a_package()

def init_db():
    top_folder = os.path.dirname(__file__)
    rel_file = os.path.join('..','db', 'pypi.sqlite')
    db_file = os.path.join(top_folder, rel_file)
    db_session.global_init(db_file)


if __name__ == '__main__':
    main()