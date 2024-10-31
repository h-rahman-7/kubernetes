# Kubernetes - k8s 

- Is the leading container orchestration tool
- Designed as a loosely coupled collection of components centered around deploying, maintaining and scaling workloads
- Vendor-neutral
	- Runs on all cloud providers
- Backed by huge community

**What do K8s do?**
- Service discovery and load balancing
- Storage Orchestration
	- Local or Cloud based
- Automated rollouts and rollbacks
- Self-healing
- Secret and configuration management
- Use the same API across on-prem and cloud
**What K8s cannot do**
- Does not deploy source code
- Does not build your application
- Does not provide application-level services
	- Message buses ,databases, caches etc

**K8s Architecture Image**

![alt text](./images/k8sArchitecture.png)

**Composed of**
- Master Node also known as control plane
	- Runs Kubernetes services and controllers
- Worker Nodes
	- Runs the containers that you deploy 

**Example**
- Container runs in a pod
	- Pod runs in a node
		- All nodes form a cluster

![alt text](./images/clusterToPod.png)

## Running Kubernetes Locally

**Local K8s**
- Requires Virtualisation
	- Docker Desktop
	- MicoK8s
	- Minikube
- Runs over Docker Desktop
	- Kind (Kubernetes in Docker)
- Limited to 1 Node
	- Docker Desktop
- Multiple Nodes
	- MicroK8s
	- Minikube
	- Kind
- Windows
	- Docker Desktop is currently only way to run both Linux and windows containers
		- Runs on Hyper-V or WSL 2
	- If Hyper-V is enabled, you can't run another hypervisor at the same time
	- You can install Minikube on Hyper-V or Virtual Box

**Kubernetes Local** - Using CMD or PowerShell

-  This command lets you check if Kubernetes is running: `kubectl cluster-info dump

**Kubernetes CLI**
- K8s API:

![alt text](./images/k8sAPI.png)

- **kubectl** - The main command for K8s
	- Communicates with the api server
	- Configuration stored locally under:
		- ${HOME}/.kube/config
		- C:\Users\{USER}\.kube\config
- **K8s Context**
	- A context is a group of access parameters to a K8s cluster
	- Containers a Kubernetes cluster, a user and a namespace
	- The current context is the cluster that is currently the default for kubectl
		- All kubectl commands run against that cluster

![alt text](./images/kubectl-cheatsheet.png)

- Kube tools
	- kubectl - Useful for fast context usage, install using: `choco install kubectx-ps` if you have 'Choco' installed
- Rename a context: `kubectl config rename-context [oldname] [newname]`

**Declarative vs Imperative**
- Imperative:
	- Using kubectl commands, issue a series of commands to create resources
	- Great for learning, testing and troubleshooting
	- It's like code
- Declarative:
	- Using kubectl and YAML manifests defining the resources you need
	- Reproducible and repeatable
	- can be saved in source control
	- Its like data that can be parsed and modified

**Imperative**:

![alt text](./images/Imperative.png)

**Declarative**:

![alt text](./images/Declarative.png)

## **YAML**
 - Root level required properties
	 - apiVersion
		 - Api version of the object
	- kind
		- type of object
	- metadata.name
		- unique name for the object
	- metadata.namespace
		- scoped environment name (will default to current)
	- spec
		- object specifications or desired state
- Create an object using YAML
	  kubectl create -f [YAML file]
  
![alt text](./images/PodDefinition.png)

**Note:**
- We do NOT need to type all the YAML manually, we can get the syntax from kubernetes.io/docs and search and copy
- We can create using manifests (templates) in VS Code, in new YAML file, hitting ctrl+space and select the template you need
- Kubernetes CLI to generate manifests: `--dry-run=cleient -o yaml`

## Deploying an Imperative and Declarative container

- For **Imperative**:
	- `kubectl create deployment mynginx1 --image=nginx` 
	- we can check if its created using: `kubectl get  deploy`
- For **Declarative**
	- `kubectl create -f deploy-example.yaml` - Must have the 'deploy-example.yaml' file exist and must contain some data
- **Useful commands**
	- `kubectl get  deploy` - Listing all the running deployments
	- `kubectl delete deploy example-deployment-name ` - after running the first command, you can delete using the 'name' 

## Namespaces
- Allow to group resources
	- Example: Dev,Test,Prod
- K8s create a default workspace
- Objects in one namespace can access objects in a different one
	- Example: objectname.**prod**.scv.cluster.local
- Deleting a namespace will delete all its child objects

- Define a namespace
- Specify the namespace when defining objects

![alt text](./images/pod-namespace.png)

- You can limit resources using the resource quota object

![alt text](./images/resource-quota.png)

**Kubectl - Namespace sheet commands**

![alt text](./images/Namespace-cheatsheet.png)


## Kubernetes Storage

- **Why Persistent Storage?**
  - Pods are **ephemeral** – created and deleted often, so not ideal for storing data!
  - Persistent storage provides **data reliability** beyond the pod lifecycle.
  - Essential for **stateful applications** like:
    - Databases
    - Message queues
    - Apps that need to remember past interactions

- **Persistent Volumes (PV)**
  - Acts as **dedicated storage** in Kubernetes (like a shared hard drive).
  - **Created by admins** and available for applications to use.
  - Think of it as **pre-configured storage** ready to go when needed.

- **Persistent Volume Claim (PVC)**
  - PVC is how an app requests storage – **“I need space”**.
  - When a PVC matches an available PV, it gets **bound** to that volume.
  - Similar to asking IT for shared storage; once approved, you can use it freely.


## ConfigMaps

- **Purpose**: Store non-confidential data needed by applications in Kubernetes.
- **Configuration Management**: Provides a way to manage and supply configuration settings to pods without embedding values directly in application code.
- **Flexibility**: Allows **dynamic configuration changes** without needing to rebuild the application.
- **Usage**:
  - Used for items like environment variables, config files, command-line arguments, etc.
  - Ideal for things like API URLs, app modes (development, production), and other non-sensitive settings.
- **Consistency**: Ensures that **pods receive correct configurations** every time they start, making deployments more reliable.

Creating a Config map:

- $ kctl create configmap my-config --from-literal=APP_COLOUR=blue --from-literal=APP_MODE=production

## Secrets

- Store sensitive data securely in Kubernetes by encoding it as Base64.
- Create a secret with the command:
  ```
  kubectl create secret generic my-secret --from-literal=username=myuser --from-literal=password=mypassword
  ```
To retrieve and view secrets in YAML format:

`kubectl get secrets -o yaml`

The output will include encoded values like:
```
data:
  password: bXlwYXNzd29yZA==
  username: bXl1c2Vy
```
Decode a secret (e.g., password) with:

`echo "bXlwYXNzd29yZA==" | base64 -d` <br>
This returns the original plaintext values.

## Kubernetes Networking

Pod Networking: All pods can communicate with each other and with nodes without Network Address Translation (NAT).

Cluster-IP Consistency: The IP a pod sees for itself is the same IP that others use to reach it.

For example, create two pods, apache and nginx:

```
kubectl run apache --image=httpd
kubectl run nginx --image=nginx
```
Verify they’re running:

`kubectl get pods`

```
NAME    READY   STATUS    RESTARTS   AGE
apache  1/1     Running   0          10s
nginx   1/1     Running   0          20s
```
Get pod IP addresses:


`kubectl get pods -o wide`

```
Copy code
NAME    READY   STATUS    RESTARTS   AGE   IP          NODE
apache  1/1     Running   0          20s   10.244.0.9  minikube
nginx   1/1     Running   0          30s   10.244.0.8  minikube
```
Access nginx pod terminal:
```
kubectl exec nginx -it -- sh
```
Inside nginx, use curl to reach the apache pod:

`curl 10.244.0.9`

Expected output:

`<html><body><h1>It works!</h1></body></html>` 

This confirms inter-pod communication without explicit network configuration.


## Service Discovery and DNS

Service Discovery: Kubernetes Services abstract and manage access to pods.

DNS: Enables automatic name resolution for services, facilitating intra-cluster connectivity.

Key Concepts:
Service Types: ClusterIP, NodePort, LoadBalancer, etc.
DNS Lab: Test DNS with a network troubleshooting image:

`kubectl run tmp-shell --rm -i --tty --image=moabukar/netshoot`

## Network Policies

Network policies are sets of rules that govern communication between pods, defining which pods can interact with each other and with external resources. Without these policies, all pods can communicate freely—this isn’t ideal in production, where tighter controls are necessary.

For instance, network policies can restrict frontend pods to only communicate with backend pods, while backend pods connect solely with a database. This ensures structured and secure interactions between services.

### Key Concepts
- **Pod Communication Control**: Defines how groups of pods communicate with each other and external network endpoints.
- **Ingress**: Controls incoming traffic to pods.
- **Egress**: Controls outgoing traffic from pods.

### Ingress Controller
- Manages external access to services within the cluster, typically over HTTP/HTTPS.
- Routes external requests to the appropriate service based on predefined rules.

### Egress Controller
- Controls outbound traffic from the pods to external services.
- Often used to enforce network security policies and restrict external access.

