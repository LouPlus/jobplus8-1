<<<<<<< HEAD
import  json
from ..models import Job, Company, User, db, Delivery
from faker import Faker
import os
import random

faker = Faker("zh_CN")
class Data:
    def __init__(self):
        self.f_company = 0
        self.f_name = 0

    @property
    def user(self):
        return  User(name = faker.name(),
                username = self.f_name,
                email = faker.email(),
                role = 20,
                phonenumber = faker.phone_number(),
                password = "123456",
                companys = self.f_company
                )

    @property
    def companys(self):
        with open(os.path.join(os.path.dirname(__file__), '..', 'data', 'data.json')) as f:
            dics = json.load(f)

        for i in dics:
            self.f_name = i['name']
            yield Company(  url = i['url'],
                            logo = "https:"+i['logo'],
                            about = i['about'],
                            description = i['description'],
                            location = i['location'],
                            tags = i['tags'],
                            c_email = faker.email(),
                            phone = faker.phone_number()
                        )

    @property
    def jobs(self):
        de = ['大专以上','本科以上','硕士以上']
        ex = ['1年以上','1-3年','3-5年','无经验',]
        lo = [2000,3000,5000,6000]
        hi = [7000,8000,9000,10000]


        return   Job(jobname=faker.job(),
                    description=faker.sentence(),
                    experience_requirement = random.choice(ex),
                    degree_requirement = random.choice(de),
                    lowest_salary = random.choice(lo),
                    highest_salary =random.choice(hi),
                    location = faker.province(),
                    job_label = faker.word() + ' ' + faker.word() + ' ' + faker.word(),
                    company = self.f_company
                    )

    def delivery(self, job_id ,user_id):
        company_id = Job.query.filter_by(id = job_id).first().company.id
        return Delivery(job_id = job_id,
        user_id = user_id,
        company_id = company_id

        )

    @property
    def add_data(self):
        for company in self.companys:
            db.session.add(company)
            try:
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.rollback()


            self.f_company = Company.query.filter_by(id = company.id).first()


            user = self.user
            db.session.add(user)
            try:
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.rollback()


            for i in range(10):
                job = self.jobs
                db.session.add(job)

                try:
                    db.session.commit()
                except Exception as e:
                    print(e)
                    db.session.rollback()

        #add admin
        user =  User(name = faker.name(),
                username = 'admin',
                email = 'admin@qq.com',
                role = 30,
                phonenumber = faker.phone_number(),
                password = "123456"
                )

        db.session.add(user)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

        #add user
        user =  User(name = faker.name(),
                username = 'user',
                email = 'user@qq.com',
                role = 10,
                phonenumber = faker.phone_number(),
                password = "123456"
                )

        db.session.add(user)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

        #add delivery
        user = User.query.filter_by(username = 'user').first()
        for job_id in range(2,100):
            delivery = self.delivery(job_id, user.id)
            db.session.add(delivery)
            db.session.commit()


def run():
    Data().add_data
=======
from json
from ..models import Job, Company
from faker import Faker


with open('/jobplus/data/data.json') as f:
    dic = json.load(f)

<<<<<<< HEAD
print(dic) 
>>>>>>> 1
=======
print(dic)
>>>>>>> 1
