# awesome-fast-attention [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of efficient attention modules

## Table of Contents

* **[About This Repo](#about-this-repo)**
* **[Efficient Attention](#efficient-attention)**
* **[Articles](#articles)**

## About This Repo

* WIP

## Efficient Attention

|Paper (citations)|Code|Complexity|AutoRegressive|Main Idea|
|:---:|:---:|:---:|:---:|:---:|
|[Generating Wikipedia by Summarizing Long Sequences](https://http://arxiv.org/abs/1801.10198v1 ) (208)|-|![formula](https://render.githubusercontent.com/render/math?math=\mathcal{O}({b}\cdot\frac{N}{b}\cdot\frac{N}{{b}\cdot{k}}\cdot{D}))|:x:|<details><summary>EXPAND</summary><p>compresses key and value + blocked attention</p></details>|
|[CCNet: Criss-Cross Attention for Semantic Segmentation](https://http://arxiv.org/abs/1811.11721v2 ) (148)|[CCNet](https://github.com/speedinghzl/CCNet ) ![](https://img.shields.io/github/stars/speedinghzl/CCNet.svg?style=social )|![formula](https://render.githubusercontent.com/render/math?math=\mathcal{O}({N}\cdot({H}%2b{W})\cdot{D}))|:x:|<details><summary>EXPAND</summary><p>each pixel attends to its row and column simultaneously</p></details>|
|[Efficient Attention: Attention with Linear Complexities](https://http://arxiv.org/abs/1812.01243v8 ) (2)|[efficient-attention](https://github.com/cmsflash/efficient-attention ) ![](https://img.shields.io/github/stars/cmsflash/efficient-attention.svg?style=social )|![formula](https://render.githubusercontent.com/render/math?math=\mathcal{O}(N\cdotD^2))|:x:|<details><summary>EXPAND</summary><p>Softmax({Q})*(Softmax({K}^{T})*V)</p></details>|
|[Generating Long Sequences with Sparse Transformers](https://http://arxiv.org/abs/1904.10509v1 ) (138)|[torch-blocksparse](https://github.com/ptillet/torch-blocksparse ) ![](https://img.shields.io/github/stars/ptillet/torch-blocksparse.svg?style=social )|![formula](https://render.githubusercontent.com/render/math?math=\mathcal{O}({N}\cdot\sqrt{N}\cdot{D}))|:heavy_check_mark:|<details><summary>EXPAND</summary><p>sparse block based attention</p></details>|
|[GCNet: Non-local Networks Meet Squeeze-Excitation Networks and Beyond](https://http://arxiv.org/abs/1904.11492v1 ) (96)|[GCNet](https://github.com/xvjiarui/GCNet ) ![](https://img.shields.io/github/stars/xvjiarui/GCNet.svg?style=social )|![formula](https://render.githubusercontent.com/render/math?math=\mathcal{O}({N}\cdot{D}^2))|:x:|<details><summary>EXPAND</summary><p>squeeze and excitation with an attention pooling (instead of a GAP)</p></details>|
|[Interlaced Sparse Self-Attention for Semantic Segmentation](https://http://arxiv.org/abs/1907.12273v2 ) (13)|IN_PAPER|![formula](https://render.githubusercontent.com/render/math?math=\mathcal{O}({N}\cdot{D}^2%2b{N}\cdot\sqrt{N}\cdot{D}))|:heavy_check_mark:|<details><summary>EXPAND</summary><p>combination of a short length and then long range(dilated) attention</p></details>|
|[Expectation-Maximization Attention Networks for Semantic Segmentation](https://http://arxiv.org/abs/1907.13426v2 ) (38)|[EMANet](https://github.com/XiaLiPKU/EMANet ) ![](https://img.shields.io/github/stars/XiaLiPKU/EMANet.svg?style=social )|![formula](https://render.githubusercontent.com/render/math?math=\mathcal{O}({N}\cdot{k}\cdot{D}))|:x:|<details><summary>EXPAND</summary><p>applys expectation maximization to cluster keys into k clusters</p></details>|
|[Compressive Transformers for Long-Range Sequence Modelling](https://http://arxiv.org/abs/1911.05507v1 ) (20)|[compressive-transformer-pytorch](https://github.com/lucidrains/compressive-transformer-pytorch ) ![](https://img.shields.io/github/stars/lucidrains/compressive-transformer-pytorch.svg?style=social )|![formula](https://render.githubusercontent.com/render/math?math=\mathcal{O}({N}^2\cdot{D}))|:heavy_check_mark:|<details><summary>EXPAND</summary><p>compresses distant tokens instead of just stop_grad() ing them, more efficient version of transformerXL</p></details>|
|[BP-Transformer: Modelling Long-Range Context via Binary Partitioning](https://http://arxiv.org/abs/1911.04070v1 ) (8)|[BPT](https://github.com/yzh119/BPT ) ![](https://img.shields.io/github/stars/yzh119/BPT.svg?style=social )|![formula](https://render.githubusercontent.com/render/math?math=\mathcal{O}({N}\cdot{k}\cdot\log(\frac{N}{k})\cdot{D}))|:heavy_check_mark:|<details><summary>EXPAND</summary><p>attends to distant tokens coarsely and attends to close tokens in a more fine-grained manner</p></details>|

## Articles

* [A Survey of Long-Term Context in Transformers](https://www.pragmatic.ml/a-survey-of-methods-for-incorporating-long-term-context/)

