# Path to GitOps

## 1. What is GitOps?
### GitOps Principles
In October 2021, the GitOps Working Group released the OpenGitOps Principles, a set of principles for managing software systems.

#### Declarative
A system managed by GitOps must have its desired state expressed declaratively.

A system in this context is defined as one or more runtime environments consisting of resources under management, the management agents within each runtime, and the policies for controlling access and management of repositories, deployments, and runtimes.

Desire state means that you represent the way you want the system to work in an “end state”, which will be the final state achieved by changes made by the GitOps environment.

The desired state must be declarative. The state of a system is stored as a set of declarations without procedures for how that state will be achieved.

#### Versioned and Immutable
>Desired state is stored in a way that enforces immutability and versioning and that retains a complete version history.

The canonical example of the “versioned and immutable” principle is Git, which is why it’s the first element in the term GitOps. Git’s store is versioned and immutable because each change is tracked in a new version without altering previous versions. So you can revert back to a previous version while preserving an audit of all the changes that have been made.

#### Pulled Automatically
>Software agents automatically pull the desired state declarations from the source.

GitOps software agents check the desired state by pulling declarations from the state store at regular intervals, which means polling as well as pulling. in GitOps, there is no webhook that needs to be hit. Instead, there is a reconciliation loop. This design leads to the final principle.

#### Continuously Reconciled
>Software agents continuously observe actual system state and attempt to apply the desired state.

This principle directly mirrors the functions of the Kubernetes controllers, but GitOps applies it to a whole application or infrastructure stack instead of just one object. If there is a difference between the desired and running state, they are reconciled by changing the running state.

### GitOps and CI/CD
CI/CD is one of the prominent practices in the DevOps movement. The main concepts attributed to CI/CD are continuous integration, continuous delivery, and continuous deployment.

#### Traditional CI/CD Workflows
Continuous integration builds and tests new code changes and merges them into a shared repository on a regular basis.

Continuous delivery refers to automating release of changes to the dev/staging and pre-production environments. The changes then get deployed to production. It also automates the manual steps that slow down application delivery.

The purpose of continuous delivery is to deploy new code with minimal effort. Continuous deployment takes continuous delivery one step further, deploying the changes into actual production.

#### Operations via Pull Request
The idea of gitOps is to apply the same workflow to any change that goes into infrastructure and applications. Changes are proposed by issuing a pull request to the respective Git repository. After reviews and approval, the change gets merged into the repository which is then applied to the target infrastructure.

### Summary
In this chapter, we introduced GitOps as a practice, took a quick look at its history, and showed its relationship to the DevOps movement and CI/CD. We then explored how Kubernetes was the catalyst for refining how we operate our infrastructure and application deployments today. We also took a look at the GitOps principles as defined by the OpenGitOps Sandbox project.

## 2. Tools of the Trade
In this chapter, we will go over various tools used most often to manage GitOps workflows. Many of the tools were developed to fill a gap in earlier tools used in Infrastructure as code (IaC).

### Infrastructure as Code
Infrastructure as code is a method for managing, configuring, and updating the entire software infrastructure at a datacenter using configuration files that are both machine-readable and human-readable. The configuration files are machine-readable in structured format (usually YAML) so that software tools can read them to automate changes. They are also human-readable so that administrators can maintain them easily and immediately understand what they define.

#### History of Infrastructure as Code
The advantages of Infrastructure as code are cost and speed. The concept “do more with less” applies here. With IaC, you no longer need to hire at a “person per node” ratio. Removing the need for manual configuration frees up administrators to do other things.

IaC gives you vastly more speed because you can manage thousands of nodes all at once. You also reduce the risk that could be introduced by human error, because all the nodes get the same configuration.

#### Challenges of Infrastructure as Code
The idea behind IaC is to make it mostly event-driven. In other words, changes to your platform should adapt to changes automatically instead of requiring human intervention.

Suppose the commands try to update a local database on a system where change had occurred, or after an administrator had deleted the whole database. In those scenarios, the command will fail. So, the mutability of servers and virtual machines is the biggest challenge to IaC. This is where containers provide an advantage.

#### Containers Change the Game
Containers represent a totally different view of continuity in your infrastructure. You make software changes not by updating an existing configuration, but by deleting the whole virtual system and creating a new container. So in the example of updating a database in the previous section, Kubernetes heals the system simply by starting a new set of containers. This is the advantage that Kubernetes gives you.

### Argo CD
Argo CD was written with GitOps in mind, to deliver changes to a Kubernetes cluster at massive scale. It detects and prevents drift in your Kubernetes clusters by working with raw YAML stored in a Git repository and using the apply functionality in Kubernetes.

### Flux
Flux performs many of the same functions as Argo CD, but is different in a lot of ways. The main difference is that Flux uses the Helm Golang package. Flux doesn’t render the YAML, but instead deals with Helm directly.

### Open Cluster Management
Open Cluster Management (OCM) has its roots in IBM Multicloud Manager. The tool  goes beyond just applying YAML and detecting drift: it also manages the lifecycle of your Kubernete cluster. The idea behind OCM and Red Hat Advanced Cluster management is multicluster management from a single pane of glass. As with other GitOps tools, you can use these to keep your cluster in sync with a Git repository and detect and fix drift. But additionally, you can also manage the lifecycle of those clusters.

### Other GitOps Tools
#### PipeCD
PipeCD lets you manage and promote deployments from one environment to another.

#### Keptn
Keptn was designed to provide visibility into your environments. It aims to provide Service Level Objectives (SLOs) throughout the multistage deployment. Keptn is meant to automatically set up environments with gating based on metrics for your CI/CD workflows.

#### Pulumi Kubernetes Operator
The Pulumi Kubernetes Operator is particularly interesting because it broadens the Kubernetes idea of declarations to make them more appealing to developers. The Pulumi Kubernetes Operator lets developers write declarations in their chosen language: Golang, TypeScript, Python…

### Summary
In this chapter, we reviewed the origins of Infrastructure as code, along with its advantages and shortcomings. We also saw how Kubernetes changed the game for Infrastructure as code. We went through popular GitOps tools, what they have to offer, and what choices you have when looking for a GitOps controller.
