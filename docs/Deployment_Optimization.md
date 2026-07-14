Problem
--------
Initial Docker image exceeded 9 GB due to GPU-enabled ML dependencies.

Root Cause
----------
CUDA-enabled PyTorch dependency resolution.

Solution
--------
CPU-only PyTorch installation.
Curated production dependencies.

Result
------
Image Size:
9.81 GB → 3.22 GB

Content Size:
3.26 GB → 703 MB

Status
------
Validated successfully in local Docker before Oracle deployment.