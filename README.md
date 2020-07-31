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
|[Generating Wikipedia by Summarizing Long Sequences](https://http://arxiv.org/abs/1801.10198v1 ) (208)|-|O(![formula](https://render.githubusercontent.com/render/math?math=\mathcal{O}({b}\cdot\frac{N}{b}\cdot\frac{N}{{b}\cdot{k}}\cdot{D})))|:x:|<details><summary>EXPAND</summary><p>compresses key and value + blocked attention</p></details>|
|[CCNet: Criss-Cross Attention for Semantic Segmentation](https://http://arxiv.org/abs/1811.11721v2 ) (148)|[CCNet](https://github.com/speedinghzl/CCNet ) ![](https://img.shields.io/github/stars/speedinghzl/CCNet.svg?style=social )|O(![formula](https://render.githubusercontent.com/render/math?math=\mathcal{O}({N}\cdot({H}+{W})\cdot{D})))|:x:|<details><summary>EXPAND</summary><p>each pixel attends to its row and column simultaneously</p></details>|

## Articles

* [A Survey of Long-Term Context in Transformers](https://www.pragmatic.ml/a-survey-of-methods-for-incorporating-long-term-context/)

