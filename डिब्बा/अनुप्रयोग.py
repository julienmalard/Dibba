from डिब्बा.कला.अरूप import अरूप_साधारण


class अनुप्रयोग(object):
    def __init__(खुद, नाम, उँचाई=350, लम्बाई=400, अरूप=None, तरह='TK'):
        """
        
        :param नाम: 
        :type नाम: str
        :param तरह:
        :type तरह: str
        """

        खुद.नाम = नाम
        खुद.उँचाई = उँचाई
        खुद.लम्बाई = लम्बाई

        if अरूप is None:
            अरूप = अरूप_साधारण
        खुद.अरूप = अरूप

        if तरह == 'TK':
            खुद.implémentation = अनुप्रयोग_टिके(नाम=नाम, अरूप=खुद.अरूप)
        else:
            raise ValueError('अपहचाई अनुप्रयोग की तरह ({})'.format(तरह))

    def जोड़ना(खुद, पन्ना):
        खुद.implémentation.जोड़ना(पन्ना=पन्ना)

    def चलाना(खुद):
        खुद.implémentation.चलाना()


class अनुप्रयोग_implémentation(object):

    def __init__(खुद, नाम, अरूप):
        खुद.अरूप = अरूप
        खुद.नाम = नाम

    def जोड़ना(खुद, पन्ना):
        raise NotImplementedError

    def चलाना(खुद):
        raise NotImplementedError


class अनुप्रयोग_टिके(अनुप्रयोग_implémentation):
    pass
