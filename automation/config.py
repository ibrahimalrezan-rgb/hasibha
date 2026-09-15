#!/usr/bin/env python3
"""
إعدادات مشتركة لمشاريع Hasibha
"""

SITE_URL = "https://hasibha.com"
SITE_NAME = "حاسبها"
SITE_NAME_EN = "Hasibha"

# قائمة جميع الحاسبات - المصد ر الوحيد للحقيقة
PAGES = [
    {"slug": "mortgage", "title_ar": "حاسبة التمويل العقاري", "title_en": "Mortgage Calculator", "category": "finance", "icon": "🏠",
     "desc_ar": "قسطك الشهري وقدرتك على الشراء لأي عقار سكني.",
     "desc_en": "Monthly payment and purchasing power for any residential property."},
    {"slug": "personal-loan", "title_ar": "حاسبة التمويل الشخصي", "title_en": "Personal Loan Calculator", "category": "finance", "icon": "💵",
     "desc_ar": "القسط الشهري والفائدة لأي مبلغ ومدة تمويل.",
     "desc_en": "Monthly installment and interest for any amount and term."},
    {"slug": "eos", "title_ar": "حاسبة نهاية الخدمة", "title_en": "End of Service Calculator", "category": "finance", "icon": "📋",
     "desc_ar": "مكافأتك وفق نظام العمل السعودي — استقالة أو فصل.",
     "desc_en": "Your benefit according to Saudi Labor Law — resignation or termination."},
    {"slug": "vat", "title_ar": "حاسبة ضريبة القيمة المضافة", "title_en": "VAT Calculator", "category": "finance", "icon": "🧾",
     "desc_ar": "إضافة أو استبعاد 15% من أي مبلغ في ثانية.",
     "desc_en": "Add or exclude 15% from any amount in a second."},
    {"slug": "salary", "title_ar": "الراتب بعد التأمينات", "title_en": "Salary After Insurance", "category": "finance", "icon": "💼",
     "desc_ar": "صافي راتبك بعد خصم التأمينات الاجتماعية (GOSI).",
     "desc_en": "Your net salary after GOSI social insurance deduction."},
    {"slug": "zakat", "title_ar": "حاسبة الزكاة", "title_en": "Zakat Calculator", "category": "finance", "icon": "🕌",
     "desc_ar": "احسب زكاة أموالك بدقة وفق الأحكام الشرعية",
     "desc_en": "Calculate your Zakat accurately according to Sharia principles."},
    {"slug": "gold-value", "title_ar": "حاسبة قيمة الذهب", "title_en": "Gold Value Calculator", "category": "finance", "icon": "🥇",
     "desc_ar": "احسب قيمة الذهب حسب الوزن والعيار والسعر الحالي",
     "desc_en": "Calculate gold value by weight, karat and current price."},
    {"slug": "currency", "title_ar": "تحويل العملات", "title_en": "Currency Converter", "category": "conversion", "icon": "💱",
     "desc_ar": "ريال سعودي، دولار، يورو وأكثر — بأسعار محدثة.",
     "desc_en": "SAR, USD, EUR and more — with updated rates."},
    {"slug": "length", "title_ar": "تحويل الطول", "title_en": "Length Converter", "category": "conversion", "icon": "📏",
     "desc_ar": "أمتار، أقدام، إنشات وبوصات بضغطة واحدة.",
     "desc_en": "Meters, feet, inches in one click."},
    {"slug": "weight", "title_ar": "تحويل الوزن", "title_en": "Weight Converter", "category": "conversion", "icon": "⚖️",
     "desc_ar": "كيلوغرام، رطل، أونصة وجرام بدقة كاملة.",
     "desc_en": "Kilograms, pounds, ounces and grams with full precision."},
    {"slug": "area", "title_ar": "تحويل المساحة", "title_en": "Area Converter", "category": "conversion", "icon": "📐",
     "desc_ar": "متر مربع، فدان، هكتار وكيلومتر مربع.",
     "desc_en": "Square meters, acres, hectares and square kilometers."},
    {"slug": "bmi", "title_ar": "مؤشر كتلة الجسم BMI", "title_en": "BMI Calculator", "category": "health", "icon": "🧍",
     "desc_ar": "وزنك المثالي وتصنيفك الصحي بالتفصيل.",
     "desc_en": "Your ideal weight and health classification in detail."},
    {"slug": "calorie", "title_ar": "حاسبة السعرات الحرارية", "title_en": "Calorie Calculator", "category": "health", "icon": "🍎",
     "desc_ar": "احتياجك اليومي من الطاقة حسب نشاطك وهدفك.",
     "desc_en": "Your daily energy needs based on activity and goal."},
    {"slug": "water", "title_ar": "حاسبة احتياج الماء", "title_en": "Water Intake Calculator", "category": "health", "icon": "💧",
     "desc_ar": "كم لتر يحتاج جسمك يوميًا بناءً على وزنك.",
     "desc_en": "How many liters your body needs daily based on weight."},
    {"slug": "age", "title_ar": "حاسبة العمر", "title_en": "Age Calculator", "category": "general", "icon": "🎂",
     "desc_ar": "عمرك بالسنوات والأشهر والأيام بدقة كاملة.",
     "desc_en": "Your exact age in years, months and days."},
    {"slug": "discount", "title_ar": "حاسبة نسبة الخصم", "title_en": "Discount Calculator", "category": "general", "icon": "🏷️",
     "desc_ar": "كم وفّرت فعلًا من السعر الأصلي في التخفيضات.",
     "desc_en": "How much you actually saved from the original price."},
    {"slug": "date-diff", "title_ar": "الوقت بين تاريخين", "title_en": "Date Difference", "category": "general", "icon": "📅",
     "desc_ar": "الفارق بين أي تاريخين بالأيام والشهور والسنوات.",
     "desc_en": "The gap between any two dates in days, months and years."},
]

# التصنيفات
CATEGORIES = {
    "finance": {"ar": "مالية", "en": "Finance"},
    "conversion": {"ar": "تحويلات", "en": "Converters"},
    "health": {"ar": "صحة", "en": "Health"},
    "general": {"ar": "عامة", "en": "General"},
}
