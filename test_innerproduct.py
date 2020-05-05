#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
import ch_5

class TestInnerProduct(unittest.TestCase):
    
    def setUp(self):
        print("setup")
        self.case = ch_5.Ch5()
        
    def tearDown(self):
        print("end")
        
    # 課題1 ユークリッド内積を求め，直交性を判定する関数
    # （引数：ベクトルx,ベクトルy）
    def test_euclidean_inner_product(self): # テスト対象の関数の名前
        # 整数 2次元
        self.assertEqual(-25,self.case.euclidean_inner_product([[-11],[20]],[[15],[7]])) # 直交でない
        
        # 整数 3次元
        self.assertEqual(-1,self.case.euclidean_inner_product([[2],[3],[-1]],[[4],[-2],[3]])) # 直交でない
        
        # 整数 4次元
        self.assertEqual(3,self.case.euclidean_inner_product([[5],[2],[1],[4]],[[-3],[2],[2],[3]])) # 直交でない

        # 小数
        self.assertAlmostEqual(1.023,self.case.euclidean_inner_product([[0.4],[5.6],[-0.07]],[[-1.1],[0.22],[-3.3]])) # 直交でない
        
        # 複素数
        self.assertEqual(-3-9j,self.case.euclidean_inner_product([[2-1j],[1j],[-1j]],[[3j],[1+1j],[4+1j]])) # 直交でない
        
        # 複素数 xとyを入れ替える
        self.assertEqual(-3+9j,self.case.euclidean_inner_product([[3j],[1+1j],[4+1j]],[[2-1j],[1j],[-1j]])) # 直交でない
        
        # 異なる型の組み合わせ
        self.assertAlmostEqual(1.2-2.25j,self.case.euclidean_inner_product([[3],[1.2],[0.5j]],[[2+1j],[-4],[1.5]])) # 直交でない
        
        # 直交な場合
        self.assertEqual(0,self.case.euclidean_inner_product([[2],[3],[-1]],[[4],[-2],[2]])) # 直交である
        
        
    def test_raise_Exception(self):
        with self.assertRaises(Exception):
            # 成分数が異なる x > y
            self.case.euclidean_inner_product([[2],[3],[-1]],[[4],[-2]]) # 計算不能(エラー処理)
            
            # 成分数が異なる x < y
            self.case.euclidean_inner_product([[2],[3],[-1]],[[4],[-2],[3],[6]]) # 計算不能(エラー処理)

            # 要検討
            # 縦ベクトル・横ベクトル
            self.case.euclidean_inner_product([[2],[3],[-1]],[[4,-2,3]]) # 計算不能(? 計算するとすれば行列?)

            # 要検討
            # 横ベクトル・縦ベクトル
            self.case.euclidean_inner_product([[2,3,-1]],[[4],[-2],[3]]) # 計算不能(? 計算するとすれば内積?)

            # 要検討
            # 横ベクトル・横ベクトル
            self.case.euclidean_inner_product([[2,3,-1]],[[4,-2,3]]) # 計算不能(?)

        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


# In[ ]:




