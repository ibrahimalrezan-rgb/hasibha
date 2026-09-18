#!/usr/bin/env python3
"""إعدادات موقع حاسبها - المصدر الوحيد للتصنيفات"""

SITE_URL = "https://hasibha.com"

CATEGORIES = {
    "finance":    {"ar": "مالية",    "en": "Finance",    "icon": "💰"},
    "conversion": {"ar": "تحويلات",  "en": "Conversion", "icon": "🔄"},
    "health":     {"ar": "صحية",     "en": "Health",     "icon": "❤️"},
    "general":    {"ar": "عامة",     "en": "General",    "icon": "📦"},
}

PAGES = [
    {"slug": "mortgage",      "title_ar": "حاسبة التمويل العقاري",      "title_en": "Mortgage Calculator",       "desc_ar": "قسطك الشهري وقدرتك على الشراء لأي عقار سكني.",            "desc_en": "Monthly payment and purchasing power for any home.",   "category": "finance",    "icon": "🏠"},
    {"slug": "personal-loan", "title_ar": "حاسبة التمويل الشخصي",       "title_en": "Personal Loan Calculator",    "desc_ar": "القسط الشهري والفائدة لأي مبلغ ومدة تمويل.",              "desc_en": "Monthly installment and interest for any amount.",     "category": "finance",    "icon": "💵"},
    {"slug": "eos",           "title_ar": "حاسبة نهاية الخدمة",         "title_en": "End of Service Calculator",   "desc_ar": "مكافأتك وفق نظام العمل السعودي — استقالة أو فصل.",        "desc_en": "Your benefit per Saudi Labor Law — resignation or termination.", "category": "finance", "icon": "📋"},
    {"slug": "vat",           "title_ar": "حاسبة ضريبة القيمة المضافة", "title_en": "VAT Calculator",              "desc_ar": "إضافة أو استبعاد 15% من أي مبلغ في ثانية.",               "desc_en": "Add or remove 15% VAT from any amount instantly.",     "category": "finance",    "icon": "🧾"},
    {"slug": "salary",        "title_ar": "الراتب بعد التأمينات",       "title_en": "Salary After Insurance",      "desc_ar": "صافي راتبك بعد خصم التأمينات الاجتماعية (GOSI).",         "desc_en": "Your net salary after GOSI deduction.",                "category": "finance",    "icon": "💼"},
    {"slug": "zakat",         "title_ar": "حاسبة الزكاة",               "title_en": "Zakat Calculator",            "desc_ar": "احسب زكاة أموالك بدقة وفق الأحكام الشرعية.",              "desc_en": "Calculate your Zakat accurately per Sharia rules.",    "category": "finance",    "icon": "🕌"},
    {"slug": "gold-value",    "title_ar": "حاسبة قيمة الذهب",           "title_en": "Gold Value Calculator",       "desc_ar": "احسب قيمة الذهب حسب الوزن والعيار والسعر الحالي.",        "desc_en": "Gold value by weight, karat and current price.",       "category": "finance",    "icon": "🥇"},
    {"slug": "currency",      "title_ar": "تحويل العملات",              "title_en": "Currency Converter",          "desc_ar": "ريال سعودي، دولار، يورو وأكثر — بأسعار محدثة.",           "desc_en": "SAR, USD, EUR and more with live rates.",              "category": "conversion", "icon": "💱"},
    {"slug": "length",        "title_ar": "تحويل الطول",                "title_en": "Length Converter",            "desc_ar": "أمتار، أقدام، إنشات وبوصات بضغطة واحدة.",                 "desc_en": "Meters, feet, inches in one click.",                   "category": "conversion", "icon": "📏"},
    {"slug": "weight",        "title_ar": "تحويل الوزن",                "title_en": "Weight Converter",            "desc_ar": "كيلوغرام، رطل، أونصة وجرام بدقة كاملة.",                  "desc_en": "Kilograms, pounds, ounces and grams.",                 "category": "conversion", "icon": "⚖️"},
    {"slug": "area",          "title_ar": "تحويل المساحة",              "title_en": "Area Converter",              "desc_ar": "متر مربع، فدان، هكتار وكيلومتر مربع.",                    "desc_en": "Square meters, acres, hectares and km².",              "category": "conversion", "icon": "📐"},
    {"slug": "bmi",           "title_ar": "مؤشر كتلة الجسم",            "title_en": "BMI Calculator",              "desc_ar": "وزنك المثالي وتصنيفك الصحي بالتفصيل.",                    "desc_en": "Your ideal weight and health category.",               "category": "health",     "icon": "🧍"},
    {"slug": "calorie",       "title_ar": "حاسبة السعرات الحرارية",     "title_en": "Calorie Calculator",          "desc_ar": "احتياجك اليومي من الطاقة حسب نشاطك وهدفك.",               "desc_en": "Daily energy needs based on activity and goal.",       "category": "health",     "icon": "🍎"},
    {"slug": "water",         "title_ar": "حاسبة احتياج الماء",         "title_en": "Water Intake Calculator",     "desc_ar": "كم لتر يحتاج جسمك يوميًا بناءً على وزنك.",                "desc_en": "How many liters your body needs daily.",               "category": "health",     "icon": "💧"},
    {"slug": "age",           "title_ar": "حاسبة العمر",                "title_en": "Age Calculator",              "desc_ar": "عمرك بالسنوات والأشهر والأيام بدقة كاملة.",               "desc_en": "Your exact age in years, months and days.",            "category": "general",    "icon": "🎂"},
    {"slug": "discount",      "title_ar": "حاسبة نسبة الخصم",           "title_en": "Discount Calculator",         "desc_ar": "كم وفّرت فعلًا من السعر الأصلي في التخفيضات.",             "desc_en": "How much you really saved from the original price.",   "category": "general",    "icon": "🏷️"},
    {"slug": "date-diff",     "title_ar": "الوقت بين تاريخين",          "title_en": "Date Difference Calculator",  "desc_ar": "الفارق بين أي تاريخين بالأيام والشهور والسنوات.",          "desc_en": "Gap between any two dates in days and months.",        "category": "general",    "icon": "📅"},
]
