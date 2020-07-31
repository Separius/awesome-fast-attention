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

|date|name|paper(citation_count)|code(github_stars)|main_idea|complexity(Big_O)|autoregressive?|custom_mask?|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|2018/11|Criss Cross Attention|[CCNet: Criss-Cross Attention for Semantic Segmentation](http://arxiv.org/abs/1811.11721v2 )(148)|[CCNet](https://github.com/speedinghzl/CCNet ) ![](https://img.shields.io/github/stars/speedinghzl/CCNet.svg?style=social )|each pixel attends to its row and column simultaneously|O(N\*(H+W)\*D)|:x:|:x:|
|2018/12|Efficient Attention|[Efficient Attention: Attention with Linear Complexities](http://arxiv.org/abs/1812.01243v8 )(2)|[efficient-attention](https://github.com/cmsflash/efficient-attention ) ![](https://img.shields.io/github/stars/cmsflash/efficient-attention.svg?style=social )|softmax(q)(softmax(k)v)|O(N\*D^2)|:x:|:x:|
|2019/04|GCNet|[GCNet: Non-local Networks Meet Squeeze-Excitation Networks and Beyond](http://arxiv.org/abs/1904.11492v1 )(96)|[GCNet](https://github.com/xvjiarui/GCNet ) ![](https://img.shields.io/github/stars/xvjiarui/GCNet.svg?style=social )|squeeze and excitation with an attention pooling (instead of a GAP)|O(N\*D^2)|:x:|:x:|
|2019/07|Interlaced Attention|[Interlaced Sparse Self-Attention for Semantic Segmentation](http://arxiv.org/abs/1907.12273v2 )(13)|IN_PAPER|combination of a short length and then long range(dilated) attention|O(N\*D^2+N\*sqrt(N)\*D)|:heavy_check_mark:|:wavy_dash:|
|2019/11|Compressive Transformer|[Compressive Transformers for Long-Range Sequence Modelling](http://arxiv.org/abs/1911.05507v1 )(20)|[compressive-transformer-pytorch](https://github.com/lucidrains/compressive-transformer-pytorch ) ![](https://img.shields.io/github/stars/lucidrains/compressive-transformer-pytorch.svg?style=social )|compresses distant tokens instead of just stop_grad() ing them, more efficient version of transformerXL|O(N^2\*D)|:heavy_check_mark:|:wavy_dash:|
|2019/11|BP-Transformer|[BP-Transformer: Modelling Long-Range Context via Binary Partitioning](http://arxiv.org/abs/1911.04070v1 )(8)|[BPT](https://github.com/yzh119/BPT ) ![](https://img.shields.io/github/stars/yzh119/BPT.svg?style=social )|attends to distant tokens coarsely and attends to close tokens in a more fine-grained manner|O(N\*k\*log(N/k)\*D)|:heavy_check_mark:|:wavy_dash:|
|2019/12|Axial Attention|[Axial Attention in Multidimensional Transformers](http://arxiv.org/abs/1912.12180v1 )(5)|[axial-attention](https://github.com/lucidrains/axial-attention ) ![](https://img.shields.io/github/stars/lucidrains/axial-attention.svg?style=social )|apply attention on each axis separately|O(N\*(H+W)\*D)|:heavy_check_mark:|:x:|
|2020/02|Transformer on a Diet|[Transformer on a Diet](http://arxiv.org/abs/2002.06170v1 )(2)|[transformer-on-diet](https://github.com/cgraywang/transformer-on-diet ) ![](https://img.shields.io/github/stars/cgraywang/transformer-on-diet.svg?style=social )|dilated transformer like wavenet|O(N\*k\*D)|:heavy_check_mark:|:wavy_dash:|
|2020/03|SAC|[SAC: Accelerating and Structuring Self-Attention via Sparse Adaptive Connection](http://arxiv.org/abs/2003.09833v2 )(1)|-|learns the q, k connections == dynamically creates a sparse attention matrix|O(N\*k\*D)|:heavy_check_mark:|:heavy_check_mark:|
|2020/03|Routing Transformer|[Efficient Content-Based Sparse Attention with Routing Transformers](http://arxiv.org/abs/2003.05997v1 )(11)|[routing-transformer](https://github.com/lucidrains/routing-transformer ) ![](https://img.shields.io/github/stars/lucidrains/routing-transformer.svg?style=social )|computes attention with same-cluster tokens (computed by online k-means)|O(N\*sqrt(N)\*D)|:x:|:x:|
|2020/04|AutoNL|[Neural Architecture Search for Lightweight Non-Local Networks](http://arxiv.org/abs/2004.01961v1 )(2)|[AutoNL](https://github.com/LiYingwei/AutoNL ) ![](https://img.shields.io/github/stars/LiYingwei/AutoNL.svg?style=social )|computes Q(KV) and also down samples q, k, v both in spatial and channel dimensions|O((H/h\*W/w)\*(D/k)^2)|:x:|:x:|
|2020/04|ETC|[ETC: Encoding Long and Structured Data in Transformers](http://arxiv.org/abs/2004.08483v2 )(2)|-|combines global attention (star transformer with multiple global tokens) with local attention|O((N\*g+g^2+N\*k)\*D)|:heavy_check_mark:|:wavy_dash:|
|2020/07|FANet|[Real-time Semantic Segmentation with Fast Attention](http://arxiv.org/abs/2007.03815v2 )(0)|-|l2_norm(q)*(l2_norm(k)*v)|O(N\*D^2)|:x:|:x:|

## Articles

* [A Survey of Long-Term Context in Transformers](https://www.pragmatic.ml/a-survey-of-methods-for-incorporating-long-term-context/)

