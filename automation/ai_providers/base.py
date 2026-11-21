"""
الواجهة المشتركة لمزودي AI
كل مزود جديد يجب أن يطبق هذه الدوال
"""

class AIProvider:
    """الفئة الأساسية لمزودي AI"""
    
    def __init__(self, api_key):
        self.api_key = api_key
    
    def generate(self, prompt, max_tokens=3000):
        """
        يولّد نص من AI
        
        Args:
            prompt: النص المُرسل للـ AI
            max_tokens: الحد الأقصى للرد
        
        Returns:
            str: النص المُولّد
        """
        raise NotImplementedError("يجب تنفيذ هذه الدالة")
    
    def generate_article(self, calc, lang="ar"):
        """يولّد مقال كامل"""
        raise NotImplementedError()
    
    def generate_faq(self, calc, lang="ar"):
        """يولّد أسئلة شائعة"""
        raise NotImplementedError()
    
    def generate_script(self, calc, lang="ar"):
        """يولّد JavaScript للحسابة"""
        raise NotImplementedError()
