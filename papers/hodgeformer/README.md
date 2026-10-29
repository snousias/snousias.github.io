# HodgeFormer: Transformers for Learnable Operators on Triangular Meshes through Data-Driven Hodge Matrices



## Paper & Code availability 

*Project page:* 
<a href="https://hodgeformer.github.io/" target="_blank">https://hodgeformer.github.io/</a>

*Paper:* 
<a href="https://arxiv.org/abs/2509.01839" target="_blank">https://arxiv.org/abs/2509.01839</a>


*Code:* 
<a href="https://github.com/hodgeformer/hodgeformer" target="_blank">https://github.com/hodgeformer/hodgeformer</a>


<!-- *Reviewed on Openreview:* 
<a href="https://openreview.net/forum?id=PCbFYiMhlO" target="_blank">https://openreview.net/forum?id=PCbFYiMhlO</a> -->



## Abstract

Currently, prominent Transformer architectures applied on graphs and meshes for shape analysis tasks employ traditional attention layers that heavily utilize spectral features requiring costly eigenvalue decomposition-based methods. To encode the mesh structure, these methods derive positional embeddings that heavily rely on eigenvalue decomposition based operations, e.g. on the Laplacian matrix, or on heat-kernel signatures, which are then concatenated to the input features.

This paper proposes a novel approach inspired by the explicit construction of the Hodge Laplacian operator in Discrete Exterior Calculus as a product of discrete Hodge operators and exterior derivatives, i.e. $L := \star_0^{-1} d_0^T \star_1 d_0$. We adjust the Transformer architecture in a novel deep learning layer that utilizes the multi-head attention mechanism to approximate Hodge matrices $\star_0, \star_1$ and $\star_2$ and learn families of discrete operators $L$ that act on mesh vertices, edges and faces.

Our approach results in a computationally-efficient architecture that achieves comparable performance in mesh segmentation and classification tasks, through a direct learning framework, while eliminating the need for costly eigenvalue decomposition operations or complex preprocessing operations.

## Problem statement 

Existing methods for 3D mesh analysis using spectral features rely on costly eigendecomposition of Laplacian matrices, creating a computational bottleneck and exhibiting high complexity. 

Alternatives convolutional based methods are often constrained by architectural limitations: some require specific mesh connectivity to construct their operators or use fixed operators that cannot adapt to the underlying data. 

Modern Transformer-based still depend on pre-computed spectral features for positional encoding. This reliance on expensive, rigid, and often complex preprocessing steps limits the efficiency, scalability, and flexibility of deep learning on meshes.


## Core Contribution


This paper proposes a novel approach inspired by the explicit construction of the Hodge Laplacian operator in Discrete Exterior Calculus as a product of discrete Hodge operators and exterior derivatives, i.e. $(L := \star_0^{-1} d_0^T \star_1 d_0)$. We adjust the Transformer architecture in a novel deep learning layer that utilizes the multi-head attention mechanism to approximate Hodge matrices $\star_0$, $\star_1$ and $\star_2$ and learn families of discrete operators $L$ that act on mesh vertices, edges and faces. Our approach results in a computationally-efficient architecture that achieves comparable performance in mesh segmentation and classification tasks, through a direct learning framework, while eliminating the need for costly eigenvalue decomposition operations or complex preprocessing operations. 
 



## Methodology

### Discrete Exterior Calculus Foundation

The mathematical foundation relies on two key DEC constructs:

*Discrete Exterior Derivatives*: Sparse signed incidence matrices that capture topological connectivity:

* $d_0$: maps vertex features to edge features
* $d_1$: maps edge features to face features


*Discrete Hodge Star Operators*: Encode metric information (angles, lengths, areas) and are traditionally represented as diagonal matrices. The paper's key insight is to reinterpret these operators in a data-driven context, learning them as general (non-diagonal) matrices through attention mechanisms.

The Hodge Laplacian operator, which acts on k-forms (features on vertices, edges, or faces), is constructed as:

$$
L_v = \star_0^{-1} d_0^T \star_1 d_0
$$

for vertices, with similar expressions for edges and faces.

### Transformer Model with Hodge Attention

#### 1. Input Feature Construction

##### Vertex Input Features $X_{v_{in}} \in \mathbb{R}^{n_v \times d_{v_{in}}}$

- 3D vertex coordinates $(x, y, z)$
- Vertex normal (weighted average of incident face normals)
- Vertex-associated cell area (weighted average of incident face areas)

##### Edge Input Features $X_{e_{in}} \in \mathbb{R}^{n_e \times d_{e_{in}}}$

- 3D coordinates of the two edge vertices
- 3D coordinates of vertices opposite to the edge (from incident faces)
- Edge normal (average of incident vertex normals)
- Edge lengths of edges belonging to incident faces

##### Face Input Features $X_{f_{in}} \in \mathbb{R}^{n_f \times d_{f_{in}}}$

- 3D coordinates of the three face vertices (ordered by face orientation)
- Face normal vector
- Face area

**Preprocessing**: All meshes are zero-centered and scaled to the unit sphere. During training, random rotations and small perturbations along mesh edges are applied for data augmentation.



#### 2. Adjacency Aggregation Matrices

The adjacency matrices $A_v$, $A_e$, and $A_f$ encode one-hop neighborhood information for each mesh element type. These are constructed via **breadth-first search (BFS)** on the mesh element adjacency structure.

For sparse attention, a sparsity pattern $S_i$ is defined for each element $i$, consisting of:

- $\sqrt{n}$ neighbors total
- 4:1 ratio of local neighbors (from BFS) to random connections



#### 3. Embedding Layer (Equation 13)

The embedding layer transforms input features into latent representations by aggregating one-hop neighborhood information:

$$x_k = \text{MLP}\left(X_{k_{in}} + A_k X_{k_{in}}\right), \quad k \in {v, e, f}$$

where:

- $x_v \in \mathbb{R}^{n_v \times d}$, $x_e \in \mathbb{R}^{n_e \times d}$, $x_f \in \mathbb{R}^{n_f \times d}$ are the latent embeddings
- **MLP** is a **two-layer feedforward network** with:
    - Input dimension: $d_{k_{in}}$ (feature-dependent)
    - Hidden dimension: $d_h = 512$
    - Output dimension: $d = 256$
    - Activation: **ReLU**

$$\text{MLP}(x) = W_2 \cdot \text{ReLU}(W_1 x + b_1) + b_2$$

where $W_1 \in \mathbb{R}^{d_h \times d_{k_{in}}}$, $b_1 \in \mathbb{R}^{d_h}$, $W_2 \in \mathbb{R}^{d \times d_h}$, $b_2 \in \mathbb{R}^{d}$.



#### 4. Query, Key, and Value Projections

For each mesh element type $k \in {v, e, f}$ and each attention head, the embeddings are linearly projected:

$$Q_k = x_k W_{Q_k}, \quad K_k = x_k W_{K_k}, \quad V_k = x_k W_{V_k}$$

where:

- $W_{Q_k}, W_{K_k} \in \mathbb{R}^{d \times d_k}$ with $d_k = d_h / h = 512 / 4 = 64$
- $W_{V_k} \in \mathbb{R}^{d \times d}$ with $d = 256$
- $h = 4$ is the number of attention heads

These are **learnable parameters** initialized using standard PyTorch defaults



#### 5. Sparse Multi-head Attention (Hodge Star Operators)

For each element $i$, sparse attention is computed over its sparsity pattern $S_i$:

$$x_i = \sum_{j \in S_i} A_{ij} V_j$$

where the attention weight is:

$$A_{ij} = \frac{\exp\left(\frac{Q_i K_j^T}{\sqrt{d_k}}\right)}{\sum_{j' \in S_i} \exp\left(\frac{Q_i K_{j'}^T}{\sqrt{d_k}}\right)}$$

This defines the **learned Hodge Star operator** $\star_k$ as:

$$\star_k(x_k) = \sigma\left(\frac{Q_k K_k^T}{\sqrt{d_k}}\right) V_k$$

where $\sigma(\cdot)$ is the **row-wise softmax** function applied over the sparsity pattern.

For the **inverse Hodge Star operators** $\star_k^{-1}$, dedicated separate query and key projections are used.



#### 6. Hodge Laplacian on Vertices (Equation 14 & 17)

The Hodge Laplacian operator for vertices is constructed as:

$$L_v = \star_0^{-1}(x_v) \circ d_0^T \circ \star_1(x_e) \circ d_0$$

Expanding with attention mechanisms:

$$L_v = \sigma\left(\frac{Q_v K_v^T}{\sqrt{d_v}}\right)^{-1} \cdot d_0^T \cdot \sigma\left(\frac{Q_e K_e^T}{\sqrt{d_e}}\right) \cdot d_0$$

where:

- $d_0 \in {-1, 0, 1}^{n_e \times n_v}$ is the **vertex-to-edge incidence matrix** (signed, sparse)
- $d_0^T \in {-1, 0, 1}^{n_v \times n_e}$ is its transpose

The **updated vertex features** are computed by applying the Laplacian to the value vectors:

$$X_v = L_v \cdot V_v(x_v)$$



#### 7. Multi-head Implementation

For $h = 4$ attention heads, the computation is performed in parallel for each head, then concatenated and projected:

$$\text{MultiHead}(x) = \text{Concat}(\text{head}_1, \text{head}_2, \text{head}_3, \text{head}_4) W^O$$

where each head $i$ computes:

$$\text{head}_i = L_v^{(i)} \cdot V_v^{(i)}$$

with separate $W_{Q_v}^{(i)}, W_{K_v}^{(i)}, W_{V_v}^{(i)}$ for each head, and $W^O \in \mathbb{R}^{d \times d}$ is the output projection.



#### 8. Feed-forward Network (Equation 6)

After attention, a position-wise feed-forward network is applied with residual connections:

$$\text{FFN}(x) = W_2 \cdot \text{ReLU}(W_1 x + b_1) + b_2$$

where $W_1 \in \mathbb{R}^{d_h \times d}$, $W_2 \in \mathbb{R}^{d \times d_h}$, with $d_h = 512$.

The complete HodgeFormer layer with residual connections is:

$$H_l(x_v, x_e, x_f) = G_l\left(A_{H_l}(x_v, x_e, x_f)\right) + (x_v, x_e, x_f)$$

where $A_{H_l}$ is the Multi-head Hodge Attention and $G_l$ is the FFN.










## Citation 

```
Nousias, A. and Nousias, S., 2025. HodgeFormer: Transformers for Learnable Operators on Triangular Meshes through Data-Driven Hodge Matrices. arXiv preprint arXiv:2509.01839.
```

```
@article{nousias2025hodgeformer,
  title={HodgeFormer: Transformers for Learnable Operators on Triangular Meshes through Data-Driven Hodge Matrices},
  author={Nousias, Akis and Nousias, Stavros},
  journal={arXiv preprint arXiv:2509.01839},
  year={2025}
}
```