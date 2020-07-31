# awesome-fast-attention [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[![Build Status](https://travis-ci.com/Separius/awesome-sentence-embedding.svg?branch=master)](https://travis-ci.com/Separius/awesome-fast-attention)
[![GitHub - LICENSE](https://img.shields.io/github/license/Separius/awesome-fast-attention.svg?style=flat)](./LICENSE)

A curated list of efficient attention modules

## Table of Contents

* **[About This Repo](#about-this-repo)**
* **[Efficient Attention](#efficient-attention)**
* **[Articles](#articles)**

## About This Repo

* enjoy!

## Efficient Attention

|Paper(citations)|Code|Complexity|Mask|main_idea|
|:---:|:---:|:---:|:---:|:---:|
|[CCNet: Criss-Cross Attention for Semantic Segmentation](https://http://arxiv.org/abs/1811.11721v2 )(148)|[CCNet](https://github.com/speedinghzl/CCNet ) ![](https://img.shields.io/github/stars/speedinghzl/CCNet.svg?style=social )|O(N\*(H+W)\*D)|Autoregressive::x: CustomMask::x:|<details><summary>EXPAND</summary><p>each pixel attends to its row and column simultaneously</p></details>|
|[Efficient Attention: Attention with Linear Complexities](https://http://arxiv.org/abs/1812.01243v8 )(2)|[efficient-attention](https://github.com/cmsflash/efficient-attention ) ![](https://img.shields.io/github/stars/cmsflash/efficient-attention.svg?style=social )|O(N\*D^2)|Autoregressive::x: CustomMask::x:|<details><summary>EXPAND</summary><p>softmax(q)(softmax(k)v)</p></details>|
|[GCNet: Non-local Networks Meet Squeeze-Excitation Networks and Beyond](https://http://arxiv.org/abs/1904.11492v1 )(96)|[GCNet](https://github.com/xvjiarui/GCNet ) ![](https://img.shields.io/github/stars/xvjiarui/GCNet.svg?style=social )|O(N\*D^2)|Autoregressive::x: CustomMask::x:|<details><summary>EXPAND</summary><p>squeeze and excitation with an attention pooling (instead of a GAP)</p></details>|
|[Interlaced Sparse Self-Attention for Semantic Segmentation](https://http://arxiv.org/abs/1907.12273v2 )(13)|IN_PAPER|O(N\*D^2+N\*sqrt(N)\*D)|Autoregressive::heavy_check_mark: CustomMask::wavy_dash:|<details><summary>EXPAND</summary><p>combination of a short length and then long range(dilated) attention</p></details>|
|[Compressive Transformers for Long-Range Sequence Modelling](https://http://arxiv.org/abs/1911.05507v1 )(20)|[compressive-transformer-pytorch](https://github.com/lucidrains/compressive-transformer-pytorch ) ![](https://img.shields.io/github/stars/lucidrains/compressive-transformer-pytorch.svg?style=social )|O(N^2\*D)|Autoregressive::heavy_check_mark: CustomMask::wavy_dash:|<details><summary>EXPAND</summary><p>compresses distant tokens instead of just stop_grad() ing them, more efficient version of transformerXL</p></details>|
|[BP-Transformer: Modelling Long-Range Context via Binary Partitioning](https://http://arxiv.org/abs/1911.04070v1 )(8)|[BPT](https://github.com/yzh119/BPT ) ![](https://img.shields.io/github/stars/yzh119/BPT.svg?style=social )|O(N\*k\*log(N/k)\*D)|Autoregressive::heavy_check_mark: CustomMask::wavy_dash:|<details><summary>EXPAND</summary><p>attends to distant tokens coarsely and attends to close tokens in a more fine-grained manner</p></details>|
|[Axial Attention in Multidimensional Transformers](https://http://arxiv.org/abs/1912.12180v1 )(5)|[axial-attention](https://github.com/lucidrains/axial-attention ) ![](https://img.shields.io/github/stars/lucidrains/axial-attention.svg?style=social )|O(N\*(H+W)\*D)|Autoregressive::heavy_check_mark: CustomMask::x:|<details><summary>EXPAND</summary><p>apply attention on each axis separately</p></details>|
|[Transformer on a Diet](https://http://arxiv.org/abs/2002.06170v1 )(2)|[transformer-on-diet](https://github.com/cgraywang/transformer-on-diet ) ![](https://img.shields.io/github/stars/cgraywang/transformer-on-diet.svg?style=social )|O(N\*k\*D)|Autoregressive::heavy_check_mark: CustomMask::wavy_dash:|<details><summary>EXPAND</summary><p>dilated transformer like wavenet</p></details>|
|[SAC: Accelerating and Structuring Self-Attention via Sparse Adaptive Connection](https://http://arxiv.org/abs/2003.09833v2 )(1)|-|O(N\*k\*D)|Autoregressive::heavy_check_mark: CustomMask::heavy_check_mark:|<details><summary>EXPAND</summary><p>learns the q, k connections == dynamically creates a sparse attention matrix</p></details>|
|[Efficient Content-Based Sparse Attention with Routing Transformers](https://http://arxiv.org/abs/2003.05997v1 )(11)|[routing-transformer](https://github.com/lucidrains/routing-transformer ) ![](https://img.shields.io/github/stars/lucidrains/routing-transformer.svg?style=social )|O(N\*sqrt(N)\*D)|Autoregressive::x: CustomMask::x:|<details><summary>EXPAND</summary><p>computes attention with same-cluster tokens (computed by online k-means)</p></details>|
|[Neural Architecture Search for Lightweight Non-Local Networks](https://http://arxiv.org/abs/2004.01961v1 )(2)|[AutoNL](https://github.com/LiYingwei/AutoNL ) ![](https://img.shields.io/github/stars/LiYingwei/AutoNL.svg?style=social )|O((H/h\*W/w)\*(D/k)^2)|Autoregressive::x: CustomMask::x:|<details><summary>EXPAND</summary><p>computes Q(KV) and also down samples q, k, v both in spatial and channel dimensions</p></details>|
|[ETC: Encoding Long and Structured Data in Transformers](https://http://arxiv.org/abs/2004.08483v2 )(2)|-|O((N\*g+g^2+N\*k)\*D)|Autoregressive::heavy_check_mark: CustomMask::wavy_dash:|<details><summary>EXPAND</summary><p>combines global attention (star transformer with multiple global tokens) with local attention</p></details>|
|[Real-time Semantic Segmentation with Fast Attention](https://http://arxiv.org/abs/2007.03815v2 )(0)|-|O(N\*D^2)|Autoregressive::x: CustomMask::x:|<details><summary>EXPAND</summary><p>l2_norm(q)*(l2_norm(k)*v)</p></details>|

## Articles

* [A Survey of Long-Term Context in Transformers](https://www.pragmatic.ml/a-survey-of-methods-for-incorporating-long-term-context/)

