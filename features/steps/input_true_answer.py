from behave import *
import main

@Given('Пустое поле ввода и картинка с заданием')
def step_impl(context):
    assert main.ui.lineEdit_for_point.isEnabled() == True
    assert main.ui.label_for_img1.isEnabled() == True

@When('Вводим верный ответ в поле ввода и нажимаем "Отправить"')
def step_impl(context):
    assert main.ui.find_answer(main.answers[main.ui.p - 1][1]) == True
    main.ui.pushButton_input.click()

@Then('Счет увеличивается и отображается корректно')
def step_impl(context):
    assert main.ui.label_score.text() == str(main.score)



