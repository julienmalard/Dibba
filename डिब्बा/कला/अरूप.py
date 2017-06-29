class अरूप(object):

    मूल_कोश = {
        'रंग': {
            'Botón_normal': '',
            'Botón_sel': '',
            'Botón_clic': '',

            'Fondo': '#FFFFFF',

            'Texto_bt': '',
            'Texto_1': '',
            'Texto_2': '',
            'Texto_3': '',
            'Texto_4': '',

            'Bt_sí_normal': '',
            'Bt_sí_sel': '',
            'Bt_sí_clic': '',

            'Bt_no_normal': '',
            'Bt_no_sel': '',
            'Bt_no_clic': '',

            'Bt_bueno_normal': '',
            'Bt_bueno_sel': '',
            'Bt_bueno_clic': ''
        },
        'माप': {
            'Texto_1': '',
            'Texto_2': '',
            'Texto_3': '',
            'Texto_4': '',

            'Ingr_tx': '',
            'Menú': ''
        },
        'लिपि': {
            'Texto_1': '',
            'Texto_2': '',
            'Texto_3': '',
            'Texto_4': '',

            'Ingr_tx': '',
            'Menú': ''
        }
    }

    def __init__(खुद, कोश):

        कोश_तैयार = {}
        for अ in खुद.मूल_कोश:
            if अ in कोश:
                कोश_तैयार[अ] = {}
                for आ in खुद.मूल_कोश[अ]:
                    if अ in कोश:
                        कोश_तैयार[अ][आ] = कोश[अ][आ]
                    else:
                        कोश_तैयार[अ][आ] = खुद.मूल_कोश[अ]
            else:
                कोश_तैयार[अ] = खुद.मूल_कोश[अ]

        खुद.कोश = कोश_तैयार

    def __getitem__(खुद, item):
        return खुद.कोश[item]


अरूप_साधारण = अरूप(कोश={})
