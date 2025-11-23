# merge_config.py
import pandas as pd
MERGE_MAP = {
    "Wheat(Chapati,Roti,Naan,Dalia,Rawa/Sooji,Seviyaan": [
            'Wheat(Chapati,Roti,Naan,Dalia,Rawa/Sooji,Seviyaan'],
    
    "Wheat Free Cereals": [
        "RICE(RICE,RICE FLOOR, DOSA,POHA,IDLLI,MURMURA)",
        "MAIZE(CHAPATI,CHHALI,BHUTTA,CORN COB",
        "OATS(OATS MEAL,ROLLED",
        "BARLEY",
        "RAGI,BAJRA,JOWAR",
        "AMARANTH(CHULAI,RAJGIRA,SEEL",
        "OTHERS(EX. BESAN ROTI,ETC" ],
    
    "Fruits": [
        "RED,DEEP ORANGES,YELLOW FRUITS(MANGO,PAPAYA,PEACH ETC",
        "CITRUS FRUITS(LEMON,ORANGE,GRAPEFRUITS ETC",
        "BERRIES AND GRAPES(RASBERRY, CHERRY,STRAWBERRY,AMLA,GRAPES",
        "OTHERS( APPLE,BANANA,CHEEKU,KIWI,ETC"],
    
    "Other Vegetables": [
        "GREEN LEAFY",
        "GREEN(TINDA.TORI,KADU ETC"
        "CRUCIFEROUS",
        "BULBS(GARLIC,OINION)",
        "OTHERS(BRINJAL,CARROT,RADISH,CUCUMBER, TERNIP,GINGER ETC)"],
    
    "Starchy(Potato,Sweet Patato,Arbi Etc)": ["Starchy(Potato,Sweet Patato,Arbi Etc)"],
    
    "Pulses And Legumes": [
        "PULSES(LENTILS,ARHAR,TUR,GREEN GRAMS,BLACK GRAMS ETC)",
        "LEGUMES( GREEN PEAS,CHICKPEA,RAJMAH,RONGI ETC)",
        "SOYBEANS"],
    
    " Predominant Saturated Fats": ["DESI GHEE,BUTER,MALAI",
                                   "COCONUT OIL, PALM OIL"],
    
    "Trans Fats": ["DALDA","VANASPATI"],
    
    "Predominant Unsaturated Fats": [
        "RICE_BRAN_OIL","SUNFLOWER_OIL","SAFFLOWER_OIL","LINSEED_OIL",
        "CANOLA_OIL","MUSTARD_OIL","OLIVE_OIL"],
    
    "Nuts And Oilseeds": ["ALMONDS","WALNUTS","GROUNDNUTS","CASHEWNUTS","FLAX_SEEDS","SUNFLOWER_SEEDS"],
    
    "Eggs,Fish And Poultry": ["EGGS",
                              "CHICKEN/TURKEY",
                              "FISH AND SEAFOOD"],
    
    "Red Meat": ["RED MEAT(MOTTON/PORK/BEEF)"],
    
    "Milk": ["MILK"],
    
    "Low Lactose_Dairy": ["HOME MADE CURD",
                          "HOMEMADE BUTTERMILK/LASSI/CHAACH",
                         "COTTAGE CHEESE(PANIR)"],
    
    "Sweetend Beverages": ["CARBONATED DRINKS/SODA",
                           "BOTTLED/TETRA-PACK/POWDERED JUICES/FRUITS DRINKS/CONCENTRATES",
                           "ENERGY DRINKS",
                           "BOTTLED/PACKED DAIRY DRINKS"],
    
    "Ultra Processed Foods": [
        "PACKED BREADS/BUNS/KULCHA/PAV",
        "CAKES/MUFFIN/PASTRY/CAKE MIX",
        "BREAKFAST CEREAL/BREAKFAST BARS",
        "ICE CREAM","PUDDINGS AND PIES",
        "JELLIES N JAM",
        "CHOCOLATES",
        "CANDIES/GUMMIES",
        "DRESSINGS,MAYONNAISE,SPREADS AND MARGARINES",
        "PACKED SOUPS",
        "INSTANT NOODLES",
        "PACKED MEAT/FISH/VEGETABLES",
        "PROCESSED CHEESE"
        "PRE PREPARED READY TO EAT MEALS",
        "CONDENSED MILK/MILKMAID"
    ],
    "Readt To Eat Packaged Snacks": ["SALTY(CHIPS/ KURKURE/COOKIES/BISCUITS)",
                                     "SWEETS(BISCUITS/RUSKS/COOKIES"],
    
    "Savory Snacks": ["SAMOSA/KACHORI,PAKORA,MATHRI,ETC",
                      "MANCHURIAN/URGER/HOT DOGS ETC",
                      "BHEL PURI/MURI/PANI PURI/PUCHKA/BHALLA/DHOKLA",
                      "PIZZA/PASTA/NOODLES/PATTY/MOMOS ETC"],

    "Processed Foods": ["FROZEN FOOD(NOVA CLASS- 1)",
                        "KETCHUP/PUREE(CLASS-III)_",
                        "PICKLES(NOVA-III)",
                        "CHUTNEY(NOVA -III",
                        "CANNED VEGITABLES PRESEVERED IN SALTY SOLUTIONS/VINEGER(NOVA CLASS- III",
                        "CANNED FRUITS IN SUGAR SYRUP(NOVA CLASS III",
                        "CANNED FISH(NOVA-III",
                        "SALTED DRIED SMOKE MEAT/FISH/SAUSAGES(NOVA CLASS-III",
                        "ALMOND MILK,SOY MILK,COCONUT MILK OAT MILK,TOFU"],
    
    "Indian Sweet Meats": ["KHOYA BURFI,RUBRI,LADOO,KALAKAND,GULAB JAMUN,SUNDESH,KHEER,HALWA,IMRTI, ETC",
                           "KHOYA"],
    
    "Food Supplements": ["CALCIUM SUPPLEMENTS",	
                         "VIT -D SUPPLEMENTS",
                         "ZINC SUPPLEMENTS",
                         "IRON SUPPLEMENTS",
                         "PROTEIN SUPPLEMENTS"],
    
    "Ergogenic Supplements": ["FAT BURNERS/BODY BUILDING GYM SUPPLEMENTS"],
    
}

