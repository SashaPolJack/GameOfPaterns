import unittest
import main


class MyTestCase(unittest.TestCase):


    def test_click_button(self):
        main.ui.pushButton_input.click()
        assert type(main.ui.lineEdit_for_point.text().lower()) == str


    def test_image_validity(self):
        assert main.ui.label_for_img1.pixmap().toImage() == main.ui.pic.toImage()


    def test_picture_correct(self):
        assert main.image_in_class_work_image.size == main.ui.image_before.size