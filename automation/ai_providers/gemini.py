"""
مزود Google Gemini
مجاني - 1500 طلب يومياً
"""

import os
import json
import urllib.request
import urllib.error
from .base import AIProvider


class GeminiProvider(AIProvider):
    """مزود Google Gemini"""
    
    BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models"
    
    def __init__(self, api_key, model="gemini-3.6-flash"):
        super().__init__(api_key)
        self.model = model
    
    def generate(self, prompt, max_tokens=3000):
        """يولّد نص باستخدام Gemini"""
        url = f"{self.BASE_URL}/{self.model}:generateContent?key={self.api_key}"
        
        payload = {
            "contents": [{
                "parts": [{"text": prompt}]
            }],
            "generationConfig": {
                "maxOutputTokens": max_tokens,
                "temperature": 0.7
            }
        }
        
        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode('utf-8'),
                headers={'Content-Type': 'application/json'}
            )
            
            with urllib.request.urlopen(req, timeout=60) as response:
                result = json.loads(response.read().decode('utf-8'))
                
                if 'candidates' in result and len(result['candidates']) > 0:
                    return result['candidates'][0]['content']['parts'][0]['text']
                else:
                    print(f"⚠️ رد غير متوقع: {result}")
                    return ""
        
        except urllib.error.HTTPError as e:
            print(f"⚠️ خطأ HTTP {e.code}: {e.read().decode('utf-8')}")
            return ""
        except Exception as e:
            print(f"⚠️ خطأ: {e}")
            return ""
    
    def generate_article(self, calc, lang="ar"):
        """يولّد مقال كامل للحاسبة"""
        title = calc['title_ar'] if lang == "ar" else calc['title_en']
        desc = calc['description_ar'] if lang == "ar" else calc['description_en']
        
        if lang == "ar":
            prompt = f"""اكتب مقالاً عربياً احترافياً عن "{title}" لموقع حاسبات سعودي.

المعلومات:
- الوصف: {desc}

المطلوب:
1. مقدمة (100 كلمة)
2. شرح الحاسبة (150 كلمة)
3. كيفية الاستخدام (100 كلمة)
4. نصائح أو حقائق مفيدة

المتطلبات:
- اكتب بصيغة HTML جاهزة
- استخدم <h3> و <p> و <ul> و <div class="tip">
- لا تكتب <html> أو <body>
- أسلوب احترافي وواضح
- المعلومات دقيقة للسوق السعودي
- اكتب بالعربية الفصحى
"""
        else:
            prompt = f"""Write a professional English article about "{title}" for a Saudi calculators website.

Info:
- Description: {desc}

Requirements:
1. Introduction (100 words)
2. Explanation (150 words)
3. How to use (100 words)
4. Tips or facts

Format:
- Write ready HTML
- Use <h3>, <p>, <ul>, <div class="tip">
- Don't include <html> or <body>
- Professional and clear tone
- Saudi market relevant
"""
        return self.generate(prompt, max_tokens=2500)
    
    def generate_faq(self, calc, lang="ar"):
        """يولّد أسئلة شائعة"""
        title = calc['title_ar'] if lang == "ar" else calc['title_en']
        
        if lang == "ar":
            prompt = f"""اكتب 4 أسئلة شائعة مع إجابات عن "{title}".

المطلوب: JSON فقط بالشكل التالي:
[
  {{"q": "السؤال 1", "a": "الإجابة 1"}},
  {{"q": "السؤال 2", "a": "الإجابة 2"}},
  {{"q": "السؤال 3", "a": "الإجابة 3"}},
  {{"q": "السؤال 4", "a": "الإجابة 4"}}
]

بدون شرح إضافي. JSON فقط.
"""
        else:
            prompt = f"""Write 4 FAQs with answers about "{title}".

Output: JSON only in this format:
[
  {{"q": "Question 1", "a": "Answer 1"}},
  {{"q": "Question 2", "a": "Answer 2"}},
  {{"q": "Question 3", "a": "Answer 3"}},
  {{"q": "Question 4", "a": "Answer 4"}}
]

No extra text. JSON only.
"""
        response = self.generate(prompt, max_tokens=1500)
        
        response = response.strip()
        if response.startswith("```"):
            response = response.split("```")[1]
            if response.startswith("json"):
                response = response[4:]
        response = response.strip()
        
        try:
            return json.loads(response)
        except:
            return []
    
    def generate_script(self, calc, lang="ar"):
        """يولّد JavaScript للحسابة"""
        fields = json.dumps(calc['fields'], ensure_ascii=False, indent=2)
        formula = calc.get(f'formula_{lang}', '')
        
        if lang == "ar":
            prompt = f"""اكتب كود JavaScript لحاسبة "{calc['title_ar']}" داخل دالة اسمها `calculate`.

الحقول المتوفرة (استخدم نفس id):
{fields}

المعادلة:
{formula}

القواعد الصارمة:
1. الكود **يجب** أن يكون داخل دالة اسمها calculate() بهذا الشكل بالضبط:

function calculate() {{
  var field1 = parseFloat(document.getElementById('FIELD_ID').value) || 0;
  var result = ...;
  document.getElementById('finalResult').textContent = formatNumber(result) + ' ريال';
  document.getElementById('resultCard').style.display = 'block';
}}

2. استخدم `document.getElementById('ID')` لكل حقل حسب id المذكور
3. عرض النتيجة في `document.getElementById('finalResult')`
4. أظهر البطاقة بـ `document.getElementById('resultCard').style.display = 'block'`
5. استخدم `formatNumber()` للتنسيق (موجودة مسبقاً)
6. إذا كان الحقل فاضي، اعتبره 0

مثال على المخرجات الصحيحة:

function calculate() {{
  var cash = parseFloat(document.getElementById('cash').value) || 0;
  var gold = parseFloat(document.getElementById('gold').value) || 0;
  var total = cash + gold;
  var zakat = total * 0.025;
  document.getElementById('finalResult').textContent = formatNumber(zakat) + ' ريال';
  document.getElementById('resultCard').style.display = 'block';
}}

المخرجات: JavaScript فقط. لا تكتب ``` أو أي شرح. ابدأ مباشرة بـ `function calculate()`.
"""
        else:
            prompt = f"""Write JavaScript code for "{calc['title_en']}" calculator inside a function called `calculate`.

Available fields (use same id):
{fields}

Formula:
{formula}

Strict rules:
1. Code **must** be inside a function named calculate() like this:

function calculate() {{
  var field1 = parseFloat(document.getElementById('FIELD_ID').value) || 0;
  var result = ...;
  document.getElementById('finalResult').textContent = formatNumber(result) + ' SAR';
  document.getElementById('resultCard').style.display = 'block';
}}

2. Use `document.getElementById('ID')` for each field
3. Display result in `document.getElementById('finalResult')`
4. Show card with `document.getElementById('resultCard').style.display = 'block'`
5. Use `formatNumber()` (already exists)
6. Empty fields count as 0

Output: JavaScript only. No ``` blocks. No explanations. Start with `function calculate()`.
"""
        response = self.generate(prompt, max_tokens=2000)
        
        response = response.strip()
        if response.startswith("```"):
            response = response.split("```")[1]
            if response.startswith("javascript") or response.startswith("js"):
                response = response.split("\n", 1)[1] if "\n" in response else response
        response = response.strip()
        
        return response
