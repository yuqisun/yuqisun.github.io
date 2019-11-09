---
title: [译] Dropout: A Simple Way to Prevent Neural Networks from Overfitting
tags:
- Deep Learning
- Regularization
- Dropout
- Translate
desc: 对于论文《Dropout: A Simple Way to Prevent Neural Networks from Overfitting》的翻译，以后自己回顾起来更快一些。
layout: post
---

[Dropout: A Simple Way to Prevent Neural Networks from Overfitting](https://www.cs.toronto.edu/~hinton/absps/JMLRdropout.pdf)

## Abstract

1. prevent overfitting
2. prevent co-adapting(共适应)

Training 时经过 dropout 后变成指数数量的 "thinned" networks；Test 时，使用完整的有更小权重的网络，近似于平均这些 "thinned" 网络的影响。

## 1. Introduction

在无限运算时，最好的正规化方法是对所有参数和权重下产生的预测进行平均。Dropout 是一种更低运算量的近似。

------

model 组合几乎总能提高机器学习性能，但平均每个单独训练的网络的输出很昂贵。

在每个单独 model 彼此不同时，对模型组合最有帮助，为了使模型不同，应该：

1. 让模型有不同结构
2. 或者在不同数据上训练

训练很多不同结构的模型很难：

1. 为每个结构找出最优超参数难
2. 计算量大
3. 大型网络需要大量数据
4. 即使可以训练，在需要快速反应时不可用

------

**Dropout 解决两个问题**：

1. 防止过拟合
2. 提供一种近似组合大量不同神经网络结构的方式

在最简单情况，每个 unit 保留的概率 P 是固定的，通常为 0.5；对于输入层 units，保留概率 P 通常接近 1。

------

对神经网络应用 dropout 相当于从其中抽取一个 "thinned" 网络样本。

n 个神经元的网络可视为有 2^n^ 种可能的 "thinned" 神经网络的集合。

这些网络共享权重，所以参数总量依然是 O(n^2^) 或更少。

所以使用 dropout 训练网络就相当于训练 2^n^ 个 "thinned" 网络的集合，它们共享权重。

----

在 test 时，计算指数级的神经网络的预测值的平均不可能，可以用近似方法。方法就是在 test 时不使用 dropout 而是将权重乘以概率 P，这确保 train 时的期望和 test 时实际输出相同。

通过这种方式，在 test 时可将 2^n^ 个共享权重的网络合并成一个网络。

----

dropout 不仅用于前馈神经网络，更通用于图模型，例如：Boltzmann Machines 玻尔兹曼机。

## 2. Motivation

dropout 灵感来源于有性繁殖，父母各遗传一半的基因加上很小的随机突变产生后代。无性繁殖通过复制父辈基因加少量突变产生后代。看起来无性繁殖更合理，因为一组能很好工作的基因可以直接遗传给后代，而有性繁殖会破坏基因组中的共同合作。然而有性繁殖是最高级的生物进化方式。

----

一种可能的解释是，自然选择考察的不是个体的适应性而是基因的混合能力。一组基因能够和另一组随机的基因合作的能力使其更健壮。因为基因不能依赖大量的伙伴(partners) 总是存在 --- （指有性繁殖中维护一个大的基因库，所有基因都要存在），它必须学会自己做一些有用的事或者只依赖少量的其他基因。

通过该理论，有性繁殖不仅允许有用的新基因在种群中传播，也减少了复杂的共适应。类似的，通过 dropout 训练的神经网络中的每个隐藏单元必须学会和随机选中的其他单元合作，这使每个隐藏单元更健壮，并促使其向着创造有用特征的方向去，而不依赖其他隐藏单元来纠正它的错误。

----

另一个稍不同的灵感来自于成功的阴谋。有10个阴谋，每个需要5个人，比一个要求50个人都各自准确完成自己的工作的大阴谋更容易造成一次大破坏。复杂的共适应在训练集可被训练的比较好，但在测试集上比多个简单共适应更容易失败。

## 3. Related Work

dropout 可以看成是通过往隐藏单元添加噪音的方式对 NN 正规化。dropout 20% input units 和 50% hidden units 通常是最优的。

## 4. Model Description

L 层神经网络

$l \in\{1, \ldots, L\}$

$\mathbf{z}^{(l)}$ 表示第 $l$ 层输入向量

$\mathbf{y}^{(l)}$ 表示第 $l$ 层输出向量  ($\mathbf{y}^{(0)}=\mathbf{x}$)

$W^{(l)}$ 和 $\mathbf{b}^{(l)}$ 是第 $l$ 层的权重和偏差

一个标准的前馈神经网络过程可以表示成 ($\text { for } l \in\{0, \ldots, L-1\}$ , any hidden unit $i$)：

$z_{i}^{(l+1)}=\mathbf{w}_{i}^{(l+1)} \mathbf{y}^{l}+b_{i}^{(l+1)}$

$y_{i}^{(l+1)}=f\left(z_{i}^{(l+1)}\right)$

$f$ 是任意激活函数，例如：$f(x)=1 /(1+\exp (-x))$

----

使用 dropout，前馈操作变成：

$r_{j}^{(l)} \sim \text { Bernoulli }(p)$

$\widetilde{\mathbf{y}}^{(l)}=\mathbf{r}^{(l)} * \mathbf{y}^{(l)}$

$z_{i}^{(l+1)}=\mathbf{w}_{i}^{(l+1)} \widetilde{\mathbf{y}}^{l}+b_{i}^{(l+1)}$

$y_{i}^{(l+1)}=f\left(z_{i}^{(l+1)}\right)$

----

这里 $*$ 是元素间(element-wise) 乘法。对于任意层 $l$ ，$\mathbf{r}^{(l)}$ 是一个由独立伯努利 (Bernoulli) 随机变量组成的向量，每个变量是 1 的可能性为 p。这个向量 ($\mathbf{r}^{(l)}$) 与这一层的输出 $\mathbf{y}^{(l)}$ 做 element-wise 乘法，得到 "thinned" 输出 $\widetilde{\mathbf{y}}^{(l)}$。这个 "thinned" 输出接下来做下一层的输入，这个过程被应用到每一层，这相当于从一个大的网络中采样出一个子网络 (sub-network)。在 training时，loss function 反向传播的导数是通过子网络 (sub-network) 计算的；在 test时，权重被缩放成 $W_{t e s t}^{(l)}=p W^{(l)}$ ，作为结果的神经网络是不用 dropout 的。

----

> **Bernoulli** - 伯努利分布，又名两点分布或 0-1 分布。是一个离散型概率分布，若伯努利实验成功，则伯努利随机变量取值为 1，失败则为 0。记其成功概率为 p，则失败概率为 q=1-p。
>
> 这里在前向传播之前使用伯努利分布就是想得到离散的 $r_{j}^{(l)}$，得到概率是 0 或者 1，0则丢弃，1则保留。使用 $\mathbf{r}^{(l)} * \mathbf{y}^{(l)}$ 得到 dropout 后的值用于计算。

## 5. Learning Dropout Nets

这一张描述训练 dropout 的过程。

### 5.1 Backpropagation

训练 dropout 神经网络与训练标准的神经网络相似，可以使用随机梯度下降 (stochastic gradient descent)。唯一的不同是对于一个mini-batch 中的每个 training case 会通过 drop out units 采样出一个 "thinned" 网络。对于该 training case 的前向和反向传播都是只在这个 "thinned" 网络上做的。在每个 mini-batch 的 training case 上的每个参数的梯度是被求平均值的，任何没有使用参数的 training case (被 drop out 了) 对那个参数的贡献则为 0。

> 每个 mini-batch 对应一个 "thinned" 网络；多个 mini-batch 中训练出的参数的梯度求平均。

有很多方法被使用去提高随机梯度下降，例如 momentum, annealed learning rates 和 L2 weight decay。这些对于 dropout 神经网络同样有效。

----

一种特定形式的正规化对 dropout 尤其有用 - 即约束每个隐藏单元的权重向量的上限为一个固定常量 c。换言之，如果 w 代表权重向量，则神经网络要在约束条件 $\|\mathbf{w}\|_{2} \leq c$ 进行优化。这个约束在任何 w 将超出半径为 c 的球表面时起作用。这也被称为 **max-norm regularization** ，因为任何权重能取得的最大值都是 c。常量 c 是一个可调节的超参数 (hyperparameter)，由验证集(validation set) 决定。即使不使用 dropout，max-norm regularization 也可以显著提升随机梯度下降的性能。

----

虽然只使用 dropout 即可有显著提升，但 dropout 与 max-norm regularization, large decaying learning rates, high momentum 结合会有更显著的效果。一种可能是解释是约束权重向量是其限制在固定半径的球中，则可使用大学习率而不至于不能收敛（发散）。由 dropout 提供的噪声使最优化过程能搜索权重空间的不同部分，随着学习率衰减，最优化步长减小，因而探索范围减小，最终到达最优点。

> 这里是将权重 weight 想象成空间向量来理解，权重的维度对应空间的方向（轴），而最优化的权重范围在空间中是一个立体的范围，max-norm 将空间限制成一个球体，半径就是常量 c，dropout 提供的噪声使最优化不能单纯依赖某个或某些维度，而使其向更多维度探索（探索最优解）。decay learning rate 使越接近最小值（最优化结果）步长越小。

### 5.2 Unsupervised Pretraining

## 6. Experimental Results

## 7. Salient Features

## 8. Dropout Restricted Boltzmann Machines

## 9. Marginalizing Dropout

## 10. Multiplicative Gaussian Noise

## 11. Conclusion

Dropout 通过降低过拟合来改善神经网络，标准的反向传播学习会建立脆弱的共适应 (co-adaptations)，只适用于 training data，而不适用于未见过的一般化数据。随机 dropout 通过使任意特定隐藏单元不可依赖来打破共适应 (co-adaptations)。dropout 被发现能为神经网络在各个领域提高性能，包括：对象分类，数字识别，语音识别，文档分类，计算生物数据分析。这说明 dropout 是一种一般化技术而不是针对特定领域。dropout 不仅对 SVHN, ImageNet, CIFAR-100 and MNIST 有帮助，对在其他数据上的标准神经网络也有显著提升。

----

这个 idea (dropout) 可以扩展到 RBM(Restricted Boltzmann Machines) 和其他图方法。 dropout的中心思想是把从一个容易发生过拟合的大 model 和重复的样本中提取出更小的子model (sub-models) 来训练。RBMs 很容易融入这个框架，我们开发出了 *Dropout RBMs* 并且经验显示其具备多项很好的属性。

----

Dropout 的一个缺点是训练时间变长，同样结构下，使用 dropout 的训练时间一般比标准神经网络长 2-3 倍。造成时间增加的主要原因是参数更新非常嘈杂。每个训练 case 都极力试图训练一个不同的随机结构，因为正在被计算的梯度并不是会应用在测试上的最终结构。因而 dropout 需要的训练时间更长久不足为奇了。dropout 的随机性可以防止过拟合，这在过拟合和训练时间之间建立了权衡，用更多的时间，可以使用 high dropout 和 less overfitting。然而，一种既拥有 dropout 的优点又不要随机性的方式是边缘化噪音来获得一个和 dropout 做同样事情的正规化器 (regularizer)。我们已经展示对于线性回归，这个正规化器是 L2 正规化的变种，对于更复杂的模型，则难以很容易的找到等价的正规化器。加速 dropout 是未来工作的一个有趣的方向。

> 这一段就是吴军在《写科技论文的诀窍》中讲的 “好的论文最后都会从学术的角度，讲一下自己未完成的工作，这些工作或许是自己正在进行的，或许是留给同行的。”

## Appendix A. A Practical Guide for Training Dropout Networks

神经网络在需要大量调整参数方面一直被诟病，dropout 也不例外，在这一章展示了一些可能对应用 dropout 有用的启发。

### A.1 Network Size

意料之中，dropout 会降低神经网络容量，设任意一层的隐藏单元数为 n，单元保留率为 p，则 dropout 后单元数为 pn，然而这个 pn 个单元的集合每次都不一样，可以防止共适应。因而对于给定任务，如果一个标准神经网络的理想的一层的大小是 n (n 个 units)，则一个好的 dropout 网络应该有 n/p 个单元。我们发现这无论是对卷积还是全连接网络，对于设置隐藏单元的数量是一个启示。

### A.2 Learning Rate and Momentum

dropout 相比于标准随机梯度下降(sgd: stochastic gradient descent) 在梯度上引入了大量噪音，因而大量的梯度倾向于彼此抵消。为了弥补这一点，dropout 网络应该用标准神经网络学习率的 10~100倍的学习率，另一种减少影响的方法是高动量(high momentum)，对于标准网络常用的动量值为 0.9，而对于 dropout 网络，我们发现使用 0.95的值会好很多，使用高学习率 and/or 大动量能显著提高学习速度。

### A.3 Max norm Regularization

> norm 范数

虽然大动量和大学习率能加速学习，但有时也导致网络权重变得很大。为防止这一点，可以使用 max-norm 正规化。它能将每个隐藏单元的权重向量的范数约束在常亮 c 内，c 的范围通常为 3~4。

### A.4 Dropout Rate

dropout 引入了一个额外的超参数 - 单元保留率 p。这个超参数控制 dropout 的强度，p=1， 不使用 dropout；p 越小，dropout 强度越大。对于隐藏单元，典型的 p 值为 0.5~0.8。对于输入层，决定于输入的类型，对于实数(real-valued)输入(图像块或语音帧)，典型取值为 0.8；对于隐藏层，p 的选择和隐藏层单元数 n有关系，p 越小，则需要 n 很大(p 小会减慢训练速度，导致欠拟合)，p很大可能不能起到足够的 dropout 作用来防止过拟合。

