from jobplus.app import create_app
from jobplus.models import User, Job, Delivery, Company, db
from faker import Faker
import random
import pytest
import os
import  json
faker = Faker('zh-CN')

@pytest.fixture(scope='module')
def admin():
    return User(
            id = 1,
            name = 'admin',
            username = 'admin',
            email = 'admin@qq.com',
            role = 30,
            phonenumber = faker.phone_number(),
            password = "123456",

            )
@pytest.fixture(scope='module')
def user():
    return User(
            id = 2,
            name = 'user',
            username = 'user',
            email = 'user@qq.com',
            role = 10,
            phonenumber = faker.phone_number(),
            password = "123456",
            )
@pytest.fixture(scope='module')
def company():
    return User(
            id = 3,
            name = 'company',
            username = 'company',
            email = 'company@qq.com',
            role = 20,
            phonenumber = faker.phone_number(),
            password = "123456",
            )

@pytest.fixture(scope='module')
def job():
            de = ['大专以上','本科以上','硕士以上']
            ex = ['1年以上','1-3年','3-5年','无经验',]
            lo = [2000,3000,5000,6000]
            hi = [7000,8000,9000,10000]


            return   Job(
                        id = 1,
                        jobname=faker.job(),

                        description=faker.sentence(),
                        experience_requirement = random.choice(ex),
                        degree_requirement = random.choice(de),
                        lowest_salary = random.choice(lo),
                        highest_salary =random.choice(hi),
                        location = faker.province(),
                        job_label = faker.word() + ' ' + faker.word() + ' ' + faker.word(),
                        )


@pytest.fixture(scope='module')
def cp():
    with open(os.path.join(os.path.dirname(__file__), '..', "jobplus",'data', 'data.json')) as f:

        dics = json.load(f)

    for i in dics:
        return Company( id = 1,
                        url = i['url'],
                        logo = "https:"+i['logo'],
                        about = i['about'],
                        description = i['description'],
                        location = i['location'],
                        tags = i['tags'],
                        user_id = 3,
                        c_email = faker.email(),
                        phone = faker.phone_number()
                    )


@pytest.fixture(scope='module')
def delivery():
    return Delivery(
    id = 1,
    job_id = 1,
    user_id = 2,
    company_id = 1)

@pytest.fixture(scope='module')
def client():
    app =  create_app('testing')
    client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    yield client
    ctx.pop()

@pytest.fixture(scope='module')
def init_database(user,admin, company, cp, job, delivery):
    # Create the database and the database table

    db.create_all()
    # Insert user data
    print(User.query.get(1))
    if not User.query.get(1):

        db.session.add(user)
        db.session.add(admin)
        db.session.add(company)
        job.company_id = 1
        db.session.add(job)
        cp.user_id = 3

        db.session.add(cp)
        delivery.user_id = 3
        delivery.company_id = 1
        delivery.job_id = 1
        db.session.add(delivery)


        # Commit the changes for the users
        db.session.commit()

    yield db  # this is where the testing happens!
