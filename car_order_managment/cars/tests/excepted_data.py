test_data = {
    "colors": {
        "data": [
            {
                "name": "Purple"
            },
            {
                "name": "Blue"
            },
            {
                "name": "Red"
            },
            {
                "name": "Green"
            },
            {
                "name": "Yellow"
            },
            {
                "name": "Black"
            },
            {
                "name": "White"
            },
            {
                "name": "Gray"
            }
        ],
        'bad': {
            'already': {
                "name": [
                    "Цвет with this Цвет автомобиля already exists."
                ]
            },
            'blank': {
                "name": [
                    "This field may not be blank."
                ]
            },
            '404': {
                "detail": "Not found."
            }
        },
    },

    "brands": {
        "data": [
            {
                "name": "BMW"
            },
            {
                "name": "LADA"
            },
            {
                "name": "Geely"
            },
            {
                "name": "Toyota"
            },
            {
                "name": "Opel"
            },
            {
                "name": "Renault"
            },
            {
                "name": "Citroen"
            }
        ],
        'bad': {
            'already': {
                "name": [
                    "Марка with this Марка автомобиля already exists."
                ]
            },
            'blank': {
                "name": [
                    "This field may not be blank."
                ]
            },
            '404': {
                "detail": "Not found."
            }
        },
    },

    "models": {
        "data": [
            {
                "name": "M5"
            },
            {
                "name": "Vesta"
            },
            {
                "name": "X-Ray"
            },
            {
                "name": "X3"
            },
            {
                "name": "2106"
            },
            {
                "name": "Niva"
            },
            {
                "name": "M1"
            }
        ],
        'bad': {
            'already': {
                "name": [
                    "Модель with this Модель автомобиля already exists."
                ]
            },
            'required': {
                "name": [
                    "This field may not be blank."
                ],
                "car_brand": [
                    "This field is required."
                ]
            },
            'blank': {
                "name": [
                    "This field may not be blank."
                ]
            },
            '404': {
                "detail": "Not found."
            }
        },
    },

    "orders": {

    }
}
