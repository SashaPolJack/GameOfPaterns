from behave import *
import main

@Given('Пустое поле ввода и картинка с заданием 2')
def step_impl(context):
    assert main.ui.lineEdit_for_point.isEnabled() == True
    assert main.ui.label_for_img1.isEnabled() == True

@When('Вводим неверный ответ в поле ввода и нажимаем "Отправить"')
def step_impl(context):
    assert main.ui.find_answer("test") == False
    main.ui.pushButton_input.click()

@Then('Счет остается прежним')
def step_impl(context):
    assert main.ui.label_score.text() == str(main.score)

