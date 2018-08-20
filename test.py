import db_helper



def test_verify_get_user_data():

    expect = 'andy lai'

    result = db_helper.get_user_data()

    assert expect == result

def test_verify_create_user():

    expect = True
    result = db_helper.create_user()

    assert expect == result

def test_will_succeed():
	
	expect = 'andy lai'
	
	result = db_helper.get_user_data()
	
	assert expect == result
	
def test_verify_create_user():

    expect = True
    result = db_helper.create_user(usr)

    assert expect == result
	
def verify_milk_tea_order():

	expect = 'regular PMT'
	
	result = db_helper.get_milk_tea_order()
	
	assert expect == result
	
def get_wrong_PMT_order():

	expect = 'Earl Grey MT'
	
	result = db_helper.get_milk_tea_order()
	
	assert expect == result