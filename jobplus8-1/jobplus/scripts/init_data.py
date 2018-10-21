from json
from ..models import Job, Company
from faker import Faker


with open('/jobplus/data/data.json') as f:
    dic = json.load(f)

print(dic)
