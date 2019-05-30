from pony.orm import db_session
from app import db
from models.Ad import Ad
from models.Medium import Medium
from models.Work import Work
from models.User import User, UserSchema
from datetime import datetime, timedelta

db.drop_all_tables(with_all_data=True)
db.create_tables()

with db_session():




    animation = Medium(name='Animation')
    music = Medium(name='Music')
    application = Medium(name='Application')
    picture = Medium(name='Picture')


    tom = User(
    username='Tom',
    email='Tomjhinton@gmail.com',
    password_hash=UserSchema().generate_hash('pass'),
    lookingforwork=True,
	photo="tom.png"
    )

    company = User(
    username='Company',
    email='Company@gmail.com',
    password_hash=UserSchema().generate_hash('pass'),
    lookingforwork=True,
    medium=animation,
	photo="tom.png"
    )





    Work(
        createdBy=tom,
        created="2018/07/02",
        name="Python pic 1",
        picture="https://66.media.tumblr.com/2e27aafca3635fc39ed986936b50379e/tumblr_ps9jc4j0UH1w3debko1_1280.png",
        description="Image distortion with Python",
        medium=picture
    )

    Work(
        createdBy=tom,
        created="2018/07/02",
        name="Python abstraction",
        iframe="link.co.uk",
        embed="link.png",
        picture="https://66.media.tumblr.com/0a30785b2846aea9bf3d535d80319a0c/tumblr_ps9jpbjEkG1w3debko1_1280.png",
        github="github link",
        code="heres some code",
        description="Made some stuff",
        medium=animation
    )

    Work(
        createdBy=tom,
        created="2018/07/02",
        name="work 2",
        iframe="link.co.uk",
        embed="link.png",
        picture="https://66.media.tumblr.com/0a30785b2846aea9bf3d535d80319a0c/tumblr_ps9jpbjEkG1w3debko1_1280.png",
        github="github link",
        code="heres some code",
        description="Made some stuff",
        medium=animation
    )


    Ad(
        name="Advertisement",
        createdBy=company,
        created="2018/07/02",
        description="Made some stuff",
        medium=animation
    )








    db.commit()
