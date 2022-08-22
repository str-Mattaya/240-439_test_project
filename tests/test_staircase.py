import unittest
from sample.staircase import gen_staircase


class TestStaircase(unittest.TestCase):
    def test_give_n_neg1_display_hash_return_nothing(self):
        n = -1 ; display = '#'
        expect = []
        result = gen_staircase(n, display)
        self.assertEqual(result, expect)
    
    def test_give_n_0_display_hash_return_nothing(self):
        n = 0 ; display = '#'
        expect = []
        result = gen_staircase(n, display)
        self.assertEqual(result, expect)
    
    def test_give_n_1_display_hash_return_listofstair(self):
        n = 1 ; display = '#'
        expect = ['#']
        result = gen_staircase(n, display)
        self.assertEqual(result, expect)
    
    def test_give_n_2_display_hash_return_listofstair(self):
        n = 2 ; display = '#'
        expect = [
            ' #',
            '##'
        ]
        result = gen_staircase(n, display)
        self.assertEqual(result, expect)
    
    def test_give_n_14_display_hash_return_listofstair(self):
        n = 14 ; display = '#'
        expect = [
            '             #',
            '            ##',
            '           ###',
            '          ####',
            '         #####',
            '        ######',
            '       #######',
            '      ########',
            '     #########',
            '    ##########',
            '   ###########',
            '  ############',
            ' #############',
            '##############',
        ]
        result = gen_staircase(n, display)
        self.assertEqual(result, expect)
    
    def test_give_n_15_display_hash_return_listofstair(self):
        n = 15 ; display = '#'
        expect = [
            '              #',
            '             ##',
            '            ###',
            '           ####',
            '          #####',
            '         ######',
            '        #######',
            '       ########',
            '      #########',
            '     ##########',
            '    ###########',
            '   ############',
            '  #############',
            ' ##############',
            '###############',
        ]
        result = gen_staircase(n, display)
        self.assertEqual(result, expect)
    
    def test_give_n_16_display_hash_return_listofstair(self):
        n = 16 ; display = '#'
        expect = [
            '               #',
            '              ##',
            '             ###',
            '            ####',
            '           #####',
            '          ######',
            '         #######',
            '        ########',
            '       #########',
            '      ##########',
            '     ###########',
            '    ############',
            '   #############',
            '  ##############',
            ' ###############',
            '################',
        ]
        result = gen_staircase(n, display)
        self.assertEqual(result, expect)
    
    def test_give_n_29_display_hash_return_listofstair(self):
        n = 29 ; display = '#'
        expect = [
            '                            #',
            '                           ##',
            '                          ###',
            '                         ####',
            '                        #####',
            '                       ######',
            '                      #######',
            '                     ########',
            '                    #########',
            '                   ##########',
            '                  ###########',
            '                 ############',
            '                #############',
            '               ##############',
            '              ###############',
            '             ################',
            '            #################',
            '           ##################',
            '          ###################',
            '         ####################',
            '        #####################',
            '       ######################',
            '      #######################',
            '     ########################',
            '    #########################',
            '   ##########################',
            '  ###########################',
            ' ############################',
            '#############################',
        ]
        result = gen_staircase(n, display)
        self.assertEqual(result, expect)
    
    def test_give_n_30_display_hash_return_listofstair(self):
        n = 30 ; display = '#'
        expect = [
            '                             #',
            '                            ##',
            '                           ###',
            '                          ####',
            '                         #####',
            '                        ######',
            '                       #######',
            '                      ########',
            '                     #########',
            '                    ##########',
            '                   ###########',
            '                  ############',
            '                 #############',
            '                ##############',
            '               ###############',
            '              ################',
            '             #################',
            '            ##################',
            '           ###################',
            '          ####################',
            '         #####################',
            '        ######################',
            '       #######################',
            '      ########################',
            '     #########################',
            '    ##########################',
            '   ###########################',
            '  ############################',
            ' #############################',
            '##############################',
        ]
        result = gen_staircase(n, display)
        self.assertEqual(result, expect)
    
    def test_give_n_31_display_hash_return_nothing(self):
        n = 31 ; display = '#'
        expect = []
        result = gen_staircase(n, display)
        self.assertEqual(result, expect)
    
    def test_five_n_5_display_hash_return_listofstair(self):
        n = 5 ; display = '#'
        expect = [
            '    #',
            '   ##',
            '  ###',
            ' ####',
            '#####',
        ]
        result = gen_staircase(n, display)
        self.assertEqual(result, expect)
    
    def test_five_n_5_display_nonestr_return_listofnonestr(self):
        n = 5 ; display = ''
        expect = [
            '',
            '',
            '',
            '',
            '',
        ]
        result = gen_staircase(n, display)
        self.assertEqual(result, expect)
    
    def test_five_n_5_display_2hash_return_listof2widestair(self):
        n = 5 ; display = '##'
        expect = [
            '        ##',
            '      ####',
            '    ######',
            '  ########',
            '##########',
        ]
        result = gen_staircase(n, display)
        self.assertEqual(result, expect)
    
    def test_five_n_5_display_3hash_return_listof3widestair(self):
        n = 5 ; display = '###'
        expect = [
            '            ###',
            '         ######',
            '      #########',
            '   ############',
            '###############',
        ]
        result = gen_staircase(n, display)
        self.assertEqual(result, expect)
    
    def test_five_n_5_display_asterisk_return_listofstair(self):
        n = 5 ; display = '*'
        expect = [
            '    *',
            '   **',
            '  ***',
            ' ****',
            '*****',
        ]
        result = gen_staircase(n, display)
        self.assertEqual(result, expect)
    
    def test_five_n_5_display_space_return_squareofspace(self):
        n = 5 ; display = ' '
        expect = [
            '     ',
            '     ',
            '     ',
            '     ',
            '     ',
        ]
        result = gen_staircase(n, display)
        self.assertEqual(result, expect)
    
    def test_five_n_5_display_str_return_listofstair_str(self):
        n = 5 ; display = 'str'
        expect = [
            '            str',
            '         strstr',
            '      strstrstr',
            '   strstrstrstr',
            'strstrstrstrstr',
        ]
        result = gen_staircase(n, display)
        self.assertEqual(result, expect)

