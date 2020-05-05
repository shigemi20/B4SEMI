#!/usr/bin/env python
# coding: utf-8

# In[7]:


import unittest
import ch_5
import math

class TestNnorm(unittest.TestCase):
    def setUp(self):
        print("setup")
        self.case = ch_5.Ch5()
        
    def tearDown(self):
        print("end")
        
    # 課題2 引数をベクトルとnに設定し，n-ノルムを求める関数
    # （引数：ベクトル,n）
    # l_2ノルム→n=2
    # l_1ノルム→n=1
    def test_n_norm(self): # テスト対象の関数の名前
        # 整数 2次元 l_2
        self.assertAlmostEqual(math.sqrt(274),self.case.n_norm([[15],[-7]],2)) # math.sqrt(274)=16.552945...
        # 整数 2次元 l_1
        self.assertEqual(22,self.case.n_norm([[15],[-7]],1))
        
        # 整数 3次元 l_2
        self.assertAlmostEqual(math.sqrt(14),self.case.n_norm([[2],[3],[-1]],2)) # math.sqrt(14)=3.741657...
        # 整数 3次元 l_1
        self.assertEqual(6,self.case.n_norm([[2],[3],[-1]],1)) 
        
        # 整数 4次元 l_2
        self.assertAlmostEqual(math.sqrt(26),self.case.n_norm([[-3],[2],[2],[3]],2)) # math.sqrt(26)=5.099019...
        # 整数 4次元 l_1
        self.assertEqual(10,self.case.n_norm([[-3],[2],[2],[3]],1)) 
        
        # 小数 l_2
        self.assertAlmostEqual(math.sqrt(31.5249),self.case.n_norm([[0.4],[5.6],[-0.07]],2)) # math.sqrt(31.5249)=5.614703...
        # 小数 l_1
        self.assertAlmostEqual(6.07,self.case.n_norm([[0.4],[5.6],[-0.07]],1)) 
        
        # 複素数 l_2
        self.assertAlmostEqual(math.sqrt(7),self.case.n_norm([[2-1j],[1j],[-1j]],2)) # math.sqrt(7)=2.645751...
        # 複素数 l_1
        self.assertAlmostEqual(2+math.sqrt(5),self.case.n_norm([[2-1j],[1j],[-1j]],1)) # 2+math.sqrt(5)=4.236067...


        # 異なる型の組み合わせ l_2
        self.assertAlmostEqual(math.sqrt(57.36),self.case.n_norm([[-3],[5.6],[4+1j]],2)) # math.sqrt(57.36)=7.573638...
        # 異なる型の組み合わせ l_1
        self.assertAlmostEqual(8.6+math.sqrt(17),self.case.n_norm([[-3],[5.6],[4+1j]],1)) # 8.6+math.sqrt(17)=12.723105...
        
        

        
#     def test_raise_Exception(self):
#         with self.assertRaises(Exception):
        
        # 要相談
        # 横ベクトルの場合
        # n != 1 or n != 2の場合

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


# In[ ]:




