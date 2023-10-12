from behave import *
import main

@Given('Запущенный интерфейс')
def step_impl(context):
    main.ui.start_load()

@When('Отображается изображение с заданием')
def step_impl(context):
    assert main.ui.label_for_img1.pixmap().toImage() == main.ui.pic.toImage()

@Then('Корректное отображение заданного изображения')
def step_impl(context):
    assert main.image_in_class_work_image.size == main.ui.image_before.size

