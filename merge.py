# merge_config.py
import pandas as pd
MERGE_MAP = {
    "WHEAT(CHAPATI,ROTI,NAAN,DALIA,RAWA/SOOJI,SEVIYAAN": [
            "WHEAT(CHAPATI,ROTI,NAAN,DALIA,RAWA/SOOJI,SEVIYAAN"],
    
    "WHEAT FREE CEREALS": [
        "RICE(RICE, RICE FLOOR, DOSA, POHA, IDLI, MURMURA)",
        "MAIZE(CHAPATI, CHHALI, BHUTTA, CORN COB)",
        "OATS(OATS MEAL, ROLLED OATS)",
        "BARLEY",
        "RAGI, BAJRA, JOWAR",
        "AMARANTH(CHULAI, RAJGIRA, SEEL)",
        "OTHERS(EX. BESAN ROTI, ETC)" ],
    
    "FRUITS": [
        "RED, DEEP ORANGES, YELLOW FRUITS(MANGO, PAPAYA, PEACH ETC)",
        "CITRUS FRUITS(LEMON, ORANGE, GRAPEFRUITS ETC)",
        "BERRIES AND GRAPES(RASBERRY, CHERRY, STRAWBERRY, AMLA, GRAPES)",
        "OTHERS(APPLE, BANANA, CHEEKU, KIWI, ETC)"],
    
    "OTHER VEGETABLES": [
        "GREEN LEAFY",
        "GREEN(TINDA.TORI, KADU ETC)",
        "CRUCIFEROUS",
        "BULBS(GARLIC, ONION)",
        "OTHERS(BRINJAL, CARROT, RADISH, CUCUMBER, TURNIP, GINGER ETC)"],
    
    "STARCHY(POTATO,SWEET PATATO,ARBI ETC)": ["STARCHY(POTATO,SWEET PATATO,ARBI ETC)"],
    
    "PULSES AND LEGUMES": [
        "PULSES(LENTILS, ARHAR, TUR, GREEN GRAMS, BLACK GRAMS ETC)",
        "LEGUMES( GREEN PEAS, CHICKPEA, RAJMAH, RONGI ETC)",
        "SOYBEANS"],
    
    "PREDOMINANT SATURATED FATS": ["DESI GHEE, BUTER, MALAI",
                                   "COCONUT OIL, PALM OIL"],

    "PREDOMINANT UNSATURATED FATS": [
        "RICE BRAN OIL, SUNFLOWER OIL, SAFFLOWER ETC",
        "LINSEED OIL(ALSI), CANOLA OIL, MUSTARD OIL, OLIVE OIL"],


    
    "TRANS FATS": ["DALDA,VANASPATI,ETC"],
    
    
    
    "NUTS AND OILSEEDS": ["ALMONDS,WALNUTS,GROUNDNUTS,CASHEWNUTS,FLAX_SEEDS,SUNFLOWER_SEEDS"],
    
    "EGGS,FISH AND POULTRY": ["EGGS",
                              "CHICKEN/TURKEY",
                              "FISH AND SEAFOOD"],
    
    "RED MEAT": ["RED MEAT(MOTTON/PORK/BEEF)"],
    
    "MILK ": ["MILK"],
    
    "LOW LACTOSE DAIRY": ["HOME MADE CURD",
                          "HOMEMADE BUTTERMILK/LASSI/CHAACH",
                         "COTTAGE CHEESE(PANIR)"],
    
    "SWEETEND BEVERAGES": ["CARBONATED DRINKS/SODA",
                           "BOTTLED/TETRA-PACK/POWDERED JUICES/FRUITS DRINKS/CONCENTRATES",
                           "ENERGY DRINKS",
                           "BOTTLED/PACKED DAIRY DRINKS"],
    
    "ULTRA PROCESSED FOODS": [
        "PACKED BREADS/BUNS/KULCHA/PAV",
        "CAKES/MUFFIN/PASTRY/CAKE MIX",
        "BREAKFAST CEREAL/BREAKFAST BARS",
        "ICE CREAM",
        "PUDDINGS AND PIES",
        "JELLIES N JAM",
        "CHOCOLATES",
        "DRESSINGS, MAYONNAISE, SPREADS AND MARGARINES",
        "CANDIES/GUMMIES",
        "PACKED SOUPS",
        "INSTANT NOODLES",
        "PACKED MEAT/FISH/VEGETABLES",
        "PROCESSED CHEESE",
        "CONDENSED MILK/MILKMAID",
        "PRE PREPARED READY TO EAT MEALS"

    ],
    "READT TO EAT PACKAGED SNACKS": ["SALTY(CHIPS/ KURKURE/COOKIES/BISCUITS)",
                                     "SWEETS(BISCUITS/RUSKS/COOKIES)"],
    
    "SAVORY SNACKS": ["SAMOSA/KACHORI, PAKORA, MATHRI, ETC",
                      "MANCHURIAN/URGER/HOT DOGS ETC",
                      "BHEL PURI/MURI/PANI PURI/PUCHKA/BHALLA/DHOKLA",
                      "PIZZA/PASTA/NOODLES/PATTY/MOMOS ETC"],

    "PROCESSED FOODS": ["FROZEN FOOD(NOVA CLASS- 1)",
                        "KETCHUP/PUREE(CLASS-III)",
                        "PICKLES(NOVA-III)",
                        "CHUTNEY(NOVA -III)",
                        "CANNED VEGITABLES PRESEVERED IN SALTY SOLUTIONS/VINEGER(NOVA CLASS- III)",
                        "CANNED FRUITS IN SUGAR SYRUP(NOVA CLASS III)",
                        "CANNED FISH(NOVA-III)",
                        "SALTED DRIED SMOKE MEAT/FISH/SAUSAGES(NOVA CLASS-III)",
                        "ALMOND MILK, SOY MILK, COCONUT MILK, OAT MILK, TOFU"],
    
    "INDIAN SWEET MEATS": ["KHOYA BURFI, RUBRI, LADOO, KALAKAND, GULAB JAMUN, SUNDESH, KHEER, HALWA, IMRTI, ETC",
                           "KHOYA"],
    
    "FOOD SUPPLEMENTS": ["CALCIUM SUPPLEMENTS",	
                         "VIT -D SUPPLEMENTS",
                         "ZINC SUPPLEMENTS",
                         "IRON SUPPLEMENTS",
                         "PROTEIN SUPPLEMENTS"],
    
    "ERGOGENIC SUPPLEMENTS": ["FAT BURNERS/BODY BUILDING GYM SUPPLEMENTS"],
    
}

def merge_features(df_raw: pd.DataFrame) -> pd.DataFrame:
    merged = {}
    for merged_name, raw_features in MERGE_MAP.items():
        existing = [f for f in raw_features if f in df_raw.columns]
        merged[merged_name] = df_raw[existing].sum(axis=1) if existing else 0
    return pd.DataFrame(merged)








