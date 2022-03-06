## Kubernetes Objects  

Kubernetes Objects are persistent entities in the cluster and are used to represent the state of the cluster.  

Some of the Kubernetes Objects:
1. Pods
2. Namespaces
3. ReplicationController (Manages Pods)
4. DeploymentController (Manages Pods)
5. StatefulSets
6. DaemonSets
7. Services
8. ConfigMaps
9. Volumes

### Pods  

<p align="center">
  <img src="../images/k8s_pods.png" width="500">
</p>

Every microservice is deployed as a single container.  
A 'Pod' represents a single instance of a running process in your cluster.  

So what's the relation between these two?  
Pods can contain one or more containers. When a Pod runs multiple containers, the containers are managed as a single entity and share the Pod's resources. A Pod is meant to run a single instance of your application on your cluster. When a pod contains multiple containers, all the containers run on one node, they can not be distibuted across worker nodes.  

An example of a multi-container pod can be:  
One container is responsible for the front-end of a website, while another is responsible for collecting logs and sending it to a server.  

NOTE: One thing to keep in mind is that the IP address is allocated to each pod, not for each container in the pod.

### Namespaces 

Namespaces provides a mechanism for isolating groups of resources within a single cluster. Names of resources need to be unique within a namespace, but not across namespaces; which means, a combination of an object name and a namespace, each object gets an unique identity across the cluster.

By default, a Kubernetes cluster is created with the following three namespaces:
1. default: By default all the resource created in Kubernetes cluster are created in the default namespace.
2. kube-public: Namespace for resources that are publicly readable by all users. This namespace is generally reserved for cluster usage.
3. kube-system: It is the Namespace for objects created by Kubernetes systems/control plane.  

Namespaces are intended for use in environments with many users spread across multiple teams, or projects.

### Replication Controller  

A ReplicationController ensures that a specified number of pod replicas are running at any one time.

If there are too many pods, the ReplicationController terminates the extra pods. If there are too few, the ReplicationController starts more pods. Unlike manually created pods, the pods maintained by a ReplicationController are automatically replaced if they fail, are deleted, or are terminated. 

### Deployment Controller

The Deployment controller and Job controller are examples of controllers that come as part of Kubernetes itself ("built-in" controllers).

You describe a desired state in a Deployment, and the Deployment Controller changes the actual state to the desired state at a controlled rate. 

### Stateful Sets

StatefulSet is a Kubernetes resource used to manage stateful applications. It manages the deployment and scaling of a set of Pods, and provides guarantee about the ordering and uniqueness of these Pods.

### Daemon Sets

A DaemonSet is a controller that ensures that the pod runs on all the nodes of the cluster. If a node is added/removed from a cluster, DaemonSet automatically adds/deletes the pod. A typical use case for this is monitoring/logging pods that need to run on all the nodes. 

### Services

A Service is a logical collection of pods in a Kubernetes cluster and is used to expose an application. Since pods are regularly created and destroyed, with their IP addresses changing constantly, it will be close to impossible for the application frontend to discover these deployed pods and connect to them. Services keep track of these changes and expose a single IP to the end user. 

There are four types of Kubernetes services — ClusterIP, NodePort, LoadBalancer and ExternalName. 

1. ClusterIP  
  a. ClusterIP is the default and most common service type.  
  b. Kubernetes will assign a cluster-internal IP address to ClusterIP service. This makes the service only reachable within the cluster.  
  c. You cannot make requests to service (pods) from outside the cluster.  

2. NodePort  
  a. NodePort service is an extension of ClusterIP service. It exposes the service outside of the cluster by adding a cluster-wide port on top of ClusterIP.  
  b. External traffic has access to fixed port on each Node. It means any request to your cluster on that port gets forwarded to the service.  
  c. You can contact the NodePort Service, from outside the cluster, by requesting `<NodeIP>:<NodePort>`

3. LoadBalancer  
  a. LoadBalancer service is an extension of NodePort service.    
  b. It integrates NodePort with cloud-based load balancers and exposes the service externally using a cloud provider’s load balancer.  
  c. Each cloud provider (AWS, Azure, GCP, etc) has its own native load balancer implementation. The cloud provider will create a load balancer, which then automatically routes requests to your Kubernetes Service.

4. ExternalName  
  These services are used to have a cluster internal service name that forwards traffic to another (internal or external) DNS name. In practice what an ExternalName does is create a CNAME record that maps the external DNS name to a cluster-local name. It does not expose anything out of your cluster. 

### ConfigMaps

<p align="center">
  <img src="../images/configmap.gif" width="300">
</p>

In Kubernetes, ConfigMaps are used to store your application's configuration settings (connection strings, public credentials, hostnames, etc.) as a dictionary. This dictionary consists of key-value pairs of strings which are then provided to the containers. We use this approach as we want to keep application code separate from configuration. 

As seen in the animation above, we can use different configuration settings for our containers based on our needs by using ConfigMaps. 

### Volumes

A Kubernetes volume is a directory that contains data accessible to containers in a given Pod in the orchestration and scheduling platform. Volumes provide a plug-in mechanism to connect ephemeral containers with persistent data stores elsewhere. Kubernetes volumes persist until the Pod is deleted. 

No matter what Node the Pod runs on, Kubernetes will mount the Pod's volumes to it, allowing containers to move across infrastructure without losing access to the externally hosted data that they require for the workload.