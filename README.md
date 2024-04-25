> \[!CAUTION\]
> **THIS PROJECT IS UNDER CONSTRUCTION (WIP). DO NOT TAKE IT SERIOUSLY YET!**

---

<div align="center">

<!-- PROJECT LOGO -->
# 📝 POC: Kubernetes Custom Admission Control for Deployments


<!-- TECNOLOGIES -->
![Kubernetes Badge](https://img.shields.io/badge/Kubernetes-326CE5?logo=kubernetes&logoColor=fff&style=flat)
![Docker Badge](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff&style=flat)
![FastAPI Badge](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=fff&style=flat)


This repository contains a well detailed PoC about an specific use case: enabling custom validation and mutating webhook for your Kubernetes deployments based on a set of rules.
There are many solutions out there like OPA Gatekeeper or Kyverno specialized for this.
However, understanding how could you configure your custom server for validation or mutating webhook can provide you even farther flexibility if needed.

[Report Bug](https://github.com/paf-triarii/kubernetes-deployment-validation-and-mutating--webhook/issues) · [Request Feature](https://github.com/paf-triarii/kubernetes-deployment-validation-and-mutating--webhook/issues)
</div>

<!-- TABLE OF CONTENTS -->


## 📚 Table of contents

- [📝 POC: Kubernetes Custom Admission Control for Deployments](#-poc-kubernetes-custom-admission-control-for-deployments)
  - [📚 Table of contents](#-table-of-contents)
  - [💡 Structure](#-structure)
  - [🚀 Installation and Execution](#-installation-and-execution)
    - [🔨 Prerequisites](#-prerequisites)
    - [🗜️ Installation](#️-installation)
    - [💼 Usage](#-usage)
  - [📍 Roadmap](#-roadmap)
  - [📎 Contributing](#-contributing)
  - [📃 License](#-license)
  - [👥 Contact](#-contact)

<!--te-->

<!-- PROJECT DETAILS -->
## 💡 Structure


## 🚀 Installation and Execution

### 🔨 Prerequisites

- Docker
- Python 3.10+
- Kubernet

[🔝 Back to top](#-poc-kubernetes-custom-admission-control-for-deployments)

### 🗜️ Installation

1. Build required docker images and upload to your cluster registry. Other option is to use my already built images published in Docker Hub (uvicorn: , caddy:)

```bash
docker build . -f docker/Dockerfile.service -t uvicorn:1.0
```

[🔝 Back to top](#-poc-kubernetes-custom-admission-control-for-deployments)

<!-- USAGE EXAMPLES -->
### 💼 Usage


_For more examples, please refer to the [Documentation](https://example.com)_

[🔝 Back to top](#-poc-kubernetes-custom-admission-control-for-deployments)

<!-- GETTING STARTED -->

<!-- ROADMAP -->
## 📍 Roadmap

- [x] Create validation/mutating server with FaskAPI.
- [x] Prepare docker and kubernetes deployment (two flavors).

See the [open issues](https://github.com/paf-triarii/kubernetes-deployment-validation-and-mutating--webhook/issues) for a full list of proposed features (and known issues).

[🔝 Back to top](#-poc-kubernetes-custom-admission-control-for-deployments)

<!-- CONTRIBUTING -->
## 📎 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated** :chart:.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch

   ```sh
   git checkout -b feature/AmazingFeature
   ```

3. Commit your Changes

   ```sh
   git commit -m 'Add some AmazingFeature
   ```

4. Push to the Branch

   ```sh
   git push origin feature/AmazingFeature
   ```

5. Open a Pull Request

[🔝 Back to top](#-poc-kubernetes-custom-admission-control-for-deployments)

<!-- LICENSE -->
## 📃 License

Distributed under the [`APACHE 2.0`](./LICENSE) License.

[🔝 Back to top](#-poc-kubernetes-custom-admission-control-for-deployments)

<!-- CONTACT -->
## 👥 Contact

<div align="center">

---

**`PAF TRIARII (pedroarias1015@gmail.com) a member of Code Triarii`**

---

[![X](https://img.shields.io/badge/X-%23000000.svg?style=for-the-badge&logo=X&logoColor=white)](https://twitter.com/codetriariism)
[![TikTok](https://img.shields.io/badge/TikTok-%23000000.svg?style=for-the-badge&logo=TikTok&logoColor=white)](https://www.tiktok.com/@codetriariism)
[![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@codetriariism)
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/@CodeTriariiSM)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://www.instagram.com/codetriariismig/)

</div>

As we always state, our main purpose is keep learning, contributing to the community and finding ways to collaborate in interesting initiatives.
Do not hesitate to contact us at `codetriariism@gmail.com`

If you are interested in our content creation, also check our social media accounts. We have all sorts of training resources, blogs, hackathons, write-ups and more!
Do not skip it, you will like it :smirk: :smirk: :smirk: :+1:

Don't forget to give the project a star if you liked it! Thanks again! :star2: :yellow_heart:

[🔝 Back to top](#-poc-kubernetes-custom-admission-control-for-deployments)
