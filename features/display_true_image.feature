Feature: Отображение изображения в интерфейсе

  Scenario: Корректное отображение картинки с заданием в интерфейсе
    Given Запущенный интерфейс
    When Отображается изображение с заданием
    Then Корректное отображение заданного изображения

