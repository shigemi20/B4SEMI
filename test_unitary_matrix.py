#!/usr/bin/env python
# coding: utf-8

# In[2]:


import unittest
import ch_5
import math

class TestUnitaryMatrix(unittest.TestCase):
    def setUp(self):
        print("setup")
        self.case = ch_5.Ch5()
        
    def tearDown(self):
        print("end")
        
    # 課題4 ユニタリ行列かどうか判定する関数
    # （引数：行列u）
    def test_unitary_matrix(self): # テスト対象の関数の名前
        # 整数 2*2
        self.assertTrue(self.case.unitary_matrix([[0,-1],[1,0]]))
        
        # 整数 3*3
        self.asserTrue([[0,-1,0],[0,0,-1],[1,0,0]])

        # 整数 4*4
        self.asserTrue([[1,0,0,0],[0,0,0,1],[0,0,-1,0],[0,1,0,0]])

        # 小数
        self.assertTrue(self.case.unitary_matrix([[0.8,-0.6],[0.6,0.8]])) 

        # 小数(ルートあり)
        self.assertTrue(self.case.unitary_matrix([[(1/math.sqrt(2)),0,(1/math.sqrt(2))],[0,1,0],[(-1/math.sqrt(2)),0,(1/math.sqrt(2))]])) 

        # 要検討
        # 複素数のみ

        # 組み合わせ
        self.assertTrue(self.case.unitary_matrix([[(1j/2),(1/math.sqrt(2)),(1/2)],[(1/math.sqrt(2)),0,(1j/math.sqrt(2))],[(1j/2),(-1/math.sqrt(2)),1/2]])) 
        
        
        
        # ユニタリ行列ではない正方行列
        self.assertFalse(self.case.unitary_matrix([[2-1j,4,-2j],[2,-1.1,-2],[0.4,3j,1.2]]))

        # 長方行列
        self.assertFalse(self.case.unitary_matrix([[2-1j,4,-2j,1],[2,-1.1,-2,0],[0.4,3j,1.2,3]]))
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


# In[ ]:




