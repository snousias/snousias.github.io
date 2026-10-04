---
layout: page
permalink: /computer-vision/
title: vision
description: A research synthesis of computer vision, 2016-2026 - the task taxonomy, the shared pipeline and objective template, the key innovations era by era, and the six mechanisms that recur across all of them.
nav: true
nav_order: 6
toc:
  sidebar: left
---

<!-- _pages/computer_vision.md - generated from the website-cv static site -->

## Overview {#cv-overview}

#### What this is {#cv-overview--what}

This site is a structured analysis of the computer-vision research record, assembled from a set of working notes covering two things that are usually kept apart:

- A **systematic treatment of the field itself** — the task taxonomy, the shared processing pipeline, the objective template that unifies classical and learned methods, the loss and regularizer vocabulary, and the practical mechanisms that make any of it work on real data.
- A **chronological account of the key innovations** from 2016 to 2026, era by era, with the original papers' own figures and the mechanism behind each result.

The organising claim is that these two are the same material viewed from different angles. Every innovation in the timeline is a new answer to a question the taxonomy already poses: where does supervision come from, how is correspondence represented, what prior resolves the remaining ambiguity, what does the output interface look like.

> **The distinction that saves the most confusion**
> A **loss** measures disagreement during training. A **residual** is the per-sample quantity the loss consumes. A **regularizer** encodes a prior. A **constraint** must hold exactly. A **metric** is the reported quantity, and it is rarely the loss that was optimised. Detection trains boxes with Smooth L1 and is evaluated with IoU; segmentation trains with pixelwise cross-entropy and is evaluated with mean IoU or Dice.

#### The five questions the decade answered {#cv-overview--questions}

- **1 · How deep can a network be?** — **Answered 2016**, then it stopped being interesting. Residual connections made depth free, and architecture ceased to be the binding constraint.

- **2 · Where does supervision come from?** — **2019–2023.** Contrastive → masked modelling → self-distillation → synthetic teachers → model-in-the-loop data engines.

- **3 · What is the output interface?** — **2020–2025.** Dense grid + NMS → set prediction → promptable, open-vocabulary output.

- **4 · How is geometry represented?** — **2020–2025.** Implicit neural fields → explicit primitives → feed-forward any-view prediction.

- **5 · How is the image distribution modelled?** — **2018–2024.** Adversarial → denoising diffusion → latent diffusion → flow matching and few-step sampling.

- **Still open** — Calibrated uncertainty, compositional and geometric reasoning, evaluation that survives distribution shift, and video as a model of dynamics, not of appearance alone.

#### The ten-year arc {#cv-overview--arc}

Seven overlapping eras. The names describe what became _possible_ in each window, not when the first paper appeared — the eras overlap heavily in time.

- [**2016–2018** — Depth & detection](#cv-depth-detection-and-the-first-believable-images)
- [**2018–2020** — Scale & self-supervision](#cv-scale-self-supervision-and-set-prediction)
- [**2020–2022** — Transformer takeover](#cv-the-transformer-takeover)
- [**2022–2023** — Foundation & prompting](#cv-foundation-models-and-the-promptable-paradigm)
- [**2023–2024** — 3D & multimodal](#cv-3d-becomes-real-time-vision-learns-to-talk)
- [**2024–2025** — Video, depth, concepts](#cv-video-depth-and-concepts)
- [**2025–2026** — Any-view geometry](#cv-any-view-geometry-concepts-and-embodiment)

| Era                                                                  | Binding constraint attacked                                          | Representative results                                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| [**2016–2018**](#cv-depth-detection-and-the-first-believable-images) | Network depth; detection speed–accuracy; dense-prediction resolution | ResNet, FPN, Faster/Mask R-CNN, YOLO, SSD, focal loss, MobileNet, ProGAN, StyleGAN                  |
| [**2018–2020**](#cv-scale-self-supervision-and-set-prediction)       | Label cost; principled scaling; hand-designed post-processing        | EfficientNet, MoCo, SimCLR, BYOL, SwAV, panoptic + PQ, SlowFast, RAFT, StyleGAN2, DETR              |
| [**2020–2022**](#cv-the-transformer-takeover)                        | Architectural inductive bias; generation cost                        | ViT, DeiT, Swin, SegFormer, CLIP, DINO, BEiT, MAE, DDPM, classifier-free guidance, Latent Diffusion |
| [**2022–2023**](#cv-foundation-models-and-the-promptable-paradigm)   | The closed class vocabulary; task-specific architectures             | ConvNeXt (+V2), Mask2Former, OWL-ViT, Grounding DINO, DINOv2, SAM, ControlNet, SDXL                 |
| [**2023–2024**](#cv-3d-becomes-real-time-vision-learns-to-talk)      | Implicit 3D rendering cost; the vision–language interface            | 3D Gaussian Splatting, LLaVA, SAM 2, YOLOv9/v10, consistency models, flow matching                  |
| [**2024–2025**](#cv-video-depth-and-concepts)                        | Temporal coherence; dense-feature degradation at scale               | Sora, Depth Anything V2, DINOv3, YOLO11, Qwen2.5-VL, InternVL                                       |
| [**2025–2026**](#cv-any-view-geometry-concepts-and-embodiment)       | Multi-view optimisation pipelines; geometric prompting               | VGGT, Depth Anything 3, SAM 3, SAM 3D, RF-DETR, YOLO26, embodied VLMs                               |

#### Six mechanisms that recur {#cv-overview--mechanisms}

Forty papers, six recurring mechanisms. Each is treated in full on the [synthesis page](#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid).

- **[1 · Make the easy path identity](#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--m1)** — A block that can do nothing at zero cost makes depth — and later, adaptation — safe.<br>`ResNet → ControlNet zero-convs → adaLN-Zero → LoRA`

- **[2 · Predict a set, not a grid](#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--m2)** — Move duplicate suppression out of inference and into the loss.<br>`DETR → Mask2Former → YOLOv10 → YOLO26 → RF-DETR`

- **[3 · Manufacture the supervision](#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--m3)** — Signal constructed by contrast, masking, distillation or synthesis.<br>`MoCo → MAE → DINOv2/v3 → Depth Anything`

- **[4 · Work in a latent space](#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--m4)** — Compress perceptually irrelevant detail away, then do the hard work cheaply.<br>`Latent Diffusion → DiT → Sora`

- **[5 · Heavy encoder, cheap head](#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--m5)** — Encode once, answer many queries.<br>`SAM → SAM 2/3 → frozen-backbone probing`

- **[6 · Return to explicit primitives](#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--m6)** — Where implicit representations are slow, go back to primitives.<br>`NeRF → 3D Gaussian Splatting`

#### The output interface, in three steps {#cv-overview--interface}

The clearest single progression in the decade. Each step removes a hand-designed component: the proposal generator, then the duplicate filter, then the fixed class list.

- **Dense enumeration 2014–2019** — Anchors or grid cells, a score threshold, and non-maximum suppression. Three hand-tuned components, each with dataset-specific hyperparameters.

- **Set prediction 2020–2024** — A fixed number of queries and a bipartite matching loss. Duplicate suppression is trained into the loss, so the NMS stage is removed.

- **Promptable output 2023–** — A point, box, mask or noun phrase selects what to segment or detect. The vocabulary is open and chosen at query time.

#### Where to go next {#cv-overview--map}

- **[Task taxonomy](#cv-the-master-task-taxonomy)** — Twelve task families with inputs and outputs, how they depend on each other, and why the field is better organised as inverse problems than as architectures.

- **[Pipeline & objectives](#cv-the-shared-pipeline-and-the-objective-template)** — The ten-step pipeline shared by classical and learned systems, the common objective template, and the full data-term and regularizer vocabulary.

- **[Photometric consistency](#cv-photometric-consistency)** — The warp-and-compare principle in depth: the equations, the six assumptions it rests on, and the ecosystem of tricks that make it survive real data.

- **[The atlas — 29 modules](#cv-the-atlas-29-modules)** — Every topic with its own page: calibration, restoration, primitives, correspondence, detection, segmentation, keypoints, flow, stereo, SLAM, tracking, video, point clouds, rendering, generation and vision–language.

- **[Losses & regularization](#cv-losses-and-regularization)** — The complete objective vocabulary, organised by what each loss assumes — plus multi-task weighting, uncertainty, and the surrogate–metric gap.

- **[Cross-cutting practice](#cv-cross-cutting-mechanisms-and-failure-modes)** — Robust estimation, multiscale processing, the seven consistency constraints, augmentation, imbalance, post-processing — and a twelve-row failure-mode checklist.

- **[Synthesis](#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid)** — The six mechanisms in full, the supervision ladder, the architectural outcomes, the limits of the benchmarks, and the open problems entering 2026.

- **[Paper index](#cv-paper-index)** — Every paper on this site in one searchable, sortable table — filterable by era and by the mechanism it exemplifies, with arXiv links.

- **[Curriculum](#cv-a-29-module-curriculum)** — A 29-module teaching sequence derived from the taxonomy, with the recommended production order and a consistent per-module template.

#### The central conclusion {#cv-overview--conclusion}

The unifying idea is that computer-vision methods are combinations of **representation + correspondence + constraint + robust optimisation**. Deep learning changes the representation and often learns parts of matching or inference, but the classical constraints remain plainly visible in modern systems:

- Photometric warping supervises depth and neural rendering.
- Reprojection error drives calibration and bundle adjustment.
- Smoothness regularizes flow and geometry.
- Pyramids handle scale — as image pyramids, FPNs, U-Net skips, or hierarchical transformers.
- RANSAC and robust losses handle outliers.
- Cost volumes represent correspondence.
- Consistency checks handle ambiguity.

Treating these elements explicitly produces a more durable understanding than studying network names in isolation — which is the reason this site is organised the way it is.

## Foundations

### The master task taxonomy {#cv-the-master-task-taxonomy}

_This page organises computer vision as a family of **inverse problems**: infer scene properties from measurements produced by cameras or related sensors._

#### Purpose and scope {#cv-the-master-task-taxonomy--scope}

The properties being inferred are appearance, geometry, motion, identity, semantics, or physical state. The measurements come from one or more cameras or related sensors. That framing — measurement in, scene property out — is what makes otherwise unrelated tasks comparable.

A complete treatment of any task therefore needs **five layers**. Skipping any one of them produces the familiar failure of a method that works on a benchmark and nowhere else:

- **1 · Input and desired output** — What is measured, and what must be estimated. Fixes the observability question before any method is chosen.

- **2 · Image-formation assumptions** — What physical model links the scene to the measurement — projection, reflectance, exposure, sampling, noise.

- **3 · Processing pipeline** — The sequence of representation, hypothesis generation, scoring and inference.

- **4 · Objective or loss** — What is being minimised, on which residuals, under which priors — and how that relates to the metric actually reported.

- **5 · Practical mechanisms** — How ambiguity, noise, occlusion and computational limits are handled. In practice this layer decides whether a method survives contact with real data.

> **Loss, residual, regularizer, constraint, metric — not interchangeable**
> These five words are used loosely in the literature and the confusion is expensive. Precisely:
>
> - **Residual** — the per-observation discrepancy `r<sub>i</sub>(θ)` between prediction and measurement.
> - **Loss** — the aggregate scalar minimised during training, built by passing residuals through a penalty and summing.
> - **Regularizer** — a term that encodes a prior and resolves what the data term leaves underdetermined.
> - **Constraint** — a condition that must hold exactly, not be traded off against other terms.
> - **Metric** — what is reported at evaluation, frequently non-differentiable and frequently _not_ the training loss.
>
> Classical vision minimises an explicit energy over _scene variables_; deep vision minimises a training objective over _network parameters_; post-processing may solve a separate _discrete_ optimisation. Object detection trains box coordinates with Smooth L1 while being evaluated with IoU. Semantic segmentation trains with pixelwise cross-entropy while being evaluated with mean IoU or Dice. The gap between surrogate and metric is a design decision, and usually an unexamined one.

#### Twelve task families {#cv-the-master-task-taxonomy--families}

The authoritative curriculum spans image formation; filtering and multiscale processing; feature detection and matching; segmentation; alignment; structure from motion; dense motion; stitching; computational photography; stereo; 3D reconstruction; recognition; video understanding; and vision–language systems. In 3D vision the corresponding core tasks are classification, segmentation, detection, tracking, reconstruction, registration, completion and 6-DoF pose estimation. Organised by _what is estimated_, they collapse into twelve families.

| Family                           | Principal tasks                                                                         | Typical input                      | Typical output                                                       |
| -------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------- | -------------------------------------------------------------------- |
| **Measurement & calibration**    | Camera calibration, radiometric calibration, synchronization, rectification             | Calibration images, sensor streams | Intrinsics, distortion, extrinsics, response curves, aligned sensors |
| **Low-level vision**             | Denoising, deblurring, demosaicing, enhancement, super-resolution, inpainting           | One or more corrupted images       | Restored or enhanced image                                           |
| **Primitive extraction**         | Edges, corners, blobs, lines, contours, regions, descriptors                            | Image                              | Sparse primitives, region proposals, descriptors                     |
| **Correspondence & alignment**   | Feature matching, registration, homography, stitching                                   | Image pair or set                  | Correspondences and transformation                                   |
| **Recognition**                  | Classification, retrieval, verification, re-identification, OCR                         | Image or crop                      | Class, identity, text, embedding, ranking                            |
| **Localization**                 | Object detection, landmark detection, 2D pose                                           | Image                              | Boxes, centers, keypoints, confidence                                |
| **Pixel understanding**          | Semantic, instance, panoptic segmentation; matting                                      | Image                              | Class map, object masks, alpha matte                                 |
| **Motion & time**                | Optical flow, scene flow, tracking, action recognition, event detection                 | Video or temporal sensors          | Motion field, tracks, action/event labels                            |
| **Geometry**                     | Stereo, monocular depth, MVS, SfM, visual odometry, SLAM                                | Multiple views, video, RGB-D       | Depth, camera poses, sparse/dense map                                |
| **3D perception**                | Point-cloud classification/detection/segmentation, registration, completion, 6-DoF pose | Point cloud, RGB-D, LiDAR          | 3D labels, boxes, transforms, completed geometry                     |
| **Rendering & generation**       | Novel-view synthesis, NeRF, image synthesis, translation, editing                       | Posed images, text, latent code    | Rendered or generated visual content                                 |
| **Scene & multimodal reasoning** | Scene graphs, VQA, captioning, grounding, open-vocabulary recognition                   | Images/video plus language         | Relations, answers, captions, grounded regions                       |

#### How the families depend on each other {#cv-the-master-task-taxonomy--dependencies}

These tasks are not independent, and the dependency structure explains why progress propagates the way it does — an improvement in a foundational family shows up months later in several downstream ones.

> **Upstream enablers**
>
> - **Calibration** supports stereo, pose, SfM and any metric measurement.
> - **Feature matching** underlies registration, stitching, SfM, localization and loop closure.
> - **Detection** feeds tracking, which feeds action and event analysis.
> - **Optical flow** supports tracking and temporal aggregation.

> **Downstream consumers**
>
> - **Depth and pose** feed view synthesis and reconstruction.
> - **Segmentation** supports measurement, reconstruction and editing.
> - **Reconstruction** feeds simulation, rendering and embodied reasoning.
> - **Recognition** feeds retrieval, grounding and scene reasoning.

> **Why this matters for reading the timeline**
> ResNet's effect was not confined to classification. Because recognition backbones sit upstream of detection, segmentation, depth and tracking, a better backbone improved all of them at once without any of those subfields changing their own methods. The same structural argument explains CLIP (a text-aligned encoder unlocked open-vocabulary detection and segmentation), DINOv2/v3 (frozen dense features unlocked depth and tracking probes), and SAM (a promptable mask model became a component in other people's pipelines). **Innovations in upstream families produce field-wide step changes; innovations in downstream families do not.**

#### Reading the taxonomy against the timeline {#cv-the-master-task-taxonomy--reading}

Each era in the [chronological account](#cv-overview--arc) can be read as pressure applied at a particular point in this table:

- **2016–2018** worked mostly on _localization_ and _pixel understanding_, with the backbone improvements in _recognition_ spilling into both.
- **2018–2020** attacked the _supervision_ requirement common to all families, and rebuilt the _localization_ output interface with set prediction.
- **2020–2022** replaced the representation layer across every family at once, and moved _rendering and generation_ from adversarial to diffusion training.
- **2022–2023** removed the closed class vocabulary from _recognition_, _localization_ and _pixel understanding_ simultaneously.
- **2023–2026** rebuilt _geometry_ and _3D perception_ — first the representation (splatting), then the inference procedure (feed-forward any-view prediction).

Notice which family has been least disturbed: _measurement and calibration_. The physical model of image formation has not been learned away, and every geometric method on this site still depends on it being right.

### Image formation and cameras {#cv-image-formation-and-cameras}

_Every inverse problem in vision is inverting \_this_ forward model. Getting it wrong produces bias, not noise — and bias does not average away with more data.\_

#### The pinhole camera model {#cv-image-formation-and-cameras--pinhole}

A point $$\mathbf{X}_w = (X, Y, Z)^\top$$ in the world is mapped to a pixel $$\mathbf{u} = (u, v)^\top$$ by a rigid transform into the camera frame followed by a perspective division and an affine map into pixels.

**Full projection, homogeneous form**

$$ s\begin{bmatrix} u \\ v \\ 1 \end{bmatrix} \;=\; \mathbf{K}\,[\,\mathbf{R} \mid \mathbf{t}\,]\begin{bmatrix} X \\ Y \\ Z \\ 1 \end{bmatrix} \;=\; \mathbf{P}\,\tilde{\mathbf{X}}\_w $$

- $$\mathbf{K}$$ — intrinsics (3×3, upper triangular)
- $$\mathbf{R},\mathbf{t}$$ — extrinsics: world→camera rotation and translation
- $$s$$ — the homogeneous scale, equal to the camera-frame depth $$Z_c$$
- $$\mathbf{P}$$ — the 3×4 camera matrix, 11 degrees of freedom

**Intrinsic matrix**

$$ \mathbf{K} = \begin{bmatrix} f_x & \gamma & c_x \\ 0 & f_y & c_y \\ 0 & 0 & 1 \end{bmatrix} $$

_$$f_x, f_y$$ are focal length in pixels (they differ only if pixels are non-square); $$(c_x, c_y)$$ is the principal point; $$\gamma$$ is skew and is essentially always $$0$$ on real sensors. Note $$f_x = f \cdot s_x$$ where $$f$$ is metres and $$s_x$$ is pixels per metre — **focal length in pixels is not a physical property of the lens alone**, which is why it changes when the image is resized._

> **Consequences of resizing and cropping**
> Scaling an image by $$\alpha$$ scales $$f_x, f_y, c_x, c_y$$ by $$\alpha$$. Cropping shifts $$c_x, c_y$$ by the crop offset, and leaves $$f$$ unchanged. Neither is optional bookkeeping: an augmentation pipeline that resizes images without updating $$\mathbf{K}$$ silently trains the network on an inconsistent camera. This is the most common [geometry-aware augmentation](#cv-cross-cutting-mechanisms-and-failure-modes--augmentation) bug.

#### Perspective projection and its consequences {#cv-image-formation-and-cameras--projection}

Dropping to inhomogeneous coordinates, with $$(X_c, Y_c, Z_c)$$ the point in camera coordinates:

$$ u = f_x\frac{X_c}{Z_c} + c_x, \qquad v = f_y\frac{Y_c}{Z_c} + c_y $$

The division by $$Z_c$$ is what makes vision hard. Three consequences follow directly:

- **Depth is unobservable from one view.** Any point on the ray $$\lambda\,\mathbf{K}^{-1}\tilde{\mathbf{u}}$$, $$\lambda > 0$$, produces the same pixel. Monocular depth is therefore a _prior_, not a measurement.
- **Scale ambiguity.** Scaling the whole scene and the translation by the same factor, $$(\mathbf{X} \to k\mathbf{X},\ \mathbf{t} \to k\mathbf{t})$$, leaves every image unchanged. Monocular SfM and SLAM recover geometry only up to one global scale.
- **Depth resolution degrades quadratically.** For a stereo baseline $$B$$, $$Z = f B / d$$ with disparity $$d$$, so $$\;\partial Z/\partial d = -fB/d^2 = -Z^2/(fB)$$. A fixed disparity error produces a depth error growing as $$Z^2$$ — the reason [everything is parameterised in inverse depth](#cv-stereo-and-depth-estimation--inverse-depth).

> **Weak perspective and when it is safe**
> If the scene's depth range $$\Delta Z$$ is small relative to its distance $$\bar Z$$, then $$1/Z \approx 1/\bar Z$$ is constant and projection becomes _affine_: $$u \approx (f_x/\bar Z)X_c + c_x$$. This is why distant planar scenes can be aligned with an affine or homography warp rather than a full 3D model — and why [choosing the simplest valid transform](#cv-correspondence-and-registration--models) matters.

#### Coordinate frames and rigid motion {#cv-image-formation-and-cameras--frames}

The rigid transform lives in $$SE(3)$$, with rotation in $$SO(3)$$. The composition $$\mathbf{T}_{wc} = \mathbf{T}_{wb}\mathbf{T}_{bc}$$ chains body-to-camera and world-to-body. Four parameterisations of rotation are in common use, and the choice matters for optimisation:

| Parameterisation                  | Size      | Property                                                                                  | Use                              |
| --------------------------------- | --------- | ----------------------------------------------------------------------------------------- | -------------------------------- |
| Rotation matrix $$\mathbf{R}$$    | 9 (3 DoF) | Over-parameterised; needs $$\mathbf{R}^\top\mathbf{R}=\mathbf{I}$$, $$\det\mathbf{R}=1$$  | Composition, transforming points |
| Euler angles                      | 3         | Minimal but has **gimbal lock**; not a global chart                                       | Human-readable output only       |
| Unit quaternion $$\mathbf{q}$$    | 4 (3 DoF) | Double cover ($$\mathbf{q}$$ and $$-\mathbf{q}$$ are the same rotation); no singularities | Interpolation, state vectors     |
| Axis–angle / $$\mathfrak{so}(3)$$ | 3         | Minimal local chart via $$\exp$$/$$\log$$                                                 | **Optimisation increments**      |

**Exponential map (Rodrigues)**

$$ \mathbf{R} = \exp([\boldsymbol{\omega}]_\times) = \mathbf{I} + \frac{\sin\theta}{\theta}[\boldsymbol{\omega}]_\times + \frac{1-\cos\theta}{\theta^2}[\boldsymbol{\omega}]\_\times^2, \qquad \theta = \lVert\boldsymbol{\omega}\rVert $$

_Optimisers update rotations \_on the manifold_: $$\mathbf{R} \leftarrow \mathbf{R}\exp([\delta\boldsymbol{\omega}]_\times)$$ with a 3-vector increment, rather than perturbing 9 matrix entries and re-orthonormalising. This is what "Lie-algebra increments" means in a bundle-adjustment implementation, and it is why the Jacobians are 3-column rather than 9-column.\_

#### Lens distortion {#cv-image-formation-and-cameras--distortion}

Real lenses violate the pinhole model. The standard Brown–Conrady model applies a polynomial correction in _normalised_ coordinates $$(x, y) = (X_c/Z_c,\ Y_c/Z_c)$$, **before** multiplication by $$\mathbf{K}$$:

**Radial and tangential distortion**

$$ \begin{aligned} x*d &= x\underbrace{(1 + k_1 r^2 + k_2 r^4 + k_3 r^6)}*{\text{radial}} + \underbrace{2p*1 xy + p_2(r^2 + 2x^2)}*{\text{tangential}} \\ y_d &= y(1 + k_1 r^2 + k_2 r^4 + k_3 r^6) + p_1(r^2 + 2y^2) + 2p_2 xy \end{aligned} $$

_with $$r^2 = x^2 + y^2$$. Radial terms model barrel ($$k_1<0$$) and pincushion ($$k_1>0$$); tangential terms model a lens not parallel to the sensor. Because the correction scales with $$r$$, **distortion is only observable away from the image centre** — the reason calibration targets must cover the periphery._

For wide-angle and fisheye lenses the polynomial model breaks down, because the field of view approaches or exceeds $$180°$$ and $$\tan$$ diverges. Fisheye models parameterise the _angle_ instead:

**Equidistant fisheye**

$$ r_d = f\,\theta(1 + k_1\theta^2 + k_2\theta^4 + k_3\theta^6 + k_4\theta^8), \qquad \theta = \arctan(r) $$

_Other standard fisheye projections: stereographic $$r = 2f\tan(\theta/2)$$, orthographic $$r = f\sin\theta$$, equisolid $$r = 2f\sin(\theta/2)$$. Choosing the wrong family produces a residual that no amount of polynomial refinement removes._

#### Radiometry, reflectance and exposure {#cv-image-formation-and-cameras--radiometry}

Geometry says _where_ a point lands; radiometry says _how bright_ it is. The recorded value is the end of a chain, each stage of which some method depends on:

**Irradiance to pixel value**

$$ I = f\!\left(\,t \cdot \frac{\pi}{4}\left(\frac{d}{f\_{\text{len}}}\right)^{2}\!\cos^4\alpha \cdot L \;+\; n \right) $$

- $$L$$ — scene radiance toward the camera
- $$t$$ — exposure time
- $$\cos^4\alpha$$ — natural vignetting — off-axis rays are attenuated
- $$n$$ — noise (see below)
- $$f(\cdot)$$ — the camera response function, typically non-linear (gamma-like)

##### The Lambertian assumption {#cv-image-formation-and-cameras--lambert}

A Lambertian surface has radiance independent of viewing direction:

$$ L*o = \frac{\rho}{\pi}\!\int*\Omega L_i(\boldsymbol{\omega}\_i)\,(\mathbf{n}\cdot\boldsymbol{\omega}\_i)\,d\boldsymbol{\omega}\_i \qquad\Longrightarrow\qquad L_o \ \text{independent of}\ \boldsymbol{\omega}\_o $$

> **This single assumption underwrites most of geometric vision**
> Brightness constancy in [optical flow](#cv-optical-flow-and-scene-flow), the matching cost in [stereo](#cv-stereo-and-depth-estimation), the photometric residual in [self-supervised depth and direct SLAM](#cv-photometric-consistency), and the RGB loss in [neural rendering](#cv-neural-rendering-and-novel-views) all assume a point looks the same from two viewpoints. Specularities, transparency, subsurface scattering and retro-reflection all violate it — and they do so _silently_, producing confident wrong geometry rather than a flagged failure.

##### Sensor noise {#cv-image-formation-and-cameras--noise}

Noise is not additive Gaussian with constant variance. It is dominated by photon shot noise, which is Poisson and therefore _signal-dependent_:

**Heteroscedastic noise model**

$$ \sigma^2(I) = a\,I + b $$

_$$a$$ captures shot noise (proportional to the number of photons, hence to intensity), $$b$$ captures read noise and dark current (constant). Denoisers and uncertainty-weighted losses trained on constant-$$\sigma$$ Gaussian noise systematically under-perform on real raw data, which is the argument for [training on realistic degradations](#cv-restoration-and-enhancement--tricks)._

#### Rolling shutter and motion blur {#cv-image-formation-and-cameras--temporal}

> **Rolling shutter**
> CMOS sensors expose rows sequentially. Row $$r$$ is captured at $$t_r = t_0 + r\,\tau$$, so each row sees a _different_ camera pose: $$\mathbf{u}_r = \pi\big(\mathbf{K}\,\mathbf{T}(t_0 + r\tau)\,\mathbf{X}\big)$$ A single image no longer corresponds to one projection matrix. Ignoring this under fast motion produces skew, wobble and a systematic bias in estimated pose — which is why [rolling-shutter models](#cv-camera-pose-sfm-vo-and-slam--tricks) appear in any serious VO system on a phone or drone.

> **Motion blur**
> A finite exposure integrates the scene over camera motion: $$ I*{\text{blur}}(\mathbf{u}) = \frac{1}{t}\int_0^{t} I\big(\mathbf{W}(\mathbf{u};\boldsymbol{\theta}(s))\big)\,ds $$ This is a \_spatially varying* convolution whenever the motion is not a pure translation, which is what makes blind deblurring hard. See [deblurring](#cv-restoration-and-enhancement--deblur).

#### Failure modes {#cv-image-formation-and-cameras--failures}

| Assumption violated             | Symptom                                                                 | Remedy                                                                    |
| ------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Pinhole (distortion unmodelled) | Straight lines curve; reprojection error grows toward the periphery     | Brown–Conrady or fisheye model; undistort before rectification            |
| Wrong distortion family         | Residual that will not reduce no matter how many coefficients are added | Switch to a fisheye/angle-based projection                                |
| Global shutter                  | Skewed verticals, wobbling trajectory under fast motion                 | Per-row pose model; IMU-aided interpolation                               |
| Lambertian reflectance          | Depth spikes on specular highlights; flow fails on glass and water      | Robust penalties, visibility masks, multi-view minimum, polarisation cues |
| Constant exposure               | Photometric residual large despite correct geometry                     | Affine brightness model $$I' = aI + b$$; census/gradient costs            |
| Homoscedastic noise             | Over-smoothing in bright regions, under-smoothing in dark               | Heteroscedastic likelihood; work in linear light on raw data              |

#### Takeaways {#cv-image-formation-and-cameras--takeaways}

1. **The projection equation is the whole of geometric vision's forward model.** Everything downstream is an attempt to invert it under ambiguity.
2. **Perspective division creates the three fundamental ambiguities** — depth from one view, global scale, and quadratically degrading depth resolution.
3. **Optimise rotations on the manifold**, with $$\mathfrak{so}(3)$$ increments, not by perturbing matrix entries.
4. **Distortion is observable only at the periphery**, which dictates how calibration data must be collected.
5. **The Lambertian assumption is load-bearing and routinely false.** Most "mysterious" failures in flow, stereo, depth and rendering are this assumption breaking quietly.
6. **Resizing an image changes its intrinsics.** An augmentation that does not update $$\mathbf{K}$$ leaves the geometry wrong before training starts.

### Calibration and sensor alignment {#cv-calibration-and-sensor-alignment}

_The least glamorous family in vision, the one the decade left almost untouched, and the one every metric claim still rests on._

#### Problem definition and observability {#cv-calibration-and-sensor-alignment--problem}

**Input:** images of a known target, or natural correspondences across views. **Output:** intrinsics $$\mathbf{K}$$, distortion $$\mathbf{d}$$, per-view extrinsics $$(\mathbf{R}_i, \mathbf{t}_i)$$, and — for multi-sensor rigs — the rigid transform between sensors.

> **What is and is not observable**
>
> - **From a single view of a plane:** a homography, 8 DoF. Not enough to separate $$\mathbf{K}$$ from pose — this is why Zhang's method needs _several_ orientations.
> - **Focal length vs. distance:** nearly unidentifiable if all views are fronto-parallel at similar depth. The Jacobian columns become almost collinear and the normal equations are ill-conditioned.
> - **Distortion:** only observable where $$r$$ is large, i.e. at the image periphery. A centre-only dataset yields confident nonsense at the edges.
> - **Principal point:** weakly observable, and strongly correlated with translation. Many pipelines fix $$(c_x,c_y)$$ at the image centre rather than estimate it badly.

#### The objective {#cv-calibration-and-sensor-alignment--objective}

Calibration is an instance of the [general template](#cv-vision-objectives-and-optimization--template) with $$\theta = \{\mathbf{K}, \mathbf{d}, \mathbf{R}_i, \mathbf{t}_i\}$$ and a reprojection residual.

**Reprojection objective**

$$ \mathcal{L}(\theta) \;=\; \sum*{i=1}^{N*{\text{views}}}\sum*{j=1}^{N*{\text{pts}}} w*{ij}\,\rho\Big( \big\lVert \mathbf{u}*{ij} - \pi(\mathbf{K}, \mathbf{d}, \mathbf{R}\_i, \mathbf{t}\_i, \mathbf{X}\_j) \big\rVert_2 \Big) $$

_$$\mathbf{u}_{ij}$$ is the detected corner, $$\mathbf{X}_j$$ its known 3D position on the target, and $$\pi$$ the full projection including distortion. Minimised by Levenberg–Marquardt. The residual is measured **in pixels**, which is the only space where the noise model is approximately isotropic — this is why one never minimises error in world units here.\_

##### Why a single RMS number is not enough {#cv-calibration-and-sensor-alignment--rms}

The reported RMS reprojection error is an average over all corners in all views. It hides exactly the failures that matter:

- **Plot residuals spatially.** A radial pattern means the distortion model is wrong or under-parameterised. Systematic structure is bias; scatter is noise.
- **Plot residuals per view.** One blurry or mis-detected view can dominate, or be silently absorbed into a distorted $$\mathbf{K}$$.
- **Check per-camera and cross-camera residuals separately** in a multi-camera rig. A good average can hide one badly modelled camera.

#### The Direct Linear Transform {#cv-calibration-and-sensor-alignment--dlt}

The standard linear initialiser. From $$\mathbf{u} \times \mathbf{P}\tilde{\mathbf{X}} = \mathbf{0}$$ — the cross product vanishes when the projection is parallel to the measurement — each correspondence yields two independent linear equations in the 12 entries of $$\mathbf{P}$$:

$$ \begin{bmatrix} \mathbf{0}^\top & -\tilde{\mathbf{X}}^\top & v\,\tilde{\mathbf{X}}^\top \\ \tilde{\mathbf{X}}^\top & \mathbf{0}^\top & -u\,\tilde{\mathbf{X}}^\top \end{bmatrix} \begin{bmatrix}\mathbf{p}^1 \\ \mathbf{p}^2 \\ \mathbf{p}^3\end{bmatrix} = \mathbf{0} \qquad\Longrightarrow\qquad \mathbf{A}\mathbf{p} = \mathbf{0} $$

_Stack $$\geq 6$$ correspondences and take $$\mathbf{p}$$ as the right singular vector of $$\mathbf{A}$$ with the smallest singular value. $$\mathbf{K}$$ and $$\mathbf{R}$$ are then recovered from the left 3×3 block of $$\mathbf{P}$$ by RQ decomposition._

> **Normalise the points first — this is not optional**
> Raw pixel coordinates have magnitudes around $$10^3$$ while homogeneous entries are $$1$$, so the columns of $$\mathbf{A}$$ differ by three orders of magnitude and the SVD is dominated by numerical noise. **Hartley normalisation** applies a similarity $$\mathbf{T}$$ that centres the points at the origin and scales their mean distance to $$\sqrt{2}$$, solves in normalised coordinates, then un-normalises: $$\mathbf{P} = \mathbf{T}'^{-1}\hat{\mathbf{P}}\mathbf{T}$$. The same argument applies to the eight-point algorithm for the fundamental matrix.

#### Zhang's method {#cv-calibration-and-sensor-alignment--zhang}

The practical workhorse: several views of a planar grid. Setting $$Z=0$$ on the target plane collapses the projection to a homography.

$$ \mathbf{H} = \mathbf{K}\begin{bmatrix}\mathbf{r}\_1 & \mathbf{r}\_2 & \mathbf{t}\end{bmatrix} \quad\text{(up to scale)} $$

Orthonormality of $$\mathbf{r}_1, \mathbf{r}_2$$ gives two constraints per view on $$\mathbf{B} = \mathbf{K}^{-\top}\mathbf{K}^{-1}$$, the image of the absolute conic:

$$ \mathbf{h}\_1^\top \mathbf{B}\,\mathbf{h}\_2 = 0, \qquad \mathbf{h}\_1^\top \mathbf{B}\,\mathbf{h}\_1 = \mathbf{h}\_2^\top \mathbf{B}\,\mathbf{h}\_2 $$

_$$\mathbf{B}$$ is symmetric with 6 unknowns (5 up to scale), so **three views in general position suffice**. $$\mathbf{K}$$ follows from the Cholesky factorisation of $$\mathbf{B}$$. Distortion is then introduced and everything is refined jointly by nonlinear least squares._

The procedure in full: detect corners to subpixel accuracy → estimate per-view homographies → solve linearly for $$\mathbf{B}$$, hence $$\mathbf{K}$$ → recover per-view $$(\mathbf{R}_i,\mathbf{t}_i)$$ → initialise distortion at zero → refine all parameters by LM on the reprojection objective.

#### Stereo calibration and rectification {#cv-calibration-and-sensor-alignment--stereo}

For two cameras, calibration additionally yields the relative pose $$(\mathbf{R}, \mathbf{t})$$, from which the epipolar geometry follows:

**Essential and fundamental matrices**

$$ \mathbf{E} = [\mathbf{t}]\_\times\mathbf{R}, \qquad \mathbf{F} = \mathbf{K}'^{-\top}\mathbf{E}\,\mathbf{K}^{-1}, \qquad \mathbf{u}'^\top \mathbf{F}\,\mathbf{u} = 0 $$

_$$\mathbf{E}$$ has 5 DoF (3 rotation + 2 translation direction; scale is unrecoverable), $$\mathbf{F}$$ has 7. The epipolar constraint says a point in one image must lie on a line in the other — it reduces correspondence search from 2D to **1D**._

**Rectification** applies homographies $$\mathbf{H}, \mathbf{H}'$$ that map the epipoles to infinity along the horizontal axis, so corresponding points share a row and disparity is a pure horizontal shift. This is the step that makes [classical stereo](#cv-stereo-and-depth-estimation) tractable, and it is why an uncalibrated or mis-rectified pair produces stereo that fails in a way no matching cost can repair.

**Depth from disparity, after rectification**

$$ Z = \frac{f\,B}{d}, \qquad d = u_L - u_R $$

#### Multi-sensor alignment {#cv-calibration-and-sensor-alignment--multisensor}

> **Hand–eye calibration**
> Find the unknown rigid transform $$\mathbf{X}$$ between a robot's end effector and a camera, from pairs of motions: $$ \mathbf{A}\mathbf{X} = \mathbf{X}\mathbf{B} $$ where $$\mathbf{A}$$ is the measured end-effector motion and $$\mathbf{B}$$ the observed camera motion. The rotation part, $$\mathbf{R}_A\mathbf{R}_X = \mathbf{R}_X\mathbf{R}_B$$, is solvable in closed form (Tsai–Lenz, Park–Martin); the translation follows linearly. **Requires at least two motions with non-parallel rotation axes**, or the rotation is under-determined.

> **Camera–LiDAR and camera–IMU** > **Camera–LiDAR:** minimise reprojection of 3D points onto image edges or a shared target; the objective is the same reprojection form, with the LiDAR points playing the role of $$\mathbf{X}_j$$.<br><br> **Camera–IMU:** estimate the rigid transform _and_ the time offset $$t_d$$, since unsynchronised clocks masquerade as a spatial offset under motion. Typically solved inside a visual–inertial bundle adjustment with IMU preintegration.

**Temporal synchronisation** is a first-class parameter, not a detail. A 10 ms offset on a camera moving at 1 m/s is a 1 cm systematic error that calibration will happily absorb into the extrinsics, producing a rig that is self-consistent at one speed and wrong at every other.

#### Engineering tricks {#cv-calibration-and-sensor-alignment--tricks}

- **Cover the entire image with the target**, especially the corners — distortion lives there.
- **Vary orientation and distance**; include strongly tilted views to decorrelate focal length from depth.
- **Subpixel corner refinement** (saddle-point fitting); checkerboards give higher accuracy than printed circles, ChArUco beats both for partial visibility.
- **Initialise distortion conservatively** — start with $$k_1$$ only and add terms while the residual improves; more coefficients always fit the training corners better and often extrapolate worse.
- **Reject blurry views and outlier corners**; use a robust $$\rho$$ (Huber) in the refinement.
- **Print flatness matters.** A target taped to a slightly curved surface introduces a systematic bias that looks exactly like distortion.
- **Re-calibrate after any mechanical shock**, temperature swing, or lens re-focus.

#### Metrics and failure modes {#cv-calibration-and-sensor-alignment--metrics}

| Diagnostic                         | Healthy                   | Unhealthy, and what it means                                   |
| ---------------------------------- | ------------------------- | -------------------------------------------------------------- |
| RMS reprojection error             | < 0.5 px for a decent rig | > 1 px: wrong model, bad detections, or a blurred view         |
| Residual field over the image      | Isotropic scatter         | Radial or swirl pattern: distortion model mis-specified        |
| Per-view residual                  | Comparable across views   | One outlier view: motion blur or a mis-detected board          |
| Parameter covariance               | Small, low correlation    | High $$f$$–$$t_z$$ correlation: not enough orientation variety |
| Epipolar error after rectification | < 0.3 px vertical         | Larger: relative pose wrong; stereo will fail downstream       |

#### Takeaways {#cv-calibration-and-sensor-alignment--takeaways}

1. **Calibration is a nonlinear least-squares problem with a linear initialiser.** DLT/Zhang give the starting point; Levenberg–Marquardt performs the refinement.
2. **Normalise before any DLT-style solve.** Conditioning, not cosmetics.
3. **Observability dictates data collection.** Peripheral coverage for distortion, orientation variety for focal length.
4. **Never trust one RMS number.** Inspect residuals spatially and per view.
5. **Time offset is an extrinsic parameter.** Unsynchronised sensors produce bias that calibration hides rather than reveals.
6. **This family was not learned away.** Every metric claim from a modern geometry model still rests on a camera model somebody estimated classically.

### Vision objectives and optimization {#cv-vision-objectives-and-optimization}

_One template covers most of the field. Learning which of its five slots a method fills is the fastest way to understand an unfamiliar paper._

#### The common objective template {#cv-vision-objectives-and-optimization--template}

**The template**

$$ \theta^{\*} \;=\; \arg\min*{\theta}\; \underbrace{\sum*{i\in\mathcal{V}} w*i\,\rho\big(r_i(\theta)\big)}*{\text{data term}} \;+\; \underbrace{\sum*{k}\lambda_k R_k(\theta)}*{\text{regularizers}} $$

- $$\theta$$ — unknowns: image, motion, geometry, pose, labels, or network parameters
- $$r_i$$ — an observation residual — see the [nine families](#cv-vision-objectives-and-optimization--data-terms)
- $$\rho$$ — a robust penalty shaping the influence of large residuals
- $$w_i$$ — confidence or visibility weight
- $$\mathcal{V}$$ — the valid set: visible, unoccluded, in-bounds observations
- $$R_k, \lambda_k$$ — priors and their weights

> **Read any method by filling the five slots**
> What is $$\theta$$? What is $$r_i$$, and against what — a label, another measurement, or a rendering? What are $$\mathcal{V}$$ and $$w_i$$? What is $$\rho$$? What are $$R_k$$? Most papers state the first and fourth explicitly; **the interesting engineering is usually hidden in $$\mathcal{V}$$ and $$w_i$$** — occlusion handling, visibility masks, and outlier rejection.

#### The MAP interpretation {#cv-vision-objectives-and-optimization--map}

The template is not arbitrary. Maximising the posterior $$p(\theta\mid \mathbf{z}) \propto p(\mathbf{z}\mid\theta)\,p(\theta)$$ and taking negative logs gives

$$ \theta^{\*} = \arg\min\_\theta \Big[-\log p(\mathbf{z}\mid\theta) - \log p(\theta)\Big] $$

_The data term \_is_ the negative log-likelihood; the regularizer _is_ the negative log-prior. This fixes which $$\rho$$ corresponds to which noise model.\_

| Penalty $$\rho(r)$$                      | Implied noise model            | Influence $$\psi = \rho'$$           | Behaviour                                 |
| ---------------------------------------- | ------------------------------ | ------------------------------------ | ----------------------------------------- |
| $$\tfrac12 r^2$$ (L2)                    | Gaussian                       | $$r$$ — unbounded                    | One outlier can dominate                  |
| $$\lvert r\rvert$$ (L1)                  | Laplacian                      | $$\operatorname{sign}(r)$$ — bounded | Robust; non-smooth at 0                   |
| Charbonnier $$\sqrt{r^2+\epsilon^2}$$    | Smoothed Laplacian             | $$r/\sqrt{r^2+\epsilon^2}$$          | L1-like but differentiable                |
| Huber                                    | Gaussian core, Laplacian tails | clipped at $$\delta$$                | The default in bundle adjustment          |
| Cauchy $$\tfrac{c^2}{2}\log(1+(r/c)^2)$$ | Heavy-tailed                   | $$r/(1+(r/c)^2)$$ — _redescending_   | Large residuals lose influence            |
| Tukey biweight                           | Hard rejection                 | Exactly $$0$$ beyond $$c$$           | Outliers fully discarded; needs good init |

**Huber**

$$ \rho\_\delta(r) = \begin{cases} \tfrac{1}{2}r^2 & \lvert r\rvert \le \delta \\[2pt] \delta\big(\lvert r\rvert - \tfrac{1}{2}\delta\big) & \lvert r\rvert > \delta \end{cases} $$

> **Redescending penalties have a basin of attraction**
> Cauchy and Tukey drive the influence of large residuals toward zero, which is the required behaviour _once the estimate is approximately correct_, and the wrong behaviour from a poor initialisation, where true inliers resemble outliers and are discarded. This is why the ordering is always **RANSAC first, robust refinement second**, and why [coarse registration precedes ICP](#cv-point-clouds-and-3d-perception--registration).

#### The nine data terms {#cv-vision-objectives-and-optimization--data-terms}

| Data term           | Residual                                                 | Tasks                                                | Assumption                        |
| ------------------- | -------------------------------------------------------- | ---------------------------------------------------- | --------------------------------- |
| **Photometric**     | $$I_t(\mathbf{p}) - I_s(\mathbf{W}(\mathbf{p};\theta))$$ | Flow, stereo, direct VO, self-supervised depth, NeRF | Corresponding surfaces look alike |
| **Reprojection**    | $$\mathbf{u} - \pi(\mathbf{K},\mathbf{T},\mathbf{X})$$   | Calibration, PnP, SfM, bundle adjustment             | Camera model and matches valid    |
| **Epipolar**        | $$\mathbf{u}'^\top\mathbf{F}\mathbf{u}$$                 | Two-view pose, SfM init                              | Rigid two-view geometry           |
| **Feature**         | $$\lVert \mathbf{f}_a - \mathbf{f}_b\rVert$$             | Registration, retrieval, SLAM                        | Descriptor invariant to nuisances |
| **Semantic**        | $$-\log p_\theta(y\mid\mathbf{x})$$                      | Classification, detection, segmentation              | Labels valid, classes defined     |
| **Region overlap**  | $$1 - \mathrm{IoU}$$, Dice                               | Segmentation, detection                              | Overlap represents utility        |
| **Metric learning** | margin on embedding distances                            | Retrieval, face, Re-ID                               | Similarity is geometric           |
| **Rendering**       | $$\hat{C}(\mathbf{r}) - C(\mathbf{r})$$                  | NeRF, inverse rendering, 3DGS                        | Renderer approximates formation   |
| **Temporal**        | $$\theta_t - \theta_{t-1}$$, ID consistency              | Tracking, video segmentation                         | State varies smoothly             |

> **The self-supervision insight hiding in this table**
> Rows 1–4 and 8–9 require **no human labels** — they compare measurements against other measurements under a geometric or physical model. Rows 5–7 require labels. Nearly the whole self-supervised story of 2019–2025 is work migrating out of the labelled rows into the unlabelled ones. See the [supervision ladder](#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--ladder).

#### Regularizers and priors {#cv-vision-objectives-and-optimization--regularizers}

**Common spatial priors**

$$ R*{\text{TV}}(\mathbf{x}) = \sum*{\mathbf{p}} \lVert\nabla \mathbf{x}(\mathbf{p})\rVert*1, \qquad R*{\text{Tik}}(\mathbf{x}) = \sum\_{\mathbf{p}} \lVert\nabla \mathbf{x}(\mathbf{p})\rVert_2^2 $$

_Total variation preserves discontinuities (L1 on gradients tolerates a few large jumps); Tikhonov smoothness penalises them quadratically and blurs edges. The choice determines whether the depth map has crisp object boundaries or soft ones._

**Edge-aware smoothness**

$$ R*{\text{edge}}(d) = \sum*{\mathbf{p}} \Big( \lvert\partial_x d\rvert\,e^{-\lVert\partial_x I\rVert} + \lvert\partial_y d\rvert\,e^{-\lVert\partial_y I\rVert} \Big) $$

_Smooth the estimate where the image is flat, allow jumps where the image has an edge. Standard in self-supervised depth and flow. Note it imports the assumption that \_depth discontinuities coincide with intensity edges_, which fails for low-contrast object boundaries.\_

Other priors in routine use: sparsity ($$\ell_1$$), low rank (nuclear norm), non-local self-similarity, piecewise planarity, surface-normal consistency, rigidity, temporal constancy, entropy control, and topology constraints. For the relational family — cycle, left–right, forward–backward — see [consistency constraints](#cv-cross-cutting-mechanisms-and-failure-modes--consistency).

> **Regularization is not decoration**
> It resolves the underdetermination that _remains after_ the data term. Horn–Schunck is the standard case: brightness constancy gives one scalar equation per pixel for two unknowns, so the system is underdetermined by construction — the [aperture problem](#cv-optical-flow-and-scene-flow--aperture). Smoothness is what makes it well-posed at all.

#### Optimization machinery {#cv-vision-objectives-and-optimization--optimization}

##### Gauss–Newton and Levenberg–Marquardt {#cv-vision-objectives-and-optimization--gn}

For a nonlinear least-squares objective $$\tfrac12\lVert \mathbf{r}(\theta)\rVert^2$$ with Jacobian $$\mathbf{J} = \partial\mathbf{r}/\partial\theta$$:

$$ \underbrace{(\mathbf{J}^\top\mathbf{J})\,\delta = -\mathbf{J}^\top\mathbf{r}}_{\text{Gauss–Newton}} \qquad\qquad \underbrace{(\mathbf{J}^\top\mathbf{J} + \mu\,\mathbf{D})\,\delta = -\mathbf{J}^\top\mathbf{r}}_{\text{Levenberg–Marquardt}} $$

_GN approximates the Hessian as $$\mathbf{J}^\top\mathbf{J}$$, dropping second-derivative terms — valid when residuals are small or nearly linear. LM adds a damping term: large $$\mu$$ gives a short, safe gradient-descent step; small $$\mu$$ recovers GN's fast quadratic convergence. $$\mu$$ is adapted each iteration based on whether the step reduced the cost._

Robust penalties enter through **iteratively reweighted least squares**: minimising $$\sum\rho(r_i)$$ is equivalent to repeatedly solving a weighted least-squares problem with $$w_i = \psi(r_i)/r_i$$, recomputed each iteration.

##### Exploiting structure: the Schur complement {#cv-vision-objectives-and-optimization--sparsity}

In bundle adjustment $$\theta$$ splits into camera parameters $$\mathbf{c}$$ and points $$\mathbf{p}$$, and a point is seen by few cameras, so the system is very sparse and block-structured:

$$ \begin{bmatrix}\mathbf{B} & \mathbf{E}\\ \mathbf{E}^\top & \mathbf{C}\end{bmatrix}\begin{bmatrix}\delta*{\mathbf{c}}\\ \delta*{\mathbf{p}}\end{bmatrix} = \begin{bmatrix}\mathbf{v}\\ \mathbf{w}\end{bmatrix} \;\Longrightarrow\; \big(\mathbf{B} - \mathbf{E}\mathbf{C}^{-1}\mathbf{E}^\top\big)\,\delta\_{\mathbf{c}} = \mathbf{v} - \mathbf{E}\mathbf{C}^{-1}\mathbf{w} $$

_$$\mathbf{C}$$ is block-diagonal (3×3 per point), so $$\mathbf{C}^{-1}$$ is trivial. Solving the reduced camera system is what makes BA over thousands of views feasible. See [bundle adjustment](#cv-camera-pose-sfm-vo-and-slam--ba)._

##### Discrete optimisation {#cv-vision-objectives-and-optimization--discrete}

- **Dynamic programming** — Exact on a chain. Used for scanline stereo and, along multiple 1D paths, as the approximation inside [Semi-Global Matching](#cv-stereo-and-depth-estimation--sgm).

- **Graph cuts** — Exact for binary submodular energies via max-flow/min-cut; $$\alpha$$-expansion gives a bounded approximation for multi-label problems. Used in segmentation and stereo.

- **Belief propagation** — Exact on trees, approximate ("loopy") on grids. Message passing over an MRF; competitive with graph cuts on stereo.

#### RANSAC and robust model fitting {#cv-vision-objectives-and-optimization--ransac}

Sample a minimal set, fit, count inliers, repeat, keep the best. The required number of iterations follows from wanting probability $$p$$ of at least one all-inlier sample:

$$ N \;=\; \frac{\log(1-p)}{\log\big(1-(1-\varepsilon)^{s}\big)} $$

- $$\varepsilon$$ — outlier ratio
- $$s$$ — minimal sample size (4 for a homography, 5 for essential, 3 for PnP)
- $$p$$ — desired success probability, typically 0.99

_The exponential in $$s$$ is why minimal solvers matter so much: at $$\varepsilon = 0.5$$, $$s=4$$ needs ~72 iterations while $$s=8$$ needs ~1177._

- **MLESAC** maximises a likelihood rather than counting inliers, so near-threshold points contribute smoothly.
- **PROSAC** samples from matches ordered by descriptor quality, finding a good hypothesis far sooner in practice.
- **LO-RANSAC** runs a local optimisation on the inlier set of each promising hypothesis.
- **Always refine on all inliers** after RANSAC — the minimal-sample estimate is unbiased but high-variance.

#### Takeaways {#cv-vision-objectives-and-optimization--takeaways}

1. **One template covers most of vision.** Filling its five slots specifies the method.
2. **The penalty encodes a noise model.** Choosing L2 assumes the residuals are Gaussian.
3. **Redescending penalties need good initialisation.** Hence RANSAC first, robust refinement second — always in that order.
4. **Regularizers fix underdetermination, not numerics.** Without them many vision problems have no unique solution at all.
5. **Structure is what makes large problems tractable.** Sparsity and the Schur complement, not raw solver speed.
6. **The optimised surrogate is rarely the reported metric.** Several of the decade's results come from reducing that gap.

### Multiscale vision and filtering {#cv-multiscale-vision-and-filtering}

_The single most reused structural idea in the field, wearing a different costume in every decade: image pyramids, feature pyramids, U-Net skips, cost-volume cascades, hash grids, hierarchical transformers._

#### Convolution and correlation {#cv-multiscale-vision-and-filtering--convolution}

$$ (f \* g)(\mathbf{p}) = \sum*{\mathbf{q}} f(\mathbf{q})\,g(\mathbf{p}-\mathbf{q}), \qquad (f \star g)(\mathbf{p}) = \sum*{\mathbf{q}} f(\mathbf{q})\,g(\mathbf{p}+\mathbf{q}) $$

_Convolution flips the kernel; correlation does not. They coincide for symmetric kernels — which is why the distinction rarely matters for Gaussians and always matters for derivative filters. **Deep-learning "convolution" layers compute correlation**; since the kernel is learned, the flip is absorbed into it._

Two properties carry most of the practical weight:

- **Separability.** A 2D Gaussian factors as $$G_\sigma(x,y) = G_\sigma(x)G_\sigma(y)$$, reducing a $$k\times k$$ filter from $$O(k^2)$$ to $$O(2k)$$ per pixel. The same factorisation motivates [depthwise separable convolutions](#cv-depth-detection-and-the-first-believable-images--mobilenet).
- **Linearity and shift invariance.** Together these make the frequency-domain view available, and make convolution the unique operator commuting with translation.

#### Gaussian scale space {#cv-multiscale-vision-and-filtering--scalespace}

The scale-space representation convolves the image with Gaussians of increasing width:

$$ L(x, y; t) = G*{\sqrt{t}} \* I, \qquad G*\sigma(x,y) = \frac{1}{2\pi\sigma^2}\exp\!\left(-\frac{x^2+y^2}{2\sigma^2}\right) $$

_Equivalently, $$L$$ solves the heat equation $$\partial_t L = \tfrac12\nabla^2 L$$ with $$L(\cdot;0)=I$$. The Gaussian is the \_unique_ kernel that creates no new extrema as scale increases — the formal statement of "coarser means simpler", and the reason scale space is built with Gaussians rather than box filters.\_

##### Gaussian and Laplacian pyramids {#cv-multiscale-vision-and-filtering--pyramids}

> **Gaussian pyramid** > $$G_0 = I$$, and $$G_{\ell+1} = \operatorname{down}_2(G_\ell * g)$$. Blur _then_ subsample — the blur is anti-aliasing, not decoration. Skipping it aliases high frequencies into low ones, which is exactly the artefact that makes naive downsampling destroy thin structures.

> **Laplacian pyramid** > $$L_\ell = G_\ell - \operatorname{up}_2(G_{\ell+1})$$, with $$L_n = G_n$$. Each level holds one octave of _bandpass_ detail, and the decomposition is invertible: $$G_\ell = L_\ell + \operatorname{up}_2(G_{\ell+1})$$. This exact reconstruction is what makes it the right structure for [multiband blending](#cv-image-stitching-and-fusion--blending).

**Scale-normalised Laplacian — the blob detector**

$$ \nabla^2*{\text{norm}} L = t\,\big(L*{xx} + L\_{yy}\big), \qquad \mathrm{DoG} = L(\cdot;k^2t) - L(\cdot;t) \approx (k-1)t\,\nabla^2 L $$

_Without the factor $$t$$, response magnitude decays with scale and extrema are never found at coarse scales. Extrema of the scale-normalised response in $$(x,y,t)$$ give both a location \_and_ a characteristic scale — this is the mechanism behind [SIFT's](#cv-features-and-visual-primitives--sift) scale invariance, and the Difference-of-Gaussians is simply a cheap approximation to it.\_

#### The frequency-domain view {#cv-multiscale-vision-and-filtering--frequency}

**Convolution theorem**

$$ \mathcal{F}\{f \* g\} = \mathcal{F}\{f\}\cdot\mathcal{F}\{g\} $$

Three things follow that are worth carrying around:

- **Blurring is low-pass filtering.** $$\mathcal{F}\{G_\sigma\}$$ is a Gaussian of width $$1/\sigma$$, so a wide blur kernel is a narrow frequency window. Deconvolution is division by this — and division by near-zero values is why [deblurring is ill-posed](#cv-restoration-and-enhancement--deblur).
- **Sampling requires band-limiting.** Nyquist: a signal sampled at rate $$f_s$$ must contain no content above $$f_s/2$$, or aliasing folds it down. Hence blur-before-subsample.
- **Spectral bias.** Networks fit low frequencies first. This is precisely why NeRF needs [positional encoding](#cv-neural-rendering-and-novel-views--encoding): an MLP on raw coordinates cannot represent high-frequency detail in reasonable time.

#### Image derivatives and the structure tensor {#cv-multiscale-vision-and-filtering--derivatives}

Differentiation amplifies noise, so derivatives are always taken of a _smoothed_ image — and by associativity that is a single convolution with the derivative of the Gaussian:

$$ \partial*x (G*\sigma _ I) = (\partial*x G*\sigma) _ I $$

Sobel and Scharr are small discrete approximations to exactly this. Aggregating first derivatives over a window gives the structure tensor:

**Structure tensor**

$$ \mathbf{M} = \sum\_{\mathbf{q}\in W} w(\mathbf{q}) \begin{bmatrix} I_x^2 & I_xI_y \\ I_xI_y & I_y^2 \end{bmatrix} $$

_Its eigenvalues $$\lambda_1 \ge \lambda_2$$ classify local structure: both small → flat; one large → edge; both large → corner. This one matrix underlies [Harris corners](#cv-features-and-visual-primitives--harris), the Shi–Tomasi "good features to track" score, and the invertibility condition of [Lucas–Kanade](#cv-optical-flow-and-scene-flow--lk) — three methods that appear unrelated until the shared depend on $$\mathbf{M}$$ being well-conditioned._

#### Nonlinear and edge-preserving filters {#cv-multiscale-vision-and-filtering--nonlinear}

| Filter                    | Form                                                                                                                                                 | Property                                                                                       |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Median**                | Order statistic over a window                                                                                                                        | Removes impulse noise without blurring edges; not linear, so no frequency interpretation       |
| **Bilateral**             | $$\frac{1}{W}\sum_{\mathbf{q}} G_{\sigma_s}(\lVert\mathbf{p}-\mathbf{q}\rVert)\,G_{\sigma_r}(\lvert I_\mathbf{p}-I_\mathbf{q}\rvert)\,I_\mathbf{q}$$ | Weights by spatial _and_ intensity distance; smooths within regions, preserves edges           |
| **Guided**                | Local linear model of a guide image                                                                                                                  | Bilateral-like behaviour, $$O(N)$$, no gradient reversal; used for depth upsampling            |
| **Anisotropic diffusion** | $$\partial_t I = \nabla\!\cdot\!\big(c(\lVert\nabla I\rVert)\nabla I\big)$$                                                                          | Heat equation with conductivity that shuts off at edges                                        |
| **Non-local means**       | Weights from _patch_ similarity, not pixel distance                                                                                                  | Exploits self-similarity; the direct ancestor of [BM3D](#cv-restoration-and-enhancement--bm3d) |

##### Morphology {#cv-multiscale-vision-and-filtering--morphology}

$$ (I \ominus B)(\mathbf{p}) = \min*{\mathbf{b}\in B} I(\mathbf{p}+\mathbf{b}), \qquad (I \oplus B)(\mathbf{p}) = \max*{\mathbf{b}\in B} I(\mathbf{p}+\mathbf{b}) $$

_Erosion and dilation. Their compositions are **opening** $$I\circ B = (I\ominus B)\oplus B$$, which removes structures smaller than $$B$$, and **closing** $$I\bullet B = (I\oplus B)\ominus B$$, which fills holes smaller than $$B$$. Both are idempotent, which is why they are safe as [post-processing](#cv-cross-cutting-mechanisms-and-failure-modes--postproc) — applying twice changes nothing._

#### Coarse-to-fine optimisation {#cv-multiscale-vision-and-filtering--coarse-to-fine}

The reason pyramids matter beyond efficiency. For a warp-based objective such as [photometric alignment](#cv-photometric-consistency), the cost surface has many local minima at fine scale: shifting by one period of a texture is locally as good as the true alignment. Blurring removes that structure.

**Coarse-to-fine schedule**

$$ \theta^{(\ell-1)} \leftarrow \arg\min*\theta \sum*{\mathbf{p}} \rho\Big(I^{(\ell-1)}\_t(\mathbf{p}) - I^{(\ell-1)}\_s\big(\mathbf{W}(\mathbf{p};\theta)\big)\Big), \quad \text{initialised from } \theta^{(\ell)} \text{ upscaled} $$

_At level $$\ell$$ a displacement of $$d$$ pixels appears as $$d/2^\ell$$, so a large motion becomes a small one and falls inside the linearisation's basin of attraction. Flow and disparity estimates are scaled by 2 when passed down a level._

> **The structural flaw, and RAFT's answer**
> A small, fast-moving object _disappears_ at coarse levels and can never be recovered at fine ones — the coarse estimate has already committed to the background motion. [RAFT](#cv-scale-self-supervision-and-set-prediction--video) rejects the pyramid entirely: build **all-pairs correlation at a single high resolution** and refine iteratively with a shared recurrent operator. The lesson generalises — coarse-to-fine buys a larger basin of attraction at the price of small structure, and that trade is not always worth taking.

#### The same idea, six decades of costumes {#cv-multiscale-vision-and-filtering--lineage}

| Incarnation                                                                          | Era         | Mechanism                                                        |
| ------------------------------------------------------------------------------------ | ----------- | ---------------------------------------------------------------- |
| Gaussian / Laplacian pyramids                                                        | 1980s       | Explicit blur-and-subsample stack                                |
| Scale space, SIFT                                                                    | 1990s–2000s | Extrema over $$(x,y,\sigma)$$ give scale invariance              |
| Coarse-to-fine warping                                                               | 1990s–2010s | Enlarges the optimisation basin for flow and stereo              |
| [Feature Pyramid Networks](#cv-depth-detection-and-the-first-believable-images--fpn) | 2017        | Top-down pathway + lateral connections; semantics at every scale |
| U-Net skip connections                                                               | 2015–       | Concatenative recovery of resolution lost to striding            |
| Atrous / dilated convolution                                                         | 2015–2018   | Receptive field without resolution loss                          |
| Cost-volume cascades                                                                 | 2018–       | Coarse-to-fine depth hypotheses in MVS                           |
| Multiresolution hash grids                                                           | 2022        | Level-of-detail feature lookup for neural fields                 |
| [Swin patch merging](#cv-the-transformer-takeover--swin)                             | 2021        | Transformer hierarchy: resolution halves, channels double        |

#### Takeaways {#cv-multiscale-vision-and-filtering--takeaways}

1. **Blur before subsampling.** Everything else about pyramids is downstream of Nyquist.
2. **The Gaussian is not an arbitrary choice** — it is the unique kernel that creates no new structure as scale coarsens.
3. **Scale-normalisation is what makes scale _selection_ possible**, and is the mechanism behind SIFT's invariance.
4. **One matrix — the structure tensor — underlies Harris, Shi–Tomasi and Lucas–Kanade.**
5. **Coarse-to-fine trades small structure for a larger basin of attraction.** RAFT showed that trade is optional.
6. **Every generation reinvents the pyramid.** Recognising it identifies each reinvention as the same construction.

### The shared pipeline and the objective template {#cv-the-shared-pipeline-and-the-objective-template}

_Almost every vision system, classical or learned, decomposes into the same ten operations — and a large fraction of the field can be written as a single optimisation template._

#### The ten-step pipeline {#cv-the-shared-pipeline-and-the-objective-template--pipeline}

This decomposition is deliberately method-agnostic. A 1998 stereo algorithm and a 2025 feed-forward geometry transformer both instantiate it; they differ in _which steps are learned_ and _which are hand-specified_, not in which steps exist.

**1 · Acquire and calibrate**

Model lens distortion, camera intrinsics, exposure, synchronization, sensor-to-sensor extrinsics and rolling shutter. Errors introduced here are systematic and cannot be recovered downstream — they show up as bias, not noise.

**2 · Normalize and preprocess**

Undistort, rectify, denoise, resize, normalize intensity or colour, construct image pyramids, optionally mask invalid regions. Rectification in particular converts a 2D search into a 1D one and is why classical stereo is tractable at all.

**3 · Represent**

Choose the carrier of information: pixels, gradients, patches, keypoints and descriptors, superpixels, feature maps, tokens, voxels, points, meshes, signed distance fields, or radiance fields. **This is the layer deep learning changed most.**

**4 · Generate hypotheses**

Propose matches, boxes, masks, poses, disparities, flow vectors, tracks or scene structure. The move from _enumerated_ hypotheses (sliding windows, anchors, disparity ranges) to _learned_ ones (queries, proposals) is one of the decade's clearest trends.

**5 · Score with data terms**

Compare predictions to observations or labels using photometric, geometric, semantic, appearance or distributional residuals. See [the data-term table](#cv-the-shared-pipeline-and-the-objective-template--data-terms) below.

**6 · Regularize**

Inject priors: smoothness, sparsity, piecewise rigidity, temporal continuity, shape constraints, weight decay. Not decoration — this is what resolves the underdetermination the data term leaves behind.

**7 · Reject outliers and resolve ambiguity**

RANSAC, robust penalties, gating, confidence thresholds, visibility masks, left–right checks, hard-negative mining, uncertainty weighting. Real residual distributions are contaminated; assuming they are not is the most common practical error.

**8 · Optimize**

Closed-form estimation, dynamic programming, graph cuts, belief propagation, Gauss–Newton, Levenberg–Marquardt, gradient descent, or end-to-end backpropagation. The choice is dictated by the structure of the objective, not by fashion.

**9 · Post-process**

Non-maximum suppression, connected components, morphology, CRFs, median filtering, hole filling, track birth/death rules, mesh cleanup. Each of these **embodies a prior the network was not asked to learn** — which is exactly why removing them took a decade.

**10 · Evaluate and calibrate confidence**

Select metrics aligned with the application, test robustness, and inspect failure modes, in place of a single average score.

> **Three structural observations**
>
> - **Image pyramids and wavelets** provide multiscale analysis and accelerate operations — the idea reappears as Gaussian/Laplacian pyramids, FPNs, U-Net skips, coarse-to-fine cost volumes, multiresolution hash grids and hierarchical transformers.
> - **Geometric warps** — rotation, shear, affine, perspective — are the vocabulary of step 4 whenever correspondence is involved.
> - **Energy minimisation** connects many classical algorithms to Bayesian or Markov-random-field estimation, which is what makes step 5 and step 6 formally comparable across methods.

#### The common objective template {#cv-the-shared-pipeline-and-the-objective-template--template}

A large fraction of computer vision can be written in one form:

**θ<sup>\*</sup> = arg min<sub>θ</sub> Σ<sub>i ∈ 𝒱</sub> w<sub>i</sub> ρ( r<sub>i</sub>(θ) ) + Σ<sub>k</sub> λ<sub>k</sub> R<sub>k</sub>(θ)**

_**θ** — unknown image, motion, geometry, pose, label or network parameters · **r<sub>i</sub>** — an observation residual · **ρ** — a robust penalty · **w<sub>i</sub>** — a confidence or visibility weight · **𝒱** — the set of valid (visible, unoccluded, in-bounds) observations · **R<sub>k</sub>** — priors or regularizers with weights λ<sub>k</sub>._

> **Why this template is worth memorising**
> It makes classical and learned methods _directly comparable_. A network may predict θ instead of an optimiser solving for it, but the loss still encodes what a valid visual explanation should look like. Four questions identify a method: what θ is, what the residual is, what the robust penalty and the visibility set are, and what priors are imposed. Most papers answer only the first and third explicitly — the interesting engineering is usually hidden in **w<sub>i</sub> and 𝒱**.

#### Data terms {#cv-the-shared-pipeline-and-the-objective-template--data-terms}

The residual is where the physics enters. Each data term carries an assumption that, when violated, produces a characteristic failure — listed in the last column and expanded on the [failure-mode checklist](#cv-cross-cutting-mechanisms-and-failure-modes--failures).

| Data term                | Residual being measured                           | Common tasks                                         | Main assumption                                      |
| ------------------------ | ------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| **Photometric**          | Pixel or patch appearance after warping/rendering | Flow, stereo, direct VO, self-supervised depth, NeRF | Corresponding surfaces retain comparable appearance  |
| **Reprojection**         | Observed 2D point versus projected 3D point       | Calibration, PnP, SfM, bundle adjustment             | Camera model and correspondences are valid           |
| **Epipolar**             | Point-to-epipolar-line consistency                | Stereo, two-view pose, SfM initialization            | Rigid two-view projective geometry                   |
| **Feature / descriptor** | Descriptor distance after association             | Registration, retrieval, SLAM, tracking              | Descriptor is invariant to nuisance changes          |
| **Semantic**             | Predicted class distribution versus label         | Classification, detection, segmentation              | Labels are valid and classes well defined            |
| **Region overlap**       | Predicted and target sets / masks / boxes         | Segmentation, detection                              | Spatial overlap represents task utility              |
| **Metric-learning**      | Pair / triplet / contrastive embedding relation   | Retrieval, face recognition, Re-ID                   | Semantic similarity can be represented geometrically |
| **Rendering**            | Rendered pixel / depth / mask versus observation  | NeRF, inverse rendering, 3D reconstruction           | Renderer approximates image formation                |
| **Temporal**             | Prediction or identity consistency across frames  | Tracking, video segmentation, action models          | Relevant state changes smoothly or predictably       |

> **The self-supervision insight hiding in this table**
> Rows 1–4 and 8–9 need **no human labels** — they compare measurements against other measurements under a geometric or physical model. Rows 5–7 need labels. Nearly the whole self-supervised-learning story of 2019–2025 is the field moving work out of the labelled rows and into the unlabelled ones: photometric reprojection replaced labelled depth, rendering residuals replaced labelled geometry, and contrastive/masked objectives manufactured a residual out of the data's own structure.

#### Regularizers and priors {#cv-the-shared-pipeline-and-the-objective-template--regularizers}

Common priors include first- or second-order smoothness, total variation, sparsity, low rank, non-local self-similarity, piecewise planarity, surface-normal consistency, cycle consistency, left–right consistency, forward–backward consistency, rigidity, temporal constancy, entropy control, and shape or topology constraints.

> **Regularization is not numerical decoration**
> It resolves the underdetermination that _remains after_ the data term. The standard case is Horn–Schunck optical flow: the brightness-constancy equation gives one scalar constraint per pixel, but flow has two unknown components per pixel, so the system is underdetermined by construction — the aperture problem. Smoothness is not a convenience there; it is what makes the problem well-posed at all.

- **Spatial priors** — Smoothness (1st/2nd order), total variation, piecewise planarity, surface-normal consistency, edge-aware weighting. Assume the world is locally simple, and encode _where_ it is allowed not to be.

- **Structural priors** — Sparsity, low rank, non-local self-similarity, shape and topology constraints. Assume the signal lives on a much smaller set than the ambient space.

- **Relational priors** — Cycle, left–right, forward–backward and temporal consistency; rigidity. Assume that several estimates of the same quantity must agree — see [the consistency table](#cv-cross-cutting-mechanisms-and-failure-modes--consistency).

#### How to read a method with this template {#cv-the-shared-pipeline-and-the-objective-template--reading}

Given a new paper, the template turns a vague "what does it do" into five answerable questions:

1. **What is θ?** Scene variables, or network parameters, or both in alternation?
2. **What is r<sub>i</sub>?** Which of the nine data terms, and against what — a label, another measurement, or a rendering?
3. **What is 𝒱 and w<sub>i</sub>?** Which observations are excluded, and how is confidence assigned? This is where occlusion, visibility and outlier handling live.
4. **What is ρ?** Squared error, L1, Charbonnier, Huber, Tukey, or a learned/implicit robustness?
5. **What are R<sub>k</sub> and λ<sub>k</sub>?** Which priors, and how are the weights set — tuned, annealed, or learned?

A method that cannot be placed in this template is usually either a pure representation change (a new backbone) or a pure inference change (a new sampler) — both are easier to evaluate once identified as such.

## Image level

### Restoration and enhancement {#cv-restoration-and-enhancement}

_The clearest case in vision where the unknown being optimised is the \_image itself_ — and the family in which the gap between the optimised quantity and the perceived one is provably irreducible.\_

#### The generic degradation model {#cv-restoration-and-enhancement--model}

**Forward model**

$$ \mathbf{y} = \mathcal{D}(\mathbf{x};\,k,s,c) + \mathbf{n} \;=\; \mathbf{S}\_s\big(k \* \mathbf{x}\big) + \mathbf{n} $$

- $$\mathbf{x}$$ — the latent clean image
- $$k$$ — blur kernel / point-spread function
- $$\mathbf{S}_s$$ — sampling or decimation by factor $$s$$
- $$c$$ — camera-response and colour-filter effects
- $$\mathbf{n}$$ — noise, generally signal-dependent

Each task is a different instantiation: denoising sets $$k=\delta$$, $$s=1$$; deblurring keeps $$k$$ non-trivial; super-resolution has $$s>1$$; demosaicing makes $$\mathbf{S}$$ the Bayer pattern; inpainting makes $$\mathbf{S}$$ a binary mask. Restoration inverts it under a prior:

$$ \mathbf{x}^{\*} = \arg\min\_{\mathbf{x}}\; \rho\big(\mathbf{y} - \mathcal{D}(\mathbf{x})\big) \;+\; \lambda R(\mathbf{x}) $$

_This is the [general template](#cv-vision-objectives-and-optimization--template) with $$\theta = \mathbf{x}$$. Without $$R$$ the problem is ill-posed: the forward operator has a near-null space, so infinitely many $$\mathbf{x}$$ explain $$\mathbf{y}$$ equally well._

#### Deconvolution {#cv-restoration-and-enhancement--deblur}

**Wiener filter**

$$ \hat{X}(\boldsymbol{\omega}) = \frac{\overline{K(\boldsymbol{\omega})}}{\lvert K(\boldsymbol{\omega})\rvert^{2} + \dfrac{S_n(\boldsymbol{\omega})}{S_x(\boldsymbol{\omega})}}\;Y(\boldsymbol{\omega}) $$

_The MMSE linear estimator, in the frequency domain. The added noise-to-signal ratio term is what prevents division by near-zero $$K$$ — with zero noise it degenerates to naive inverse filtering, which explodes exactly where the blur has killed the signal. This single term is the whole reason regularization exists in restoration._

**Richardson–Lucy**

$$ \mathbf{x}^{(t+1)} = \mathbf{x}^{(t)} \odot \left( k^{\!_} _ \frac{\mathbf{y}}{k \* \mathbf{x}^{(t)} + \epsilon} \right) $$

_Multiplicative EM iteration for **Poisson** noise; preserves non-negativity and total flux by construction, which is why it dominates in astronomy and microscopy. Amplifies noise as iterations grow — the iteration count is itself the regularizer, and stopping early is the standard practice._

**The four classical deconvolution methods differ only in what is known.** Wiener: $$k$$ known, Gaussian noise, known spectra. Regularized: $$k$$ known, explicit $$R(\mathbf{x})$$. Richardson–Lucy: $$k$$ known, Poisson noise. Blind: $$k$$ unknown, so $$k$$ and $$\mathbf{x}$$ are estimated jointly — which is severely ill-posed, since $$(k*\delta)$$ and $$(\delta*k)$$ explain the data identically, and needs priors on _both_.

#### Classical image priors {#cv-restoration-and-enhancement--priors}

**Total variation (ROF)**

$$ \mathbf{x}^{\*} = \arg\min*{\mathbf{x}} \tfrac{1}{2}\lVert \mathbf{y}-\mathbf{x}\rVert_2^2 + \lambda\sum*{\mathbf{p}}\lVert\nabla\mathbf{x}(\mathbf{p})\rVert_2 $$

_$$\ell_1$$ on gradient magnitude tolerates a few large jumps, so edges survive while noise is removed. The characteristic artefact is **staircasing**: smooth ramps are flattened into piecewise-constant steps, because the prior literally prefers them._

**Non-local means**

$$ \hat{x}(\mathbf{p}) = \frac{1}{Z(\mathbf{p})}\sum*{\mathbf{q}} \exp\!\left(-\frac{\lVert P*\mathbf{p} - P*\mathbf{q}\rVert^2*{2,a}}{h^2}\right) y(\mathbf{q}) $$

_Weights come from similarity of \_patches_ $$P$$, not proximity of pixels. The prior is **self-similarity**: natural images repeat their own structure, so a noisy patch has clean relatives elsewhere in the same image.\_

<a id="cv-restoration-and-enhancement--bm3d"></a>

> **BM3D — the strongest statement of the self-similarity prior**
> Four stages: (1) **block matching** groups similar patches into a 3D stack; (2) a 3D transform is applied and coefficients are **collaboratively shrunk** — because similar patches share structure, the true signal is sparse in that basis while noise is not; (3) estimates are **aggregated** back with weights; (4) the first estimate guides a second **Wiener** pass. It remained the benchmark to beat for nearly a decade, and learned denoisers only clearly surpassed it once they were trained on realistic rather than Gaussian noise.

#### Deep objectives {#cv-restoration-and-enhancement--deep}

| Loss             | Form                                                                  | Effect                                                      |
| ---------------- | --------------------------------------------------------------------- | ----------------------------------------------------------- |
| L2 / MSE         | $$\lVert\hat{\mathbf{x}}-\mathbf{x}\rVert_2^2$$                       | Maximises PSNR; produces the _conditional mean_, hence blur |
| L1 / Charbonnier | $$\lVert\hat{\mathbf{x}}-\mathbf{x}\rVert_1$$                         | Conditional median; visibly sharper than L2 in practice     |
| SSIM / MS-SSIM   | structure, luminance, contrast                                        | Correlates better with perception than PSNR                 |
| Perceptual       | $$\lVert\phi_\ell(\hat{\mathbf{x}})-\phi_\ell(\mathbf{x})\rVert_2^2$$ | Matches deep features, not pixels; recovers texture         |
| Adversarial      | $$-\log D(\hat{\mathbf{x}})$$                                         | Pushes output onto the natural-image manifold               |
| Total variation  | $$\lVert\nabla\hat{\mathbf{x}}\rVert_1$$                              | Suppresses residual noise and ringing                       |
| Frequency / FFT  | $$\lVert\mathcal{F}\hat{\mathbf{x}}-\mathcal{F}\mathbf{x}\rVert$$     | Directly targets missing high-frequency bands               |

**ESRGAN** combines perceptual, adversarial and L1 content terms. It improves perceptual realism and simultaneously _reduces_ PSNR — which is not a bug, and is the cleanest illustration of the following.

> **The perception–distortion tradeoff**
> It is a proven result, not an empirical observation, that distortion (any full-reference metric such as MSE) and perceptual quality (divergence between the output distribution and the natural-image distribution) **cannot both be optimal**. Improving one past a point necessarily degrades the other.
>
> Consequences: report _both_ a fidelity metric and a perceptual metric; never compare a GAN-based method to an MSE-based one on PSNR alone; and **do not deploy a generative restorer in any measurement or safety-critical setting** — it is drawing a plausible sample, not recovering a measurement, and it will hallucinate texture that was never in the scene.

#### Task-specific notes {#cv-restoration-and-enhancement--tasks}

- **Super-resolution** — The degradation used in training _defines_ the method. Bicubic-downsample training generalises poorly to real images; "blind SR" instead randomises blur kernels, noise and compression to cover realistic degradations. Sub-pixel (pixel-shuffle) upsampling avoids the checkerboard artefacts of transposed convolution.

- **Demosaicing** — Recovering three channels from a Bayer mosaic. Best solved _jointly_ with denoising, because independent demosaicing propagates and correlates the noise, after which no denoiser can undo it.

- **HDR and tone mapping** — Estimate the camera response $$f$$, merge bracketed exposures weighted by reliability, then compress dynamic range for display. Merging must happen in **linear light**; tone mapping is a perceptual, not a physical, step.

- **Inpainting** — Classical: diffusion for small gaps, patch-based synthesis (PatchMatch) for texture. Modern: masked diffusion. Large holes are _generation_, not restoration — the information is simply absent.

#### Engineering tricks {#cv-restoration-and-enhancement--tricks}

- **Work in linear light** when the physics demands it — merging, blending and noise modelling are all wrong in gamma space.
- **Use raw sensor data** where possible; the ISP has already applied irreversible non-linearities.
- **Model heteroscedastic noise**, $$\sigma^2(I) = aI + b$$. Constant-$$\sigma$$ Gaussian training under-performs on real data.
- **Tile with overlap** and blend, to avoid seams on large images; pad reflectively rather than with zeros.
- **Augment with realistic degradations** — random kernels, JPEG artefacts, sensor noise — not just additive Gaussian.
- **Report fidelity and perception separately.**
- **Prevent hallucinated detail** wherever the output feeds a measurement.

#### Metrics and failure modes {#cv-restoration-and-enhancement--metrics}

| Metric                                        | Measures               | Caveat                                               |
| --------------------------------------------- | ---------------------- | ---------------------------------------------------- |
| PSNR $$=10\log_{10}\frac{L^2}{\mathrm{MSE}}$$ | Pixel fidelity         | Rewards blur; poor perceptual correlation            |
| SSIM / MS-SSIM                                | Local structure        | Better, still reference-based                        |
| LPIPS                                         | Deep-feature distance  | Correlates well with humans; depends on the backbone |
| FID / NIQE                                    | Distributional realism | No per-image meaning; needs many samples             |

**Failure modes:** staircasing from TV; over-smoothing from L2; hallucinated texture from adversarial losses; ringing from deconvolution near strong edges; colour shifts from per-channel processing; and — most consequentially — **train/test degradation mismatch**, where a model trained on bicubic downsampling collapses on real photographs.

#### Takeaways {#cv-restoration-and-enhancement--takeaways}

1. **All restoration tasks are one forward model** with different $$k$$, $$s$$ and $$\mathbf{S}$$.
2. **The prior is not optional** — the forward operator has a near-null space, so the data alone does not determine the answer.
3. **Classical deconvolution methods differ in what is known**, not in their objective structure.
4. **BM3D is the self-similarity prior taken seriously**, and it set the bar for a decade.
5. **Perception and distortion trade off provably.** Report both; never rank across the tradeoff with one number.
6. **A generative restorer invents plausible detail.** That is a feature for photography and a defect for measurement.

### Features and visual primitives {#cv-features-and-visual-primitives}

_Learned descriptors displaced SIFT and ORB for matching — but the \_structure_ of this pipeline survived intact into learned feature matching, and NMS, invented here, outlived the family by a decade.\_

#### The classical pipeline {#cv-features-and-visual-primitives--pipeline}

Six stages, in this order, for every classical detector–descriptor:

**1 · Smooth at one or more scales**

Differentiation amplifies noise; every derivative is taken of a Gaussian-smoothed image. See [image derivatives](#cv-multiscale-vision-and-filtering--derivatives).

**2 · Compute derivatives or local comparisons**

Gradients for edges and corners, Laplacian/DoG for blobs, intensity comparisons for binary tests (FAST, BRIEF).

**3 · Score candidate points**

A cornerness, edgeness or blobness response per pixel and per scale.

**4 · Non-maximum suppression**

Keep only local maxima of the response. **This is where NMS was invented**, and it took until [DETR](#cv-scale-self-supervision-and-set-prediction--detr) to remove it from detection.

**5 · Refine to subpixel**

Fit a quadratic to the response around the maximum and take its vertex.

**6 · Assign scale and orientation, then describe**

Normalising for scale and dominant orientation is what makes the descriptor invariant.

#### Edges: Canny {#cv-features-and-visual-primitives--edges}

Canny is an optimality argument as well as an algorithm: it maximises a criterion combining good detection, good localisation and a single response per edge. Four stages:

$$ \mathbf{g} = \nabla(G\_\sigma \* I), \qquad M = \lVert\mathbf{g}\rVert_2, \qquad \vartheta = \operatorname{atan2}(g_y, g_x) $$

1. **Gaussian smoothing** at scale $$\sigma$$.
2. **Gradient magnitude and orientation.**
3. **Non-maximum suppression along the gradient direction** — thins ridges to one-pixel width. This is the step that distinguishes Canny from a plain gradient threshold.
4. **Hysteresis thresholding** with $$\tau_{\text{low}} < \tau_{\text{high}}$$: seed edges above $$\tau_{\text{high}}$$, then extend through pixels above $$\tau_{\text{low}}$$ connected to a seed. Two thresholds give continuity that one cannot.

#### Corners: Harris and Shi–Tomasi {#cv-features-and-visual-primitives--harris}

Consider the weighted SSD of a patch against itself under a small shift $$\Delta\mathbf{u}$$:

$$ E(\Delta\mathbf{u}) = \sum\_{\mathbf{q}} w(\mathbf{q})\big[I(\mathbf{q}+\Delta\mathbf{u}) - I(\mathbf{q})\big]^2 \;\approx\; \Delta\mathbf{u}^\top \mathbf{M} \,\Delta\mathbf{u} $$

_with $$\mathbf{M}$$ the [structure tensor](#cv-multiscale-vision-and-filtering--derivatives). A corner is a point where $$E$$ is large in \_every_ direction, i.e. both eigenvalues of $$\mathbf{M}$$ are large.\_

**Corner responses**

$$ R*{\text{Harris}} = \det\mathbf{M} - \kappa\,(\operatorname{tr}\mathbf{M})^2, \qquad R*{\text{Shi–Tomasi}} = \lambda\_{\min} = \min(\lambda_1,\lambda_2) $$

_Harris avoids an eigendecomposition by using $$\det = \lambda_1\lambda_2$$ and $$\operatorname{tr} = \lambda_1+\lambda_2$$, with $$\kappa \approx 0.04$$–$$0.06$$. Shi–Tomasi thresholds $$\lambda_{\min}$$ directly and is the better predictor of whether a patch is _trackable_ — which is why it is called "good features to track" and why it pairs with [Lucas–Kanade](#cv-optical-flow-and-scene-flow--lk), whose solvability requires exactly this matrix to be well-conditioned.\_

> **The aperture problem, stated as linear algebra** > $$\lambda_2 \approx 0$$ means $$\mathbf{M}$$ is rank-deficient: there is a direction along which the patch looks the same, so motion along it is unobservable. That is an edge. Corner detection and the aperture problem are the same statement about the conditioning of one matrix.

#### Blobs and scale selection: DoG and SIFT {#cv-features-and-visual-primitives--sift}

**Difference of Gaussians**

$$ D(x,y,\sigma) = \big(G*{k\sigma} - G*{\sigma}\big) _ I \;\approx\; (k-1)\,\sigma^2\nabla^2 G\_\sigma _ I $$

_A cheap approximation to the scale-normalised Laplacian. Extrema of $$D$$ over the 3D neighbourhood in $$(x,y,\sigma)$$ give both position \_and_ characteristic scale — the mechanism behind scale invariance.\_

**SIFT** in full:

1. Build a Gaussian/DoG pyramid over octaves and sub-scales.
2. Find $$(x,y,\sigma)$$ extrema; refine by fitting a 3D quadratic.
3. **Reject unstable extrema:** low contrast $$\lvert D\rvert < \tau$$, and edge-like responses using the curvature ratio

$$ \frac{\operatorname{tr}(\mathbf{H})^2}{\det(\mathbf{H})} = \frac{(r+1)^2}{r}, \qquad r = \lambda*{\max}/\lambda*{\min} \;\;\text{rejected if}\;\; r > 10 $$

_$$\mathbf{H}$$ is the 2×2 Hessian of $$D$$. The same trace/determinant trick as Harris, reused to discard points that lie along an edge and are therefore poorly localised in one direction._

1. **Assign dominant orientation** from a 36-bin histogram of gradient orientations weighted by magnitude; duplicate the keypoint for each secondary peak above 80% of the maximum.
2. **Describe:** a $$4\times4$$ grid of 8-bin orientation histograms, computed _relative to_ the dominant orientation, giving a 128-D vector; normalise, clip at 0.2, renormalise to reduce the influence of large gradients from illumination change.

#### Fast and binary: FAST, BRIEF, ORB {#cv-features-and-visual-primitives--binary}

- **FAST** — A pixel is a corner if $$n$$ contiguous pixels on a radius-3 Bresenham circle of 16 are all brighter than $$I_p+t$$ or all darker than $$I_p-t$$. A high-speed test on pixels 1, 5, 9, 13 rejects most candidates in a few comparisons.

- **BRIEF** — A binary string from $$n$$ intensity comparisons at fixed sampling pairs: $$b_i = \mathbb{1}[I(\mathbf{a}_i) < I(\mathbf{b}_i)]$$. Matching becomes a Hamming distance — an XOR and a popcount.

- **ORB** — Oriented FAST + rotated BRIEF. Orientation from the intensity centroid, $$\vartheta = \operatorname{atan2}(m_{01}, m_{10})$$; the BRIEF pattern is steered by $$\vartheta$$, and the pairs are _learned_ to be decorrelated and high-variance.

> **Binary descriptors are a hardware argument, not an accuracy one**
> A 256-bit ORB descriptor is matched with XOR + popcount — a handful of CPU instructions — versus 128 floating-point multiply-adds for SIFT. The accuracy is lower; the throughput is one to two orders of magnitude higher. That trade is why ORB, not SIFT, sits inside real-time SLAM.

#### Lines and regions: Hough and MSER {#cv-features-and-visual-primitives--regions}

**Hough transform**

$$ r = x\cos\vartheta + y\sin\vartheta $$

_Each edge pixel votes for every $$(r,\vartheta)$$ line through it, tracing a sinusoid in parameter space; collinear pixels produce intersecting sinusoids, so peaks in the accumulator are lines. The $$(r,\vartheta)$$ parameterisation is used instead of $$y = mx+c$$ precisely because the latter has unbounded $$m$$ for vertical lines. Generalises to circles and arbitrary shapes at the cost of accumulator dimensionality._

**MSER** sweeps an intensity threshold and tracks connected components; a region is _maximally stable_ where its area changes slowly with threshold:

$$ q(t) = \frac{\lvert Q*{t+\Delta}\rvert - \lvert Q*{t-\Delta}\rvert}{\lvert Q_t\rvert} \quad\text{minimised over } t $$

_Affine-covariant and robust to monotonic illumination change, since only the \_ordering_ of intensities matters. Heavily used in text detection, where characters are stable blobs by construction.\_

#### Matching and distances {#cv-features-and-visual-primitives--matching}

**Lowe's ratio test**

$$ \text{accept if}\quad \frac{d_1}{d_2} < \tau, \qquad \tau \approx 0.8 $$

_$$d_1, d_2$$ are the distances to the nearest and second-nearest neighbours. The insight: an \_absolute_ distance threshold is meaningless because descriptor scale varies, but a match that is much better than the runner-up is distinctive. On SIFT this removes ~90% of false matches while discarding ~5% of correct ones.\_

- **Mutual (cross-check) matching:** keep $$(a,b)$$ only if $$b$$ is $$a$$'s nearest neighbour _and_ $$a$$ is $$b$$'s.
- **Distances:** L2 for SIFT-like float descriptors, Hamming for binary, cosine for normalised learned embeddings.
- **Geometric verification** with [RANSAC](#cv-vision-objectives-and-optimization--ransac) is mandatory — the ratio test removes ambiguity, not repeated structure.

#### What replaced this, and what did not {#cv-features-and-visual-primitives--modern}

| Stage                    | Classical         | Learned successor                                            | Survived?                                          |
| ------------------------ | ----------------- | ------------------------------------------------------------ | -------------------------------------------------- |
| Detection                | Harris, FAST, DoG | SuperPoint, R2D2, DISK                                       | Structure kept, operator replaced                  |
| Description              | SIFT, ORB         | HardNet, SOSNet, learned joint det+desc                      | Replaced                                           |
| Matching                 | NN + ratio test   | **SuperGlue / LightGlue** — attention over both sets jointly | Genuinely superseded: matching became _contextual_ |
| Verification             | RANSAC            | RANSAC (still)                                               | **Unreplaced**                                     |
| NMS, subpixel refinement | —                 | —                                                            | **Unreplaced**                                     |

The interesting entry is matching. Classical matching treats each descriptor independently; SuperGlue conditions on the _whole set_ of keypoints in both images via attention, so the assignment respects global consistency — closer in spirit to [set prediction](#cv-scale-self-supervision-and-set-prediction--detr) than to nearest-neighbour search. Note also that [VGGT](#cv-any-view-geometry-concepts-and-embodiment--vggt) dispenses with explicit matching altogether.

#### Failure modes and takeaways {#cv-features-and-visual-primitives--failures}

| Failure                                         | Cause                                                    | Defense                                                              |
| ----------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------------------- |
| Features cluster in one textured region         | Global top-$$k$$ by response                             | Bucketing / spatial quotas — keep features distributed               |
| Repeated texture yields confident wrong matches | Ratio test cannot help; neighbours are genuinely similar | Geometric verification, larger context, cycle consistency            |
| Fails under large viewpoint change              | Similarity-invariant only, not affine                    | Affine-covariant detectors (Hessian-Affine, ASIFT), learned matchers |
| Poor localisation on edges                      | Rank-deficient structure tensor                          | Curvature-ratio rejection (SIFT step 3)                              |
| Blur destroys corners                           | Response scales with gradient magnitude                  | Multi-scale detection; reject low-contrast frames                    |

1. **One matrix — the structure tensor — explains edges, corners and trackability.**
2. **Scale selection needs scale-normalised responses**, otherwise coarse scales never win.
3. **Normalise for orientation and scale _before_ describing.** That is the source of the invariance.
4. **The ratio test works because it is relative**, not absolute.
5. **Binary descriptors trade accuracy for throughput**, deliberately.
6. **The pipeline outlived its operators.** Detect → refine → normalise → describe → match → verify is still the shape of learned matching.

### Correspondence and registration {#cv-correspondence-and-registration}

_Estimating the transformation that aligns two images. The upstream family for stitching, SfM, SLAM, localisation and loop closure — which is why an improvement here propagates everywhere._

#### Two routes to the same answer {#cv-correspondence-and-registration--two-routes}

> **Feature-based (sparse, indirect)**
> Detect → describe → match → reject ambiguous → robustly fit a model → refine on inliers.<br><br> **Minimises a reprojection residual** on a sparse set. Robust to illumination change and large displacement; needs texture and discards most of the image.

> **Direct (dense, photometric)**
> Initialise a warp → transform → compute photometric residuals → linearise → solve → iterate coarse-to-fine.<br><br> **Minimises a [photometric residual](#cv-photometric-consistency)** over all valid pixels. Uses all image gradient, sub-pixel accurate; needs a good initialisation and photometric consistency.

The same split reappears one level up as feature-based vs. direct [visual odometry](#cv-camera-pose-sfm-vo-and-slam--direct). It is the single most consequential architectural choice in geometric vision.

#### The transform hierarchy {#cv-correspondence-and-registration--models}

Choosing the model is choosing how many degrees of freedom the data must support. Each row is a subgroup of the one below it.

| Model             | Matrix                                                                          | DoF  | Invariants                  | Min. points |
| ----------------- | ------------------------------------------------------------------------------- | ---- | --------------------------- | ----------- |
| Translation       | $$\begin{bsmallmatrix}\mathbf{I}&\mathbf{t}\\ \mathbf{0}&1\end{bsmallmatrix}$$  | 2    | Orientation, length, area   | 1           |
| Euclidean         | $$\begin{bsmallmatrix}\mathbf{R}&\mathbf{t}\\ \mathbf{0}&1\end{bsmallmatrix}$$  | 3    | Length, angle, area         | 2           |
| Similarity        | $$\begin{bsmallmatrix}s\mathbf{R}&\mathbf{t}\\ \mathbf{0}&1\end{bsmallmatrix}$$ | 4    | Angle, length ratios        | 2           |
| Affine            | $$\begin{bsmallmatrix}\mathbf{A}&\mathbf{t}\\ \mathbf{0}&1\end{bsmallmatrix}$$  | 6    | Parallelism, area ratios    | 3           |
| Homography        | $$\mathbf{H}$$ (3×3)                                                            | 8    | Straight lines, cross-ratio | 4           |
| Thin-plate spline | —                                                                               | many | Smoothness only             | many        |

> **Choose the simplest model the data supports**
> An over-parameterised warp fits noise and produces alignment that looks plausible and is wrong — the most reliable way to ruin a stitching pipeline. A homography is exact only for a **planar scene** or a **purely rotating camera**. Use it on a translating camera viewing a 3D scene and parallax will make it fail, no matter how many inliers RANSAC reports.

#### Estimating a homography {#cv-correspondence-and-registration--homography}

$$ \tilde{\mathbf{u}}' \sim \mathbf{H}\tilde{\mathbf{u}}, \qquad u' = \frac{h*{11}u + h*{12}v + h*{13}}{h*{31}u + h*{32}v + h*{33}}, \quad v' = \frac{h*{21}u + h*{22}v + h*{23}}{h*{31}u + h*{32}v + h*{33}} $$

Cross-multiplying linearises this; each correspondence gives two equations, so four points determine $$\mathbf{H}$$ up to scale:

$$ \begin{bmatrix} \tilde{\mathbf{u}}^\top & \mathbf{0}^\top & -u'\tilde{\mathbf{u}}^\top \\ \mathbf{0}^\top & \tilde{\mathbf{u}}^\top & -v'\tilde{\mathbf{u}}^\top \end{bmatrix}\mathbf{h} = \mathbf{0} \;\Longrightarrow\; \mathbf{A}\mathbf{h}=\mathbf{0},\quad \mathbf{h} = \text{null}(\mathbf{A}) $$

> **Hartley normalisation is mandatory**
> Raw pixel coordinates are $$O(10^3)$$ while homogeneous entries are $$O(1)$$, so the columns of $$\mathbf{A}$$ differ by three orders of magnitude and the smallest singular vector is dominated by round-off.
>
> Apply a similarity $$\mathbf{T}$$ centring the points and scaling their mean distance to $$\sqrt{2}$$, solve for $$\hat{\mathbf{H}}$$, then un-normalise: $$\mathbf{H} = \mathbf{T}'^{-1}\hat{\mathbf{H}}\mathbf{T}$$. The identical argument applies to the eight-point algorithm for $$\mathbf{F}$$ and to [camera DLT](#cv-calibration-and-sensor-alignment--dlt).

The algebraic (DLT) solution minimises a quantity with no geometric meaning. Always refine it by minimising the **symmetric transfer error** on the inliers:

$$ \mathcal{L}(\mathbf{H}) = \sum_i \Big[ d\big(\mathbf{u}'_i, \mathbf{H}\mathbf{u}_i\big)^2 + d\big(\mathbf{u}_i, \mathbf{H}^{-1}\mathbf{u}'_i\big)^2 \Big] $$

#### Direct alignment: Lucas–Kanade {#cv-correspondence-and-registration--direct}

Minimise photometric error over warp parameters $$\mathbf{p}$$:

$$ \mathbf{p}^{\*} = \arg\min*{\mathbf{p}} \sum*{\mathbf{x}} \Big[ I\big(\mathbf{W}(\mathbf{x};\mathbf{p})\big) - T(\mathbf{x}) \Big]^2 $$

Linearising in $$\Delta\mathbf{p}$$ gives a Gauss–Newton step:

$$ \Delta\mathbf{p} = \mathbf{H}^{-1}\sum*{\mathbf{x}}\left[\nabla I\frac{\partial\mathbf{W}}{\partial\mathbf{p}}\right]^{\!\top}\!\big[T(\mathbf{x}) - I(\mathbf{W}(\mathbf{x};\mathbf{p}))\big], \qquad \mathbf{H} = \sum*{\mathbf{x}}\left[\nabla I\frac{\partial\mathbf{W}}{\partial\mathbf{p}}\right]^{\!\top}\!\left[\nabla I\frac{\partial\mathbf{W}}{\partial\mathbf{p}}\right] $$

_For a pure translation $$\mathbf{W}$$, $$\partial\mathbf{W}/\partial\mathbf{p} = \mathbf{I}$$ and $$\mathbf{H}$$ becomes exactly the [structure tensor](#cv-multiscale-vision-and-filtering--derivatives) — so LK is solvable precisely where Shi–Tomasi says the patch is trackable._

> **Inverse compositional: why it is ~10× faster**
> In the forward formulation $$\nabla I$$ and hence $$\mathbf{H}$$ must be recomputed every iteration, because the warp moves. The **inverse compositional** trick swaps the roles — the increment is applied to the _template_ and inverted, $$\mathbf{W}(\mathbf{x};\mathbf{p}) \leftarrow \mathbf{W}(\mathbf{x};\mathbf{p})\circ\mathbf{W}(\mathbf{x};\Delta\mathbf{p})^{-1}$$ — so $$\nabla T$$, the Jacobian and $$\mathbf{H}$$ are all _constant_ and precomputable. Same convergence, a fraction of the per-iteration cost. This is standard in any real-time tracker.

#### Similarity criteria for direct methods {#cv-correspondence-and-registration--criteria}

| Criterion              | Form                                                                                              | Invariant to                                      | Use                                              |
| ---------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------ |
| SSD / SAD              | $$\sum (I_a-I_b)^2$$ / $$\sum\lvert I_a-I_b\rvert$$                                               | Nothing                                           | Same sensor, same exposure                       |
| **NCC**                | $$\dfrac{\sum (I_a-\bar I_a)(I_b-\bar I_b)}{\sqrt{\sum (I_a-\bar I_a)^2 \sum (I_b-\bar I_b)^2}}$$ | Affine intensity $$aI+b$$                         | Exposure / gain change                           |
| **ECC**                | Normalised correlation maximised over warp                                                        | Affine intensity                                  | Photometric-robust alignment                     |
| **Mutual information** | $$\sum p(a,b)\log\frac{p(a,b)}{p(a)p(b)}$$                                                        | Any monotonic — indeed any statistical — relation | **Cross-modal**: MR/CT, RGB/thermal, image/LiDAR |
| Census / Hamming       | Bit string of local comparisons                                                                   | Monotonic intensity change                        | Stereo on embedded hardware                      |

Mutual information is the one that enables _cross-modal_ registration: it assumes only that the two modalities are statistically dependent, not that bright maps to bright. That is why it dominates in medical registration, where a bone is bright in CT and dark in some MR sequences.

#### Engineering tricks {#cv-correspondence-and-registration--tricks}

- **Mutual nearest-neighbour** plus [Lowe's ratio test](#cv-features-and-visual-primitives--matching) before any model fitting.
- **Normalise points before DLT** — conditioning, not cosmetics.
- **RANSAC / MLESAC / PROSAC**, then refine on all inliers with a robust kernel.
- **Coarse-to-fine** pyramid alignment for direct methods; **inverse compositional** updates for speed.
- **Mask moving objects** — a dynamic region is an outlier population, not noise.
- **Gain and bias compensation**, or use NCC/ECC, whenever exposure varies between frames.
- **Validate the model choice**: if a homography's inlier count collapses as the camera translates, the scene is not planar.

#### Failure modes and takeaways {#cv-correspondence-and-registration--failures}

| Failure                                    | Cause                                              | Defense                                                           |
| ------------------------------------------ | -------------------------------------------------- | ----------------------------------------------------------------- |
| Plausible but wrong alignment              | Over-parameterised transform fitting noise         | Use the simplest valid model; compare inlier counts across models |
| Homography fails with parallax             | Scene not planar, camera translating               | Full 3D model, or local/multi-plane warps                         |
| Direct method converges to a local minimum | Displacement outside the linearisation basin       | Coarse-to-fine; feature-based initialisation                      |
| Alignment drifts with exposure             | SSD is not illumination invariant                  | NCC, ECC, census, or an explicit $$aI+b$$ model                   |
| Repeated texture gives confident garbage   | Ratio test cannot separate genuine near-duplicates | Geometric verification; larger context; cycle consistency         |
| Degenerate RANSAC sample                   | All 4 points collinear / coplanar-degenerate       | Sample checks; degeneracy tests (DEGENSAC)                        |

1. **Feature-based minimises reprojection; direct minimises photometric.** Everything else about the two families follows from that.
2. **Model selection is the highest-leverage decision.** Simplest valid transform, always.
3. **Normalise before DLT.**
4. **Algebraic solutions are initialisations**, not answers — refine on a geometric error.
5. **Inverse compositional makes direct alignment real-time** by making the Hessian constant.
6. **Mutual information is the cross-modal tool**, because it assumes only statistical dependence.

### Image stitching and fusion {#cv-image-stitching-and-fusion}

_Registration estimates a transformation. Stitching adds four problems registration never has to solve: which projection, which seam, which exposure, and how to hide the join._

#### The pipeline {#cv-image-stitching-and-fusion--pipeline}

**1 · Pairwise matching**

Features, matching, and RANSAC homographies between overlapping pairs. See [registration](#cv-correspondence-and-registration).

**2 · Topology and verification**

Build a match graph; verify pairs probabilistically (an overlap is real if inliers $$n_i > \alpha + \beta n_f$$ for the features in the overlap). Discard spurious edges and find connected components — one panorama per component.

**3 · Global alignment**

Bundle-adjust all camera rotations jointly, not pairwise. Pairwise chaining accumulates drift and fails to close the loop on a 360° sweep.

**4 · Choose a projection surface**

Planar, cylindrical or spherical, depending on field of view.

**5 · Exposure compensation**

Solve for per-image gains so overlaps agree photometrically.

**6 · Seam selection**

Cut through regions where images already agree.

**7 · Blending**

Feathering or multiband, to hide the residual step across the seam.

#### Why panoramas are a rotation problem {#cv-image-stitching-and-fusion--rotation}

For a camera rotating about its optical centre, with no translation, the mapping between two views is exactly a homography that depends only on rotation:

$$ \mathbf{H}\_{ij} = \mathbf{K}\_i\,\mathbf{R}\_i\mathbf{R}\_j^{\top}\,\mathbf{K}\_j^{-1} $$

_No depth appears. This is why a panorama can be built with **no 3D reconstruction at all** — and why it breaks the instant the camera translates, since then parallax makes the required warp depend on scene depth._

Global alignment therefore optimises rotations (and optionally focal lengths) over all images at once:

**Global bundle adjustment for panoramas**

$$ \min*{\{\mathbf{R}\_i, f_i\}} \sum*{(i,j)\in\mathcal{E}}\ \sum*{k\in\mathcal{M}*{ij}} \rho\Big( \big\lVert \mathbf{u}^k_i - \pi\big(\mathbf{K}\_i\mathbf{R}\_i\mathbf{R}\_j^\top\mathbf{K}\_j^{-1}\tilde{\mathbf{u}}^k_j\big) \big\rVert \Big) $$

_Rotations are parameterised in $$\mathfrak{so}(3)$$ and updated on the manifold. One rotation must be fixed as the gauge (otherwise the whole solution can be rotated freely). A Huber $$\rho$$ absorbs surviving mismatches._

#### Choosing the projection surface {#cv-image-stitching-and-fusion--projection}

| Surface         | Mapping                                                                                    | Usable FoV                        | Property                                                         |
| --------------- | ------------------------------------------------------------------------------------------ | --------------------------------- | ---------------------------------------------------------------- |
| **Planar**      | $$(x,y) = f(X/Z,\ Y/Z)$$                                                                   | < ~90°                            | Straight lines stay straight; stretches without bound toward 90° |
| **Cylindrical** | $$(\vartheta, h) = \big(f\arctan\frac{X}{Z},\ f\frac{Y}{\sqrt{X^2+Z^2}}\big)$$             | 360° horizontal, limited vertical | Vertical lines stay straight; horizontal lines bow               |
| **Spherical**   | $$(\vartheta,\varphi) = \big(f\arctan\frac{X}{Z},\ f\arctan\frac{Y}{\sqrt{X^2+Z^2}}\big)$$ | Full 360°×180°                    | Only surface that covers everything; distorts near the poles     |

> **The projection choice is forced by field of view**
> A planar panorama cannot exceed 180° even in principle — points at 90° project to infinity. A full sweep requires either curved lines (cylindrical) or polar distortion (spherical). There is no projection that preserves straight lines _and_ covers a hemisphere; this is a statement about differential geometry, not about software.

#### Exposure compensation {#cv-image-stitching-and-fusion--exposure}

Auto-exposure and vignetting make overlapping images disagree in brightness. Solve for per-image gains $$g_i$$ minimising the disagreement over overlaps, with a prior keeping gains near 1 (otherwise $$g_i \to 0$$ is a trivial optimum):

$$ \min*{\{g_i\}}\ \frac{1}{2}\sum*{i}\sum*{j}\ N*{ij}\left(\frac{(g*i\bar I*{ij} - g*j\bar I*{ji})^2}{\sigma_N^2} + \frac{(1-g_i)^2}{\sigma_g^2}\right) $$

- $$\bar I_{ij}$$ — mean intensity of image $$i$$ in the region overlapping $$j$$
- $$N_{ij}$$ — number of overlapping pixels — weights larger overlaps more
- $$\sigma_N,\sigma_g$$ — expected intensity error and expected gain deviation

_Linear least squares in $$\{g_i\}$$. Gain alone cannot fix vignetting, which is spatially varying — hence block-wise gain compensation or an explicit $$\cos^4$$ vignetting model._

#### Seam selection {#cv-image-stitching-and-fusion--seam}

Rather than blending everywhere, cut where the images already agree. Formulate as a labelling problem: assign each output pixel a source image $$\ell(\mathbf{p})$$, minimising

$$ E(\ell) = \sum*{\mathbf{p}} D*{\mathbf{p}}\big(\ell(\mathbf{p})\big) \;+\; \lambda\!\!\sum\_{(\mathbf{p},\mathbf{q})\in\mathcal{N}}\!\! V\big(\ell(\mathbf{p}),\ell(\mathbf{q}),\mathbf{p},\mathbf{q}\big) $$

_$$D$$ penalises using a pixel outside an image's valid region; the pairwise term penalises a seam where the two candidate images \_disagree_: $$V = \lVert I_{\ell(\mathbf{p})}(\mathbf{p}) - I_{\ell(\mathbf{q})}(\mathbf{p})\rVert + \lVert I_{\ell(\mathbf{p})}(\mathbf{q}) - I_{\ell(\mathbf{q})}(\mathbf{q})\rVert$$. Solved by [graph cut](#cv-vision-objectives-and-optimization--discrete) ($$\alpha$$-expansion), or by Dijkstra for a simple two-image strip.\_

> **Seam finding is how moving objects are handled**
> A person who walked through the scene between two shots appears in one image and not the other. Blending averages them into a ghost; a well-placed seam routes _around_ them so only one version survives. This is why seam selection precedes blending, and why "deghosting" is mostly a seam problem rather than a blending problem.

#### Blending {#cv-image-stitching-and-fusion--blending}

> **Feathering (alpha blending)**
> Weight each image by distance to its valid-region boundary: $$ I(\mathbf{p}) = \frac{\sum_k w_k(\mathbf{p})\,I_k(\mathbf{p})}{\sum_k w_k(\mathbf{p})} $$
>
> Cheap. Hides exposure steps well, but **blurs** where alignment is imperfect: averaging misregistered detail destroys it.

> **Multiband (Laplacian pyramid) blending**
> Blend each frequency band over a different spatial extent: $$ L^{\ell}\_{\text{blend}} = \sum_k W^{\ell}\_k \cdot L^{\ell}\_k $$ with the mask $$W$$ blurred more at coarse levels $$\ell$$.
>
> **Low frequencies blend over a wide band** (hiding exposure differences), **high frequencies over a narrow one** (preserving sharpness). Reconstruct by collapsing the pyramid.

Multiband blending is the reason [Laplacian pyramids](#cv-multiscale-vision-and-filtering--pyramids) still matter: the decomposition is _invertible_, so bands can be manipulated independently and the image reconstructed exactly. Gradient-domain (Poisson) blending goes further, solving $$\nabla^2 f = \nabla\!\cdot\!\mathbf{v}$$ to match gradients rather than intensities, which removes visible seams entirely at higher cost.

#### Failure modes {#cv-image-stitching-and-fusion--failures}

| Artefact                        | Cause                                                   | Remedy                                                                            |
| ------------------------------- | ------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Ghosting**                    | Moving objects averaged across images                   | Seam routing around them; median/mode compositing                                 |
| **Parallax misalignment**       | Camera translated; homography invalid                   | Rotate about the no-parallax point; local warps; APAP / as-projective-as-possible |
| **Visible exposure step**       | Gain compensation insufficient or vignetting unmodelled | Block gains, vignetting model, multiband blending                                 |
| **Blur at the join**            | Feathering over misregistered detail                    | Multiband blending; better alignment                                              |
| **Drift / loop not closing**    | Pairwise chaining instead of global alignment           | Global bundle adjustment over all rotations                                       |
| **Extreme stretching at edges** | Planar projection beyond ~90° FoV                       | Cylindrical or spherical surface                                                  |
| **Wavy horizon**                | Unknown or wrong focal length; no up-vector constraint  | Estimate $$f$$ in the bundle; apply a straightening prior on the up vector        |

#### Takeaways {#cv-image-stitching-and-fusion--takeaways}

1. **A panorama is a rotation estimation problem.** No depth appears — and that is exactly why translation breaks it.
2. **Align globally, not pairwise.** Chaining drifts and will not close a loop.
3. **Field of view forces the projection surface**; no surface preserves straight lines over a hemisphere.
4. **Exposure compensation needs a prior on the gains**, or the trivial all-black solution minimises the objective.
5. **Seam finding, not blending, is how moving objects are handled.**
6. **Multiband blending works by giving each frequency its own blend width.**

## Semantic understanding

### Classification, retrieval and recognition {#cv-classification-retrieval-and-recognition}

_The family that produced the backbones everything else uses — and the one where the split between \_closed-set classification_ and _open-set embedding_ matters far more than any architecture choice.\_

#### Two output types, two loss families {#cv-classification-retrieval-and-recognition--two-outputs}

> **Closed set → a distribution over $$C$$ classes**
> Classification, multi-label recognition. Trained with cross-entropy family losses. **Cannot express "none of these"** — softmax always sums to one, which is why a closed-set classifier is confidently wrong on unseen categories.

> **Open set → an embedding $$\mathbf{f}\in\mathbb{R}^d$$**
> Retrieval, face verification, person Re-ID, place recognition. Trained with metric-learning losses. Handles identities never seen in training, because the decision is a _distance_, not a class index.

#### Cross-entropy and its variants {#cv-classification-retrieval-and-recognition--ce}

**Softmax cross-entropy**

$$ p*i = \frac{e^{z_i}}{\sum*{j=1}^{C} e^{z*j}}, \qquad \mathcal{L}*{\text{CE}} = -\sum*{i=1}^{C} y_i \log p_i = -\log p*{y} $$

**Label smoothing**

$$ y_i^{\text{LS}} = (1-\varepsilon)\,y_i + \frac{\varepsilon}{C} $$

_Prevents the logit gap from diverging. Hard targets push $$z_y \to \infty$$ relative to the others, producing over-confident, poorly calibrated models; smoothing caps the optimal gap at a finite value. Typically $$\varepsilon = 0.1$$. It improves accuracy and calibration but \_tightens_ class clusters, which measurably hurts downstream [retrieval and distillation](#cv-classification-retrieval-and-recognition--metric).\_

**Focal loss**

$$ \mathcal{L}\_{\text{FL}} = -\alpha_t (1-p_t)^{\gamma}\log p_t $$

_The modulating factor collapses the contribution of already-confident examples: at $$\gamma=2$$, a sample with $$p_t = 0.9$$ contributes $$100\times$$ less than at $$\gamma = 0$$. Designed for [dense detection](#cv-object-detection--focal), where easy background dominates by orders of magnitude, but useful for any severe imbalance._

**Class-balanced reweighting (effective number)**

$$ w_c = \frac{1-\beta}{1-\beta^{n_c}}, \qquad \beta \in [0,1) $$

_Weighting by $$1/n_c$$ over-corrects, because samples within a class are correlated and redundant. The "effective number" $$\,(1-\beta^{n_c})/(1-\beta)$$ interpolates between no reweighting ($$\beta=0$$) and inverse frequency ($$\beta\to1$$)._

#### Metric-learning losses {#cv-classification-retrieval-and-recognition--metric}

**Contrastive — an _absolute_ criterion**

$$ \mathcal{L} = y\,d^2 + (1-y)\,\max(0,\ m-d)^2, \qquad d = \lVert \mathbf{f}\_a - \mathbf{f}\_b\rVert_2 $$

_Pulls positives to zero distance, pushes negatives beyond a margin $$m$$. The weakness is that $$m$$ is a global constant in a space whose scale is arbitrary._

**Triplet — a _relative_ criterion**

$$ \mathcal{L} = \big[\, d(\mathbf{f}_a,\mathbf{f}_p) - d(\mathbf{f}_a,\mathbf{f}_n) + m \,\big]\_{+} $$

_Only the \_ordering_ must hold: the positive must be closer than the negative by $$m$$. Far less sensitive to the embedding's global scale, which is why triplet largely displaced contrastive for retrieval.\_

**Angular margin (ArcFace)**

$$ \mathcal{L} = -\log \frac{e^{s\cos(\vartheta*{y}+m)}}{e^{s\cos(\vartheta*{y}+m)} + \sum\_{j\neq y} e^{s\cos\vartheta_j}}, \qquad \cos\vartheta_j = \frac{\mathbf{W}\_j^\top\mathbf{f}}{\lVert\mathbf{W}\_j\rVert\lVert\mathbf{f}\rVert} $$

_Normalise both weights and features onto a hypersphere of radius $$s$$, then add an **additive angular** margin $$m$$ to the target class before the softmax. CosFace instead subtracts a cosine margin, $$\cos\vartheta_y - m$$. The key advantage over triplet: it needs **no pair or triplet sampling** — every sample compares against all class centres at once, which removes the entire mining problem._

**InfoNCE — the self-supervised workhorse**

$$ \mathcal{L} = -\log\frac{\exp(\mathbf{q}\cdot\mathbf{k}^{+}/\tau)}{\sum\_{i=0}^{K}\exp(\mathbf{q}\cdot\mathbf{k}\_i/\tau)} $$

_A $$(K{+}1)$$-way classification among one positive and $$K$$ negatives. $$\tau$$ controls how sharply the loss concentrates on hard negatives: small $$\tau$$ makes it nearly a max over negatives. This is the objective behind [MoCo](#cv-scale-self-supervision-and-set-prediction--moco), [SimCLR](#cv-scale-self-supervision-and-set-prediction--simclr) and [CLIP](#cv-the-transformer-takeover--clip)._

#### Sampling and hard-negative mining {#cv-classification-retrieval-and-recognition--mining}

With $$N$$ samples there are $$O(N^3)$$ triplets, almost all of which are already satisfied and contribute zero gradient. Mining is therefore not an optimisation — it is what makes training possible at all.

| Strategy             | Selects                                 | Behaviour                                                                                                                           |
| -------------------- | --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Random               | Any triplet                             | Gradient vanishes quickly; slow convergence                                                                                         |
| **Hardest** negative | $$\arg\min_n d(a,n)$$                   | **Collapses.** The hardest negatives are usually label noise or near-duplicates, so the model learns to map everything to one point |
| **Semi-hard**        | $$d(a,p) < d(a,n) < d(a,p)+m$$          | Informative but not pathological. The standard choice.                                                                              |
| Batch-hard           | Hardest within a $$P\!\times\!K$$ batch | Bounded hardness by construction; strong for Re-ID                                                                                  |

> **Semi-hard mining exists because hardest-negative mining fails**
> The highest-loss examples are frequently mislabelled ones, so a scheme that up-weights the highest-loss samples also up-weights the label noise. The same tension is why [robust losses](#cv-vision-objectives-and-optimization--map) and hard mining pull in opposite directions and must be balanced deliberately.

#### Augmentation: Mixup and CutMix {#cv-classification-retrieval-and-recognition--augmentation}

$$ \textbf{Mixup:}\quad \tilde{\mathbf{x}} = \lambda\mathbf{x}\_a + (1-\lambda)\mathbf{x}\_b, \qquad \tilde{y} = \lambda y_a + (1-\lambda) y_b, \qquad \lambda\sim\mathrm{Beta}(\alpha,\alpha) $$ $$ \textbf{CutMix:}\quad \tilde{\mathbf{x}} = \mathbf{M}\odot\mathbf{x}\_a + (\mathbf{1}-\mathbf{M})\odot\mathbf{x}\_b, \qquad \tilde{y} = \lambda y_a + (1-\lambda)y_b,\quad \lambda = \frac{\lvert\mathbf{M}\rvert}{HW} $$

_Mixup interpolates images and labels globally; CutMix pastes a rectangular patch and mixes targets \_by area_. CutMix keeps local statistics natural (no ghostly superpositions) and forces the model to use partial evidence, which is why it transfers better to localisation tasks.\_

#### Confidence calibration {#cv-classification-retrieval-and-recognition--calibration}

A model is calibrated if, among predictions made with confidence $$p$$, a fraction $$p$$ are correct. Modern networks are systematically **over-confident**.

**Expected Calibration Error**

$$ \mathrm{ECE} = \sum\_{b=1}^{B}\frac{\lvert B_b\rvert}{n}\Big\lvert \operatorname{acc}(B_b) - \operatorname{conf}(B_b)\Big\rvert $$

_Bin predictions by confidence and measure the gap between accuracy and confidence in each bin._

**Temperature scaling**

$$ \hat{p}\_i = \frac{e^{z_i/T}}{\sum_j e^{z_j/T}}, \qquad T \ \text{fit on a held-out set by NLL} $$

_A single scalar, fitted post hoc. It does not change the arg-max, so accuracy is unchanged, and it removes most of the miscalibration. It is the strongest baseline in the area and should be the default before anything more elaborate. **But it does not survive distribution shift** — a $$T$$ fitted in-domain is wrong out-of-domain, which is the [open problem](#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--open)._

#### Classical and deep pipelines {#cv-classification-retrieval-and-recognition--pipelines}

> **Classical**
> Normalise → handcrafted features (colour histograms, LBP, [HOG, SIFT](#cv-features-and-visual-primitives)) → encode (bag-of-visual-words, Fisher vectors, VLAD) → train an SVM or logistic regression. The encoding step aggregates local descriptors into a fixed-length vector — Fisher vectors do so via gradients of a GMM likelihood, and remained competitive until roughly 2012.

> **Deep**
> Augment → encode with a CNN or [ViT](#cv-the-transformer-takeover--vit) → pool (global average, or GeM $$\big(\frac1n\sum f^p\big)^{1/p}$$ for retrieval) → classify or L2-normalise into an embedding → calibrate → optionally retrieve nearest neighbours with an ANN index.

#### Metrics {#cv-classification-retrieval-and-recognition--metrics}

| Task           | Metric                              | Note                                                               |
| -------------- | ----------------------------------- | ------------------------------------------------------------------ |
| Classification | Top-1 / Top-5 accuracy              | Assumes balanced classes; use balanced accuracy otherwise          |
| Multi-label    | mAP over classes                    | Per-class AP averaged; robust to imbalance                         |
| Retrieval      | mAP, Recall@K, mean reciprocal rank | mAP rewards ranking _all_ positives highly                         |
| Verification   | ROC-AUC, TAR@FAR                    | TAR at a fixed low FAR ($$10^{-6}$$) is what matters operationally |
| Re-ID          | Rank-1, mAP                         | Rank-1 alone hides how well the rest of the gallery is ordered     |
| Calibration    | ECE, NLL, Brier                     | Orthogonal to accuracy — report separately                         |

#### Failure modes and takeaways {#cv-classification-retrieval-and-recognition--failures}

| Failure                           | Cause                                             | Defense                                                                 |
| --------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------- |
| Confident on unseen classes       | Softmax cannot express "none of the above"        | Open-set methods, energy/OOD scores, abstention threshold               |
| Embedding collapse                | Hardest-negative mining on noisy labels           | Semi-hard or batch-hard mining                                          |
| Shortcut learning                 | Background or watermark correlates with the label | Grouped splits, augmentation, attribution audits                        |
| Long-tail collapse                | Head classes dominate the gradient                | Class-balanced loss, decoupled classifier retraining, balanced sampling |
| Over-confidence                   | Hard targets drive logit gaps up                  | Label smoothing, temperature scaling                                    |
| Retrieval fails after fine-tuning | Label smoothing over-compresses clusters          | Train the embedding without smoothing                                   |

1. **Closed-set and open-set are genuinely different problems.** Pick the output type before the architecture.
2. **Relative criteria score above absolute ones** — triplet over contrastive, for reasons of scale invariance.
3. **Angular-margin losses removed the mining problem** by comparing against class centres rather than sampled pairs.
4. **The hardest examples are not the most useful.** Aggressive mining amplifies label noise.
5. **Calibration is orthogonal to accuracy**, cheap to fix in-domain, and unsolved out-of-domain.
6. **This family supplies everyone else's backbone**, which is why its advances propagate field-wide.

### Object detection {#cv-object-detection}

_The family where the decade's clearest structural progression happened: dense enumeration → set prediction → open vocabulary. Three hand-designed components removed, one per stage._

#### The detection objective {#cv-object-detection--objective}

$$ \mathcal{L}_{\text{det}} = \lambda_{\text{cls}}\mathcal{L}_{\text{cls}} + \lambda_{\text{obj}}\mathcal{L}_{\text{obj}} + \lambda_{\text{box}}\mathcal{L}_{\text{box}} + \lambda_{\text{aux}}\mathcal{L}\_{\text{aux}} $$

_The weights are a persistent source of irreproducibility: they interact with the label-assignment rule, the batch size and the image resolution, and are rarely transferable between datasets._

{% include figure.liquid loading="lazy" path="assets/img/cv/fasterrcnn_rpn.png" class="img-fluid rounded z-depth-1" zoomable=true alt="Faster R-CNN Region Proposal Network sliding over the shared feature map, classifying k anchors per location." caption="<strong>The Region Proposal Network.</strong> The step that absorbed the last hand-built stage — Selective Search — into the network. <em>Ren, He, Girshick & Sun, NeurIPS 2015 (arXiv:1506.01497).</em>" %}

#### Anchors and box parameterisation {#cv-object-detection--anchors}

An anchor is a prior box of fixed scale and aspect ratio tiled over the feature map. The network regresses an _offset_ rather than absolute coordinates, because offsets are scale-normalised and therefore learnable with a single set of weights across the image:

**R-CNN box encoding**

$$ t_x = \frac{x - x_a}{w_a},\quad t_y = \frac{y - y_a}{h_a},\quad t_w = \log\frac{w}{w_a},\quad t_h = \log\frac{h}{h_a} $$

_The $$\log$$ on size makes the target symmetric — halving and doubling are equal-magnitude errors — and guarantees positive width and height after decoding. Subscript $$a$$ denotes the anchor._

**Smooth L1 (Huber on box offsets)**

$$ \operatorname{smooth}\_{L_1}(x) = \begin{cases} 0.5x^2 & \lvert x\rvert < 1 \\ \lvert x\rvert - 0.5 & \text{otherwise}\end{cases} $$

_Quadratic near zero for stable gradients on good boxes, linear far away so a badly-placed anchor cannot dominate the batch._

**Anchor-free** alternatives predict the four distances from a point to the box sides (FCOS), or a pair of corner keypoints grouped by embedding (CornerNet), or a centre plus size (CenterNet). These remove the anchor hyperparameters — scales, ratios, and the IoU thresholds that assign them — but not duplicate suppression.

#### Label assignment — the quiet centre of the field {#cv-object-detection--assignment}

Label assignment fixes which predictions are responsible for which ground-truth object. It accounts for more of the COCO AP gained between 2019 and 2022 than the backbone does.

| Scheme               | Rule                                                          | Problem it addresses                                             |
| -------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------- |
| IoU threshold        | Positive if $$\mathrm{IoU} > 0.5$$ (0.7 for RPN)              | Simple; but small objects match few anchors                      |
| Centre sampling      | Only points near the object centre may be positive            | Low-quality positives at object edges                            |
| **ATSS**             | Adaptive threshold = mean + std of candidate IoUs, per object | A fixed threshold suits neither large nor small objects          |
| **OTA / SimOTA**     | Optimal transport: assignment as a global cost-minimisation   | Per-object greedy assignment ignores competition between objects |
| **Hungarian (DETR)** | One-to-one bipartite matching                                 | Removes duplicates _by construction_; no NMS needed              |

> **One-to-many versus one-to-one**
> One-to-many assignment gives rich supervision and fast convergence, but produces duplicates that must be filtered. One-to-one produces no duplicates but supervises sparsely and converges slowly — the reason [DETR needed 500 epochs](#cv-scale-self-supervision-and-set-prediction--detr). [YOLOv10's](#cv-3d-becomes-real-time-vision-learns-to-talk--yolov10) resolution is to train _both_ heads with a _consistent_ matching metric so they rank candidates identically, then discard the one-to-many head at inference. Set prediction reaches real-time latency this way.

#### Class imbalance and focal loss {#cv-object-detection--focal}

A dense detector scores $$\sim10^5$$ locations per image; the overwhelming majority are trivially negative. Summed, they dominate the gradient even though each term is individually small.

$$ \mathcal{L}\_{\text{FL}}(p_t) = -\alpha_t\,(1-p_t)^{\gamma}\log(p_t), \qquad p_t = \begin{cases} p & y=1\\ 1-p & \text{otherwise}\end{cases} $$

{% include figure.liquid loading="lazy" path="assets/img/cv/focal_loss.png" class="img-fluid rounded z-depth-1" zoomable=true alt="Focal loss curves for several gamma values compared with cross-entropy." caption="<strong>The modulating factor.</strong> At $$\gamma = 2$$ a well-classified example ($$p_t = 0.9$$) contributes 100× less than under plain cross-entropy. <em>Lin, Goyal, Girshick, He & Dollár, ICCV 2017.</em>" %}

Later refinements make the classification target reflect _localisation_ quality rather than a binary label: **Quality Focal Loss** regresses a soft target equal to the IoU with the matched box, and **Varifocal Loss** weights positives and negatives asymmetrically. Both address the same mismatch — the ranking used by NMS is a classification score, but the quantity that matters is box quality.

#### The IoU loss family {#cv-object-detection--iou}

$$ \mathrm{IoU} = \frac{\lvert B \cap B^{gt}\rvert}{\lvert B \cup B^{gt}\rvert}, \qquad \mathcal{L}\_{\text{IoU}} = 1 - \mathrm{IoU} $$

_**The flaw:** if the boxes do not overlap, $$\mathrm{IoU} = 0$$ regardless of how far apart they are, so the gradient is zero and the box receives no signal about which way to move._

**GIoU — restores gradient on disjoint boxes**

$$ \mathrm{GIoU} = \mathrm{IoU} - \frac{\lvert C \setminus (B\cup B^{gt})\rvert}{\lvert C\rvert} $$

_$$C$$ is the smallest axis-aligned box enclosing both. The penalty term grows as the boxes separate, so $$\mathrm{GIoU}\in[-1,1]$$ and the gradient never vanishes._

**DIoU and CIoU — faster convergence, aspect-ratio awareness**

$$ \mathrm{DIoU} = \mathrm{IoU} - \frac{\rho^2(\mathbf{b},\mathbf{b}^{gt})}{c^2}, \qquad \mathrm{CIoU} = \mathrm{DIoU} - \alpha v $$ $$ v = \frac{4}{\pi^2}\left(\arctan\frac{w^{gt}}{h^{gt}} - \arctan\frac{w}{h}\right)^{2}, \qquad \alpha = \frac{v}{(1-\mathrm{IoU}) + v} $$

_$$\rho$$ is the centre distance and $$c$$ the enclosing box's diagonal. DIoU pulls centres together directly (GIoU can waste iterations enlarging the box instead); CIoU adds an aspect-ratio consistency term $$v$$._

> **Why this family exists at all**
> It is the clearest instance in the field of deliberately **closing the gap between the surrogate loss and the evaluation metric**. Smooth L1 optimises coordinates; the metric is IoU; the two disagree, especially across scales, because an equal coordinate error means very different IoU for a small and a large box. See [objective–metric mismatch](#cv-evaluation-and-failure-analysis--mismatch).

#### Non-maximum suppression, and its removal {#cv-object-detection--nms}

Sort by score; greedily keep the top box; delete every box with $$\mathrm{IoU} > \tau$$ against it; repeat.

**Soft-NMS — decay instead of delete**

$$ s_i \leftarrow s_i\,\exp\!\left(-\frac{\mathrm{IoU}(\mathcal{M}, b_i)^2}{\sigma}\right) $$

_Hard NMS deletes a genuinely distinct object that happens to overlap — the failure case for crowds. Soft-NMS decays its score instead, so a correct but overlapping detection can still survive if its score was high enough._

- **Class-aware vs. class-agnostic:** suppressing across classes removes duplicate detections of the same object under different labels, but also deletes genuinely overlapping objects of different classes.
- **NMS is a latency cost** as well as an accuracy choice: it is sequential and data-dependent, which is poor for accelerators. Removing it therefore has a deployment consequence as well as an accuracy one.
- **The removal path**: [DETR](#cv-scale-self-supervision-and-set-prediction--detr) (bipartite matching, 2020) → [YOLOv10](#cv-3d-becomes-real-time-vision-learns-to-talk--yolov10) (consistent dual assignment, 2024) → [YOLO26](#cv-any-view-geometry-concepts-and-embodiment--yolo26) (natively one-to-one, 2025).

#### Set prediction {#cv-object-detection--set}

**Bipartite matching**

$$ \hat{\sigma} = \arg\min*{\sigma\in\mathfrak{S}\_N}\sum*{i=1}^{N}\mathcal{L}_{\text{match}}\big(y_i, \hat{y}_{\sigma(i)}\big) $$ $$ \mathcal{L}_{\text{match}} = -\mathbb{1}_{\{c*i\neq\varnothing\}}\hat{p}*{\sigma(i)}(c*i) + \mathbb{1}*{\{c*i\neq\varnothing\}}\Big[\lambda*{L*1}\lVert b_i - \hat{b}*{\sigma(i)}\rVert*1 + \lambda*{\text{giou}}\mathcal{L}\_{\text{giou}}\Big] $$

_Solved in $$O(N^3)$$ by the Hungarian algorithm. Because the assignment is a **bijection**, two predictions cannot claim the same object, so duplicate suppression is trained into the loss. Ground truth is padded to $$N$$ with $$\varnothing$$._

#### Metrics {#cv-object-detection--metrics}

**Average Precision**

$$ \mathrm{AP} = \int*0^1 p(r)\,dr \;\approx\; \sum_n (r_n - r*{n-1})\,p*{\text{interp}}(r_n), \qquad p*{\text{interp}}(r) = \max\_{\tilde r \ge r} p(\tilde r) $$

_COCO's headline metric averages AP over IoU thresholds $$0.50\!:\!0.05\!:\!0.95$$ and over classes, and additionally reports $$\mathrm{AP}_S$$, $$\mathrm{AP}_M$$, $$\mathrm{AP}_L$$ by object area. **The size breakdown is the informative part**: a single AP number aggregates over the small-object regime, where the methods differ most._

#### Tricks and failure modes {#cv-object-detection--tricks}

> **Tricks that reliably help**
>
> - [FPN](#cv-depth-detection-and-the-first-believable-images--fpn) neck; multi-scale training and testing
> - Mosaic and copy-paste augmentation; scale jitter
> - EMA of weights; longer schedules with strong augmentation
> - **Tiled inference** for small objects in large images
> - Ignore regions for ambiguous or crowd-labelled areas

> **Failure modes**
>
> - **Small objects** — too few positive anchors; resolution lost to striding
> - **Crowds** — NMS deletes true positives
> - **Score/quality mismatch** — a confident but badly localised box is the one NMS keeps
> - **Closed vocabulary** — everything unlisted is background
> - **Domain shift** — anchor priors and thresholds are dataset-specific

#### Takeaways {#cv-object-detection--takeaways}

1. **Label assignment, not the backbone, drove most of the AP gains** from 2019 to 2022.
2. **Focal loss fixed a loss problem, not an architecture problem.** One-stage detectors were never structurally inferior.
3. **The IoU loss family exists to close the surrogate–metric gap**, and each member fixes a specific gradient pathology of the previous one.
4. **One-to-many converges fast but needs NMS; one-to-one needs no NMS but converges slowly.** Consistent dual assignment resolves the dilemma.
5. **NMS is a latency cost as well as an accuracy compromise.**
6. **Read AP by object size.** The aggregate number hides where the methods differ.

### Segmentation and matting {#cv-segmentation-and-matting}

_Four output types that look similar and are optimised very differently — and the one family where the evaluation metric was eventually adopted \_as_ the loss.\_

#### Four tasks, four outputs {#cv-segmentation-and-matting--tasks}

| Task         | Output per pixel                                 | Handles                                          | Metric               |
| ------------ | ------------------------------------------------ | ------------------------------------------------ | -------------------- |
| **Semantic** | Class label $$c \in \{1..C\}$$                   | "Stuff" and "things" alike; no instances         | mIoU                 |
| **Instance** | Mask + class per object                          | Countable "things"; may overlap; ignores "stuff" | Mask AP              |
| **Panoptic** | $$(c, \text{id})$$ — exhaustive, non-overlapping | Both, in one consistent partition                | PQ                   |
| **Matting**  | Continuous opacity $$\alpha \in [0,1]$$          | Hair, smoke, motion blur, glass                  | SAD, MSE, Grad, Conn |

{% include figure.liquid loading="lazy" path="assets/img/cv/panoptic_task.png" class="img-fluid rounded z-depth-1" zoomable=true alt="One input image with its semantic, instance and panoptic ground truth." caption="<strong>The same image, three outputs.</strong> Semantic labels amorphous stuff; instance separates countable things; panoptic assigns every pixel a class and, where applicable, an instance id. <em>Kirillov, He, Girshick, Rother & Dollár, CVPR 2019.</em>" %}

#### The four loss families {#cv-segmentation-and-matting--losses}

##### 1 · Pixel-distribution losses {#cv-segmentation-and-matting--pixel}

$$ \mathcal{L}_{\text{CE}} = -\frac{1}{\lvert\Omega\rvert}\sum_{\mathbf{p}\in\Omega}\sum\_{c=1}^{C} w_c\, y_c(\mathbf{p})\log \hat{p}\_c(\mathbf{p}) $$

_Decomposes over pixels, so it is easy to optimise and well-behaved — but it is **blind to shape**: a prediction missing a thin structure entirely may have a lower loss than one that gets it roughly right, because the thin structure is a handful of pixels._

##### 2 · Region-overlap losses {#cv-segmentation-and-matting--overlap}

**Soft Dice**

$$ \mathcal{L}_{\text{Dice}} = 1 - \frac{2\sum_{\mathbf{p}} \hat{p}(\mathbf{p})\,y(\mathbf{p}) + \epsilon}{\sum*{\mathbf{p}} \hat{p}(\mathbf{p})^2 + \sum*{\mathbf{p}} y(\mathbf{p})^2 + \epsilon} $$

_A differentiable relaxation of the Dice coefficient, using soft probabilities rather than a threshold. **Self-normalising**: the denominator scales with object size, so a tiny object contributes as much as a large one. This is why Dice is the default in medical imaging, where the target may occupy 0.1% of the volume._

**Tversky — asymmetric control of FP vs FN**

$$ \mathcal{L}\_{\text{Tv}} = 1 - \frac{TP + \epsilon}{TP + \alpha\,FP + \beta\,FN + \epsilon} $$

_$$\alpha=\beta=0.5$$ recovers Dice; $$\beta > \alpha$$ penalises false negatives more, which matches screening applications where a miss costs more than a false alarm._

**Lovász–Softmax**

$$ \mathcal{L}_{\text{Lov}} = \overline{\Delta_{J_c}}\big(\mathbf{m}(c)\big), \qquad m_i(c) = \begin{cases}1-\hat{p}\_i(c) & y_i = c\\ \hat{p}\_i(c) & \text{otherwise}\end{cases} $$

_The \_Lovász extension_ is the tight convex surrogate of a submodular set function — and the Jaccard (IoU) loss is submodular. So this is, in a precise sense, the correct convex relaxation of IoU rather than an ad-hoc one. Computed by sorting the errors and taking a dot product with the gradient of the extension.\_

##### 3 · Boundary losses {#cv-segmentation-and-matting--boundary}

$$ \mathcal{L}_{\text{bd}} = \sum_{\mathbf{p}\in\Omega}\phi\_{G}(\mathbf{p})\,\hat{p}(\mathbf{p}), \qquad \phi_G = \text{signed distance transform of the GT boundary} $$

_Weights each prediction by its distance from the true boundary, so errors far from the contour cost more than errors adjacent to it. Overlap losses under-weight thin structures and boundary precision; this family compensates. Related: Hausdorff-distance losses and topology-aware (persistent-homology) losses that preserve connectivity._

##### 4 · Compound and task-specific {#cv-segmentation-and-matting--compound}

In practice almost every strong system uses a **compound**: mask BCE + Dice is the standard for instance masks; CE + Lovász or CE + boundary for semantic segmentation. The rationale is that CE provides well-conditioned early gradients while the overlap term aligns the objective with the metric.

#### Panoptic quality {#cv-segmentation-and-matting--panoptic}

$$ \mathrm{PQ} = \underbrace{\frac{\sum*{(p,g)\in TP}\mathrm{IoU}(p,g)}{\lvert TP\rvert}}*{\text{segmentation quality (SQ)}}\times\underbrace{\frac{\lvert TP\rvert}{\lvert TP\rvert + \tfrac12\lvert FP\rvert + \tfrac12\lvert FN\rvert}}\_{\text{recognition quality (RQ)}} $$

_RQ is exactly the $$F_1$$ score over segments. Matching at $$\mathrm{IoU} > 0.5$$ is **provably unique** — at most one prediction can exceed half overlap with a given ground-truth segment — which is what makes the metric well-defined without a greedy tie-break._

#### Classical algorithms {#cv-segmentation-and-matting--classical}

- **Thresholding & morphology** — Otsu's method picks the threshold maximising between-class variance. Followed by connected components and morphological opening/closing to clean up.

- **Watershed** — Treat intensity as topography and flood from markers. Over-segments badly without marker control — the classic remedy is marker-controlled watershed on a gradient image.

- **Active contours / level sets** — Evolve a curve to minimise an energy of image and smoothness terms. Level sets handle topology changes (splitting, merging) naturally by representing the curve implicitly.

**Graph cuts and GrabCut**

$$ E(\mathbf{L}) = \sum*{\mathbf{p}} D*{\mathbf{p}}(L*\mathbf{p}) + \lambda\!\!\sum*{(\mathbf{p},\mathbf{q})\in\mathcal{N}}\!\! V*{\mathbf{p}\mathbf{q}}(L*\mathbf{p},L*\mathbf{q}), \qquad V*{\mathbf{p}\mathbf{q}} \propto \exp\!\left(-\frac{\lVert I*\mathbf{p}-I*\mathbf{q}\rVert^2}{2\sigma^2}\right) $$

_For two labels with a submodular pairwise term this is solved **exactly** by max-flow/min-cut. GrabCut iterates: fit GMM colour models to current foreground/background, run the cut, refit. The contrast-sensitive pairwise term encodes the prior that label boundaries coincide with intensity edges — the same prior a [CRF](#cv-segmentation-and-matting--crf) imposes post hoc._

#### Dense CRF refinement {#cv-segmentation-and-matting--crf}

$$ E(\mathbf{x}) = \sum*i \psi_u(x_i) + \sum*{i<j}\psi*p(x_i,x_j), \qquad \psi_p = \mu(x_i,x_j)\sum*{m}w^{(m)}k^{(m)}(\mathbf{f}\_i,\mathbf{f}\_j) $$

_With Gaussian kernels over position and colour, mean-field inference is $$O(N)$$ per iteration via the permutohedral lattice, making a \_fully connected_ CRF over every pixel pair tractable. It was the standard post-process for DeepLab v1/v2, and was dropped once networks (atrous convolution, decoders, stronger backbones) learned sharp boundaries directly — a clean example of a [post-processing prior being absorbed into the model](#cv-cross-cutting-mechanisms-and-failure-modes--postproc).\_

#### Matting {#cv-segmentation-and-matting--matting}

**The compositing equation**

$$ I*{\mathbf{p}} = \alpha*{\mathbf{p}} F*{\mathbf{p}} + (1-\alpha*{\mathbf{p}}) B*{\mathbf{p}}, \qquad \alpha*\mathbf{p}\in[0,1] $$

_**Severely under-determined:** 3 equations (RGB) and 7 unknowns ($$\alpha$$, $$F$$, $$B$$) per pixel. Hence the need for a trimap marking definite foreground, definite background and the unknown band — or a strong learned prior._

**Closed-form matting** assumes $$F$$ and $$B$$ are locally constant, which makes $$\alpha$$ locally linear in the image and yields a sparse "matting Laplacian" $$\mathbf{L}$$; $$\alpha$$ is then the solution of a sparse linear system with the trimap as boundary conditions. Deep matting adds:

- **Alpha loss** $$\lVert\hat\alpha - \alpha\rVert_1$$ (or Charbonnier).
- **Compositional loss** $$\lVert \hat\alpha F + (1-\hat\alpha)B - I\rVert_1$$ — enforces that the predicted matte actually reproduces the observed image.
- **Gradient and Laplacian-pyramid losses** for crisp hair and fibre detail.

#### Tricks {#cv-segmentation-and-matting--tricks}

- **Preserve rare classes in crop sampling.** Uniform random crops remove the rare classes; sample crops conditioned on containing one.
- **Ignore labels** for ambiguous pixels (boundaries, void regions) so they contribute no gradient rather than a wrong one.
- **Online hard-example mining** or top-$$k$$ loss over pixels.
- **Auxiliary losses at intermediate resolutions** (deep supervision) to stabilise deep decoders.
- **Atrous / dilated convolution** and pyramid pooling for context without resolution loss.
- **Sliding-window inference with overlap** at test time; average logits, not labels.
- **Point-sampled loss** (as in [Mask2Former](#cv-foundation-models-and-the-promptable-paradigm--mask2former)) instead of dense mask loss — a large memory saving at equal accuracy.

#### Failure modes and takeaways {#cv-segmentation-and-matting--failures}

| Failure                         | Cause                                                   | Defense                                               |
| ------------------------------- | ------------------------------------------------------- | ----------------------------------------------------- |
| Thin structures vanish          | CE and overlap losses under-weight few-pixel regions    | Boundary or topology-aware loss; higher resolution    |
| Boundaries blurred              | Stride-induced resolution loss; label noise at contours | Decoder with skips, atrous conv, boundary refinement  |
| Rare classes never predicted    | Frequency imbalance dominates the loss                  | Class weighting, balanced crops, Dice/Lovász          |
| Dice unstable early in training | Near-empty predictions give tiny, noisy denominators    | Warm up with CE; use a compound loss                  |
| Instance masks merge in crowds  | One-to-many assignment plus mask NMS                    | Query-based set prediction (Mask2Former)              |
| Matting fails without a trimap  | The problem is genuinely under-determined               | Trimap, background capture, or a strong learned prior |

1. **Choose the loss family by what the metric rewards.** Dice for imbalance, Lovász for IoU, boundary for thin structure.
2. **Lovász is the principled IoU surrogate**, not a heuristic — it is the tight convex extension of a submodular function.
3. **Compound losses win** because CE conditions the early gradients and the overlap term aligns with the metric.
4. **PQ works because the $$\mathrm{IoU}>0.5$$ match is unique.**
5. **CRFs encoded a prior the network later learned.** A post-processing stage is a prior that has not been trained.
6. **Matting is under-determined by construction** — 3 equations, 7 unknowns — so it always needs an external constraint.

### Keypoints and pose {#cv-keypoints-and-pose}

_Localising semantic points rather than corners — and the family where a single representational choice, heatmap versus coordinate, determined a decade of accuracy._

#### Corners versus semantic keypoints {#cv-keypoints-and-pose--taxonomy}

> **A different problem from [feature detection](#cv-features-and-visual-primitives)**
> A Harris corner is defined by _local image structure_ and is repeatable but anonymous — any corner will do. A semantic keypoint ("left elbow", "nose tip") is defined by _meaning_, may sit in a textureless region, and must be identified consistently across subjects and viewpoints. The first is found by an operator; the second must be learned.

#### Heatmaps versus direct regression {#cv-keypoints-and-pose--representation}

**Gaussian heatmap target**

$$ H*k(\mathbf{p}) = \exp\!\left(-\frac{\lVert \mathbf{p} - \mathbf{p}\_k^{\*}\rVert^2}{2\sigma^2}\right), \qquad \mathcal{L} = \frac{1}{K}\sum*{k=1}^{K} v_k \lVert \hat{H}\_k - H_k\rVert_2^2 $$

_$$v_k$$ is a visibility flag — occluded joints must not be supervised, or the network learns to hallucinate them at the mean position. $$\sigma$$ trades localisation precision against gradient coverage: too small and almost every pixel is background, too large and the peak is imprecise._

> **Why heatmaps replaced direct regression**
> The output stays **spatial**: the network never has to convert a spatial activation into a number, a mapping convolutions are structurally poor at. Every pixel receives gradient, and multi-modal ambiguity is representable. The cost is quantisation to the heatmap grid and $$O(K \cdot HW)$$ memory.

> **Why regression came back**
> Direct coordinate regression is cheap, resolution-independent and end-to-end differentiable — which matters when pose feeds a downstream geometric loss. **Soft-argmax** closed most of the accuracy gap by making the two nearly equivalent.

**Soft-argmax / integral regression**

$$ \hat{\mathbf{p}}_k = \sum_{\mathbf{p}\in\Omega} \mathbf{p}\cdot\frac{\exp(\beta\,\hat{H}_k(\mathbf{p}))}{\sum_{\mathbf{q}}\exp(\beta\,\hat{H}\_k(\mathbf{q}))} $$

_The expectation of position under the normalised heatmap. Differentiable, sub-pixel by construction, and it lets a coordinate loss be applied to a spatial representation — combining both advantages. $$\beta$$ controls sharpness; as $$\beta\to\infty$$ it approaches a hard arg-max. **Caveat:** an expectation is a poor summary of a bimodal heatmap, e.g. left/right ambiguity, where it returns a point between the two modes that is correct for neither._

Standard refinements: quarter-pixel offset correction using the local gradient of the heatmap around the peak; unbiased encoding–decoding (DARK) that corrects the systematic bias introduced by discretising the Gaussian.

#### Top-down versus bottom-up {#cv-keypoints-and-pose--multiperson}

|                | Top-down (detect then pose)                                             | Bottom-up (pose then group)                        |
| -------------- | ----------------------------------------------------------------------- | -------------------------------------------------- |
| **Procedure**  | Detect people → crop → single-person pose per crop                      | Detect all joints in the image → group into people |
| **Cost**       | Linear in the number of people                                          | Constant in the number of people                   |
| **Accuracy**   | Higher — the crop normalises scale                                      | Lower, especially for small people                 |
| **Fails when** | The detector misses a person; heavy overlap puts two people in one crop | Crowds make grouping ambiguous                     |

**Part Affinity Fields — grouping by line integral**

$$ E = \int*{u=0}^{1} \mathbf{L}\_c\big(\mathbf{p}(u)\big)\cdot\frac{\mathbf{d}*{j*2}-\mathbf{d}*{j*1}}{\lVert\mathbf{d}*{j*2}-\mathbf{d}*{j*1}\rVert}\,du, \qquad \mathbf{p}(u) = (1-u)\,\mathbf{d}*{j*1} + u\,\mathbf{d}*{j_2} $$

_$$\mathbf{L}_c$$ is a 2-channel vector field for limb $$c$$, pointing along the limb. The integral scores how well the field between two candidate joints agrees with the direction connecting them; bipartite matching on these scores assembles skeletons. The alternative, **associative embedding**, predicts a scalar tag per joint and groups by tag similarity — simpler, with no explicit limb model._

#### From 2D to 6-DoF: PnP {#cv-keypoints-and-pose--pnp}

Given $$n \ge 3$$ correspondences between known 3D model points $$\mathbf{X}_i$$ and image points $$\mathbf{u}_i$$, recover $$(\mathbf{R},\mathbf{t})$$:

$$ (\mathbf{R}^{_},\mathbf{t}^{_}) = \arg\min*{\mathbf{R},\mathbf{t}} \sum*{i=1}^{n}\rho\Big(\big\lVert\mathbf{u}\_i - \pi(\mathbf{K},\mathbf{R},\mathbf{t},\mathbf{X}\_i)\big\rVert^2\Big) $$

_P3P gives up to four solutions from three points — a fourth disambiguates. EPnP solves the general case in $$O(n)$$ by expressing points in a basis of four virtual control points. In practice: **P3P inside RANSAC** for the hypothesis, then nonlinear refinement on all inliers. The minimal sample of 3 is what makes RANSAC cheap here._

#### 6-DoF object pose and its metrics {#cv-keypoints-and-pose--6dof}

**ADD — average distance for distinguishable objects**

$$ \mathrm{ADD} = \frac{1}{\lvert\mathcal{M}\rvert}\sum\_{\mathbf{x}\in\mathcal{M}}\big\lVert(\mathbf{R}\mathbf{x}+\mathbf{t}) - (\hat{\mathbf{R}}\mathbf{x}+\hat{\mathbf{t}})\big\rVert $$

**ADD-S — for symmetric objects**

$$ \mathrm{ADD\text{-}S} = \frac{1}{\lvert\mathcal{M}\rvert}\sum*{\mathbf{x}\_1\in\mathcal{M}}\min*{\mathbf{x}\_2\in\mathcal{M}}\big\lVert(\mathbf{R}\mathbf{x}\_1+\mathbf{t}) - (\hat{\mathbf{R}}\mathbf{x}\_2+\hat{\mathbf{t}})\big\rVert $$

_A pose is counted correct if the distance is below 10% of the object diameter._

> **Symmetry is not a detail — it breaks the loss**
> For a rotationally symmetric object (a bowl, a bottle, a bolt) many distinct rotations produce an identical image. A naive rotation loss punishes a _correct_ prediction that happens to pick a different-but-equivalent representative, so the network is trained to be wrong and converges to the mean of the equivalent poses. The fix is to make the loss **symmetry-aware** — the $$\min$$ in ADD-S — or to restrict the target to a canonical fundamental domain.

**Rotation geodesic loss**

$$ d(\mathbf{R},\hat{\mathbf{R}}) = \arccos\!\left(\frac{\operatorname{tr}(\mathbf{R}^{\top}\hat{\mathbf{R}}) - 1}{2}\right) $$

_The angle of the relative rotation — the true geodesic distance on $$SO(3)$$, unlike an $$\ell_2$$ distance between quaternions or matrix entries, which is not._

#### 3D human pose {#cv-keypoints-and-pose--3dpose}

- **MPJPE** — mean per-joint position error after aligning the root joint. **PA-MPJPE** aligns by Procrustes (similarity), removing global rotation, translation and scale; it is the fairer number for monocular methods, which cannot recover scale.
- **Lifting** 2D to 3D is ambiguous up to depth reflection per joint. Priors that resolve it: bone-length constancy, joint-angle limits, temporal smoothness, and a learned pose prior (e.g. a body model such as SMPL).
- **Reprojection loss** $$\lVert \pi(\mathbf{X}_{3\text{D}}) - \mathbf{u}_{2\text{D}}\rVert$$ allows weak supervision from 2D annotations alone — the same [reprojection residual](#cv-vision-objectives-and-optimization--data-terms) used in calibration and SfM.

**Bone-length prior**

$$ \mathcal{L}_{\text{bone}} = \sum_{(i,j)\in\mathcal{E}} \Big( \lVert\mathbf{X}_i - \mathbf{X}\_j\rVert - \ell_{ij} \Big)^{2} $$

#### OKS: the keypoint analogue of IoU {#cv-keypoints-and-pose--oks}

$$ \mathrm{OKS} = \frac{\sum_i \exp\!\left(-\dfrac{d_i^2}{2s^2\kappa_i^2}\right)\delta(v_i > 0)}{\sum_i \delta(v_i > 0)} $$

- $$d_i$$ — distance between predicted and ground-truth keypoint $$i$$
- $$s$$ — object scale (square root of segment area)
- $$\kappa_i$$ — per-keypoint falloff constant, calibrated from human annotator variance
- $$v_i$$ — visibility flag

_The $$\kappa_i$$ are the interesting part: they are measured from \_inter-annotator disagreement_, so the metric tolerates more error on joints humans themselves localise inconsistently (hips) than on precise ones (eyes). AP is then computed over OKS thresholds exactly as detection AP is over IoU.\_

#### Tricks and failure modes {#cv-keypoints-and-pose--tricks}

> **Tricks**
>
> - Gaussian heatmap targets with visibility masking
> - Soft-argmax plus quarter-pixel offset correction
> - **Flip testing** — average predictions over a horizontal flip, remembering to swap left/right joint indices
> - Multi-stage refinement with intermediate supervision
> - RANSAC-PnP, then ICP refinement when depth is available
> - Kinematic constraints and temporal smoothing

> **Failure modes**
>
> - **Left/right confusion** — the classic bimodal heatmap; flip augmentation without index swapping _causes_ it
> - **Occluded joints hallucinated** at the dataset mean
> - **Crowds** — top-down crops contain two people; bottom-up grouping fails
> - **Symmetric objects** — non-symmetry-aware loss trains toward the mean pose
> - **Truncation** — joints outside the crop have no valid heatmap target
> - **Scale/depth ambiguity** in monocular 3D — report PA-MPJPE

#### Takeaways {#cv-keypoints-and-pose--takeaways}

1. **Keeping the output spatial is why heatmaps score above regression**; soft-argmax then recovered regression's advantages.
2. **Soft-argmax is an expectation**, so it fails silently on genuinely bimodal predictions.
3. **Top-down buys accuracy with linear cost; bottom-up buys constant cost with grouping risk.**
4. **PnP is the bridge from 2D keypoints to 6-DoF pose**, and its 3-point minimal sample makes RANSAC cheap.
5. **Symmetry must be built into the loss**, or the loss actively trains the wrong answer.
6. **OKS calibrates tolerance to human annotator variance** — a metric design idea worth borrowing elsewhere.

### Text and document vision {#cv-text-and-document-vision}

_A pipeline distinct enough to deserve separate treatment: the output is a \_sequence_, not a label or a box, and the alignment between image and sequence is unknown.\_

#### Why this differs from detection plus classification {#cv-text-and-document-vision--why}

> **The structural difference**
> Detection outputs an unordered _set_; classification outputs one _label_. Text recognition outputs an ordered _sequence of variable length_, with no supervision about which image column produced which character. That missing alignment is the whole technical problem, and it is why CTC and attention decoders — borrowed from speech — are the core machinery here rather than anything from object detection.

#### Text detection {#cv-text-and-document-vision--detection}

Text is not a generic object: instances are extreme-aspect-ratio, densely packed, arbitrarily oriented and often curved. Three representations, in order of generality:

| Representation         | Parameterisation                     | Handles                     |
| ---------------------- | ------------------------------------ | --------------------------- |
| Rotated box            | $$(x,y,w,h,\vartheta)$$              | Oriented straight text      |
| Quadrilateral          | 4 corner points                      | Perspective-distorted text  |
| **Segmentation-based** | Per-pixel text/non-text + separation | Curved and arbitrary shapes |

Segmentation-based detectors face one specific problem: adjacent text lines merge into one blob. Two standard answers — **shrink masks** (predict a shrunken kernel per instance, then dilate to recover the full extent, as in PSENet/DBNet) and **link prediction** (predict whether neighbouring pixels belong to the same instance).

**Differentiable binarization (DBNet)**

$$ \hat{B}_{\mathbf{p}} = \frac{1}{1 + e^{-k\,(P_{\mathbf{p}} - T\_{\mathbf{p}})}} $$

_A hard threshold is not differentiable, so the threshold map $$T$$ cannot be learned. Replacing the step with a steep sigmoid ($$k\approx50$$) makes the binarization differentiable, so the network learns an \_adaptive, per-pixel_ threshold jointly with the probability map $$P$$. A small idea with a large effect on curved-text accuracy.\_

**MSER** remains relevant here: characters are, by construction, regions that stay stable over a range of thresholds, which is exactly what [MSER](#cv-features-and-visual-primitives--regions) detects.

#### Recognition I: CTC {#cv-text-and-document-vision--ctc}

The image is sliced into $$T$$ frames left-to-right; the network emits a distribution over the alphabet plus a _blank_ at each frame. CTC marginalises over every alignment consistent with the target string.

**CTC objective**

$$ p(\mathbf{y}\mid\mathbf{x}) = \sum*{\boldsymbol{\pi}\in\mathcal{B}^{-1}(\mathbf{y})} \prod*{t=1}^{T} p(\pi*t \mid \mathbf{x}), \qquad \mathcal{L}*{\text{CTC}} = -\log p(\mathbf{y}\mid\mathbf{x}) $$

- $$\boldsymbol{\pi}$$ — a frame-level path over alphabet $$\cup\ \{\text{blank}\}$$
- $$\mathcal{B}$$ — the collapsing map: remove repeats, then remove blanks

_The blank is what allows repeated characters: "ll" is emitted as `l–blank–l`, which survives collapsing, whereas `l–l` would collapse to a single "l". The sum over exponentially many paths is computed in $$O(T\lvert\mathbf{y}\rvert)$$ by the forward–backward algorithm._

> **CTC's conditional-independence assumption**
> CTC factorises $$p(\boldsymbol{\pi}\mid\mathbf{x}) = \prod_t p(\pi_t\mid\mathbf{x})$$ — outputs are independent given the input. So the model has **no internal language model** and cannot use "q is followed by u" unless the visual evidence says so. This is why CTC decoding is usually combined with an external n-gram or neural language model via beam search, and why attention decoders outperform it on noisy text.

#### Recognition II: attention and transformers {#cv-text-and-document-vision--attention}

$$ p(\mathbf{y}\mid\mathbf{x}) = \prod*{t=1}^{L} p(y_t \mid y*{<t}, \mathbf{x}), \qquad \mathcal{L} = -\sum*{t=1}^{L}\log p(y_t\mid y*{<t},\mathbf{x}) $$

_Autoregressive: each character is conditioned on the previous ones, so the decoder learns an implicit language model. Strictly more expressive than CTC, at the cost of sequential decoding and a tendency to **hallucinate fluent-but-wrong text** when the image evidence is weak — the language prior overrides the pixels._

**Attention drift** is the characteristic failure: on long or low-quality text the alignment wanders and the decoder either repeats or truncates. Standard mitigations are a monotonic-alignment penalty, a CTC auxiliary head to anchor the alignment, and coverage penalties borrowed from machine translation.

#### Geometric rectification {#cv-text-and-document-vision--rectification}

Scene text is rarely fronto-parallel. Rectifying before recognition is worth several points, and is done with a learned **thin-plate spline**:

**Thin-plate spline warp**

$$ f(\mathbf{p}) = \mathbf{A}\begin{bmatrix}\mathbf{p}\\1\end{bmatrix} + \sum\_{i=1}^{K} w_i\,U\big(\lVert\mathbf{p}-\mathbf{c}\_i\rVert\big), \qquad U(r) = r^2\log r^2 $$

_An affine part plus a sum of radial basis functions at $$K$$ control points $$\mathbf{c}_i$$. It is the interpolant that minimises bending energy $$\iint (f_{xx}^2 + 2f*{xy}^2 + f*{yy}^2)$$. A localisation network predicts the control points, the grid is sampled differentiably, and the whole rectifier trains end-to-end with the recogniser (the STN/RARE recipe).\_

For document images the analogous step is **dewarping** — undoing page curl and perspective, typically by predicting a dense backward-mapping flow field.

#### Document layout and structure {#cv-text-and-document-vision--layout}

- **Layout analysis** — Detect and classify regions: title, paragraph, list, figure, caption, table, header/footer. Treated as ordinary object detection or instance segmentation, but with a strong reading-order prior.

- **Table structure** — Two sub-problems: detection (where is the table) and _structure recognition_ (rows, columns, spanning cells). Output is a grid or an HTML/LaTeX string — so it is a sequence task again, with a tree-shaped target.

- **Formula recognition** — Image-to-LaTeX. Strictly a structured sequence task: the target is a token sequence whose validity is governed by a grammar, so decoding benefits from constrained beam search.

**2D positional encoding for documents**

$$ \mathbf{e}_i = \mathbf{E}_{\text{tok}}(w*i) + \mathbf{E}*{x}(x*0) + \mathbf{E}*{y}(y*0) + \mathbf{E}*{x}(x*1) + \mathbf{E}*{y}(y*1) + \mathbf{E}*{\text{img}}(\mathbf{v}\_i) $$

_The LayoutLM family's core idea: a document token carries \_where it is on the page_ as well as what it says. Reading order alone is insufficient — a two-column paper, a form, or an invoice is only interpretable with spatial layout, and 1D sequence position actively misleads.\_

#### OCR-free document understanding {#cv-text-and-document-vision--ocrfree}

The pipeline _detect → recognise → layout → reason_ compounds errors: a missed character propagates to a wrong field value. **OCR-free** models (Donut, Pix2Struct, and modern [VLMs](#cv-vision-language-understanding)) read the page image directly and emit structured output — JSON, an answer, a table — with no explicit text-detection stage.

> **Where this family currently stands**
> Document understanding is the **strongest capability of modern VLMs**: Qwen2.5-VL reports 96.4% on DocVQA, and the same models exceed 90% on chart understanding. That sits in sharp contrast with their ~30–45% on fine-grained shape and pattern recognition. The pattern is consistent — these models _read_ text in images extremely well and _reason about geometry_ in them poorly. See [the 2024–2025 consolidation](#cv-video-depth-and-concepts--vlm).

#### Metrics {#cv-text-and-document-vision--metrics}

| Level             | Metric                 | Definition / note                                                                           |
| ----------------- | ---------------------- | ------------------------------------------------------------------------------------------- |
| Character         | **CER**                | $$(S+D+I)/N$$ — edit distance over characters, normalised by reference length               |
| Word              | **WER**                | Same, over words. Can exceed 1.                                                             |
| Word (scene text) | Exact-match accuracy   | Usually case-insensitive and alphanumeric-only — read the protocol before comparing numbers |
| Detection         | H-mean (F1) at IoU 0.5 | Precision/recall over text instances                                                        |
| End-to-end        | Spotting F1            | Detection and transcription must _both_ be right                                            |
| Table             | TEDS                   | Tree-edit distance over the HTML structure, so it scores structure and content jointly      |
| Document VQA      | ANLS                   | Average normalised Levenshtein similarity — tolerates minor OCR slips in the answer         |

#### Failure modes and takeaways {#cv-text-and-document-vision--failures}

| Failure                       | Cause                                                    | Defense                                                    |
| ----------------------------- | -------------------------------------------------------- | ---------------------------------------------------------- |
| Hallucinated fluent text      | Attention decoder's language prior overrides weak pixels | CTC auxiliary head; confidence thresholding; abstention    |
| Attention drift on long lines | Alignment wanders; repeats or truncates                  | Monotonic alignment penalty; coverage; CTC anchor          |
| Adjacent lines merge          | Segmentation-based detector without separation           | Shrink masks, link prediction, differentiable binarization |
| Curved / perspective text     | Box representation too rigid                             | Polygon output plus TPS rectification                      |
| Rare scripts and diacritics   | Long-tailed character distribution                       | Synthetic rendering, balanced sampling, subword units      |
| Reading order wrong           | 1D sequence order assumed on a 2D page                   | 2D positional encoding; explicit layout model              |
| Compounding pipeline errors   | Detect → recognise → parse chained                       | OCR-free end-to-end model                                  |

1. **The unknown image-to-sequence alignment is the core problem**, and CTC and attention are two different answers to it.
2. **CTC has no language model; attention has too much of one.** Their failure modes are exact opposites.
3. **Rectify before recognising** — learned TPS warping is worth several points on scene text.
4. **Documents need 2D position**; reading order alone destroys the information that makes forms and tables interpretable.
5. **OCR-free models remove error compounding** and are now the strongest capability VLMs have.
6. **Check the evaluation protocol** — scene-text accuracy is usually case-insensitive and alphanumeric-only, which flatters it.

## Motion and geometry

### Optical flow and scene flow {#cv-optical-flow-and-scene-flow}

_One scalar equation per pixel, two unknowns per pixel. Everything in this family is a different way of supplying the missing constraint._

#### Brightness constancy {#cv-optical-flow-and-scene-flow--bcc}

Assume a scene point keeps its intensity between frames:

$$ I(x, y, t) = I(x + u\,\delta t,\; y + v\,\delta t,\; t + \delta t) $$

A first-order Taylor expansion gives the **optical flow constraint equation**:

**Optical flow constraint**

$$ I_x u + I_y v + I_t = 0 \qquad\Longleftrightarrow\qquad \nabla I \cdot \mathbf{v} + I_t = 0 $$

- $$I_x, I_y$$ — spatial image gradients
- $$I_t$$ — temporal derivative
- $$(u,v)$$ — the unknown flow

_Note what the linearisation costs: it is valid only for **small** displacements, since $$I$$ must be locally well-approximated by its tangent plane. Large motion must be handled by warping or by an explicit correspondence search._

#### The aperture problem {#cv-optical-flow-and-scene-flow--aperture}

> **One equation, two unknowns — per pixel**
> The constraint determines only the flow component _parallel to the gradient_: $$ v\_{\perp} = \frac{-I_t}{\lVert\nabla I\rVert} $$ The component along an edge is completely unconstrained. Viewed through a small aperture, a moving edge gives no evidence of motion along its own direction.
>
> This is the same statement as a rank-deficient [structure tensor](#cv-multiscale-vision-and-filtering--derivatives). Corner detection, trackability and flow observability are one question asked three ways.

#### Horn–Schunck: global smoothness {#cv-optical-flow-and-scene-flow--hs}

$$ E(u,v) = \iint \underbrace{\big(I*x u + I_y v + I_t\big)^2}*{\text{data}} \;+\; \lambda\underbrace{\big(\lVert\nabla u\rVert^2 + \lVert\nabla v\rVert^2\big)}\_{\text{smoothness}}\; dx\,dy $$

The Euler–Lagrange equations give a linear system solved by Jacobi iteration:

$$ u^{(k+1)} = \bar{u}^{(k)} - \frac{I_x\big(I_x\bar{u}^{(k)} + I_y\bar{v}^{(k)} + I_t\big)}{\lambda^{-1} + I_x^2 + I_y^2}, \qquad v^{(k+1)} = \bar{v}^{(k)} - \frac{I_y(\cdots)}{\lambda^{-1} + I_x^2 + I_y^2} $$

_$$\bar u, \bar v$$ are local averages. Each pixel's flow is pulled toward its neighbours' average and corrected along the gradient — information \_propagates_ from textured regions into textureless ones. That propagation is what makes the underdetermined problem solvable, and it is why the quadratic smoothness term also blurs motion boundaries.\_

#### Lucas–Kanade: local constancy {#cv-optical-flow-and-scene-flow--lk}

Assume flow is constant in a window $$W$$ and solve the resulting over-determined system by weighted least squares:

$$ \begin{bmatrix}\sum w I_x^2 & \sum w I_xI_y\\ \sum w I_xI_y & \sum w I_y^2\end{bmatrix}\begin{bmatrix}u\\v\end{bmatrix} = -\begin{bmatrix}\sum w I_xI_t\\ \sum w I_yI_t\end{bmatrix} \qquad\Longleftrightarrow\qquad \mathbf{M}\mathbf{v} = -\mathbf{b} $$

_$$\mathbf{M}$$ is exactly the structure tensor. It is invertible precisely where [Shi–Tomasi](#cv-features-and-visual-primitives--harris) says the patch is a good corner — which is why KLT tracks corners and not edges, and why "good features to track" is literally the name of that criterion._

**Horn–Schunck vs. Lucas–Kanade** is the dense-global vs. sparse-local split: HS regularises with a smoothness prior and yields flow everywhere; LK regularises by assuming local constancy and yields flow only where $$\mathbf{M}$$ is well-conditioned.

#### Making the data term robust {#cv-optical-flow-and-scene-flow--robust}

**Robust variational flow**

$$ E = \int \rho_D\big(\lvert I_2(\mathbf{x}+\mathbf{w}) - I_1(\mathbf{x})\rvert\big) + \gamma\,\rho_D\big(\lvert \nabla I_2(\mathbf{x}+\mathbf{w}) - \nabla I_1(\mathbf{x})\rvert\big) + \lambda\,\rho_S\big(\lVert\nabla\mathbf{w}\rVert\big)\,d\mathbf{x} $$

_Three upgrades over Horn–Schunck: (1) the residual uses the full warped image rather than its linearisation, so large motion is representable; (2) a **gradient-constancy** term adds invariance to additive brightness change; (3) $$\rho$$ is a robust penalty — typically Charbonnier $$\sqrt{r^2+\epsilon^2}$$ — on both data and smoothness, so occlusions and motion boundaries are not over-penalised._

The **census transform** goes further on illumination robustness: encode each pixel by the bit pattern of comparisons with its neighbours, and compare by Hamming distance. Only the local _ordering_ of intensities matters, so any monotonic photometric change is absorbed.

#### Cost volumes and correlation {#cv-optical-flow-and-scene-flow--costvolume}

$$ \mathbf{C}(\mathbf{x}, \mathbf{d}) = \frac{1}{N}\,\mathbf{f}\_1(\mathbf{x})^{\top}\mathbf{f}\_2(\mathbf{x}+\mathbf{d}) $$

_Correlating learned features rather than raw pixels makes the matching cost explicit and differentiable. A 2D flow search over displacements $$\mathbf{d}$$ gives a 4D volume $$H\times W\times (2R{+}1)\times(2R{+}1)$$ — expensive, which is why classical deep flow (FlowNet, PWC-Net) restricted $$\mathbf{d}$$ to a small range and used a coarse-to-fine pyramid to cover large motion._

> **RAFT: all-pairs correlation plus a recurrent operator**
> Coarse-to-fine has a structural flaw: a small, fast-moving object _disappears_ at coarse levels, and the pyramid has already committed to the background motion before the fine level ever sees it.
>
> RAFT builds **all-pairs** correlation once, at a single high resolution, pools it into a 4-level pyramid _over displacement_ (not over image scale), and then iteratively refines a flow field with a shared **GRU** that looks up correlation at the current estimate: $$ \mathbf{f}^{(k+1)} = \mathbf{f}^{(k)} + \Delta\mathbf{f}^{(k)}, \qquad \Delta\mathbf{f}^{(k)} = \mathrm{GRU}\big(\mathbf{h}^{(k)},\ \mathbf{C}(\mathbf{f}^{(k)}),\ \mathbf{f}^{(k)}\big) $$ One operator applied many times instead of a cascade of different ones. The result was a large accuracy gain _and_ unusually strong cross-dataset generalisation. The same structural move appears in [SlowFast](#cv-video-understanding--slowfast) and in diffusion samplers.

**Sequence loss over iterations**

$$ \mathcal{L} = \sum*{k=1}^{K}\gamma^{\,K-k}\,\big\lVert \mathbf{f}^{(k)} - \mathbf{f}*{gt}\big\rVert_1, \qquad \gamma \approx 0.8 $$

_Every iterate is supervised, with exponentially increasing weight. This is what makes the recurrent operator converge rather than drift, and it is the same trick as DETR's auxiliary per-layer decoder losses._

#### Occlusion and consistency {#cv-optical-flow-and-scene-flow--occlusion}

**Forward–backward consistency check**

$$ \big\lVert \mathbf{f}_{1\to2}(\mathbf{x}) + \mathbf{f}_{2\to1}\big(\mathbf{x}+\mathbf{f}_{1\to2}(\mathbf{x})\big) \big\rVert^2 < \alpha_1\Big(\lVert\mathbf{f}_{1\to2}\rVert^2 + \lVert\mathbf{f}\_{2\to1}\rVert^2\Big) + \alpha_2 $$

_Warp forward, then backward; the result returns to the starting point. Failure indicates occlusion or a mismatch. The threshold is made \_relative_ to flow magnitude because absolute tolerance would reject all fast motion.\_

Occluded pixels have no correspondence _by definition_, so their photometric residual is meaningless. They must be excluded from the data term — this is the $$\mathcal{V}$$ set in the [objective template](#cv-vision-objectives-and-optimization--template) — via forward–backward checks, a predicted occlusion mask, or range checks for out-of-bounds warps.

#### Scene flow {#cv-optical-flow-and-scene-flow--sceneflow}

$$ \mathbf{s}(\mathbf{X}) = \big(\Delta X, \Delta Y, \Delta Z\big), \qquad \mathbf{f}\_{\text{2D}} = \pi\big(\mathbf{X} + \mathbf{s}\big) - \pi(\mathbf{X}) $$

_Optical flow is the \_projection_ of scene flow. Recovering 3D motion needs depth as well: from stereo (disparity at $$t$$ and $$t{+}1$$ plus flow), from RGB-D, or from a point cloud pair. For LiDAR the task is point-wise 3D displacement, evaluated with 3D endpoint error and "accuracy strict" (fraction of points within 5 cm or 5%).\_

#### Metrics {#cv-optical-flow-and-scene-flow--metrics}

**Endpoint error**

$$ \mathrm{EPE} = \frac{1}{\lvert\Omega\rvert}\sum*{\mathbf{x}\in\Omega}\big\lVert \hat{\mathbf{f}}(\mathbf{x}) - \mathbf{f}*{gt}(\mathbf{x})\big\rVert_2 $$

- **Fl-all** (KITTI): percentage of pixels with EPE $$> 3$$ px _and_ $$> 5\%$$ of the ground-truth magnitude — an outlier rate rather than an average, which is far more informative for driving.
- **Breakdowns matter**: report EPE separately for all / noc (non-occluded) / occ, and for small vs. large displacement. A method can win on average while failing entirely on fast motion.

#### Failure modes and takeaways {#cv-optical-flow-and-scene-flow--failures}

| Failure                                | Cause                                           | Defense                                                   |
| -------------------------------------- | ----------------------------------------------- | --------------------------------------------------------- |
| Textureless regions get arbitrary flow | Data term is flat; only the prior acts          | Smoothness, larger context, semantic priors               |
| Small fast objects lost                | Coarse-to-fine erases them at coarse levels     | All-pairs correlation at single resolution (RAFT)         |
| Motion boundaries over-smoothed        | Quadratic smoothness penalises jumps            | Robust $$\rho_S$$, edge-aware weighting                   |
| Occlusion regions corrupt the estimate | No valid correspondence exists                  | Forward–backward check, occlusion prediction              |
| Illumination change breaks matching    | Brightness constancy violated                   | Gradient constancy, census transform                      |
| Specular / transparent surfaces        | Appearance is view-dependent                    | Robust penalties; there is no full fix                    |
| Sim-to-real gap                        | Trained on synthetic flow (FlyingChairs/Things) | Strong augmentation; architectures that generalise (RAFT) |

1. **One equation, two unknowns.** Every method is a different missing constraint — global smoothness, local constancy, or a learned prior.
2. **The aperture problem and corner detection are the same linear-algebra fact.**
3. **Linearisation is valid only for small motion**; warping and explicit correspondence search are how large motion is recovered.
4. **Cost volumes make matching explicit**; RAFT showed the pyramid was the expendable part, not the correlation.
5. **Occluded pixels must be excluded, not down-weighted.** They have no correct answer.
6. **Report outlier rates and breakdowns**, as well as mean EPE.

### Stereo and depth estimation {#cv-stereo-and-depth-estimation}

_Depth is unobservable from a single view. Everything here is a way of supplying the missing dimension — a second camera, many cameras, motion, or a learned prior._

#### Geometry and the disparity relation {#cv-stereo-and-depth-estimation--geometry}

After [rectification](#cv-calibration-and-sensor-alignment--stereo), corresponding points share a row and differ only horizontally:

$$ Z = \frac{f\,B}{d}, \qquad d = u_L - u_R $$

- $$B$$ — baseline — distance between optical centres
- $$f$$ — focal length in pixels
- $$d$$ — disparity

<a id="cv-stereo-and-depth-estimation--inverse-depth"></a>

**Why everything is parameterised in inverse depth**

$$ \frac{\partial Z}{\partial d} = -\frac{fB}{d^2} = -\frac{Z^2}{fB} \qquad\Longrightarrow\qquad \sigma_Z \approx \frac{Z^2}{fB}\,\sigma_d $$

_Depth uncertainty grows **quadratically** with range for fixed disparity noise. At 10× the distance, the same sub-pixel matching error produces 100× the depth error. Disparity (equivalently inverse depth) has roughly uniform uncertainty, so it is the right variable for estimation, for smoothness priors, and for probabilistic fusion. This is also why a stereo rig has a hard effective range set by $$fB/\sigma_d$$._

#### Matching costs {#cv-stereo-and-depth-estimation--costs}

| Cost                 | Form                                                    | Invariant to                           |
| -------------------- | ------------------------------------------------------- | -------------------------------------- |
| SAD / SSD            | $$\sum\lvert I_L - I_R\rvert$$, $$\sum(I_L-I_R)^2$$     | Nothing                                |
| NCC                  | normalised correlation over a window                    | Affine intensity $$aI+b$$              |
| **Census / Hamming** | bit pattern of local comparisons                        | Any _monotonic_ intensity change       |
| Mutual information   | $$\sum p(a,b)\log\frac{p(a,b)}{p(a)p(b)}$$              | Any statistical relation — cross-modal |
| Learned              | $$\mathbf{f}_L^\top\mathbf{f}_R$$ or an MLP on the pair | Whatever the training data contained   |

Census dominates embedded stereo: it is illumination-robust, needs no multiplication, and reduces matching to XOR + popcount — the same hardware argument that favours [binary descriptors](#cv-features-and-visual-primitives--binary).

#### Semi-Global Matching {#cv-stereo-and-depth-estimation--sgm}

The ideal is a 2D Markov random field over the disparity map, which is NP-hard. SGM approximates it by summing exact dynamic-programming solutions along several 1D paths:

**SGM path cost**

$$ L*{\mathbf{r}}(\mathbf{p}, d) = C(\mathbf{p},d) + \min\begin{cases} L*{\mathbf{r}}(\mathbf{p}-\mathbf{r},\, d)\\ L*{\mathbf{r}}(\mathbf{p}-\mathbf{r},\, d\pm1) + P_1\\ \min*{k} L*{\mathbf{r}}(\mathbf{p}-\mathbf{r},\, k) + P_2 \end{cases} \;-\; \min_k L*{\mathbf{r}}(\mathbf{p}-\mathbf{r},k) $$ $$ S(\mathbf{p},d) = \sum*{\mathbf{r}} L*{\mathbf{r}}(\mathbf{p},d) $$

- $$P_1$$ — small penalty for a $$\pm1$$ disparity step — permits slanted surfaces
- $$P_2$$ — large penalty for any bigger jump — permits genuine depth discontinuities
- $$\mathbf{r}$$ — path direction; 8 or 16 directions are typical

_The trailing subtraction keeps the accumulated cost bounded. The **two-penalty design is the key idea**: a single smoothness penalty must either forbid slant or permit noise, whereas $$P_1 \ll P_2$$ allows gradual surfaces while still preserving object boundaries. $$P_2$$ is usually adapted down where the image gradient is high._

The full classical pipeline: rectify → compute cost volume → aggregate (SGM) → winner-take-all → subpixel parabola fit → left–right consistency check → invalidate occlusions → median filter → hole-fill.

**Subpixel refinement by parabola fit**

$$ \hat{d} = d^{_} + \frac{C(d^{_}\!-\!1) - C(d^{_}\!+\!1)}{2\big(C(d^{_}\!-\!1) - 2C(d^{_}) + C(d^{_}\!+\!1)\big)} $$

#### Deep stereo {#cv-stereo-and-depth-estimation--deep-stereo}

The modern architecture mirrors the classical pipeline, with each stage learned: shared feature extraction → cost volume by concatenation or correlation across the disparity range → 3D convolutional aggregation → differentiable arg-min.

**Soft-argmin — differentiable disparity selection**

$$ \hat{d} = \sum*{d=0}^{D*{\max}} d\times\sigma\big(-C_d\big) $$

_A softmax over negated costs, then an expectation. Differentiable and sub-pixel — but, being an expectation, it produces a value \_between_ the modes when the cost volume is genuinely bimodal, i.e. at occlusion boundaries and on repeated texture. The same caveat as [soft-argmax](#cv-keypoints-and-pose--representation) for keypoints.\_

#### Supervised losses {#cv-stereo-and-depth-estimation--supervised}

**Scale-invariant log loss (Eigen)**

$$ \mathcal{L}\_{\text{SI}} = \frac{1}{n}\sum_i g_i^2 - \frac{\lambda}{n^2}\Big(\sum_i g_i\Big)^{2}, \qquad g_i = \log\hat{Z}\_i - \log Z_i $$

_With $$\lambda = 1$$ the loss is invariant to a global scale factor — exactly the ambiguity a monocular method cannot resolve. Penalising it would train the network to guess an unknowable constant. Setting $$\lambda \in (0,1)$$ partially restores scale sensitivity when some absolute cue exists._

**BerHu (reversed Huber)**

$$ \mathcal{B}(x) = \begin{cases}\lvert x\rvert & \lvert x\rvert \le c\\[2pt] \dfrac{x^2 + c^2}{2c} & \lvert x\rvert > c\end{cases} $$

_L1 for small errors (fine detail), L2 for large ones (strong gradient where the estimate is badly wrong) — the opposite emphasis to Huber, and empirically better for depth regression._

Also standard: gradient-matching and surface-normal losses to sharpen boundaries, ordinal regression (treat depth as ordered bins — easier than regression and naturally handles the long-tailed depth distribution), and uncertainty-weighted likelihoods.

#### Self-supervised depth {#cv-stereo-and-depth-estimation--selfsup}

The reprojection loss replaces ground-truth depth entirely. See [photometric consistency](#cv-photometric-consistency) for the full treatment; the essentials:

$$ pe(I_a, I_b) = \frac{\alpha}{2}\big(1-\mathrm{SSIM}(I_a,I_b)\big) + (1-\alpha)\lVert I_a - I_b\rVert_1, \qquad \alpha = 0.85 $$

**Edge-aware disparity smoothness**

$$ \mathcal{L}\_{s} = \big\lvert\partial_x d^{_}\big\rvert e^{-\lvert\partial_x I\rvert} + \big\lvert\partial_y d^{_}\big\rvert e^{-\lvert\partial_y I\rvert}, \qquad d^{\*} = d\,/\,\bar{d} $$

_The **mean-normalisation** $$d/\bar{d}$$ is not cosmetic: without it the smoothness term is trivially minimised by shrinking all disparities toward zero, so the network learns to predict everything as infinitely far away._

> **Monodepth2's three refinements — all to the _valid set_, not the network**
>
> - **Per-pixel minimum reprojection:** $$\min_{s} pe(I_t, I_{s\to t})$$ over source frames instead of the mean. A pixel occluded in one view is usually visible in another, and the minimum selects that view automatically — occlusion handling with no occlusion model.
> - **Auto-masking:** keep a pixel only if $$\min_s pe(I_t, I_{s\to t}) < \min_s pe(I_t, I_s)$$, i.e. the warped source explains the target better than the _unwarped_ one. This discards pixels where the camera-motion assumption fails — a static camera, or an object moving at the camera's velocity.
> - **Full-resolution multi-scale:** upsample each scale's disparity to full resolution before computing the loss, removing texture-copy artefacts and holes.

#### Multi-view stereo and monocular priors {#cv-stereo-and-depth-estimation--mvs}

> **MVS**
> Sweep a reference frustum over depth hypotheses, warp source views by the induced homography at each plane, and build a cost volume: $$ \mathbf{H}\_i(d) = \mathbf{K}\_i\mathbf{R}\_i\Big(\mathbf{I} - \frac{(\mathbf{t}\_i - \mathbf{t}\_r)\mathbf{n}^{\top}}{d}\Big)\mathbf{R}\_r^{\top}\mathbf{K}\_r^{-1} $$ Regularise in 3D, regress depth, fuse across views with geometric consistency checks. Cascade/coarse-to-fine hypothesis refinement makes high resolution affordable.

> **Monocular depth**
> There is no geometric constraint at all — the output is entirely a learned prior over scene structure. Hence it is **relative**, not metric, unless calibrated by a known scale. [Depth Anything V2](#cv-video-depth-and-concepts--depthanything2) showed the decisive factor is _data_: a synthetic-label teacher pseudo-labelling 62M real images beat far more expensive diffusion-based approaches by >10×.

[Depth Anything 3](#cv-any-view-geometry-concepts-and-embodiment--da3) unified the whole family behind a single **depth–ray** target over any number of views, removing the distinction between monocular, stereo and MVS at the interface level.

#### Metrics {#cv-stereo-and-depth-estimation--metrics}

$$ \mathrm{AbsRel} = \frac{1}{n}\sum*i \frac{\lvert \hat{Z}\_i - Z_i\rvert}{Z_i}, \qquad \mathrm{RMSE} = \sqrt{\frac{1}{n}\sum_i (\hat{Z}\_i - Z_i)^2}, \qquad \delta*\tau = \frac{1}{n}\Big\lvert\Big\{i : \max\Big(\tfrac{\hat{Z}\_i}{Z_i}, \tfrac{Z_i}{\hat{Z}\_i}\Big) < \tau\Big\}\Big\rvert $$

_$$\delta_1 = \delta_{1.25}$$ is the standard threshold accuracy. For stereo, **D1-all** reports the percentage of pixels with disparity error $$>3$$ px and $$>5\%$$. **Monocular results are usually reported after median scaling** — the prediction is multiplied by $$\operatorname{med}(Z)/\operatorname{med}(\hat{Z})$$ — which hides the scale ambiguity. Always check whether a number is scale-aligned before comparing it to a stereo method.\_

#### Failure modes and takeaways {#cv-stereo-and-depth-estimation--failures}

| Failure                                | Cause                                                    | Defense                                                     |
| -------------------------------------- | -------------------------------------------------------- | ----------------------------------------------------------- |
| Textureless walls, sky                 | Flat matching cost                                       | Smoothness, plane priors, semantics, SGM's $$P_1/P_2$$      |
| Repetitive structure (fences, windows) | Periodic cost volume — multiple equal minima             | Larger context, left–right check, global aggregation        |
| Occlusion boundaries                   | No correspondence exists in the other view               | Left–right consistency, invalidate and fill                 |
| Transparent / specular                 | Photometric consistency violated                         | Robust costs, polarisation; no full fix                     |
| Far range unreliable                   | $$\sigma_Z \propto Z^2$$                                 | Longer baseline, sub-pixel refinement, accept a range limit |
| Depth collapses to a constant          | Un-normalised smoothness term                            | Mean-normalise disparity before smoothing                   |
| Dynamic objects "infinitely far"       | Object moving with the camera has zero apparent parallax | Auto-masking; motion segmentation                           |

1. **Estimate in disparity / inverse depth.** Uncertainty is uniform there and quadratic in depth.
2. **SGM's two penalties** are what let one prior express both slant and discontinuity.
3. **Soft-argmin is an expectation** — it fails exactly where the cost volume is bimodal.
4. **Scale-invariant losses exist because monocular scale is unknowable**; penalising it trains a guess.
5. **The self-supervised gains came from the valid set**, not from the architecture.
6. **Check for median scaling** before comparing monocular and stereo numbers.

### Camera pose, SfM, VO and SLAM {#cv-camera-pose-sfm-vo-and-slam}

_Estimating where the camera was and what the scene looks like, simultaneously — the most mature optimisation pipeline in vision, and the one a single 2025 transformer proved could be replaced by a forward pass._

#### Two-view geometry {#cv-camera-pose-sfm-vo-and-slam--epipolar}

**The epipolar constraint**

$$ \mathbf{u}'^{\top}\mathbf{F}\,\mathbf{u} = 0, \qquad \hat{\mathbf{x}}'^{\top}\mathbf{E}\,\hat{\mathbf{x}} = 0, \qquad \mathbf{E} = [\mathbf{t}]\_\times\mathbf{R} = \mathbf{K}'^{\top}\mathbf{F}\mathbf{K} $$

_$$\mathbf{F}$$ has 7 DoF (9 entries, minus scale, minus $$\det\mathbf{F}=0$$); $$\mathbf{E}$$ has 5 (3 rotation + 2 translation direction — **translation magnitude is unrecoverable**, the origin of monocular scale ambiguity). The constraint says a point in one image lies on a \_line_ in the other, reducing the correspondence search from 2D to 1D.\_

> **8-point algorithm**
> Linear in the entries of $$\mathbf{F}$$; stack 8 correspondences and take the smallest right singular vector, then project to rank 2 by zeroing the smallest singular value. **Requires Hartley normalisation** — unnormalised it is numerically useless.

> **5-point algorithm**
> Uses the calibrated constraints ($$\mathbf{E}$$ has two equal singular values, third zero) to work from the minimal 5 correspondences, yielding up to 10 solutions via a 10th-degree polynomial. The smaller minimal sample makes [RANSAC](#cv-vision-objectives-and-optimization--ransac) dramatically cheaper — and it handles planar scenes, where the 8-point algorithm degenerates.

**Pose from E, and the cheirality test**

$$ \mathbf{E} = \mathbf{U}\operatorname{diag}(1,1,0)\mathbf{V}^{\top} \;\Longrightarrow\; \mathbf{R} \in \{\mathbf{U}\mathbf{W}\mathbf{V}^\top,\ \mathbf{U}\mathbf{W}^\top\mathbf{V}^\top\},\quad \mathbf{t} = \pm\mathbf{u}\_3 $$

_Four combinations; exactly one places triangulated points \_in front of both cameras_. That is the cheirality check, and it is what resolves the sign ambiguity.\_

#### Triangulation {#cv-camera-pose-sfm-vo-and-slam--triangulation}

$$ \begin{bmatrix} u\,\mathbf{p}\_3^{\top} - \mathbf{p}\_1^{\top}\\ v\,\mathbf{p}\_3^{\top} - \mathbf{p}\_2^{\top}\\ u'\,\mathbf{p}'^{\top}\_3 - \mathbf{p}'^{\top}\_1\\ v'\,\mathbf{p}'^{\top}\_3 - \mathbf{p}'^{\top}\_2 \end{bmatrix}\tilde{\mathbf{X}} = \mathbf{0} $$

_The DLT form: rays never meet exactly, so solve in least squares via SVD. This minimises an \_algebraic_ error; the statistically correct answer minimises reprojection error in both images (the optimal two-view method solves a degree-6 polynomial). **Always refine.** Triangulation is ill-conditioned at small parallax — two nearly parallel rays intersect at a poorly determined depth, which is why keyframe selection enforces a minimum baseline.\_

#### Bundle adjustment {#cv-camera-pose-sfm-vo-and-slam--ba}

**The joint objective**

$$ \min*{\{\mathbf{T}\_i\},\{\mathbf{X}\_j\}} \sum*{(i,j)\in\mathcal{O}} \rho\Big( \big\lVert \mathbf{u}_{ij} - \pi(\mathbf{K}\_i,\mathbf{T}\_i,\mathbf{X}\_j)\big\rVert^{2}_{\Sigma\_{ij}} \Big) $$

_$$\mathcal{O}$$ is the set of observations (camera $$i$$ sees point $$j$$), $$\Sigma_{ij}$$ the measurement covariance, $$\rho$$ a robust kernel (Huber). This is the maximum-likelihood estimate under Gaussian pixel noise, and it is the gold standard against which every learned alternative is measured.\_

**Exploiting structure — the Schur complement**

$$ \begin{bmatrix}\mathbf{B} & \mathbf{E}\\ \mathbf{E}^{\top} & \mathbf{C}\end{bmatrix}\begin{bmatrix}\delta*{\mathbf{c}}\\ \delta*{\mathbf{p}}\end{bmatrix} = \begin{bmatrix}\mathbf{v}\\ \mathbf{w}\end{bmatrix} \;\Longrightarrow\; \underbrace{\big(\mathbf{B} - \mathbf{E}\mathbf{C}^{-1}\mathbf{E}^{\top}\big)}_{\text{reduced camera system}}\delta_{\mathbf{c}} = \mathbf{v} - \mathbf{E}\mathbf{C}^{-1}\mathbf{w} $$

_$$\mathbf{C}$$ is block-diagonal with 3×3 blocks (one per point), so $$\mathbf{C}^{-1}$$ is trivially parallel. The reduced system has dimension $$6\times N_{\text{cam}}$$ instead of $$6N_{\text{cam}} + 3N_{\text{pts}}$$ — typically thousands instead of millions. **This one algebraic step is what makes BA tractable at all.**\_

> **Gauge freedom**
> The objective is invariant to a global similarity transform: rotate, translate and scale the whole reconstruction and every reprojection is unchanged. The Hessian is therefore **rank-deficient by 7** (6 for a calibrated stereo/metric setup). Fix the gauge by holding one camera fixed, or add a weak prior, or use a pseudo-inverse — otherwise the solver drifts along the null space and the covariance is meaningless.

#### The two pipelines {#cv-camera-pose-sfm-vo-and-slam--pipelines}

> **Feature-based (indirect)**
> Detect and match → essential matrix with RANSAC → recover pose, check cheirality → triangulate → register new views with PnP-RANSAC → add landmarks → local and global BA.<br><br> **Minimises reprojection error.** Robust to illumination change and large baselines; discards most of the image; needs texture.

<a id="cv-camera-pose-sfm-vo-and-slam--direct"></a>

> **Direct**
> Select high-gradient pixels → warp by candidate depth and pose → minimise [photometric error](#cv-photometric-consistency) → marginalise old states → keyframes → local photometric BA.<br><br> **Minimises photometric error.** Uses all image gradient (works on faint texture), sub-pixel accurate; needs photometric calibration and a good initialisation.

The distinction is exactly the one from [registration](#cv-correspondence-and-registration--two-routes), one level up. Semi-direct methods (SVO) use direct alignment for tracking and feature-based BA for mapping, taking both advantages.

#### What SLAM adds over VO {#cv-camera-pose-sfm-vo-and-slam--slam}

Visual odometry is _locally_ consistent and drifts without bound. SLAM adds the machinery to recover _global_ consistency:

**Map management**

Keyframe insertion and culling; landmark creation, merging and removal; a covisibility graph linking keyframes that see common points.

**Place recognition**

Bag-of-words over visual vocabularies (DBoW) or learned global descriptors (NetVLAD). Must be fast and recall-oriented; candidates are verified geometrically afterwards.

**Loop verification**

A geometric check (enough RANSAC inliers for a consistent rigid transform) plus temporal consistency across several frames. **A false positive here is catastrophic** — it welds two unrelated places together and corrupts the whole map.

**Pose-graph optimisation**

Distribute the loop-closure error over the trajectory.

**Pose-graph optimisation**

$$ \min*{\{\mathbf{T}\_i\}} \sum*{(i,j)\in\mathcal{E}} \Big\lVert \log\big(\mathbf{Z}_{ij}^{-1}\,\mathbf{T}\_i^{-1}\mathbf{T}\_j\big)^{\vee}\Big\rVert^{2}_{\Omega\_{ij}} $$

- $$\mathbf{Z}_{ij}$$ — measured relative pose between keyframes $$i$$ and $$j$$
- $$\log(\cdot)^{\vee}$$ — $$SE(3)$$ logarithm to a 6-vector — the error is computed on the manifold
- $$\Omega_{ij}$$ — information matrix of the constraint

_Points have been marginalised out, so this is far cheaper than full BA. Run pose-graph optimisation immediately on loop closure to fix gross drift, then a full BA in a background thread to refine._

#### Visual–inertial fusion {#cv-camera-pose-sfm-vo-and-slam--inertial}

An IMU supplies metric scale, gravity direction, and high-rate motion — precisely the quantities monocular vision cannot observe. The difficulty is rate mismatch (IMU at ~200 Hz, camera at ~30 Hz).

**IMU preintegration**

$$ \Delta\mathbf{R}_{ij} = \prod_{k=i}^{j-1}\exp\big((\tilde{\boldsymbol{\omega}}_k - \mathbf{b}^g)\Delta t\big), \quad \Delta\mathbf{v}_{ij} = \sum*k \Delta\mathbf{R}*{ik}(\tilde{\mathbf{a}}_k - \mathbf{b}^a)\Delta t, \quad \Delta\mathbf{p}_{ij} = \sum*k \Big[\Delta\mathbf{v}*{ik}\Delta t + \tfrac12\Delta\mathbf{R}\_{ik}(\tilde{\mathbf{a}}\_k - \mathbf{b}^a)\Delta t^2\Big] $$

_The key idea: integrate IMU measurements into a \_relative_ motion constraint expressed in the body frame, so the result does not depend on the (still-unknown) absolute pose and need not be recomputed every time the optimiser updates the state. Bias updates are handled by a first-order correction rather than re-integration.\_

**Observability:** a visual–inertial system needs sufficient _rotational and translational excitation_ to make scale and biases observable. Constant-velocity motion leaves accelerometer bias and scale entangled — which is why VIO initialisation requires the device to be moved.

#### The 2025 alternative: feed-forward geometry {#cv-camera-pose-sfm-vo-and-slam--feedforward}

> **VGGT and Depth Anything 3** > [VGGT](#cv-any-view-geometry-concepts-and-embodiment--vggt) replaces the entire pipeline — features, matching, RANSAC, triangulation, BA — with a _single forward pass_ of a transformer that alternates frame-wise and global attention and jointly predicts cameras, depth, point maps and tracks. [Depth Anything 3](#cv-any-view-geometry-concepts-and-embodiment--da3) does the same with a plain backbone and a unified depth–ray target. Both beat the specialised optimisation pipelines on their benchmarks, and both are also useful as _initialisers_ for a subsequent bundle adjustment — which is how they are most often deployed in practice.

#### Tricks and failure modes {#cv-camera-pose-sfm-vo-and-slam--tricks}

> **Tricks**
>
> - 5-point RANSAC; ratio test plus geometric verification; cheirality
> - Robust Huber/Tukey kernels; information-matrix weighting
> - Keyframe selection on parallax and tracked-feature ratio
> - Local sliding-window BA; **marginalisation** of old states into a prior
> - Schur complement; sparse Cholesky ordering
> - Constant-velocity motion prior for initialisation
> - Rolling-shutter and photometric (gain/exposure) models

> **Failure modes**
>
> - **Pure rotation** — no parallax, so triangulation and scale fail entirely
> - **Planar / low-parallax scenes** — essential matrix degenerate; use the homography branch
> - **Dynamic objects** — corrupt pose unless masked
> - **Scale drift** in monocular systems
> - **False loop closure** — irrecoverable map corruption
> - **Repetitive environments** (corridors, car parks) — place recognition aliasing
> - **Motion blur and rolling shutter** under fast motion

#### Metrics and takeaways {#cv-camera-pose-sfm-vo-and-slam--metrics}

**ATE** (absolute trajectory error) aligns the estimated and ground-truth trajectories with a similarity transform — Sim(3) for monocular, SE(3) when scale is observed — and reports RMSE of positions. **RPE** (relative pose error) measures drift over fixed sub-sequences and is the better diagnostic for odometry, since ATE can be dominated by a single early error.

1. **The epipolar constraint reduces search from 2D to 1D.** Everything two-view follows from it.
2. **Translation magnitude is unrecoverable from two calibrated views** — the root of monocular scale ambiguity.
3. **Bundle adjustment is the MLE**, and the Schur complement is what makes it computable.
4. **Gauge freedom means the Hessian is singular by construction.** Fix it deliberately.
5. **VO drifts; SLAM closes loops.** That single addition is the entire difference.
6. **A false loop closure is worse than no loop closure** — verify geometrically and temporally.

### Visual tracking {#cv-visual-tracking}

_Maintaining identity over time. The detection component is largely solved. \_Association_ and _lifecycle management_ account for most of the remaining error.\_

#### Four distinct problems {#cv-visual-tracking--taxonomy}

| Task                             | Initialised by                                  | Core difficulty                         |
| -------------------------------- | ----------------------------------------------- | --------------------------------------- |
| **Point / feature tracking**     | A detector (corners)                            | Drift, occlusion; solved by KLT         |
| **Single-object tracking (SOT)** | A box in frame 1 — _any_ object, class-agnostic | No category prior; appearance change    |
| **Multi-object tracking (MOT)**  | A detector, every frame                         | Data association; identity preservation |
| **Multi-camera tracking**        | Detectors across views                          | Cross-view Re-ID, clock sync, geometry  |

#### The Kalman filter {#cv-visual-tracking--kalman}

A constant-velocity motion model with state $$\mathbf{x} = [u, v, s, r, \dot{u}, \dot{v}, \dot{s}]^{\top}$$ (centre, scale, aspect, velocities):

**Predict**

$$ \hat{\mathbf{x}}_{k|k-1} = \mathbf{F}\hat{\mathbf{x}}_{k-1|k-1}, \qquad \mathbf{P}_{k|k-1} = \mathbf{F}\mathbf{P}_{k-1|k-1}\mathbf{F}^{\top} + \mathbf{Q} $$

**Update**

$$ \mathbf{K}_k = \mathbf{P}_{k|k-1}\mathbf{H}^{\top}\big(\mathbf{H}\mathbf{P}_{k|k-1}\mathbf{H}^{\top} + \mathbf{R}\big)^{-1} $$ $$ \hat{\mathbf{x}}_{k|k} = \hat{\mathbf{x}}_{k|k-1} + \mathbf{K}\_k\big(\mathbf{z}\_k - \mathbf{H}\hat{\mathbf{x}}_{k|k-1}\big), \qquad \mathbf{P}_{k|k} = (\mathbf{I} - \mathbf{K}\_k\mathbf{H})\mathbf{P}_{k|k-1} $$

_The Kalman gain $$\mathbf{K}_k$$ interpolates between prediction and measurement according to their relative uncertainties: confident prediction ($$\mathbf{P}$$ small) ⇒ trust the model; noisy measurement ($$\mathbf{R}$$ large) ⇒ trust the model. During an occlusion no measurement arrives, $$\mathbf{P}$$ grows with each predict step, and the gate widens, which is the required behaviour and is where a filter differs from linear extrapolation._

A **particle filter** generalises this to non-Gaussian, multi-modal posteriors by representing the distribution with weighted samples — necessary when the state is genuinely ambiguous (e.g. in clutter), at much higher cost.

#### Data association {#cv-visual-tracking--association}

Given $$N$$ tracks and $$M$$ detections, build a cost matrix $$\mathbf{C}\in\mathbb{R}^{N\times M}$$ and solve a linear assignment problem:

**Assignment**

$$ \min*{\mathbf{A}} \sum*{i=1}^{N}\sum*{j=1}^{M} C*{ij}A*{ij} \quad\text{s.t.}\quad \sum_j A*{ij}\le 1,\ \ \sum*i A*{ij}\le 1,\ \ A\_{ij}\in\{0,1\} $$

_Solved exactly in $$O(n^3)$$ by the **Hungarian algorithm**. The constraint that each track takes at most one detection and vice versa is a \_bipartite matching_ — structurally the same as [DETR's](#cv-object-detection--set) loss, applied across time instead of across queries.\_

##### Cost terms {#cv-visual-tracking--costs}

**Mahalanobis (motion) distance**

$$ d^{(1)}(i,j) = (\mathbf{z}\_j - \mathbf{H}\hat{\mathbf{x}}\_i)^{\top}\,\mathbf{S}\_i^{-1}\,(\mathbf{z}\_j - \mathbf{H}\hat{\mathbf{x}}\_i), \qquad \mathbf{S}\_i = \mathbf{H}\mathbf{P}\_i\mathbf{H}^{\top} + \mathbf{R} $$

_Distance normalised by the predicted covariance, so it is measured in standard deviations rather than pixels. Under a Gaussian assumption it is $$\chi^2$$-distributed with 4 DoF, giving a principled **gate**: reject pairs with $$d^{(1)} > \chi^2_{0.95} = 9.4877$$.\_

**Appearance (cosine) distance and the combined cost**

$$ d^{(2)}(i,j) = \min*k\Big\{1 - \mathbf{r}\_j^{\top}\mathbf{r}^{(i)}\_k \ \Big|\ \mathbf{r}^{(i)}\_k \in \mathcal{R}\_i\Big\}, \qquad c*{ij} = \lambda\,d^{(1)} + (1-\lambda)\,d^{(2)} $$

_$$\mathcal{R}_i$$ is a \_gallery_ of the last ~100 appearance descriptors for track $$i$$; taking the minimum over the gallery makes re-identification robust to temporary appearance change. Motion and appearance are complementary: motion is reliable short-term, appearance survives long occlusions.\_

#### Three trackers, three ideas {#cv-visual-tracking--trackers}

| Method        | Signal              | Key idea                                                                                                                                               |
| ------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **SORT**      | Motion (IoU)        | Kalman prediction + IoU cost + Hungarian. Minimal and fast, and a strong baseline, because most of MOT accuracy comes from the detector.               |
| **DeepSORT**  | Motion + appearance | Adds a Re-ID embedding and a **matching cascade**: match recently-seen tracks first, so a long-lost track cannot steal a detection from an active one. |
| **ByteTrack** | Motion, two-stage   | Associate high-confidence detections first; then use the _remaining_ low-confidence detections to recover unmatched tracks.                            |

> **ByteTrack's observation is worth isolating**
> A low-confidence detection is frequently a **real object that is occluded**, not a false positive. Earlier trackers removed these at the first threshold, which produced identity switches at the moment of occlusion. Keeping them, and using them only in a second association pass where a track is already hypothesised, recovers most of that loss at negligible added cost. The gain here comes from removing a threshold, not from adding a model.

#### Track lifecycle {#cv-visual-tracking--lifecycle}

The unglamorous part that determines real-world behaviour:

**Birth**

An unmatched detection creates a _tentative_ track. It must be confirmed by $$n_{\text{init}}$$ consecutive matches (typically 3) before being output — this suppresses flickering false positives.

**Confirmation**

Only confirmed tracks are reported. A detector's false positives rarely persist for three frames in a consistent location; genuine objects do.

**Occlusion**

Unmatched but confirmed tracks continue to be predicted, with growing covariance. They stay alive for up to $$a_{\max}$$ frames (the "lost buffer").

**Termination**

Deleted after $$a_{\max}$$ unmatched frames. Too short causes ID switches through occlusion; too long causes ghost tracks and identity theft.

**Interpolation**

Offline only: fill short gaps after the fact, which measurably improves MOTA and is legitimate for post-hoc analysis but not for online use.

#### Metrics — and why MOTA is misleading {#cv-visual-tracking--metrics}

**MOTA**

$$ \mathrm{MOTA} = 1 - \frac{\sum_t \big(FN_t + FP_t + IDSW_t\big)}{\sum_t GT_t} $$

_**Dominated by detection.** FN and FP are typically orders of magnitude more numerous than identity switches, so MOTA measures association weakly: an accurate tracker on a weak detector scores below a weak tracker on an accurate detector. It can also be negative._

**IDF1 — identity-centric**

$$ \mathrm{IDF1} = \frac{2\,IDTP}{2\,IDTP + IDFP + IDFN} $$

_Computed after a \_global_ bipartite matching between ground-truth and predicted trajectories, so it measures how consistently identity is preserved over the whole sequence rather than per frame.\_

**HOTA — the decomposition**

$$ \mathrm{HOTA} = \sqrt{\mathrm{DetA}\cdot\mathrm{AssA}} $$

_Explicitly factors detection accuracy from association accuracy and takes their geometric mean, so the two contribute equally and can be reported separately. **Report HOTA with its DetA/AssA breakdown**: of the three metrics it is the one that separates detector error from tracker error._

#### Tricks and failure modes {#cv-visual-tracking--tricks}

> **Tricks**
>
> - **Gate before assigning** — set impossible pairs to infinity so the Hungarian solver cannot choose them
> - Matching cascade by track age
> - Appearance galleries with EMA feature updates
> - **Camera-motion compensation** — estimate a global homography between frames and warp track predictions; essential on moving platforms
> - Two-threshold (ByteTrack) association
> - Class-consistent association; separate Kalman parameters per class

> **Failure modes**
>
> - **ID switches at crossings** — two similar objects swap under mutual occlusion
> - **Fragmentation** — long occlusion exceeds $$a_{\max}$$
> - **Identity theft** — a lost track absorbs a new object's detection
> - **Ghost tracks** — coasting predictions persist after the object left
> - **Camera motion** breaks the constant-velocity assumption
> - **Crowds** — NMS in the detector deletes the occluded person the tracker needed

#### Takeaways {#cv-visual-tracking--takeaways}

1. **Association is a bipartite matching problem** — the same structure as DETR's loss, applied across time.
2. **The Kalman covariance is doing real work**: it widens the gate exactly when the object is occluded.
3. **Mahalanobis distance gives a principled gate**; pixel thresholds do not.
4. **Motion and appearance are complementary**, not redundant — short-term versus long-term.
5. **ByteTrack removes a threshold.** Low-confidence detections are frequently occluded objects.
6. **Report HOTA with DetA/AssA.** MOTA measures the detector more than the tracker.

### Video understanding {#cv-video-understanding}

\_Adding a temporal axis multiplies compute and adds almost no labels. Every architecture here is a different answer to: \_which temporal structure is worth paying for?\_\_

#### The task family {#cv-video-understanding--tasks}

| Task                          | Output                                                       | Metric                           |
| ----------------------------- | ------------------------------------------------------------ | -------------------------------- |
| Video / action classification | One label per trimmed clip                                   | Top-1, mAP                       |
| Temporal action localisation  | $$(t_{\text{start}}, t_{\text{end}}, c)$$ in untrimmed video | mAP at temporal IoU              |
| Spatio-temporal detection     | Per-frame boxes with an action label                         | frame-mAP, video-mAP             |
| Temporal segmentation         | Per-frame label                                              | Frame accuracy, edit score, F1@k |
| Anomaly detection             | Frame-level anomaly score                                    | AUC (frame-level)                |
| Anticipation                  | Action before it occurs                                      | Top-5 at anticipation time       |

#### Classical: dense trajectories {#cv-video-understanding--classical}

Before deep learning, the strongest approach was **improved dense trajectories**: sample points densely, track them with [optical flow](#cv-optical-flow-and-scene-flow--lk) for $$L\approx15$$ frames, and describe the tube around each trajectory with HOG (appearance), HOF (flow), and **MBH** — motion boundary histograms, the gradient of the flow field.

$$ \mathrm{MBH} = \big(\partial_x u,\ \partial_y u,\ \partial_x v,\ \partial_y v\big) $$

_Differentiating the flow field cancels any \_constant_ flow component — which is exactly camera motion. MBH is therefore camera-motion invariant by construction, and that is why it was the single strongest descriptor of the era. The same idea reappears in modern systems as explicit camera-motion compensation.\_

#### Deep architectures {#cv-video-understanding--architectures}

**Two-stream (2014)**

One CNN on RGB frames (appearance), one on stacked optical flow (motion), fused late. It works because _flow is a hand-computed motion feature the network would otherwise have to learn_ from limited data. Its weakness is cost: flow must be precomputed, and it accounts for most of the compute budget.

**3D CNNs and inflation (I3D, 2017)**

Replace $$k\times k$$ kernels with $$t\times k\times k$$. The **inflation** trick makes them trainable: take a 2D ImageNet-pretrained kernel $$\mathbf{W}\in\mathbb{R}^{k\times k}$$ and initialise the 3D kernel as $$\mathbf{W}_{3D}[i] = \mathbf{W}/t$$ for all $$i$$, so a constant video reproduces the 2D network's response exactly. Without this, 3D CNNs were hopeless — there is nowhere near enough labelled video to train them from scratch.

**Factorised 3D (R(2+1)D, P3D)**

Decompose $$t\times k\times k$$ into a spatial $$1\times k\times k$$ followed by a temporal $$t\times1\times1$$. Fewer parameters, an extra non-linearity between the two, and easier optimisation — the same factorisation argument as [depthwise separable convolutions](#cv-depth-detection-and-the-first-believable-images--mobilenet).

<a id="cv-video-understanding--slowfast"></a>

**SlowFast (2019)**

Semantics and motion change at different rates, so sample them at different rates. A **Slow** pathway at low frame rate with high channel capacity captures _what_; a **Fast** pathway at $$\alpha\!=\!8\times$$ the frame rate with $$\beta\!=\!1/8$$ the channels captures _how it moves_; lateral connections fuse Fast into Slow. The thin fast pathway keeps total cost near a single 3D CNN — the same heavy/cheap asymmetry as [mechanism 5](#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--m5).

**Video transformers (2021)**

Joint space-time attention costs $$O\big((THW)^2\big)$$ — prohibitive. **TimeSformer's divided space-time attention** factorises it: attend over space within a frame, then over time at the same spatial location, reducing cost to $$O\big(T\cdot(HW)^2 + HW\cdot T^2\big)$$. ViViT and MViT explore related factorisations and pooling.

#### Self-supervised video: VideoMAE {#cv-video-understanding--ssl}

**Tube masking**

$$ \mathbf{M}(x,y,t) = \mathbf{M}(x,y) \quad \forall t \qquad\text{with mask ratio } 90\text{–}95\% $$

_Masking the \_same_ spatial locations across all frames is essential. Random per-frame masking leaks the answer: a patch masked at $$t$$ is usually visible at $$t{\pm}1$$, and because adjacent frames are nearly identical, the model can reconstruct by copying rather than by understanding. Tube masking removes that shortcut, which is why the viable mask ratio is far higher than [image MAE's](#cv-the-transformer-takeover--mae) 75%.\_

The general lesson: **temporal redundancy is both the opportunity and the trap** in video self-supervision. Any pretext task must be designed so that the trivially-copyable solution is unavailable.

#### Temporal localisation {#cv-video-understanding--localisation}

Structurally the 1D analogue of [object detection](#cv-object-detection), and it inherits the same machinery:

$$ \mathrm{tIoU}(A, B) = \frac{\lvert A\cap B\rvert}{\lvert A\cup B\rvert} \quad\text{over time intervals} $$

- **Anchor-based:** multi-scale temporal anchors, classification plus boundary regression, then **temporal NMS**.
- **Boundary-based (BMN, BSN):** predict start and end probabilities per frame, then score all start–end pairs with a boundary-matching confidence map.
- **Query-based:** DETR-style set prediction over intervals, with Hungarian matching — removing temporal NMS exactly as DETR removed spatial NMS.

The metric is mAP averaged over tIoU thresholds (typically 0.5:0.05:0.95 on ActivityNet, 0.3:0.1:0.7 on THUMOS). **Boundaries are intrinsically ambiguous** — human annotators disagree substantially about when an action starts — which caps achievable tIoU and should temper how seriously high-threshold numbers are read.

#### Anomaly detection {#cv-video-understanding--anomaly}

Anomalies are rare, diverse and poorly defined, so supervised classification is unworkable. Two standard formulations:

**Multiple-instance ranking (weakly supervised)**

$$ \mathcal{L} = \max\Big(0,\ 1 - \max*{i\in\mathcal{B}\_a} f(v_i) + \max*{i\in\mathcal{B}_n} f(v_i)\Big) + \lambda_1\sum_i\big(f(v_i)-f(v_{i+1})\big)^2 + \lambda_2\sum_i f(v_i) $$

_Video-level labels only. The \_highest-scoring_ segment of an anomalous video should outrank the highest-scoring segment of a normal one. The two regularisers impose temporal smoothness and sparsity — anomalies are brief.\_

The alternative is **reconstruction- or prediction-based**: train an autoencoder or future-frame predictor on normal video only, and score by reconstruction error. The known failure is that a sufficiently powerful autoencoder generalises to anomalies too and reconstructs them well — hence memory-augmented and constrained variants.

#### Sampling and aggregation {#cv-video-understanding--sampling}

| Strategy            | Method                                                     | Use                                                                                      |
| ------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **Dense clip**      | Contiguous 16–64 frames                                    | Short atomic actions                                                                     |
| **Sparse (TSN)**    | Split into $$K$$ segments, sample one frame from each      | Long actions; covers the whole video cheaply                                             |
| **Multi-view test** | $$N$$ temporal clips × $$M$$ spatial crops, average logits | Standard at evaluation — **read the protocol**, since 10×3 views costs 30× a single clip |

> **Video benchmark numbers are rarely comparable as published**
> Accuracy depends on frame rate, clip length, the number of test views, input resolution and pretraining corpus — and these vary freely between papers. A "+1.5%" gain frequently reflects 30 test views against 10. Always check views × crops and the pretraining set before comparing.

#### Failure modes and takeaways {#cv-video-understanding--failures}

| Failure                                  | Cause                                                | Defense                                                                        |
| ---------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------ |
| **Scene bias** — a single frame suffices | Backgrounds correlate with actions (swimming ⇒ pool) | Evaluate on temporally-sensitive sets (Something-Something); background mixing |
| Temporal direction ignored               | Many models score a reversed clip identically        | Test with reversed clips; use ordering pretext tasks                           |
| Long-range dependency lost               | Clips of 2–3 s cannot span a minute-long activity    | Sparse sampling, memory modules, hierarchical models                           |
| Boundary ambiguity                       | Annotators genuinely disagree                        | Soft boundary targets; report multiple tIoU thresholds                         |
| Compute explosion                        | The temporal axis multiplies everything              | Factorised attention, SlowFast asymmetry, sparse sampling                      |
| Label scarcity                           | Annotating video is far costlier than images         | Image-pretrained inflation; VideoMAE; video–text pretraining                   |

1. **Inflation is what made 3D CNNs trainable** — there was never enough labelled video to do it from scratch.
2. **Factorisation is the recurring answer to temporal cost**: (2+1)D convolution, divided space-time attention, SlowFast's two rates.
3. **MBH was camera-motion invariant by construction**, which is why differentiating the flow field scores above describing it.
4. **Temporal redundancy is a trap for self-supervision**; tube masking exists to close the copying shortcut.
5. **Check whether the task requires the temporal dimension.** Many "video" benchmarks are solvable from one frame.
6. **Test-time view counts make published numbers incomparable.** Check the protocol first.

## 3D and generative

### Point clouds and 3D perception {#cv-point-clouds-and-3d-perception}

_Unordered, irregular, non-uniformly dense data. The representation choice — points, voxels, pillars, range images, graphs — determines which operator is even available, and it is made before anything else._

#### Why point clouds need their own machinery {#cv-point-clouds-and-3d-perception--properties}

> **Three properties that break image operators**
>
> - **Unordered.** A set of $$N$$ points has $$N!$$ equivalent orderings. Any function of the cloud must be _permutation invariant_, which a convolution over an array is not.
> - **Irregular.** There is no grid, so there is no neighbour-by-index. Neighbourhoods must be queried geometrically (kd-tree, ball query, hashing).
> - **Non-uniform density.** LiDAR returns are dense near the sensor and sparse far away, so a fixed-radius neighbourhood contains wildly varying point counts.

#### Five representations {#cv-point-clouds-and-3d-perception--representations}

| Representation    | Operator                    | Strength                                          | Weakness                                             |
| ----------------- | --------------------------- | ------------------------------------------------- | ---------------------------------------------------- |
| **Raw points**    | Shared MLP + symmetric pool | No quantisation loss; memory-proportional to data | Neighbour queries are the bottleneck                 |
| **Voxels**        | Sparse 3D convolution       | Regular; reuses CNN machinery                     | Quantisation; cubic memory if dense                  |
| **Pillars / BEV** | 2D convolution              | Very fast; the vertical axis is collapsed once    | Loses fine vertical structure                        |
| **Range image**   | 2D convolution              | The sensor's native format; dense and compact     | Distorts metric neighbourhoods; occlusion boundaries |
| **Graph**         | Message passing (EdgeConv)  | Explicit local geometry; dynamic neighbourhoods   | Graph construction cost                              |

#### PointNet: permutation invariance done minimally {#cv-point-clouds-and-3d-perception--pointnet}

**The universal symmetric form**

$$ f(\{\mathbf{x}_1,\dots,\mathbf{x}\_N\}) \;\approx\; \gamma\!\left(\operatorname\*{MAX}_{i=1..N}\ h(\mathbf{x}\_i)\right) $$

_Apply a shared MLP $$h$$ to every point independently, aggregate with a **symmetric** function (element-wise max), then apply $$\gamma$$. Max is permutation invariant by construction, and the paper proves this form can approximate any continuous set function to arbitrary accuracy given enough width._

> **What max-pooling computes, and its limitation**
> Each output channel records the _single_ point that maximised it, so the global feature is determined by a small set of "critical points" — effectively a learned skeleton of the shape. This gives strong robustness to missing or corrupted points, since deleting a non-critical point changes nothing.
>
> It also means PointNet has **no local neighbourhood structure at all**: it sees each point in isolation and then globally. **PointNet++** fixes this by applying PointNet hierarchically — sample centroids with farthest-point sampling, group by ball query, apply PointNet to each group, repeat — recovering exactly the multi-scale hierarchy that [every family eventually rediscovers](#cv-multiscale-vision-and-filtering--lineage).

**Farthest-point sampling**

$$ \mathbf{c}_{k+1} = \arg\max_{\mathbf{x}\in\mathcal{P}}\ \min\_{j\le k}\ \lVert\mathbf{x} - \mathbf{c}\_j\rVert_2 $$

_Greedily picks the point furthest from everything chosen so far. Gives far better spatial coverage than random sampling at $$O(NK)$$ cost, and is what keeps thin structures represented after downsampling._

#### Sparse convolution {#cv-point-clouds-and-3d-perception--sparseconv}

A dense 3D convolution over a $$1000^3$$ voxel grid is impossible, and pointless: LiDAR occupies well under 1% of it. **Sparse convolution** stores only occupied voxels in a hash map and computes outputs only there.

- **Submanifold sparse convolution** restricts output to voxels that were _already_ occupied. This is the critical variant: ordinary sparse convolution dilates the occupied set at every layer, so after a few layers the "sparse" tensor is dense and the advantage is gone.
- Regular sparse convolution is still needed where receptive field must genuinely grow — typically at downsampling layers only.

#### Registration: ICP and its variants {#cv-point-clouds-and-3d-perception--registration}

**Point-to-point ICP**

$$ (\mathbf{R}^{_},\mathbf{t}^{_}) = \arg\min*{\mathbf{R},\mathbf{t}}\sum*{i}\big\lVert \mathbf{R}\mathbf{p}_i + \mathbf{t} - \mathbf{q}_{\kappa(i)}\big\rVert^{2} $$

_Alternate: (1) find correspondences $$\kappa$$ by nearest neighbour, (2) solve for the transform in closed form. Step 2 has an exact solution via SVD of the cross-covariance (the Kabsch/Procrustes algorithm): centre both clouds, take $$\mathbf{H} = \sum \tilde{\mathbf{p}}_i\tilde{\mathbf{q}}_i^{\top} = \mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^\top$$, then $$\mathbf{R} = \mathbf{V}\operatorname{diag}(1,1,\det(\mathbf{V}\mathbf{U}^\top))\mathbf{U}^{\top}$$ — the determinant term prevents a reflection._

**Point-to-plane ICP — converges far faster**

$$ \min\_{\mathbf{R},\mathbf{t}}\sum_i \Big(\big(\mathbf{R}\mathbf{p}\_i + \mathbf{t} - \mathbf{q}\_i\big)\cdot\mathbf{n}\_i\Big)^{2} $$

_Penalise only the component of the residual \_along the surface normal_. Sliding along a flat surface is then free, which is exactly right — two planar patches genuinely do not constrain in-plane motion. Typically converges in an order of magnitude fewer iterations. Linearised for small angles, it becomes a $$6\times6$$ linear system per iteration.\_

> **ICP is local — coarse alignment must come first**
> ICP converges to the nearest local minimum of a highly non-convex cost, and it does so _confidently_. A global initialisation is mandatory: RANSAC over **FPFH** descriptor matches, 4PCS, or a learned registration front end. This is the same ordering rule as [RANSAC before robust refinement](#cv-vision-objectives-and-optimization--map) — redescending objectives need a good starting point.

**FPFH** (Fast Point Feature Histogram) describes a point by histogramming the angular relations $$(\alpha,\phi,\theta)$$ between its normal and those of its neighbours, then convolving with neighbours' histograms. It is rotation-invariant by construction, which is what makes descriptor-based global registration possible at all.

#### Set-to-set losses {#cv-point-clouds-and-3d-perception--losses}

**Chamfer distance**

$$ d*{\mathrm{CD}}(\mathcal{S}\_1,\mathcal{S}\_2) = \frac{1}{\lvert\mathcal{S}\_1\rvert}\sum*{\mathbf{x}\in\mathcal{S}_1}\min_{\mathbf{y}\in\mathcal{S}_2}\lVert\mathbf{x}-\mathbf{y}\rVert_2^2 + \frac{1}{\lvert\mathcal{S}\_2\rvert}\sum_{\mathbf{y}\in\mathcal{S}_2}\min_{\mathbf{x}\in\mathcal{S}\_1}\lVert\mathbf{x}-\mathbf{y}\rVert_2^2 $$

_Cheap ($$O(N\log N)$$ with a kd-tree) and differentiable. **Its weakness is systematic:** it is minimised by clumping points in high-density regions, because nothing forces a one-to-one correspondence. Chamfer-optimal reconstructions look blurry and lose thin structure._

**Earth Mover's Distance**

$$ d*{\mathrm{EMD}}(\mathcal{S}\_1,\mathcal{S}\_2) = \min*{\phi:\ \mathcal{S}_1\to\mathcal{S}\_2}\ \sum_{\mathbf{x}\in\mathcal{S}\_1}\lVert \mathbf{x} - \phi(\mathbf{x})\rVert_2 $$

_$$\phi$$ is a \_bijection_, so every point must be used exactly once — which is precisely what prevents clumping. The cost is $$O(N^3)$$ exactly, or $$O(N^2)$$ with a Sinkhorn approximation, and it requires equal cardinality. EMD gives visibly better distributions; Chamfer is what most people can afford.\_

**Eikonal regularizer for implicit surfaces**

$$ \mathcal{L}_{\text{eik}} = \mathbb{E}_{\mathbf{x}}\Big[\big(\lVert\nabla_{\mathbf{x}} f(\mathbf{x})\rVert_2 - 1\big)^{2}\Big] $$

_A true signed distance field satisfies $$\lVert\nabla f\rVert = 1$$ everywhere. Without this term a learned implicit function has the right zero level set but meaningless values off-surface, which breaks sphere tracing, normal computation and any downstream geometric use._

#### 3D object detection {#cv-point-clouds-and-3d-perception--detection}

Output is a 7-DoF box $$(x,y,z,l,w,h,\vartheta)$$ — yaw only, since objects on a ground plane do not roll or pitch. Three architectural families:

- **Voxel-based** — VoxelNet, SECOND: voxelise, sparse-convolve, detect in BEV. Accurate; the sparse convolution is the cost.

- **Pillar-based** — PointPillars: collapse the vertical axis into pillars, then use a plain 2D CNN. Substantially faster, and the standard real-time choice.

- **Point-based** — PointRCNN: generate proposals directly from points, refine in canonical coordinates. No quantisation loss; slower.

**Yaw regression — avoiding the wrap-around**

$$ \mathcal{L}_{\vartheta} = \operatorname{smooth}_{L_1}\!\big(\sin(\hat{\vartheta} - \vartheta)\big) \qquad\text{or}\qquad \text{bin classification} + \text{residual regression} $$

_Regressing $$\vartheta$$ directly is broken at the $$\pm\pi$$ discontinuity, where a tiny angular error produces a huge loss. The $$\sin$$ form is smooth and periodic, but cannot distinguish a box from its 180° flip — acceptable for cars (a symmetric box), handled elsewhere by a separate direction classifier._

#### Tricks and failure modes {#cv-point-clouds-and-3d-perception--tricks}

> **Tricks**
>
> - **Voxel downsampling** to equalise density before anything else
> - **Ground removal** by RANSAC plane fitting — removes most points and most false positives
> - Normal estimation by local PCA (smallest eigenvector of the neighbourhood covariance)
> - **Ground-truth sampling augmentation**: paste extra object point clouds into scenes — the single strongest augmentation for 3D detection
> - Class-balanced voxel sampling; range-dependent neighbourhood radii
> - Correspondence rejection by normal compatibility and distance ratio

> **Failure modes**
>
> - **ICP converges to a confident wrong pose** from poor initialisation
> - **Sparse distant objects** — a car at 70 m may return ~10 points
> - **Symmetric and featureless geometry** — a cylinder or flat wall does not constrain pose
> - **Chamfer clumping** in reconstruction
> - **Reflective and transparent surfaces** — no return, or a spurious one
> - **Sensor-specific overfitting** — a model trained on 64-beam LiDAR fails on 32-beam

#### Takeaways {#cv-point-clouds-and-3d-perception--takeaways}

1. **Permutation invariance is the defining constraint**, and a symmetric pooling function is the minimal way to satisfy it.
2. **PointNet has no locality; PointNet++ adds the hierarchy back.** Multiscale structure is rediscovered here as everywhere.
3. **Submanifold sparse convolution exists to stop sparsity dilating away.**
4. **Point-to-plane ICP converges faster because it does not penalise legitimate sliding.**
5. **ICP is local and must be initialised globally** — FPFH + RANSAC, then refine.
6. **Chamfer is affordable and biased; EMD is correct and expensive.** The choice selects which artefact appears.

### 3D reconstruction and completion {#cv-3d-reconstruction-and-completion}

_Estimating continuous geometry rather than labels or boxes. Deliberately separate from [3D perception](#cv-point-clouds-and-3d-perception): that family predicts what and where, this one predicts \_surface_.\_

#### Choosing a surface representation {#cv-3d-reconstruction-and-completion--representations}

| Representation      | Stores                                        | Topology                         | Cost                                                |
| ------------------- | --------------------------------------------- | -------------------------------- | --------------------------------------------------- |
| **Point cloud**     | Samples on the surface                        | None — no connectivity           | $$O(N)$$                                            |
| **Mesh**            | Vertices + faces                              | Explicit, fixed at creation      | $$O(V+F)$$; editable, renderable                    |
| **Occupancy grid**  | $$o(\mathbf{x})\in\{0,1\}$$ per voxel         | Arbitrary                        | $$O(n^3)$$ — the binding constraint                 |
| **TSDF**            | Truncated signed distance per voxel           | Arbitrary                        | $$O(n^3)$$ dense, $$O(\text{surface})$$ hashed      |
| **Neural implicit** | $$f_\theta(\mathbf{x}) \to$$ SDF or occupancy | Arbitrary, continuous resolution | $$O(\lvert\theta\rvert)$$; needs a query per sample |

> **Implicit versus explicit — the trade that keeps recurring**
> An implicit field is resolution-free, handles arbitrary topology, and is compact. An explicit mesh or point set is directly renderable, editable and measurable. The decade's 3D story is largely a swing from explicit (TSDF, meshes) to implicit ([NeRF](#cv-neural-rendering-and-novel-views), DeepSDF) and then partly back to explicit ([3D Gaussian Splatting](#cv-3d-becomes-real-time-vision-learns-to-talk--3dgs)) — [mechanism 6](#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--m6).

#### TSDF fusion {#cv-3d-reconstruction-and-completion--tsdf}

**Per-voxel signed distance from one depth map**

$$ \mathrm{sdf}\_i(\mathbf{v}) = D_i\big(\pi(\mathbf{T}\_i^{-1}\mathbf{v})\big) - \big[\mathbf{T}_i^{-1}\mathbf{v}\big]\_z, \qquad \mathrm{tsdf}\_i(\mathbf{v}) = \max\!\Big(\!-1, \min\big(1, \tfrac{\mathrm{sdf}\_i}{\mu}\big)\!\Big) $$

_Positive in front of the surface, negative behind, truncated at $$\pm\mu$$. Truncation matters: it confines each depth measurement's influence to a band around the surface, so a measurement cannot assert anything about distant free space it never observed._

**Weighted running fusion**

$$ \mathrm{TSDF}_{k}(\mathbf{v}) = \frac{W_{k-1}(\mathbf{v})\,\mathrm{TSDF}_{k-1}(\mathbf{v}) + w_k(\mathbf{v})\,\mathrm{tsdf}\_k(\mathbf{v})}{W_{k-1}(\mathbf{v}) + w*k(\mathbf{v})}, \qquad W_k = \min\big(W*{k-1} + w*k,\ W*{\max}\big) $$

_A running weighted average — the MLE under Gaussian depth noise. Weights encode measurement confidence (angle to the normal, range, edge proximity). Capping $$W$$ at $$W_{\max}$$ keeps the model adaptive to change instead of frozen by history: without the cap, early measurements dominate forever and the reconstruction cannot correct itself.\_

Dense voxel grids scale as $$O(n^3)$$, so large scenes use **voxel hashing** — allocate blocks only near observed surfaces — or an octree. This is the same sparsity argument as [sparse convolution](#cv-point-clouds-and-3d-perception--sparseconv).

#### Marching cubes {#cv-3d-reconstruction-and-completion--marching}

Extract the zero level set as a mesh. For each cube of 8 voxels, the sign pattern at the corners gives an 8-bit index into a table of 256 cases (15 up to symmetry), each specifying which triangles to emit. Vertices are placed on edges by **linear interpolation**:

$$ \mathbf{p} = \mathbf{v}\_a + \frac{0 - f(\mathbf{v}\_a)}{f(\mathbf{v}\_b) - f(\mathbf{v}\_a)}\,(\mathbf{v}\_b - \mathbf{v}\_a) $$

_This interpolation is what gives sub-voxel accuracy — without it the mesh is blocky at the grid resolution. The classic caveat is **ambiguous cases**: some sign patterns admit two valid triangulations, and choosing inconsistently between adjacent cubes creates holes. Marching Cubes 33 and the asymptotic decider resolve this properly._

#### Poisson surface reconstruction {#cv-3d-reconstruction-and-completion--poisson}

Given oriented points $$(\mathbf{p}_i, \mathbf{n}_i)$$, treat the normals as samples of the gradient of an indicator function $$\chi$$ (1 inside, 0 outside) and solve for $$\chi$$:

$$ \min\_{\chi}\ \big\lVert \nabla\chi - \vec{V}\big\rVert^{2} \qquad\Longleftrightarrow\qquad \nabla^2\chi = \nabla\cdot\vec{V} $$

_$$\vec{V}$$ is a smoothed vector field built from the oriented normals. A Poisson equation, solved on an adaptive octree with a multigrid solver; the surface is then the level set at the average value of $$\chi$$ at the samples._

> **Why Poisson is the default for scanned data**
> Because it is a _global_ solve, it is inherently robust to noise — an erroneous normal is outvoted by its neighbours rather than producing a local spike, as it would in any local triangulation method. It also produces a watertight, manifold surface by construction.
>
> **The price:** it hallucinates surface in unobserved regions, closing over genuine holes with plausible geometry. Screened Poisson adds a positional constraint pulling the surface to the points; the standard practice is to trim the output by sampling density so invented regions are removed. **Normal orientation must be globally consistent** — flipped normals produce inside-out surfaces, and consistent orientation is itself a non-trivial minimum-spanning-tree problem.

#### Neural implicit surfaces {#cv-3d-reconstruction-and-completion--neural}

**DeepSDF-style objective**

$$ \mathcal{L} = \sum*{i}\big\lvert \operatorname{clamp}(f*\theta(\mathbf{x}_i), \delta) - \operatorname{clamp}(s_i, \delta)\big\rvert + \lambda_{\text{eik}}\,\mathbb{E}_{\mathbf{x}}\Big[\big(\lVert\nabla f_\theta(\mathbf{x})\rVert_2 - 1\big)^{2}\Big] $$

_Clamping concentrates capacity near the surface, where accuracy matters, rather than spending it on distant free space. The **Eikonal** term enforces $$\lVert\nabla f\rVert = 1$$, which is what makes $$f$$ a genuine signed \_distance_ rather than merely a function with the right zero set — necessary for sphere tracing, normals and offsetting.\_

**Occupancy networks** instead predict $$p(\text{occupied}\mid\mathbf{x})$$ with a BCE loss; simpler to train, but the field carries no distance information, so extracting normals requires finite differences. Sampling strategy dominates results in both: uniform sampling wastes capacity, so samples are drawn near the surface with a decaying offset distribution.

#### Shape completion {#cv-3d-reconstruction-and-completion--completion}

Real scans are partial — self-occlusion, limited viewpoints, absorbing or specular materials. Completion fills the unobserved geometry.

> **Completion is generation, not measurement**
> The back of an object was never observed. Any completion is a _sample from a learned prior_ over plausible shapes, and the model will produce one confidently whether or not it is right. [SAM 3D](#cv-any-view-geometry-concepts-and-embodiment--sam3d) makes this explicit — it predicts complete geometry including occluded regions, with a 5:1 human-preference win rate, while the occluded part remains plausible rather than measured. For any metrology application, report _observed_ and _inferred_ geometry separately.

#### Metrics and validation {#cv-3d-reconstruction-and-completion--metrics}

**Accuracy, completeness, F-score**

$$ \mathrm{Acc} = \operatorname*{median}*{\mathbf{p}\in R}\ \min*{\mathbf{q}\in G}\lVert\mathbf{p}-\mathbf{q}\rVert, \qquad \mathrm{Comp} = \operatorname*{median}_{\mathbf{q}\in G}\ \min_{\mathbf{p}\in R}\lVert\mathbf{p}-\mathbf{q}\rVert $$ $$ F*\tau = \frac{2 P*\tau R*\tau}{P*\tau + R*\tau}, \qquad P*\tau = \frac{\lvert\{\mathbf{p}\in R : \min\_{\mathbf{q}}\lVert\mathbf{p}-\mathbf{q}\rVert < \tau\}\rvert}{\lvert R\rvert} $$

_Accuracy penalises invented surface; completeness penalises missing surface. **Report both** — Poisson reconstruction trades one for the other directly, and a single Chamfer number hides which way. The F-score at a stated threshold $$\tau$$ is the standard summary (Tanks&Temples, ETH3D)._

**Normal consistency** $$\tfrac{1}{\lvert R\rvert}\sum \lvert \mathbf{n}_\mathbf{p}\cdot\mathbf{n}_{\mathrm{NN}(\mathbf{p})}\rvert$$ measures whether the surface _orientation_ is right, which Chamfer distance ignores entirely — two surfaces can be close yet differently oriented.

##### Geometric validation {#cv-3d-reconstruction-and-completion--mesh-validation}

- **Manifoldness** — every edge shared by exactly two faces; no non-manifold vertices.
- **Watertightness** — no boundary edges, so the mesh bounds a volume and can be measured.
- **Orientation consistency** — all face normals point outward; check via the sign of the signed volume.
- **Self-intersection** — must be absent for simulation, 3D printing or boolean operations.
- **Euler characteristic** $$V - E + F = 2 - 2g$$ — a quick genus check that catches spurious handles from noise.

#### Failure modes and takeaways {#cv-3d-reconstruction-and-completion--failures}

| Failure                       | Cause                                | Defense                                                                                    |
| ----------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------ |
| Surface invented over holes   | Poisson's global watertight solve    | Density trimming; screened Poisson                                                         |
| Inside-out surface            | Inconsistent normal orientation      | Global orientation propagation (MST over the kNN graph)                                    |
| Spurious handles / genus      | Noise bridging nearby surfaces       | Higher truncation $$\mu$$; topology-aware cleanup; Euler check                             |
| Over-smoothed thin structures | Voxel resolution below feature size  | Finer grid, hashing, implicit representation                                               |
| Drift in large scenes         | Pose error accumulating in fusion    | Loop closure and [deformation-graph](#cv-camera-pose-sfm-vo-and-slam--slam) re-integration |
| Blocky mesh                   | Marching cubes without interpolation | Linear edge interpolation; disambiguated case table                                        |

1. **Truncation is what makes TSDF sound** — a depth measurement should not claim knowledge of far-away free space.
2. **Cap the fusion weight**, or the reconstruction can never correct itself.
3. **Poisson is robust because it is global**, and hallucinates for the same reason.
4. **The Eikonal term is what makes an implicit field a distance field.**
5. **Completion is generation.** Separate observed from inferred geometry when it matters.
6. **Report accuracy and completeness separately**, plus normal consistency — one number hides the trade.

### Neural rendering and novel views {#cv-neural-rendering-and-novel-views}

_Make the renderer differentiable and the scene becomes an optimisation variable. The entire family follows from that one move._

#### The volume rendering integral {#cv-neural-rendering-and-novel-views--volrend}

**Continuous form**

$$ C(\mathbf{r}) = \int*{t_n}^{t_f} T(t)\,\sigma\big(\mathbf{r}(t)\big)\,\mathbf{c}\big(\mathbf{r}(t), \mathbf{d}\big)\,dt, \qquad T(t) = \exp\!\left(-\int*{t_n}^{t}\sigma\big(\mathbf{r}(s)\big)\,ds\right) $$

- $$\mathbf{r}(t)$$ — the ray $$\mathbf{o} + t\mathbf{d}$$
- $$\sigma$$ — volume density — differential probability of terminating at $$t$$
- $$\mathbf{c}$$ — view-dependent emitted colour
- $$T(t)$$ — accumulated transmittance: the probability the ray survives to $$t$$

**Discrete quadrature — the computed form**

$$ \hat{C}(\mathbf{r}) = \sum*{i=1}^{N} T_i\,\alpha_i\,\mathbf{c}\_i, \qquad \alpha_i = 1 - e^{-\sigma_i\delta_i}, \qquad T_i = \prod*{j=1}^{i-1}(1-\alpha_j) $$

_$$\delta_i = t_{i+1} - t*i$$ is the sample spacing. This is exactly **front-to-back alpha compositing** — the same operation as classical volume rendering and as [splatting](#cv-neural-rendering-and-novel-views--3dgs). Every term is differentiable with respect to $$\sigma_i$$ and $$\mathbf{c}_i$$, so a photometric loss on rendered pixels propagates gradients into the scene representation.*

> **The whole field in one sentence**
> Because rendering is differentiable, a [photometric residual](#cv-photometric-consistency) against the training views _optimises the scene itself_ — no 3D supervision, no correspondences, no explicit reconstruction step. The scene is whatever explains the images.

#### NeRF {#cv-neural-rendering-and-novel-views--nerf}

{% include figure.liquid loading="lazy" path="assets/img/cv/nerf_pipeline.png" class="img-fluid rounded z-depth-1" zoomable=true alt="NeRF pipeline: 5D coordinates sampled along rays, fed to an MLP producing colour and density, composited by volume rendering and compared to the observed pixel." caption="<strong>The differentiable loop.</strong> Sample along rays → query the MLP → composite → compare to the observed pixel. <em>Mildenhall et al., ECCV 2020 (arXiv:2003.08934).</em>" %}

$$ F*\Theta : (\mathbf{x}, \mathbf{d}) \mapsto (\mathbf{c}, \sigma), \qquad \mathcal{L} = \sum*{\mathbf{r}\in\mathcal{R}}\Big[\big\lVert\hat{C}_c(\mathbf{r}) - C(\mathbf{r})\big\rVert_2^2 + \big\lVert\hat{C}_f(\mathbf{r}) - C(\mathbf{r})\big\rVert_2^2\Big] $$

_Both the coarse and fine networks are supervised. Note the architectural detail that enforces multi-view consistency: $$\sigma$$ is predicted from $$\mathbf{x}$$ **alone**, and only $$\mathbf{c}$$ sees the view direction $$\mathbf{d}$$. Letting density depend on direction would allow the model to cheat by inventing different geometry per view._

##### Positional encoding — why it is mandatory {#cv-neural-rendering-and-novel-views--encoding}

$$ \gamma(p) = \Big(\sin(2^0\pi p),\ \cos(2^0\pi p),\ \dots,\ \sin(2^{L-1}\pi p),\ \cos(2^{L-1}\pi p)\Big) $$

_MLPs have a **spectral bias**: they fit low frequencies first and high frequencies extremely slowly. Without $$\gamma$$, NeRF produces blurry mush regardless of training time. Mapping coordinates to a Fourier basis makes high-frequency detail representable in a shallow network — equivalently, it turns the network's effective kernel from a wide smooth one into a tunable-bandwidth one. $$L=10$$ for position, $$L=4$$ for direction._

##### Hierarchical sampling {#cv-neural-rendering-and-novel-views--sampling}

Uniform sampling along a ray wastes almost all its samples in empty space. NeRF uses a coarse pass to build a piecewise-constant PDF from the coarse weights $$w_i = T_i\alpha_i$$, then inverse-transform-samples the fine pass from it — concentrating computation where the ray is likely to terminate. Later work replaces this with **occupancy grids** (skip empty space entirely) and **multiresolution hash encodings** (Instant-NGP), which together cut training from days to seconds.

#### 3D Gaussian Splatting {#cv-neural-rendering-and-novel-views--3dgs}

{% include figure.liquid loading="lazy" path="assets/img/cv/gaussiansplatting_pipeline.png" class="img-fluid rounded z-depth-1" zoomable=true alt="3DGS pipeline: SfM initialisation, projection, differentiable tile rasterisation, gradient flow and adaptive density control." caption="<strong>No network in the inner loop.</strong> Initialise from SfM points, project and rasterise, backpropagate, and adaptively clone, split or prune. <em>Kerbl, Kopanas, Leimkühler & Drettakis, SIGGRAPH 2023.</em>" %}

**The primitive**

$$ G(\mathbf{x}) = \exp\!\left(-\tfrac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^{\top}\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})\right), \qquad \boldsymbol{\Sigma} = \mathbf{R}\mathbf{S}\mathbf{S}^{\top}\mathbf{R}^{\top} $$

_The factorisation $$\boldsymbol{\Sigma} = \mathbf{R}\mathbf{S}\mathbf{S}^\top\mathbf{R}^\top$$ with a rotation $$\mathbf{R}$$ (quaternion) and a diagonal scale $$\mathbf{S}$$ guarantees $$\boldsymbol{\Sigma}$$ stays **positive semi-definite** under unconstrained gradient descent. Optimising the six entries of $$\boldsymbol{\Sigma}$$ directly would produce invalid covariances._

**Projection to 2D**

$$ \boldsymbol{\Sigma}' = \mathbf{J}\mathbf{W}\boldsymbol{\Sigma}\mathbf{W}^{\top}\mathbf{J}^{\top} $$

_$$\mathbf{W}$$ is the viewing transform and $$\mathbf{J}$$ the Jacobian of the affine approximation to the perspective projection. A projected 3D Gaussian is a 2D Gaussian — which is exactly why the primitive was chosen, since it makes rasterisation closed-form._

**Compositing — the same alpha blend as NeRF**

$$ C = \sum*{i\in\mathcal{N}} c_i\,\alpha_i\prod*{j=1}^{i-1}(1-\alpha_j) $$

_Over depth-sorted Gaussians overlapping the tile. Identical in form to NeRF's quadrature — the difference is that $$\alpha_i$$ comes from evaluating an analytic 2D Gaussian rather than from querying an MLP, so there is **no network in the inner loop**._

##### Adaptive density control {#cv-neural-rendering-and-novel-views--density}

The part that makes it work. Every ~100 iterations, examine the view-space positional gradient $$\lVert\nabla_{\boldsymbol{\mu}}\mathcal{L}\rVert$$:

- **Clone** — large gradient, small Gaussian ⇒ the region is _under-reconstructed_; duplicate the Gaussian and move the copy along the gradient.
- **Split** — large gradient, large Gaussian ⇒ it is covering too much; replace with two smaller ones sampled from its own distribution, scaled by $$1/\phi$$ ($$\phi\approx1.6$$).
- **Prune** — opacity below a threshold, or a Gaussian that has grown implausibly large in world or screen space.
- **Opacity reset** — periodically set all $$\alpha$$ near zero and let them recover, which culls floaters that the photometric loss alone would keep.

#### The regularizers, and what each prevents {#cv-neural-rendering-and-novel-views--regularizers}

$$ \mathcal{L} = \lambda*{\text{rgb}}\mathcal{L}*{\text{rgb}} + \lambda*{\text{depth}}\mathcal{L}*{\text{depth}} + \lambda*{\text{mask}}\mathcal{L}*{\text{mask}} + \lambda*{\text{geom}}\mathcal{L}*{\text{geom}} + \lambda*{\text{reg}}\mathcal{L}*{\text{reg}} $$

| Term                   | Form                                                       | Failure it prevents                                                                            |
| ---------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Distortion**         | $$\sum_{i,j} w_i w_j \lvert t_i - t_j\rvert$$              | **Floaters** — encourages weights to concentrate at one depth rather than spread along the ray |
| **Opacity entropy**    | $$-\big(\alpha\log\alpha + (1-\alpha)\log(1-\alpha)\big)$$ | Semi-transparent haze; pushes $$\alpha$$ toward 0 or 1                                         |
| **Total variation**    | $$\lVert\nabla\sigma\rVert_1$$ on the grid                 | High-frequency noise in voxel/hash representations                                             |
| **Eikonal**            | $$(\lVert\nabla f\rVert - 1)^2$$                           | Degenerate SDFs in surface-based variants (NeuS, VolSDF)                                       |
| **Normal consistency** | agreement of predicted and gradient normals                | Geometry that renders correctly but has wrong orientation                                      |
| **SSIM / perceptual**  | $$1-\mathrm{SSIM}$$                                        | Over-smoothed texture from pure L2                                                             |

> **Why floaters exist at all**
> With few views, a small semi-transparent blob placed just in front of a camera can explain that camera's pixels perfectly while being invisible to the others. The photometric loss is _fully satisfied_. Nothing in the data rules it out — only a prior can, which is what the distortion and entropy terms supply. This is the clearest example in the site of [regularization resolving genuine underdetermination](#cv-vision-objectives-and-optimization--regularizers) rather than merely smoothing.

#### Practical machinery {#cv-neural-rendering-and-novel-views--tricks}

- **Appearance embeddings** — a per-image latent absorbing exposure and white-balance variation, so the geometry is not forced to explain photometric inconsistency.
- **Transient masks** — per-image uncertainty fields that down-weight pedestrians and other movers in unstructured photo collections (NeRF-W).
- **Camera pose refinement** — jointly optimise $$\mathbf{T}_i$$ with the scene; SfM poses are rarely accurate enough for sharp results.
- **Background models** — an inverted-sphere or NDC parameterisation for unbounded scenes (NeRF++, Mip-NeRF 360), since a bounded grid cannot represent the sky.
- **Patch-based losses** rather than isolated rays, so structural terms such as SSIM are computable.
- **Coarse-to-fine frequency schedules** — anneal in the high-frequency positional-encoding bands, which markedly improves pose-refinement stability.

#### Metrics and failure modes {#cv-neural-rendering-and-novel-views--metrics}

Reported as **PSNR / SSIM / LPIPS** on held-out views. The same [perception–distortion caveat](#cv-restoration-and-enhancement--deep) applies: PSNR rewards blur, and a method can win on PSNR while looking worse. For geometry quality, report depth or mesh metrics separately — **view synthesis quality does not imply correct geometry**, and 3DGS in particular can look photorealistic while being locally wrong by centimetres.

| Failure                       | Cause                                                 | Defense                                               |
| ----------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| **Floaters**                  | Few views; blob explains one camera only              | Distortion loss, opacity reset, more views            |
| **Background collapse**       | Unbounded scene in a bounded parameterisation         | NDC / inverted-sphere background model                |
| **Blur**                      | Inaccurate poses; no positional encoding; pure L2     | Pose refinement, encoding, SSIM term                  |
| **Ghosting from movers**      | Transient objects treated as static geometry          | Transient masks, uncertainty fields                   |
| **Anisotropic spikes (3DGS)** | Elongated Gaussians fit view-dependent effects        | Scale regularisation; pruning oversized primitives    |
| **No usable surface**         | Density field is not a surface                        | SDF-based variants (NeuS), or SuGaR / 2DGS for splats |
| **Specular surfaces wrong**   | View-dependent colour absorbs what should be geometry | Ref-NeRF-style reflection parameterisation            |

#### Takeaways {#cv-neural-rendering-and-novel-views--takeaways}

1. **Differentiable rendering turns the scene into an optimisation variable.** That single move defines the field.
2. **NeRF and 3DGS composite identically** — front-to-back alpha blending. They differ only in where $$\alpha$$ comes from.
3. **Positional encoding is not a trick but a necessity**, because MLPs are spectrally biased.
4. **Density must not depend on view direction**, or multi-view consistency is forfeited.
5. **Adaptive density control is what makes splatting work**; the primitive alone is not enough.
6. **Regularizers here resolve genuine ambiguity.** Floaters are consistent with the data, and only a prior excludes them.
7. **Good renders do not imply good geometry.** Evaluate them separately.

### Image generation and translation {#cv-image-generation-and-translation}

_Learning the image \_distribution_, as opposed to [reconstructing a particular scene](#cv-neural-rendering-and-novel-views). Kept separate deliberately: rendering is constrained by camera geometry, generation is not.\_

#### Four model families {#cv-image-generation-and-translation--families}

| Family               | Objective                                  | Sampling                         | Weakness                                                |
| -------------------- | ------------------------------------------ | -------------------------------- | ------------------------------------------------------- |
| **VAE**              | ELBO — lower bound on likelihood           | One forward pass                 | Blurry: the Gaussian decoder produces conditional means |
| **GAN**              | Adversarial minimax                        | One forward pass                 | Unstable; mode collapse; no likelihood                  |
| **Autoregressive**   | Exact likelihood by chain rule             | $$O(N)$$ sequential              | Slow; imposes an arbitrary pixel ordering               |
| **Diffusion / flow** | Denoising regression (an ELBO in disguise) | Iterative, $$10$$–$$1000$$ steps | Sampling cost                                           |

#### VAE {#cv-image-generation-and-translation--vae}

**Evidence lower bound**

$$ \log p*\theta(\mathbf{x}) \;\ge\; \underbrace{\mathbb{E}*{q*\phi(\mathbf{z}\mid\mathbf{x})}\big[\log p*\theta(\mathbf{x}\mid\mathbf{z})\big]}_{\text{reconstruction}} \;-\; \underbrace{D_{\mathrm{KL}}\big(q*\phi(\mathbf{z}\mid\mathbf{x})\,\big\Vert\,p(\mathbf{z})\big)}*{\text{regularization}} $$

_The reparameterisation trick $$\mathbf{z} = \boldsymbol{\mu}_\phi + \boldsymbol{\sigma}_\phi\odot\boldsymbol{\epsilon}$$, $$\boldsymbol{\epsilon}\sim\mathcal{N}(0,\mathbf{I})$$, moves the stochasticity outside the network so gradients flow through $$\boldsymbol{\mu}$$ and $$\boldsymbol{\sigma}$$. With a Gaussian likelihood the reconstruction term is an L2 loss, which is why plain VAEs are blurry — **L2 produces the conditional mean of all plausible outputs**._

**VQ-VAE** replaces the continuous latent with a learned discrete codebook, sidestepping posterior collapse and making the latent amenable to an autoregressive or diffusion prior. It is the reason latent diffusion has a usable latent space at all.

#### GANs {#cv-image-generation-and-translation--gan}

**The minimax objective**

$$ \min*G\max_D\ \mathbb{E}*{\mathbf{x}\sim p*{\text{data}}}\big[\log D(\mathbf{x})\big] + \mathbb{E}*{\mathbf{z}\sim p\_{\mathbf{z}}}\big[\log\big(1 - D(G(\mathbf{z}))\big)\big] $$

_At the optimal discriminator this minimises the **Jensen–Shannon divergence** between generated and real distributions. That is the source of the instability: if the two distributions have disjoint support — which is typical early in training, since natural images lie on a low-dimensional manifold — JS is constant at $$\log 2$$ and its gradient is \_zero_. The generator receives no signal about which way to move.\_

**Wasserstein GAN with gradient penalty**

$$ \mathcal{L} = \mathbb{E}_{\tilde{\mathbf{x}}}\big[D(\tilde{\mathbf{x}})\big] - \mathbb{E}_{\mathbf{x}}\big[D(\mathbf{x})\big] + \lambda\,\mathbb{E}_{\hat{\mathbf{x}}}\Big[\big(\lVert\nabla_{\hat{\mathbf{x}}}D(\hat{\mathbf{x}})\rVert_2 - 1\big)^{2}\Big] $$

_The Earth Mover's distance is finite and differentiable even for disjoint supports, so gradients survive. The Kantorovich–Rubinstein duality requires $$D$$ to be 1-Lipschitz; the gradient penalty enforces that softly on interpolates $$\hat{\mathbf{x}}$$ between real and fake, which works far better than the original weight clipping._

The StyleGAN line then attacked quality rather than stability: **progressive growing** (train at $$4^2$$, fade in resolution) made high-resolution training stable; **StyleGAN** added a mapping network $$z\to w$$ and per-resolution AdaIN injection for a disentangled latent; **StyleGAN2** diagnosed AdaIN-induced blob artefacts and replaced it with weight demodulation, plus a path-length regularizer that also made the generator far easier to invert. See [the 2016–2018 era page](#cv-depth-detection-and-the-first-believable-images--gans).

> **Mode collapse, precisely**
> Nothing in the minimax objective rewards _coverage_. A generator that produces one perfect image fools a discriminator just as well as one that covers the distribution, so the equilibrium is not unique and training can converge to a degenerate solution. Diffusion does not have this failure mode because its objective is a per-sample regression, not a game.

#### Diffusion {#cv-image-generation-and-translation--diffusion}

**Forward process — fixed, no learning**

$$ q(\mathbf{x}_t\mid\mathbf{x}_{t-1}) = \mathcal{N}\big(\mathbf{x}_t;\ \sqrt{1-\beta_t}\,\mathbf{x}_{t-1},\ \beta*t\mathbf{I}\big) $$ $$ q(\mathbf{x}\_t\mid\mathbf{x}\_0) = \mathcal{N}\big(\mathbf{x}\_t;\ \sqrt{\bar\alpha_t}\,\mathbf{x}\_0,\ (1-\bar\alpha_t)\mathbf{I}\big), \qquad \bar\alpha_t = \prod*{s=1}^{t}(1-\beta_s) $$

_The closed form for $$q(\mathbf{x}_t\mid\mathbf{x}_0)$$ is what makes training cheap: any timestep is reached in one step, $$\mathbf{x}_t = \sqrt{\bar\alpha_t}\mathbf{x}_0 + \sqrt{1-\bar\alpha_t}\,\boldsymbol{\epsilon}$$, instead of simulating the chain._

**Training objective — a plain regression**

$$ \mathcal{L}_{\text{simple}} = \mathbb{E}_{t,\mathbf{x}_0,\boldsymbol{\epsilon}}\Big[\big\lVert\boldsymbol{\epsilon} - \boldsymbol{\epsilon}_\theta\big(\sqrt{\bar\alpha_t}\mathbf{x}\_0 + \sqrt{1-\bar\alpha_t}\boldsymbol{\epsilon},\ t\big)\big\rVert^{2}\Big] $$

_Predict the noise that was added. Stable, has a unique optimum, needs no discriminator, and is a reweighted ELBO. **This objective is the whole reason diffusion displaced GANs** — not sample quality per se, but that the optimisation is a well-posed regression._

**Reverse (sampling) step**

$$ \mathbf{x}_{t-1} = \frac{1}{\sqrt{1-\beta_t}}\left(\mathbf{x}\_t - \frac{\beta_t}{\sqrt{1-\bar\alpha_t}}\,\boldsymbol{\epsilon}_\theta(\mathbf{x}\_t,t)\right) + \sigma_t\mathbf{z}, \qquad \mathbf{z}\sim\mathcal{N}(0,\mathbf{I}) $$

**Classifier-free guidance**

$$ \tilde{\boldsymbol{\epsilon}}_\theta(\mathbf{x}\_t, \mathbf{c}) = \boldsymbol{\epsilon}_\theta(\mathbf{x}_t,\varnothing) + s\big(\boldsymbol{\epsilon}_\theta(\mathbf{x}_t,\mathbf{c}) - \boldsymbol{\epsilon}_\theta(\mathbf{x}\_t,\varnothing)\big) $$

_Train one model with random condition dropout, then \_extrapolate_ away from the unconditional prediction at sampling time. One scalar $$s$$ trades diversity for prompt adherence; $$s\approx7.5$$ is typical. Universally adopted, and the single most important sampling-time knob.\_

**Score-based view**

$$ \boldsymbol{\epsilon}_\theta(\mathbf{x}\_t,t) \approx -\sqrt{1-\bar\alpha_t}\ \nabla_{\mathbf{x}\_t}\log p_t(\mathbf{x}\_t) $$

_Noise prediction \_is_ score estimation up to scale. This unifies DDPM with score matching and with SDE/ODE formulations, and is what licenses deterministic samplers (DDIM, DPM-Solver) that integrate the probability-flow ODE in 10–50 steps instead of 1000.\_

#### Latent diffusion and DiT {#cv-image-generation-and-translation--latent}

{% include figure.liquid loading="lazy" path="assets/img/cv/ldm_arch.png" class="img-fluid rounded z-depth-1" zoomable=true alt="Latent diffusion architecture: VAE encoder to a compressed latent, diffusion U-Net with cross-attention conditioning, decoder back to pixels." caption="<strong>Compress once, denoise many times.</strong> Diffusion runs at ~64×64 instead of 512×512 — roughly a 48× smaller tensor. <em>Rombach, Blattmann, Lorenz, Esser & Ommer, CVPR 2022.</em>" %}

**Cross-attention conditioning**

$$ \operatorname{Attn}(\mathbf{Q},\mathbf{K},\mathbf{V}) = \operatorname{softmax}\!\left(\frac{\mathbf{Q}\mathbf{K}^{\top}}{\sqrt{d}}\right)\mathbf{V}, \qquad \mathbf{Q} = \mathbf{W}_Q\varphi(\mathbf{z}\_t),\quad \mathbf{K},\mathbf{V} = \mathbf{W}_{K,V}\,\tau\_\theta(\mathbf{c}) $$

_The conditioning $$\mathbf{c}$$ — text, layout, depth, semantic map — enters as keys and values while the noisy latent supplies queries. Because $$\tau_\theta$$ is modality-agnostic, the same architecture accepts any conditioning signal, which is why one model family covers text-to-image, inpainting, super-resolution and layout-to-image.\_

**DiT** replaces the U-Net with a transformer over latent patches, conditioned through **adaLN-Zero** — per-block scale and shift regressed from the timestep embedding, initialised so each block starts as the identity ([mechanism 1](#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--m1)). Its finding: FID decreases smoothly with transformer Gflops, giving generation a scaling law and making [video generation](#cv-video-depth-and-concepts--sora) a compute question.

#### Flow matching and few-step sampling {#cv-image-generation-and-translation--flow}

**Flow matching / rectified flow**

$$ \mathbf{x}_t = (1-t)\,\mathbf{x}\_0 + t\,\mathbf{x}\_1, \qquad \mathcal{L} = \mathbb{E}_{t,\mathbf{x}_0,\mathbf{x}\_1}\Big[\big\lVert v_\theta(\mathbf{x}\_t, t) - (\mathbf{x}\_1 - \mathbf{x}\_0)\big\rVert^{2}\Big] $$

_Regress the \_velocity field_ transporting noise to data along a prescribed — preferably straight — path. Simulation-free training, and straight paths need fewer integration steps than diffusion's curved ones. Adopted as the training objective of SD3 and Flux.\_

**Consistency models**

$$ f*\theta(\mathbf{x}\_t, t) = \mathbf{x}\_0 \quad\forall t, \qquad \mathcal{L} = d\big(f*\theta(\mathbf{x}_{t_{n+1}}, t*{n+1}),\ f*{\theta^-}(\hat{\mathbf{x}}\_{t_n}, t_n)\big) $$

_Train a network mapping \_any_ point on a probability-flow ODE trajectory directly to its origin, with a self-consistency constraint along the trajectory ($$\theta^-$$ is an EMA target). Gives **one- or two-step** sampling. Two routes to the same goal: _shorten the path_ (flow matching) or _learn to skip along it_ (consistency).\_

#### Image-to-image translation {#cv-image-generation-and-translation--translation}

**CycleGAN — unpaired translation**

$$ \mathcal{L}_{\text{cyc}} = \mathbb{E}_{\mathbf{x}}\big[\lVert F(G(\mathbf{x})) - \mathbf{x}\rVert_1\big] + \mathbb{E}\_{\mathbf{y}}\big[\lVert G(F(\mathbf{y})) - \mathbf{y}\rVert_1\big] $$

_With no paired data, an adversarial loss alone is satisfied by \_any_ output in the target domain — the mapping is unconstrained. Cycle consistency forces $$G$$ and $$F$$ to be approximate inverses, which pins content while allowing style to change. A canonical instance of the [consistency-constraint](#cv-cross-cutting-mechanisms-and-failure-modes--consistency) family. Its known pathology: the network can _steganographically_ hide source information in imperceptible high-frequency noise to satisfy the cycle without preserving semantics.\_

**Pix2Pix** handles the paired case with a conditional GAN plus an L1 term, and uses a _PatchGAN_ discriminator that classifies $$N\times N$$ patches rather than whole images — restricting the discriminator to local texture, since L1 already handles low frequencies. **ControlNet** (see [2022–2023](#cv-foundation-models-and-the-promptable-paradigm--controlnet)) is the modern answer: a frozen diffusion base plus a zero-initialised trainable branch accepting edges, depth, pose or segmentation.

#### Metrics {#cv-image-generation-and-translation--metrics}

**Fréchet Inception Distance**

$$ \mathrm{FID} = \lVert\boldsymbol{\mu}\_r - \boldsymbol{\mu}\_g\rVert_2^2 + \operatorname{Tr}\!\Big(\boldsymbol{\Sigma}\_r + \boldsymbol{\Sigma}\_g - 2(\boldsymbol{\Sigma}\_r\boldsymbol{\Sigma}\_g)^{1/2}\Big) $$

_Fréchet distance between Gaussians fitted to Inception features of real and generated sets. **Caveats that are routinely ignored:** it is biased by sample count (compare only at equal $$N$$, usually 50k); it depends on the Inception backbone and even the resizing implementation; and it cannot evaluate a single image._

- **Precision / recall** for generative models separate _fidelity_ (samples lie on the data manifold) from _coverage_ (the manifold is covered) — FID conflates them, so a mode-collapsed model can score deceptively well.
- **CLIP score** for prompt adherence; **human preference** remains the arbiter, since all automatic metrics correlate imperfectly.

#### Failure modes and takeaways {#cv-image-generation-and-translation--failures}

| Failure                               | Cause                                       | Defense                                                        |
| ------------------------------------- | ------------------------------------------- | -------------------------------------------------------------- |
| Mode collapse (GAN)                   | Objective does not reward coverage          | WGAN-GP, minibatch discrimination, or use diffusion            |
| Blurry samples (VAE)                  | Gaussian likelihood ⇒ L2 ⇒ conditional mean | Discrete latents, adversarial or perceptual decoder loss       |
| Over-saturated, low-diversity samples | Guidance scale too high                     | Lower $$s$$; dynamic thresholding                              |
| Poor compositional prompts            | Cross-attention binds attributes weakly     | Attention control, layout conditioning, stronger text encoders |
| Text rendering garbled                | Latent VAE discards glyph-scale detail      | Higher-resolution latents; character-aware text encoders       |
| CycleGAN hides information            | Cycle loss satisfiable steganographically   | Noise/augmentation in the cycle; additional structural losses  |

1. **Diffusion replaced adversarial training because its objective is a stable regression**, not because of any single sample-quality result.
2. **GAN instability is a divergence problem** — JS has no gradient on disjoint supports; Wasserstein does.
3. **Noise prediction is score estimation**, which is what licenses fast ODE samplers.
4. **Classifier-free guidance is the key sampling knob**, and it trades diversity for adherence.
5. **Working in a latent space is what made generation affordable** ([mechanism 4](#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--m4)).
6. **FID is fragile.** Equal sample counts, same backbone, and report precision/recall alongside.

## Multimodal

### Vision–language understanding {#cv-vision-language-understanding}

_Language as an open label space. The family that removed the fixed class list — and imported a new set of failure modes with it._

#### The task family {#cv-vision-language-understanding--tasks}

| Task                                | Input → output                                           | Metric               |
| ----------------------------------- | -------------------------------------------------------- | -------------------- |
| Captioning                          | Image → sentence                                         | CIDEr, SPICE, BLEU   |
| VQA                                 | Image + question → answer                                | VQA accuracy, ANLS   |
| Text–image retrieval                | Query → ranked set                                       | Recall@K             |
| Referring grounding                 | Image + phrase → box/mask                                | Precision@IoU        |
| Open-vocab detection / segmentation | Image + class names → boxes/masks                        | AP on novel classes  |
| Scene graphs                        | Image → $$\langle$$subject, predicate, object$$\rangle$$ | Recall@K on triplets |

#### Contrastive image–text pretraining {#cv-vision-language-understanding--contrastive}

{% include figure.liquid loading="lazy" path="assets/img/cv/clip_arch.png" class="img-fluid rounded z-depth-1" zoomable=true alt="CLIP: contrastive pretraining matching images to captions within a batch, then zero-shot classification from class-name prompts." caption="<strong>The batch is the task.</strong> Identify the $$N$$ correct pairings among $$N^2$$ candidates; at test time the text tower synthesises a classifier from class names. <em>Radford et al., ICML 2021.</em>" %}

**CLIP's symmetric InfoNCE**

$$ \mathcal{L} = \tfrac12\Big[\underbrace{-\tfrac{1}{N}\sum_{i}\log\frac{e^{\langle \mathbf{I}_i, \mathbf{T}_i\rangle/\tau}}{\sum_j e^{\langle \mathbf{I}_i, \mathbf{T}_j\rangle/\tau}}}_{\text{image}\to\text{text}} \;+\; \underbrace{-\tfrac{1}{N}\sum_{j}\log\frac{e^{\langle \mathbf{I}_j, \mathbf{T}_j\rangle/\tau}}{\sum_i e^{\langle \mathbf{I}_i, \mathbf{T}_j\rangle/\tau}}}_{\text{text}\to\text{image}} \Big] $$

_Embeddings are L2-normalised, so $$\langle\cdot,\cdot\rangle$$ is cosine similarity. $$\tau$$ is \_learned_ (as $$\log\tau$$, clipped) rather than fixed. The softmax normalises over the whole batch, which is why CLIP needs very large batches — the negatives _are_ the batch.\_

**SigLIP — replacing softmax with sigmoid**

$$ \mathcal{L} = -\frac{1}{N}\sum*{i=1}^{N}\sum*{j=1}^{N}\log\frac{1}{1 + e^{\,z*{ij}(-t\,\langle\mathbf{I}\_i,\mathbf{T}\_j\rangle + b)}}, \qquad z*{ij} = \begin{cases}+1 & i=j\\ -1 & i\neq j\end{cases} $$

_Every pair is an independent binary classification, so there is **no global normalisation over the batch**. Consequences: memory no longer scales with $$N^2$$ across devices, training works at modest batch sizes, and the learned bias $$b$$ absorbs the severe positive/negative imbalance. This is why SigLIP largely replaced CLIP as a vision tower._

**Zero-shot classification by prompt**

$$ \hat{y} = \arg\max\_{c}\ \big\langle \mathbf{I},\ \mathbf{T}(\text{"a photo of a } \{c\}\text{"})\big\rangle $$

_**Prompt ensembling** — averaging the normalised embeddings of ~80 templates ("a bad photo of a {c}", "a cropped photo of a {c}", …) — reliably adds several points, because it marginalises over rendering style rather than committing to one phrasing._

#### Connector architectures {#cv-vision-language-understanding--connectors}

How do image tokens enter a language model? This is the main design axis of the entire generative-VLM literature.

| Connector                          | Mechanism                                                          | Tokens             | Trade                                               |
| ---------------------------------- | ------------------------------------------------------------------ | ------------------ | --------------------------------------------------- |
| **Linear / MLP** (LLaVA)           | Project every patch embedding into the LLM's token space           | All ($$\sim$$576)  | Simplest; token count grows with resolution         |
| **Q-Former** (BLIP-2)              | $$K$$ learned queries cross-attend to image features               | Fixed ($$\sim$$32) | Constant cost; a bottleneck that can drop detail    |
| **Perceiver resampler** (Flamingo) | Latent array cross-attends; gated cross-attn inserted into the LLM | Fixed              | Handles video; more invasive to the LLM             |
| **Native / early fusion**          | Patches are tokens from layer 0                                    | Dynamic            | Most flexible; must be trained jointly from scratch |

{% include figure.liquid loading="lazy" path="assets/img/cv/llava_arch.png" class="img-fluid rounded z-depth-1" zoomable=true alt="LLaVA architecture: frozen CLIP vision encoder, learned projection, pretrained language model." caption="<strong>Architecturally minimal, methodologically novel.</strong> The contribution was using language-only GPT-4 to <em>synthesise</em> multimodal instruction data that did not exist. <em>Liu, Li, Wu & Lee, NeurIPS 2023.</em>" %}

**Resolution** is the recurring practical problem: a fixed $$224^2$$ tower destroys small text and fine structure. Answers are AnyRes/tiling (split the image into crops plus a thumbnail) and **native dynamic-resolution ViTs** with window attention, as in Qwen2.5-VL, which preserve native resolution at bounded cost.

#### Grounding losses {#cv-vision-language-understanding--grounding}

**Region–word alignment**

$$ \mathcal{L}_{\text{ground}} = -\sum_{i}\log\frac{\exp\big(\langle \mathbf{r}_i, \mathbf{w}_{\pi(i)}\rangle/\tau\big)}{\sum*{j}\exp\big(\langle \mathbf{r}\_i, \mathbf{w}*{j}\rangle/\tau\big)} $$

_Replaces a detector's fixed classification head with a similarity against \_text_ embeddings, which is what makes the vocabulary open: adding a class means adding a string. [Grounding DINO](#cv-foundation-models-and-the-promptable-paradigm--openvocab) fuses language at the neck, the query initialisation _and_ the head rather than only at the output, which is why it handles arbitrary referring expressions and not just class names.\_

The composition **Grounding DINO + SAM** became the default open-vocabulary _segmentation_ pipeline: one model names and localises, the other produces the mask. That is a direct consequence of [SAM's decision not to classify](#cv-foundation-models-and-the-promptable-paradigm--sam-decisions).

#### Hallucination and its control {#cv-vision-language-understanding--hallucination}

> **Object hallucination is the characteristic failure**
> A VLM describes objects that are not present, because the language model's prior over plausible scenes overrides weak visual evidence — "a kitchen" strongly predicts "a refrigerator" whether or not one is visible. Measured by **POPE**, which asks balanced yes/no questions about object presence, including adversarially-chosen absent objects that _co-occur_ frequently with present ones. Models score far worse on the adversarial split, which is the diagnostic that the failure is prior-driven rather than perceptual.

- **Mitigations:** contrastive decoding against a blurred or blank image (amplifying what the image contributes); grounding verification, where each claim must be localisable; retrieval augmentation; and explicit abstention training.
- **Evaluation caution:** CIDEr and BLEU reward fluent, generic captions and barely penalise a hallucinated object — so caption metrics systematically understate this failure.

#### Where the family stands {#cv-vision-language-understanding--state}

| Capability                     | Status     | Evidence                                                     |
| ------------------------------ | ---------- | ------------------------------------------------------------ |
| Document & chart understanding | **Strong** | DocVQA 96.4% (Qwen2.5-VL); >90% on charts                    |
| Open-vocabulary recognition    | **Strong** | Zero-shot transfer across arbitrary class lists              |
| Multi-discipline reasoning     | Moderate   | MMMU ~70% with test-time scaling (InternVL 2.5)              |
| Counting, spatial relations    | Weak       | Caption supervision rarely depends on them                   |
| Fine-grained shape & pattern   | **Weak**   | **~30–45%** for InternVL3 and Qwen2.5-VL (2026 benchmarking) |

> **The gap is the interface, not the language model**
> These models _read_ text in images superbly and _reason about geometry_ in them poorly — a 50-point spread between two capabilities that both require "understanding the image". The cause is the training distribution and the vision–language interface: web captions describe objects and text, not angles, counts or spatial relations. Scaling the LLM does not fix it, which is why this is listed among the [open problems](#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--open).

#### Tricks and takeaways {#cv-vision-language-understanding--tricks}

- **Large, diverse paired data** accounts for more of the result than any other factor; curation and deduplication matter more than architecture.
- **Hard-negative captions** — minimally edited captions (swapped attributes, reordered relations) are what force compositional binding rather than bag-of-words matching.
- **Frozen versus jointly trained vision tower** is the most consequential architectural choice; freezing preserves the tower's robustness, unfreezing adapts it to the LLM.
- **Prompt ensembling and class-name templates** for zero-shot.
- **Two-stage training**: align the connector first with everything else frozen, then instruction-tune.
- **Feed OCR tokens** alongside pixels when documents matter and the tower's resolution is limited.

1. **Language as label space removed the closed vocabulary** — the decade's third interface change.
2. **SigLIP's sigmoid removes the batch-size coupling** that made CLIP expensive to train.
3. **The connector is the design axis**: token count, resolution handling, and whether the tower is frozen.
4. **Grounding is contrastive alignment against text**, which is what makes the vocabulary open.
5. **Hallucination is the language prior overriding weak pixels**, and caption metrics hide it.
6. **These models read text accurately and estimate quantities poorly.** Which side a task falls on determines whether they apply.

### Scene reasoning and embodied vision {#cv-scene-reasoning-and-embodied-vision}

_Where perception stops being the output and becomes an input to action — which changes what "good enough" means, and makes calibrated uncertainty a requirement._

#### Scene graphs and relationships {#cv-scene-reasoning-and-embodied-vision--scenegraph}

**Factorised scene-graph likelihood**

$$ p(G\mid I) = \underbrace{p(B\mid I)}_{\text{boxes}}\cdot\underbrace{p(O\mid B, I)}_{\text{object labels}}\cdot\underbrace{p(R\mid O, B, I)}\_{\text{relations}} $$

_A graph $$G = (O, R)$$ of objects and $$\langle$$subject, predicate, object$$\rangle$$ triplets. Conditioning relations on \_both_ object labels is what lets a strong language prior do most of the work — which is also the problem below.\_

> **Scene-graph benchmarks are dominated by predicate frequency**
> "on", "has" and "wearing" account for the great majority of annotated relations. A model that _ignores the image_ and predicts the most frequent predicate compatible with the object pair scores high on Recall@K. This is why **mean Recall@K** (averaged over predicate classes) and zero-shot triplet recall are the meaningful numbers — an instance of the general [evaluation](#cv-evaluation-and-failure-analysis) problem where an aggregate metric is raised by exploiting the label prior.

#### Affordances {#cv-scene-reasoning-and-embodied-vision--affordance}

Not _what_ an object is, but _what can be done with it_: graspable, sittable, pourable, pushable. The representation is usually a per-pixel or per-point heat map per action class, trained from interaction data or video of humans performing the action.

> **Why affordance is not a relabelling of segmentation**
> Affordance is **agent-relative and multi-label**. The same surface is sittable for a human and not for a forklift; a mug handle is simultaneously graspable and not pourable while the rim is the reverse. A single-label semantic mask cannot express this, so the output must be a set of overlapping, agent-conditioned maps.

#### Visual navigation {#cv-scene-reasoning-and-embodied-vision--navigation}

| Task                          | Goal specified as                    | Core difficulty                                                      |
| ----------------------------- | ------------------------------------ | -------------------------------------------------------------------- |
| PointGoal                     | Coordinates $$(\Delta x, \Delta y)$$ | Mapping and obstacle avoidance; near-saturated with perfect odometry |
| ObjectGoal                    | A category ("find a toilet")         | Semantic priors about where things are                               |
| ImageGoal                     | A target photograph                  | Visual localisation and matching                                     |
| **Vision-and-Language (VLN)** | A natural-language route instruction | Grounding language to actions over a long horizon                    |

**Success weighted by Path Length**

$$ \mathrm{SPL} = \frac{1}{N}\sum\_{i=1}^{N} S_i\,\frac{\ell_i}{\max(p_i, \ell_i)} $$

- $$S_i$$ — 1 if the episode succeeded, else 0
- $$\ell_i$$ — shortest-path length
- $$p_i$$ — path taken

_Success alone rewards exhaustive search — an agent that visits every room eventually finds the toilet. SPL penalises path length, so the metric measures \_navigation_ and not _coverage_.\_

#### Active vision {#cv-scene-reasoning-and-embodied-vision--active}

The camera is no longer a passive observer: the agent chooses the next viewpoint. The natural criterion is expected information gain:

**Next-best-view selection**

$$ a^{\*} = \arg\max*{a}\ \Big[ H\big(p(\mathbf{s})\big) - \mathbb{E}*{\mathbf{z}\sim p(\mathbf{z}\mid a)}\big[H\big(p(\mathbf{s}\mid\mathbf{z},a)\big)\big] \Big] $$

_Choose the action maximising the expected \_reduction_ in entropy over the scene state $$\mathbf{s}$$. In practice this is approximated by counting unobserved or uncertain voxels visible from a candidate pose. Active perception is the clearest case where **calibrated uncertainty enters the decision**: a miscalibrated model selects the wrong next view, as well as reporting the wrong confidence.\_

#### Sensorimotor prediction and world models {#cv-scene-reasoning-and-embodied-vision--prediction}

**Latent dynamics**

$$ \mathbf{z}_{t+1} \sim p_\theta\big(\mathbf{z}_{t+1}\mid \mathbf{z}\_t, \mathbf{a}\_t\big), \qquad \hat{\mathbf{o}}_{t+1} = d*\theta(\mathbf{z}*{t+1}) $$

_Learn dynamics in a compressed latent rather than in pixels — the same [latent-space argument](#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--m4) as diffusion. Planning then happens by rolling out the latent model, which is orders of magnitude cheaper than rendering._

> **"World model" is doing a lot of work in that phrase**
> A model trained to predict future _observations_ learns what video looks like, not what physics is. [Sora](#cv-video-depth-and-concepts--sora) was explicitly framed as a step toward general-purpose physical simulation, and that framing shaped a great deal of subsequent research — but object permanence, contact and causality remain emergent, partial and inconsistent. For any task where being wrong has physical consequences, treat generated futures as _plausible samples_, not predictions.

#### Uncertainty and safety {#cv-scene-reasoning-and-embodied-vision--uncertainty}

**Decomposing predictive uncertainty**

$$ \underbrace{\operatorname{Var}\big[y\big]}_{\text{total}} = \underbrace{\mathbb{E}_{\theta}\big[\sigma^2_\theta(\mathbf{x})\big]}_{\text{aleatoric}} + \underbrace{\operatorname{Var}_{\theta}\big[\mu_\theta(\mathbf{x})\big]}\_{\text{epistemic}} $$

_**Aleatoric** uncertainty is irreducible sensor and scene noise — more data will not help. **Epistemic** uncertainty is ignorance about the model, and \_does_ shrink with data. The distinction is operational: high epistemic uncertainty means "collect more data or refuse to act"; high aleatoric means "this measurement will never be better, design around it".\_

**Heteroscedastic regression loss**

$$ \mathcal{L} = \frac{1}{2\sigma*\theta^2(\mathbf{x})}\big\lVert y - \mu*\theta(\mathbf{x})\big\rVert^2 + \frac{1}{2}\log\sigma^2\_\theta(\mathbf{x}) $$

_Predict a variance as well as a mean. The first term down-weights samples the model declares uncertain; the $$\log\sigma^2$$ term is what stops it declaring everything uncertain to avoid the first term. This is the [objective template's](#cv-vision-objectives-and-optimization--template) $$w_i$$ made learnable._

> **What changes when perception feeds control**
>
> - **Latency becomes correctness.** A perfect result that arrives after the decision point is a failure.
> - **Error asymmetry is real.** A missed obstacle and a phantom obstacle have utterly different costs, so a symmetric loss is the wrong objective.
> - **The tail is the product.** Average accuracy is nearly irrelevant; the 99.99th percentile failure is what determines whether the system can be deployed.
> - **Abstention must be an available output.** A closed-set softmax cannot say "I do not know", which is precisely the answer safety requires. See [calibration](#cv-classification-retrieval-and-recognition--calibration).
> - **Distribution shift is the norm**, not an edge case — new sites, weather, lighting, and hardware revisions.

#### Where this family stands {#cv-scene-reasoning-and-embodied-vision--state}

A distinct model category emerged in 2025–2026 targeting embodied agents specifically: mixture-of-experts vision–language models activating a few billion parameters per token, evaluated on embodied perception, physical-world understanding and navigation rather than static VQA. [Hy-Embodied-VLM-1.0](#cv-any-view-geometry-concepts-and-embodiment--embodied) ranked first on 19 of 38 such benchmarks, with strong results on R2R-CE vision-and-language navigation and zero-shot object-goal navigation.

The framing shift being claimed is from _"vision as a bolt-on adapter"_ — a pretrained LLM trunk with a vision encoder attached, the LLaVA/Qwen-VL generation — toward models whose trunk is itself a world model that predicts and acts. Whether that delivers is the open question of the current window; the [documented geometric-reasoning gap](#cv-vision-language-understanding--state) is the main reason for scepticism, since navigation and manipulation are geometric tasks.

#### Failure modes and takeaways {#cv-scene-reasoning-and-embodied-vision--takeaways}

| Failure                                  | Cause                                 | Defense                                      |
| ---------------------------------------- | ------------------------------------- | -------------------------------------------- |
| Scene-graph model ignores the image      | Predicate frequency prior suffices    | Report mean Recall@K and zero-shot triplets  |
| Navigation succeeds by exhaustive search | Success-only metric                   | SPL and path-efficiency metrics              |
| Sim-to-real collapse                     | Simulator appearance and dynamics gap | Domain randomisation; real-world fine-tuning |
| Over-confident under shift               | Calibration fitted in-domain          | Ensembles, epistemic estimates, abstention   |
| Compounding error over a long horizon    | Open-loop rollout of a learned model  | Closed-loop replanning; short horizons       |
| Generated futures treated as predictions | "World model" framing                 | Use as samples; validate against physics     |

1. **Affordance is agent-relative and multi-label** — not a relabelling of segmentation.
2. **SPL exists because success alone rewards brute-force search.**
3. **Active vision makes calibrated uncertainty operationally necessary**, not merely desirable.
4. **Aleatoric and epistemic uncertainty imply different actions.** Separate them.
5. **Video prediction learns appearance, not physics.**
6. **When perception feeds control, the tail is the product** — and abstention must be a permitted output.

## Cross-cutting

### Photometric consistency {#cv-photometric-consistency}

_One principle — **warp and compare** — supervises optical flow, stereo, direct visual odometry, self-supervised depth, multi-view stereo and neural rendering. It deserves its own treatment because it is not a formula but an ecosystem._

#### The warp-and-compare principle {#cv-photometric-consistency--principle}

Given a target image _I<sub>t</sub>_, a source image _I<sub>s</sub>_, geometry or depth _D_, camera intrinsics _K_ and relative pose _T<sub>t→s</sub>_, the source image is sampled at projected coordinates to synthesise the target:

**_Î_<sub>s→t</sub>(p) = _I<sub>s</sub>_( π( K T<sub>t→s</sub> D<sub>t</sub>(p) K<sup>−1</sup> p̃ ) )**

_Back-project pixel p to 3D using its depth, transform into the source camera's frame, project back to the image plane, and sample there. π is the projection; p̃ is p in homogeneous coordinates._

A basic masked photometric loss then compares the synthesised image against the real one:

**ℒ<sub>photo</sub> = [ Σ<sub>p</sub> M(p) ρ( _I<sub>t</sub>_(p) − _Î_<sub>s→t</sub>(p) ) ] / [ Σ<sub>p</sub> M(p) + ε ]**

_M is a validity mask; ρ is a robust penalty; ε prevents division by zero when the mask is empty. Note that the normalisation is by \_mask weight_, not pixel count — otherwise the loss rewards masking everything out.\_

> **Why this is the most reused idea in geometric vision**
> The gradient of this loss flows into _D_ and _T_ — the geometry and the pose — without any ground-truth depth or pose ever being needed. Every self-supervised depth network, every direct SLAM system and every radiance field is, at bottom, minimising a version of this residual. Cross-view methods warp one view into another using intrinsics and extrinsics, then impose pixel, gradient, structural, depth–flow, view-synthesis or forward–backward consistency on the result.

#### The robust formulation that became standard {#cv-photometric-consistency--robust}

Raw squared error on pixel differences is a poor comparison: it is dominated by illumination changes and insensitive to structural mismatch. The widely used learned formulation mixes L1 with SSIM:

**pe(_I<sub>a</sub>_, _I<sub>b</sub>_) = (α/2) ( 1 − SSIM(_I<sub>a</sub>_, _I<sub>b</sub>_) ) + (1 − α) ‖ _I<sub>a</sub>_ − _I<sub>b</sub>_ ‖<sub>1</sub>**

_Typically α = 0.85. L1 retains luminance and colour fidelity; SSIM compares \_local structure_ and is far more tolerant of smooth brightness variation. Almost always paired with edge-aware depth smoothness.\_

Unsupervised multi-view stereo commonly extends this further, combining pixel and gradient photometric terms with SSIM and depth smoothness — the gradient term adding invariance to additive brightness offsets that neither L1 nor SSIM fully removes.

#### What photometric consistency assumes {#cv-photometric-consistency--assumptions}

Six assumptions, each of which is violated routinely in real scenes. The list is the set of causes to check when a depth or flow system fails without an evident reason.

- **1 · Same physical surface** — The compared pixels observe the same point in the world. Violated at occlusion boundaries and by independently moving objects.

- **2 · Lambertian reflectance** — The surface looks the same from both viewpoints, or the appearance change is explicitly modelled. Violated by specularities, transparency and retro-reflectors.

- **3 · Comparable radiometry** — Exposure, white balance, vignetting and response curves are comparable or compensated. Violated by auto-exposure between frames — extremely common.

- **4 · Accurate geometry and calibration** — The warp is only as good as _K_, _D_ and _T_. Calibration error produces a systematic residual that the optimiser will absorb into _wrong geometry_.

- **5 · Differentiable, valid resampling** — Sampling must be differentiable and must not cross invalid boundaries. Bilinear interpolation supplies both the value and a usable gradient.

- **6 · Bad regions are handled** — Occluded, disoccluded, saturated, reflective, transparent or dynamic regions are masked or robustly down-weighted — not silently averaged in.

#### Traditional and modern tricks {#cv-photometric-consistency--tricks}

This is the ecosystem. Each entry exists because one of the six assumptions fails in a specific, predictable way.

| Trick                         | What it does                                                                                | Failure it addresses                              |
| ----------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| **Coarse-to-fine pyramids**   | Makes large displacement appear small and enlarges the optimisation basin                   | Local minima under large motion                   |
| **Inverse warping**           | Samples the source at target-defined coordinates, avoiding holes from forward splatting     | Resampling artefacts                              |
| **Bilinear interpolation**    | Yields continuous samples and useful gradients                                              | Non-differentiable sampling                       |
| **Gradient or census terms**  | Reduces sensitivity to additive brightness and local radiometric variation                  | Exposure / illumination change                    |
| **SSIM + L1 / Charbonnier**   | Compares structure as well as intensity; improves robustness over squared error             | Illumination change, outliers                     |
| **Robust M-estimators**       | Huber, Charbonnier, Tukey or Cauchy reduce the influence of outliers                        | Contaminated residual distribution                |
| **Visibility masks**          | Excludes pixels outside the image, behind surfaces, or failing consistency checks           | Occlusion, out-of-bounds warps                    |
| **Minimum reprojection**      | Takes the best source-view residual per pixel instead of averaging                          | Occlusion contamination across views              |
| **Auto-masking**              | Rejects pixels an _unwarped_ source explains as well as the geometry-based warp             | Stationary camera; objects moving with the camera |
| **Forward–backward checks**   | Rejects correspondences that do not return near their starting point                        | Mismatches, occlusion                             |
| **Exposure compensation**     | Jointly estimates affine brightness parameters, or compares normalised patches/features     | Auto-exposure, vignetting                         |
| **Edge-aware regularization** | Smooths depth or flow in homogeneous regions while preserving image-aligned discontinuities | Textureless regions; over-smoothed boundaries     |

> **Monodepth2: three tricks that changed self-supervised depth**
> One paper crystallised three of the entries above, and the combination is still the default recipe:
>
> - **Per-pixel minimum reprojection.** With several source frames, take the _minimum_ residual per pixel rather than the mean. A pixel occluded in one view is usually visible in another, and the minimum picks that view automatically — no explicit occlusion model needed.
> - **Auto-masking.** Discard pixels where the unwarped source image matches the target at least as well as the warped one. Those are exactly the pixels for which the camera-motion assumption fails: a static camera, or an object moving at the camera's velocity.
> - **Full-resolution multiscale reprojection.** Compute the loss at full resolution for every scale rather than at each scale's own resolution, which removes texture-copy artefacts and holes in low-texture regions.
>
> The pattern is worth noting: all three are _visibility and validity_ refinements — improvements to **𝒱** and **w<sub>i</sub>** in the [objective template](#cv-the-shared-pipeline-and-the-objective-template--template), not to the network or the penalty.

#### Where photometric consistency shows up in the timeline {#cv-photometric-consistency--where}

- **Optical flow** — brightness constancy is the photometric residual in its simplest form; Horn–Schunck and Lucas–Kanade differ only in the prior used to make it well-posed. [See the atlas.](#cv-optical-flow-and-scene-flow)
- **Self-supervised depth** — the reprojection loss replaces ground-truth depth entirely. This is what made monocular depth trainable at scale.
- **Direct visual odometry and SLAM** — minimise photometric residuals over pose directly, rather than reprojection residuals over matched features. [See the atlas.](#cv-camera-pose-sfm-vo-and-slam)
- **NeRF and 3D Gaussian Splatting** — the rendering loss is a photometric residual against the training views. The renderer is differentiable precisely so this gradient exists. [See the atlas.](#cv-neural-rendering-and-novel-views)
- **Multi-view stereo** — photometric consistency across views is the classical matching cost and the modern self-supervised objective alike.

> **The limitation that has not been solved**
> Photometric consistency fails on **reflection, transparency, saturation and dynamics** — and it fails _silently_, producing confident wrong geometry rather than an error. Every trick in the table above mitigates a symptom; none removes the underlying assumption that appearance is a reliable proxy for correspondence. This is the single largest reason learned geometry is not yet survey-grade.

### Losses and regularization {#cv-losses-and-regularization}

_A consolidated reference for the objective vocabulary used across every other module — organised by \_what the loss assumes_, since that is what determines when it fails.\_

#### Regression losses {#cv-losses-and-regularization--regression}

| Loss               | Form                          | Estimates              | Implied noise                  |
| ------------------ | ----------------------------- | ---------------------- | ------------------------------ |
| L2 / MSE           | $$\tfrac12 r^2$$              | Conditional **mean**   | Gaussian                       |
| L1 / MAE           | $$\lvert r\rvert$$            | Conditional **median** | Laplacian                      |
| Huber              | quadratic core, linear tails  | Robust mean            | Gaussian core, Laplacian tails |
| Charbonnier        | $$\sqrt{r^2+\epsilon^2}$$     | Smooth L1-like         | Smoothed Laplacian             |
| BerHu              | L1 small, L2 large            | Depth regression       | Emphasises large errors        |
| Quantile / pinball | $$\max(\tau r, (\tau{-}1)r)$$ | $$\tau$$-quantile      | Asymmetric costs               |

> **The single most useful fact in this module** > **L2 produces the conditional mean, L1 the conditional median.** When the target is genuinely ambiguous — the texture behind an occluder, the appearance of a super-resolved edge — the mean of all plausible answers is a blur that is _itself implausible_. That is why L2-trained restoration, VAEs and future-frame prediction are blurry, and it is not fixable by more capacity. It is a property of the objective.

#### Classification losses {#cv-losses-and-regularization--classification}

$$ \mathcal{L}_{\text{CE}} = -\sum_c y_c\log p_c, \qquad \mathcal{L}_{\text{BCE}} = -\big[y\log p + (1-y)\log(1-p)\big] $$ $$ \mathcal{L}\_{\text{focal}} = -\alpha_t(1-p_t)^{\gamma}\log p_t, \qquad y^{\text{LS}}\_c = (1-\varepsilon)y_c + \varepsilon/C $$

**Cross-entropy vs. BCE** is a modelling choice, not a preference: softmax CE assumes classes are _mutually exclusive_; per-class BCE does not, and is therefore correct for multi-label problems and for detection heads where "several things overlap here" is legitimate.

See [classification](#cv-classification-retrieval-and-recognition--ce) for label smoothing and class-balanced reweighting, and [detection](#cv-object-detection--focal) for the focal family's quality-aware successors.

#### Overlap and boundary losses {#cv-losses-and-regularization--overlap}

$$ \mathcal{L}_{\text{Dice}} = 1 - \frac{2\sum \hat{p}y + \epsilon}{\sum \hat{p}^2 + \sum y^2 + \epsilon}, \qquad \mathcal{L}_{\text{Tversky}} = 1 - \frac{TP}{TP + \alpha FP + \beta FN} $$ $$ \mathcal{L}_{\text{IoU}} = 1 - \mathrm{IoU}, \qquad \mathcal{L}_{\text{GIoU}} = 1 - \mathrm{IoU} + \frac{\lvert C\setminus(B\cup B^{gt})\rvert}{\lvert C\rvert} $$

These exist to **close the surrogate–metric gap**. Full treatments: [segmentation's four families](#cv-segmentation-and-matting--losses) and [the IoU loss family](#cv-object-detection--iou). The Lovász–Softmax is the principled member — the tight convex extension of the submodular Jaccard loss, rather than a heuristic relaxation.

#### Distributional and adversarial losses {#cv-losses-and-regularization--distributional}

| Divergence                     | Form                                                             | Behaviour                                                                     |
| ------------------------------ | ---------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Forward KL** $$D(p\Vert q)$$ | $$\int p\log\frac{p}{q}$$                                        | _Mode-covering_: $$q$$ must be non-zero wherever $$p$$ is, so it spreads mass |
| **Reverse KL** $$D(q\Vert p)$$ | $$\int q\log\frac{q}{p}$$                                        | _Mode-seeking_: $$q$$ can ignore modes of $$p$$ — the origin of mode collapse |
| **Jensen–Shannon**             | symmetric mixture of KLs                                         | Constant $$\log 2$$ on disjoint supports ⇒ **zero gradient**                  |
| **Wasserstein-1**              | $$\sup_{\lVert f\rVert_L\le1}\mathbb{E}_p[f] - \mathbb{E}_q[f]$$ | Finite and differentiable even on disjoint supports                           |

This table explains GAN instability entirely: the standard GAN minimises JS, and early in training the generated and real distributions have disjoint support, so there is no gradient. See [generation](#cv-image-generation-and-translation--gan).

**Knowledge distillation**

$$ \mathcal{L}_{\text{KD}} = (1-\lambda)\,\mathcal{L}_{\text{CE}}(y, \sigma(\mathbf{z}_s)) + \lambda\,T^2\,D_{\mathrm{KL}}\big(\sigma(\mathbf{z}\_t/T)\,\Vert\,\sigma(\mathbf{z}\_s/T)\big) $$

_The $$T^2$$ factor keeps the gradient magnitude of the soft term comparable to the hard term as $$T$$ varies (soft-target gradients scale as $$1/T^2$$). The "dark knowledge" is in the \_relative_ probabilities of the wrong classes, which is why temperature matters.\_

#### Regularizers {#cv-losses-and-regularization--regularizers}

| Regularizer             | Form                                                        | Prior asserted                            |
| ----------------------- | ----------------------------------------------------------- | ----------------------------------------- |
| Tikhonov / weight decay | $$\lVert\boldsymbol{\theta}\rVert_2^2$$                     | Small parameters; Gaussian prior          |
| Sparsity                | $$\lVert\mathbf{x}\rVert_1$$                                | Few active components                     |
| Total variation         | $$\lVert\nabla\mathbf{x}\rVert_1$$                          | Piecewise constant — _preserves edges_    |
| Laplacian smoothness    | $$\lVert\nabla\mathbf{x}\rVert_2^2$$                        | Globally smooth — _blurs edges_           |
| Edge-aware smoothness   | $$\lvert\partial d\rvert e^{-\lvert\partial I\rvert}$$      | Depth jumps coincide with image edges     |
| Low rank                | $$\lVert\mathbf{X}\rVert_*$$                                | Data lies near a low-dimensional subspace |
| Eikonal                 | $$(\lVert\nabla f\rVert-1)^2$$                              | $$f$$ is a true signed distance field     |
| Distortion (rendering)  | $$\sum w_iw_j\lvert t_i-t_j\rvert$$                         | Ray weight concentrates at one depth      |
| Path length (StyleGAN2) | $$\big(\lVert\mathbf{J}_w^\top\mathbf{y}\rVert - a\big)^2$$ | Latent→image map is smooth and invertible |

> **Reading a regularizer as a claim about the world**
> Every entry asserts something. TV asserts the scene is piecewise constant — true for cartoons and depth maps, false for gradients, which is why TV causes _staircasing_. Edge-aware smoothness asserts depth discontinuities align with intensity edges — false for a low-contrast object boundary. When a regularizer produces a characteristic artefact, that artefact _is_ the prior showing through.

#### Multi-task weighting {#cv-losses-and-regularization--multitask}

A compound objective $$\mathcal{L} = \sum_k \lambda_k\mathcal{L}_k$$ raises the question of how to set $$\lambda_k$$ when the terms have incommensurable units — pixels, radians, logits, metres.

**Uncertainty weighting (Kendall & Gal)**

$$ \mathcal{L} = \sum\_{k}\left(\frac{1}{2\sigma_k^2}\mathcal{L}\_k + \log\sigma_k\right) $$

_Learn a per-task noise scale $$\sigma_k$$ jointly with the model. The first term down-weights tasks the model finds noisy; the $$\log\sigma_k$$ term prevents the degenerate solution of sending all $$\sigma_k\to\infty$$. In practice parameterise $$s_k = \log\sigma_k^2$$ for stability. This turns a hand-tuned hyperparameter search into an optimisation._

- **GradNorm** balances the _gradient magnitudes_ of each task rather than the loss values, which is closer to the actual concern.
- **Gradient surgery (PCGrad)** projects away the component of one task's gradient that conflicts with another's — addressing the case where tasks genuinely disagree rather than merely differ in scale.

#### Uncertainty {#cv-losses-and-regularization--uncertainty}

**Aleatoric — learned observation noise**

$$ \mathcal{L} = \frac{1}{2\sigma^2*\theta(\mathbf{x})}\lVert y - \mu*\theta(\mathbf{x})\rVert^2 + \frac{1}{2}\log\sigma^2\_\theta(\mathbf{x}) $$

**Epistemic — via an ensemble**

$$ \mu*\* = \frac{1}{M}\sum*{m}\mu*m(\mathbf{x}), \qquad \sigma^2*_ = \underbrace{\frac{1}{M}\sum*m\sigma^2_m(\mathbf{x})}*{\text{aleatoric}} + \underbrace{\frac{1}{M}\sum*m\big(\mu_m(\mathbf{x}) - \mu*_\big)^2}\_{\text{epistemic}} $$

_Deep ensembles score above MC-dropout and most variational approximations as an estimator of epistemic uncertainty, at $$M\times$$ the cost. The decomposition matters operationally: see [embodied vision](#cv-scene-reasoning-and-embodied-vision--uncertainty)._

#### Training objective versus evaluation metric {#cv-losses-and-regularization--mismatch}

| Task         | Typically trained with      | Evaluated with        | Bridge                             |
| ------------ | --------------------------- | --------------------- | ---------------------------------- |
| Detection    | Smooth L1 + CE              | AP at IoU thresholds  | GIoU/DIoU/CIoU; quality focal loss |
| Segmentation | Pixel CE                    | mIoU                  | Lovász–Softmax; Dice               |
| Restoration  | L1 / L2                     | PSNR _and_ LPIPS      | Perceptual + adversarial terms     |
| Retrieval    | Triplet / ArcFace           | mAP, Recall@K         | Direct AP surrogates (Smooth-AP)   |
| Tracking     | Per-frame association costs | HOTA                  | Largely unbridged                  |
| Generation   | Denoising MSE               | FID, human preference | Largely unbridged                  |

> **The gap is a design decision, usually unexamined**
> Metrics are frequently non-differentiable, non-decomposable over samples, or defined only over a whole dataset — so a surrogate is unavoidable. But the _choice_ of surrogate encodes assumptions that should be stated. The decade's most reliable progress came from papers that closed a specific gap deliberately: focal loss for imbalance, GIoU for disjoint boxes, PQ for panoptic, Lovász for IoU. See [evaluation and failure analysis](#cv-evaluation-and-failure-analysis).

#### Takeaways {#cv-losses-and-regularization--takeaways}

1. **Every loss implies a noise model.** Choosing L2 is asserting Gaussian residuals, which real vision data almost never has.
2. **L2 gives the mean, L1 the median.** Blur under ambiguity is a property of the objective, not the network.
3. **Softmax CE asserts mutual exclusivity.** Use BCE when that is false.
4. **The minimised divergence determines the failure mode** — mode-seeking against mode-covering, gradient or no gradient.
5. **Every regularizer is a claim about the world**, and its characteristic artefact is that claim being wrong.
6. **Multi-task weights can be learned** rather than tuned, via observation noise.
7. **Name the surrogate–metric gap explicitly.** Several of the decade's results come from reducing it.

### Cross-cutting mechanisms and failure modes {#cv-cross-cutting-mechanisms-and-failure-modes}

_The techniques that appear in every task family, and the twelve ways vision systems fail. This is the fifth layer of the [five-layer treatment](#cv-the-master-task-taxonomy--scope) — the one that decides whether a method survives contact with real data._

#### Robust estimation {#cv-cross-cutting-mechanisms-and-failure-modes--robust}

Ordinary L2 assumes approximately Gaussian residuals and gives large influence to outliers. Real vision residuals are contaminated by mismatches, occlusion, moving objects, saturation, specularities and label errors — _always_, not occasionally.

| Defense                                   | Where it acts                         | What it assumes                                                    |
| ----------------------------------------- | ------------------------------------- | ------------------------------------------------------------------ |
| **RANSAC** (and MLESAC, PROSAC)           | Before nonlinear refinement           | A minimal subset of clean data exists and can be found by sampling |
| **Huber / Charbonnier / Tukey / Cauchy**  | During optimisation, as the penalty ρ | Outliers are a minority and should have bounded influence          |
| **Trimmed or top-k aggregation**          | At loss aggregation                   | A known fraction of residuals can be discarded                     |
| **Confidence weighting**                  | As w<sub>i</sub> in the objective     | Reliability is predictable per observation                         |
| **Explicit mixture / uncertainty models** | In the likelihood itself              | The contamination process can be modelled rather than resisted     |

> **The ordering matters**
> RANSAC first, then robust refinement. A robust penalty has a limited basin of attraction: it can suppress outliers once the estimate is roughly right, but it cannot rescue an initialisation that is grossly wrong, because from there the true inliers look like the outliers. This is the same reason [coarse global registration precedes ICP](#cv-point-clouds-and-3d-perception--tricks).

#### Multiscale processing {#cv-cross-cutting-mechanisms-and-failure-modes--multiscale}

Pyramids capture large motion, objects at multiple sizes, broad context, and coarse geometry before fine detail. The concept is close to universal — and worth recognising in its many costumes:

- **Classical** — Gaussian and Laplacian pyramids, wavelets, scale space, coarse-to-fine warping.

- **Convolutional** — Feature Pyramid Networks, U-Net skip connections, atrous/dilated convolution, pyramid pooling.

- **Modern** — Coarse-to-fine depth volumes, multiresolution hash grids, hierarchical transformers with patch merging.

The recurring trade is the same in all of them: coarse levels enlarge the optimisation basin and supply context, but destroy small or fast-moving structure. [RAFT's](#cv-optical-flow-and-scene-flow) refusal to use a pyramid at all — all-pairs correlation at one resolution, refined iteratively — is the clearest statement that the trade is not always worth taking.

#### Consistency constraints {#cv-cross-cutting-mechanisms-and-failure-modes--consistency}

Seven relations that let a system check itself without labels. Each is a free supervisory signal derived from redundancy, and together they are the backbone of self-supervised vision.

| Consistency          | Typical relation                                               | Used in                                |
| -------------------- | -------------------------------------------------------------- | -------------------------------------- |
| **Left–right**       | Disparity from left and right views should agree               | Stereo, self-supervised depth          |
| **Forward–backward** | Warp forward then backward should return to the start          | Flow, tracking, correspondence         |
| **Cycle**            | Mapping around a domain or view cycle should recover the input | Translation, matching, pose, tracking  |
| **Temporal**         | State or output should vary coherently over time               | Tracking, video masks, depth, pose     |
| **Geometric**        | Cross-view depth and pose should reproject consistently        | MVS, SfM, NeRF, calibration            |
| **Semantic**         | Corresponding regions retain identity or class                 | Video segmentation, domain adaptation  |
| **Teacher–student**  | Predictions should agree under perturbation                    | Semi-supervised learning, distillation |

> **Consistency is where self-supervision comes from**
> Every row is a statement that two independently computed estimates of the same quantity must agree. Disagreement is a residual; a residual is a training signal. This is the mechanism behind self-supervised depth (rows 1, 2, 5), contrastive and distillation pretraining (row 7), and unsupervised tracking (rows 2, 3, 4) — and it is why the [supervision ladder](#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--ladder) could be climbed at all.

#### Data and augmentation {#cv-cross-cutting-mechanisms-and-failure-modes--augmentation}

> **Geometry-aware augmentation must transform labels consistently**
> Boxes, masks, keypoints, depth, normals, flow, camera matrices and poses **cannot be treated like class labels**. A horizontal flip negates the x-component of flow and swaps left/right body keypoints; a crop changes the principal point; a resize changes focal length in pixels. Each of these is a silent correctness bug that produces a model that trains fine and is subtly wrong.

Photometric augmentation can improve robustness but may _violate the exact assumptions used by self-supervised photometric losses_. If correspondence is the supervision, then colour transforms must be applied identically to both views, or applied analytically so the loss can compensate. Randomly jittering the colour of one view of a stereo pair destroys the very signal being learned from.

#### Sampling and imbalance {#cv-cross-cutting-mechanisms-and-failure-modes--imbalance}

Dense visual problems contain enormous numbers of easy background pixels, anchors or pairs. Without intervention, the loss is dominated by examples that are already correct.

> **Loss-side remedies**
>
> - Focal loss — explicitly designed so easy negatives do not dominate dense one-stage detection
> - Class weighting and class-balanced reweighting
> - Top-k loss; online hard-example mining

> **Sampling-side remedies**
>
> - Balanced crops; foreground oversampling
> - Hard-negative mining
> - Stratified ray sampling (neural rendering)
> - Uncertainty-guided sampling

#### Post-processing {#cv-cross-cutting-mechanisms-and-failure-modes--postproc}

Post-processing usually embodies a **strong prior that the network was not asked to learn**. Reading the list this way explains both why these steps work and why removing them was hard:

- **NMS** enforces sparse detections — the prior that one object yields one box.
- **CRFs** align labels to image boundaries — the prior that class changes coincide with intensity edges.
- **Connected components** enforce object coherence.
- **Morphology** fills or removes structures below a scale.
- **Median filtering** rejects impulse errors.
- **Left–right checks** reject stereo occlusions.
- **Bundle adjustment** imposes global geometric agreement.

> **The decade-long arc of removing them**
> Every one of these is a hand-designed component with dataset-specific thresholds. [DETR](#cv-scale-self-supervision-and-set-prediction--detr) showed that NMS could be replaced by putting the sparsity prior _into the loss_ via bipartite matching; [YOLOv10](#cv-3d-becomes-real-time-vision-learns-to-talk--yolov10) and [YOLO26](#cv-any-view-geometry-concepts-and-embodiment--yolo26) apply the same construction at real-time latency. The pattern recurs: a post-processing step is a prior you have not yet found a way to train.

#### Failure-mode checklist {#cv-cross-cutting-mechanisms-and-failure-modes--failures}

Twelve failure sources, their symptoms and their defenses. Most debugging of a vision system consists of identifying which row applies.

| Failure source                     | Symptoms                                               | Defenses                                                                                   |
| ---------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| **Illumination / exposure change** | High photometric residual despite correct geometry     | Gradient/census/normalized correlation, affine brightness model, radiometric calibration   |
| **Specularity / transparency**     | False depth, flow or reconstruction                    | Robust masks, polarization or multiview cues, learned features, explicit reflectance model |
| **Occlusion / disocclusion**       | Ghosting, wrong correspondences, track breaks          | Visibility reasoning, z-buffering, minimum reprojection, forward–backward checks           |
| **Textureless regions**            | Ambiguous flow, stereo or depth                        | Smoothness, plane priors, semantics, active illumination, larger context                   |
| **Repeated texture**               | Wrong but visually plausible matches                   | Ratio tests, geometric verification, larger descriptors, cycle consistency                 |
| **Dynamic objects**                | Corrupted camera pose or static-scene depth            | Motion segmentation, auto-masking, object-level models, robust estimation                  |
| **Poor calibration**               | Systematic reprojection or depth bias                  | Recalibration, distortion and rolling-shutter models, joint refinement                     |
| **Scale ambiguity**                | Monocular trajectory or depth correct only up to scale | Stereo, IMU, known object size, ground plane, metric supervision                           |
| **Class imbalance**                | Background dominance, missed rare classes              | Focal or weighted losses, balanced sampling, hard mining                                   |
| **Domain shift**                   | Accuracy collapse under new camera, weather or site    | Colour and geometry augmentation, adaptation, calibration, diverse data                    |
| **Label noise**                    | Boundary blur, unstable hard examples                  | Soft labels, robust loss, relabeling, uncertainty, ignore zones                            |
| **Objective mismatch**             | Good loss but poor task metric or visual quality       | Align the surrogate with the metric; report fidelity and perception separately             |

> **Note the shape of the table**
> Rows 1–8 are violations of _image-formation assumptions_ — physics, not statistics. No amount of additional training data fixes a specularity or a scale ambiguity, because the information is genuinely absent from the measurement. Rows 9–12 are violations of _statistical assumptions_, and those _are_ addressable with data and loss design. Diagnosing which half applies determines whether the fix is a better sensor setup or a better training set.

### Evaluation and failure analysis {#cv-evaluation-and-failure-analysis}

_The module that matters most and is taught least. By 2026 the field's hardest open problems are measurement problems, not capability problems._

#### Metrics by task family {#cv-evaluation-and-failure-analysis--metrics}

| Task           | Primary metric              | What it hides                                   |
| -------------- | --------------------------- | ----------------------------------------------- |
| Classification | Top-1 / Top-5               | Class imbalance; calibration                    |
| Retrieval      | mAP, Recall@K               | Gallery size dependence                         |
| Detection      | AP@[.5:.95]                 | **Small-object performance**; crowd behaviour   |
| Segmentation   | mIoU                        | Thin structures; boundary quality; rare classes |
| Panoptic       | PQ = SQ × RQ                | Report SQ and RQ separately                     |
| Depth          | AbsRel, RMSE, $$\delta_1$$  | **Whether median scaling was applied**          |
| Flow           | EPE, Fl-all                 | Occluded vs. non-occluded; large displacement   |
| Pose           | MPJPE / PA-MPJPE, OKS-AP    | Procrustes alignment removes scale and rotation |
| Tracking       | HOTA = √(DetA·AssA)         | MOTA measures the _detector_                    |
| Reconstruction | Accuracy, completeness, F@τ | One Chamfer number hides the trade              |
| Rendering      | PSNR / SSIM / LPIPS         | Good renders ≠ good geometry                    |
| Generation     | FID, human preference       | Sample count, backbone, fidelity vs. coverage   |

> **The pattern in the right-hand column**
> Almost every entry hides the same thing: **a distribution collapsed into a mean**. The aggregate rewards performance on the common, easy majority and is nearly insensitive to the rare, hard minority, which is frequently the case of interest. The response is the same in each row: _report the breakdown_, by object size, class frequency, occlusion state, displacement magnitude or domain.

#### Dataset leakage and biased splits {#cv-evaluation-and-failure-analysis--splits}

| Leak                          | Mechanism                                                  | Correct split                                  |
| ----------------------------- | ---------------------------------------------------------- | ---------------------------------------------- |
| **Near-duplicates**           | Burst photos, re-uploads, crops of one image across splits | Perceptual-hash dedup before splitting         |
| **Same scene / session**      | Consecutive video frames in both train and test            | Split by _sequence_, never by frame            |
| **Same subject**              | One person or patient in both splits                       | Split by identity                              |
| **Same site / camera**        | Backgrounds and intrinsics memorised                       | Split by site; hold out a camera               |
| **Pretraining contamination** | Web-scale corpus contains the benchmark                    | Not measurable while the corpus is undisclosed |

> **"Zero-shot" is under-specified when the corpus is undisclosed**
> With web-scale pretraining, "zero-shot" means _unseen during fine-tuning_, not unseen. Since the pretraining corpus is typically undisclosed and unsearchable, contamination cannot be ruled out — and it grew steadily through the decade as corpora grew. Treat cross-domain transfer benchmarks ([RF100-VL](#cv-any-view-geometry-concepts-and-embodiment--rfdetr), VTAB) as more informative than any single zero-shot number.

#### Calibration {#cv-evaluation-and-failure-analysis--calibration}

$$ \mathrm{ECE} = \sum\_{b=1}^{B}\frac{\lvert B_b\rvert}{n}\Big\lvert\operatorname{acc}(B_b) - \operatorname{conf}(B_b)\Big\rvert, \qquad \mathrm{Brier} = \frac{1}{n}\sum_i \lVert \mathbf{p}\_i - \mathbf{y}\_i\rVert_2^2 $$

_Calibration is **orthogonal to accuracy** — a model can be accurate and badly calibrated, or vice versa — so it must be reported separately. [Temperature scaling](#cv-classification-retrieval-and-recognition--calibration) fixes most in-domain miscalibration with one scalar and does not change accuracy. **It does not survive distribution shift**, which is the unsolved part._

#### Domain shift and robustness {#cv-evaluation-and-failure-analysis--shift}

> **Kinds of shift**
>
> - **Covariate shift** — $$p(\mathbf{x})$$ changes, $$p(y\mid\mathbf{x})$$ does not: new camera, weather, lighting
> - **Label shift** — class frequencies change
> - **Concept shift** — $$p(y\mid\mathbf{x})$$ changes: the grading standard itself moves
> - **Open-set** — genuinely new categories appear

> **Standard robustness suites**
>
> - **ImageNet-V2** — a fresh test set, same protocol: accuracy drops even with no corruption
> - **ImageNet-C** — 15 corruptions × 5 severities; report mCE
> - **ImageNet-A** — natural adversarial examples
> - **ImageNet-R / Sketch** — rendition and abstraction shift
> - **ObjectNet** — controlled viewpoint, rotation and background

**Effective robustness**

$$ \rho = \mathrm{acc}_{\text{OOD}} - f\big(\mathrm{acc}_{\text{ID}}\big) $$

_Out-of-distribution accuracy is strongly predicted by in-distribution accuracy along a consistent line $$f$$ across a huge range of models. **Effective robustness** is the residual above that line, which separates a shift in the line from a move along it. Very few interventions produce positive $$\rho$$; [CLIP-style](#cv-the-transformer-takeover--clip) pretraining was one of the notable exceptions._

#### Label noise {#cv-evaluation-and-failure-analysis--labelnoise}

A fraction of every large dataset is mislabelled — ImageNet's validation set has a measurable error rate, and segmentation boundary labels are systematically imprecise. Consequences that matter:

- **Hard-example mining amplifies it.** The highest-loss samples are disproportionately the mislabelled ones — which is exactly why [semi-hard mining](#cv-classification-retrieval-and-recognition--mining) exists and hardest-negative mining collapses.
- **Memorisation is late.** Networks fit clean patterns first and memorise noise later, so early stopping is itself a noise-robustness method.
- **Benchmark ceilings are noise ceilings.** Once model error approaches annotator disagreement, further "improvement" is fitting one annotator's idiosyncrasies.
- **Defenses:** soft or smoothed labels, robust losses (symmetric CE, generalised CE), sample reweighting, co-teaching, and explicit ignore zones at ambiguous boundaries.

> **A metric-design idea worth copying** > [OKS](#cv-keypoints-and-pose--oks) calibrates its per-keypoint tolerance $$\kappa_i$$ from measured _inter-annotator variance_ — so it demands precision on joints humans localise consistently and forgives error on those they do not. Very few metrics do this, and most would be better if they did.

#### Ablation discipline {#cv-evaluation-and-failure-analysis--ablation}

> **The confound that recurred all decade**
> Architecture papers changed the _training recipe_ at the same time as the architecture. [ConvNeXt quantified it](#cv-foundation-models-and-the-promptable-paradigm--convnext): **+2.7 points from the recipe alone**, before any architectural change. [EfficientNet's](#cv-scale-self-supervision-and-set-prediction--efficientnet) scaling rule turned out to matter less than its NAS-found baseline.
>
> "Method + baseline + recipe" is one confounded unit unless deliberately separated. Minimum standard: hold the recipe fixed, hold the pretraining corpus fixed, report compute-matched comparisons, and report variance over seeds.

- **Report seed variance.** A 0.3-point gain within seed noise is not a gain.
- **Compute-match, and state throughput on real hardware** — FLOPs are a poor proxy, as ConvNeXt's ~49% throughput advantage over Swin at similar FLOPs shows.
- **Controlled diagnostics localise error where aggregate scores do not:** synthetic probes with a known answer, sensitivity sweeps over one nuisance factor, and counterfactual inputs (blur the object, remove the context, blank the image).
- **Test the null hypothesis.** Measure what a single frame scores on the video task, what predicate frequency alone scores on the scene graph, and what the caption prior alone scores on VQA.

#### Objective–metric mismatch {#cv-evaluation-and-failure-analysis--mismatch}

The recurring structural problem, treated at length in [losses and regularization](#cv-losses-and-regularization--mismatch). Symptoms to watch for: validation loss improving while the metric stagnates; a method scoring higher on PSNR while rated lower by observers; AP rising from better label assignment rather than better perception.

> **Where the decade's most reliable progress came from**
> Papers that closed one specific surrogate–metric gap deliberately: **focal loss** for dense imbalance, **GIoU** for disjoint boxes, **PQ** for joint stuff-and-things evaluation, **Lovász** for IoU, **HOTA** for separating detection from association. Each replaced a proxy that had quietly stopped measuring the thing of interest.

#### Safety-critical evaluation {#cv-evaluation-and-failure-analysis--safety}

- **The tail is the product.** Mean accuracy is nearly irrelevant; the 99.9th-percentile failure determines deployability.
- **Error costs are asymmetric.** A missed obstacle and a phantom obstacle have wholly different consequences, so a symmetric metric misranks methods.
- **Latency is correctness.** A right answer after the decision point is a wrong answer.
- **Abstention must be possible.** A closed-set softmax cannot say "I do not know".
- **Report runtime, memory, energy and latency** alongside accuracy — a model that cannot be deployed has no accuracy in practice.
- **Auditability.** "The model said so" is not a defensible position in a liability chain; keep the inputs, version and confidence.

#### Takeaways {#cv-evaluation-and-failure-analysis--takeaways}

1. **Aggregate metrics hide the distribution that matters.** Always report the breakdown.
2. **Split by the unit of correlation** — sequence, identity, site — never by the individual sample.
3. **Calibration is orthogonal to accuracy**, fixable in-domain, and unsolved under shift.
4. **Effective robustness** separates a shift in the accuracy line from a move along it.
5. **Hard-example mining amplifies label noise**; benchmark ceilings are annotator-disagreement ceilings.
6. **Recipe and architecture are confounded unless deliberately separated.**
7. **Capability outran evaluation.** The hardest open problems in 2026 are measurement problems.

## Key innovations

### Depth, detection and the first believable images {#cv-depth-detection-and-the-first-believable-images}

_One of the most productive periods in the field's history: deeper backbones, mature two-stage and one-stage detectors, the rise of instance segmentation, efficient mobile architectures, and rapid progress in GANs._

#### What was open, and what this era settled {#cv-depth-detection-and-the-first-believable-images--overview}

> **Open problems entering the window**
>
> - Depth degradation — deeper networks were empirically _worse_, and not because of overfitting
> - Detection was accurate _or_ fast, never both
> - Dense prediction had no canonical architecture
> - GAN training was unstable above 128×128

> **Vocabulary this era established**
>
> - Residual / identity shortcut connections
> - Region proposal networks, RoIAlign
> - Feature pyramids and lateral connections
> - Depthwise separable convolutions, inverted residuals
> - Focal loss; anchor-free keypoint detection
> - Progressive training for high-resolution synthesis

Every component introduced here is present, largely unmodified, in a 2026 production stack.

#### ResNet: the degradation problem {#cv-depth-detection-and-the-first-believable-images--resnet}

**CVPR 2016** · He, Zhang, Ren & Sun — Microsoft Research · [arXiv:1512.03385](https://arxiv.org/abs/1512.03385) · **Mechanism 1**

{% include figure.liquid loading="lazy" path="assets/img/cv/resnet_curves.png" class="img-fluid rounded z-depth-1" zoomable=true alt="Training and test error on CIFAR-10 for 20-layer and 56-layer plain networks; the deeper network has higher error on both." caption="<strong>The problem, stated as a plot.</strong> The 56-layer plain network has <em>higher training error</em> than the 20-layer one. This is not overfitting. <em>He et al., CVPR 2016.</em>" %}

The diagnosis is what makes the paper. A deeper model can always represent a shallower one by setting the extra blocks to identity, so it should never be _worse_ — yet SGD did not find that solution. The failure is in optimisation, not capacity, and batch normalization had already ruled out naive vanishing gradients.

**The residual reformulation makes the identity the default state of a block.**

{% include figure.liquid loading="lazy" path="assets/img/cv/resnet_block.png" class="img-fluid rounded z-depth-1" zoomable=true alt="A residual building block: two weight layers with an identity shortcut added to their output." caption="<strong>The residual block.</strong> The block computes the residual F(x) = H(x) − x, and its output adds the input back. <em>He et al., CVPR 2016.</em>" %}

**y = ℱ(x, {W<sub>i</sub>}) + x**

- W<sub>i</sub> → 0 gives an **exact identity** at zero cost, so adding layers can no longer hurt.
- The gradient with respect to x contains an unattenuated term flowing through the shortcut.
- **ResNet-152: 4.49% top-5 single model; 3.57% as an ensemble.** Swept ILSVRC-2015 classification, detection and localization, plus COCO detection and segmentation.

The 2016 follow-up, _Identity Mappings in Deep Residual Networks_ ([arXiv:1603.05027](https://arxiv.org/abs/1603.05027)), analysed propagation through the block and showed that pre-activation ordering (BN → ReLU → conv) makes the shortcut a genuinely _clean_ identity path — enabling a stable 1001-layer network, reported at 4.62% error on CIFAR-10.

> **Why this is the single most reused idea on the site**
> A branch initialised to the identity recurs outside depth. It is why [ControlNet's zero-initialised convolutions](#cv-foundation-models-and-the-promptable-paradigm--controlnet) can add conditioning to a frozen diffusion model without degrading it; why [DiT's adaLN-Zero](#cv-video-depth-and-concepts--dit) initialises each block as identity; and why LoRA adapters are safe to attach to a pretrained model. Same mechanism, three different decades of use.

#### The backbone zoo, 2015–2018 {#cv-depth-detection-and-the-first-believable-images--backbones}

ResNet was the pivot, but the window produced a whole family of structural ideas, most of which factorise a dense operation into a cheaper structured one and spend the savings on depth or width.

| Architecture      | Year        | Structural idea                                            | ImageNet top-1 |
| ----------------- | ----------- | ---------------------------------------------------------- | -------------- |
| Inception-v3      | 2015        | Factorised multi-branch convolutions                       | ~78%           |
| **ResNet-152**    | 2016        | Identity shortcuts                                         | ~78%           |
| ResNeXt           | 2017        | Grouped convolution; "cardinality" as a third scaling dial | ~80%           |
| DenseNet          | 2017        | Concatenative reuse of all previous feature maps           | ~77%           |
| Xception          | 2017        | 36 depthwise-separable layers replacing Inception modules  | ~79%           |
| SENet             | 2017        | Channel-wise squeeze-and-excitation recalibration          | ~82%           |
| MobileNet v1 / v2 | 2017 / 2018 | Separable convs; inverted residual with linear bottleneck  | 70.6% / 72.0%  |
| ShuffleNet v1     | 2018        | Group convolution + channel shuffle                        | ~67.6%         |

Squeeze-and-excitation factorises nothing. It rescales channels by a global statistic, and that operation continues in transformer-era block design as channel attention.

#### MobileNet: the efficiency lineage {#cv-depth-detection-and-the-first-believable-images--mobilenet}

**2017 / CVPR 2018** · Howard et al.; Sandler et al. — Google · [arXiv:1704.04861](https://arxiv.org/abs/1704.04861) · [arXiv:1801.04381](https://arxiv.org/abs/1801.04381)

{% include figure.liquid loading="lazy" path="assets/img/cv/mobilenetv2_block.png" class="img-fluid rounded z-depth-1" zoomable=true alt="Comparison of a residual block and an inverted residual block, showing the shortcut on the narrow bottleneck ends." caption="<strong>The inverted residual.</strong> Expand with 1×1, filter depthwise, project back down — with the shortcut connecting the <em>narrow</em> ends, not the wide ones. <em>Sandler et al., CVPR 2018.</em>" %}

A k×k convolution over C<sub>in</sub> → C<sub>out</sub> costs k²·C<sub>in</sub>·C<sub>out</sub> per position. Factor it into a depthwise k²·C<sub>in</sub> plus a pointwise C<sub>in</sub>·C<sub>out</sub> and the ratio becomes 1/C<sub>out</sub> + 1/k² — roughly a 8–9× reduction for k = 3.

- **V1** added a _width multiplier_ and a _resolution multiplier_, which define an accuracy/latency curve for one architecture, now the standard way to release a family of models.
- **V2** introduced the inverted residual and the **linear bottleneck**: no ReLU on the projection, because ReLU applied in a low-dimensional space destroys manifold information. ~3.4M parameters at ~72% top-1.

#### Dense prediction finds its architecture {#cv-depth-detection-and-the-first-believable-images--dense}

Classification backbones destroy spatial resolution on purpose — stride is how they buy receptive field cheaply. Every dense-prediction architecture is a different answer to _getting resolution back_.

- **FCN (2015)** — Replace the classifier's fully-connected layers with 1×1 convolutions; upsample with learned deconvolution; fuse coarse and fine strides with skips. The template for everything that follows.

- **U-Net (2015)** — Symmetric encoder–decoder with _concatenative_ skips at every resolution, trained on very few images with heavy elastic augmentation. Still the default diffusion backbone a decade later.

- **DeepLab v1–v3+ (2015–18)** — Atrous convolution enlarges the receptive field without losing resolution or adding parameters; ASPP samples several dilation rates in parallel; v3+ adds a decoder and atrous _separable_ convolutions.

#### Feature Pyramid Networks {#cv-depth-detection-and-the-first-believable-images--fpn}

**CVPR 2017** · Lin, Dollár, Girshick, He, Hariharan & Belongie · [arXiv:1612.03144](https://arxiv.org/abs/1612.03144)

{% include figure.liquid loading="lazy" path="assets/img/cv/fpn_arch.png" class="img-fluid rounded z-depth-1" zoomable=true alt="Four strategies for multi-scale features, ending with the FPN top-down pathway with lateral connections." caption="<strong>Four ways to handle scale.</strong> (a) featurised image pyramids — accurate, prohibitively slow. (b) single feature map — fast, poor on small objects. (d) FPN: reuse the backbone's own pyramid. <em>Lin et al., CVPR 2017.</em>" %}

The backbone _already computes_ a pyramid. Its levels differ in semantic level: fine levels carry localisation and little semantics, coarse levels the reverse. FPN takes the deep coarse maps, upsamples 2×, and adds them laterally to the 1×1-projected shallow maps, repeating down the pyramid. The result is strong semantics at every resolution for marginal extra cost, and it became a default neck for detection, instance segmentation and panoptic models alike.

#### Faster R-CNN and Mask R-CNN {#cv-depth-detection-and-the-first-believable-images--rcnn}

The R-CNN → Fast R-CNN → Faster R-CNN lineage is one long exercise in absorbing hand-built stages into the network. [The RPN figure and its analysis are in the task atlas.](#cv-object-detection) Faster R-CNN reached ~0.2 s/image at 73.2% mAP on VOC 07+12, and made detection end-to-end trainable for the first time.

**ICCV 2017** · He, Gkioxari, Dollár & Girshick — FAIR · [arXiv:1703.06870](https://arxiv.org/abs/1703.06870)

##### Mask R-CNN

{% include figure.liquid loading="lazy" path="assets/img/cv/maskrcnn_framework.png" class="img-fluid rounded z-depth-1" zoomable=true alt="The Mask R-CNN framework: a mask branch added in parallel to the existing box and class branches." caption="<strong>One extra branch.</strong> A small FCN mask head runs <em>in parallel</em> with the box and class heads, predicting one m×m binary mask per class. <em>He et al., ICCV 2017.</em>" %}

Two design details carry most of the gain:

- **Decoupled mask and class prediction.** Predicting one mask per class, and selecting by the classification head, avoids competition between classes in the mask output.
- **RoIAlign.** RoIPool quantises RoI boundaries to the feature grid twice over — harmless for boxes, fatal for pixel-accurate masks. RoIAlign samples at exact fractional locations with bilinear interpolation, and is worth several mask AP on its own.

Mask R-CNN swept all three COCO 2017 tracks — instance segmentation, bounding-box detection and person keypoint detection — beating the 2016 challenge winners by about 2 AP with no additional tricks, at roughly 5 fps. Its single-model result reached 47.9 box AP and 42.6 mask AP.

**Cascade R-CNN** (2018) then chained multiple detection heads at progressively increasing IoU thresholds, fixing the mismatch between the IoU used in training and the IoU demanded at evaluation, for 2–4% mAP in high-precision regimes.

#### One-stage detection: YOLO, SSD, RetinaNet {#cv-depth-detection-and-the-first-believable-images--onestage}

**CVPR 2016** · Redmon, Divvala, Girshick & Farhadi · [arXiv:1506.02640](https://arxiv.org/abs/1506.02640)

##### YOLO — detection as one regression

{% include figure.liquid loading="lazy" path="assets/img/cv/yolo_model.png" class="img-fluid rounded z-depth-1" zoomable=true alt="The YOLO model: an S×S grid where each cell predicts bounding boxes, confidences and class probabilities." caption="<strong>One forward pass, no proposals.</strong> An S×S grid; each cell predicts B boxes with confidences and C class probabilities. <em>Redmon et al., CVPR 2016.</em>" %}

- ~45 fps at 63.4% VOC mAP; a "Fast YOLO" variant reached 155 fps.
- Global context per prediction produced roughly half the background false positives of Fast R-CNN.
- **The weakness is structural:** one cell with a limited box budget localises small, clustered objects poorly.

**ECCV 2016** · Liu, Anguelov, Erhan, Szegedy, Reed, Fu & Berg · [arXiv:1512.02325](https://arxiv.org/abs/1512.02325)

##### SSD — multi-scale single-shot detection

{% include figure.liquid loading="lazy" path="assets/img/cv/ssd_arch.png" class="img-fluid rounded z-depth-1" zoomable=true alt="SSD architecture compared with YOLO, showing extra convolutional feature layers of decreasing size used for prediction." caption="<strong>Predict at every scale of the backbone.</strong> Fine maps catch small objects, coarse maps catch large ones — the insight FPN formalised a year later. <em>Liu et al., ECCV 2016.</em>" %}

SSD300 reached **74.3% mAP at 59 fps** — faster than Faster R-CNN and more accurate than YOLOv1, which is exactly the gap it was designed to close.

**ICCV 2017** · Lin, Goyal, Girshick, He & Dollár — FAIR · [arXiv:1708.02002](https://arxiv.org/abs/1708.02002)

##### Focal loss — why one-stage detectors were losing

{% include figure.liquid loading="lazy" path="assets/img/cv/focal_loss.png" class="img-fluid rounded z-depth-1" zoomable=true alt="Focal loss variants plotted against cross-entropy as a function of the probability of the ground-truth class." caption="<strong>The modulating factor.</strong> (1 − pt)γ collapses the contribution of confidently classified examples. <em>Lin et al., ICCV 2017.</em>" %}

**FL(p<sub>t</sub>) = − α<sub>t</sub> (1 − p<sub>t</sub>)<sup>γ</sup> log(p<sub>t</sub>)**

A one-stage detector scores ~10<sup>5</sup> candidate locations per image, overwhelmingly easy background. Summed over that many terms, the easy negatives account for most of the gradient although each contributes little. At γ = 2, a p<sub>t</sub> = 0.9 example contributes 100× less. RetinaNet with a ResNet-101-FPN backbone reached **39.1% COCO AP** — the first one-stage detector to match two-stage accuracy. _The architecture was never the problem; the loss was._

#### Detection scoreboard, 2015–2018 {#cv-depth-detection-and-the-first-believable-images--scoreboard}

| Model             | Year    | Paradigm               | Backbone       | Accuracy               | Speed      |
| ----------------- | ------- | ---------------------- | -------------- | ---------------------- | ---------- |
| Faster R-CNN      | 2015/16 | Two-stage              | VGG-16         | 73.2% VOC 07+12        | ~7–10 fps  |
| YOLO v1           | 2016    | One-stage              | GoogLeNet      | 66.4% VOC 07+12        | ~45–60 fps |
| SSD300/512        | 2016    | One-stage, multi-scale | VGG-16         | 74.3–76.8% VOC         | ~22–59 fps |
| YOLOv2 / YOLO9000 | 2017    | One-stage, anchors     | Darknet-19     | 76.8% VOC / 21.6% COCO | 40–67 fps  |
| RetinaNet         | 2017    | One-stage + focal loss | ResNet-101-FPN | 39.1% COCO AP          | moderate   |
| Mask R-CNN        | 2017    | Two-stage + masks      | ResNet-101-FPN | 47.9 box AP COCO       | ~5 fps     |
| YOLOv3            | 2018    | One-stage, multi-scale | Darknet-53     | 33.0% COCO AP          | real-time  |
| CornerNet         | 2018    | Anchor-free keypoints  | Hourglass-104  | 42.1% COCO AP          | slower     |

> **What every row still shares**
> Anchors (or a grid), a confidence threshold, and NMS — three hand-designed components with dataset-specific hyperparameters. **CornerNet is the first crack:** predicting paired top-left and bottom-right corner keypoints and grouping them by embedding removes anchors, but not duplicate suppression. Removing _both_ takes until [DETR in 2020](#cv-scale-self-supervision-and-set-prediction--detr), and reaching real-time while doing so takes until [2025](#cv-any-view-geometry-concepts-and-embodiment--yolo26).

#### Generative models reach photorealism {#cv-depth-detection-and-the-first-believable-images--gans}

**ICLR 2018** · Karras, Aila, Laine & Lehtinen — NVIDIA · [arXiv:1710.10196](https://arxiv.org/abs/1710.10196)

##### Progressive Growing of GANs

{% include figure.liquid loading="lazy" path="assets/img/cv/progan_growing.png" class="img-fluid rounded z-depth-1" zoomable=true alt="Progressive growing: generator and discriminator start at 4x4 and incrementally add layers doubling resolution to 1024x1024." caption="<strong>A procedural fix, not an architectural one.</strong> Start at 4×4; fade in new layer pairs that double resolution, so each stage refines an already-converged distribution. <em>Karras et al., ICLR 2018.</em>" %}

This made high-resolution training roughly an order of magnitude more stable and produced the first genuinely photorealistic 1024×1024 GAN faces, alongside the CelebA-HQ dataset built for the purpose.

**CVPR 2019 (arXiv Dec 2018)** · Karras, Laine & Aila — NVIDIA · [arXiv:1812.04948](https://arxiv.org/abs/1812.04948)

##### StyleGAN

Replaced direct latent-vector injection with an eight-layer mapping network feeding an intermediate latent space, then injected style codes at every resolution via adaptive instance normalization (AdaIN), plus per-pixel noise for stochastic detail. The mapping network's purpose is to escape the entanglement forced by sampling z from a fixed Gaussian — the intermediate space _w_ need not match any prescribed distribution. The result was a disentangled, style-mixable latent space; FID improved from ProGAN's 8.04 to **4.40** on the newly released FFHQ dataset.

**WGAN and WGAN-GP** (2017) address the same instability through the objective, in place of the architecture, replacing the standard adversarial loss with an Earth Mover's (Wasserstein) distance enforced by weight clipping or a gradient penalty — yielding more reliable dynamics and, unusually for GANs, interpretable loss curves. **BigGAN** (2018) pulled a different lever again: scaling parameter count, batch size and dataset breadth for class-conditional generation across all 1,000 ImageNet categories rather than one narrow domain.

#### Era recap {#cv-depth-detection-and-the-first-believable-images--recap}

> **Solved**
>
> - Depth — residual reformulation
> - Scale — feature pyramids, atrous convolution
> - Resolution recovery — FCN/U-Net skip connections
> - Instance masks — a parallel branch plus RoIAlign
> - Class imbalance — focal loss
> - High-resolution GAN training — progressive growing

> **Still structurally broken**
>
> - Everything requires **dense human labels**
> - Fixed, closed class vocabulary
> - Anchors, NMS and thresholds — hand-tuned per dataset
> - No representation shared across tasks
> - Geometry and recognition share no machinery

[Mechanism 1](#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--m1) is now established. The next era addresses the first item on the right, the source of the supervision.

### Scale, self-supervision and set prediction {#cv-scale-self-supervision-and-set-prediction}

_A transitional phase: efficient CNN design matured, self-supervised learning closed the gap with supervised pretraining, panoptic segmentation unified two tasks, and — most consequentially — transformers entered vision via DETR._

#### Three breakthroughs, three consolidations {#cv-scale-self-supervision-and-set-prediction--overview}

> **Independent breakthroughs**
>
> - Scaling became a _principled procedure_ — EfficientNet
> - Pretraining stopped needing labels — MoCo, SimCLR, BYOL, SwAV
> - Detection stopped needing anchors _and_ NMS — DETR

> **Consolidations**
>
> - Semantic + instance unified as _panoptic_, with the PQ metric
> - Video got a principled two-rate design — SlowFast
> - Optical flow got its own architectural reset — RAFT

The three breakthroughs are independent but they compose. DETR plus a self-supervised transformer backbone is, structurally, the 2025 detector — it took five more years only to make it fast.

#### EfficientNet: compound scaling {#cv-scale-self-supervision-and-set-prediction--efficientnet}

**ICML 2019** · Tan & Le — Google Brain · [arXiv:1905.11946](https://arxiv.org/abs/1905.11946)

{% include figure.liquid loading="lazy" path="assets/img/cv/efficientnet_scaling.png" class="img-fluid rounded z-depth-1" zoomable=true alt="Model scaling: baseline, width scaling, depth scaling, resolution scaling, and compound scaling of all three together." caption="<strong>Scale all three dimensions together.</strong> (a) baseline; (b–d) conventional single-dimension scaling; (e) compound scaling. <em>Tan & Le, ICML 2019.</em>" %}

Depth, width and input resolution are not independent: deeper networks need wider layers to exploit, and higher resolution to feed, the added capacity. The paper ties them to a single coefficient φ:

**d = α<sup>φ</sup>, w = β<sup>φ</sup>, r = γ<sup>φ</sup> subject to α · β<sup>2</sup> · γ<sup>2</sup> ≈ 2, α, β, γ ≥ 1**

_The constraint keeps FLOPs growing roughly as 2<sup>φ</sup>, because FLOPs scale linearly in depth and quadratically in both width and resolution._

- **B0**, found by NAS over an MBConv + squeeze-excite space: 5.3M parameters, 0.39B FLOPs, 77.3% top-1.
- **B7**: **84.3–84.4% top-1**, matching GPipe (557M parameters) while being 8.4× smaller and 6.1× faster at inference.
- Transferred well: 91.7% on CIFAR-100 and 98.8% on Flowers with an order of magnitude fewer parameters than comparable networks.

> **Limitations**
> Later ablations found the _NAS-discovered baseline_ contributed more than the scaling rule: applying compound scaling to a plain ResNet baseline underperforms the EfficientNet family. This is a recurring methodological trap — "method + baseline" is one confounded unit unless the two are deliberately separated, and the field would run into it again with [ConvNeXt](#cv-foundation-models-and-the-promptable-paradigm--convnext).

#### MoCo: unsupervised learning as dictionary lookup {#cv-scale-self-supervision-and-set-prediction--moco}

**CVPR 2020** · He, Fan, Wu, Xie & Girshick — FAIR · [arXiv:1911.05722](https://arxiv.org/abs/1911.05722) · **Mechanism 3**

{% include figure.liquid loading="lazy" path="assets/img/cv/moco_arch.png" class="img-fluid rounded z-depth-1" zoomable=true alt="Momentum Contrast: a query encoder and a momentum-updated key encoder, with keys stored in a queue serving as negatives." caption="<strong>A dictionary look-up formulation.</strong> Match an encoded query to its positive key among many negatives held in a queue. <em>He et al., CVPR 2020.</em>" %}

InfoNCE accuracy increases with the number of negatives. A single batch bounds that number by its own size:

**ℒ<sub>q</sub> = − log exp(q·k<sub>+</sub>/τ) / Σ<sub>i=0..K</sub> exp(q·k<sub>i</sub>/τ)**

Two ideas solve it:

- **A FIFO queue** of keys from previous batches, which decouples the negative count K from the batch size.
- **A momentum encoder**, θ<sub>k</sub> ← m·θ<sub>k</sub> + (1−m)·θ<sub>q</sub> with m ≈ 0.999. Without it the queued keys — computed at different times by a rapidly changing encoder — are mutually inconsistent and training collapses. The slow-moving key encoder is what makes an old key still comparable to a new query.
- **Shuffling BN** prevents the model from cheating through intra-batch statistics.

First unsupervised pretraining to _exceed_ supervised pretraining on several downstream detection and segmentation transfers.

#### SimCLR: ablation of the components {#cv-scale-self-supervision-and-set-prediction--simclr}

**ICML 2020** · Chen, Kornblith, Norouzi & Hinton — Google Brain · [arXiv:2002.05709](https://arxiv.org/abs/2002.05709) · **Mechanism 3**

{% include figure.liquid loading="lazy" path="assets/img/cv/simclr_arch.png" class="img-fluid rounded z-depth-1" zoomable=true alt="Heatmap of linear-evaluation accuracy under individual and composed data augmentations." caption="<strong>Composition is what matters.</strong> Linear-evaluation accuracy under individual augmentations (diagonal) versus compositions (off-diagonal). <em>Chen et al., ICML 2020.</em>" %}

No memory queue and no momentum encoder. Four components: stochastic augmentation, a base encoder, a projection head, and NT-Xent over in-batch negatives. The ablations:

- **The composition of augmentations matters, not any single one.** Random crop + colour distortion is the critical pair. Crop alone leaves a shortcut: two crops of one image share a colour histogram, so the network can solve the task without learning anything semantic.
- **A nonlinear projection head, discarded afterwards, markedly improves the representation kept beneath it.** The contrastive objective destroys information (colour, orientation) that the head can absorb, leaving the encoder free to retain it.
- Large batches and long schedules help far more than they do in supervised training.

MoCo v2 subsequently folded SimCLR's stronger augmentations and MLP projection head back into the MoCo framework, so both components transfer across the two methods.

#### Beyond negatives: BYOL, SwAV and the collapse question {#cv-scale-self-supervision-and-set-prediction--byol}

Contrastive methods were assumed to need negatives, because the constant function satisfies "two views should agree" perfectly. Two 2020 papers showed the assumption was wrong.

> **BYOL — no negatives at all**
> An online network with a _predictor_ head is trained to match a target network updated as an exponential moving average of the online weights. Collapse is avoided — empirically and robustly — by the asymmetry alone: predictor + stop-gradient + EMA target. Exactly _why_ remained contested for years, which is itself instructive about how much of this era was empirical.

> **SwAV — online clustering**
> Replace pairwise comparison with cluster assignment: predict one view's "code" from the other, with a Sinkhorn equipartition constraint preventing collapse by forcing cluster usage to stay balanced. Also introduced **multi-crop** — several additional low-resolution views — which alone is worth several points and was adopted almost universally afterwards.

BYOL's asymmetric self-distillation template — student, EMA teacher, stop-gradient — becomes [DINO](#cv-the-transformer-takeover--dino), then [DINOv2](#cv-foundation-models-and-the-promptable-paradigm--dinov2), then [DINOv3](#cv-video-depth-and-concepts--dinov3). It is the single most durable recipe in self-supervised vision.

#### Panoptic segmentation and PQ {#cv-scale-self-supervision-and-set-prediction--panoptic}

**CVPR 2019** · Kirillov, He, Girshick, Rother & Dollár — FAIR · [arXiv:1801.00868](https://arxiv.org/abs/1801.00868)

Semantic segmentation handled amorphous _stuff_; instance segmentation handled countable _things_. Separate datasets, separate models, separate metrics, and no way to compare them. Panoptic assigns every pixel a class _and_, for things, an instance id — a non-overlapping, exhaustive partition. [The task figure is in the atlas.](#cv-segmentation-and-matting)

**PQ = [ Σ<sub>(p,g)∈TP</sub> IoU(p,g) / |TP| ] × [ |TP| / ( |TP| + ½|FP| + ½|FN| ) ]**

_The first factor is **segmentation quality** (how well matched segments overlap); the second is **recognition quality** (an F₁ over segments). Matching at IoU > 0.5 is provably unique, which is what makes the metric well defined._

The companion paper, _Panoptic Feature Pyramid Networks_, adds a semantic branch to Mask R-CNN's existing FPN and reports both tasks from one network.

#### Video and motion: SlowFast and RAFT {#cv-scale-self-supervision-and-set-prediction--video}

> **SlowFast (ICCV 2019, arXiv:1812.03982)**
> Sample semantics and motion at their own rates. A **Slow** pathway at low frame rate with high channel capacity captures what is there; a **Fast** pathway at high frame rate with ~⅛ the channels captures how it moves; lateral connections fuse Fast into Slow. SOTA on Kinetics, Charades and AVA, with the deliberately thin fast pathway keeping total cost near a single 3D CNN.

> **RAFT (ECCV 2020 best paper, arXiv:2003.12039)**
> Coarse-to-fine flow pyramids lose small fast-moving objects irrecoverably. RAFT builds **all-pairs 4D correlation volumes once at a single high resolution**, then iteratively updates a flow field with a shared GRU that looks up correlation at the current estimate. One operator applied many times instead of a cascade of different ones — a large accuracy gain _and_ unusually strong cross-dataset generalisation.

Both replace a hand-designed multi-stage pipeline with a single learned operator applied repeatedly — the same structural move that diffusion samplers and DETR's decoder layers make.

#### StyleGAN2: diagnosing the artefacts in its own output {#cv-scale-self-supervision-and-set-prediction--stylegan2}

**CVPR 2020** · Karras, Laine, Aittala, Hellsten, Lehtinen & Aila — NVIDIA · [arXiv:1912.04958](https://arxiv.org/abs/1912.04958)

StyleGAN images carried characteristic **blob artefacts**. AdaIN normalises each feature map to zero mean and unit variance, which discards map magnitude. The generator creates one large localised spike beforehand; the spike sets the mean and variance of its map, so magnitude survives normalisation as a ratio to the spike. The artefact was the model routing around its own architecture.

- **Weight modulation / demodulation** replaces AdaIN — scale the convolution weights and normalise them analytically. StyleGAN normalises activations; StyleGAN2 scales the weights.
- **Drop progressive growing** (it caused phase artefacts) in favour of a skip/residual generator and discriminator.
- **Path-length regularization** penalises variation in the Jacobian norm of the latent-to-image map, smoothing it.

| Model         | FID (FFHQ) | Perceptual path length |
| ------------- | ---------- | ---------------------- |
| ProGAN        | 8.04       | —                      |
| StyleGAN      | 4.40       | 363.9                  |
| **StyleGAN2** | **2.84**   | **129.4**              |

The PPL improvement matters beyond image quality: a smoother latent map makes the generator far easier to _invert_, which enables reliable attribution of a generated image to its source model and real-image editing. **StyleGAN2-ADA** (2020) then added adaptive discriminator augmentation, reaching comparable quality with 10–100× less training data by tuning augmentation strength from an overfitting heuristic.

#### DETR: detection as direct set prediction {#cv-scale-self-supervision-and-set-prediction--detr}

**ECCV 2020** · Carion, Massa, Synnaeve, Usunier, Kirillov & Zagoruyko — FAIR · [arXiv:2005.12872](https://arxiv.org/abs/2005.12872) · **Mechanism 2**

{% include figure.liquid loading="lazy" path="assets/img/cv/detr_pipeline.png" class="img-fluid rounded z-depth-1" zoomable=true alt="DETR pipeline: CNN backbone, transformer encoder-decoder, a set of object queries each predicting one class and box, matched by bipartite matching." caption="<strong>No anchors, no NMS, no hand-designed post-processing.</strong> A CNN backbone feeds a transformer encoder–decoder; N learned object queries each emit one (class, box) in parallel. <em>Carion et al., ECCV 2020.</em>" %}

**The loss is the contribution, not the architecture.** Pad the ground truth to size N with ∅ and find the permutation that minimises total matching cost:

**σ̂ = arg min<sub>σ∈𝔖<sub>N</sub></sub> Σ<sub>i=1..N</sub> ℒ<sub>match</sub>( y<sub>i</sub>, ŷ<sub>σ(i)</sub> )**

_Solved by the Hungarian algorithm. The box cost mixes ℓ₁ with generalised IoU so it is scale-invariant; unmatched slots are trained toward "no object"._

Because the assignment is a **bijection**, two queries cannot both claim one object. Duplicate suppression is _trained into the loss_, so the NMS stage is removed. Auxiliary decoding losses at every decoder layer are required for it to converge at all.

> **Results**
>
> - DETR-R50: **42.0 COCO AP**, matching Faster R-CNN
> - 86 GFLOPs versus 180 — less than half
> - Higher AP on _large_ objects, from global attention

> **Costs**
>
> - Lower AP on small objects
> - **500 epochs** to converge
> - Both follow from dense attention on one low-resolution feature map

**ICLR 2021** · Zhu, Su, Lu, Li, Wang & Dai · [arXiv:2010.04159](https://arxiv.org/abs/2010.04159)

##### Deformable DETR — sparsity fixes both problems

{% include figure.liquid loading="lazy" path="assets/img/cv/deformdetr_attn.png" class="img-fluid rounded z-depth-1" zoomable=true alt="Deformable attention module: a query attends to a small set of learned sampling offsets around a reference point." caption="<strong>Attend to K learned offsets, not everything.</strong> Cost becomes linear in feature-map size, making multi-scale features affordable. <em>Zhu et al., ICLR 2021.</em>" %}

At initialisation, dense global attention is nearly uniform over all spatial locations; learning to be selective is what consumes hundreds of epochs. Uniform attention also cannot afford high-resolution feature maps — which is exactly why small objects suffered. Deformable attention samples only K learned offsets around a reference point per query per level, giving **46.2 AP with 10× fewer training epochs** and closing the small-object gap. The follow-up line (Conditional DETR, DAB-DETR, DN-DETR, DINO) attacks query semantics and denoising, and leads directly to [RF-DETR in 2025](#cv-any-view-geometry-concepts-and-embodiment--rfdetr).

#### Era recap {#cv-scale-self-supervision-and-set-prediction--recap}

| Method          | Year | Mechanism                                  | Headline                                          |
| --------------- | ---- | ------------------------------------------ | ------------------------------------------------- |
| EfficientNet-B7 | 2019 | Compound depth/width/resolution scaling    | 84.3% top-1, 8.4× smaller than GPipe              |
| MoCo            | 2019 | Queue of negatives + momentum encoder      | Unsup. pretraining exceeds supervised on transfer |
| SimCLR          | 2020 | Augmentation composition + projection head | Established the contrastive recipe                |
| BYOL / SwAV     | 2020 | Asymmetric EMA target / online clustering  | Collapse avoided without negatives                |
| Panoptic FPN    | 2019 | Semantic branch on Mask R-CNN's FPN        | One network, one metric (PQ)                      |
| SlowFast        | 2019 | Two pathways at two temporal rates         | SOTA on Kinetics / Charades / AVA                 |
| RAFT            | 2020 | All-pairs correlation + recurrent updates  | Accuracy plus cross-dataset generalisation        |
| StyleGAN2       | 2020 | Weight demodulation, path-length reg.      | FID 4.40 → 2.84 on FFHQ                           |
| DETR            | 2020 | Set prediction + Hungarian matching        | 42.0 AP, no anchors or NMS                        |
| Deformable DETR | 2020 | Sparse deformable attention                | 46.2 AP, 10× faster convergence                   |

> **The quiet turning point**
> DETR placed a transformer within a vision system. The next era applies the transformer to the backbone as well.

### The transformer takeover {#cv-the-transformer-takeover}

_The period in which transformers were applied across vision tasks. It opens with DETR applying one to detection, continues with ViT exceeding CNN accuracy on classification above a data threshold, and closes with diffusion reporting lower FID than GANs._

#### Two shifts at once {#cv-the-transformer-takeover--overview}

> **Architecture**
>
> - ViT — plain transformers exceed CNN accuracy above a data threshold
> - DeiT — and below it too, with the right recipe
> - Swin / PVT / SegFormer — hierarchy restored for dense prediction

> **Supervision and generation**
>
> - CLIP — language becomes an open label space
> - DINO / BEiT / MAE — self-supervised ViTs
> - DDPM → guidance → latent diffusion — GANs displaced

Every component of a 2026 system is present in prototype form by the end of this window.

#### ViT: an image is a sequence of patches {#cv-the-transformer-takeover--vit}

**ICLR 2021** · Dosovitskiy et al. — Google Research / Brain · [arXiv:2010.11929](https://arxiv.org/abs/2010.11929)

{% include figure.liquid loading="lazy" path="assets/img/cv/vit_arch.png" class="img-fluid rounded z-depth-1" zoomable=true alt="Vision Transformer: image split into patches, linearly embedded, position embeddings added, fed to a standard transformer encoder." caption="<strong>A standard, unmodified transformer encoder.</strong> Split into 16×16 patches, flatten, linearly project, prepend a [CLS] token, add learned 1D positional embeddings. No convolutions, no pyramid, no vision-specific inductive bias. <em>Dosovitskiy et al., ICLR 2021.</em>" %}

{% include figure.liquid loading="lazy" path="assets/img/cv/vit_scaling.png" class="img-fluid rounded z-depth-1" zoomable=true alt="Transfer accuracy versus pretraining dataset size, showing ViT below ResNets on small datasets and above them on large ones." caption="<strong>The data-scale crossover.</strong> ViT variants underperform BiT ResNets (shaded) when pretrained on small datasets, and overtake them on large ones. <em>Dosovitskiy et al., ICLR 2021.</em>" %}

ViT-L/16 top-1 on ImageNet, by pretraining corpus:

- ImageNet-1k only: **76.5%** — _worse than a comparable ResNet_
- ImageNet-21k: **85.3%**
- JFT-300M: **87.8%** — above the highest CNN result at matched parameters and FLOPs

> **What the crossover measures**
> Locality and translation equivariance are a _prior_. Priors substitute for data — and therefore _cost_ accuracy once data is abundant, because they constrain the hypothesis space in ways the data no longer requires. The crossover sits somewhere around 10<sup>8</sup> images. **This single result reoriented the field's research agenda from architecture design to pretraining scale.**

**DeiT** (ICML 2021) then reached competitive ImageNet-1k-only accuracy using strong augmentation, heavy regularisation and a distillation token — so part of the threshold is attributable to the training recipe. This is the same confound that [ConvNeXt](#cv-foundation-models-and-the-promptable-paradigm--convnext) would quantify a year later.

#### Swin Transformer: hierarchy and linear cost {#cv-the-transformer-takeover--swin}

**ICCV 2021** · Liu et al. — Microsoft Research Asia · [arXiv:2103.14030](https://arxiv.org/abs/2103.14030)

{% include figure.liquid loading="lazy" path="assets/img/cv/swin_windows.png" class="img-fluid rounded z-depth-1" zoomable=true alt="Shifted window partitioning: regular windows in layer l, shifted windows in layer l+1, allowing cross-window connections." caption="<strong>Shifted windows.</strong> Alternate the window partition between consecutive blocks so information crosses window boundaries at no extra FLOPs. <em>Liu et al., ICCV 2021.</em>" %}

ViT is unusable for dense prediction: attention is O(N²) in the number of patches, and the resolution never changes. Swin fixes both:

- **Windowed attention** restricts self-attention to non-overlapping M×M windows (M = 7), making cost _linear_ in image size.
- **Shifted windows** alternate the partition by ⌊M/2⌋ between consecutive blocks, with a cyclic shift plus masking to keep batches regular.
- **Patch merging** concatenates each 2×2 token neighbourhood between stages: resolution halves, channels double — a feature pyramid built from transformer blocks, directly compatible with FPN-style heads.

**87.3% ImageNet-1K top-1, 58.7 COCO box AP, 53.5 ADE20K mIoU** — above the prior reported results on all three. Shifted windows and hierarchical merging were adopted across dense-prediction backbones afterwards.

##### The hierarchical-transformer wave {#cv-the-transformer-takeover--hier-wave}

- **PVT (2021)** — Progressive shrinking across four stages with _spatial-reduction attention_, downsampling keys and values to make attention affordable at high resolution.

- **SegFormer (2021)** — Hierarchical Mix Transformer encoder plus an **all-MLP decoder**. Drops positional encodings entirely — using a 3×3 depthwise conv in the FFN instead — so it generalises across test resolutions without interpolation.

- **Twins, CSWin, MViT** — Variations on the same axis: which tokens attend to which, and how to restore a pyramid. MViT adds pooling attention for video.

> **The convergence worth noting**
> Every successful "transformer for dense prediction" re-imports the two properties ViT discarded: **locality** (windows, pooling, spatial reduction) and **multi-scale hierarchy** (patch merging, staged shrinking). In these designs the inductive bias sits in the attention pattern and the stage layout, where it can be changed without changing the operator.

#### CLIP: language as the label space {#cv-the-transformer-takeover--clip}

**ICML 2021** · Radford et al. — OpenAI · [arXiv:2103.00020](https://arxiv.org/abs/2103.00020)

{% include figure.liquid loading="lazy" path="assets/img/cv/clip_arch.png" class="img-fluid rounded z-depth-1" zoomable=true alt="CLIP: contrastive pretraining matching images to captions in a batch, then zero-shot classification by embedding class-name prompts." caption="<strong>Contrastive pretraining, then a synthesised classifier.</strong> Within a batch of N pairs, identify the N correct pairings among N² candidates; at test time the text tower embeds class names to build a classifier on the fly. <em>Radford et al., ICML 2021.</em>" %}

Trained on **400 million image–text pairs** scraped from the web with a symmetric InfoNCE objective over a learned temperature. At test time the text encoder _synthesises_ a linear classifier: embed "a photo of a {class}" for an arbitrary class list and classify by nearest embedding. **The class list is supplied at inference as text.** Ensembling over several prompt templates raises ImageNet accuracy by close to 5 points, at no additional training cost.

CLIP was a simplified, massively scaled re-derivation of the earlier ConVIRT approach — the predecessor mattered far less than the scale.

> **What it became**
>
> - The text-conditioning mechanism for DALL·E 2 and Stable Diffusion
> - The vision tower of most early multimodal LLMs
> - The basis of open-vocabulary detection and segmentation
> - A robustness result in its own right — much flatter degradation across ImageNet-V2/R/Sketch than supervised models at equal ImageNet accuracy

> **Documented weaknesses**
>
> - Poor at **counting**, spatial relations and compositional binding — web captions rarely depend on them
> - Weak on fine-grained and specialist domains; zero-shot is not free expertise
> - The softmax contrastive loss needs very large batches. **SigLIP** (2023) replaces it with a pairwise _sigmoid_ loss — no global normalisation, so it trains well at modest batch size and scales better

#### Self-supervised ViTs: DINO, BEiT, MAE {#cv-the-transformer-takeover--ssl-vit}

Three routes to the same goal, with a durable division of labour between them.

- <a id="cv-the-transformer-takeover--dino"></a>**DINO (ICCV 2021)** — BYOL-style self-distillation with a ViT: the student matches an EMA teacher's sharpened output distribution, with centring to prevent collapse, over multi-crop views.<br><br>**The surprise:** the [CLS] token's attention maps contain clean _unsupervised object segmentations_, and k-NN on the features alone is strong. Emergent structure nobody trained for.

- **BEiT (ICLR 2022)** — BERT for images: tokenise the image with a discrete VAE, mask patches, and predict the _visual token ids_ rather than pixels. Establishes masked image modelling but inherits a dependency on a separately trained tokeniser.

- **MAE (CVPR 2022)** — Drops the tokeniser: predict _raw pixels_ of masked patches, with a very high mask ratio and an asymmetric encoder–decoder. Simpler, faster and better — and the asymmetry is what makes it scale.

The division that persists: contrastive and distillation methods give strong **linear-probe** features; masked modelling gives features that **fine-tune** better. [DINOv2](#cv-foundation-models-and-the-promptable-paradigm--dinov2) later combines both objectives precisely for this reason.

<a id="cv-the-transformer-takeover--mae"></a>

**CVPR 2022** · He, Chen, Xie, Li, Dollár & Girshick — FAIR · [arXiv:2111.06377](https://arxiv.org/abs/2111.06377) · **Mechanism 3**

##### MAE: asymmetry is the mechanism

{% include figure.liquid loading="lazy" path="assets/img/cv/mae_arch.png" class="img-fluid rounded z-depth-1" zoomable=true alt="MAE architecture: encoder processes only visible patches; a lightweight decoder reconstructs the full image from latents plus mask tokens." caption="<strong>The encoder never sees a mask token.</strong> It operates on the visible 25% only; a lightweight decoder handles reconstruction and is discarded after pretraining. <em>He et al., CVPR 2022.</em>" %}

- Masking **75%** of patches, with an ℓ₂ loss on normalised patch targets.
- The encoder cost drops ~4×, giving **>3× faster wall-clock training**.
- The high ratio is essential: at low ratios the task is solvable by local interpolation and teaches nothing semantic.
- ViT-Huge reached **87.8% on ImageNet-1K using only ImageNet-1K data** — no web-scale corpus, no paired text. A direct counterpoint to CLIP's premise.

#### Diffusion, in three steps {#cv-the-transformer-takeover--diffusion}

> **DDPM (2020)**
> Fix a forward noising process and learn to reverse it. Reparameterise to predict the noise:<br>`ℒ = 𝔼[ ‖ε − ε<sub>θ</sub>(x<sub>t</sub>, t)‖² ]`<br>A stable regression objective — **no discriminator, no mode collapse**. The cost is hundreds of sequential steps.

> **Guidance (2021–22)**
> Classifier guidance steers sampling with an external classifier's gradient. **Classifier-free guidance** removes the classifier: jointly train conditional and unconditional models via random condition dropout, then extrapolate<br>`ε̃ = ε<sub>∅</sub> + s(ε<sub>c</sub> − ε<sub>∅</sub>)`<br>One scalar trading diversity for fidelity. Universally adopted.

> **Beating GANs (2021)**
> "Diffusion Models Beat GANs" established diffusion as SOTA on ImageNet synthesis. The remaining cost is hundreds of U-Net evaluations at full pixel resolution. Latent diffusion addresses that cost.

Adversarial training is replaced by a regression loss on the added noise, which has a single global optimum. The GAN stability literature — WGAN, gradient penalties, progressive growing, path-length regularization — was not carried further.

#### Latent Diffusion: move the work to a small space {#cv-the-transformer-takeover--ldm}

**CVPR 2022** · Rombach, Blattmann, Lorenz, Esser & Ommer — released as Stable Diffusion · [arXiv:2112.10752](https://arxiv.org/abs/2112.10752) · **Mechanism 4**

{% include figure.liquid loading="lazy" path="assets/img/cv/ldm_arch.png" class="img-fluid rounded z-depth-1" zoomable=true alt="Latent diffusion architecture: a VAE encoder compresses to a latent, diffusion runs there with cross-attention conditioning, a decoder reconstructs." caption="<strong>Compress once, denoise many times.</strong> A pretrained autoencoder compresses to a ~64×64 latent; the whole diffusion process runs there; cross-attention injects text, layout, depth or semantic conditioning. <em>Rombach et al., CVPR 2022.</em>" %}

Most bits in an image are perceptually irrelevant detail. Spend diffusion capacity only on the semantic part:

- **Stage 1** — a VQ- or KL-regularised autoencoder compresses by f = 4–8, trained once with a perceptual plus patch-adversarial loss.
- **Stage 2** — diffusion at ~64×64 instead of 512×512, roughly a **48× smaller tensor to denoise**.
- **Cross-attention** layers in the U-Net inject conditioning of any modality.

Released publicly in August 2022 under an open licence, it was the first capable text-to-image model with open weights that ran on consumer GPU hardware and could be freely fine-tuned — widely regarded as the accessibility inflection point for the whole field.

##### Text-to-image, 2021–2022 {#cv-the-transformer-takeover--t2i-timeline}

| Model                | Release  | Architecture                          | Resolution | Key innovation                                                                  |
| -------------------- | -------- | ------------------------------------- | ---------- | ------------------------------------------------------------------------------- |
| DALL·E               | Jan 2021 | Autoregressive (GPT-3 + dVAE)         | 256×256    | First text-to-image proof of concept; image and text tokens as one sequence     |
| DALL·E 2 (unCLIP)    | Apr 2022 | Diffusion + CLIP embeddings           | 1024×1024  | Diffusion decoder conditioned on CLIP image embeddings produced from text       |
| Imagen               | May 2022 | Cascaded diffusion + LLM text encoder | 1024×1024  | Large language-model text embeddings drive a cascaded super-resolution pipeline |
| Parti                | Jun 2022 | Autoregressive (non-diffusion)        | —          | An alternative autoregressive route, kept alive as a counterfactual             |
| **Stable Diffusion** | Aug 2022 | Latent diffusion + CLIP conditioning  | 512×512    | First capable open-weight model runnable on consumer hardware                   |

DALL·E was a 12-billion-parameter GPT-3 variant: text to BPE tokens, autoregressive generation of 1,024 image tokens, decoding through a discrete VAE, then re-ranking candidates with CLIP. DALL·E 2 moved to diffusion and reported more photorealistic results with _fewer_ parameters (3.5B), so the gain is attributable to the change of model class at reduced scale.

#### Era recap {#cv-the-transformer-takeover--recap}

| Method                 | Year    | Mechanism                                 | Headline                                             |
| ---------------------- | ------- | ----------------------------------------- | ---------------------------------------------------- |
| ViT                    | 2020/21 | Patch tokens + plain transformer encoder  | 87.8% top-1 with JFT-300M pretraining                |
| DeiT                   | 2021    | Distillation token + strong augmentation  | Competitive with ImageNet-1k only                    |
| CLIP                   | 2021    | Contrastive image–text on 400M pairs      | Zero-shot transfer; robustness to distribution shift |
| Swin / PVT / SegFormer | 2021    | Windowed or reduced attention + hierarchy | Dense prediction becomes affordable                  |
| DINO                   | 2021    | Self-distillation with a ViT              | Emergent unsupervised segmentation                   |
| BEiT / MAE             | 2021    | Masked image modelling                    | 87.8% IN-1K using IN-1K only (MAE)                   |
| DDPM + CFG             | 2020–22 | Denoising regression + guidance scale     | Diffusion overtakes GANs                             |
| Latent Diffusion       | 2022    | Diffusion in a compressed latent          | Consumer-hardware text-to-image                      |

> **The shared shape**
> Every row decouples an _expensive_ stage from a _cheap_ one and scales only the expensive stage once: pretrain once and use many times; compress once and denoise many times. That is the foundation-model thesis, and the next era is its consequence.

### Foundation models and the promptable paradigm {#cv-foundation-models-and-the-promptable-paradigm}

_The CNN mounts a genuine counterattack, segmentation unifies around universal mask prediction, self-supervision reaches production-grade backbones, and the "promptable" paradigm from language models arrives fully in vision._

#### Consolidation, then a new interface {#cv-foundation-models-and-the-promptable-paradigm--overview}

> **Consolidation**
>
> - ConvNeXt (and V2) — it was the recipe, not the operator
> - Mask2Former — one architecture for all three segmentation tasks
> - DINOv2 — frozen features that no longer need fine-tuning

> **The interface opens**
>
> - SAM — promptable, zero-shot segmentation at scale
> - Grounding DINO / OWL-ViT — open-vocabulary detection
> - ControlNet — structural conditioning without retraining

The defining shift: models stop being trained _for_ a task and start being _queried_ for one.

#### ConvNeXt: a controlled experiment {#cv-foundation-models-and-the-promptable-paradigm--convnext}

**CVPR 2022** · Liu, Mao, Wu, Feichtenhofer, Darrell & Xie — FAIR / UC Berkeley · [arXiv:2201.03545](https://arxiv.org/abs/2201.03545)

{% include figure.liquid loading="lazy" path="assets/img/cv/convnext_roadmap.png" class="img-fluid rounded z-depth-1" zoomable=true alt="The ConvNeXt modernization roadmap: incremental design changes from ResNet-50 to ConvNeXt with accuracy after each step." caption="<strong>Every step benchmarked individually.</strong> Start from ResNet-50, import Swin's choices one at a time, stay purely convolutional. <em>Liu et al., CVPR 2022.</em>" %}

Not an architecture paper — an _ablation_ paper, and a direct response to the moment when vision transformers seemed poised to replace convolutional networks entirely. The modernisation proceeded through five stages:

- **Training recipe alone** (AdamW, 300 epochs, RandAugment, Mixup, stochastic depth): **76.1 → 78.8%**, before any architectural change at all.
- **Macro design:** stage compute ratio 3:3:9:3; a "patchify" 4×4 stride-4 stem, mirroring Swin.
- **ResNeXt-style** grouped/depthwise convolution with an inverted bottleneck.
- **Larger kernels**, up to 7×7.
- **Micro design:** GELU for ReLU, fewer activation and normalization layers, LayerNorm for BatchNorm, separate spatial downsampling layers.

Result: **82.0% versus Swin-T's 81.3%**, with roughly 49% higher GPU throughput because convolutions map better to hardware. Scaled up, the family reached 87.8% top-1, scored above comparable Swin models on COCO and ADE20K, and degraded less on ImageNet-A/R/Sketch.

> **The uncomfortable first bullet**
> A 2.7-point gain from the training recipe alone, before touching the architecture. Part of the "architecture progress" reported between 2019 and 2021 is _recipe progress_ reported as architecture progress — a confound the field had already met with [EfficientNet](#cv-scale-self-supervision-and-set-prediction--efficientnet) and would keep meeting. The conclusion ConvNeXt actually supports is that the CNN/transformer gap was training recipe and micro-design, not self-attention.

#### ConvNeXt V2: giving ConvNets masked pretraining {#cv-foundation-models-and-the-promptable-paradigm--convnextv2}

**CVPR 2023** · Woo, Debnath, Hu, Chen, Liu, Kweon & Xie · [arXiv:2301.00808](https://arxiv.org/abs/2301.00808)

ConvNeXt V1 could not benefit from MAE-style pretraining, for two structural reasons:

- **Dense convolution has no notion of a missing token.** A masked region is a hole across which the convolution interpolates, so the pretext task is solvable without learning the content. Treat the masked image as _sparse_ and use sparse convolutions during pretraining, collapsing back to dense at fine-tuning time.
- **Feature collapse.** Under masked training, many channels become redundant. The fix: **Global Response Normalization** — normalise each channel by the aggregate response across channels, explicitly rewarding feature diversity.

> **The general point**
> A self-supervised objective is specified together with an architecture. Masked modelling was defined on the transformer's token structure; applying it to a convolutional operator required a sparse formulation of the masking and an additional normalisation layer. The same lesson recurs whenever a pretraining recipe is moved across architectures — and it is why "just use MAE" is rarely a complete answer.

#### Mask2Former: all segmentation is mask classification {#cv-foundation-models-and-the-promptable-paradigm--mask2former}

**CVPR 2022** · Cheng, Misra, Schwing, Kirillov & Girdhar — FAIR / UIUC · [arXiv:2112.01527](https://arxiv.org/abs/2112.01527) · **Mechanism 2**

{% include figure.liquid loading="lazy" path="assets/img/cv/mask2former_arch.png" class="img-fluid rounded z-depth-1" zoomable=true alt="Mask2Former architecture: backbone, pixel decoder and a transformer decoder with masked attention producing mask queries." caption="<strong>Set prediction generalised from boxes to masks.</strong> ~100 learnable queries, each emitting one binary mask and one class label including &quot;no object&quot;. <em>Cheng et al., CVPR 2022.</em>" %}

**One model, three tasks — the same output read differently:**

- Merge same-class masks → **semantic** segmentation
- Keep "thing" masks separate → **instance** segmentation
- Take the highest-scoring non-overlapping subset → **panoptic** segmentation

Its key technical innovation, **masked attention**, constrains each query's cross-attention to its own predicted mask region from the previous layer, in place of attending over the whole image, which localises the features and shortens the schedule. Two further efficiency choices matter in practice: high-resolution features fed round-robin to successive decoder layers, and the loss computed on _sampled points_ rather than whole masks, which is a large memory saving.

New state of the art on four benchmarks at once: **57.8 PQ** panoptic and **50.1 AP** instance on COCO, and **57.7 mIoU** semantic on ADE20K — above the specialised architectures including Mask R-CNN and DeepLab-based models, from a single model, and reducing the per-task research and engineering effort by at least threefold.

A contemporaneous counterpoint: **SegFormer** kept the traditional per-pixel grid-labelling output but rebuilt the encoder as a hierarchical Mix Transformer with a lightweight MLP decoder, becoming the go-to choice for fast, accurate _plain_ semantic segmentation. Two complementary answers to the same reframing — "predict a set of masks" versus "label every pixel, but better".

#### Open-vocabulary detection {#cv-foundation-models-and-the-promptable-paradigm--openvocab}

> **OWL-ViT (2022)**
> A minimal recipe: take a CLIP ViT, remove pooling, attach a lightweight box head and a classification head that compares each token's embedding against _text_ embeddings, then fine-tune on detection data. Detection becomes a matching problem against an open label set, and it supports _image-conditioned_ queries too.

> **Grounding DINO (2023)**
> Fuse language into a DINO-style detector at **three** points — neck, query initialisation and head — in place of the output alone. Trained jointly on detection, grounding and caption data. Zero-shot COCO transfer is reported, and the text input accepts referring expressions as well as class names.

**Grounding DINO + SAM** became the standard open-vocabulary _segmentation_ pipeline purely by composition — one model names and localises, the other produces the mask. That compositionality is a direct consequence of SAM's decision not to classify, below.

Detection inherits CLIP's open vocabulary — and [CLIP's compositional weaknesses](#cv-the-transformer-takeover--clip) along with it.

#### DINOv2: features good enough to freeze {#cv-foundation-models-and-the-promptable-paradigm--dinov2}

**TMLR 2024 (released April 2023)** · Oquab et al. — Meta AI / FAIR · [arXiv:2304.07193](https://arxiv.org/abs/2304.07193) · **Mechanism 3**

{% include figure.liquid loading="lazy" path="assets/img/cv/dinov2_dense.jpg" class="img-fluid rounded z-depth-1" zoomable=true alt="PCA visualisations of DINOv2 patch features showing coherent part-level correspondence across different images of similar objects." caption="<strong>Dense features that transfer without fine-tuning.</strong> PCA of patch features shows coherent part-level structure across different instances. <em>Oquab et al., TMLR 2024.</em>" %}

Combines DINO's image-level self-distillation with iBOT's patch-level masked prediction, then scales carefully:

- **Curated data (LVD-142M)**, assembled by retrieval-based deduplication and balancing from a large uncurated pool. The paper's argument is that _curation, not raw volume_, is what makes self-supervised learning scale.
- A model family from ViT-S (21M) to ViT-g (1.1B), with the largest distilled down into the smaller ones.
- Infrastructure at scale: fully sharded training, FlashAttention, batch sizes around 65,000.

**The result that matters:** the features work _frozen_. A linear probe gives competitive classification, segmentation, depth estimation and retrieval with no task-specific fine-tuning. It was the first self-supervised method to match or surpass weakly-supervised (CLIP-style) approaches broadly — and it uniquely learned dense properties like depth that classification supervision never produces.

#### Segment Anything {#cv-foundation-models-and-the-promptable-paradigm--sam}

**ICCV 2023** · Kirillov et al. — Meta AI / FAIR · [arXiv:2304.02643](https://arxiv.org/abs/2304.02643) · **Mechanism 5**

{% include figure.liquid loading="lazy" path="assets/img/cv/sam_overview.png" class="img-fluid rounded z-depth-1" zoomable=true alt="SAM overview: a heavyweight image encoder produces an embedding queried by a lightweight prompt encoder and mask decoder." caption="<strong>Encode once, prompt many times.</strong> A heavyweight image encoder outputs an embedding that a lightweight prompt encoder and mask decoder query at amortised cost. <em>Kirillov et al., ICCV 2023.</em>" %}

Give it an image plus a prompt — a foreground point, a bounding box, or a rough mask — and it returns a valid segmentation mask, **including for objects and image distributions never seen during training**. For an ambiguous prompt the decoder emits _three_ nested masks with confidence scores, in place of averaging them into mush.

##### Three design decisions worth copying {#cv-foundation-models-and-the-promptable-paradigm--sam-decisions}

1. **Asymmetric cost.** The ViT-H encoder runs once per image (~0.15 s); the prompt encoder and mask decoder run in ~50 ms, in a browser. This is what makes interactive use — and the annotation loop below — possible at all.
2. **A data engine, not a dataset.** Three stages: assisted-manual, then semi-automatic (the model proposes, humans add what it missed), then fully automatic over a 32×32 point grid. Yielded **SA-1B**: over 1.1 billion masks across 11 million licensed, privacy-respecting images — orders of magnitude beyond any prior segmentation dataset.
3. **It refuses to classify.** SAM produces high-quality masks and leaves object naming to a downstream classifier, detector or language model. That deliberate incompleteness is exactly what makes it composable into other people's pipelines.

> **The generalisable pattern is the data engine**
> It is a _bootstrapping_ argument: a mediocre model plus human correction produces data that trains a better model, which then needs less correction. The same structure reappears in [SAM 2's](#cv-3d-becomes-real-time-vision-learns-to-talk--sam2) video engine, [SAM 3's](#cv-video-depth-and-concepts--sam3) concept engine, and [Depth Anything's](#cv-video-depth-and-concepts--depthanything2) pseudo-labelling. **This is how the field routed around the annotation bottleneck without ever solving it.**

#### ControlNet: mechanism 1, fifteen years later {#cv-foundation-models-and-the-promptable-paradigm--controlnet}

**ICCV 2023** · Zhang, Rao & Agrawala — Stanford · [arXiv:2302.05543](https://arxiv.org/abs/2302.05543) · **Mechanism 1**

{% include figure.liquid loading="lazy" path="assets/img/cv/controlnet_block.png" class="img-fluid rounded z-depth-1" zoomable=true alt="A ControlNet block: the original neural block is locked, a trainable copy is connected through zero convolutions and added back." caption="<strong>Lock the original, clone it, connect through zero convolutions.</strong> <em>Zhang, Rao & Agrawala, ICCV 2023.</em>" %}

Text prompts control _content_ but not _geometry_. ControlNet adds conditioning on edges, depth, normals, segmentation maps or pose skeletons — without retraining the base model.

The construction: clone the encoder blocks of a frozen Stable Diffusion, connect the copy through **zero-initialised** 1×1 convolutions, and add its output back into the frozen path. At step 0 the zero convolutions output exactly zero, so the model is **bit-identical to the original** — training can only add capability, never degrade the base. And it does learn, because the gradient through a zero convolution is non-zero whenever the _input_ is non-zero.

It works from a few tens of thousands of examples and reports a sudden-convergence step at which the model begins to follow the condition.

**SDXL** (arXiv:2307.01952) pushed quality further along three axes: an ensemble of text encoders concatenating CLIP and OpenCLIP embeddings for richer conditioning; an ensemble-of-experts approach adding a dedicated _refiner_ model specialised for the final denoising steps; and micro-conditioning that feeds the model signals like original image resolution without extra supervision. **Plug-and-Play** (CVPR 2023) offered a complementary image-to-image route, using an image condition for coarse structure while the text prompt governs fine detail.

#### Era recap {#cv-foundation-models-and-the-promptable-paradigm--recap}

| Method         | Year | Mechanism                                | Headline                                    |
| -------------- | ---- | ---------------------------------------- | ------------------------------------------- |
| ConvNeXt       | 2022 | Swin's recipe inside a pure ConvNet      | 87.8% top-1; ~49% higher throughput         |
| ConvNeXt V2    | 2023 | Sparse-conv FCMAE + GRN                  | Masked pretraining ported to ConvNets       |
| Mask2Former    | 2022 | Mask queries + masked attention          | 57.8 PQ / 50.1 AP / 57.7 mIoU, one model    |
| Grounding DINO | 2023 | Language fused at neck, query and head   | Open-vocabulary detection, zero-shot COCO   |
| DINOv2         | 2023 | Self-distillation + iBOT on curated 142M | Frozen features rival supervised SOTA       |
| SAM            | 2023 | Promptable masks; encode-once decoder    | 1.1B masks / 11M images; zero-shot transfer |
| ControlNet     | 2023 | Frozen base + zero-init side branch      | Structural control, base provably preserved |
| SDXL           | 2023 | Dual text encoders + refiner ensemble    | Higher-resolution latent diffusion          |

> **Three of these eight are the same mechanism**
> DINOv2, SAM and ControlNet all say: **freeze a large pretrained thing, attach something cheap, train only that.** The variations are what gets attached — a linear probe, a prompt decoder, a zero-initialised side branch — and what the frozen thing knows.

### 3D becomes real-time, vision learns to talk {#cv-3d-becomes-real-time-vision-learns-to-talk}

_Three converging trends: promptable segmentation extends fully into video, 3D reconstruction shifts from implicit neural fields to explicit primitives, and multimodal language models become a mainstream vision interface._

#### What changed {#cv-3d-becomes-real-time-vision-learns-to-talk--overview}

> **3D changes representation**
>
> - NeRF — beautiful, implicit, fundamentally slow
> - 3D Gaussian Splatting — explicit primitives, real-time
> - Depth Anything V2 — monocular depth across indoor, outdoor and aerial imagery

> **Interface and efficiency**
>
> - LLaVA — the open vision + LLM recipe
> - SAM 2 — prompting extended to video via memory
> - YOLOv9 / v10 — NMS removed from the real-time lineage
> - Consistency models, flow matching — few-step generation

#### NeRF: the implicit baseline {#cv-3d-becomes-real-time-vision-learns-to-talk--nerf}

An MLP maps (x, y, z, θ, φ) → (colour, density), rendered by quadrature along camera rays with a differentiable volume-rendering integral. Because the whole path is differentiable, a _photometric_ loss on the training views optimises the scene itself. [The pipeline figure and the full loss family are in the task atlas.](#cv-neural-rendering-and-novel-views)

- **Positional encoding is essential** — without it the MLP's spectral bias produces blurry mush.
- View-dependence gives specularities almost for free.
- **The cost:** an MLP evaluation per sample per ray, spent uniformly — including on empty space. Days to train, seconds per frame.

#### 3D Gaussian Splatting {#cv-3d-becomes-real-time-vision-learns-to-talk--3dgs}

**SIGGRAPH / ACM TOG 2023** · Kerbl, Kopanas, Leimkühler & Drettakis — Inria / MPI · [arXiv:2308.04079](https://arxiv.org/abs/2308.04079) · **Mechanism 6**

{% include figure.liquid loading="lazy" path="assets/img/cv/gaussiansplatting_pipeline.png" class="img-fluid rounded z-depth-1" zoomable=true alt="3D Gaussian Splatting pipeline: SfM initialisation, projection, differentiable tile rasterisation, gradient flow and adaptive density control." caption="<strong>No network in the inner loop.</strong> Initialise from SfM points, project and rasterise, backpropagate, and adaptively clone, split or prune Gaussians. <em>Kerbl et al., SIGGRAPH 2023.</em>" %}

Represent the scene as millions of anisotropic 3D Gaussians — position, covariance (factored as scale × rotation to keep it positive semi-definite), opacity, and spherical-harmonic view-dependent colour. Three contributions:

1. **3D Gaussians initialised from the sparse SfM point cloud** already produced by camera calibration, which keeps the properties of a continuous volumetric radiance field and places no primitives in empty space.
2. **Interleaved optimisation and adaptive density control** — clone Gaussians in under-reconstructed regions, split over-large ones, prune transparent ones, driven by view-space positional gradients.
3. **A fast, visibility-aware tile-based rasteriser** with per-tile depth sorting and correct differentiable α-blending, which accelerates both training and rendering.

**State-of-the-art visual quality at ≥30 fps, 1080p** — a combination the prior NeRF-based methods, which query a network per pixel, did not reach at the same time. A 2024 survey records the combination of the reconstruction quality of implicit neural models with an explicit data structure that is dramatically more editable and efficient to render.

##### Splatting: advantages and limitations {#cv-3d-becomes-real-time-vision-learns-to-talk--3dgs-tradeoffs}

> **The mechanism**
>
> - **Compute follows content.** Empty space costs nothing because there are no primitives there. NeRF pays for it on every ray.
> - **Rasterisation, not ray marching.** Decades of GPU design are optimised for exactly this operation.
> - **Explicit data structures are editable** — crop, transform, compose, stream. A NeRF's scene lives in opaque MLP weights.
> - **Optimisation is well-conditioned** — each Gaussian has local influence, so gradients do not fight globally.

> **The costs**
>
> - **No surface.** A Gaussian cloud is not a mesh and has no well-defined normal; extracting geometry needs extra machinery (SuGaR, 2DGS and successors).
> - **Optimised for view synthesis, not metric accuracy.** It can look photorealistic while being locally wrong.
> - **Memory-hungry** — millions of primitives per scene.
> - Anisotropic Gaussians produce their own characteristic artefacts at extrapolated viewpoints.

#### LLaVA and the VLM architecture template {#cv-3d-becomes-real-time-vision-learns-to-talk--llava}

**NeurIPS 2023 Oral** · Liu, Li, Wu & Lee — Wisconsin / Microsoft / Columbia · [arXiv:2304.08485](https://arxiv.org/abs/2304.08485)

{% include figure.liquid loading="lazy" path="assets/img/cv/llava_arch.png" class="img-fluid rounded z-depth-1" zoomable=true alt="LLaVA architecture: a frozen CLIP vision encoder, a learned projection, and a pretrained language model." caption="<strong>Architecturally minimal.</strong> Frozen CLIP ViT-L/14 → a learned projection → a pretrained LLM, with image tokens placed directly in the text sequence. <em>Liu et al., NeurIPS 2023.</em>" %}

**The contribution is the training data.** Language-only GPT-4 was prompted with existing image annotations, captions and boxes, to generate multimodal instruction-following dialogue. Training then proceeds in two stages:

- **Stage 1** — feature alignment on a 558K-image subset of LAION-CC-SBU, training the projection only, with both encoder and LLM frozen.
- **Stage 2** — visual instruction tuning on ~150K GPT-generated dialogues plus ~515K academic VQA examples.

The first model reached an 85.1% relative score against GPT-4 on a synthetic multimodal benchmark, and **92.53% on ScienceQA** when fine-tuned. LLaVA-1.5 (October 2023) improved the projection to a two-layer MLP and led 11 of 12 benchmarks at release; LLaVA-NeXT (2024) extended to new LLM backbones and higher resolutions.

**The design space this opened:** connector type (linear, MLP, Q-Former, perceiver resampler); whether the vision tower is frozen or jointly trained; and how to handle native resolution (tiling, AnyRes, dynamic ViT). Every subsequent open VLM is a set of choices in that space.

OpenAI's **GPT-4V**, released in 2023, was the leading closed counterpart, scoring 67.7% on the MM-Vet benchmark for integrated vision–language capability — substantially ahead of contemporary open models at the time. Researchers found that visual Chain-of-Thought prompting yielded significant additional improvements on structured visual reasoning such as mathematical reasoning and chart analysis.

#### SAM 2: an image is a one-frame video {#cv-3d-becomes-real-time-vision-learns-to-talk--sam2}

**Meta FAIR, July 2024** · Ravi, Gabeur, Hu, Hu, Ryali, Ma, Khedr, Rädle, Rolland, Gustafson et al. · [arXiv:2408.00714](https://arxiv.org/abs/2408.00714) · **Mechanism 5**

{% include figure.liquid loading="lazy" path="assets/img/cv/sam2_arch.png" class="img-fluid rounded z-depth-1" zoomable=true alt="SAM 2 architecture: per-frame encoding conditioned on a memory bank via memory attention, producing masklets across a video." caption="<strong>Streaming memory.</strong> A memory encoder writes per-frame features and mask predictions into a FIFO bank; memory attention conditions the current frame on it. <em>Ravi et al., 2024.</em>" %}

Generalises SAM from single images to video by treating an image as a single-frame video. The new task, **Promptable Visual Segmentation**, lets a user provide points, boxes or masks on _any_ frame and returns the corresponding spatio-temporal _masklet_ across all frames — iteratively refinable with further prompts, and robust to the object temporarily disappearing behind an occluder, with an occlusion head predicting object presence.

- **SA-V**: roughly 51,000 real-world videos and more than 600,000 masklets collected across 47 countries — **53× more annotations** than the previous largest video segmentation dataset, produced by a model-in-the-loop data engine.
- Better video accuracy using **3× fewer user interactions** than prior approaches such as SAM combined with XMem++ or Cutie.
- **6–8.4× faster than the original SAM on pure image segmentation**, and more accurate.
- Released under Apache 2.0 in four sizes (Tiny, Small, Base Plus, Large), with real-time 30+ fps for all but the largest; SAM 2.1 added multi-object tracking improvements in late 2024.

Note the shape of the result: a _memory_ module plus a _data engine_ converted an image model into a video model without changing the underlying paradigm.

#### YOLOv9 and YOLOv10: closing the set-prediction loop {#cv-3d-becomes-real-time-vision-learns-to-talk--yolov10}

**NeurIPS 2024** · Wang, Chen, Liu, Chen, Lin, Han & Ding — Tsinghua · [arXiv:2405.14458](https://arxiv.org/abs/2405.14458) · **Mechanism 2**

{% include figure.liquid loading="lazy" path="assets/img/cv/yolov10_arch.png" class="img-fluid rounded z-depth-1" zoomable=true alt="Consistent dual assignments: a one-to-many head and a one-to-one head trained together with a consistent matching metric." caption="<strong>Dual assignment.</strong> Train a one-to-many head for rich supervision alongside a one-to-one head that produces no duplicates; discard the former at inference. <em>Wang et al., NeurIPS 2024.</em>" %}

NMS was the last hand-designed stage in the real-time lineage — and a genuine latency cost, because it is sequential and data-dependent. YOLOv10 removes it entirely through **consistent dual assignments**: the two heads use a _consistent_ matching metric so they rank candidates identically, which is what lets the one-to-one head inherit the one-to-many head's fast convergence without inheriting its duplicates.

**DETR's idea, delivered at YOLO latency.** Across six variants (N, S, M, B, L, X): YOLOv10-N at 1.84 ms and YOLOv10-S at 2.49 ms are the lowest-latency options; YOLOv10-X reaches **54.4% mAP at 10.70 ms**.

**YOLOv8** (Ultralytics, 2023) had earlier introduced a CSPDarknet backbone with cross-stage partial connections and SiLU activation, and unified detection, instance segmentation, pose estimation, classification and oriented bounding boxes in one codebase. **YOLOv9** (arXiv:2402.13616) introduced _Programmable Gradient Information_ with a reversible auxiliary branch, addressing information lost through deep feedforward stacks, and showed the best balance of precision, recall and mAP in several comparative studies including adverse-weather conditions.

#### Making diffusion fast {#cv-3d-becomes-real-time-vision-learns-to-talk--fast-diffusion}

> **Consistency models (ICML 2023)**
> The probability-flow ODE defines a trajectory from noise to data. Train a network f<sub>θ</sub>(x<sub>t</sub>, t) that maps _any_ point on a trajectory to its origin, enforcing f<sub>θ</sub>(x<sub>t</sub>,t) = f<sub>θ</sub>(x<sub>t′</sub>,t′) along it. Gives **one- or two-step** sampling, either distilled from a teacher diffusion model or trained standalone. Latent Consistency Models port this to Stable Diffusion.

> **Flow matching / rectified flow (ICLR 2023)**
> The model regresses a **velocity field** that transports noise to data along prescribed paths, preferably straight ones:<br>`ℒ = 𝔼[ ‖v<sub>θ</sub>(x<sub>t</sub>,t) − (x₁ − x₀)‖² ]`<br>Simulation-free training, and straight paths mean fewer integration steps. Adopted as the training objective of SD3, Flux and much subsequent work.

Both reduce the number of network evaluations at sampling time: one shortens the trajectory, the other maps points on it directly to the origin. Both address the same property, that diffusion sampling is iterative where GAN sampling is one forward pass.

#### Era recap {#cv-3d-becomes-real-time-vision-learns-to-talk--recap}

| Method                | Year | Mechanism                                  | Headline                                       |
| --------------------- | ---- | ------------------------------------------ | ---------------------------------------------- |
| 3D Gaussian Splatting | 2023 | Explicit Gaussians + tile rasterisation    | SOTA quality at 30+ fps, 1080p                 |
| LLaVA                 | 2023 | Frozen CLIP + projection + LLM             | The open visual-instruction-tuning recipe      |
| GPT-4V                | 2023 | GPT-4 augmented with vision input          | 67.7% on MM-Vet                                |
| Consistency models    | 2023 | Map any ODE point to its origin            | 1–2 step sampling                              |
| Flow matching         | 2023 | Regress a velocity field on straight paths | Simulation-free training; SD3 / Flux           |
| YOLOv9                | 2024 | Programmable Gradient Information          | Reported precision/recall balance among v8–v10 |
| SAM 2                 | 2024 | Streaming memory over frames               | 53× larger video dataset; real-time            |
| YOLOv10               | 2024 | Consistent dual assignment, NMS-free       | 54.4% mAP at 10.7 ms                           |

> **What the frontier question became**
> SAM 2 is a _data-engine_ story. LLaVA is a _synthetic-supervision_ story. Depth Anything, in the next era, is a _distillation_ story. In each the architecture is taken from earlier work and the contribution is **the source of the training signal**.

### Video, depth and concepts {#cv-video-depth-and-concepts}

_Video generation reaches minute-long coherence, self-supervised backbones scale to billions of parameters and exceed weakly-supervised methods on dense tasks, segmentation extends from geometric prompts to natural-language concepts, and discriminatively trained monocular depth scores above diffusion-based depth._

#### DiT: giving generation a scaling law {#cv-video-depth-and-concepts--dit}

**ICCV 2023** · Peebles & Xie · [arXiv:2212.09748](https://arxiv.org/abs/2212.09748) · **Mechanism 1** · **Mechanism 4**

Replace latent diffusion's U-Net with a plain **transformer** over latent patches, conditioning through **adaLN-Zero** — regress per-block scale and shift from the timestep/class embedding, initialised so that each block starts as the identity. That last detail is [mechanism 1](#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--m1) again: a residual branch that begins as a no-op is safe to add.

**FID decreases monotonically with transformer Gflops** across the model sizes tested. The extension to video then follows by adding compute.

#### Sora: video generation as world simulation {#cv-video-depth-and-concepts--sora}

**OpenAI, February 2024** · Video generation models as world simulators · **Mechanism 4**

A text-to-video diffusion model capable of generating up to one minute of high-definition video while maintaining visual quality and strong prompt adherence. The architecture is a **diffusion transformer**:

- Compress raw video into a lower-dimensional latent _spacetime_ representation using a dedicated video compression network.
- Decompose that representation into **spacetime patches** — the direct analogue of word tokens in a language model — which serve as the transformer's input.
- Generate by starting from pure visual noise and iteratively denoising, guided by CLIP-like text conditioning.

The key technical insight was that **unifying how video and image data are represented as patches** allowed training across a much wider range of durations, resolutions and aspect ratios than prior video models could handle. Sample quality improved significantly with additional training compute — diffusion transformers scale for video as effectively as they do for language and images.

Sora builds on the same diffusion architecture underlying DALL·E 3, adapted with additional temporal controls. Open-source efforts such as Open-Sora replicated the approach with a **Spatial-Temporal Diffusion Transformer (STDiT)** that decouples spatial self-attention within each frame from temporal attention across frames at the same spatial location — making efficient video diffusion training more broadly accessible.

> **On "general purpose simulators of the physical world"**
> OpenAI explicitly framed the scaling behaviour as suggestive of a path toward world simulation, and that framing shaped a great deal of subsequent research. These models are trained on **appearance**. Object permanence, contact and causality appear in the samples partially and inconsistently, and are not constrained by the training objective.

#### Depth Anything V2: data engineering, fixed architecture {#cv-video-depth-and-concepts--depthanything2}

**NeurIPS 2024** · Yang, Kang, Huang, Zhao, Xu, Feng & Zhao · [arXiv:2406.09414](https://arxiv.org/abs/2406.09414) · **Mechanism 3**

{% include figure.liquid loading="lazy" path="assets/img/cv/depthanything2_pipeline.png" class="img-fluid rounded z-depth-1" zoomable=true alt="Depth Anything V2 pipeline: a teacher trained on synthetic images pseudo-labels millions of real unlabelled images to train student models." caption="<strong>A synthetic teacher bridging to real data through pseudo-labels.</strong> <em>Yang et al., NeurIPS 2024.</em>" %}

Monocular depth estimation — predicting a full depth map from a single RGB image, with no multi-camera setup — advanced through three _data_ choices, with the architecture held fixed:

1. **Replace all labelled real training images with photorealistic synthetic ones** for the initial teacher. Synthetic labels are exact; real depth annotations are noisy, sparse at edges, and incorrect on transparent surfaces.
2. **Scale up the teacher's capacity substantially**, so it can absorb the synthetic-to-real domain gap.
3. **Use that teacher to pseudo-label over 62 million real unlabelled images**, and train the released student models on that bridge — never on the noisy real labels.

The resulting models span 25M to 1.3B parameters and are more than **10× faster** than depth models built on Stable Diffusion such as Marigold and GeoWizard, at higher accuracy, with finer detail and smaller degradation than Depth Anything V1. The ViT-Large variant achieved roughly **97.1% mean accuracy** across indoor, outdoor, transparent, adverse-weather, aerial and underwater imagery. An engineered _discriminative_ pipeline therefore scores above the more computationally expensive generative approaches on this dense-prediction task.

#### DINOv3: self-supervision at 7B parameters {#cv-video-depth-and-concepts--dinov3}

**Meta AI / FAIR, August 2025** · Siméoni, Vo, Seitzer et al. · [arXiv:2508.10104](https://arxiv.org/abs/2508.10104) · **Mechanism 3**

{% include figure.liquid loading="lazy" path="assets/img/cv/dinov3_gram.png" class="img-fluid rounded z-depth-1" zoomable=true alt="Evolution of dense feature quality during long self-supervised training, showing degradation and the effect of Gram anchoring." caption="<strong>Dense features degrade during very long training — Gram anchoring stops it.</strong> <em>Siméoni et al., 2025.</em>" %}

A 7× larger model than DINOv2 (a 6.7-billion-parameter ViT) trained on a 12× larger dataset (roughly 1.7 billion images curated from a pool of about 17 billion), while using only a fraction of the compute that weakly-supervised methods like CLIP require.

**Gram anchoring** is the key technical innovation. In very long, large-scale self-supervised runs, _global_ features keep improving while _dense, patch-level_ features degrade — the patch similarity structure drifts and becomes noisy, which silently destroys exactly what makes the backbone useful for segmentation and depth. Gram anchoring regularises the Gram matrix of patch features toward an earlier checkpoint's, preserving dense quality without freezing the representation outright.

Evaluated as a **frozen backbone** — no fine-tuning — across roughly sixty benchmarks and fifteen distinct vision tasks, DINOv3 is reported by its authors at state-of-the-art performance. It is the first purely self-supervised model to score above weakly-supervised models such as SigLIP 2 on a broad range of dense-prediction probing tasks including object detection, semantic segmentation, depth estimation and video object tracking. Released under a commercial licence with backbones from 21M to 6.7B parameters, plus dedicated ConvNeXt variants and a specialised satellite-imagery backbone trained on MAXAR data.

> **Why this closes a loop opened in 2019** > [MoCo](#cv-scale-self-supervision-and-set-prediction--moco) made unsupervised pretraining competitive with supervised. [DINOv2](#cv-foundation-models-and-the-promptable-paradigm--dinov2) made it competitive with weakly-supervised on many tasks. DINOv3 scores above it on a broad set of dense tasks, with a correction to a failure mode, dense-feature drift, that appears only at scale. On these benchmarks the reported results require **neither labels nor paired text**.

#### SAM 3: promptable concept segmentation {#cv-video-depth-and-concepts--sam3}

**Meta AI / FAIR, November 2025** · Segment Anything with Concepts · **Mechanism 5**

SAM 1 and SAM 2 answered "segment the thing I am pointing at" — one object per prompt. SAM 3 extends the lineage beyond geometric prompts to **natural-language concept prompts**, introducing the task of **Promptable Concept Segmentation (PCS)**: given a short noun phrase such as "yellow school bus", or an image exemplar, return segmentation masks _and unique identities_ for **every matching object instance simultaneously**.

- Architecturally, an image-level detector and a memory-based video tracker share a single backbone.
- Recognition and localisation are deliberately **decoupled via a dedicated presence head**, which separates "is this concept present?" from "where exactly is it?" — and measurably boosts detection accuracy by letting each question be answered by the machinery suited to it.
- Trained via a scalable data engine producing a dataset with **4 million unique concept labels**, including deliberately constructed hard negatives, spanning both images and video.
- **2× accuracy gain** over existing systems on both image and video promptable concept segmentation, while also improving on previous SAM capabilities for standard visual segmentation.
- Open-sourced alongside a new benchmark, **Segment Anything with Concepts (SA-Co)**, built specifically to evaluate the task.

This unifies single-image, video, interactive refinement and concept-driven detection under one backbone — transforming SAM from a geometric segmentation tool into a concept-level vision foundation model.

#### YOLO11: continued real-time refinement {#cv-video-depth-and-concepts--yolo11}

**Ultralytics, September 2024**

Two headline architectural changes: compact **C3k2** CSP bottleneck blocks replacing the prior C2f blocks for improved efficiency, and a new **C2PSA** module combining cross-stage-partial design with spatial attention for more robust feature aggregation — particularly benefiting small-object detection. Multi-task support spans detection, instance segmentation, pose estimation, classification and oriented bounding boxes in one framework.

YOLO11 reports **up to 42% fewer parameters than YOLOv8** in its large variant at _higher_ mAP, pushing the accuracy–latency Pareto frontier further than any prior YOLO generation. YOLO11x reaches 54.7% mAP at 11.3 ms TensorRT latency on a T4 GPU; the smallest variant, YOLO11n, achieves 39.5% mAP at just 1.5 ms.

#### Vision–language models consolidate {#cv-video-depth-and-concepts--vlm}

By 2025 the open VLM landscape had consolidated around a small number of dominant lineages — most prominently Alibaba's Qwen-VL series and Shanghai AI Lab's InternVL series — both of which rapidly approached and in some benchmarks matched closed frontier models.

| Model          | Date     | Organisation    | Vision encoder     | Notable capability                                                   |
| -------------- | -------- | --------------- | ------------------ | -------------------------------------------------------------------- |
| InternVL 2.5   | Dec 2024 | Shanghai AI Lab | InternViT-300M/6B  | MMMU 70.1% with chain-of-thought test-time scaling                   |
| **Qwen2.5-VL** | Feb 2025 | Alibaba         | Native dynamic ViT | DocVQA 96.4%; hours-long video; agentic tool use                     |
| InternVL3      | Apr 2025 | Shanghai AI Lab | InternViT-300M/6B  | Unified multimodal/text-only pretraining, variable position encoding |
| SmolVLM        | Apr 2025 | Hugging Face    | SigLIP-B/16 (93M)  | Runs in under 1 GB VRAM at 256M parameters                           |

Qwen2-VL (2024) introduced **M-RoPE** (multimodal rotary position encoding) and native dynamic-resolution image processing; Qwen2.5-VL refined this into a native dynamic ViT combined with window attention, reducing computational cost while preserving native image resolution and adding support for hours-long video understanding and computer/phone agentic tool use.

> **The documented gap**
> A 2026 benchmarking analysis found that even leading open VLMs such as InternVL3 and Qwen2.5-VL still show notable weakness on **fine-grained shape and pattern recognition — around 30–45% accuracy** — relative to their strong performance on document and chart understanding, where they exceed 90%. They read text _in_ images superbly and reason about _geometry_ in them poorly. Visual–language alignment for abstract geometric reasoning remained an unsolved gap as of this period, and the bottleneck is the vision–language interface and training distribution, not the language model.

#### Era recap {#cv-video-depth-and-concepts--recap}

| Method            | Date     | Mechanism                                        | Headline                                         |
| ----------------- | -------- | ------------------------------------------------ | ------------------------------------------------ |
| Sora              | Feb 2024 | Diffusion transformer on spacetime patches       | Coherent HD video up to one minute               |
| Depth Anything V2 | Jun 2024 | Synthetic teacher → pseudo-labelled students     | >10× faster than diffusion depth models          |
| YOLO11            | Sep 2024 | C3k2 blocks + C2PSA spatial attention            | 54.7% mAP at 11.3 ms; 42% fewer params than v8   |
| Qwen2.5-VL        | Feb 2025 | Native dynamic-resolution ViT + window attention | 96.4% DocVQA; hours-long video; agentic use      |
| DINOv3            | Aug 2025 | Gram anchoring at 6.7B params / 1.7B images      | First SSL model to exceed weakly-supervised SOTA |
| SAM 3             | Nov 2025 | Concept prompts + presence head                  | 2× accuracy on concept segmentation              |

### Any-view geometry, concepts and embodiment {#cv-any-view-geometry-concepts-and-embodiment}

_Geometry becomes a single forward pass, segmentation reaches single-image 3D reconstruction, and a transformer detector exceeds 60 AP on COCO in real time._

#### VGGT: geometry as a single forward pass {#cv-any-view-geometry-concepts-and-embodiment--vggt}

**CVPR 2025** · Wang, Chen, Karaev, Vedaldi, Rupprecht & Novotny — Oxford VGG / Meta · [arXiv:2503.11651](https://arxiv.org/abs/2503.11651)

{% include figure.liquid loading="lazy" path="assets/img/cv/vggt_arch.png" class="img-fluid rounded z-depth-1" zoomable=true alt="VGGT architecture: images patchified by DINO, camera tokens appended, alternating frame-wise and global attention, with heads for cameras, depth, point maps and tracks." caption="<strong>Alternating frame-wise and global attention.</strong> One transformer predicts camera parameters, depth maps, point maps and tracks jointly. <em>Wang et al., CVPR 2025.</em>" %}

Classical 3D vision is an optimisation pipeline: features → matching → RANSAC → triangulation → bundle adjustment. VGGT replaces the whole thing with _one feed-forward transformer_.

- **Input:** one to hundreds of views. **Output:** camera intrinsics and extrinsics, depth maps, point maps and point tracks — predicted _jointly_.
- **Alternating attention:** frame-wise self-attention within a view, interleaved with global attention across all views. This is what lets the model reason about cross-view geometry without an explicit matching stage.
- Inference is a single forward pass, in seconds. The optimisation pipelines take minutes to hours.

Over-parameterised joint prediction is reported above the geometry-aware pipelines built around the explicit equations, and is used as an _initialiser_ for subsequent bundle adjustment, which is how the two are now combined.

#### Depth Anything 3: one target for any number of views {#cv-any-view-geometry-concepts-and-embodiment--da3}

**ByteDance Seed, November 2025** · Lin, Chen, Liew, Chen, Li, Shi, Feng & Kang · [arXiv:2511.10647](https://arxiv.org/abs/2511.10647)

{% include figure.liquid loading="lazy" path="assets/img/cv/depthanything3_teaser.png" class="img-fluid rounded z-depth-1" zoomable=true alt="Depth Anything 3 pipeline: a plain transformer predicting a unified depth-ray target from any number of input views." caption="<strong>Deliberate minimalism.</strong> A plain transformer backbone and a single unified depth–ray prediction target. <em>Lin et al., 2025.</em>" %}

Generalises monocular depth estimation into a unified spatial reconstruction system capable of predicting spatially consistent geometry from an _arbitrary_ number of visual inputs — single images, multi-view collections, or full videos — with or without known camera poses. Two deliberately minimal design choices:

- **A single plain transformer backbone**, a DINO-style encoder with no task-specific layers.
- **A singular unified "depth–ray" prediction target** replaces the multi-task training pipelines prior geometry models used. _Depth_ encodes the distance from a pixel to the camera and the _ray_ encodes that pixel's projection direction in 3D. Together they determine the geometry required for reconstruction, so one head replaces the separate per-task heads.

On its evaluation benchmark DA3 reports the highest scores across all tested tasks, above VGGT by an average of **35–44% in camera pose accuracy and 23–25% in geometric accuracy**, and above its own predecessor Depth Anything V2 on _monocular_ depth specifically — despite DA3's far broader any-view scope.

> **The team's own framing, and why it matters**
> "A plain transformer trained on depth-and-ray targets with teacher–student supervision can unify any-view geometry without ornate architectures." The claim runs against the trend toward specialised multi-task architectures in the 3D vision literature, and matches [ViT's](#cv-the-transformer-takeover--vit) argument about inductive bias: specialised structure substitutes for data and scale, and bounds accuracy once both are available.

#### SAM 3D: 3D from a single image {#cv-any-view-geometry-concepts-and-embodiment--sam3d}

**Meta AI / FAIR, November 2025** · SAM 3D: 3Dfy Anything in Images · **Mechanism 4**

A companion suite of two generative models that reconstruct full 3D geometry, texture and spatial layout directly from a single 2D image.

- **SAM 3D Objects** — a two-stage architecture of diffusion transformers: a first stage predicting coarse 3D shape and object pose, followed by a refinement stage adding realistic texture and surface detail, with a DINOv2 encoder processing the input image.
- **SAM 3D Body** — a transformer encoder–decoder predicting 3D human pose and mesh parameters directly from a single image, robust under partial occlusion.

Both were trained via a human-and-model-in-the-loop data engine combining synthetic 3D asset pretraining with real-world image alignment — an approach Meta describes as "breaking the 3D data barrier", since ground-truth 3D annotations for natural images are otherwise extremely scarce.

- At least a **5:1 win rate** over prior leading single-image 3D reconstruction methods in human preference tests.
- **28% reduction in Chamfer Distance and 19% improvement in normal consistency** on public benchmarks.
- Unlike prior approaches limited to 2.5D visible-surface reconstruction, it predicts **complete 3D geometry** that can be re-rendered from any viewpoint — including occluded or unseen parts of an object.

Because reconstructed objects and human meshes can be composed into unified 3D scenes, SAM 3D was rapidly integrated into consumer products including Facebook Marketplace's "View in Room" feature and Meta's Quest 3 and Horizon Worlds creation tools.

> **A different point on the data-efficiency curve — with a caveat**
> Prior 3D-from-images methods — MVS, NeRF, splatting — all require _many calibrated views_. Single-image reconstruction is qualitatively different, and unlocks 3D from legacy photographs where re-capture is impossible. **But these are generative priors as much as reconstructors.** The occluded geometry is _plausible_, not measured. The model is inventing a statistically likely back surface, and it will do so confidently whether or not the invention is right.

#### RF-DETR: the first real-time detector past 60 AP {#cv-any-view-geometry-concepts-and-embodiment--rfdetr}

**ICLR 2026 (released March 2025)** · Robinson, Robicheaux, Popov, Ramanan & Peri — Roboflow · [arXiv:2511.09554](https://arxiv.org/abs/2511.09554) · **Mechanism 2**

{% include figure.liquid loading="lazy" path="assets/img/cv/rfdetr_pareto.png" class="img-fluid rounded z-depth-1" zoomable=true alt="Latency versus COCO mAP showing the RF-DETR family on the accuracy-latency Pareto frontier." caption="<strong>The accuracy–latency frontier.</strong> RF-DETR variants against prior real-time detectors on COCO. <em>Robinson et al., 2025.</em>" %}

A transformer-based real-time detector built on a **DINOv2 vision-transformer backbone**, with weight-sharing neural architecture search used to identify optimal accuracy–latency tradeoffs across model sizes. It became the first real-time model — defined as 25+ FPS on an NVIDIA T4 — to exceed **60 mean Average Precision** on Microsoft COCO.

- Six sizes from Nano (30.5M parameters, 384×384 input, 2.3 ms latency) to 2XL (126.9M parameters, 880×880 input).
- RF-DETR-2XL reaches **60.1 AP<sub>50:95</sub>**; RF-DETR-L reaches 56.5 AP<sub>50:95</sub> at 6.8 ms on TensorRT FP16.
- Also leads **RF100-VL**, a benchmark that measures transfer to custom domains. COCO measures one fixed category set.
- An RF-DETR Segmentation variant, extending the base architecture with a MaskDINO-inspired segmentation head, previewed in October 2025 with the full size family following in January 2026.

**It directly overturned the long-standing assumption that DETR-style architectures were inherently too slow for real-time deployment** relative to YOLO-family single-stage detectors — five years after DETR made the idea work at all.

> **Note the benchmark shift**
> RF-DETR reports RF100-VL alongside COCO. COCO AP has saturated, and _transfer_ to a domain the model was not trained on is the quantity these benchmarks now separate. See [what the benchmarks hid](#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--benchmarks).

#### YOLO26: native end-to-end detection {#cv-any-view-geometry-concepts-and-embodiment--yolo26}

**Ultralytics, September 2025** · **Mechanism 2**

YOLO26 removes non-maximum suppression through a **native end-to-end training strategy**, in place of an approximation of one. Whereas earlier detectors relied on NMS to filter duplicate overlapping detections, YOLO26 is trained from the outset to learn a one-to-one relationship between objects and outputs, producing a single definitive box per object instance directly.

Three further innovations underpin the shift:

- **Removal of Distribution Focal Loss** in favour of a simpler, more hardware-friendly bounding-box parameterisation.
- **Small-Target-Aware Label Assignment (STAL)** paired with **Progressive Loss Balancing (ProgLoss)** for training stability, particularly benefiting small-object accuracy.
- A novel **MuSGD optimiser** — a hybrid of SGD and the Muon optimiser, inspired by techniques from large language model training — for faster, more stable convergence.

The performance gains were pronounced specifically on CPU and edge hardware: **up to a 43% reduction in CPU inference latency** compared to NMS-based baselines, with the nano variant exceeding 40 mAP at roughly 1.5 ms and the extra-large variant reaching approximately 57.5 mAP at 11.5 ms, surpassing YOLO11x while maintaining real-time throughput. It is the first Ultralytics release to natively unify detection, instance segmentation, classification, pose estimation and oriented bounding boxes in one NMS-free architecture.

> **A five-year arc, completed**
> A comparative retrospective spanning YOLOv5 through YOLO26 characterises the series' trajectory as a "deployment-first philosophy", where each generation removed one more architectural or post-processing stage — first accuracy, then efficiency, and finally, with YOLO26, complete inference-pipeline simplicity. [DETR proposed set prediction in 2020.](#cv-scale-self-supervision-and-set-prediction--detr) It took until 2025 for the idea to arrive, natively, in the lineage optimised for speed.

#### Embodied vision–language models {#cv-any-view-geometry-concepts-and-embodiment--embodied}

A distinct new category emerged explicitly targeting embodied agents operating in the physical world, moving vision–language models beyond static image-and-text reasoning toward navigation and interaction.

**Hy-Embodied-VLM-1.0** (Tencent, July 2026) exemplifies the trend: a Mixture-of-Experts vision–language foundation model activating only about 3 billion parameters per token out of roughly 30 billion total, built on a dedicated language backbone paired with a specialised vision encoder. Evaluated across 38 benchmarks spanning embodied perception, physical-world understanding and embodied reasoning, it ranked first on 19 benchmarks and second on 11 more, achieving state-of-the-art results on vision-and-language navigation tasks such as R2R-CE and strong zero-shot performance on object-goal navigation in Matterport3D environments.

> **The architectural shift being claimed**
> The field increasingly frames this as a move from _"vision as a bolt-on adapter"_ — a pretrained LLM trunk with a vision encoder attached, the LLaVA/Qwen-VL/GPT-4V generation — toward models whose **trunk itself functions as a world model** that predicts and acts within physical environments, early-fusing all modalities into a single transformer. Whether that reframing delivers is the open question of the next window.

#### Era recap {#cv-any-view-geometry-concepts-and-embodiment--recap}

| Method              | Date                 | Mechanism                                       | Headline                                      |
| ------------------- | -------------------- | ----------------------------------------------- | --------------------------------------------- |
| RF-DETR             | Mar 2025 (ICLR 2026) | DINOv2 backbone + weight-sharing NAS            | First real-time model to exceed 60 AP on COCO |
| VGGT                | Mar 2025             | One feed-forward transformer for all 3D targets | Scores above optimisation-based pipelines     |
| YOLO26              | Sep 2025             | Native one-to-one assignment, no NMS            | 43% faster CPU inference vs. NMS baselines    |
| SAM 3D              | Nov 2025             | Two-stage DiT: shape/pose, then texture         | 5:1 human-preference win; complete geometry   |
| Depth Anything 3    | Nov 2025             | Plain transformer + depth–ray target            | +35–44% camera pose accuracy over VGGT        |
| Hy-Embodied-VLM-1.0 | Jul 2026             | MoE backbone + specialised vision encoder       | 1st place on 19 of 38 embodied benchmarks     |

> **Where the decade lands**
> Recognition is promptable by concept. Geometry is recoverable from any number of views, including one, in a single forward pass. Backbones are self-supervised and used frozen. And the last hand-designed post-processing step — NMS — is gone from both major detection lineages. [The synthesis page](#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid) assembles what this means.

## Synthesis and reference

### The atlas — 29 modules {#cv-the-atlas-29-modules}

_Every topic, grouped into six blocks. Each module follows the same shape: what it estimates, the image-formation assumptions, classical and deep pipelines, objectives, tricks, failure modes and takeaways._

#### Foundations · 1–5 {#cv-the-atlas-29-modules--foundations}

The language every later module depends on. Nothing downstream is safe to read before these.

- **[1 · Task map & taxonomy](#cv-the-master-task-taxonomy)** — Twelve families of inverse problems, their inputs and outputs, and the dependency structure that explains why upstream advances propagate field-wide.

- **[2 · Image formation & cameras](#cv-image-formation-and-cameras)** — Pinhole projection, distortion, radiometry, noise, rolling shutter. The forward model every inverse problem inverts.

- **[3 · Calibration & alignment](#cv-calibration-and-sensor-alignment)** — DLT, Zhang's method, rectification, hand–eye, camera–LiDAR and camera–IMU. The family the decade left untouched.

- **[4 · Objectives & optimization](#cv-vision-objectives-and-optimization)** — The common template, robust M-estimators and their MAP reading, Gauss–Newton, LM, the Schur complement, RANSAC.

- **[5 · Multiscale & filtering](#cv-multiscale-vision-and-filtering)** — Scale space, pyramids, the structure tensor, edge-preserving filters, morphology, and coarse-to-fine optimisation.

- **[+ The shared pipeline](#cv-the-shared-pipeline-and-the-objective-template)** — The ten operations common to classical and learned systems, and where each family's methods sit within them.

#### Image level · 6–9 {#cv-the-atlas-29-modules--image}

- **[6 · Restoration](#cv-restoration-and-enhancement)** — One degradation model for denoising, deblurring, SR, demosaicing and inpainting — plus the perception–distortion tradeoff.

- **[7 · Features & primitives](#cv-features-and-visual-primitives)** — Canny, Harris, DoG/SIFT, ORB, Hough, MSER — and the pipeline that outlived its own operators.

- **[8 · Correspondence](#cv-correspondence-and-registration)** — Feature-based vs. direct alignment, the transform hierarchy, DLT normalisation, inverse-compositional LK.

- **[9 · Stitching & fusion](#cv-image-stitching-and-fusion)** — Global rotation bundle adjustment, projection surfaces, exposure compensation, seam cuts and multiband blending.

#### Semantic understanding · 10–14 {#cv-the-atlas-29-modules--semantic}

- **[10 · Classification & retrieval](#cv-classification-retrieval-and-recognition)** — Closed-set vs. open-set outputs, metric-learning losses, mining, Mixup/CutMix, calibration.

- **[11 · Object detection](#cv-object-detection)** — Anchors, label assignment, focal loss, the IoU loss family, NMS and its removal by set prediction.

- **[12 · Segmentation & matting](#cv-segmentation-and-matting)** — Four output types, four loss families, PQ, dense CRFs, and the compositing equation.

- **[13 · Keypoints & pose](#cv-keypoints-and-pose)** — Heatmaps vs. regression, soft-argmax, PAFs, PnP, 6-DoF pose and symmetry-aware losses.

- **[14 · Text & document](#cv-text-and-document-vision)** — CTC vs. attention decoding, TPS rectification, 2D layout encoding, OCR-free models.

#### Motion & geometry · 15–19 {#cv-the-atlas-29-modules--motion}

- **[15 · Optical & scene flow](#cv-optical-flow-and-scene-flow)** — Brightness constancy, the aperture problem, Horn–Schunck, Lucas–Kanade, cost volumes, RAFT.

- **[16 · Stereo & depth](#cv-stereo-and-depth-estimation)** — Why everything is inverse depth, SGM's two penalties, soft-argmin, and the self-supervised recipe.

- **[17 · Pose, SfM, VO & SLAM](#cv-camera-pose-sfm-vo-and-slam)** — Epipolar geometry, triangulation, bundle adjustment, gauge freedom, loop closure, IMU preintegration.

- **[18 · Visual tracking](#cv-visual-tracking)** — Kalman prediction, Hungarian assignment, Mahalanobis gating, track lifecycle, HOTA.

- **[19 · Video understanding](#cv-video-understanding)** — Inflation, factorised 3D convolution, SlowFast, divided attention, tube masking, temporal localisation.

#### 3D & generative · 20–23 {#cv-the-atlas-29-modules--threed}

- **[20 · Point clouds](#cv-point-clouds-and-3d-perception)** — Permutation invariance, sparse convolution, ICP variants, FPFH, Chamfer vs. EMD, 3D detection.

- **[21 · 3D reconstruction](#cv-3d-reconstruction-and-completion)** — TSDF fusion, marching cubes, Poisson reconstruction, implicit surfaces, completion as generation.

- **[22 · Neural rendering](#cv-neural-rendering-and-novel-views)** — The volume rendering integral, positional encoding, 3DGS density control, and why floaters exist.

- **[23 · Generation & translation](#cv-image-generation-and-translation)** — VAE/GAN/AR/diffusion, the divergence table, classifier-free guidance, flow matching, CycleGAN.

#### Multimodal · 24–25 {#cv-the-atlas-29-modules--multimodal}

- **[24 · Vision–language](#cv-vision-language-understanding)** — Contrastive pretraining, SigLIP's sigmoid loss, connector architectures, grounding, hallucination control, and the documented geometric-reasoning gap.

- **[25 · Scene reasoning & embodied](#cv-scene-reasoning-and-embodied-vision)** — Scene graphs, affordances, navigation and SPL, active vision, world models, and what changes when perception feeds control.

#### Cross-cutting · 26–29 {#cv-the-atlas-29-modules--crosscutting}

- **[26 · Photometric consistency](#cv-photometric-consistency)** — Warp-and-compare, its six assumptions, the engineering corrections, and Monodepth2's three refinements.

- **[27 · Losses & regularization](#cv-losses-and-regularization)** — The complete objective vocabulary, organised by what each loss assumes; multi-task weighting and uncertainty.

- **[28 · Engineering tricks](#cv-cross-cutting-mechanisms-and-failure-modes)** — Robust estimation, multiscale, the seven consistency constraints, augmentation, imbalance, post-processing.

- **[29 · Evaluation & failure](#cv-evaluation-and-failure-analysis)** — Metrics and what they hide, leakage, calibration, effective robustness, label noise, ablation discipline.

#### Threads that cross the atlas {#cv-the-atlas-29-modules--threads}

Several ideas recur in modules that otherwise look unrelated. Following one of these across pages is a faster route to understanding than reading in order.

| Thread                         | Appears in                                                                                                                                                                                                                                       |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **The structure tensor**       | [5](#cv-multiscale-vision-and-filtering--derivatives) · [7 (Harris)](#cv-features-and-visual-primitives--harris) · [15 (Lucas–Kanade)](#cv-optical-flow-and-scene-flow--lk) — corner detection, trackability and flow observability are one fact |
| **Reprojection error**         | [3](#cv-calibration-and-sensor-alignment--objective) · [13 (PnP)](#cv-keypoints-and-pose--pnp) · [17 (BA)](#cv-camera-pose-sfm-vo-and-slam--ba) — the canonical geometric residual                                                               |
| **Photometric residual**       | [26](#cv-photometric-consistency) · [15](#cv-optical-flow-and-scene-flow) · [16](#cv-stereo-and-depth-estimation--selfsup) · [17 (direct)](#cv-camera-pose-sfm-vo-and-slam--direct) · [22](#cv-neural-rendering-and-novel-views)                 |
| **Multiscale hierarchy**       | [5](#cv-multiscale-vision-and-filtering--lineage) — pyramids, FPN, U-Net skips, cost-volume cascades, hash grids, Swin patch merging                                                                                                             |
| **Set prediction**             | [11](#cv-object-detection--set) · [12 (Mask2Former)](#cv-segmentation-and-matting) · [18 (association)](#cv-visual-tracking--association) · [19 (temporal)](#cv-video-understanding--localisation)                                               |
| **Expectation-based decoding** | [13 (soft-argmax)](#cv-keypoints-and-pose--representation) · [16 (soft-argmin)](#cv-stereo-and-depth-estimation--deep-stereo) — both fail on bimodal distributions                                                                               |
| **RANSAC before refinement**   | [4](#cv-vision-objectives-and-optimization--map) · [8](#cv-correspondence-and-registration) · [17](#cv-camera-pose-sfm-vo-and-slam) · [20 (ICP)](#cv-point-clouds-and-3d-perception--registration)                                               |
| **Surrogate–metric gap**       | [11 (GIoU)](#cv-object-detection--iou) · [12 (Lovász)](#cv-segmentation-and-matting--overlap) · [27](#cv-losses-and-regularization--mismatch) · [29](#cv-evaluation-and-failure-analysis--mismatch)                                              |

### Six mechanisms, one ladder, and what the numbers hid {#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid}

_Forty papers, six recurring mechanisms. This page sets out what recurred, where the supervision came from, which architectures persisted, and what the benchmarks did not measure._

#### The six mechanisms {#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--six}

|       | Mechanism                     | First clean instance         | Where it recurs                                                    |
| ----- | ----------------------------- | ---------------------------- | ------------------------------------------------------------------ |
| **1** | Make the easy path identity   | ResNet (2016)                | Pre-activation blocks, ControlNet zero-convs, DiT adaLN-Zero, LoRA |
| **2** | Predict a set, not a grid     | DETR (2020)                  | Mask2Former, YOLOv10, YOLO26, RF-DETR, SAM 3                       |
| **3** | Manufacture the supervision   | MoCo / SimCLR (2019–20)      | BYOL, MAE, DINOv2/v3, Depth Anything, every data engine            |
| **4** | Work in a latent space        | Latent Diffusion (2022)      | DiT, SDXL, Sora spacetime patches, SAM 3D stage one                |
| **5** | Heavy encoder, cheap head     | SAM (2023)                   | SAM 2/3, frozen-backbone probing, VLM connectors                   |
| **6** | Return to explicit primitives | 3D Gaussian Splatting (2023) | Splat-based SLAM and editing, hybrid representations               |

<a id="cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--m1"></a>

**1 · Make the easy path identity**

If a block can do nothing at zero cost, adding it can only help. [ResNet](#cv-depth-detection-and-the-first-believable-images--resnet) established this for depth, and it never stopped being useful — because the same argument applies to _any_ modification of a working model.

- **ControlNet's zero convolutions** make the augmented diffusion model bit-identical to the original at step 0, so training can only add capability.
- **DiT's adaLN-Zero** initialises each transformer block as identity.
- **LoRA** adapters initialise one factor to zero for the same reason.

<a id="cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--m2"></a>

**2 · Predict a set, not a grid**

Move duplicate suppression out of inference and into the loss. [DETR's](#cv-scale-self-supervision-and-set-prediction--detr) bipartite matching makes the assignment a bijection, so two predictions cannot claim one object, and the NMS stage is removed.

The five-year lag before this reached real-time latency ([YOLOv10](#cv-3d-becomes-real-time-vision-learns-to-talk--yolov10), [YOLO26](#cv-any-view-geometry-concepts-and-embodiment--yolo26), [RF-DETR](#cv-any-view-geometry-concepts-and-embodiment--rfdetr)) is the clearest example on this site of an idea being _correct_ long before it was _deployable_.

<a id="cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--m3"></a>

**3 · Manufacture the supervision**

The training signal is constructed from the data itself, by contrast, masking, distillation or synthesis. This is the decade's largest single theme and gets [its own section below](#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--ladder).

<a id="cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--m4"></a>

**4 · Work in a latent space**

Most bits in an image are perceptually irrelevant. Compress them away with an autoencoder trained once, then spend the expensive iterative computation on a tensor roughly 48× smaller. [Latent Diffusion](#cv-the-transformer-takeover--ldm) is the clean instance; [Sora's](#cv-video-depth-and-concepts--sora) spacetime patches extend it to video, and SAM 3D's first stage applies it to shape.

The generalisation: _find the representation in which the hard problem is small._

<a id="cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--m5"></a>

**5 · Heavy encoder, cheap head**

Encode once, answer many queries. [SAM's](#cv-foundation-models-and-the-promptable-paradigm--sam) ViT-H encoder runs once per image at ~0.15 s; the prompt decoder answers in ~50 ms, which is what makes interactive segmentation and the annotation loop possible.

The same split underlies every frozen-backbone-plus-linear-probe setup, every VLM connector, and SlowFast's thin fast pathway. It is also an _economic_ argument: amortise the expensive computation across many uses.

<a id="cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--m6"></a>

**6 · Return to explicit primitives**

Where implicit representations are slow, go back to primitives. [3D Gaussian Splatting](#cv-3d-becomes-real-time-vision-learns-to-talk--3dgs) replaced NeRF's MLP-in-the-inner-loop with millions of explicit Gaussians and a rasteriser — cost then scales with occupied volume, empty regions contain no primitives, and the scene is editable because it is data rather than weights.

This is the one mechanism that runs _against_ the decade's general direction, which is why it is worth stating: more learning is not always the answer, and "differentiable" does not have to mean "neural".

#### The supervision ladder {#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--ladder}

Each rung yields more supervision per unit of human effort than the one before.

| Rung                       | Representative work  | What supplies the signal                                            | Limitation                                                           |
| -------------------------- | -------------------- | ------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **1 · Human labels**       | ImageNet, COCO       | Annotators                                                          | Bounded by cost; fixes the vocabulary in advance                     |
| **2 · Contrast views**     | MoCo, SimCLR         | Two augmentations of one image must agree                           | Needs augmentation priors; texture shortcuts                         |
| **3 · Mask & reconstruct** | BEiT, MAE            | The image predicts its own missing parts                            | No priors needed, but linear-probe features are weaker               |
| **4 · Self-distil**        | DINO, DINOv2, DINOv3 | An EMA teacher supervises the student                               | Dense features drift at very long training — fixed by Gram anchoring |
| **5 · Synthetic teacher**  | Depth Anything V2    | A simulator provides exact labels                                   | Synthetic-to-real domain gap; needs a large teacher to absorb it     |
| **6 · Data engine**        | SA-1B, SA-V, SA-Co   | A model proposes, humans correct, the corrections retrain the model | Humans remain in the loop — as correctors, not annotators            |

> **Read it as an economic argument, not a technical one**
> Annotation cost was addressed by six successive sources of training signal. In the last two rungs a person **corrects** model output in place of producing it from scratch, a 10–100× difference in rate, with the kind of human input unchanged. That distinction matters when forecasting: the cost curve bent sharply, but it did not go to zero, and every "zero-shot" model on this site was trained on someone's labelled data at some remove.

Notice also which [data terms](#cv-the-shared-pipeline-and-the-objective-template--data-terms) each rung uses. Rungs 2–4 manufacture a residual out of the data's own structure — they are [consistency constraints](#cv-cross-cutting-mechanisms-and-failure-modes--consistency) promoted to training objectives. Rung 5 borrows a residual from a simulator. Rung 6 is the only one that still needs a human to look at an image.

#### Architectural outcomes {#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--architecture}

> **Observed outcomes**
>
> - **Attention became the default operator.** [ConvNeXt](#cv-foundation-models-and-the-promptable-paradigm--convnext) showed a modernised ConvNet matches Swin at equal recipe; ConvNeXt V2 showed it can take masked pretraining too.
> - **The common factor is the plain, scalable block** — uniform, few inductive biases, LayerNorm, GELU, residual, trained with a modern recipe at scale. ViT and ConvNeXt are both instances.
> - **Hierarchy came back** everywhere dense prediction mattered — windows, patch merging, spatial reduction.

> **Confounds worth naming**
>
> - Architecture papers changed the training recipe at the same time. ConvNeXt _quantified_ this: +2.7 points from recipe alone.
> - Pretraining corpus is rarely held constant across comparisons.
> - Compute-matched comparisons are rarer than they should be, and throughput ≠ FLOPs on real hardware.
> - State-space alternatives (VMamba, Vision Mamba) have lower asymptotic complexity and have not replaced attention on the reported benchmarks, which bounds how much the operator accounts for.

The pattern across ViT, ConvNeXt and Depth Anything 3 is consistent enough to state as a rule: **specialised structure substitutes for data and scale, and bounds accuracy once both are available.** Every one of those three papers makes the argument in a different subfield, and the 2025 geometry models make it again against hand-designed multi-view pipelines.

#### What the benchmarks hid {#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--benchmarks}

> **Measurement problems**
>
> - **COCO AP has saturated.** Recent increments come largely from label-assignment and training-schedule changes.
> - **Test-set contamination** at web-scale pretraining cannot be measured while the corpus is undisclosed, and the corpora grew through the decade.
> - **"Zero-shot" is under-specified** when the pretraining corpus is undisclosed — it means unseen in _fine-tuning_, not unseen.
> - **Single-number reporting** hides the distribution that matters: small objects, rare classes, hard negatives.

> **What the field did about it**
>
> - Robustness suites — ImageNet-A/R/Sketch/V2, ObjectNet — became standard alongside in-distribution accuracy.
> - **Transfer benchmarks** (VTAB, RF100-VL) measure accuracy on new domains instead of one fixed taxonomy.
> - Frozen-feature evaluation across many tasks (DINOv2/v3's ~60 benchmarks) resists overfitting to any one of them.
> - Human-preference evaluation for generation, where reference-based metrics such as FID are known to correlate poorly.

This is also visible in the [objective template](#cv-the-shared-pipeline-and-the-objective-template--template): the surrogate loss and the reported metric were never the same object, and the decade's most reliable progress came when a paper closed that gap deliberately — focal loss for imbalance, GIoU for box regression, PQ for panoptic, Lovász for IoU.

#### Open problems entering 2026 {#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--open}

> **Representation and reasoning**
>
> - **Compositional and geometric reasoning in VLMs** — 30–45% on fine-grained shape tasks is the headline failure of the current paradigm.
> - **Calibrated uncertainty** under distribution shift; confidence remains a ranking signal, not a probability.
> - **Video as dynamics, not appearance.** Generation is excellent; prediction of physical outcomes is not.
> - **Long-horizon memory** beyond a bounded frame buffer.

> **Method and practice**
>
> - **Metric geometry from learned models** — depth and splats are relative and plausible, not surveyed.
> - **Surface extraction** from explicit radiance primitives remains bolted on.
> - **Evaluation of promptable models**: an unbounded output space means unbounded, unenumerable failure modes.
> - **Efficiency of the frontier** — 6.7B-parameter backbones are not deployable, and distillation loses exactly the dense quality that was hard to get.

#### Takeaways {#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid--takeaways}

1. **2016 removed the depth ceiling, and identity-initialised branches never stopped being useful.** ResNet, ControlNet, adaLN-Zero and LoRA are one idea wearing four costumes.
2. **The binding constraint moved: architecture → supervision → interface.** The constraint a paper addresses places it in that sequence.
3. **Set prediction removed hand-designed post-processing.** DETR's idea needed five years to reach YOLO latency — and it got there.
4. **Nobody solved annotation; the field routed around it six times.** The supervision ladder is the decade's real throughline.
5. **Geometry and semantics converged onto one backbone family**, and geometry became feed-forward.
6. **Capability outran evaluation.** The hardest open problems are now measurement problems.

> **The central conclusion, restated**
> Computer-vision methods are combinations of **representation + correspondence + constraint + robust optimisation**. Deep learning changed the representation and learned parts of matching and inference, but the classical constraints remain plainly visible: photometric warping supervises depth and rendering; reprojection error drives calibration and bundle adjustment; smoothness regularizes flow and geometry; pyramids handle scale; RANSAC and robust losses handle outliers; cost volumes represent correspondence; consistency checks handle ambiguity. Treating these explicitly produces a more durable understanding than studying network names in isolation.

### Paper index {#cv-paper-index}

_Every paper discussed on this page, with era and mechanism columns._

<a id="cv-paper-index--paperTable"></a>

| Year | Paper                        | Authors / group                               | Venue            | Contribution                                                                     | Mech. | Link                                                                              |
| ---- | ---------------------------- | --------------------------------------------- | ---------------- | -------------------------------------------------------------------------------- | ----- | --------------------------------------------------------------------------------- |
| 2014 | **FCN**                      | Long, Shelhamer, Darrell                      | CVPR 2015        | Fully convolutional dense prediction; the template for every segmentation net    |       | [arXiv](https://arxiv.org/abs/1411.4038)                                          |
| 2015 | **U-Net**                    | Ronneberger, Fischer, Brox                    | MICCAI 2015      | Symmetric encoder–decoder with concatenative skips; still the diffusion backbone |       | [arXiv](https://arxiv.org/abs/1505.04597)                                         |
| 2015 | **Faster R-CNN**             | Ren, He, Girshick, Sun                        | NeurIPS 2015     | Learned region proposals; detection becomes end-to-end trainable                 |       | [arXiv](https://arxiv.org/abs/1506.01497)                                         |
| 2016 | **PointNet**                 | Qi, Su, Mo, Guibas                            | CVPR 2017        | Permutation-invariant direct point-cloud processing                              |       | [arXiv](https://arxiv.org/abs/1612.00593)                                         |
| 2015 | **ResNet**                   | He, Zhang, Ren, Sun — MSR                     | CVPR 2016        | Residual reformulation; 152 layers, 3.57% top-5 ensemble                         | **1** | [arXiv](https://arxiv.org/abs/1512.03385)                                         |
| 2016 | **Identity Mappings**        | He, Zhang, Ren, Sun — MSR                     | ECCV 2016        | Pre-activation block ordering; stable 1001-layer network                         | **1** | [arXiv](https://arxiv.org/abs/1603.05027)                                         |
| 2015 | **YOLO**                     | Redmon, Divvala, Girshick, Farhadi            | CVPR 2016        | Detection as one regression; ~45 fps                                             |       | [arXiv](https://arxiv.org/abs/1506.02640)                                         |
| 2015 | **SSD**                      | Liu, Anguelov, Erhan, Szegedy et al.          | ECCV 2016        | Multi-scale single-shot detection; 74.3% mAP at 59 fps                           |       | [arXiv](https://arxiv.org/abs/1512.02325)                                         |
| 2016 | **FPN**                      | Lin, Dollár, Girshick, He et al.              | CVPR 2017        | Top-down pathway with lateral connections; semantics at every scale              |       | [arXiv](https://arxiv.org/abs/1612.03144)                                         |
| 2017 | **Mask R-CNN**               | He, Gkioxari, Dollár, Girshick — FAIR         | ICCV 2017        | Parallel mask branch + RoIAlign; swept COCO 2017                                 |       | [arXiv](https://arxiv.org/abs/1703.06870)                                         |
| 2017 | **Focal loss / RetinaNet**   | Lin, Goyal, Girshick, He, Dollár — FAIR       | ICCV 2017        | Down-weights easy negatives; 39.1 COCO AP one-stage                              |       | [arXiv](https://arxiv.org/abs/1708.02002)                                         |
| 2017 | **MobileNets**               | Howard et al. — Google                        | arXiv 2017       | Depthwise separable convs; width and resolution multipliers                      |       | [arXiv](https://arxiv.org/abs/1704.04861)                                         |
| 2018 | **MobileNetV2**              | Sandler, Howard, Zhu et al. — Google          | CVPR 2018        | Inverted residual with linear bottleneck; ~3.4M params                           | **1** | [arXiv](https://arxiv.org/abs/1801.04381)                                         |
| 2017 | **ProGAN**                   | Karras, Aila, Laine, Lehtinen — NVIDIA        | ICLR 2018        | Progressive growing; first photorealistic 1024² faces                            |       | [arXiv](https://arxiv.org/abs/1710.10196)                                         |
| 2018 | **StyleGAN**                 | Karras, Laine, Aila — NVIDIA                  | CVPR 2019        | Mapping network + AdaIN style injection; FID 4.40, FFHQ                          |       | [arXiv](https://arxiv.org/abs/1812.04948)                                         |
| 2018 | **DeepLabv3+**               | Chen, Zhu, Papandreou, Schroff, Adam          | ECCV 2018        | Atrous separable convolution with a decoder                                      |       | [arXiv](https://arxiv.org/abs/1802.02611)                                         |
| 2018 | **Cascade R-CNN**            | Cai, Vasconcelos                              | CVPR 2018        | Progressive IoU-threshold heads for high-precision detection                     |       | [arXiv](https://arxiv.org/abs/1712.00726)                                         |
| 2019 | **EfficientNet**             | Tan, Le — Google Brain                        | ICML 2019        | Compound scaling of depth/width/resolution; B7 at 84.3%                          |       | [arXiv](https://arxiv.org/abs/1905.11946)                                         |
| 2019 | **MoCo**                     | He, Fan, Wu, Xie, Girshick — FAIR             | CVPR 2020        | Queue of negatives + momentum encoder; exceeds supervised transfer               | **3** | [arXiv](https://arxiv.org/abs/1911.05722)                                         |
| 2020 | **SimCLR**                   | Chen, Kornblith, Norouzi, Hinton              | ICML 2020        | Augmentation composition + projection head                                       | **3** | [arXiv](https://arxiv.org/abs/2002.05709)                                         |
| 2020 | **BYOL**                     | Grill, Strub, Altché et al. — DeepMind        | NeurIPS 2020     | Self-supervision with no negatives; predictor + EMA target                       | **3** | [arXiv](https://arxiv.org/abs/2006.07733)                                         |
| 2020 | **SwAV**                     | Caron, Misra, Mairal et al. — FAIR            | NeurIPS 2020     | Online clustering with Sinkhorn; multi-crop                                      | **3** | [arXiv](https://arxiv.org/abs/2006.09882)                                         |
| 2018 | **Panoptic Segmentation**    | Kirillov, He, Girshick, Rother, Dollár        | CVPR 2019        | Unified stuff + things task and the PQ metric                                    |       | [arXiv](https://arxiv.org/abs/1801.00868)                                         |
| 2018 | **SlowFast**                 | Feichtenhofer, Fan, Malik, He — FAIR          | ICCV 2019        | Two pathways at two frame rates; SOTA on Kinetics/AVA                            |       | [arXiv](https://arxiv.org/abs/1812.03982)                                         |
| 2020 | **RAFT**                     | Teed, Deng — Princeton                        | ECCV 2020        | All-pairs correlation + recurrent GRU updates for optical flow                   |       | [arXiv](https://arxiv.org/abs/2003.12039)                                         |
| 2019 | **StyleGAN2**                | Karras, Laine, Aittala et al. — NVIDIA        | CVPR 2020        | Weight demodulation; path-length reg.; FID 2.84                                  |       | [arXiv](https://arxiv.org/abs/1912.04958)                                         |
| 2020 | **DETR**                     | Carion, Massa, Synnaeve et al. — FAIR         | ECCV 2020        | Set prediction + Hungarian matching; no anchors or NMS                           | **2** | [arXiv](https://arxiv.org/abs/2005.12872)                                         |
| 2020 | **Deformable DETR**          | Zhu, Su, Lu, Li, Wang, Dai                    | ICLR 2021        | Sparse deformable attention; 46.2 AP, 10× faster convergence                     | **2** | [arXiv](https://arxiv.org/abs/2010.04159)                                         |
| 2020 | **NeRF**                     | Mildenhall, Srinivasan, Tancik et al.         | ECCV 2020        | Implicit radiance field + differentiable volume rendering                        |       | [arXiv](https://arxiv.org/abs/2003.08934)                                         |
| 2020 | **DDPM**                     | Ho, Jain, Abbeel — Berkeley                   | NeurIPS 2020     | Denoising diffusion as noise-prediction regression                               | **4** | [arXiv](https://arxiv.org/abs/2006.11239)                                         |
| 2020 | **ViT**                      | Dosovitskiy et al. — Google                   | ICLR 2021        | Patch tokens + plain transformer; the data-scale crossover                       |       | [arXiv](https://arxiv.org/abs/2010.11929)                                         |
| 2020 | **DeiT**                     | Touvron, Cord, Douze et al. — FAIR            | ICML 2021        | Distillation token; competitive ViT with ImageNet-1k only                        |       | [arXiv](https://arxiv.org/abs/2012.12877)                                         |
| 2021 | **CLIP**                     | Radford, Kim, Hallacy et al. — OpenAI         | ICML 2021        | Contrastive image–text on 400M pairs; zero-shot transfer                         |       | [arXiv](https://arxiv.org/abs/2103.00020)                                         |
| 2021 | **Swin Transformer**         | Liu, Lin, Cao, Hu et al. — MSRA               | ICCV 2021        | Shifted windows + patch merging; 87.3% / 58.7 AP / 53.5 mIoU                     |       | [arXiv](https://arxiv.org/abs/2103.14030)                                         |
| 2021 | **PVT**                      | Wang, Xie, Li, Fan et al.                     | ICCV 2021        | Pyramid ViT with spatial-reduction attention                                     |       | [arXiv](https://arxiv.org/abs/2102.12122)                                         |
| 2021 | **SegFormer**                | Xie, Wang, Yu, Anandkumar et al.              | NeurIPS 2021     | Mix Transformer encoder + all-MLP decoder; no positional encoding                |       | [arXiv](https://arxiv.org/abs/2105.15203)                                         |
| 2021 | **DINO**                     | Caron, Touvron, Misra et al. — FAIR           | ICCV 2021        | Self-distillation with ViT; emergent unsupervised segmentation                   | **3** | [arXiv](https://arxiv.org/abs/2104.14294)                                         |
| 2021 | **BEiT**                     | Bao, Dong, Piao, Wei — Microsoft              | ICLR 2022        | Masked image modelling predicting discrete visual tokens                         | **3** | [arXiv](https://arxiv.org/abs/2106.08254)                                         |
| 2021 | **MAE**                      | He, Chen, Xie, Li, Dollár, Girshick — FAIR    | CVPR 2022        | 75% masking, asymmetric encoder–decoder; 87.8% IN-1K-only                        | **3** | [arXiv](https://arxiv.org/abs/2111.06377)                                         |
| 2021 | **Latent Diffusion**         | Rombach, Blattmann, Lorenz, Esser, Ommer      | CVPR 2022        | Diffusion in a compressed VAE latent; released as Stable Diffusion               | **4** | [arXiv](https://arxiv.org/abs/2112.10752)                                         |
| 2022 | **Classifier-free guidance** | Ho, Salimans — Google                         | arXiv 2022       | One scalar trading diversity for fidelity; universally adopted                   |       | [arXiv](https://arxiv.org/abs/2207.12598)                                         |
| 2021 | **Diffusion Beats GANs**     | Dhariwal, Nichol — OpenAI                     | NeurIPS 2021     | Diffusion established as SOTA for ImageNet synthesis                             |       | [arXiv](https://arxiv.org/abs/2105.05233)                                         |
| 2022 | **DALL·E 2 (unCLIP)**        | Ramesh, Dhariwal, Nichol et al. — OpenAI      | arXiv 2022       | Diffusion decoder conditioned on CLIP image embeddings                           | **4** | [arXiv](https://arxiv.org/abs/2204.06125)                                         |
| 2022 | **ConvNeXt**                 | Liu, Mao, Wu, Feichtenhofer, Darrell, Xie     | CVPR 2022        | Controlled modernisation of ResNet; 82.0% vs Swin-T 81.3%                        |       | [arXiv](https://arxiv.org/abs/2201.03545)                                         |
| 2023 | **ConvNeXt V2**              | Woo, Debnath, Hu, Chen, Liu, Kweon, Xie       | CVPR 2023        | Sparse-conv masked pretraining + Global Response Normalization                   | **3** | [arXiv](https://arxiv.org/abs/2301.00808)                                         |
| 2021 | **Mask2Former**              | Cheng, Misra, Schwing, Kirillov, Girdhar      | CVPR 2022        | Masked attention + mask queries; 57.8 PQ / 50.1 AP / 57.7 mIoU                   | **2** | [arXiv](https://arxiv.org/abs/2112.01527)                                         |
| 2022 | **OWL-ViT**                  | Minderer, Gritsenko, Stone et al. — Google    | ECCV 2022        | Open-vocabulary detection from a CLIP ViT with detection heads                   |       | [arXiv](https://arxiv.org/abs/2205.06230)                                         |
| 2023 | **Grounding DINO**           | Liu, Zeng, Ren, Li et al.                     | ECCV 2024        | Language fused at neck, query and head; zero-shot COCO transfer                  |       | [arXiv](https://arxiv.org/abs/2303.05499)                                         |
| 2023 | **DINOv2**                   | Oquab, Darcet, Moutakanni et al. — FAIR       | TMLR 2024        | Self-distillation + iBOT on curated LVD-142M; frozen features                    | **3** | [arXiv](https://arxiv.org/abs/2304.07193)                                         |
| 2023 | **SAM**                      | Kirillov, Mintun, Ravi, Mao et al. — FAIR     | ICCV 2023        | Promptable segmentation; SA-1B with 1.1B masks                                   | **5** | [arXiv](https://arxiv.org/abs/2304.02643)                                         |
| 2023 | **ControlNet**               | Zhang, Rao, Agrawala — Stanford               | ICCV 2023        | Frozen base + zero-initialised trainable side branch                             | **1** | [arXiv](https://arxiv.org/abs/2302.05543)                                         |
| 2023 | **SDXL**                     | Podell, English, Lacey et al. — Stability AI  | ICLR 2024        | Dual text encoders + refiner ensemble; micro-conditioning                        |       | [arXiv](https://arxiv.org/abs/2307.01952)                                         |
| 2023 | **SigLIP**                   | Zhai, Mustafa, Kolesnikov, Beyer — Google     | ICCV 2023        | Pairwise sigmoid loss; no global normalisation, small-batch friendly             |       | [arXiv](https://arxiv.org/abs/2303.15343)                                         |
| 2023 | **3D Gaussian Splatting**    | Kerbl, Kopanas, Leimkühler, Drettakis         | SIGGRAPH 2023    | Explicit anisotropic Gaussians + tile rasteriser; 30+ fps at 1080p               | **6** | [arXiv](https://arxiv.org/abs/2308.04079)                                         |
| 2023 | **LLaVA**                    | Liu, Li, Wu, Lee — Wisconsin/Microsoft        | NeurIPS 2023     | Visual instruction tuning; GPT-4-synthesised dialogue data                       | **5** | [arXiv](https://arxiv.org/abs/2304.08485)                                         |
| 2022 | **DiT**                      | Peebles, Xie — Berkeley/NYU                   | ICCV 2023        | Transformer diffusion backbone; adaLN-Zero; FID scales with Gflops               | **4** | [arXiv](https://arxiv.org/abs/2212.09748)                                         |
| 2023 | **Consistency Models**       | Song, Dhariwal, Chen, Sutskever — OpenAI      | ICML 2023        | Map any ODE trajectory point to its origin; 1–2 step sampling                    |       | [arXiv](https://arxiv.org/abs/2303.01469)                                         |
| 2022 | **Flow Matching**            | Lipman, Chen, Ben-Hamu, Nickel, Le — FAIR     | ICLR 2023        | Simulation-free velocity-field regression on straight paths                      |       | [arXiv](https://arxiv.org/abs/2210.02747)                                         |
| 2024 | **SAM 2**                    | Ravi, Gabeur, Hu, Hu, Ryali et al. — FAIR     | arXiv 2024       | Streaming memory; SA-V with 600K+ masklets; 6–8.4× faster on images              | **5** | [arXiv](https://arxiv.org/abs/2408.00714)                                         |
| 2024 | **YOLOv10**                  | Wang, Chen, Liu, Chen et al. — Tsinghua       | NeurIPS 2024     | Consistent dual assignment; NMS-free; 54.4% mAP at 10.7 ms                       | **2** | [arXiv](https://arxiv.org/abs/2405.14458)                                         |
| 2024 | **YOLOv9**                   | Wang, Yeh, Liao                               | ECCV 2024        | Programmable Gradient Information with reversible auxiliary branch               |       | [arXiv](https://arxiv.org/abs/2402.13616)                                         |
| 2024 | **Sora**                     | OpenAI                                        | Tech report 2024 | Diffusion transformer over spacetime patches; one minute of HD video             | **4** | [report](https://openai.com/research/video-generation-models-as-world-simulators) |
| 2024 | **Depth Anything V2**        | Yang, Kang, Huang, Zhao et al.                | NeurIPS 2024     | Synthetic teacher → 62M pseudo-labelled real images; >10× faster than SD-based   | **3** | [arXiv](https://arxiv.org/abs/2406.09414)                                         |
| 2025 | **DINOv3**                   | Siméoni, Vo, Seitzer et al. — FAIR            | arXiv 2025       | Gram anchoring at 6.7B params / 1.7B images; beats weakly-supervised             | **3** | [arXiv](https://arxiv.org/abs/2508.10104)                                         |
| 2025 | **SAM 3**                    | Meta AI / FAIR                                | 2025             | Promptable concept segmentation; presence head; 4M concept labels                | **5** | [site](https://ai.meta.com/sam3/)                                                 |
| 2024 | **YOLO11**                   | Ultralytics                                   | 2024             | C3k2 blocks + C2PSA attention; 42% fewer params than v8 at higher mAP            |       | [docs](https://docs.ultralytics.com/models/yolo11/)                               |
| 2025 | **Qwen2.5-VL**               | Qwen Team — Alibaba                           | arXiv 2025       | Native dynamic-resolution ViT + window attention; DocVQA 96.4%                   |       | [arXiv](https://arxiv.org/abs/2502.13923)                                         |
| 2025 | **VGGT**                     | Wang, Chen, Karaev, Vedaldi et al. — VGG/Meta | CVPR 2025        | One feed-forward transformer for cameras, depth, points and tracks               |       | [arXiv](https://arxiv.org/abs/2503.11651)                                         |
| 2025 | **Depth Anything 3**         | Lin, Chen, Liew, Chen et al. — ByteDance Seed | arXiv 2025       | Plain transformer + unified depth–ray target; +35–44% pose over VGGT             |       | [arXiv](https://arxiv.org/abs/2511.10647)                                         |
| 2025 | **SAM 3D**                   | Meta AI / FAIR                                | 2025             | Two-stage DiT: shape and pose, then texture; complete occluded geometry          | **4** | [site](https://ai.meta.com/sam3d/)                                                |
| 2025 | **RF-DETR**                  | Robinson, Robicheaux, Popov, Ramanan, Peri    | ICLR 2026        | DINOv2 backbone + weight-sharing NAS; first real-time past 60 COCO AP            | **2** | [arXiv](https://arxiv.org/abs/2511.09554)                                         |
| 2025 | **YOLO26**                   | Ultralytics                                   | 2025             | Natively NMS-free; DFL removed; STAL + ProgLoss; MuSGD optimiser                 | **2** | [docs](https://docs.ultralytics.com/models/yolo26/)                               |
| 2026 | **Hy-Embodied-VLM-1.0**      | Tencent                                       | 2026             | MoE embodied VLM; 1st on 19 of 38 embodied benchmarks                            |       |                                                                                   |

> **A note on dates**
> The **Year** column is the arXiv preprint year where one exists, and the **Venue** column gives the publication venue and year. These differ frequently — ResNet is arXiv 2015 / CVPR 2016, Mask2Former is arXiv 2021 / CVPR 2022 — and the era assignment on this site follows the _preprint_, because that is when the idea entered circulation and began influencing other work.

### A 29-module curriculum {#cv-a-29-module-curriculum}

_The [task taxonomy](#cv-the-master-task-taxonomy) turned into a teaching sequence: twenty-nine modules in six blocks, a recommended production order, and one consistent template so the series stays coherent._

#### Block 1 · Foundations {#cv-a-29-module-curriculum--foundations}

These establish the language needed for every later task. Nothing downstream is safe to teach before them.

**1 · Computer Vision Task Map**

What vision estimates: appearance, semantics, geometry, motion, identity, physical state · inputs and outputs for major task families · classical, deep and hybrid approaches · relationships between tasks · the difference between loss, residual, regularizer, constraint and evaluation metric.

**2 · Image Formation and Cameras**

Pinhole model · perspective projection · coordinate systems · lens distortion · radiometry, illumination, reflectance, exposure and noise · Lambertian assumptions and their limits · rolling shutter and motion blur.

**3 · Calibration and Sensor Alignment**

Intrinsic and extrinsic calibration · stereo and multi-camera · camera–LiDAR and camera–IMU · hand–eye · rectification and synchronization · reprojection error · DLT, Zhang calibration, nonlinear refinement, robust calibration.

**4 · Vision Objectives and Optimization**

Data terms versus regularizers · L1, L2, Charbonnier, Huber, Tukey, Cauchy · photometric, reprojection, epipolar, feature, semantic, overlap and temporal residuals · maximum likelihood and MAP interpretations · gradient descent, Gauss–Newton, Levenberg–Marquardt, dynamic programming, graph cuts · RANSAC and robust estimation · uncertainty and confidence weighting.

**5 · Multiscale Vision and Filtering**

Convolution and correlation · Gaussian and Laplacian pyramids · scale space · Fourier and frequency-domain interpretation · image derivatives · morphological processing · coarse-to-fine optimization · classical filtering versus learned feature pyramids.

#### Block 2 · Image level {#cv-a-29-module-curriculum--image-level}

**6 · Restoration and Enhancement**

Denoising · deblurring and deconvolution · demosaicing · super-resolution · low-light enhancement · HDR and exposure fusion · inpainting · compression-artifact removal · Wiener filtering, Richardson–Lucy, total variation, non-local means, BM3D · reconstruction, perceptual, adversarial, gradient, frequency and TV losses.

**7 · Features and Visual Primitives**

Edges, corners, blobs, ridges, lines · contours and connected components · Harris, Shi–Tomasi, FAST, Canny, DoG, Hough, MSER · SIFT, SURF, BRIEF, ORB, HOG, LBP · scale and orientation invariance · non-maximum suppression · descriptor normalization and matching distances.

**8 · Correspondence and Registration**

Patch and template matching · feature matching · nearest-neighbour and mutual matching · ratio tests · RANSAC, MLESAC, PROSAC · translation, rigid, similarity, affine, homography and deformable transformations · direct versus feature-based alignment · SSD, SAD, NCC, mutual information, ECC and feature-space losses.

**9 · Image Stitching and Fusion**

Feature matching and homography estimation · global alignment · cylindrical and spherical projections · exposure compensation · seam selection · feathering and multiband blending · ghosting and parallax · panorama evaluation.

_Kept separate from module 8 deliberately: registration estimates transformations, while stitching adds projection choice, seam optimization, photometric compensation and compositing._

#### Block 3 · Semantic understanding {#cv-a-29-module-curriculum--semantic}

**10 · Classification and Retrieval**

Single-label and multi-label classification · fine-grained recognition · instance and place retrieval · face verification and person re-identification · classical bag-of-visual-words and Fisher vectors · CNN and transformer encoders · cross-entropy, BCE, label smoothing, focal loss, class weighting · contrastive, triplet, center and angular-margin losses · hard-negative mining, Mixup, CutMix, calibration.

**11 · Object Detection**

Sliding windows and cascades · region proposals · one-stage and two-stage detectors · anchor-based and anchor-free · dense prediction and query-based detection · classification, objectness and box-regression losses · Smooth L1, IoU, GIoU, DIoU, CIoU · label assignment, hard-negative mining, focal loss · NMS, Soft-NMS, tiling, multiscale inference.

**12 · Segmentation and Matting**

Thresholding, watershed, region growing, active contours, graph cuts, GrabCut · semantic, instance and panoptic segmentation · interactive and prompt-based segmentation · image and video matting · cross-entropy, Dice, Tversky, Lovász, focal, boundary and topology-aware losses · CRFs, morphology, connected components, boundary refinement.

**13 · Keypoints and Pose**

Corners versus semantic keypoints · facial, hand, animal and human landmarks · top-down and bottom-up human pose · heatmap prediction versus coordinate regression · part affinity and keypoint grouping · 2D and 3D articulated pose · heatmap, coordinate, visibility, bone, reprojection and temporal losses · soft-argmax, integral regression, PnP, kinematic constraints.

**14 · Text and Document Vision**

Text detection · OCR · handwriting recognition · scene-text recognition · document layout analysis · tables, formulas and key–value extraction · sequence recognition, CTC, attention, encoder–decoder models · geometric rectification and language-model correction.

_Deserves its own module: OCR otherwise gets scattered across recognition and vision–language reasoning despite having a distinct pipeline._

#### Block 4 · Motion and geometry {#cv-a-29-module-curriculum--motion}

**15 · Optical Flow and Scene Flow**

Brightness constancy · the aperture problem · Lucas–Kanade and Horn–Schunck · sparse versus dense motion · coarse-to-fine warping · cost volumes and correlation · photometric and feature constancy · smoothness and edge-aware regularization · forward–backward consistency · occlusion detection · supervised endpoint-error losses.

**16 · Stereo and Depth**

Epipolar geometry and rectification · stereo correspondence · local and global matching · census transform and Semi-Global Matching · disparity and inverse depth · monocular depth · multi-view stereo · depth completion and fusion · photometric reprojection, SSIM, smoothness, normal and scale-invariant losses · left–right consistency, minimum reprojection, auto-masking.

**17 · Camera Pose, SfM, VO and SLAM**

Fundamental and essential matrices · relative pose · PnP and camera localization · triangulation · structure from motion · bundle adjustment · feature-based and direct visual odometry · SLAM map management · relocalization and loop closure · pose-graph optimization · reprojection versus photometric objectives · robust kernels, keyframes, marginalization, scale recovery.

**18 · Visual Tracking**

Point and feature tracking · single- and multi-object tracking · tracking by detection · Kalman and particle filters · Hungarian assignment · motion, IoU and appearance costs · SORT, DeepSORT, ByteTrack · track birth, confirmation, occlusion, termination, re-identification · identity switches and trajectory metrics.

**19 · Video Understanding**

Video classification · action recognition · temporal action localization · event and anomaly detection · temporal segmentation · action anticipation · classical trajectories and motion descriptors · two-stream models, 3D CNNs, recurrent models, video transformers · temporal sampling, aggregation, consistency and temporal NMS.

#### Block 5 · 3D and generative {#cv-a-29-module-curriculum--threed}

**20 · Point Clouds and 3D Perception**

Filtering and downsampling · ground and plane removal · 3D classification · 3D semantic and instance segmentation · 3D object detection · point-cloud registration · ICP, point-to-plane ICP, RANSAC, FPFH, SHOT · voxel, pillar, BEV, range-image, graph and direct-point representations · Chamfer, Earth Mover's, occupancy, SDF, normal and 3D IoU losses.

**21 · 3D Reconstruction and Completion**

Depth fusion · occupancy grids · TSDF fusion · meshing and Marching Cubes · Poisson reconstruction · shape completion · implicit surfaces and signed distance fields · surface, normal, Eikonal, occupancy and topology objectives · mesh cleaning and geometric validation.

_Separate from module 20: perception predicts labels, boxes and poses; reconstruction estimates continuous or discrete geometry._

**22 · Neural Rendering and Novel Views**

Differentiable rendering · inverse rendering · NeRF and radiance fields · neural implicit surfaces · 3D Gaussian Splatting · novel-view synthesis · relighting and material estimation · RGB, depth, mask, normal, perceptual, distortion, sparsity and Eikonal losses · camera-pose refinement, exposure embeddings, occupancy acceleration, transient-object masking.

**23 · Image Generation and Translation**

Image synthesis · conditional generation · image-to-image translation · style transfer · editing and inpainting · GANs, VAEs, autoregressive models, diffusion models · adversarial, reconstruction, perceptual, identity, cycle-consistency and diffusion objectives · fidelity, diversity, controllability, hallucination.

_Separate from module 22: neural rendering reconstructs a scene under camera geometry, whereas generative modelling learns an image distribution._

#### Block 6 · Multimodal and cross-cutting {#cv-a-29-module-curriculum--multimodal}

**24 · Vision–Language Understanding**

Image captioning · VQA · text–image retrieval · referring-expression grounding · open-vocabulary detection and segmentation · scene graphs · document and OCR-aware reasoning · contrastive image–text learning · cross-attention and multimodal tokenization · grounding and language-model losses · prompting, instruction tuning, hallucination control.

**25 · Scene Reasoning and Embodied Vision**

Object relationships · scene graphs · affordances · visual navigation · goal-conditioned perception · active vision · sensorimotor prediction · spatial and temporal reasoning · mapping perception outputs into planning and control · uncertainty and safety considerations.

**26 · Photometric Consistency**

Warp-and-compare formulation · brightness and colour constancy · L1, L2, Charbonnier, SSIM, census, gradient and feature losses · inverse warping and differentiable sampling · visibility and occlusion masks · minimum reprojection · auto-masking · exposure compensation · forward–backward and cycle consistency · failure under reflection, transparency, saturation and dynamics. [Covered in full here.](#cv-photometric-consistency)

**27 · Losses and Regularization**

Regression and classification losses · overlap and boundary losses · metric-learning losses · photometric and geometric losses · distributional and adversarial losses · smoothness, TV, sparsity, low-rank, shape, temporal and consistency regularization · single-task versus multi-task weighting · aleatoric and epistemic uncertainty · training objective versus evaluation metric.

**28 · Engineering Tricks**

Pyramids and multiscale training · data normalization · geometric and photometric augmentation · hard-negative mining · balanced sampling · robust estimation · confidence thresholds · visibility reasoning · NMS, morphology, CRFs, hole filling · mixed precision, tiling, caching, deployment constraints · test-time augmentation and ensembling. [Covered in full here.](#cv-cross-cutting-mechanisms-and-failure-modes)

**29 · Evaluation and Failure Analysis**

Classification, detection, segmentation, depth, flow, pose, tracking, reconstruction and rendering metrics · dataset leakage and biased splits · confidence calibration · domain shift · label noise · adversarial and natural corruption · ablations and controlled diagnostics · runtime, memory, energy, latency · safety-critical evaluation · objective–metric mismatch.

#### Recommended production order {#cv-a-29-module-curriculum--order}

For building the modules sequentially, this ordering keeps every module's prerequisites behind it. It differs from the block order above because some cross-cutting modules are best written _after_ the tasks that motivate them.

1. Computer Vision Task Map
2. Image Formation and Cameras
3. Calibration and Sensor Alignment
4. Objectives and Optimization
5. Multiscale Vision and Filtering
6. Features and Visual Primitives
7. Correspondence and Registration
8. Restoration and Enhancement
9. Classification and Retrieval
10. Object Detection

11. Segmentation and Matting
12. Keypoints and Pose
13. Optical Flow and Scene Flow
14. Stereo and Depth
15. Camera Pose, SfM, VO and SLAM
16. Visual Tracking
17. Video Understanding
18. Point Clouds and 3D Perception
19. 3D Reconstruction and Completion

20. Neural Rendering and Novel Views
21. Image Generation and Translation
22. Text and Document Vision
23. Vision–Language Understanding
24. Scene Reasoning and Embodied Vision
25. Photometric Consistency
26. Losses and Regularization
27. Engineering Tricks
28. Evaluation and Failure Analysis

> **Where to start**
> The starting point is **module 1, the Computer Vision Task Map**. It should define the whole structure and show visually how calibration, correspondence, recognition, motion, geometry, reconstruction and multimodal reasoning connect — which is exactly the job the [taxonomy page](#cv-the-master-task-taxonomy) does on this site.

#### The standard module template {#cv-a-29-module-curriculum--template}

Every module should use the same internal structure, so the series stays coherent and a reader can navigate an unfamiliar task by position alone.

| #   | Section                    | What it answers                                      |
| --- | -------------------------- | ---------------------------------------------------- |
| 1   | **Problem definition**     | What is observed and what must be estimated?         |
| 2   | **Applications**           | Why does the task matter?                            |
| 3   | **Observability**          | What can and cannot be inferred from the inputs?     |
| 4   | **Image-formation model**  | Which physical assumptions are involved?             |
| 5   | **Classical pipeline**     | Processing stages before deep learning               |
| 6   | **Classical algorithms**   | Canonical methods and equations                      |
| 7   | **Deep pipeline**          | Learned representation and inference                 |
| 8   | **Historical progression** | Especially 2016 onward                               |
| 9   | **Data terms**             | What measures agreement with observations or labels? |
| 10  | **Regularizers**           | What priors resolve ambiguity?                       |
| 11  | **Optimization**           | How is the solution computed?                        |
| 12  | **Engineering tricks**     | What makes the method work in practice?              |
| 13  | **Post-processing**        | Which constraints are applied after inference?       |
| 14  | **Metrics and datasets**   | How is performance evaluated?                        |
| 15  | **Failure modes**          | Where and why does it fail?                          |
| 16  | **Key papers**             | Foundational, 2016–2018, and later updates           |
| 17  | **Worked example**         | One complete numerical or visual pipeline            |
| 18  | **Takeaways**              | The five points to remember                          |

#### Structure for a larger written study {#cv-a-29-module-curriculum--volumes}

If the material is written up as a document rather than taught as modules, four volumes work better than an architecture-by-architecture treatment:

1. **Foundations** — image formation, cameras, sampling, filtering, optimization, probability, robust estimation, geometry, photometry.
2. **Task atlas** — each task as input/output, assumptions, classical pipeline, deep pipeline, losses, tricks, metrics, datasets, failure modes.
3. **Historical transition** — how 2016–2018 methods inherited classical ideas (pyramids, cost volumes, warping, robust losses, proposals, anchors, graph optimization) and made them differentiable or learnable.
4. **Modern unification** — self-supervision, foundation models, differentiable rendering, multimodal systems, and how photometric and geometric constraints remain relevant.

This site is organised along exactly those lines: [taxonomy](#cv-the-master-task-taxonomy) and [pipeline](#cv-the-shared-pipeline-and-the-objective-template) for volume 1, the [task atlas](#cv-the-atlas-29-modules) for volume 2, the [era pages](#cv-depth-detection-and-the-first-believable-images) for volume 3, and the [synthesis](#cv-six-mechanisms-one-ladder-and-what-the-numbers-hid) for volume 4.
