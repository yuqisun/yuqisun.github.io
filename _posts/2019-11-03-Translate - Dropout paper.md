---
title: Translate - Dropout paper
tags:
- Deep Learning
- Regularization
- Dropout
- Translate
desc: Translate paper "Dropout: A Simple Way to Prevent Neural Networks from Overfitting".
layout: post
---

[Dropout: A Simple Way to Prevent Neural Networks from Overfitting](https://www.cs.toronto.edu/~hinton/absps/JMLRdropout.pdf)

## Abstract

1. prevent overfitting
2. prevent co-adapting(共适应)

Training 时经过 dropout 后变成指数数量的 "thinned" networks；Test 时，使用完整的有更小权重的网络，近似于平均这些 "thinned" 网络的影响。
