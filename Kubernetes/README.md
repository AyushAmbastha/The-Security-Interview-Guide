# Kubernetes

Kubernetes is an open-source container orchestration platform. A container orchestrator is essentially an administrator in charge of operating a fleet of containerized applications. It keeps track of your container applications that are deployed into the cloud. It restarts orphaned containers, shuts down containers when they're not being used, and automatically provisions resources like memory, storage, and CPU when necessary.

## Why is it needed?

For organizations that operate at a massive scale, a single Linux container instance isn’t enough to satisfy all of their applications’ needs. It’s not uncommon for sufficiently complex applications, such as ones that communicate through microservices, to require multiple Linux containers that communicate with each other. That architecture introduces a new scaling problem: how do you manage all those individual containers? Developers will still need to take care of scheduling the deployment of containers to specific machines, managing the networking between them, growing the resources allocated under heavy load, and much more.
