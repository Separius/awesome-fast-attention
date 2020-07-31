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

|paper(citation_count)|code(github_stars)|complexity(Big_O)|autoregressive?|custom_mask?|main_idea|
|:---:|:---:|:---:|:---:|:---:|:---:|
|[CCNet: Criss-Cross Attention for Semantic Segmentation](http://arxiv.org/abs/1811.11721v2 )(148)|[CCNet](https://github.com/speedinghzl/CCNet ) ![](https://img.shields.io/github/stars/speedinghzl/CCNet.svg?style=social )|O(N\*(H+W)\*D)|:x:|:x:|each pixel attends to its row and column simultaneously|
|[Efficient Attention: Attention with Linear Complexities](http://arxiv.org/abs/1812.01243v8 )(2)|[efficient-attention](https://github.com/cmsflash/efficient-attention ) ![](https://img.shields.io/github/stars/cmsflash/efficient-attention.svg?style=social )|O(N\*D^2)|:x:|:x:|softmax(q)(softmax(k)v)|
|[GCNet: Non-local Networks Meet Squeeze-Excitation Networks and Beyond](http://arxiv.org/abs/1904.11492v1 )(96)|[GCNet](https://github.com/xvjiarui/GCNet ) ![](https://img.shields.io/github/stars/xvjiarui/GCNet.svg?style=social )|O(N\*D^2)|:x:|:x:|squeeze and excitation with an attention pooling (instead of a GAP)|
|[Interlaced Sparse Self-Attention for Semantic Segmentation](http://arxiv.org/abs/1907.12273v2 )(13)|IN_PAPER|O(N\*D^2+N\*sqrt(N)\*D)|:heavy_check_mark:|:wavy_dash:|combination of a short length and then long range(dilated) attention|
|[Compressive Transformers for Long-Range Sequence Modelling](http://arxiv.org/abs/1911.05507v1 )(20)|[compressive-transformer-pytorch](https://github.com/lucidrains/compressive-transformer-pytorch ) ![](https://img.shields.io/github/stars/lucidrains/compressive-transformer-pytorch.svg?style=social )|O(N^2\*D)|:heavy_check_mark:|:wavy_dash:|compresses distant tokens instead of just stop_grad() ing them, more efficient version of transformerXL|
|[BP-Transformer: Modelling Long-Range Context via Binary Partitioning](http://arxiv.org/abs/1911.04070v1 )(8)|[BPT](https://github.com/yzh119/BPT ) ![](https://img.shields.io/github/stars/yzh119/BPT.svg?style=social )|O(N\*k\*log(N/k)\*D)|:heavy_check_mark:|:wavy_dash:|attends to distant tokens coarsely and attends to close tokens in a more fine-grained manner|
|[Axial Attention in Multidimensional Transformers](http://arxiv.org/abs/1912.12180v1 )(5)|[axial-attention](https://github.com/lucidrains/axial-attention ) ![](https://img.shields.io/github/stars/lucidrains/axial-attention.svg?style=social )|O(N\*(H+W)\*D)|:heavy_check_mark:|:x:|apply attention on each axis separately|
|[Transformer on a Diet](http://arxiv.org/abs/2002.06170v1 )(2)|[transformer-on-diet](https://github.com/cgraywang/transformer-on-diet ) ![](https://img.shields.io/github/stars/cgraywang/transformer-on-diet.svg?style=social )|O(N\*k\*D)|:heavy_check_mark:|:wavy_dash:|dilated transformer like wavenet|
|[SAC: Accelerating and Structuring Self-Attention via Sparse Adaptive Connection](http://arxiv.org/abs/2003.09833v2 )(1)|-|O(N\*k\*D)|:heavy_check_mark:|:heavy_check_mark:|learns the q, k connections == dynamically creates a sparse attention matrix|
|[Efficient Content-Based Sparse Attention with Routing Transformers](http://arxiv.org/abs/2003.05997v1 )(11)|[routing-transformer](https://github.com/lucidrains/routing-transformer ) ![](https://img.shields.io/github/stars/lucidrains/routing-transformer.svg?style=social )|O(N\*sqrt(N)\*D)|:x:|:x:|computes attention with same-cluster tokens (computed by online k-means)|
|[Neural Architecture Search for Lightweight Non-Local Networks](http://arxiv.org/abs/2004.01961v1 )(2)|[AutoNL](https://github.com/LiYingwei/AutoNL ) ![](https://img.shields.io/github/stars/LiYingwei/AutoNL.svg?style=social )|O((H/h\*W/w)\*(D/k)^2)|:x:|:x:|computes Q(KV) and also down samples q, k, v both in spatial and channel dimensions|
|[ETC: Encoding Long and Structured Data in Transformers](http://arxiv.org/abs/2004.08483v2 )(2)|-|O((N\*g+g^2+N\*k)\*D)|:heavy_check_mark:|:wavy_dash:|combines global attention (star transformer with multiple global tokens) with local attention|
|[Real-time Semantic Segmentation with Fast Attention](http://arxiv.org/abs/2007.03815v2 )(0)|-|O(N\*D^2)|:x:|:x:|l2_norm(q)*(l2_norm(k)*v)|

## Articles

* [A Survey of Long-Term Context in Transformers](https://www.pragmatic.ml/a-survey-of-methods-for-incorporating-long-term-context/)

