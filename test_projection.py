#!/usr/bin/env python
# coding: utf-8

# In[3]:


import unittest
import ch_5
import math

class TestOrthogonalProjection(unittest.TestCase):
    def setUp(self):
        print("setup")
        self.case = ch_5.Ch5()
        
    def tearDown(self):
        print("end")
        
    # 課題6 正射影を求める関数
    # （引数：ベクトルx,正射影行列Pw）
    def test_orthogonal_projection(self): # テスト対象の関数の名前
        # ① u_1 = [[1],[0]], u_2 = [[0],[1]]
        # ② u_1 = [[1],[0],[0]], u_2 = [[0],[1],[0]], u_3 = [[0],[0],[1]]
        # ③ u_1 = [[1],[0],[0],[0]], u_2 = [[0],[1],[0],[0]], u_3 = [[0],[0],[1],[0]], u_4 = [[0],[0],[0],[1]]
        # ④ u_1 = [[1/math.sqrt(5)],[2/math.sqrt(5)]], u_2 = [[-2/math.sqrt(5)],[1/math.sqrt(5)]]
        # ⑤ u_1 = [[1/math.sqrt(2)],[0],[1/math.sqrt(2)]],
        #    u_2 = [[1/math.sqrt(3)],[1/math.sqrt(3)],[-1/math.sqrt(3)]],
        #    u_3 = [[-1/math.sqrt(6)],[2/math.sqrt(6)],[1/math.sqrt(6)]]
        
        # 整数 2次元
        # ①から正射影行列を作成(部分空間の次元r = 1)
        self.assertEqual([[-11],[0]],self.case.orthogonal_projection([[1,0],[0,0]],[[-11],[20]]))
        # ④から正射影行列を作成(部分空間の次元r = 1)
        self.assertAlmostEqual([[5.8],[11.6]],self.case.orthogonal_projection([[0.2,0.4],[0.4,0,8]],[[-11],[20]]))
        
        # 整数 3次元
        # ②から正射影行列を作成(部分空間の次元r = 2)
        self.assertEqual([[2],[3],[0]],self.case.orthogonal_projection([[1,0,0],[0,1,0],[0,0,0]],[[2],[3],[-1]]))
        # ⑤から正射影行列を作成(部分空間の次元r = 2)
        self.assertAlmostEqual([[2.5],[2],[-1.5]],self.case.orthogonal_projection([[5/6,1/3,1/6],[1/3,1/3,-1/3],[1/6,-1/3,5/6]],[[2],[3],[-1]]))
        
        # 整数 4次元
        # ③から正射影行列を作成(部分空間の次元r = 3)
        self.assertEqual([[5],[2],[1],[0]],self.case.orthogonal_projection([[1,0,0,0],[0,1,0,0],[0,0,0,0]],[[5],[2],[1],[4]]))
        
        # 小数
        # ②から正射影行列を作成(部分空間の次元r = 2)
        self.assertAlmostEqual([[0.4],[5.6],[0]],self.case.orthogonal_projection([[1,0,0],[0,1,0],[0,0,0]],[[0.4],[5.6],[-0.07]]))
        # ⑤から正射影行列を作成(部分空間の次元r = 2)
        self.assertAlmostEqual([[1313/600],[587/300],[-223/120]],self.case.orthogonal_projection([[5/6,1/3,1/6],[1/3,1/3,-1/3],[1/6,-1/3,5/6]],[[0.4],[5.6],[-0.07]]))
        
        # 複素数
        # ②から正射影行列を作成(部分空間の次元r = 2)
        self.assertEqual([[2-1j],[1j],[0]],self.case.orthogonal_projection([[1,0,0],[0,1,0],[0,0,0]],[[2-1j],[1j],[-1j]]))
        # ⑤から正射影行列を作成(部分空間の次元r = 2)
        self.assertAlmostEqual([[(5/3)-(2/3)*1j],[(2/3)+(1/3)*1j],[(1/3)-(4/3)*1j]],self.case.orthogonal_projection([[5/6,1/3,1/6],[1/3,1/3,-1/3],[1/6,-1/3,5/6]],[[2-1j],[1j],[-1j]]))
        
        # 異なる型の組み合わせ
        # ②から正射影行列を作成(部分空間の次元r = 2)
        self.assertAlmostEqual([[3],[1.2],[0]],self.case.orthogonal_projection([[1,0,0],[0,1,0],[0,0,0]],[[3],[1.2],[0.5j]]))
        # ⑤から正射影行列を作成(部分空間の次元r = 2)
        self.assertAlmostEqual([[2.9+(1/12)*1j],[1.4-(1/6)*1j],[0.1-(5/12)*1j]],self.case.orthogonal_projection([[5/6,1/3,1/6],[1/3,1/3,-1/3],[1/6,-1/3,5/6]],[[3],[1.2],[0.5j]]))
        
        
#     def test_raise_Exception(self):
#         with self.assertRaises(Exception):

        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


# In[ ]:




