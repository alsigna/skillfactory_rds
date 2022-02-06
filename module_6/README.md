# Прогнозирование стоимости автомобиля по характеристикам

Проект по предсказанию стоимости авто.

Auto.ru парсить свежие данные не дает, поэтому для работы был взять с Kaggle, подготовленный другим участником. В итоге использовалось два датасета:
- [Датасет с Kaggle за 2021 год](https://storage.googleapis.com/kaggle-data-sets/1622945/2667549/compressed/train_df_full_part1.csv.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20220206%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20220206T124443Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=22bca7c3cf611e39d1fdec23965ee2c38dbda5ae8756aac8f9ff369027d6c7b93cc5583b0a129e8de121ce5182e0d9a8aa0c6dc4359614a32671ea625c28fa8545625f3a6607b94d481b6fcb284aa32801d229c843861823a95321a47150976fdb1dc90ca28cc07ec07a7768fc1f183d94e811ac2a9c3ed1cc4c6b24f8f1b22f90086495c103d3b7bc5cfca15f37cbbc49fc8a2d2140c9466cb9c16e1a43f9713e284fcc244b75130d52ecb8c7ec9248bb0722b49f65bfdb060c18fcc47076558d775c56cd7eab493c16496ea9dbf50075db9bf4faf2faa68a68ed4c96c608531158c59d34a926cf016d029ad667ed61b1b71504183360b27ed532513828c359)
- [Датасет из BaseLine](https://storage.googleapis.com/kaggle-data-sets/879145/1496740/compressed/all_auto_ru_09_09_2020.csv.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20220206%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20220206T124525Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=4de768257ab56a349235cd7d24c34eea8f8ea75e5116d98850ab1c8b53cbbad5663792ccba9481b13118e6f6cfa7cc97cc67b7ec52d27d80333c8ddeac22c8ae3223c2d28ccfcca013cae8689b01bad357236ff0b7728eff2fbbc6dd63d9d3fbae5a7b5900af7edf866797fd5f4a92e9b58a25cc8b36b0f7e2a8d59764bb60f52dd8e9c027de969cb7b004adee5d6e9caf049eef61b4fe1dd756bd0e1ce8341e85785221a8f1f2966b588aa4a4d46a5eebfe2b7fcdc5ac046436ce7e4b0e4cd1fb0e91a62f9522228acd790d78e083c54e82aa146fa91d9e04ddb025e856aee6ce266f48a8102d1859140ec19001e51d4a7caead2f4ef4c4d4e90399905ce3d2)

Для обзора данных применялась библиотека pandas_profiling, отчет загружен на github [PandasProfile](https://github.com/alsigna/skillfactory_rds/blob/1b56a4112b6f92b0a24ddbfe69eea1173813f33e/module_6/car_price_prediction.html)


# Выводы
- лучшая МАРЕ (7.23) получилась на StackingRegressor (RandomForest + ExtraTrees + XGBRegressor), но при этом на Kaggle результат далеко нне лучший.
- есть ситуации, когда МАРЕ получается хорошая, но на Kaggle результат очень плохой. Возможно модель переобучается.
- править цену свежих датасетов нужно более "ителлектуально", чем просто умножить все на X.
- во всех случаях AbaBoost давал лучший результат, но время на обучение модели при этом увеличивается на порядок.
- наиболее оптимальный выбор, с моей точки зрения, это StackingRegressor, приемлемый результат и не нужнно ждать часы на обученине.
- ресурсов на GridSearchCV точно не хватает, RandomSearchCV работает через раз, ядро часто падает из-за нехватки памяти.
- лучший результат на Kaggle 10.52269, был получен с AdaBoost (RandomForest), но ячейка с параметрами была случайно удалена, следующиий результат 10.53045 так же получен с AdaBoost (RandomForest)

# Нериализованные идеи
- в выборке (тестовой и из baseline) присутсвуют раритные и просто старые авто, цена на которые может быть сильно зависеть от конкретной ситуации и не поддаваться прогнозу в принципе. Хотел выделить хотя бы раритетные авто в отдельнный датасет, что бы они не были выбросами, и делать прогнозы отдельно, затем склеивать.
- более интелектуально парсить описание, например с целью понять комплектацию или битое/нет авто, просто подсчет числа слов мало что может дать.