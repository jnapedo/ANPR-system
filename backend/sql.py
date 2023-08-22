
sql= """
    CREATE TABLE IF NOT EXISTS tb_cars(
        generated_id INTEGER PRIMARY KEY AUTOINCREMENT,
        number_plate varchar(15) NOT NULL UNIQUE,
        car_model varchar(20)  NOT NULL,
        car_color varchar(20)  NOT NULL,
        car_number INTEGER  NOT NULL UNIQUE,
        )
    """
    