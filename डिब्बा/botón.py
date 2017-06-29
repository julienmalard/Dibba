from डिब्बा.चीज़ import चीज़


class botón(चीज़):
    def __init__(खुद, acción, स्थान, आपेक्षिक_स्थान, माप, आपेक्षिक_माप, args_acción):
        super().__init__(स्थान, आपेक्षिक_स्थान, माप, आपेक्षिक_माप)

        खुद.acción = acción
        खुद.args_acción = args_acción

    def cliquear(खुद):
        खुद.acción(**खुद.args_acción)


class botón_चित्र(botón):
    def __init__(खुद, चित्र, acción, स्थान, आपेक्षिक_स्थान, माप, आपेक्षिक_माप, args_acción=None):
        super().__init__(acción, स्थान, आपेक्षिक_स्थान, माप, आपेक्षिक_माप, args_acción)


class botón_tx(botón):
    def __init__(खुद, texto, acción, स्थान, आपेक्षिक_स्थान, माप, आपेक्षिक_माप, args_acción=None):
        super().__init__(acción, स्थान, आपेक्षिक_स्थान, माप, आपेक्षिक_माप, args_acción)
