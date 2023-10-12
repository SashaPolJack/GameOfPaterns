from behave import *
import main

@Given('Отображаемое текущее кол-во очков')
def step_impl(context):
    main.ui.label_score.text()

@When('Мы вводим верный ответ и получаем очко')
def step_impl(context):
    main.ui.pushButton_input.click()
    assert  main.ui.find_answer(main.answers[main.ui.p - 1][1]) == True

@Then('Количество очков изменяется и корректно отображается в интерфейсе')
def step_impl(context):
    assert main.ui.label_score.text() == str(main.score)
