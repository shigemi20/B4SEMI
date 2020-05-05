#!/usr/bin/env python
# coding: utf-8

# In[2]:


import unittest
import ch_5
import math

class TestGramSchmidt(unittest.TestCase):
    def setUp(self):
        print("setup")
        self.case = ch_5.Ch5()
        
    def tearDown(self):
        print("end")
        
    # 課題5 グラム・シュミットの正規直交化を用いて基底を正規直交化する関数
    # （引数：基底(可変長...？)）
    def test_Gram_Schmidt_orthonormalization(self): # テスト対象の関数の名前
        # 整数 2次元
        self.assertAlmostEqual([[1/math.sqrt(5),-2/math.sqrt(5)],
                                [2/math.sqrt(5),1/math.sqrt(5)]],
                                self.case.Gram_Schmidt_orthonormalization([[1,-3],
                                                                           [-2,4]]))
        # v_1 = (1/math.sqrt(5))[[1],[2]] = [[0.4472135...],[0.8944271...]]
        # v_2 = (1/math.sqrt(5))[[-2],[1]] = [[-0.8944271...],[0.4472135...]]

        
        # 整数 3次元
        self.assertAlmostEqual([[1/math.sqrt(2),1/math.sqrt(3),-1/math.sqrt(6)],
                                [0,1/math.sqrt(3),2/math.sqrt(6)],
                                [1/math.sqrt(2),-1/math.sqrt(3),1/math.sqrt(6)]],
                                self.case.Gram_Schmidt_orthonormalization([[1,2,2],
                                                                           [0,1,3],
                                                                           [1,0,2]]))
        # v_1 = (1/math.sqrt(2))[[1],[0],[1]] = [[0.7071067...],[0],[0.7071067...]]
        # v_2 = (1/math.sqrt(3))[[1],[1],[-1]] = [[0.5773502...],[0.5773502...],[-0.5773502...]]
        # v_3 = (1/math.sqrt(6))[[-1],[2],[1]] = [[-0.4082482...],[0.8164965...],[0.4082482...]]

        
        # 小数
        self.assertAlmostEqual([[1/math.sqrt(5),(-2.8*math.sqrt(5))/7],
                                [-2/math.sqrt(5),(1.4*math.sqrt(5))/7]],
                                self.case.Gram_Schmidt_orthonormalization([[0.1,-0.2],
                                                                           [0.2,0.3]]))
        # v_1 = (10/math.sqrt(5))[[0.1],[0.2]] = [[0.4472135...],[0.8944271...]]
        # v_2 = (10*math.sqrt(5)/7)[[-0.28],[0.14]] = [[-0.8944271...],[0.4472135...]] 

        
        # 複素数
        self.assertAlmostEqual([[(2j)/math.sqrt(6),(5j)/(3*math.sqrt(3))],
                                [(1-1j)/math.sqrt(6),(1-1j)/(3*math.sqrt(3))]],
                                self.case.Gram_Schmidt_orthonormalization([[2j,1j],
                                                                           [1-1j,0]]))
        # v_1 = (1/math.sqrt(6))[[2j],[1-1j]] = [[0.8164965...j],[0.4082482...-0.4082482...j]]
        # v_2 = (1/(3*math.sqrt(3)))[[5j],[1-1j]] = [[0.962250...j],[0.1924500...-0.1924500...j]]
        
        
        # 異なる型の組み合わせ
        self.assertAlmostEqual([[1,0],
                                [0,1j]],
                                self.case.Gram_Schmidt_orthonormalization([[2,0.1],
                                                                           [0,1j]]))
        # v_1 = (1/2)[[2],[0]] = [[1],[0]]
        # v_2 = [[0],[1j]]
        
        
        # 内積が0になるのを含む場合
        self.assertAlmostEqual([[0.6,-0.8],
                                [0.8,0.6]],
                                self.case.Gram_Schmidt_orthonormalization([[3,-4],
                                                                           [4,3]]))
        # v_1 = (1/5)[[3],[4]] = [[0.6],[0.8]]
        # v_2 = (1/5)[[-4],[3]] = [[-0.8],[0.6]]
        
        
 
    def test_raise_Exception(self):
        with self.assertRaises(Exception):
            # ノルムが0になるのを含む場合
            self.case.Gram_Schmidt_orthonormalization([[3,0],
                                                       [4,0]])
            # 計算不能(エラー処理)

        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


# In[ ]:




