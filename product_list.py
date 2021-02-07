# this houses the items of the supermarket
class Fruits:
    global fruits_dict

    fruits_dict = {"APPLE (1KG)": 90,
                   "WATERMELON (1N)": 40,
                   "MELON (1N)": 60,
                   "ORANGE (1KG)": 40,
                   "PEAR (1KG)": 100,
                   "MANGO (1KG)": 85,
                   "GRAPE (1KG)": 40,
                   "PEACH (1KG)": 80,
                   "PINEAPPLE (1N)": 30,
                   "PAPAYA (1N)": 50}

    def add_item(name: str, num: int):
        fruits_dict[name] = num

    def print_items():
        count = 1
        for keys in fruits_dict:
            print(f"<{count}>{keys}: Rs.{fruits_dict[keys]}/-")
            count += 1
        print()

    def print_category():
        print("FRUITS")


class Vegetables:
    global veg_dict

    veg_dict = {"POTATO (1KG)": 20,
                "ONION (1KG)": 40,
                "TOMATO (1KG)": 15,
                "CAULIFLOWER (1N)": 25,
                "CABBAGE (1N)": 25,
                "BOTTLE GOURD (1N)": 40,
                "PUMPKIN (500G)": 20,
                "BRINJAL (1KG)": 50,
                "OKRA (1KG)": 50,
                "PEAS (1KG)": 40,
                "CARROT (500G)": 15,
                "RADISH (500G)": 15,
                "GREEN CHILLI (250G)": 20,
                "CILANTRO (1N)": 5,
                "SPINACH (1N)": 30}

    def add_item(name: str, num: int):
        veg_dict[name] = num

    def print_items():
        count = 101
        for keys in veg_dict:
            print(f"<{count}>{keys}: Rs.{veg_dict[keys]}/-")
            count += 1
        print()

    def print_category():
        print("VEGETABLES")


class Dairy:
    global dairy_dict

    dairy_dict = {"MILK (500ML)": 25,
                  "TONED MILK (500ML)": 30,
                  "CHEESE (250G)": 50,
                  "PANEER (250G)": 80,
                  "EGGS (12N)": 60,
                  "BREAD (1N)": 35}

    def add_item(name: str, num: int):
        dairy_dict[name] = num

    def print_items():
        count = 201
        for keys in dairy_dict:
            print(f"<{count}>{keys}: Rs.{dairy_dict[keys]}/-")
            count += 1
        print()

    def print_category():
        print("DAIRY PRODUCTS, EGGS AND BREAD")


class Groceries:
    global grocery_dict

    grocery_dict = {
        # flour
        "WHEAT FLOUR (5KG)": 100,
        "REFINED WHEAT FLOUR (1KG)": 30,
        "BESAN (1KG)": 80,
        "SEMOLINA (1KG)": 40,
        "CORN FLOUR (500G)": 55,
        "RICE (5KG)": 120,
        "SOYA CHUNKS (500G)": 80,
        "SABUDANA (500G)": 55,
        "POHA (500G)": 60,
        # spices
        "CORIANDER (100G)": 35,
        "TURMERIC (100G)": 35,
        "RED CHILLI (100G)": 40,
        "GARAM MASALA (100G)": 35,
        "ROSEMARY (100G)": 60,
        "PARSLEY (100G)": 35,
        "CHILLI FLAKES (100G)": 40,
        "OREGANO (100G)": 300,
        "THYME (100G)": 40,
        "MINT (100G)": 40,
        "SAFFRON (1G)": 200,
        # salts and sugar
        "SUGAR (5KG)": 550,
        "JAGGERY (1KG)": 80,
        "SALT (1KG)": 20,
        "ROCK SALT (1KG)": 190,
        # oils and ghee
        "REFINED SUNFLOWER OIL (1L)": 230,
        "REFINED MUSTARD OIL (1L)": 190,
        "COW GHEE (1L)": 600,
        "OLIVE OIL (1L)": 300,
        "EXTRA VIRGIN OLIVE OIL (1L)": 700,
        # sauces and jams
        "MIXED FRUIT JAM (1KG)": 250,
        "TOMATO SAUCE (1KG)": 90,
        "RED CHILLI SAUCE (200G)": 50,
        # dry fruits
        "ALMONDS (1KG)": 750,
        "CASHEWS (1KG)": 950,
        "RAISINS (1KG)": 980,
        "PISTACHIOS (1KG)": 1250,
        "WALNUTS (1KG)": 625
    }

    def add_item(name: str, num: int):
        grocery_dict[name] = num

    def print_items():
        count = 301
        for keys in grocery_dict:
            print(f"<{count}>{keys}: Rs.{grocery_dict[keys]}/-")
            count += 1
        print()

    def print_category():
        print("GROCERIES")


class PersonalCare:
    global pc_dict

    pc_dict = {
        # face
        "MOISTURISER (200ML)": 200,
        "NIGHT CREAM (50G)": 100,
        "TALCUM POWDER (100G)": 150,
        "ANTI ACNE FACE WASH (200ML)": 400,
        "APPLE CIDER FACE WASH (200ML)": 450,
        # shampoo and conditioner
        "ANTI-DANDRUFF SHAMPOO (200ML)": 200,
        "TOTAL REPAIR SHAMPOO (200ML)": 250,
        "CONDITIONER (100ML)": 175,
        # body wash
        "BODY WASH (200ML)": 250,
        # hair care
        "ALMOND HAIR OIL (250ML)": 100,
        "AMLA HAIR OIL (250ML)": 50,
        "HAIR GEL (50ML)": 80,
        "SHAVING CREAME (100ML)": 100,
        "SHAVING FOAM (500ML)": 350,
        "AFTERSHAVE LOTION (100ML)": 125,
        # soaps
        "CINTHOL (1N)": 20,
        "CINTHOL (PACK OF 4)": 70,
        "VIVEL (1N)": 30,
        "VIVEL (PACK OF 2)": 50,
        "DETTOL (1N)": 20,
        "DETTOL (PACK OF 4)": 70,
        "HANDWASH (250ML)": 70,
        "HANDWASH (1L MEGA PACK)": 200
    }

    def add_item(name: str, num: int):
        pc_dict[name] = num

    def print_items():
        count = 401
        for keys in pc_dict:
            print(f"<{count}>{keys}: Rs.{pc_dict[keys]}/-")
            count += 1
        print()

    def print_category():
        print("PERSONAL CARE")


class HomeNeeds:
    global hn_dict

    hn_dict = {
        # cleaning
        "FLOOR CLEANER (1L)": 100,
        "TOILET CLEANER (500ML)": 45,
        "ROOM FRESHNER (500ML)": 350,
        "DISH WASHING LIQUID (200ML)": 100,
        "DISH SCRUB (1N)": 20,
        "PLASTIC BUCKET (20L)": 50,
        "BROOM (1N)": 30,
        "MOP (5INx5IN)": 40,
        "DUSTING CLOTH (5INx5IN)": 40,
        "DUSTBIN (10L)": 45,
        "DUSTER (1N)": 25,
        "FLOOR WIPER (1N)": 200,
        "PLATFORM WIPER (1N)": 80,
        "HAND TOWEL (1N)": 50,
        "BATH TOWEL (1N)": 80,
        "MOSQUITO REPELLENT (100ML)": 100,
        # bottles and glasses
        "PLASTIC BOTTLES (PACK OF 4)": 100,
        "METAL BOTTLE (1N)": 200,
        "GLASS BOTTLES (PACK OF 2)": 150,
        "DISPOSABLE GLASSES (25N)": 25,
        "GLASSES (4N)": 300,
        "METAL GLASSES (4N)": 200,
        # pillows and blankets
        "CUSHIONS (2N)": 150,
        "BED PILLOW (1N)": 200,
        "JUMBO PILLOW (1N)": 300,
        "CUSHION COVERS (2N)": 50,
        "PILLOW COVER (1N)": 80,
        "JUMBO PILLOW COVER (1N)": 100,
    }

    def add_item(name: str, num: int):
        hn_dict[name] = num

    def print_items():
        count = 501
        for keys in hn_dict:
            print(f"<{count}>{keys}: Rs.{hn_dict[keys]}/-")
            count += 1
        print()

    def print_category():
        print("HOME NEEDS")


class Stationery:
    global st_dict

    st_dict = {
        # pens and pencils
        "BALL PENS (3N)": 10,
        "GEL PENS (1N)": 10,
        "PREMIUM GEL PEN (1N)": 40,
        "PREMIUM BALL PEN (1N)": 125,
        "HB PENCILS (PACK OF 1O)": 40,
        "EXTRA DARK PENCILS (PACK OF 10)": 50,
        "ERASER (1N)": 5,
        "JUMBO ERASER (1N)": 10,
        "SHARPENER (1N)": 5,
        "2 IN 1 ERASER SHARPENER (1N)": 20,
        "SCALE (15CM)": 10,
        "SCALE (30CM)": 25,
        # notebooks
        "SMALL NOTEBOOK (120PG)": 25,
        "SMALL NOTEBOOK THICK (240PG)": 45,
        "BIG NOTEBOOK (120PG)": 40,
        "BIG NOTEBOOK THICK (240PG)": 75,
        "REGISTER (200PG)": 50,
        "THICK REGISTER (400PG)": 100,
        "SKETCHBOOK A4": 100,
        "SKETCHBOOK A3": 150,
        "SCRAP BOOK (50PG)": 70,
        # art
        "COLOUR PENCILS (10N)": 50,
        "CRAYONS (10N)": 50,
        "GLITTER PENS (10N)": 50,
        "COLOURED PAPERS (50N)": 60
    }

    def add_item(name: str, num: int):
        st_dict[name] = num

    def print_items():
        count = 601
        for keys in st_dict:
            print(f"<{count}>{keys}: Rs.{st_dict[keys]}/-")
            count += 1
        print()

    def print_category():
        print("STATIONERY ITEMS")


class Supermarket:
    global item_dict

    item_dict = {
        "APPLE (1KG)": 1,
        "WATERMELON (1N)": 2,
        "MELON (1N)": 3,
        "ORANGE (1KG)": 4,
        "PEAR (1KG)": 5,
        "MANGO (1KG)": 6,
        "GRAPE (1KG)": 7,
        "PEACH (1KG)": 8,
        "PINEAPPLE (1N)": 9,
        "PAPAYA (1N)": 10,
        # Vegetables
        "POTATO (1KG)": 101,
        "ONION (1KG)": 102,
        "TOMATO (1KG)": 103,
        "CAULIFLOWER (1N)": 104,
        "CABBAGE (1N)": 105,
        "BOTTLE GOURD (1N)": 106,
        "PUMPKIN (500G)": 107,
        "BRINJAL (1KG)": 108,
        "OKRA (1KG)": 109,
        "PEAS (1KG)": 110,
        "CARROT (500G)": 111,
        "RADISH (500G)": 112,
        "GREEN CHILLI (250G)": 113,
        "CILANTRO (1N)": 114,
        "SPINACH (1N)": 115,
        # Dairy
        "MILK (500ML)": 201,
        "TONED MILK (500ML)": 202,
        "CHEESE (250G)": 203,
        "PANEER (250G)": 204,
        "EGGS (12N)": 205,
        "BREAD (1N)": 206,
        # Groceries
        "WHEAT FLOUR (5KG)": 301,
        "REFINED WHEAT FLOUR (1KG)": 302,
        "BESAN (1KG)": 303,
        "SEMOLINA (1KG)": 304,
        "CORN FLOUR (500G)": 305,
        "RICE (5KG)": 306,
        "SOYA CHUNKS (500G)": 307,
        "SABUDANA (500G)": 308,
        "POHA (500G)": 309,
        "CORIANDER (100G)": 310,
        "TURMERIC (100G)": 311,
        "RED CHILLI (100G)": 312,
        "GARAM MASALA (100G)": 313,
        "ROSEMARY (100G)": 314,
        "PARSLEY (100G)": 315,
        "CHILLI FLAKES (100G)": 316,
        "OREGANO (100G)": 317,
        "THYME (100G)": 318,
        "MINT (100G)": 319,
        "SAFFRON (1G)": 320,
        "SUGAR (5KG)": 321,
        "JAGGERY (1KG)": 322,
        "SALT (1KG)": 323,
        "ROCK SALT (1KG)": 324,
        "REFINED SUNFLOWER OIL (1L)": 325,
        "REFINED MUSTARD OIL (1L)": 326,
        "COW GHEE (1L)": 327,
        "OLIVE OIL (1L)": 328,
        "EXTRA VIRGIN OLIVE OIL (1L)": 329,
        "MIXED FRUIT JAM (1KG)": 330,
        "TOMATO SAUCE (1KG)": 331,
        "RED CHILLI SAUCE (200G)": 332,
        "ALMONDS (1KG)": 333,
        "CASHEWS (1KG)": 334,
        "RAISINS (1KG)": 335,
        "PISTACHIOS (1KG)": 336,
        "WALNUTS (1KG)": 337,
        # PersonalCare
        "MOISTURISER (200ML)": 401,
        "NIGHT CREAM (50G)": 402,
        "TALCUM POWDER (100G)": 403,
        "ANTI ACNE FACE WASH (200ML)": 404,
        "APPLE CIDER FACE WASH (200ML)": 405,
        "ANTI-DANDRUFF SHAMPOO (200ML)": 406,
        "TOTAL REPAIR SHAMPOO (200ML)": 407,
        "CONDITIONER (100ML)": 408,
        "BODY WASH (200ML)": 409,
        "ALMOND HAIR OIL (250ML)": 410,
        "AMLA HAIR OIL (250ML)": 411,
        "HAIR GEL (50ML)": 412,
        "SHAVING CREAME (100ML)": 413,
        "SHAVING FOAM (500ML)": 414,
        "AFTERSHAVE LOTION (100ML)": 415,
        "CINTHOL (1N)": 416,
        "CINTHOL (PACK OF 4)": 417,
        "VIVEL (1N)": 418,
        "VIVEL (PACK OF 2)": 419,
        "DETTOL (1N)": 420,
        "DETTOL (PACK OF 4)": 421,
        "HANDWASH (250ML)": 422,
        "HANDWASH (1L MEGA PACK)": 423,
        # HomeNeeds
        "FLOOR CLEANER (1L)": 501,
        "TOILET CLEANER (500ML)": 502,
        "ROOM FRESHNER (500ML)": 503,
        "DISH WASHING LIQUID (200ML)": 504,
        "DISH SCRUB (1N)": 505,
        "PLASTIC BUCKET (20L)": 506,
        "BROOM (1N)": 507,
        "MOP (5INx5IN)": 508,
        "DUSTING CLOTH (5INx5IN)": 509,
        "DUSTBIN (10L)": 510,
        "DUSTER (1N)": 511,
        "FLOOR WIPER (1N)": 512,
        "PLATFORM WIPER (1N)": 513,
        "HAND TOWEL (1N)": 514,
        "BATH TOWEL (1N)": 515,
        "MOSQUITO REPELLENT (100ML)": 516,
        "PLASTIC BOTTLES (PACK OF 4)": 517,
        "METAL BOTTLE (1N)": 518,
        "GLASS BOTTLES (PACK OF 2)": 519,
        "DISPOSABLE GLASSES (25N)": 520,
        "GLASSES (4N)": 521,
        "METAL GLASSES (4N)": 522,
        "CUSHIONS (2N)": 523,
        "BED PILLOW (1N)": 524,
        "JUMBO PILLOW (1N)": 525,
        "CUSHION COVERS (2N)": 526,
        "PILLOW COVER (1N)": 527,
        "JUMBO PILLOW COVER (1N)": 528,
        # Stationery
        "BALL PENS (3N)": 601,
        "GEL PENS (1N)": 602,
        "PREMIUM GEL PEN (1N)": 603,
        "PREMIUM BALL PEN (1N)": 604,
        "HB PENCILS (PACK OF 1O)": 605,
        "EXTRA DARK PENCILS (PACK OF 10)": 606,
        "ERASER (1N)": 607,
        "JUMBO ERASER (1N)": 608,
        "SHARPENER (1N)": 609,
        "2 IN 1 ERASER SHARPENER (1N)": 610,
        "SCALE (15CM)": 611,
        "SCALE (30CM)": 612,
        "SMALL NOTEBOOK (120PG)": 613,
        "SMALL NOTEBOOK THICK (240PG)": 614,
        "BIG NOTEBOOK (120PG)": 615,
        "BIG NOTEBOOK THICK (240PG)": 616,
        "REGISTER (200PG)": 617,
        "THICK REGISTER (400PG)": 618,
        "SKETCHBOOK A4": 619,
        "SKETCHBOOK A3": 620,
        "SCRAP BOOK (50PG)": 621,
        "COLOUR PENCILS (10N)": 622,
        "CRAYONS (10N)": 623,
        "GLITTER PENS (10N)": 624,
        "COLOURED PAPERS (50N)": 625
    }


supermarket_dict = item_dict
price = {}
price.update(fruits_dict)
price.update(veg_dict)
price.update(dairy_dict)
price.update(grocery_dict)
price.update(pc_dict)
price.update(hn_dict)
price.update(st_dict)

# more items to be added....
