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
