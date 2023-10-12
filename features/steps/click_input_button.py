from behave import *
import main

@Given('Введенный текст и кнопка подтверждения ответа')
def step_impl(context):
    main.ui.find_answer(main.answers[main.ui.p - 1][1])
    assert main.ui.pushButton_input.isEnabled() == True

@When('Нажимаем на кнопку ввода')
def step_impl(context):
    main.ui.pushButton_input.click()

@Then('Корректное считывание ответа')
def step_impl(context):
    assert type(main.ui.lineEdit_for_point.text().lower()) == str

