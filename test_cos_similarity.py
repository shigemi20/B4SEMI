#!/usr/bin/env python
# coding: utf-8

# In[2]:


import unittest
import ch_5
import math

class TestCosineSimilarity(unittest.TestCase):
    def setUp(self):
        print("setup")
        self.case = ch_5.Ch5()
        
    def tearDown(self):
        print("end")
        
    # 課題3 コサイン類似度を求める関数
    # （引数：ベクトルx,ベクトルy）
    def test_cosine_similarity(self): # テスト対象の関数の名前
        # 整数 2次元
        self.assertAlmostEqual((-25)/(math.sqrt(521)*math.sqrt(274)),self.case.cosine_similarity([[-11],[20]],[[15],[7]])) # cosθ=(-25)/(math.sqrt(521)*math.sqrt(274))=-0.06616767...
        
        # 整数 3次元
        self.assertAlmostEqual((-1)/(math.sqrt(14)*math.sqrt(29)),self.case.cosine_similarity([[2],[3],[-1]],[[4],[-2],[3]])) # cosθ=(-1)/(math.sqrt(14)*math.sqrt(29))=-0.04962916...
        
        # 整数 4次元
        self.assertAlmostEqual(3/(math.sqrt(46)*math.sqrt(26)),self.case.cosine_similarity([[5],[2],[1],[4]],[[-3],[2],[2],[3]])) # cosθ=3/(math.sqrt(46)*math.sqrt(26))=0.08674723...
        
        # 小数
        self.assertAlmostEqual(1.023/(math.sqrt(31.5249)*math.sqrt(12.1484)),self.case.cosine_similarity([[0.4],[5.6],[-0.07]],[[-1.1],[0.22],[-3.3]])) # cosθ=1.023/(math.sqrt(31.5249)*math.sqrt(12.1484))=0.05227442...
        
        # 要検討
        # 複素数
        self.assertAlmostEqual((-3-9j)/(math.sqrt(7)*math.sqrt(28)),self.case.cosine_similarity([[2-1j],[1j],[-1j]],[[3j],[1+1j],[4+1j]])) 
        
        # 要検討
        # 異なる型の組み合わせ
        self.assertAlmostEqual((1.2+3.75j)/(math.sqrt(10.69)*math.sqrt(23.25)),self.case.cosine_similarity([[3],[1.2],[0.5j]],[[2+1j],[-4],[1.5]])) 
        
        # 内積が0の場合(直交)
        self.assertEqual(0,self.case.cosine_similarity([[2],[3],[-1]],[[4],[-2],[2]])) 
        
        # 2つのベクトルが一致する場合(cosθ=1の場合)
        self.assertEqual(1,self.case.cosine_similarity([[2],[3],[-1]],[[2],[3],[-1]])) 
        
        # 2つのベクトルの向きが逆の場合(cosθ=-1の場合)
        self.assertEqual(-1,self.case.cosine_similarity([[2],[3],[-1]],[[-2],[-3],[1]])) 
        
 
    def test_raise_Exception(self):
        with self.assertRaises(Exception):
            # xのノルムが0の場合(0割り)
            self.case.cosine_similarity([[0],[0],[0]],[[4],[-2],[3]]) # 計算不能(エラー処理)
        
            # yのノルムが0の場合(0割り)
            self.case.cosine_similarity([[2],[3],[-1]],[[0],[0],[0]]) # 計算不能(エラー処理)
            
            # 要相談
            # 横ベクトルの場合
            
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


# In[ ]:




