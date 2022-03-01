## Kubernetes Objects  

Kubernetes Objects are persistent entities in the cluster. These objects are used to represent the state of the cluster.  

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