import unittest
from sample.cat_n_mouse import cat_and_mouse


class TestCatAndMouse(unittest.TestCase):

    def test_give_0_y_z_return_allnone(self):
        x = 0 ; ys = [0,1,2,49,50,51,99,100,101] ; zs = [0,1,2,49,50,51,99,100,101]
        expects = [[None]*len(zs)]*len(ys)
        results = []
        for y in ys:
            result = [cat_and_mouse(x,y,z) for z in zs]
            results.append(result)
        self.assertEqual(results, expects)
    
    def test_give_1_y_z_return_allnone(self):
        x = 1 ; ys = [0,1,2,49,50,51,99,100,101] ; zs = [0,1,2,49,50,51,99,100,101]
        expects = [
            [None]*len(zs),
            [None, 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', None],
            [None, 'Cat A', 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat B', None],
            [None, 'Cat A', 'Cat A', 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat B', None],
            [None, 'Cat A', 'Cat A', 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat B', None],
            [None, 'Cat A', 'Cat A', 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat B', None],
            [None, 'Cat A', 'Cat A', 'Cat A', 'Mouse C', 'Cat B', 'Cat B', 'Cat B', None],
            [None, 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat B', 'Cat B', 'Cat B', None],
            [None]*len(zs)
        ]
        results = []
        for y in ys:
            result = [cat_and_mouse(x,y,z) for z in zs]
            results.append(result)
        self.assertEqual(results, expects)
    
    def test_give_2_y_z_return_allnone(self):
        x = 2 ; ys = [0,1,2,49,50,51,99,100,101] ; zs = [0,1,2,49,50,51,99,100,101]
        expects = [
            [None]*len(zs),
            [None, 'Cat B', 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat A', None],
            [None, 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', None],
            [None, 'Cat A', 'Cat A', 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat B', None],
            [None, 'Cat A', 'Cat A', 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat B', None],
            [None, 'Cat A', 'Cat A', 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat B', None],
            [None, 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat B', 'Cat B', 'Cat B', None],
            [None, 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Mouse C', 'Cat B', 'Cat B', None],
            [None]*len(zs)
        ]
        results = []
        for y in ys:
            result = [cat_and_mouse(x,y,z) for z in zs]
            results.append(result)
        self.assertEqual(results, expects)
    
    def test_give_49_y_z_return_allnone(self):
        x = 49 ; ys = [0,1,2,49,50,51,99,100,101] ; zs = [0,1,2,49,50,51,99,100,101]
        expects = [
            [None]*len(zs),
            [None, 'Cat B', 'Cat B', 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat A', None],
            [None, 'Cat B', 'Cat B', 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat A', None],
            [None, 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', None],
            [None, 'Cat A', 'Cat A', 'Cat A', 'Cat B', 'Cat B', 'Cat B', 'Cat B', None],
            [None, 'Cat A', 'Cat A', 'Cat A', 'Mouse C', 'Cat B', 'Cat B', 'Cat B', None],
            [None, 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat B', 'Cat B', None],
            [None, 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat B', 'Cat B', None],
            [None]*len(zs)
        ]
        results = []
        for y in ys:
            result = [cat_and_mouse(x,y,z) for z in zs]
            results.append(result)
        self.assertEqual(results, expects)
    
    def test_give_50_y_z_return_allnone(self):
        x = 50 ; ys = [0,1,2,49,50,51,99,100,101] ; zs = [0,1,2,49,50,51,99,100,101]
        expects = [
            [None]*len(zs),
            [None, 'Cat B', 'Cat B', 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat A', None],
            [None, 'Cat B', 'Cat B', 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat A', None],
            [None, 'Cat B', 'Cat B', 'Cat B', 'Cat A', 'Cat A', 'Cat A', 'Cat A', None],
            [None, 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', None],
            [None, 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat B', 'Cat B', 'Cat B', None],
            [None, 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat B', 'Cat B', None],
            [None, 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat B', 'Cat B', None],
            [None]*len(zs)
        ]
        results = []
        for y in ys:
            result = [cat_and_mouse(x,y,z) for z in zs]
            results.append(result)
        self.assertEqual(results, expects)
    
    def test_give_51_y_z_return_allnone(self):
        x = 51 ; ys = [0,1,2,49,50,51,99,100,101] ; zs = [0,1,2,49,50,51,99,100,101]
        expects = [
            [None]*len(zs),
            [None, 'Cat B', 'Cat B', 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat A', None],
            [None, 'Cat B', 'Cat B', 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat A', None],
            [None, 'Cat B', 'Cat B', 'Cat B', 'Mouse C', 'Cat A', 'Cat A', 'Cat A', None],
            [None, 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat A', 'Cat A', 'Cat A', None],
            [None, 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', None],
            [None, 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat B', 'Cat B', None],
            [None, 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat B', 'Cat B', None],
            [None]*len(zs)
        ]
        results = []
        for y in ys:
            result = [cat_and_mouse(x,y,z) for z in zs]
            results.append(result)
        self.assertEqual(results, expects)
    
    def test_give_99_y_z_return_allnone(self):
        x = 99 ; ys = [0,1,2,49,50,51,99,100,101] ; zs = [0,1,2,49,50,51,99,100,101]
        expects = [
            [None]*len(zs),
            [None, 'Cat B', 'Cat B', 'Cat B', 'Mouse C', 'Cat A', 'Cat A', 'Cat A', None],
            [None, 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat A', 'Cat A', 'Cat A', None],
            [None, 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat A', 'Cat A', None],
            [None, 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat A', 'Cat A', None],
            [None, 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat A', 'Cat A', None],
            [None, 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', None],
            [None, 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat A', 'Cat B', None],
            [None]*len(zs)
        ]
        results = []
        for y in ys:
            result = [cat_and_mouse(x,y,z) for z in zs]
            results.append(result)
        self.assertEqual(results, expects)
    
    def test_give_100_y_z_return_allnone(self):
        x = 100 ; ys = [0,1,2,49,50,51,99,100,101] ; zs = [0,1,2,49,50,51,99,100,101]
        expects = [
            [None]*len(zs),
            [None, 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat A', 'Cat A', 'Cat A', None],
            [None, 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Mouse C', 'Cat A', 'Cat A', None],
            [None, 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat A', 'Cat A', None],
            [None, 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat A', 'Cat A', None],
            [None, 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat A', 'Cat A', None],
            [None, 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat B', 'Cat A', None],
            [None, 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', 'Mouse C', None],
            [None]*len(zs)
        ]
        results = []
        for y in ys:
            result = [cat_and_mouse(x,y,z) for z in zs]
            results.append(result)
        self.assertEqual(results, expects)
    
    def test_give_101_y_z_return_allnone(self):
        x = 101 ; ys = [0,1,2,49,50,51,99,100,101] ; zs = [0,1,2,49,50,51,99,100,101]
        expects = [[None]*len(zs)]*len(ys)
        results = []
        for y in ys:
            result = [cat_and_mouse(x,y,z) for z in zs]
            results.append(result)
        self.assertEqual(results, expects)