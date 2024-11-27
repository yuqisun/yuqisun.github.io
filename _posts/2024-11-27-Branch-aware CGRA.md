---
layout: post
title: "Paper reading: branch-aware CGRA"
tagline: "CGRA"
---

铺垫很多，重点就一个：打包节点（Packing Pair of Nodes）。  
解决的问题是 ITE的问题，用的方法是打包节点。

## 详细点就是：

### 1.先用现成的方案（Full/Partial都有）构造DFG，比如这样的一个DFG (a图)；
![img.png](https://raw.githubusercontent.com/yuqisun/yuqisun.github.io/master/_posts/images/cgra/img.png)

### 2.有DFG之后用paper里的 Algorithm 1 （输入 DFG D 如上图(a)，输出节点打包后的DFG-节点数量减少（c）)。
![img.png](https://raw.githubusercontent.com/yuqisun/yuqisun.github.io/master/_posts/images/cgra/img_1.png)

#### 算法过程：这是个从后往前推的算法。
```
# M 是已经打包了的节点的集合，while一直到M不增加，即再没有节点能打包了为止
while |M| increasing do
```
---
```
# C 是候选节点的集合，while到没有候选节点为止
while |C| increasing do
```
---
```
# 这段就是说啥样的节点属于候选节点，遍历 D 里的所有节点，两种节点是候选节点：
# 1. So = So ∩ M -> So 是 o节点的所有后继节点，So = So ∩ M 就是说 So 的所有节点和 已经打包的节点交集都是 So，就是说 o 节点的所有后继都被打包了，这样打包 o节点就不会影响后边的依赖关系了（所以说这个算法得从后往前看，DFG从下到上）；
# 2. o is a select -> 第二种就是 select 节点，整个文章要解决的就是这个 if -else 问题。
for All instructions o in D do
    So ← successors of o;
    if So = So ∩ M or o is a select then
        C ← C ∪ {o};
```
---
```
# 没太明白，大概就是和 clk 有关，得保证这俩节点在一个周期执行才能被打包
ASAP_Schedule D;
ALAP_Schedule D;
```
---
```
# 下边是打包操作，分为两种：
# 1.如果 o 是 select 操作，正中下怀，把 o 和 Ioi 和 Ioe打包成 Po，就是上图DFG (a) 变成 (b)：用六边形 e 打包了 菱形e和 et, ef；
if o is a select instruction then
    Pack o, Ioi , and Ioe into Po;

# 2.如果不是 select操作，看if和else的所有输入值（这里 x 表示笛卡尔积），按打包成本排序，i和j成本最低，有共同输入，就打包成 (c)
else
    S ← (if-path × else-path) inputs of o;
    Sort S by cost of each pair;
    if the best cost is positive then
        Replace selected pair with Po;
```

