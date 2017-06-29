from डिब्बा.चीज़ import चीज़
from डिब्बा.implementaciones import implementación


class चित्र(चीज़):

    def __init__(खुद, नाम, स्थान, आपेक्षिक_स्थान, माप, आपेक्षिक_माप):
        खुद.नाम = नाम

        super().__init__(स्थान, आपेक्षिक_स्थान, माप, आपेक्षिक_माप)


class चित्र_टिेके(implementación):
    def हटाना(खुद, तरफ़):
        pass

    def दिखाना(खुद):
        pass

    def बनाना(खुद):
        pass

    def रखना(खुद, स्थान):
        pass

    def चिपाना(खुद):
        pass
