

def test_new_admin(admin):
    assert not admin.is_user
    assert admin.is_admin == True
    assert admin.is_company == False
    assert admin.id == 1
    assert admin.check_password('123456')
    assert admin.username == 'admin'

def test_new_user(user):
    assert user.is_user == True
    assert user.is_admin == False
    assert user.is_company == False
    assert user.id == 2
    assert user.check_password('123456')
    assert user.username == 'user'

def test_new_company(company):
    assert company.is_user == False
    assert company.is_admin == False
    assert company.is_company == True
    assert company.id == 3
    assert company.check_password('123456')
    assert company.username == 'company'

def test_job(job):
    assert job.id == 1
    assert job.tags[-1] != ','
    assert '/' not in job.name

def test_delivery(delivery):
    assert delivery.id == 1
    assert delivery.job_id == 1
    assert delivery.user_id == 2
    assert delivery.company_id == 1

def test_company(cp):
    assert ',' not in cp.tag_list
    assert 'http' not in cp.web
    assert len(cp.detail)
