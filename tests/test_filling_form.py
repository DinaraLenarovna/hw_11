from modules.pages.registration_form_page import RegistrationPage
import allure

def test_filling_form():
    registration_page = RegistrationPage()
    with allure.step("Open registration form")
        registration_page.open()

    with allure.step("Fill <Name> field")
        registration_page.fill_first_name('Dinara')
    with allure.step("Fill <Lastname> field")
        registration_page.fill_last_name('Safina')
    with allure.step("Fill <Email> field")
        registration_page.fill_email('dinatest@bk.ru')
    with allure.step("Choose <Gender> radio-button")
        registration_page.choose_gender()
    with allure.step("Fill <Number> field")
        registration_page.fill_phone_number('9999999999')
    with allure.step("Choose Date of birth")
        registration_page.fill_date_of_birth('1999', 'April', '11')
    with allure.step("Fill <Subjects> field")
        registration_page.fill_subjects('Maths')
    with allure.step("Choose Hobbies checkbox")
        registration_page.fill_hobbies()
    with allure.step("Upload user photo")
        registration_page.upload_picture('test_image.jpg')
    with allure.step("Fill <Address> field")
        registration_page.fill_address('Russia, Ufa, Lenina St., 1')
    with allure.step("Choose State from list")
        registration_page.select_state('Haryana')
    with allure.step("Choose City from list")
        registration_page.select_city('Panipat')

    with allure.step("Submit form")
        registration_page.submit()

    with allure.step("Check form results")
        registration_page.assert_user_submitted_form('Dinara Safina', 'dinatest@bk.ru', 'Female', '9999999999', '11 April,1999', 'Maths', 'Sports, Reading',
        'test_image.jpg', 'Russia, Ufa, Lenina St., 1', 'Haryana Panipat')

