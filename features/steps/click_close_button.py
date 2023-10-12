from behave import *
import main

@Given('Активная кнопка "Закончить"')
def step_impl(context):
    assert main.ui.pushButton_cancel.isEnabled() == True

@When('Нажата кнопка закончить')
def step_impl(context):
    main.ui.pushButton_cancel.click()

@Then('Появление виджета с выбором завершить или остаться')
def step_impl(context):
    assert main.ui.reply


